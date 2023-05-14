while True:

 a=int(input('Введите число'))
 b=int(input('Введите число'))
 c=int(input('Выберите действие:\n1.Вывести все числа диапазона\n2.Вывестисе числа диапазона в убывающем порядке\n3.Вывести числа,кратные7 \n4.Вывести количество чисел,кратные5'))
 for x in range(a,b+1):
   if c==1:
    print(x)
   elif c==2:
    for x1 in reversed(range(a,b+1)):
      print(x1)
   elif c == 3:
    if x%7  == 0:
      print(x)
   elif c == 4:
    if x%5  == 0:
      print(x)