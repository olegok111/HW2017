import random

deltas = {}
for i in range(32):
    symbol = chr(ord('а') + i)
    delta = random.randint(-1000, 1000)
    deltas[symbol] = delta

with open("oldtext.txt", encoding='utf8') as file1:
    oldtext = file1.read()
    oldtext = oldtext.replace('ё', 'е')
    coded = ''
    for i in oldtext:
        try:
            sy = chr(ord(i)+int(deltas[i]))
            coded += sy
        except:
            pass
    with open("oldtext_cipher.txt", "w", encoding="utf8") as output:
        print(coded, file=output)
