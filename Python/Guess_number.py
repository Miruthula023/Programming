#import random library
import random

def Guess_num():
        
        #datas
        attempt = 0
        level = 1
        x = 0
        print("GUESS THE NUM\n\n")
        
        while level <=100:
            
        #reapeted playning
            while x <=100:
                
                lxt = f"\nNumber between 0 to {x}\n"
                print(lxt)
                
                Randum_num = random.randint(0,x)
                User_input = int(input("Enter the number:"))
                
                #evaluations
                if(Randum_num  != User_input):
                    print("Incorrect")
                    
                    while attempt < 100:
                        
                        Attempt_input = int(input("Enter the number: "))
                        
                        if( Attempt_input == Randum_num):
                            print("Congrats..\n move on to next level")
                            break
                        else:
                            print("incorrect")

                    attempt+=1
                    
                else:
                    
                    print("Congarts..\n Move on to next level")
                    
                x+=10
            level+=1
            
            
Guess_num()
