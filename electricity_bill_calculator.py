from num2words import num2words
oy_boshi=float(input("oy boshidagi ko'rsatgich:"))
oy_oxiri=float(input("oy oxiriidagi ko'rsatgich:"))
S1=(oy_oxiri-oy_boshi)*0.45
word_en=num2words(S1,lang='en',to='currency')
word_ru=num2words(S1,lang='ru',to='currency')
print(F"{S1}({word_en})({word_ru})")



