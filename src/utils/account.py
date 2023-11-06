from .token import Tokenizer
from os import environ


class Account:
    def __init__(self, username: str, token: str, is_admin: bool = False):
        self.username = username
        self.is_admin = is_admin
        self.token = token

    def read_flag(self) -> str:
        # if self.is_admin:
        return environ.get('FLAG')
        # else:
        #     return 'You are not admin!'


class AccountService:
    def __init__(self, tokenizer: Tokenizer):
        self.accounts = []
        self.tokenizer = tokenizer

    def create_account(self, username: str, is_admin: bool = False) -> Account:
        if self.get_account_by_username(username) is not None:
            raise Exception('Username already exists.')

        token = self.tokenizer.generate_token()
        account = Account(username, token, is_admin)
        self.accounts.append(account)
        return account

    def get_all_accounts(self) -> list[str]:
        return [account.username for account in self.accounts]

    def get_account_by_username(self, username: str) -> Account:
        for account in self.accounts:
            if account.username == username:
                return account
        return None

    def get_account_by_token(self, token: str) -> Account:
        for account in self.accounts:
            if account.token == token:
                return account
        return None
