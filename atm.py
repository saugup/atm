cash=120000
class Atm():
    def __init__(self, cardNumber, pinNumber, cash):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber
        self.cash = cash
    
    def cashWithdrawl(self, cash, cashWithdrawl):
        self.cashWithdrawl[cash] = cashWithdrawl
    
    def BalanceEnquiry(self, cash, BalanceEnquiry):
        self.BalanceEnquiry[cash] = BalanceEnquiry


print('what is your card number')
input()
print('Hello! Please enter your pin number')
input()
print('Welcome! how much cash would you like to withdraw? Your balance is', cash)
input()