from pysnmp.hlapi import *

result = getCmd(SnmpEngine(),
	CommunityData("public", mpModel=0),
	UdpTransportTarget(("10.31.70.209", "161")),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

for request in result:
	for var in request[3]:
		print(var)

result2 = nextCmd (SnmpEngine(),
	CommunityData("public", mpModel=0),
	UdpTransportTarget(("10.31.70.209", "161")),
	ContextData(),
ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
	lexicographicMode=False)
for request in result2:
	for var in request[3]:
		print(var)
