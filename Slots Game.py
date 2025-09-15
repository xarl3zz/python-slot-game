import random
from colorama import Fore, Back, Style

print(Fore.RED + "Hello in red")

try:
    bet = int(input("How much do you wanna bet?(max 500$):"))
    if bet > 500:
        print("Sorry bets over 500 are not allowed!")
        exit()
    slots = ["🍉","🍇","🍎","7️⃣"]
            
    while(True):
        
            s1 = random.choice(slots)
            s2 = random.choice(slots)
            s3 = random.choice(slots)
            s4 = random.choice(slots)
            s5 = random.choice(slots)
            s6 = random.choice(slots)
            s7 = random.choice(slots)
            s8 = random.choice(slots)
            s9 = random.choice(slots)
            print("Good luck!")
            print(s1 ,s2 ,s3)
            print(s4, s5, s6)
            print(s7, s8, s9)
            if s1 == s2 == s3 or s4 == s5 == s6 or s7 == s8 == s9:
                bet = bet * 2
                print(f"You won ${bet}!")
                raspuns = input("Do you still wanna play?yes/no:")
                if raspuns.lower() == "no":
                    print("Game over!Thanks for playing")
                    break
                elif raspuns.lower() == "yes":
                    continue
                elif raspuns.lower() == "":
                    print("Eroare!")
                    break
            else:
                bet = bet - bet/2 - 10
                if bet < 0:
                    print("You dont have any money left!")
                    break
                print(f"You lost and you have ${bet} left")
                raspuns = input("Do you still wanna play?yes/no:")
                if raspuns.lower() == "no":
                    print("Game over!Thanks for playing!")
                    break
                elif raspuns.lower() == "yes":
                    continue
                elif raspuns.lower() == "":
                    print("Error please enter a numeber!")
                    break
except ValueError:
     print( Back.BLUE + "Please enter a valid number!:")
    
        

        

