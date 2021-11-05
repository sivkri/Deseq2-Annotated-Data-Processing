import sys

input = sys.argv[1]
f1 = open(input)

output = input.replace('deseq2_annotated', '1.5_FC')
out = open(output, 'w')

header = f1.readline()
out.write(header)

for line in f1:
  l = line 
  line = line.strip().split('\t')
  gene_id = line[0]
  log2FoldChange =	float(line[2])
  adjusted_P_value = float(line[5])
  
  if log2FoldChange > 0.585 or log2FoldChange < -0.585:
        out.write(l)