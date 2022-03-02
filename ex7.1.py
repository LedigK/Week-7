#Ex7.1

fh = open("mbox-short.txt")

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
