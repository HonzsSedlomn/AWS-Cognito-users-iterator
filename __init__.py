from dotenv import load_dotenv
from typing import Dict, List
from users import Users

load_dotenv()

users = Users()

for (index, user) in enumerate(users.get_users()):
    user_attributes: List[Dict] = user['Attributes']
    user_sub = next(user_attribute['Value'] for user_attribute in user_attributes if user_attribute['Name'] == 'sub')
    print(f'User {index + 1} has sub: {user_sub}')
