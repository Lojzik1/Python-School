#--------------#
#BMI KALKULAČKA#
#--------------#

#weight = int(input("Zadej váhu:"))
#height = int(input("Zadej výšku v cm:"))

#height /=100

#bmi = weight/(height**2)

#print(bmi)

#if (bmi < 18.5):
    #print("máš podváhu")
#elif(bmi < 24.9):
    #print("jsi ok")
#else:
    #print("máš nadváhu")

#-----------------------#
#FIBONACCIHO POSLOUPNOST#
#-----------------------#

#a0 = 0
#a1 = 1

#idk = int(input("cislo"))
#idk1 = 0
#while idk1 < idk:
    #a1 = (a1+a0)
    #print (a1)
    #idk1 += 1
    #if idk1 < idk:
        #a0 = (a1+a0)
        #print (a0)
        #idk1 += 1

#------------#
#PRÁCE S POLI#
#------------#    

#cisla = [23,3,14,11,25,65,8,3,65,0]

#num = 0
#num2 = 0
#for x in cisla:
    #if x >= num:
        #num = x
#for x in cisla:
    #if x == num:
        #num2 += 1        

#print("Největší číslo je", num)
#print("Jejich počet v poli je", num2)         

#-------------------#
#MATEMATICKÉ OPERACE#
#-------------------#

#import math
#print(math.sqrt(4))

#------#
#FUNKCE#
#------#

#def my_first_function(a, b):
    #soucet = a+b
    #return soucet
#n = my_first_function(5, 5)
#print(n)

#def legs(chickens, pigs, cows):
    #count = chickens*2 + pigs*4 + cows*4
    #return count

    #print(legs(4,6,3))

#def zaokrouhli(a,b):        #5, 2
    #x = a//b                #x = 2
    #if a/b >= x+0.5:
        #return x + 1
    #else:
        #return x

#print(zaokrouhli(7,3))

#def football_points(v, r, p):
    #return v*3 + r
#print(football_points(3,4,2))

#def převod_boolean_na_string(my_bool):
    #if my_bool == True:
        #return "True"
    #elif my_bool == False:
        #return "False"
   # else:
        #return "Zadej boolean"

#print(převod_boolean_na_string(True))

#-------#
#VÝPOČET#
#-------#

#def distance(xa, ya, xb, yb):
    #"""
    #Funkce vypočítá vzdálenost dvou bodů A a B v rovině.
    #Body jsou zadané dvojicí souřadnic A(xa, ya), B(xb, yb)
    #>>> distance(0, 0, 3, 4)
    #5.0
    #"""
    
    #return 0

#if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

#--------------------#
#PŘEKLAD DO PIG LATINY#
#--------------------#

#def pig_word(word):
    #split_word = list(word)
    #split_word.append(split_word[0])
    #split_word.pop(0)
    #return "".join(split_word) + "ay"

#def pig_word_two(word):
   #return word[1:] + word[0] + "ay"


#def pig_latin(sentence):
   #split_sentence = sentence.split()
    #i = 0
    #for n in split_sentence:
        #split_sentence[i] = pig_word(n)
        #i += 1
    #return " ".join(split_sentence)

#print(pig_latin("i love pig latin"))


#pole = [3,5,2,4,23,245,13]
#n = len(pole)
#for i in range(0,n):
    #for j in range(i + 1,n):
        #if(pole[i]>pole[j]):
            #temp = pole[i]
            #pole[i] = pole[j]

#print(n)
    






    
    
    


