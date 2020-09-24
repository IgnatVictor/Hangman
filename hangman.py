import os
import math
from random import randint
import random

y = random.randint(1,183)

select_dif = int(input("1 For easy /n 2 for hard /n Select dificulty :"))
level_dif = False
while (select_dif != 1 and select_dif!= 2 ):
    if select_dif == "quit" :
        break
    select_dif = int(input("Please make a correct choice 1 or 2: "))
def lives1():
    if select_dif == 1 :
        lives2 = 4
        return lives2
    else:
        lives2 = 3
        return lives2
    





def word_country():
    fname= "countries-and-capitals.txt"
    count = 0
    if(select_dif == 1):
        with open (fname, 'r+') as f:
            for line in f:
                count+=1
                if (count == y):
                    x = line
                    z = x.split("|")
                    return z[0].strip()
    elif select_dif == 2:
        with open (fname, 'r+') as f:
                for line in f:
                    count+=1
                    if (count == y):
                        x = line
                        z = x.split("|")
                        return z[1].strip()
              


def is_litera():
    k = input("please give a letter: ")
    while (len(k) != 1 or k.isalpha() == False):
        if k == "quit":
            break
        k= input("please give a corect letter: ")
    else:
        return k 

def print_grafic(lives):
    
    print('    --------')
    print('    |       |')
    print('    |       '+'O' if lives<4 else '    |       ')
    print('    |       '+'/\\' if lives<3 else '    |       ')
    print('    |       '+'||'  if lives<2 else '    |       ')
    print('    |       '+'/\\' if lives<1 else '    |       ')
    print('-------------')






def play():
    
    p = list(word_country().upper())
    
    hidden = ["_"]* len(p)
    lives = lives1()
    n = " "
    incercari = []
    k = list(word_country().upper())
    while n in k:
        index2 = k.index(n)
        k[index2] = "_"
            
    
    gameover = False
    print(k)
    while not gameover:
        print(hidden)
        print_grafic(lives)
        
        if(k == hidden or k == " "):
            print("YOU WIN")
            break
        n= is_litera().upper()
        
        

        while (n in p and lives>0):
            index1 = p.index(n)
            p[index1] = "_"
            hidden[index1] = n
            if n not in incercari:
                incercari.append(n)
            

           
         
        else:
            
            
            if(n not in incercari ):
                incercari.append(n)
                lives = lives -1 
            
            if(lives == 0):
                print_grafic(0)
                print("game over")
                gameover =True
            print("incercari : " , incercari)
        print_grafic(lives)
        print(hidden) 
        print(f" mai ai {lives} vieti")


play()
    


              




    

