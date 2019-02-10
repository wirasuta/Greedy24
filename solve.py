points_dict = {
    '+': 5,
    '-': 4,
    '*': 3,
    '/': 2,
    '(': -1,
}

op_list = ['+','-','*','/']

def point_op(x1,op,x2):
    #Mengembalikan point dari penyambungan expresi dengan operasi dan bilangan berikutnya
    try:
        hasil = eval(f"{x1} {op} {x2}")
        diff = points_dict[op] - abs(24-hasil)
        if (abs(24-hasil) == 0):
            return diff+10
        else:
            return diff
    except ZeroDivisionError:
        return float("-inf")

def point_expr(expr):
    #Mengembalikan point dari sebuah expresi
    points = 0
    hasil = eval(expr)
    points -= abs(24-hasil)
    for c in expr:
        points += points_dict.get(c,0)
    return points

def max(list):
    #Mengembalikan nilai maksimal dari sebuah array
    #Prekondisi : Array minimal satu elemen
    maxb = list[0]
    for b in list[1:]:
        if b>maxb:
            maxb = b
    return maxb

def solve(bil):
    maxb = max(bil)
    expr = str(maxb)
    bil.remove(maxb)
    for _ in range(3):
        b = max(bil)
        bil.remove(b)
        max_point = float("-inf")
        for op in op_list:
            curr_point = point_op(expr,op,b)
            if curr_point > max_point:
                max_point = curr_point
                curr_op_max = op
                curr_b_max = b
        expr += f" {curr_op_max} {curr_b_max}"

    points = point_expr(expr)
    # print(f"{expr} ~ Points: {points}")
    return (expr,points)

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
    print(f"Average points : {avg_points}")

    count24 = 0
    for expr in solves:
        res = eval(expr[0])
        if res==24:
            count24 += 1
    print(f"24 Count : {count24}")
    

if __name__ == "__main__":
    main()
