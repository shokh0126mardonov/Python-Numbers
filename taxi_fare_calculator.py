from num2words import num2words
S1=float(input("necha km yurganizni kiriting>>"))
money=round(S1*1.20+3)
word_en=num2words(money,lang='en',to='currency')
word_en=num2words(money,lang='en',to='currency')
word_ru=num2words(money,lang='ru',to='currency')
print(F"{money}({word_en})({word_ru})")


