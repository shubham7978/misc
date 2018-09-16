from pysnmp.hlapi import *
import sys,subprocess

def snmpget(host,com,port):
 errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(com, mpModel=1),
           UdpTransportTarget((host, 161)),
           ContextData(),
           ObjectType(ObjectIdentity('IF-MIB', 'ifAdminStatus', port)),
           ObjectType(ObjectIdentity('IF-MIB', 'ifDescr', port)),
           ObjectType(ObjectIdentity('IF-MIB', 'ifOperStatus', port)),
           ObjectType(ObjectIdentity('IF-MIB','ifAlias',port)))

 ) 

 if errorIndication:
    #print(errorIndication)
    print("Warning - Interface has no description.")
    exit(1)

 elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
 else:
    a=[]

    for varBind in varBinds:
        
        a.append(' = '.join([x.prettyPrint() for x in varBind]))
    return a
#import sys,subprocess
def asnmpget(host,community,mib1,mib2,mib3,mib4):

 cmd= '/usr/bin/snmpget -c %s %s -v2c %s %s %s %s' % (community,  host, mib1,mib2,mib3,mib4)
 proc= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
 op=proc.communicate()[0]
 return (op[:-1:]).decode("utf-8")

number=sys.argv[1]
ip=sys.argv[2]
#ip='172.30.30.23'
#port = "ifOperStatus.%s" % number
#portadmin = "ifAdminStatus.%s" %number
#portnum = "ifDescr.%s" % number
#portname = "ifAlias.%s" % number
community="public"
#data=[]
data = snmpget(ip, community, number)

#print(data)
#data=dat.split(",")
#print(data)
test1=data[0]
num1=data[1]
num= num1[20::]
name1=str.strip(data[3])
name=name1[20::]
test=data[2]
if('down' in test1):
 print("Warning - Interface "+num+"- "+name+" is admininstrative down.")
 exit(1)
elif(('down' in test) and ('No Such Instance' not in name1) and name!='' ):
 print("Critical - Interface "+num+"- "+name+" is down.")
 exit(2)
elif ("up" in test):
 print("OK - Interface "+num+"- "+name+" is up.")
 exit(0)
else:
 print("Warning - Interface "+num+" has no description.")
 exit(1)

