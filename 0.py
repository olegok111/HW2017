n, m = map(int, input().split())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))
pos = [0, 0]
cep = 1
while True:
    if m > (pos[1])+1 and (ar[pos[0]][pos[1]+1])-(ar[pos[0]][pos[1]]) == 1:
        cep += 1
        pos[1] += 1
    elif pos[1] > 0 and (ar[pos[0]][pos[1]-1])-(ar[pos[0]][pos[1]]) == 1:
        cep += 1
        pos[1] -= 1
    elif n > (pos[0])+1 and (ar[pos[0]+1][pos[1]])-(ar[pos[0]][pos[1]]) == 1:
        cep += 1
        pos[0] += 1
if cep != 1:
    print(cep)
else:
    print(0)