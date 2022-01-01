class Atm():
    def __init__(self, name, cardCompany, cardNumber, cardPin):
        self.name = input("Enter your name: ")
        self.cardCompany = input("Enter the company of your card: ")
        self.cardNumber = int(input("Enter the card number: "))
        self.cardPin = int(input("Enter the card pin: "))
    def action():
        print("Please type in all caps, what you wish to do out of ")
        print("TRANSACTION \nPIN CHANGING \nDEPOSIT \nBALANCE CHECK")
        x = input("Enter action to be done from the above: ")
        if x == "TRANSACTION":
            a = int(input("Enter amount to be transacted: "))
            print("Succesfully transacted amount "+a)
        elif x == "PIN CHANGING":
            b = int(input("Enter new pin: "))
            print("Pin succesfully changed to"+b)
        elif x == "DEPOSIT":
            c = int(input("Enter amount to be desposited: "))
            print("Amount successfully deposited "+c)
        else:
            print("Your bank balance is: 34438563862")
abcd = Atm("anant", "hdfc", 1234567890, 666)
Atm.action()