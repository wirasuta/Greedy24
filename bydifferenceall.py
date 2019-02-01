from pprint import pprint
points_dict = {
    '+': 5,
    '-': 4,
    '*': 3,
    '/': 2,
    '(': -1,
}

op_list = ['+','-','*','/']

def fitness(x1,op,x2):
    try:
        hasil = eval(f"{x1} {op} {x2}")
        diff = points_dict[op] - abs(24-hasil)
        return diff
    except ZeroDivisionError:
        return float("-inf")

def calc_points(expr):
    points = 0
    hasil = eval(expr)
    points -= abs(24-hasil)
    for c in expr:
        points += points_dict.get(c,0)
    return points

def solve(bil):
    bil.sort(reverse=True)

    expr = str(bil[0])
    bil = bil[1:]
    for _ in range(3):
        b_max_fitness = float("-Inf")
        for b in bil:
            for op in op_list:
                curr_fitness = fitness(expr,op,b)
                if curr_fitness > b_max_fitness:
                    b_max_fitness = curr_fitness
                    curr_op_max = op
                    curr_b_max = b
        expr += f" {curr_op_max} {curr_b_max}"
        bil.remove(curr_b_max)

    points = calc_points(expr)
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
    solves.sort(key=lambda x: x[1],reverse=True)
    print("Worst cases:")
    pprint(solves[-300:])
    print(f"Average points : {avg_points}")
    print(f"Total points : {points}")

if __name__ == "__main__":
    main()
