# 1. Welcome to Python
# Дано: имя (переменная name) и фамилия (переменная surname).
# Задание: написать программу, которая будет приветствовать нового человека в мире Python.
# Текст сообщения: Hello NAME SURNAME! You just delved into Python. Great start!


def welcome_to_python(name: str = "Gleb", surname: str = "Rublenko"):
    return f'Hello {name} {surname}! You just delved into Python. Great start!'


# 2. Заголовок
# Дано: текст любой длины (переменная text).
# Задание: написать программу, которая выведет заголовок, используя заданный текст. Подсказка: используйте метод title.
# Пример: text = 'hello world'; результат = Hello World


def header(text: str = "hello world!"):
    return text.title()


# 3. Форматированный вывод денежной суммы
# Дано: денежная сумма (amount > 0).
# Задание: написать программу, которая распечатает число в принятом денежном формате: XXX,XXX.XX.
# Пример: amount = 100500.157; результат = 100,500.16


def format_amount(amount: float = 100500.157):
    return "{:,.2f}".format(amount)


# 4. Python art
# Дано: маркер (символ) и толщина фигуры.
# Задание: написать программу, которая будет отображать заданную фигуру.
# Пример: Маркер = H, толщина 5.

def draw_figure(thickness: int, sym: str):
    figure = ""
    for i in range(1, thickness * 2, 2):
        figure += ('{: ^' + str(thickness * 2 - 1) + '}').format(sym * i) + '\n'
    for i in range(1, thickness):
        figure += ('{: ^' + str(thickness * 2 - 1) + '}').format(sym * thickness) + \
                  ('{: >' + str(thickness * 4 - 1) + '}').format(sym * thickness) + '\n'
    for i in range(1, (thickness + 1) // 2):
        if thickness % 2 == 0:
            figure += (thickness // 2 - 1) * ' ' + sym * (thickness * 5 + thickness // 2 - 1) + '\n'
        else:
            figure += (thickness // 2) * ' ' + sym * (thickness * 5 + thickness // 2 - 1) + '\n'
    for i in range(1, thickness):
        figure += ('{: ^' + str(thickness * 2 - 1) + '}').format(sym * thickness) + \
                  ('{: >' + str(thickness * 4 - 1) + '}').format(sym * thickness) + '\n'
    for i in range(thickness * 2 - 1, 0, -2):
        figure += ('{: ^' + str(thickness * 4 + thickness // 2 - 1) + '}').format(' ' * thickness) + \
                  ('{: ^' + str(thickness * 2) + '}').format(sym * i) + '\n'
    return figure


# 5. Дизайнер ковриков
# Дизайнер составил шаблон домашних ковриков. Для массового выпуска ковриков ему нужно уметь
# быстро составлять макет произвольного размера. Известно, что длина коврика всегда больше
# в 3 раза чем его ширина (W = 3 * H).
# Дано: ширина коврика.
# Задание: написать программу, которая будет составлять макет коврика для его дальнейшего производства.

def carpet(height: int):
    width = 3 * height
    figure = ""
    for i in range(1, height, 2):
        figure += ('{:-^' + str(width) + '}').format('.|.' * i) + '\n'
    figure += ('{:-^' + str(width) + '}').format("welcome") + '\n'
    for i in range(height - 2, 0, -2):
        figure += ('{:-^' + str(width) + '}').format('.|.' * i) + '\n'
    return figure


print(welcome_to_python())
print(header())
print(format_amount())
print(draw_figure(5, '#'))
print(draw_figure(9, '3'))
print(carpet(11))
print(carpet(7))
print(carpet(3))
