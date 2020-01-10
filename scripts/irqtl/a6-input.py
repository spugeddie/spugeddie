import sys

infile1 = open('/mnt/isilon/xing_lab/parke2/z36-siri-v8/a0-misc/ri_id.info') # ri_id.info
infile2 = open(sys.argv[1]) # et file - a5-filt
outfile1 = open(sys.argv[2],'w') # junc
outfile2 = open(sys.argv[3],'w') # body

list1 = []
infile2.readline()
for line in infile2:
	fields = line.strip().split()
	list1.append(fields[0])

infile2 = open(sys.argv[1]) # et file -	a5-filt

dict1 = {}
infile1.readline()
for line in infile1:
	fields = line.strip().split()
	if fields[0] in list1:
		dict1[fields[0]] = '\t'.join([fields[4],fields[5],fields[6],fields[0]+'-'+fields[1]+'-'+fields[2]])

outfile1.write('#Chr\tstart\tend\tTargetID\t')
outfile2.write('#Chr\tstart\tend\tTargetID\t')

fields = infile2.readline().strip().split()[1:]
fields = [i.split('/')[1] for i in fields]
fields = ['-'.join(i.split('-')[:2]) for i in fields]

outfile1.write('\t'.join(fields)+'\n')
outfile2.write('\t'.join(fields)+'\n')

for line in infile2:
	fields = line.strip().split()
	outfile1.write(dict1[fields[0]]+'\t')
	outfile2.write(dict1[fields[0]]+'\t')
	fields = fields[1:]
	outfile1.write('\t'.join([i.split(',')[0] for i in fields])+'\n')
	outfile2.write('\t'.join([i.split(',')[1] for i in fields])+'\n')




