"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

acc_balance = 0
shop_list = []

def acc_increase(acc_balance):
    acc_balance += float(input('Введите сумму пополнения: '))
    return(acc_balance)

def buy(acc_balance):
    amount = float(input('Введите сумму покупки: '))
    if  amount > acc_balance:
        print('Денег недостаточно для покупки!')
        return (acc_balance)
    else:
        shop_list.append(input('Название покупки: ')+' '+str(amount))
        acc_balance -= amount
        return(acc_balance)

def print_history():
    print('Список  покупок: ')
    for item in shop_list:
        print(item)


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню ')

    if choice == '1':
        acc_balance = acc_increase(acc_balance)
    elif choice == '2':
        acc_balance = buy(acc_balance)
    elif choice == '3':
        print_history()
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
