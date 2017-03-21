# -*- coding:utf-8 -*-
import re
with open('Shinel.txt', 'r') as text:
    text_encoded = text.readlines()
    text_encoded1 = str(text_encoded)
    print(len(re.findall('[^ ]+', text_encoded1)))
