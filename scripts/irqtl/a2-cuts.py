import sys

infile = open(sys.argv[1])# pi siri output
outfile1 = open(sys.argv[2],'w')# counts
outfile2 = open(sys.argv[3],'w')# et

header = sys.argv[4]

infile.readline()

outfile1.write(header+'\n')
outfile2.write(header+'\n')

count = 1

for line in infile:
	fields = line.strip().split()
	#outfile1.write('ri_'+"%07d" %count+'\t')
	#outfile2.write('ri_'+"%07d" %count+'\t')
	outfile1.write(','.join(fields[8:14])+'\n')
	outfile2.write(','.join(fields[14:])+'\n')
	count +=1


