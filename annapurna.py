class SignUP:

    def userINFO(self):
        print("--- Enterb your Details ---")
        print("-----------------------------------------------------------------------")
        self.first_name = input("Enterb your first name : ")
        last_name = input("Enter your last name : ")
        self.user_contact_no = int(input("Enter your mobile number : "))
        self.user_mail = input("Enter your email : ")
        self.user_address = input("Enter your address : ")
        user_pswd1 = input("Enter new password : ")
        self.user_pswd2 = input("Re - Enter password : ")
        print("-----------------------------------------------------------------------")
        if user_pswd1 == self.user_pswd2:
            print("--- Account created ---")
            print("-----------------------------------------------------------------------")
            print(f"Welcome {self.first_name} please begin your first order by annapurna...")
            print("-----------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------")
            print("Password not matched... please try again!!!")
            print("-----------------------------------------------------------------------")

    def userLogin(self):
        print("-----------------------------------------------------------------------")
        print("--- USER LOGIN ---")
        print("-----------------------------------------------------------------------")
        ch = input("You may login either mobile or email (please enter valid option) : Mobile(m) | Email(e) : ")
        print("-----------------------------------------------------------------------")
        match(ch):
            case "m":
                print("-----------------------------------------------------------------------")
                user_id = int(input("Enter mobile number(ID) : "))
                if user_id == self.user_contact_no:
                    print("-----------------------------------------------------------------------")
                    print(f"Hello {self.first_name} prceed with password to login...")
                    print("-----------------------------------------------------------------------")
                    user_pasd = input("Enter your password : ")
                    if user_pasd == self.user_pswd2:
                        print("-----------------------------------------------------------------------")
                        print(f"hello {self.first_name} welcome to the annapurna....")
                        print("-----------------------------------------------------------------------")
                    else:
                        print("Invalid password... please try again...")
                        print("-----------------------------------------------------------------------")
                else:
                    print("Invalid Mobile number... please try again!!!")
                    print("-----------------------------------------------------------------------")

            case "e":
                    print("-----------------------------------------------------------------------")
                    user_email = input("Enter Emil(ID) : ")
                    if user_email == self.user_mail:
                        print("-----------------------------------------------------------------------")
                        print(f"Hello {self.first_name} prceed with password to login...")
                        print("-----------------------------------------------------------------------")
                        user_pasd = input("Enter your password : ")
                        if user_pasd == self.user_pswd2:
                            print("-----------------------------------------------------------------------")
                            print("--- Login success ---")
                            print(f"hello {self.first_name} welcome to the annapurna....")
                            print("-----------------------------------------------------------------------")
                        else:
                            print("Invalid password... please try again...")
                            print("-----------------------------------------------------------------------")
                    else:
                        print("Invalid Mobile number... please try again!!!")
                        print("-----------------------------------------------------------------------")

class Order:
    def userOrder(self):
        bill = 0.0
        print("---------------------------------------")
        while True:
                    print("--- Food Category ---")
                    print("---------------------------------------")
                    print("1. VEG")
                    print("2. NonVEG")
                    print("3. Exit")
                    print("---------------------------------------")
                    ch = int(input("Enter your choice : "))
                    print("---------------------------------------")
                    match(ch):
                        case 1:
                            print("---------------------------------------")
                            while True:
                                print("--- VEG MENU'S ---")
                                print("---------------------------------------")
                                print("1. PavBhaji")
                                print("2. Paneer tikka masala")
                                print("3. Sev bhaji")
                                print("4. Pizza")
                                print("5. Butter Naan")
                                print("6. Total Bill")
                                print("7. Exit")
                                print("---------------------------------------")
                                choice = int(input("Enter choice : "))
                                print("---------------------------------------")
                                match(choice):
                                    case 1:
                                        pavbhaji_bill = 150
                                        print("Pavbhaji added to cart success (price) : ",pavbhaji_bill)
                                        bill = bill + pavbhaji_bill
                                        print("---------------------------------------")
        
                                    case 2:
                                        ptm = 257.8
                                        print("Paneer tikka masala added to cart success (price) : ",ptm)
                                        bill = bill + ptm
                                        print("---------------------------------------")
        
                                    case 3:
                                        sevbhaji_bill = 120
                                        print("SevBhaji added to cart success (price) : ",sevbhaji_bill)
                                        bill = bill + sevbhaji_bill
                                        print("---------------------------------------")
        
                                    case 4:
                                        pizza_bill = 150.40
                                        print("pizza added to cart success (price) : ",pizza_bill)
                                        bill = bill + pizza_bill
                                        print("---------------------------------------")
        
                                    case 5:
                                        bn_bill = 40
                                        print("Butter naan added to cart success (price) : ",bn_bill)
                                        bill = bill + bn_bill
                                        print("---------------------------------------")
        
                                    case 6:
                                        print("---------------------------------------")
                                        print("Total Bill : ",bill)
        
                                    case 7:
                                        print("---------------------------------------")
                                        print("Exit")
                                        break
                        case 2:
                            print("---------------------------------------")
                            while True:
                                print("--- NONVEG MENU'S ---")
                                print("---------------------------------------")
                                print("1. Chicken Biryani")
                                print("2. chicken 65")
                                print("3. fish fry")
                                print("4. Butter Chicken")
                                print("5. Egg Curry")
                                print("6. total bill")
                                print("7. Exit")
                                print("---------------------------------------")
                                nonChoice = int(input("Enter choice : "))
                                print("---------------------------------------")
                                match(nonChoice):
                                    case 1:
                                        cb_bill = 250
                                        print("chicken biryani added to cart success (price) : ",cb_bill)
                                        bill = bill + cb_bill
                                        print("---------------------------------------")
        
                                    case 2:
                                        cs_bill = 467.90
                                        print("Chicken 65 added to cart (price) : ",cs_bill)
                                        bill = bill + cs_bill
                                        print("---------------------------------------")
        
                                    case 3:
                                        ff_bill = 450
                                        print("Fish fry added to cart (price) : ",ff_bill)
                                        bill = bill + ff_bill
                                        print("---------------------------------------")
        
                                    case 4:
                                        bc_bill = 500
                                        print("butter chiecken added to cart (price) : ",bc_bill)
                                        bill = bill + bc_bill
                                        print("---------------------------------------")
        
                                    case 5:
                                        ec_bill = 180
                                        print("Egg curry addded to cart (price) : ",ec_bill)
                                        bill = bill + ec_bill
                                        print("---------------------------------------")
                                    case 6:
                                        print("total bill : ",bill)
                                        print("---------------------------------------")
                                    case 7:
                                        print("exit")
                                        break
        
                        case 3:
                            print("--- VISIT AGAIN | THANK YOU ---")
                            break
s = SignUP()
o = Order()

s.userINFO()
s.userLogin()
o.userOrder()

                                

                        
                                
 
