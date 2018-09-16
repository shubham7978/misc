#!/usr/bin/python3
def snmpget(oid, *more_oids):
    
    from pysnmp.entity.rfc3413.oneliner import cmdgen
    
    SNMP_HOST='116.90.227.175'
    SNMP_PORT=161
    SNMP_COMMUNITY='c0m1'
    
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
result=snmpget( )
print(result)

