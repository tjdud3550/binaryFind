def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료 되었음, 잔액은 {0}원".format(balance + money))
    return balance + money
balance = 0
balance = deposit(balance,1000)
print(balance)