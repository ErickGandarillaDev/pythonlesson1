for numero2 in range(0, 100):
   if numero2 > 1:
       for i in range(2, numero2):
           if (numero2 % i) == 0:
               break
       else:
           print(numero2)