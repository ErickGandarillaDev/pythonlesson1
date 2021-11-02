var = 'mundo'
num = 12132
num2= 5789
var_rapida = 0
flotante = 123.41
flotante2 = 456.12

carac = 'c'
carac2= 'd'

bol = True
bol2 = False
bol3 = None

print (var)
print (carac+carac2)
print (var + carac )

print (num+num2)
print (flotante+flotante2)

print (not bol )
print (not bol2 )
print (bol or bol2)
print (bol and bol2)

if 10 > 5:
    print ('10 es mayor que 5')
elif 10 < 5:
    print ('Eso es imposible viejo')    

if bol:
    print ('Usamos la variable bol')

if True:
    print ('Es verdadero')

if not False:
    print ('La negacion de falso')


while bol != bol2:
    if(var_rapida>10):
         bol = False
    print(var_rapida)
    var_rapida += 1   

if type(var_rapida) is int:
    print('Es un entero')

if type(var) is str:
    print('Es cadena')

if type(flotante) is float:
    print(' es flotante ')
