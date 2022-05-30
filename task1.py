import re
ipz = '10.1.192.38'
s = []
with open('log.txt', 'r') as f:
    for line in f:
        if line.split()[0] == ipz:
            match = re.search(r'sid=/(\S+)/&', line)
            s.append(match.group(1))
sor = sorted(s)
for sid in sor: print(sid)