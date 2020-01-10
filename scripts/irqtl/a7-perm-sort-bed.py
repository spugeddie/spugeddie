import sys
import random

infile = open(sys.argv[1]) # sort.bed input
outfile = open(sys.argv[2],'w') # output

outfile.write(infile.readline())

for line in infile:
	fields = line.strip().split()
	f1 = fields[:4]
	f2 = fields[4:]
	random.shuffle(f2)
	outfile.write('\t'.join(f1)+'\t'+'\t'.join(f2)+'\n')
