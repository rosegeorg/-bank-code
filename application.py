

import Bank

from Handlingexception import WrongChoiceException

class Application:
    
    def run(self):
        self.showMainMenu()
    
    
    def showMainMenu(self):
        name = ""
        self._accountBalance = 0.0
        aBank =None
        anAccount =None
       
        while True:
            try:
                print("Please enter\n1) for opening an account\n2) for selecting your account\n3 to exit")
               
                choice = int(input("Enter your choice: "))
                
                if choice != 1 and choice !=2 and choice !=3:
                    raise WrongChoiceException
                if choice == 1:
                    
                    name = input("Enter the account Holder's Name: ")
                    print("your account balance should be atleast 10 dollars to have a savings account: ")
                    initialDepositChoice= int(input("Enter\n1. to add money in savings account \n2. to add money to your chequing account! "))
                    self._accountBalance = float(input("Enter the initial amount you want to deposit "))
                    
                    if initialDepositChoice !=1 and initialDepositChoice!=2:
                        raise WrongChoiceException

                    aBank = Bank.Bank(name,self._accountBalance)

                    
                    
                    if initialDepositChoice == 1:
                        anAccount,self._chequingInstance,self._savingInstance = aBank.openAccount(self._accountBalance,"Saving")
                        anAccount,self._chequingInstance,self._savingInstance = aBank.openAccount(0,"Chequing")
                        print("Congratulations your account has been opened")
                        print(f"Your account number is: {aBank.getAccountNumber()}")
                        self._pin = aBank.assignPin()
                        print(f"You have a pin to access your account which is: {self._pin}")
                        self._password = int(input("Enter the password for the account: "))
                        aBank.setPassword(self._password)

                    elif initialDepositChoice == 2:    
                        anAccount,self._chequingInstance,self._savingInstance = aBank.openAccount(self._accountBalance,"Chequing")
                        print(f"Your account number is: {aBank.getAccountNumber()}")
                        self._pin = aBank.assignPin()
                        print(f"You have a pin to access your account which is: {self._pin}")
                        self._password = int(input("Enter the password for the account: "))
                        aBank.setPassword(self._password)

                
                if choice ==2:
                    
                    userinput =int(input("Enter your account Number: or accountpin: "))
                    self.showAccountMenu(userinput,aBank,anAccount)
                
                
                if choice == 3:
                   
                    break
            except ValueError:
                print("Invalid choice please input a valid choice number!")
            except WrongChoiceException:
                print("wrong choice entered!")
            

    
    def showAccountMenu(self,userInput,aBank,anAccount):
        while True:
            if aBank!=None and anAccount!=None: 
                if aBank.checkPin(userInput) or aBank.searchAccount(userInput):
                    password= int(input('Your account has been found enter the password to access it: '))
                    if aBank.checkPassword(password) or viewAccess ==True:
                        viewAccess = True
                        print("Enter 1. to check balance:\n2. to deposit money into account\n3. to withdraw money\n4. to exit")
                        try:
                            choice = int(input("enter your choice: "))
                            if choice !=1 and choice!=2 and choice!=3 and choice !=4:
                                raise WrongChoiceException
                            if choice == 1:
                                
                                if self._savingInstance !=None:
                                    print(f"Your current Balance in saving account is: {self._savingInstance.getCurrentBalance()}")
                                print(f"Your current balance in chequing account is: {self._chequingInstance.getCurrentBalance()}")

                            if choice == 2:
                                
                                print("Enter 1 to deposit in savings account\nEnter 2 to deposit in chequing account.")
                                depositChoice =int(input("Enter your choice!"))
                                if depositChoice !=1 and depositChoice!=2:
                                    raise WrongChoiceException
                                depositAmount = float(input("Enter the amount you want to deposit: "))
                                if depositChoice ==1 and self._savingInstance != None:
                                    self._savingInstance.deposit(depositAmount)
                                elif depositChoice ==1 and self._savingInstance ==None:
                                    anAccount,self._chequingInstance,self._savingInstance = aBank.openAccount(depositAmount,"Saving")
                                elif depositChoice ==2:
                                    self._chequingInstance.deposit(depositAmount)
                            
                            if choice ==3:
                                
                                print("Enter 1 to withdraw money from savings account.\n2 to withdraw money from chequing account ")
                                choice = int(input("Enter your choice: "))
                                if choice !=1 and choice !=2 :
                                    raise WrongChoiceException
                                if choice == 1 and self._savingInstance != None:
                                    
                                    withdrawAmount = float(input("Enter the amount you want to withdtraw: "))
                                    
                                    if self._savingInstance.withDraw(withdrawAmount) == True:
                                        print("Your money is succesfully withdrawn from your account:")
                                    else:
                                        print("Can't perform transaction!")
                                elif choice ==1 and self._savingInstance ==None:
                                    print("Saving Account does not exist!")
                            
                                if choice == 2:
                                    print("You have an overdraftlimit to withdraw money from your chequing account which is 1000$ +your currentBalance")
                                    withdrawAmount = float(input("Enter the amount you want to withdraw: "))
                                    
                                    if self._chequingInstance.withDraw(withdrawAmount) == True:    
                                        print("Your money is succesfully withdrawn from your account: ")
                                    elif self._chequingInstance.withDraw(withdrawAmount) == False:
                                        print("Needs to maintain a minimum amount in the account, Hence transaction invalid!")
                                    else:
                                        print("Not enough money,cannot perform transaction! ")
                            
                            if choice == 4:
                                
                                viewAccess =False
                                break
                           
                        except ValueError:
                            print("Invalid number or string entered!")

                        except WrongChoiceException:
                            print("wrong choice input!")
                    else:
                        print("Wrong Password entered!")
                        break        
                else:
                    print("Invalid entry: Account doesn't exist")
                    break
            else:
                print("No such account exists!")
                break


app = Application()
app.run()
