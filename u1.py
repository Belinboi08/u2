import os
os.system("cls")

print(5 + 5)
print(5 - 5)
print(5 * 2)
print(8 / 2)
print(6 ** 3)  #upp höjt med tre 
print(10 // 4) #Det gör så att den delar 10 med 4 utan decimal tal 
print(10 % 3)  #Det är 10 modulus 3 

x= input("Vad heter du för något ")
y= input ("Hur gammal är du ")

print("Hejsan " + x + "du är " + y + "år gammal")

a= float(input("använd det första talet "))
b= float(input("använd det andra talet "))

produkt = a * b 

print("produkten av", a, "och", b, "'är", produkt)

vikt = float(input("Ange din viktigt i kilogramn: "))
langd = float(input("Ange din längd i meter:  "))
 
bmi = vikt / (langd ** 2)

print("Ditt bmi är:", round(bmi, 2)) 

years = int(input("Hur gammal är du? "))
Weeks = years * 52

print ("Du har levt ungefär så här många", Weeks, "veckor.")

viktkg = float(input("För att du ska se hur mycket du väger i ibs, skirv in din vikt i kg: "))
viktibs = viktkg * 2.20462
print("Din vikt i pounds är " , viktibs)