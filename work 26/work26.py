# from typing import Optional, List
#
# player_coins: List[int] = []
# player_name: Optional[str] = "Hello"
#

from pydantic import BaseModel
from typing import Optional, List, Dict
#
# class Player(BaseModel):
#     player_name: Optional[str]
#     player_deposit: Optional[int]
#     player_items: List[Dict[str, int]]
#     player_friends: List[str] = []
#
#
# try:
#     new_player = Player(player_name='John', player_deposit=0, player_items=[])
#     print(new_player)
#
# except:
#     print('Error')

# 
# class Users(BaseModel):
#     user: Optional[str]
#     comment: Optional[str]
#     likes: List[int] = 0
# 
# 
# try:
#     users = Users(user='John', comment='Hello')
#     print(users)
#     users.likes += 1
#     print(users)
# except:
#     print('Error')
#
# class Bank(BaseModel):
#     name: str
#     money_amount: int
#     currency: str
#
# bank_client = {'name': 'Pasha', 'money_amount': 23000, 'currency': 'sum'}
#
# client1 = Bank(**bank_client)
#
# print(client1)



