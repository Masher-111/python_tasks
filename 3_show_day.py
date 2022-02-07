#По заданному номеру дня недели вывести его название
'''def show_day():
    number = int(input('Введите номер дня недели '))
    if number == 1:  return'Понедельник'
    elif number == 2:  return 'Вторник'
    elif number == 3:  return 'Среда'
    elif number == 4:  return 'Четверг'
    elif number == 5:  return 'Пятница'
    elif number == 6:  return 'Суббота'
    elif number == 7:  return 'Воскресенье'
print(show_day())'''
def show_day2(x):
    if x == 1: return 'Понедельник'
    elif x == 2: return 'Вторник'
    elif x == 3: return 'Среда'
    elif x == 4: return 'Четверг'
    elif x == 5: return 'Пятница'
    elif x == 6: return 'Суббота'
    elif x == 7: return 'Воскресенье'
print(show_day2(7)) 