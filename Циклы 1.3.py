while True:

 a=int(input('Введите число'))
 b=int(input('Введите число'))
 for c in range(a,b):
    if c%3==0:
       print('Fizz')
    elif c%5==0:
       print('Buzz')
    elif c%3==0 or c%5==0:
       print('Fizz Buzz')
    else:
       print(c)