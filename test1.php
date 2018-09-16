<?php
$portname = "ifAlias."."2";
$portmkt = "ifName."."2";
$portnum = "ifDescr."."2";
echo "normal portnum - ".snmpget("172.20.16.35", "public", $portnum)."<br>";
$namemkt = trim(substr(snmpget ("172.20.16.35", "public", $portmkt),7));
$name = trim(substr(snmpget ("172.20.16.35", "public", $portname),7));
echo "<br>mktname - ".$namemkt."<br>";
echo "<br>normal name - ".$name."<br>";
?>
