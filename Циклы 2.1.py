while True:

 a=int(input('Введите число'))
 b=int(input('Введите число'))
 print('Простыми числами в этом диапазоне являются:')
 for c in range(a, b+1):
     if c > 1:
         for i in range(2, c):
             if (c % i) == 0:
                 break
         else:
             print(c)

