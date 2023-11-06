from utils.account import AccountService
from utils.token import Tokenizer


account_service = None
current_user = None


def main():
    global account_service, current_user

    m = 0x3f2849caaeaf1aa6ed5975ad28be8e3c6289b87035e43158b0d48c02788bff92fba5
    c = 0x81f70ad2fa1d52a77428093bb17f774d1a4cd05fa5f4545fea14f21f734f328a41fc
    n = 0x8ff8e951c848ac46d95de97944c3bdc609542a776385bfda9d899b905e98c40ff591

    tokenizer = Tokenizer(m, c, n)
    account_service = AccountService(tokenizer)

    account_service.create_account('admin', True)
    account_service.create_account('yesver')
    account_service.create_account('modupawn')

    print('==============================')
    print('Welcome to the Yesver Service!')
    print('==============================')

    while True:
        return_value = guest_menu() if current_user is None else auth_menu()
        if return_value == 0:
            break

    print('Thank you for using the service!')


def guest_menu() -> int:
    global current_user, account_service

    print('Choose one menu:')
    print('1. Register')
    print('2. Login')
    print('0. Exit')

    try:
        option = int(input('>> '))
        if not (0 <= option <= 2):
            raise ValueError()
    except ValueError:
        print('Invalid option!')
        return 1

    match option:
        case 0:
            return 0
        case 1:
            username = input('Username: ').strip()
            try:
                account = account_service.create_account(username)
            except Exception as e:
                print(e)
                return 1
            print(f'Account created! Your token: {account.token}')
            return 1
        case 2:
            token = input('Token: ').strip()
            account = account_service.get_account_by_token(token)
            if account is not None:
                current_user = account
                print(f'Welcome, {current_user.username}!')
            else:
                print('Invalid token!')
            return 1


def auth_menu() -> int:
    global current_user, account_service

    print('Choose one menu:')
    print('1. Read the Flag')
    print('2. Logout')
    print('0. Exit')

    try:
        option = int(input('>> '))
        if not (0 <= option <= 2):
            raise ValueError()
    except ValueError:
        print('Invalid option!')
        return 1

    match option:
        case 0:
            return 0
        case 1:
            flag = current_user.read_flag()
            print(flag)
            return 1
        case 2:
            current_user = None
            print('Logged out!')
            return 1


if __name__ == '__main__':
    main()
