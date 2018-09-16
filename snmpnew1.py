import sys,subprocess
def snmpget(host,community,mib1,mib2,mib3,mib4):
 
 cmd= '/usr/bin/snmpget -c %s %s -v2c %s %s %s %s' % (community,  host, mib1,mib2,mib3,mib4)
 proc= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
 op=proc.communicate()[0]
 return (op[:-1:]).decode("utf-8")

number=sys.argv[1] 
ip=sys.argv[2]
#ip='172.30.30.23'
port = "ifOperStatus.%s" % number
portadmin = "ifAdminStatus.%s" %number
portnum = "ifDescr.%s" % number
portname = "ifAlias.1.%s" % number
community="public"
dat = snmpget(ip, community, portadmin,portnum,port,portname)
data=dat.split("\n")
test1=data[0]
num1=data[1]
num= num1[-7::]
name1=str.strip(data[3])
name=name1[30::]
test=data[2]
if('INTEGER: down(2)' in test1): 
 print("Warning - Interface "+num+"- "+name+" is admininstrative down.")
 exit(1)
elif(('INTEGER: down(2)' in test) and ('No Such Instance' not in name1) and name!='' ):
 print("Critical - interface "+num+"- "+name+" is down.")
 exit(2)
elif ("INTEGER: up(1)" in test):
 print("OK - Interface "+num+"- "+name+" is up.")
 exit(0)
else:
 print("Warning - Interface "+num+" has no description.")
 exit(1)
