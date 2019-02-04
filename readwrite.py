# Testing untuk read/write file
import sys

# test write
f = open(sys.argv[1],"r")
newarr = f.read().strip().split(" ")
print(newarr)

arr = [int(x) for x in newarr]

# test write
a = open(sys.argv[2],"w")
a.write(" ".join(str(x) for x in newarr))
