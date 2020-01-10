infile = open('../a1-siri-out-split/Whole_Blood/GTEX-ZXG5-0005-SM-57WCN-intron.PI.txt')
outfile = open('ri_id.info','w')

outfile.write('ri_id\t')
outfile.write('\t'.join(infile.readline().strip().split('\t')[:8])+'\n')

count = 1
for line in infile:
	outfile.write('ri_'+"%07d" % count + '\t')
	outfile.write('\t'.join(line.strip().split('\t')[:8])+'\n')
	count +=1



