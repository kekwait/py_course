# 1. Fizz Buzz
# Дано: Число, как целочисленное (int).
# Задание:
# "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.
# Вы должны написать программу, которая принимает положительное целое число и возвращает сл. значения.
# "Fizz Buzz", если число делится на 3 и 5;
# "Fizz", если число делится на 3;
# "Buzz", если число делится на 5;
# Число, как строку для остальных случаев.


def fizz_buzz(num: int):
    return "Fizz buzz" if num % 5 == 0 and num % 3 == 0 else \
        "Fizz" if num % 3 == 0 else \
            "Buzz" if num % 5 == 0 else \
                str(num)


# 2. Оценка числа
# Дано: Число x.
# Задание: нужно написать программу, которая дает оценку заданному значению, используя следующие правила.
# если x нечетное, то это "Плохо"
# если x = [2, 5] и четное, то это "Неплохо"
# если x = [6, 20] и четное, то это "Так себе"
# если x > 20 и четное, то это "Отлично"
# Пример:
#  x = 15, результат: "Плохо"
#  x = 4, результат: "Неплохо"
#  x = 8, результат: "Так себе"
#  x = 24, результат: "Отлично"

def eval_num(num: int):
    if num % 2 != 0:
        return "Плохо"
    else:
        if 2 <= num <= 5:
            return "Неплохо"
        if 6 <= num <= 20:
            return "Так себе"
        if num > 20:
            return "Отлично"


# Дано: Число N = [1-9].
# Задание: нужно написать программу, которая выведет последовательность 123..N
# Пример:
#  N = 3, результат: 123
#  N = 9, результат: 123456789
#  x = 1, результат: 1

def generate_range(size: int):
    result_string = ""
    for i in range(1, size + 1):
        result_string += str(i)
    return result_string


# 4. Секретное сообщение
# "Где умный человек прячет лист? В лесу. Но что если леса нет? ...
# Он выращивает лес и прячет его там." -- Гилберт Кит Честертон
# Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты?
# Вы можете использовать газету, чтобы рассказать кому-то свой секрет. Даже если кто-то найдет ваше сообщение,
# легко отмахнуться и сказать что это паранойя и теория заговора. Один из самых простых способов спрятать
# ваше секретное сообщение это использовать заглавные буквы. Давайте найдем несколько таких секретных сообщений.
# Дано: Дан кусок текста (str).
# Задание: Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
# Подсказка: посмотрите внимательно на методы класса str.
# Пример:
#  текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы,
#  то получим сообщение "HELLO".

def secret_msg(msg: str):
    decoded_msg = ""
    for i in msg:
        if i.istitle():
            decoded_msg += i
    return decoded_msg


# [Junior] 5. Три слова
# Давайте научим наших роботов отличать слова от чисел.
# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв.
# Дано: Строка со словами (str).
# Задание: напишите программу, которая проверяет есть ли в исходной строке три слова подряд. Для примера, в строке
# "start 5 one two three 7 end" есть три слова подряд.
# Примеры:
# text = "Hello World hello", результат: True
# text = "He is 123 man", результат: False
# text = "1 2 3 4", результат: False

def three_words(text: str):
    text = text.split()
    i = 0
    result = [True] * len(text)
    for word in text:
        for letter in word:
            if letter.isdigit():
                result[i] = False
                break
        i += 1
    counter = 0
    for i in result:
        if i == False:
            counter = 0
        if i:
            counter += 1
        if counter == 3:
            return True
    else:
        return False


# [Junior+] 6. Мир захватили левши
# На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей." Santrock, John W. (2008). "
# "Motor, Sensory, and Perceptual Development.
# "Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и неопределеное число людей вероятно лучше всего "
# "охарактеризовать, как "симметричные"." Scientific American. www.scientificamerican.com
# Один робот был занят простой задачей: объединить последовательность строк в одно выражение для создания инструкции
# по обходу корабля. Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
# Дано: последовательность строк.
# Задание: вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
# В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left",
# даже если это часть другого слова. Все строки даны в нижнем регистре.
# Примеры:
# ["left", "right", "left", "stop"], результат: "left,left,left,stop"
# ["bright aright", "ok"], результат: "bleft aleft,ok"
# ["enough", "jokes"], результат: "enough,jokes"

def world_of_lefts(str_list: list):
    result = ""
    for i in range(0, len(str_list)-1):
        str_list[i] += ', '
    for i in str_list:
        result += i.replace("right", "left")
    return result


print(fizz_buzz(15), fizz_buzz(6), fizz_buzz(5), fizz_buzz(7), sep='; ')
print(eval_num(15), eval_num(4), eval_num(8), eval_num(24), sep='; ')
print(generate_range(3), generate_range(9), generate_range(1), sep='; ')
print(secret_msg("How are you? Eh, ok. Low or Lower? Ohhh."))

print(three_words("Hello World hello"), three_words("He is 123 man"), three_words("1 2 3 4"), sep='; ')
print(world_of_lefts(["left", "right", "left", "stop"]), world_of_lefts(["bright aright", "ok"]),
      world_of_lefts(["enough", "jokes"]), sep='; ')
