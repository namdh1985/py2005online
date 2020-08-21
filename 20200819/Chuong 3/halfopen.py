from scapy.all import * 
ip1 = IP(src="172.18.201.125", dst ="172.18.201.114" ) 
tcp1 = TCP(sport =1024, dport=80, flags="S", seq=12345) 
packet = ip1/tcp1 
p =sr1(packet, inter=1) 
p.show()
rs1 = TCP(sport =1024, dport=80, flags="R", seq=12347) 
packet1=ip1/rs1 
p1 = sr1(packet1) 
p1.show 