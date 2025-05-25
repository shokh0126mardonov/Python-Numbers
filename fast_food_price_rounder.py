from num2words import num2words
food1=float(input("$>>"))
food2=float(input("$>>"))
food3=float(input("$>>"))
S=round(food1+food2+food3,1)
word_ru=num2words(S,lang='ru',to='currency')
word_en=num2words(S,lang='en',to='currency')
print(F"Jami summa$ {S}({word_en}{word_ru})")
