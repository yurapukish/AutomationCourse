"""
Write class for bank card.

Class should reflect card lifecycle, card operations etc.
1) Use CVV, PIN, Name, Surname , end date, card_num as initial params.
2) Class should have in addition to common logic some class attributes,
as minimum one class method and as minimum  one staticmethod,
two or more getters/setters
3) Do not forget about block if __name__ == '__main__':
"""

import secrets
from datetime import datetime


class BankCard:
    """Reflect card lifecycle, card operations etc."""
    Card_Credit_Limit = 100

    Exchange_Rate = {'USD': {'rate': 1,
                             'sign': '$'},
                     'EUR': {'rate': 1.09,
                             'sign': "\u20AC"},
                     'UAH': {'rate': 0.027,
                             'sign': "\u20B4"}}

    def __init__(self, card_num, cvv, pin, name, surname, end_date, balance=Card_Credit_Limit):
        """Initialize card: add card number validation as a static method."""
        if not BankCard.validate_card_number(card_num):
            raise ValueError('Invalid card number')
        self.card_num = card_num
        self.__cvv = cvv
        self.__pin = pin
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.__balance = balance

    def __str__(self):
        """Return message about card creation."""
        return f'Bank card for {self.name} {self.surname}'

    @property
    def card_balance(self):
        """Return card Balance."""
        return self.__balance

    @card_balance.setter
    def card_balance(self, balance):
        """Update Card Balance."""
        self.__balance = balance

    @property
    def cvv(self):
        """Return card CVV."""
        return self.__cvv

    @cvv.setter
    def cvv(self, new_cvv):
        """Update CVV."""
        self.__cvv = new_cvv

    @property
    def pin(self):
        """Return card PIN."""
        return self.__pin

    @pin.setter
    def pin(self, new_pin):
        """Set card PIN."""
        self.__pin = new_pin

    @staticmethod
    def generate_new_cvv():
        """Generate new CVV."""
        return secrets.randbelow(900) + 100

    @staticmethod
    def validate_card_number(card_num):
        """Validate card number."""
        return len(card_num) == 16 and card_num.isdigit()

    @classmethod
    def get_exchange_rate(cls, currency):
        """Get exchange rate."""
        return cls.Exchange_Rate[currency]['rate']

    def withdraw(self, sum, currency='USD'):

        """Withdraw money from card.
        Raise ValueError if not enough money.
        Exchange rate should be taken from class attributes.
        """
        sign = BankCard.Exchange_Rate[currency]['sign']
        # Check that card not Expired
        if self.validate_end_date():
            raise ValueError('Card is Expired. Please request a new card.')

        if currency:
            rate = BankCard.get_exchange_rate(currency)
            sum = (sum * rate).__round__(2)
            if currency != 'USD':
                print(f'Exchange rate: 1$/{rate}{sign}.')

        if sum > self.card_balance:
            raise ValueError('Not enough money')
        self.card_balance = (self.card_balance - sum).__round__(2)
        print(f'Withdrew {sum}$. Balance: {self.card_balance}$')

    def validate_end_date(self):
        Card_Expired = False
        # Determine today's date
        date = datetime.now()
        min_date = (date.month, int(str(date.year)[2:]))
        # Parse self.end_date and convert for comparing
        card_end_date = tuple(int(x) for x in self.end_date.split('/'))

        # Compare today's date and end date
        if card_end_date[1] > min_date[1] or (card_end_date[1] == min_date[1] and card_end_date[0] >= min_date[0]):
            pass
        else:
            Card_Expired = True
        return Card_Expired


if __name__ == '__main__':
    user = BankCard('1234567890123456', 144, 442, 'John', 'Smith', '8/24')
    print('Step 1,', user.__str__(), '\n')
    print('Step 2, Is card number valid ???',
          user.validate_card_number(user.card_num), '\n')

    print('Step 3, Generate new CVV ')
    print(f'CVV before update {user.cvv= }')
    user.cvv = BankCard.generate_new_cvv()
    print(f'CVV after update {user.cvv= }', '\n')

    print('Step 4, Update pin (use getters/setters)')
    print(f'PIN before update {user.pin= }')
    user.pin = 992
    print(f'PIN after update {user.pin= }\n')
    print('Step 5, Is card Expired???',
          user.validate_end_date(), '\n')

    print('Step 5, Withdraw money')
    while True:
        amount = int(input("Enter amount you wanna withdraw. '\u2193': "))
        currency = input("Enter the currency (USD, EUR or UAH). '\u2193': \n")

        user.withdraw(amount, currency)
