import sys,os,subprocess,glob,shutil
from optparse import OptionParser

class CondorJob:
    def __init__(self, stdout, schedd, why):
        self.stdout = stdout
        self.name = "_".join(stdout.split('_')[:-1])
        self.num = stdout.split('_')[-1]+".0"
        self.schedd = schedd
        self.why = why

def makeJobQuery(options, prop, schedd=""):
    #make query
    cmd = "condor_q "
    if len(schedd)>0: cmd += "-name "+schedd+" "
    cmd += options.user+" "
    if options.held: cmd += "-hold "
    if options.running: cmd += "-run "
    cmd += "-long "
    cmd += "| grep \""+prop+"\" "
    if len(options.grep)>0: cmd += "| grep \""+options.grep+"\" "
    if len(options.vgrep)>0: cmd += "| grep -v \""+options.vgrep+"\" "
    cmd += "| sort"
    return cmd
        
def getJobs(options, schedd=""):
    cmd = makeJobQuery(options,"stdout",schedd)

    #get info for selected jobs
    joblist = filter(None,subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].split('\n'))
    joblist = [j.split(' ')[2].replace("\"","").replace(".stdout","") for j in joblist]
    jobs = []
    if len(schedd)>0 and len(joblist)>0: print schedd
    for j in joblist:
        jtmp = CondorJob(j,schedd,"")
        if options.why:
            cmdw = "condor_q "+jtmp.num+" -long "+("-name "+jtmp.schedd if len(jtmp.schedd)>0 else "")+' | grep "^HoldReason = "'
            holdreason = filter(None,subprocess.Popen(cmdw, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].split('\n'))
            if len(holdreason)>0: jtmp = CondorJob(j,schedd,holdreason[0].replace("HoldReason = ",""))
        jobs.append(jtmp)
    return jobs
        
def printJobs(jobs, stdout=False):
    if len(jobs)==0: return
    
    if stdout:
        print "\n".join([j.stdout+(" : "+j.why if len(j.why)>0 else "") for j in jobs])
    else:
        print "\n".join([j.name+(" : "+j.why if len(j.why)>0 else "") for j in jobs])

parser = OptionParser(add_help_option=False)
parser.add_option("-u", "--user", dest="user", default="mbhat", help="view jobs from this user (submitter) (default = %default)")
parser.add_option("-a", "--all", dest="all", default=False, action="store_true", help="view jobs from all schedulers (default = %default)")
parser.add_option("-h", "--held", dest="held", default=False, action="store_true", help="view only held jobs (default = %default)")
parser.add_option("-r", "--running", dest="running", default=False, action="store_true", help="view only running jobs (default = %default)")
parser.add_option("-g", "--grep", dest="grep", default="", help="view jobs with [string] in the job name (default = %default)")
parser.add_option("-v", "--vgrep", dest="vgrep", default="", help="view jobs without [string] in the job name (default = %default)")
parser.add_option("-o", "--stdout", dest="stdout", default=True, action="store_true", help="print stdout filenames instead of job names (default = %default)")
parser.add_option("-x", "--xrootd", dest="xrootd", default="", help="edit the xrootd redirector of the job (default = %default)")
parser.add_option("-e", "--edit", dest="edit", default="", help="edit the ClassAds of the job (default = %default)")
parser.add_option("-s", "--resubmit", dest="resubmit", default=True, action="store_true", help="resubmit the selected jobs (default = %default)")
parser.add_option("-k", "--kill", dest="kill", default=False, action="store_true", help="remove the selected jobs (default = %default)")
parser.add_option("-d", "--dir", dest="dir", default="/uscms_data/d3/mbhat/testVID/CMSSW_8_0_25/src/LeptoQuarkTreeMaker/Production/test/myProduction", help="directory for stdout files (used for backup when resubmitting) (default = %default)")
parser.add_option("-w", "--why", dest="why", default=False, action="store_true", help="show why a job was held (default = %default)")
parser.add_option("--help", dest="help", action="store_true", default=False, help='show this help message')
(options, args) = parser.parse_args()

if options.help:
   parser.print_help()
   sys.exit()

#check for exclusive options
if options.held and options.running:
    parser.error("Can't use -h and -r together, pick one!")
if options.why and not options.held:
    parser.error("Can only use -w with -h.")
if options.resubmit and options.kill:
    parser.error("Can't use -s and -k together, pick one!")
if options.all and (options.kill or options.resubmit):
    parser.error("Can't use -s or -k with -a.")
if len(options.xrootd)>0 and options.xrootd[0:7] != "root://":
    parser.error("Improper xrootd address: "+options.xrootd)
if len(options.xrootd)>0 and options.xrootd[-1]!='/':
    options.xrootd += '/'
    
jobs = []
if options.all:
    #loop over schedulers    
    for sch in ["cmslpc"+str(schnum)+".fnal.gov" for schnum in xrange(23,43)]:
        jobs_tmp = getJobs(options,sch)
        printJobs(jobs_tmp,options.stdout)
        jobs.extend(jobs_tmp)
else:
    jobs = getJobs(options)
    printJobs(jobs,options.stdout)

#resubmit jobs
if options.resubmit:
    #create backup dir if desired
    backup_dir = ""
    tmp_dir = ""
    if len(options.dir)>0:
        backup_dir = options.dir+"/backup"
        if not os.path.isdir(backup_dir):
            os.mkdir(backup_dir)
        tmp_dir = options.dir+"/tmp"
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
    for j in jobs:
        logfile = options.dir+"/"+j.stdout+".stdout"
        #hold running jobs first (in case hung)
        if options.running:
            if len(options.dir)>0:
                logfile = tmp_dir+"/"+j.stdout+".stdout"
                #generate a backup log from condor_tail
                cmdt = "condor_tail -maxbytes 10000000 "+j.num
                with open(logfile,'w') as logf:
                    subprocess.Popen(cmdt, shell=True, stdout=logf, stderr=subprocess.PIPE).communicate()
            cmdh = "condor_hold "+j.num
            subprocess.Popen(cmdh, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        #backup log
        if len(options.dir)>0:
            prev_logs = glob.glob(backup_dir+"/"+j.stdout+"_*")
            num_logs = 0
            #increment log number if job has been resubmitted before
            if len(prev_logs)>0:
                num_logs = max([int(log.split("_")[-1].replace(".stdout","")) for log in prev_logs])+1
            #copy logfile
            shutil.copy2(logfile,backup_dir+"/"+j.stdout+"_"+str(num_logs)+".stdout")
        #reset counts to avoid removal
        cmd3 = "condor_qedit "+j.num+" JobRunCount 0 NumJobStarts 0 NumShadowStarts 0"
        subprocess.Popen(cmd3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        #any other classad edits
        if len(options.edit)>0:
            cmd4 = "condor_qedit "+j.num+" "+options.edit
            subprocess.Popen(cmd4, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        #edit redirector
        if len(options.xrootd)>0:
            cmd1 = "condor_q -long "+j.num+" | grep \"Args\""
            args = filter(None,subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].split('\n'))
            args = args[0].split(' ')[2:]
            args = [a.replace("\"","").rstrip() for a in args]
            if "root:" not in args[-1]: args.append(options.xrootd)
            else: args[-1] = options.xrootd
            cmd2 = "condor_qedit "+j.num+" Args '\""+" ".join(args[:])+"\"'"
            subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        subprocess.Popen(["condor_release",j.num], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#or remove jobs
elif options.kill:
    for j in jobs:
        subprocess.Popen(["condor_rm",j.num], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
