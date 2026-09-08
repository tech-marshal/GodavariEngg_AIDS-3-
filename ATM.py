pin = 1234
balance = 0.0 
mobile = 9876543210
otp = 5981

userPin = int(input("Enter your pin : "))
print("-------------------------------------------")
if userPin == pin:
    print("--- Login success ---")
   
    print("-------------------------------------------")

    while True:
        otp = otp + 6
        print("-------------------------------------------")
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Check balance")
        print("4. Display user pin")
        print("5. Update user pin")
        print("6. Exit")
        print("-------------------------------------------")
        ch = int(input("Enter your choice : "))
        print("-------------------------------------------")
        match(ch):
            case 1:
                bal = float(input("Enter amount : ")) 
                balance = balance + bal
                print("--- Deposit success ---")
                print("Available balance : ",balance)
                print("-------------------------------------------")

            case 2:
                balw=float(input("Enter amount : "))
                if balw>balance:
                    print("--- insufficint funds ---")
                    print("---------------------------------------")
                else:
                    balance = balance - balw
                    print("--- withdrawl success ---")
                    print("Avaialble balance : ",balance)
                    print("-------------------------------------------")

            case 3:
                print("Avaialable balance : ",balance)
                print("-------------------------------------------")

            case 4:
                up = int(input("please re - enter your pin : "))
                if up == pin:
                    print("--- pin matched ---")
                    print("user pin : ",pin)
                    print("-------------------------------------------")
                else:
                    print("invalid pin... please try again")
                    print("-------------------------------------------")

            case 5:
                userMob = int(input("enter your mobie number that linked with bank : "))
                print("-------------------------------------------")
                if userMob == mobile:
                    print("--- number matched ---")
                    print("-------------------------------------------")
                    userOTP = int(input(f"Enter OTP send to {mobile} this number : "))
                    if userOTP == otp:
                        print("--- OTP varification success ---")
                        print("-------------------------------------------")
                        userOldPin = int(input("Enter your old pin : "))
                        if userOldPin == pin:
                            print("-------------------------------------------")
                            userNEWPin = int(input("Enter new pin : "))
                            pin = userNEWPin
                            print("--- pin update sucess ---")
                            print("-------------------------------------------")
                        else:
                            print("--- pin not matched ---")
                    else:
                        print("--- invalid OTP ---")
                else:
                    print("--- invalid mobile number ---")
            case 6:
                print("--- Logout ---")
                break 




else:
    print("--- invalid credentials ---")
    print("-------------------------------------------")
