#Register
#first name, last name, password, email
#generate user account


#login
#account number,  and password


#bank operation


#Initializing the system

print()

import random

database = {
    9279577997: ['Ann', 'Uvere', 'annuvere@gmail.com', 'annpassword', 2000000000]
}

def init():

    print("welcome to Bank Python")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
    
    if(haveAccount == 1):
    
        login()
    elif(haveAccount == 2):
            
        register()
    else:
        print("You have selected invalid option")
        init()

def login():

    print("********* Login to your account *********")

    accountNumberFromUser = input("What is your account number? \n")
    
    is_valid_account_number = account_number_validation(accountNumberFromUser)
    
    if is_valid_account_number:

        password = input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == int(accountNumberFromUser)):
                if(userDetails[3] == password):
                    bankOperation(userDetails)

        print("Invalid account or password")
        login()

    else:
        init()

def account_number_validation(accountNumber):
    
    if accountNumber:

        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True

            except ValueError:
                print("Invaid Account Number, account number should be integer")
                return False

            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Account Number cannot be less than or more than 10 digits")
            return False

    else:
        print("Account Numberis arequired field")
        return False


def register():

    print("******* Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your First name? \n")
    last_name = input("What is your Last name? \n")
    password = input("Create a password for yourself \n")

    try:

        accountNumber = generateAccountNumber()

    except ValueError():
        
        print("Account Generation failed due to internet connection")
        init()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account has been created")
    print(" ======= ======= ====== ===")
    print("Your account number is: %d" %accountNumber)
    print("Make sure you keep it safe")
    print(" ======= ======= ====== ===")

    login()
    
def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ))
    
    selectedOption = int(input("What would you ike to do? (1) deposit (2) withdrawal (3) logout (4) exit \n"))

    if(selectedOption == 1):
           
        depositOperation()
    elif(selectedOption == 2):
            
        withdrawalOperation()
    elif(selectedOption == 3):
            
        logout()
    elif(selectedOption == 4):

        exit()
    else:
        
        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    print("Withdrawal")
    #get current balance
    #get amount to withdraw
    #check if current balance > withdraw balance
    #deduct withdrawn amount from current balance
    #display current balance

def depositOperation():
    print("Deposit Operation")
    #get current balance
    #get amount to deposit
    #add deposited amount to current balance
    #display current balance

def generateAccountNumber():

    print("Generating Account Number")

    return random.randrange(1111111111,9999999999)

def set_current_balance(userDetails, balance):
    userDetails[4] = balance

def get_current_balance(userDetails):
    return userDetails[4]

def logout():
    login()


#### ACTUAL BANKING SYSTEM ####


init()
