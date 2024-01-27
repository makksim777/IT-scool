input_string=input("Введіть рядок")
if input_string==input_string[::-1]:   
   print("Введений рядок є паліндромом")
else:
   print("Введений рядок не є паліндромним")
   text=input("Ведіть текст:")
   reserved_words = input("Введіть список зарезервованих слів через кому:").split(',')
   for word in text.split():
      if word.lower()in reserved_words:
         print(text)

text = input("Ведіть тецт:")
num_sentences = text.count(',')+text.count('!')+text.count('?')
print(f"Кількість пропозицій у тексті:{num_sentences}") 



