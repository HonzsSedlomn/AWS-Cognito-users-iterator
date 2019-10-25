import boto3, os
from boto3_type_annotations.cognito_idp import Client


class Users:
    counter: int = 0

    def __init__(self):
        if self.counter == 1:
            raise BaseException('Class Users can be initialize just once.')

        self._load_user_pool_id()

        self.client: Client = boto3.client('cognito-idp')
        Users.counter += 1

    def _load_user_pool_id(self):
        self.__user_pool_id = os.getenv('USER_POOL_ID')

        if self.__user_pool_id is None:
            raise ValueError('USER_POOL_ID loaded from .env file must be defined.')

    def get_users(self) -> list:
        list_users_response: dict = self.client.list_users(UserPoolId=self.__user_pool_id)

        while True:
            for user in list_users_response['Users']:
                yield user

            if pagination_token := list_users_response.get('PaginationToken'):
                list_users_response = self.client.list_users(UserPoolId=self.__user_pool_id,
                                                             PaginationToken=pagination_token)
            else:
                break
