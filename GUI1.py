# GUI pertama

import sys
from solve import solve

# untuk read file
f = open(sys.argv[1],"r")
a = open(sys.argv[2],"w")
with f as openedfile :
    for line in openedfile :
        newarr = line.strip().split(" ")
        if newarr != [''] :
            arr = [int(x) for x in newarr]
            hasil = solve(arr)
            # untuk write file
            
            a.write(hasil[0]+"\n")
