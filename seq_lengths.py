import sys

#Prints lengths and header of all sequences

with open(sys.argv[1], "r") as fh:
    lines = fh.readlines()

for line in lines:
    line = line.strip() #removes newline at the end of all lines
    if line.startswith(">"): #header line starts with ">"
        header = line
    else: #all other are sequences
        length = len(line)
        print(length, header)
