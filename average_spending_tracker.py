from num2words import num2words
d1=float(input("1-kun$"))
d2=float(input("2-kun$"))
d3=float(input("3-kun$"))
d4=float(input("4-kun$"))
d5=float(input("5-kun$"))
d6=float(input("6-kun$"))
d7=float(input("7-kun$"))
D=(d1+d2+d3+d4+d5+d6+d7)/7
word_ru=num2words(D,lang='ru',to='currency')
word_en=num2words(D,lang='en',to='currency')
print(F"{D} ({word_en})({word_ru})")