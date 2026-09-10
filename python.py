class Bank:
    def __init__(self):
        self.balance=0
        self.acc_number=None
        self.pin=None
        self.deleted=False
        
    def create(self):
        acc_no=int(input("enter the 8 digit account number: "))
        n=len(str(acc_no))
        while(n != 8):
            print("Number is not valid")
            print("enter the 8 digit number")
            acc_no=int(input("enter the account number: "))
            if(len(str(acc_no))==8):
                self.acc_number=acc_no
            n=len(str(acc_no))
        self.acc_number=acc_no
        acc_pin=int(input("entr the 4 digit pin: "))
        m=len(str(acc_pin))
        while(m!=4):
            print("pin is not valid")
            print("enter the 4 digit pin")
            acc_pin=int(input("entr the pin: "))
            if(len(str(acc_pin))==4):
                self.pin=acc_pin
            m=len(str(acc_pin))
        self.pin=acc_pin
        print("your bank account has been created")

    def deposite(self):
        amount=int(input("enter the ammount: "))
        if amount>0:
            self.balance += amount
            print("added the amount successfully")
        else:
            print("invalid ammount. It should be greater then 0")

    def withdrow(self):
        amount=int(input("enter the ammount: "))
        if amount<=self.balance and amount> 0:
            self.balance -= amount
            print("withdrown the amount successfully")
        else:
            if(amount<=0):
                print("enter the money greater then 0")
            else:
                print("entered money is greater then banlance")

    def change_pass(self):
        passward=int(input("enter the old passward: "))
        if self.pin==passward:
            new_pin=int(input("enter the new passward: "))
            self.pin=new_pin
            print("passward successfully changed")
        else:
            print("invalid pin")

    def delete_acc(self):
        if self.balance==0:
            print("account is deleted")
            self.deleted = True
            return 0
        else:
            print("can not delete")
            
    def check_bal(self):
        print("your balance amount is ",self.balance)
d=Bank()

choice=0
while (choice != 7):
    print("\n")
    print("1. for creata a account")
    print("2. for deposite a money")
    print("3. for withdrow a money ")
    print("4. for changing the passward")
    print("5. for deleting account")
    print("6. checking balance")
    print("7. to stop")
    choice=int(input("enter the choice: "))
    if choice==1:
        d.create()
    if choice==2:
        d.deposite()
    elif choice==3:
        d.withdrow()
    elif choice==4:
        d.change_pass()
    elif choice==5:
        d.delete_acc()
    elif choice ==6:
        d.check_bal()
else:
    print("thank you")

    




        

      
