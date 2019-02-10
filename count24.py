from datetime import datetime

def product(inp,r):
    """cartesian product dari input dengan dirinya sendiri diulang sebanyak n kali
    input harus berupa string/list"""
    retlist = []
    for _ in range(r):
        if len(retlist)>0:
            new_retlist = []
            for retitem in retlist:
                for inpitem in inp:
                    new_retlist.append(retitem+inpitem)
            retlist = new_retlist.copy()
        else:
            for inpitem in inp:
                retlist.append(inpitem)
    return retlist

def permutations(inp,r):
    """mengembalikan list semua kemungkinan permutasi dari inp dengan panjang r
    input harus berupa list"""
    retlist = []
    if r<=1:
        retlist.append(inp)
    else:
        for i in range(len(inp)):
            recinp = inp[:i] + inp[i+1:] 
            rec = permutations(recinp,r-1)
            for x in rec:
                temp = [inp[i]] + x
                retlist.append(temp)
    return retlist 

def solve(inp_str):
    """solver, input berupa string 4 angka yang dipisahkan spasi"""
    #menyimpan semua kemungkinan kombinasi operasi dan urutan angka dalam list masing-masing
    all_expr = []
    opr_comb = product([x for x in "+-*/"], 3)
    num_perm = permutations(inp_str.strip().split(),4)

    #mengkombinasikan semua kemungkinan urutan angka dan operasi sebagai implementasi tahap pertama exhaustive search
    for num_item in num_perm:
        for opr_item in opr_comb:
            all_expr.append("(({num0} {op0} {num1}) {op1} {num2}) {op2} {num3}".format(num0=num_item[0], num1=num_item[1], num2=num_item[2], num3=num_item[3], op0=opr_item[0], op1=opr_item[1], op2=opr_item[2]))
            all_expr.append("({num0} {op0} ({num1} {op1} {num2})) {op2} {num3}".format(num0=num_item[0], num1=num_item[1], num2=num_item[2], num3=num_item[3], op0=opr_item[0], op1=opr_item[1], op2=opr_item[2]))
            all_expr.append("({num0} {op0} {num1}) {op1} ({num2} {op2} {num3})".format(num0=num_item[0], num1=num_item[1], num2=num_item[2], num3=num_item[3], op0=opr_item[0], op1=opr_item[1], op2=opr_item[2]))
            all_expr.append("{num0} {op0} (({num1} {op1} {num2}) {op2} {num3})".format(num0=num_item[0], num1=num_item[1], num2=num_item[2], num3=num_item[3], op0=opr_item[0], op1=opr_item[1], op2=opr_item[2]))
            all_expr.append("{num0} {op0} ({num1} {op1} ({num2} {op2} {num3}))".format(num0=num_item[0], num1=num_item[1], num2=num_item[2], num3=num_item[3], op0=opr_item[0], op1=opr_item[1], op2=opr_item[2]))
            
    #menguji semua expresi dan mencari yang hasilnya 24
    correct_expr = []
    dev = 10e-12
    for expr in all_expr:
        try:
            res = eval(expr)
            if (res >= (24-dev)) and (res <= (24+dev)):
                correct_expr.append(expr)
        except ZeroDivisionError:
            pass
    
    return list(set(correct_expr))

def main():
    count24 = 0

    for a in range(1,14):
        for b in range(1,14):
            for c in range(1,14):
                for d in range(1,14):
                    bil = " ".join([str(c) for c in [a,b,c,d]])
                    res = solve(bil)
                    if len(res) > 0:
                        print(f"{(a-1)*13*13*13+(b-1)*13*13+(c-1)*13+d} : {res[0]}")
                        count24 += 1
                    else:
                        print(f"{(a-1)*13*13*13+(b-1)*13*13+(c-1)*13+d} : No solution")

    print(f"24 Count : {count24}")

if __name__ == "__main__":
    main()