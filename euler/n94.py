import winsound as ws
res = 0
for i in range(2, 333333334):
    a = i + 1
    b = i
    h = (b**2 - (a ** 2)/4) ** 0.5
    S = a * h / 2
    if S == int(S):
        P = a + 2*b
        res += P
print(res)
ws.PlaySound('C;\Windows\Media\Windows Critical Stop.wav', 0)
