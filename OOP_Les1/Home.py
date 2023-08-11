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


class BankCard:
    """Reflect card lifecycle, card operations etc."""

    Card_Credit_Limit = 100
    Exchange_Rate = {'USD': 1, 'EUR': 0.9, 'UAH': 0.03}

    def __init__(self, card_num, cvv, pin, name, surname, end_date):
        """Initialize card: add card number validation as a static method."""
        if not BankCard.validate_card_number(card_num):
            raise ValueError('Invalid card number')
        self.card_num = card_num
        self._cvv = cvv
        self.__pin = pin
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.balance = BankCard.Card_Credit_Limit

    def __str__(self):
        """Return message about card creation."""
        return f'Created new Bank card for {self.name, self.surname}'

    @property
    def cvv(self):
        """Return card CVV."""
        return self._cvv

    @cvv.setter
    def cvv(self, new_cvv):
        """Update CVV."""
        self._cvv = new_cvv

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
    def get_exchange_rate(cls, rate):
        """Get exchange rate."""
        return cls.Exchange_Rate[rate]

    def withdraw(self, sum):
        """Withdraw money from card."""
        if sum > self.balance:
            raise ValueError('Not enough money')
        self.balance -= sum
        print(f'Withdrew {sum}. Balance: {self.balance}')


if __name__ == '__main__':
    user = BankCard('1234567890123456', 144, 442, 'John', 'Smith', '12/32')
    print('Step 1,', user.__str__(), '\n')
    print('Step 2, Is card valid ???',
          user.validate_card_number(user.card_num), '\n')

    print('Step 3, Generate new CVV ')
    print(f'CVV before update {user.cvv= }')
    user.cvv = BankCard.generate_new_cvv()
    print(f'CVV after update {user.cvv= }', '\n')

    print('Step 4, Use pin getter and setter')
    print(f'PIN before update {user.pin= }')
    user.pin = 992
    print(f'PIN after update {user.pin= }')

    print('Step 5, Withdraw money')
    while True:
        amount = int(input("Enter amount you wanna withdraw '\u2193': \n"))
        user.withdraw(amount)
