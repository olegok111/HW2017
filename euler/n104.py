import winsound as ws
seq = [0] * 200000
seq[0] = 1
seq[1] = 2
for q in range(2, len(seq)):
    seq[q] = seq[q-1] + seq[q-2]


res = None
k = 0
while not res:
    k += 1
    f = seq[k]
    f = str(f)
    if len(f) < 9:
        continue
    f_first = set(int(i) for i in f[:9])
    f_end = set(int(i) for i in f[-9:])
    if len(f_first) == 9 and 0 not in f_first and len(f_end) == 9 and 0 not in f_end:
        res = k
print(res)
ws.PlaySound('C:\Windows\Media\tada.wav', 0)
