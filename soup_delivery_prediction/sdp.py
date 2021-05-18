#
# key - data, value (0:day of week( 1-7), 1:hollyday(1/0), 2: orders(numbers))
#
D = {}
N = {}
def add_new(date, day, hol, or1):
    D[date]=[day, hol]
    N[date] = or1
    return D

def prog(date, day, hol):
    prog = []
    p = 0
    i = 0
    for i in D:
        if D[i][0] == day and D[i][1] == hol: # заменить на Пифагора
            prog.append(N[i])
    for j in prog:
        p+=j
    P = p//len(prog)
    return P


add_new(515, 1, 0, 5)
add_new(516, 2, 0, 7)
add_new(516, 3, 0, 7)
add_new(517, 4, 0, 8)
add_new(518, 5, 0, 10)
add_new(519, 6, 1, 15)
add_new(520, 7, 1, 14)

for r in D:
    print(r, N[r], D[r])

print("523, 3, 0" , 'maybe orders = ', prog(523, 3, 0))
print('of')
