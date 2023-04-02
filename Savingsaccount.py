import account
class SavingAccount(account.Account):
    def __init__(self, initialBalance, accountNum):
        super().__init__(initialBalance, accountNum)
       
        self._minimumBalance = 10

    def withDraw(self, withdrawAmount:float):
        if self.getCurrentBalance() - withdrawAmount >= self._minimumBalance:
            self._currentBalance -= withdrawAmount
            return True
        
        elif self.getCurrentBalance() -withdrawAmount <self._minimumBalance:
            return False        
            
        else:
            return "Invalid Entry!"
     