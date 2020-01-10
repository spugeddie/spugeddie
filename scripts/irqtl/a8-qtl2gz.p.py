import sys

#infile = open(sys.argv[1]) # changed to stdin
outfile = open(sys.argv[1],'w')

name = ''
outline = ''

for line in sys.stdin:
	fields = line.strip().split()
	if fields[0] != name:
		outfile.write(outline)
		name = fields[0]
		dist = 1000000
		pval = 1
		outline = line
	if float(fields[3])< pval:
		dist = abs(int(fields[2]))
		pval = float(fields[3])
		outline = line
	elif float(fields[3])==pval:
		if abs(int(fields[2])) < dist:
			dist = abs(int(fields[2]))
			pval = float(fields[3])
			outline = line
outfile.write(outline)
