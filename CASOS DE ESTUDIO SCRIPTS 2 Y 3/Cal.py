print("Bienvenido, al protocolo de llenado de 20 camiones")
bolsasCapacidad = 0
conteo = 0
suma = 0
for i in range(10):
    conteo = conteo+1
    while True:
        numero = int(input(f"\ndigite el peso del camion {conteo}, recuerde que debe de estar dentro del rango de 18000 kg y 28000 kg: "))

        if numero >= 18000 and numero <= 28000:
            print("\nCapacidad adecuada")
            break
        else: numero < 18000 and numero >28000 
        print("\npeso no adecuado, vuelve a digitar el peso del camion")
            

    bolsas =int(input("\nAhora digita la cantidad de bolsas de cal que piensas llevar en el camion 1: "))

    for i in range(bolsas):

        while True:
            i +=1
            
            bolsasCapacidad = int(input(f"\nDigite la capacidad de la bolsa {i}: "))
            i-=1

            if bolsasCapacidad >= 3000 and bolsasCapacidad <= 9000:
                
                print("\nCapacidad adecuada ")
               
                suma = suma+bolsasCapacidad
                if suma > numero :
                    print("No puedes llevar mas bolsas de cal se te quitara la ultima bolsa, haz completado el total de tu camion")
                break

                
            
        
            else: bolsasCapacidad >= 3000 and bolsasCapacidad <= 9000
            print("\ncapacidad no adecuada digita de nuevo la capacidad ")
    
    print("\ncarga finalizada, empezando con el siguiente camion")
            

            
           
            
            



                    
                
                 
      

             

            
            
