import account

class ChequingAccount(account.Account):
    def __init__(self, initialBalance, accountNum):
        super().__init__(initialBalance, accountNum)
        
        self._overdraftLimit = 1000
    
    def withDraw(self, withdrawAmount):
        if self.getCurrentBalance() + self._overdraftLimit >= withdrawAmount:
            self._currentBalance -= withdrawAmount
            return True
        else:
            return "Exception"