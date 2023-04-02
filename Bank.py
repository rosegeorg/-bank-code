

import random
import account
from Savingsaccount import SavingAccount 
from Checkquing import ChequingAccount


class Bank:
    
    def __init__(self,accountHolderName,initialBalance):
        self._accountNum = 0
        self._accountHolderName = accountHolderName    
        self._currentBalance = initialBalance
       
        self._bankName = "CIBC bank"
        self._anAccount = account.Account(self._currentBalance,self._accountNum)
        self._anAccount.setAccountHolderName(self._accountHolderName)
        self._savingInstance = None
        self._chequingInstance = None
        
        self._accountNumList = []
        self._chequingInstances =[ChequingAccount(self._currentBalance,991669020),ChequingAccount(self._currentBalance,991669021),ChequingAccount(self._currentBalance,991669022)]
        self._savingInstances =[SavingAccount(self._currentBalance,991669020),SavingAccount(self._currentBalance,991669021),SavingAccount(self._currentBalance,991669022)]
        self._password =0
  
    def openAccount(self,balance,accountType =False):
       
        self._accountNum = random.randint(900000000, 999999999)
        self._anAccount.setAccountNumber(self._accountNum)
        self._accountNumList.append(self._accountNum)
        if accountType == "Chequing":
            self._chequingInstance = ChequingAccount(balance,self._accountNum)
        elif accountType == "Saving":
            if balance >=10:
                self._savingInstance = SavingAccount(balance,self._accountNum)
        return self._anAccount,self._chequingInstance,self._savingInstance  

   
    def searchAccount(self,accountNumber):
        if accountNumber in self._accountNumList:
            return True
        else :
            return False 

    def checkPassword(self,password):
        if self.getPassword() == password:
            return True
        else:
            return False
    
    def assignPin(self):
        self._pin =random.randint(1000,9999)
        return self._pin
    
    def checkPin(self,pin):
        if self._pin == pin:
            return True
        else:
            return False
    
    def getAccountNumber(self):
        return self._accountNum
    
    def getPassword(self):
        return self._password

    def setPassword(self,password):
        self._password = password
