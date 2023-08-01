# User(name, mail, address);
#
# Banks(name, rating, opened)
#
# Cards(cardholder(User), which_bank(Banks), opened);
#
# Balance(card(Cards), amount, currenc).

from pydantic import BaseModel
from typing import Optional, List, Dict

class User(BaseModel):
    name: str
    mail: str
    afress: str

class Banks(BaseModel):
    name: str
    rating: int
    opened: int

class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: int

class Balance(BaseModel):
    card: Cards
    amount: int
    currency: int


