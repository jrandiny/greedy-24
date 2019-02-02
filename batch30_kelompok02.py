import utils
import processor.greedy1 as processor
import sys

if (len(sys.argv)==3):
    infile = open(sys.argv[1],"r")
    isi = infile.read()
    infile.close()

    num = isi.split()
    for i in range (len(num)):
        num[i] = int(num[i])

    ans = processor.calculate(num)

    print(ans[1])

    outfile = open(sys.argv[2],"w")
    outfile.write(ans[1])
    outfile.close()