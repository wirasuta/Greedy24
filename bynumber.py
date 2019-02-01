from pprint import pprint

points_dict = {
    '+': 5,
    '-': 4,
    '*': 3,
    '/': 2,
    '(': -1,
}

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

def calc_points(expr):
    points = 0
    hasil = eval(expr)
    points -= abs(24-hasil)
    for c in expr:
        points += points_dict.get(c,0)
    return points

def solve(inp):
    """solver, input berupa string 4 angka yang dipisahkan spasi"""
    #menyimpan semua kemungkinan kombinasi operasi dan urutan angka dalam list masing-masing
    all_expr = []
    opr_comb = product([x for x in "+-*/"], 3)
    num_perm = permutations(inp,4)

    #mengkombinasikan semua kemungkinan urutan angka dan operasi sebagai implementasi tahap pertama exhaustive search
    for num_item in num_perm:
        for opr_item in opr_comb:
            all_expr.append("{num0} {op0} {num1} {op1} {num2} {op2} {num3}".format(num0=num_item[0], num1=num_item[1], num2=num_item[2], num3=num_item[3], op0=opr_item[0], op1=opr_item[1], op2=opr_item[2]))

    val_max = calc_points(all_expr[0])
    expr_max = all_expr[0]
    for expr in all_expr[1:]:
        if (calc_points(expr) > val_max):
            val_max = calc_points(expr)
            expr_max = expr
    
    return (expr_max,val_max)

def main():
    # bil = [int(c) for c in input("Masukkan 4 angka dipisahkan spasi:").strip().split()]
    points = 0
    solves = []
    for a in range(1,14):
        for b in range(1,14):
            for c in range(1,14):
                for d in range(1,14):
                    bil = [a,b,c,d]
                    expre,point = solve(bil)
                    if expre not in solves:
                        solves.append((expre,point))
                        points += point
                        print(f"{(a-1)*13*13*13+(b-1)*13*13+(c-1)*13+d} : {expre}")

    avg_points = points/(13**4)
    solves.sort(key=lambda x: x[1],reverse=True)
    print("Worst cases:")
    pprint(solves[-300:])
    print(f"Average points : {avg_points}")
    print(f"Total points : {points}")

if __name__ == "__main__":
    main()