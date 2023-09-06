'''Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.'''

summ = 0
count_add = 0
count_out = 0


def withdraw(summ, count_out):
    summ_out = int(input("Сумма: "))
    comission = summ_out * 0.015
    if comission < 30:
        comission = 30
    elif comission > 600:
        comission = 600

    if summ_out + comission > summ:
        raise Exception('Error', "Недостаточно средств")
        print()

    else:
        if summ_out % 50 == 0:
            summ -= summ_out + comission

            count_out += 1
            if count_out % 3 == 0:
                summ *= 1.03
        else:
            raise Exception('Error', "Введена некорректная сумма")
    return summ


def add_money(summ, count_add):
    summ_add = int(input("Сумма: "))
    if summ_add % 50 == 0:
        summ += summ_add
        count_add += 1
        if count_add % 3 == 0:
            summ *= 1.03
    else:
        print("Введена некорректная сумма (не кратна 50)")
    return summ


def tax(summ):
    if summ > 5_000_000:
        print("С вас сняли налог на богатство", summ * 0.1)
        summ -= summ * 0.1
    return summ


while True:
    summ = tax(summ)

    action = input("Действие: ")

    if action == "q":
        print("Выходим из банкомата")
        print("Сумма: ", summ)
        break
    elif action == "a":
        summ = add_money(summ, count_add)

    elif action == "o":
        try:
            summ = withdraw(summ, count_out)
        except Exception as e:
            print(f'Ошибка снятия денег, {e}')

    print(f"Сумма: {summ}")