def snmpget(SNMP_HOST,SNMP_COMMUNITY,oid, *more_oids):

    from pysnmp.entity.rfc3413.oneliner import cmdgen

    #SNMP_HOST='116.90.227.175'
    SNMP_PORT=161
    #SNMP_COMMUNITY='c0m1'

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid,
        *more_oids
    )

    # Predefine our results list    
    results = []

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            for name, val in varBinds:
                results.append( val )

        if len(results) == 1:
            return results[0]
        else:
            return results
#result=snmpget( )
#print(result)
'''$ip = $_GET['ip'];
$port = "ifOperStatus.".$_GET['port'];
$portadmin = "ifAdminStatus.".$_GET['port'];
$portnum = "ifDescr.".$_GET['port'];
$portname = "ifAlias.".$_GET['port'];
//$portmkt = "ifName.".$_GET['port'];
'''
'''ip = "118.91.164.1"
port = "ifOperStatus.11"
portadmin = "ifAdminStatus.11"
portnum = "ifDescr.11"
portname = "ifAlias.11"
community="public"
test1 = snmpget(ip, community, portadmin)
#print(test)
#num = substr(snmpget ($ip, "public", $portnum),7);
num1=snmpget(ip,community,portnum)
num= num1[:7]
#name = trim(substr(snmpget ($ip, "public", $portname),7));
name=str.strip(snmpget(ip,community,portname)
#//echo $name."<br>";

if test1=="INTEGER: down(2)":
 print("warning - interface "+num+"- "+name+" is admininstrative down")
 exit(1)

test = snmpget(ip, community, port)
elif(test=="INTEGER: down(2)" && name!=''):
 print("Critical - interface "+num+"- "+name+" is down")
 exit(2)
elif(test==None):
 print("warning - interface "+num+" has no description")
 exit(1)
elif(test=="INTEGER: up(1)"):
 print("OK - interface "+num+"- "+name+" is admininstrative down")
 exit(0)
'''
