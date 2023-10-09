print("\t\t\tWelcome to Automated fun booth!")

height = int(input("Enter your height in ft: "))
bill = 0
totalPhotos = 50

if height >= 3:
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 150
        print(f"\tPay Ksh 150/=")

    elif age < 18:
        bill = 250
        print(f"\tPay Ksh 250/=")

    else:
        bill = 500
        print(f"\tPay Ksh 500/=")

    print("To take photos press: ")
    print("1. Yes \n"
          "2. No ")
    photos = int(input("Do you want to take photos? "))

    if photos == 1:
        bill = bill + totalPhotos
        print(f"Additional Ksh 50 for charges. Total is: {bill} ")
    else:
        print(f"Total is: {bill}")
else:
    print("You can't ride this bike")

print("Thank you for trusting us!!!!Come back again")

