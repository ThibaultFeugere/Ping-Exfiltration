from scapy import all as scapy
import hashlib

def stopFilter(x):
    if '[hash]' in str(x[scapy.Raw]):
        return True
    else:
        return False

data = scapy.sniff(filter="icmp and dst 192.168.57.5", prn=lambda x:x[scapy.Raw], stop_filter=stopFilter)
f = open("./shadow", "w")

for ligne in data:
    if '[tp3]' in str(ligne[scapy.Raw]):
        ligne_clean = str(ligne[scapy.Raw]).replace("b'", "").replace('\\n', '').replace("'", '').replace('[tp3]', '') + '\n'
        f.write(ligne_clean)
    elif '[hash]' in str(ligne[scapy.Raw]):
        hash_initial = str(ligne[scapy.Raw]).replace("b'", "").replace('\\n', '').replace("'", '').replace('[hash]', '')
f.close()

def hash_file(filename):
   h = hashlib.sha256()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

hash_value = hash_file("shadow")

print('Hash initial : ' + hash_initial)
print('Hash ici : ' + hash_value)

if hash_value == hash_initial:
    print("Contenu identique")
else:
    print("Contenu différent")
