#Ex7.2
fname = input("Enter the file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    find = line.find(":")
    flt = float(line[find + 1: ])    
    total = total + flt
    count = count + 1

print("Average spam confidence:", total/count)
