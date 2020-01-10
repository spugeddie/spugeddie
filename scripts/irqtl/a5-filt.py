import sys

infile1 = open(sys.argv[1])#counts
infile2 = open(sys.argv[2])#et

outfile1 = open(sys.argv[3],'w')#counts
outfile2 = open(sys.argv[4],'w')#et

outfile1.write(infile1.readline())
outfile2.write(infile2.readline())

for line1 in infile1:
	f1 = line1.strip().split()
	line2 = infile2.readline()
	f2 = line2.strip().split()

	# 1 reads supporting inc average
	if sum(map(float,[i.split(',')[0] for i in f1[1:]]))/len(f1[1:]) < 1: continue
	# 1 reads supporting skip average
	if sum(map(float,[i.split(',')[1] for i in f1[1:]]))/len(f1[1:]) < 1: continue
	# 10 cov average
	if (sum(map(float,[i.split(',')[0] for i in f1[1:]]))+sum(map(float,[i.split(',')[1] for i in f1[1:]])))/len(f1[1:]) < 10: continue
	# 5% diff between 90-q and 10-q for both pi
	list1 = map(float,[i.split(',')[0] for i in f2[1:] if i.split(',')[0] != "NA"])
	list2 = map(float,[i.split(',')[1] for i in f2[1:] if i.split(',')[1] != "NA"])
	list1.sort()
	list2.sort()
	if list1[len(list1)/10*9]-list1[len(list1)/10] < 0.05: continue
	if list2[len(list2)/10*9]-list2[len(list2)/10] < 0.05: continue
	outfile1.write(line1)
	outfile2.write(line2)

