1.addition/ 2.substraction/ 3.multiplication/ 4.division/ 5.modulo/
n1 = enter the number one
n2 = enter the number two
choice = int(input(enter your choice))
if choice == 1 :
   print("addition",:n1+n2)
elif choice == 2 :
   print("substraction",:n1-n2)
elif choice == 3 :
   print("multiplication",:n1*n2)
elif choice == 4 :
   print("division",:n1/n2)
elif choice == 5 :
   print("modulo",:n1%n2)
else :
   print("default choice") 