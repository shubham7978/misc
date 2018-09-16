<?php 
$ip = $_GET['ip'];
$port = "ifOperStatus.".$_GET['port'];
$portadmin = "ifAdminStatus.".$_GET['port'];
$portnum = "ifDescr.".$_GET['port'];
$portname = "ifAlias.".$_GET['port'];
$comm = "mo34";
$test = snmpget ($ip, $comm, $portadmin);
$num = substr(snmpget ($ip, $comm, $portnum),7);
$name = trim(substr(snmpget ($ip, $comm, $portname),7));

if($test=="INTEGER: down(2)")
{
echo "WARNING - Interface $num - $name is Adminstrative Down";
exit(1);
}

else
{
$test1 = snmpget ($ip, $comm, $port);
if($test1=="INTEGER: up(1)")
{
echo "Ok - Interface $num - $name is Up";
exit(0);
}
else
{
if($name=="")
{
echo "WARNING - Interface $num has no description";
exit(1);
}

else
{
echo "Critical - Interface $num - $name is Down";
exit(2);
}
}

}

?>
