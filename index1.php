<?php 
$ip = $_GET['ip'];
$port = "ifOperStatus.".$_GET['port'];
$portadmin = "ifAdminStatus.".$_GET['port'];
$portnum = "ifDescr.".$_GET['port'];
$portname = "ifAlias.1.".$_GET['port'];

$test = snmpget ($ip, "public", $portadmin);
$num = substr(snmpget ($ip, "public", $portnum),7);
$name = trim(substr(snmpget ($ip, "public", $portname),7));
if($test=="INTEGER: down(2)")
{
echo "WARNING - Interface $num - $name is Adminstrative Down";
exit(1);
}

else
{
$test1 = snmpget ($ip, "public", $port);
if($test1=="INTEGER: up(1)")
{
echo "Ok - Interface $num - $name is Up";
exit(0);
}

else if($test1=="INTEGER: down(2)" && $name!="")
{
echo "Critical - Interface $num - $name is Down";
exit(2);
}

else if(isset($test1) && $name=="")
{
echo "WARNING - Interface $num has no description";
exit(1);
}
}

?>
