# steps to use pipenv:
# 1. '$ pipenv install' command to install virtual environment 
#                       in the directory you want to work in
# 2. '$ pipenv shell' command to enter the pipenv shell
# 3. 'pytest' command to run the test file
#    'pytest -k <sample_test_line> to run specific tests, rather than whole test file
# 4. 'exit' command to exit the pipenv shell


class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        return f"{self.code}(symbol)"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name
                and self.code == other.code and self.symbol == other.symbol
                and self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        self.amount = amount
        self. currency = currency

    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        if self.currency.symbol != None:
            return f"{self.currency.symbol}{self.amount:.{self.currency.digits}f}"
        else:
            return f"{self.currency.code} {self.amount:.{self.currency.digits}f}"

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.amount == other.amount
                and self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError("Can't add money ojects of different currencies")

        return Money(self.amount + other.amount, self.currency)


    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError("Can't subtract money ojects of different currencies")

        return Money(self.amount - other.amount, self.currency)

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        return Money(self.amount * multiplier, self.currency)

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        return Money(self.amount / divisor, self.currency)

# ==================================================================== test session starts =====================================================================
# platform darwin -- Python 3.7.2, pytest-3.10.0, py-1.7.0, pluggy-0.8.0
# rootdir: /Users/chinhle/momentum/w3d2-money-faxedexcel, inifile:
# collected 15 items                                                                                                                                           

# money_test.py ...............                                                                                                                          [100%]

# ================================================================= 15 passed in 0.06 seconds ==================================================================