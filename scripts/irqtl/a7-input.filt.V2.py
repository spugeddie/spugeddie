import sys

infile1 = open(sys.argv[1]) # input file
infile2 = open(sys.argv[2]) # genotyped_samples_866

outfile = open(sys.argv[3],'w') # input.filt output

list1 = [i.strip() for i in infile2.readlines()]

header = infile1.readline()
fields = header.strip().split()
indexlist = [0,1,2,3]
for i in range(len(fields)):
	if fields[i] in list1:
		indexlist.append(i)

outfile.write('\t'.join([fields[i] for i in indexlist])+'\n')

for line in infile1:
	fields = line.strip().split()
	outfile.write('\t'.join([fields[i] for i in indexlist])+'\n')	
