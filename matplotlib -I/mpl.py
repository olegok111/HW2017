import matplotlib.pyplot as plt
import numpy as np

with open('revizor.txt', 'r', encoding='utf8') as raw_text:
    text = raw_text.read()
    symbols = dict()
    for i in text:
        o = ord(i)
        if o == 1025 or 1040 <= o <= 1071 or 1072 <= o <= 1103 or o == 1105:
            if o == 1025:
                new_i = 'ё'
            elif 1040 <= o <= 1071:
                new_i = chr(o + 32)
            else:
                new_i = i

            try:
                symbols[new_i] += 1
            except KeyError:
                symbols[new_i] = 1
    L = list(symbols.keys())
    L.sort()
    x = tuple(symbols[i] for i in L)
    y = np.arange(len(x))
    plt.bar(y, x, align='center')
    plt.xticks(y, L)
    plt.show()

    signs = dict()
    amount = 0
    for i in text:
        if i in ('.', ',', '!', '?', '"', ')', '(', '-'):
            try:
                signs[i] += 1
            except:
                signs[i] = 1
            amount += 1
    L1 = tuple(i for i in signs.keys())
    percentage = tuple((signs[i] / amount) * 100 for i in L1)
    plt.pie(percentage)
    plt.legend(L1)
    plt.show()