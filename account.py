class Account:
    def __init__(self,initialBalance,accountNum):
        self._accountNumber = accountNum
        self._accountHolderName = ""
        self._rateOfInterest = 0.0
        self._currentBalance = initialBalance

    def getAccountNumber(self):
        return self._accountNumber

    def setAccountNumber(self,accountNumber):
        self._accountNumber = accountNumber
        
    def getAccountHolderName(self):
        return self._accountHolderName
    
    def setAccountHolderName(self,name):
        self._accountHolderName = name
    
    def getCurrentBalance(self):
        return self._currentBalance
    
    def getRateOfInterest(self):
        return self._rateOfInterest
    
    def setRateOfInterest(self,RateOfInterest):
        self._rateOfInterest = RateOfInterest
    
    def deposit(self,depositAmount):
            self._currentBalance += depositAmount

    def withdraw(self, withdrawAmount):
        if self._currentBalance >= withdrawAmount:
            self._currentBalance -= withdrawAmount
            return True
        else:
            return False
    

