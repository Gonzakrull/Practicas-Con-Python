#El objetivo del dia de hoy es hacer un tributo el mismo debe tener energia vida yhmabre
#En este paso creamos variables con los nombres de cada una 
Nombre = 'Bill'
Edad = 22
Distrito = 4
Especialidad = 'Usar un Tridente'
#Estas son los estados de bill
vida = 100
energia = 100
hambre = 0
#print(f'Mi tributo se llama {Nombre} tiene {Edad} años pertenece al distrito {Distrito} y su especialidad es {Especialidad}')
#El estado del tributo es ara saber si este esta bien mal si necesita algo como puede mejorarlo
def estado ():
 print(f"""Estado inicial del tributo
Vida: {vida}
energia:{energia}
hambre:{hambre}
 """)
#Mientras la vida sea mayor a 0 entocnes bill sigue en la arena y esta vivo

def Acciones():
   global vida,energia,hambre
   Decición = input("""¿Cual es tu siguiente desición?
1.Pelear
2.Comer
3.Descansar
4.Estado
""")
   #Si tu desición es 1 entonces peleara
   if Decición == '1':
        #Pelear
        vida = vida-10
        energia = energia -5
        print(f'Tu vida { vida} y energia {energia} a sido restada ')
   #Si tu desición es 2 entonces lo alimentaras
   elif Decición == '2':
        #Comer
        comida = comida +10
        print('Tu')
     
   elif Decición == '3':
        #Descansar 
        energia = energia + 5
        print(f'Al Descansar recuperaste energia {energia} y vida ')
   elif Decición == '4':
        estado()
        
   else :
        print('Intenta nuevamente no es una desicion valida')
while vida > 0:
    Acciones()
    
    