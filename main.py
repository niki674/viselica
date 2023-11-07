import os

clear = lambda: os.system('cls')

print('Привет! Я загадал случайное слово, твоя задача - угадать его!')
print('Поехали!')

words = {'коса', 'пила', 'мыло', 'окно', 'суши', 'дыра', 'лапа', 'заяц'}
word = words.pop()

letters = []
isWin = True
attempts = 6

while attempts > 0:
    isWin = True
    letter = input('Введите букву: ')
    clear()
    letters.append(letter)
    for simb in word:
        if simb in letters:
            print(simb, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Ты выиграл! Мои поздравления!')
        break

    if letter not in word:
        attempts -= 1
        print(f'у тебя осталось {attempts} попыток.')
        if attempts <= 0:
            print('Ты проиграл')