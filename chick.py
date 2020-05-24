import socket
import time

def ip2long(ip):
	ip_long = 0
	for index,value in enumerate(reversed([int(x) for x in ip.split(".")])):
		ip_long += value<<(8*index)
	return ip_long

def long2ip(ip_long):
	ip = []
	ip.append((ip_long & 0xffffffff)>>24)
	ip.append((ip_long & 0x00ffffff)>>16)
	ip.append((ip_long & 0x0000ffff)>>8)
	ip.append((ip_long & 0x000000ff))
	return ".".join(map(str,ip))

def genip(seg):
	ip, mask = seg.split("/")
	ip_long = ip2long(ip)
	mask_long = int(str("1"*int(mask))+str("0"*(32-int(mask))),base = 2)
	return list(map(long2ip,range(mask_long&ip_long,ip_long+(mask_long^4294967295))))

if __name__ == "__main__":
	#60.205.128.0/17
	#60.205.0.0/17
	#8.209.16.0/20
	#8.209.10.0/23
	#101.132.0.0/15
	#101.132.0.0/16
	#223.7.0.0/16
	#233.7.6.0/24
	#59.110.128.0/17
	#59.110.0.0/16
	#182.92.0.0/17
	#182.92.0.0/16
	open("gen.txt","w")
	for i in genip("182.92.0.0/17"):
		open("gen.txt","a").write(i+"\n")
	for i in genip("182.92.0.0/16"):
		open("gen.txt","a").write(i+"\n")
