# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте 
# все операции поступления и снятия средств в список.

import datetime

sum = 0
money = 0
temp = 0
temp_commision = 0
temp_wealth_tax = 0
count = 0
RICH = 5_000_000
WEALTH_TAX = 0.1
ADDITIONAL_RATE = 0.03
MIN_COMMISION = 30
MAX_COMMISION = 600
COMMISION = 0.015
AMOUNT_LIMIT = 50
START_MINIMUM_LIMIT = 50
ADDITIONAL_RATE_PERIOD = 3
logs =[]


def logging(logs, money, action):
    time = str(datetime.datetime.now())
    if action == "+":
        logs.append(('+', money, time))
    else:
        logs.append(('-', money, time))
    return logs


def add_money():
    global money, sum
    while money % AMOUNT_LIMIT != 0:
        print("сумма введена некорретно")
        money = int(input("Введите сумму: "))
    if sum < RICH:
        sum += money
        print("Ваш баланс - ", sum)
    elif sum > RICH:
        sum =  (sum + money) - ((sum + money) * WEALTH_TAX)          
        print("Ваш баланс - ", sum)
    return sum

def additional_bonus_calculation():
    global sum
    bonus = sum * ADDITIONAL_RATE
    print("Вам дополнительный доход - ", bonus)     
    return bonus

def additional_bonus_push():
    global sum
    sum += sum * ADDITIONAL_RATE
    print("Ваш баланс - ", sum)
    return sum


def pull_money_poor():
    global money, sum, temp, temp_commision
    while money % AMOUNT_LIMIT != 0:
        print("сумма введена некорретно")
        money = int(input("Введите сумму: "))
    if money * COMMISION < MIN_COMMISION:
        temp = sum - (money + MIN_COMMISION)
        while temp < 0 or money % AMOUNT_LIMIT != 0:
            print ("Операция не возможна, не достаточно средств")
            money = int(input("Введите сумму: "))
            temp = sum - (money + MIN_COMMISION)
        sum -= (money + MIN_COMMISION)
        temp_commision = MIN_COMMISION
    elif money * COMMISION > MAX_COMMISION:
        temp = sum - (money + MAX_COMMISION)
        while temp < 0 or money % AMOUNT_LIMIT != 0:
            print ("Операция не возможна, не достаточно средств")
            money = int(input("Введите сумму: "))
        sum -= (money + MAX_COMMISION)
        temp_commision = MAX_COMMISION
    else:
        temp = sum - (money * COMMISION)
        while temp < 0 or money % AMOUNT_LIMIT != 0:
            print ("Операция не возможна, не достаточно средств")
            money = int(input("Введите сумму: "))
        sum -= (money * COMMISION)
        temp_commision = money * COMMISION
    print("Ваш баланс - ", sum)
    return sum


def pull_money_rich ():
    global money, sum, temp, temp_commision, temp_wealth_tax
    while money % AMOUNT_LIMIT != 0:
        print("сумма введена некорретно")
        money = int(input("Введите сумму: "))
    if money * COMMISION < MIN_COMMISION:
        temp = sum - ((money + MIN_COMMISION) + sum * WEALTH_TAX)
        while temp < 0 or money % AMOUNT_LIMIT != 0:
            print ("Операция не возможна, не достаточно средств")
            money = int(input("Введите сумму: "))
            temp = sum - ((money + MIN_COMMISION) + sum * WEALTH_TAX)
        sum -= ((money + MIN_COMMISION) + sum * WEALTH_TAX)
        temp_commision = MIN_COMMISION
        temp_wealth_tax = sum * WEALTH_TAX
    elif money * COMMISION > MAX_COMMISION:
        temp = sum - ((money + MAX_COMMISION) + sum * WEALTH_TAX)
        while temp < 0 or money % AMOUNT_LIMIT != 0:
            print ("Операция не возможна, не достаточно средств")
            money = int(input("Введите сумму: "))
            temp = sum - ((money + MAX_COMMISION) + sum * WEALTH_TAX)
        sum -= ((money + MAX_COMMISION) + sum * WEALTH_TAX)
        temp_commision = MAX_COMMISION
        temp_wealth_tax = sum * WEALTH_TAX
    else:
        temp = sum - ((money + (money * COMMISION)) + sum * WEALTH_TAX)
        while temp < 0 or money % AMOUNT_LIMIT != 0:
            print ("Операция не возможна, не достаточно средств")
            money = int(input("Введите сумму: "))
            temp = sum - ((money + (money * COMMISION)) + sum * WEALTH_TAX)
        sum -= ((money + (money * COMMISION)) + sum * WEALTH_TAX)
        temp_commision = money * COMMISION
        temp_wealth_tax = sum * WEALTH_TAX
    print("Ваш баланс - ", sum)
    return sum


while True:
    command = input("введите действие: ")
    if command == "+":
        count += 1
        money = int(input("Введите сумму: "))
        sum = add_money()
        logs = logging(logs,money, command)
        print (*logs)
    if command == "-" and sum >= START_MINIMUM_LIMIT:                
        count += 1
        money = int(input("Введите сумму: "))
        if sum < RICH:
            sum = pull_money_poor()
            logs = logging(logs,money,command)                              
            logs = logging(logs,temp_commision,command) 
            print (*logs)
        else:
            sum = pull_money_rich ()
            logs = logging(logs,money, command)                              
            logs = logging(logs,temp_commision,command) 
            logs = logging(logs,temp_wealth_tax,command) 
            print (*logs)     
    if count % ADDITIONAL_RATE_PERIOD == 0:
        bonus = additional_bonus_calculation()
        sum = additional_bonus_push()
        logs = logging(logs,bonus,"+")
        print (*logs)
    if command == "-" and sum < START_MINIMUM_LIMIT: 
        print ("На счету не достаточно средств для снятия")
    if command == "e":
        print("Ваш баланс - ", sum)
        print ("Спасибо за использование нашего банка")
        break
    

    