
int_age = int(input("Enter your age: ")) 
if int_age > 100:
    print("Sorry you're dead.")
elif int_age > 40:
    print ("You're over the hill.")
elif int_age > 65:
 print ("Enjoy your retirement!")
elif int_age < 13:
 print("You qualify for the kiddie discount.") 
elif int_age == 21:
    print("Congrats on your 21st!")
else:
 print("Age is but a number.")