### 1. Дано два текстовых файла. Выяснить, совпадают ли их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

# with open("file1.txt", 'r', encoding='utf-8') as f1:
#     lines1 = f1.readlines()
# with open("file2.txt", 'r', encoding='utf-8') as f2:
#     lines2 = f2.readlines()
# with open("file3.txt", 'w', encoding='utf-8') as f3:
#     i = 0
#     for line in lines1:
#         if lines1[i] != lines2[i]:
#             f3.writelines(lines1[i] + '\n')
#             f3.writelines(lines2[i])
#         i += 1


### 2. Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр

# with open('text.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#
# with open('text1.txt', 'w', encoding='utf-8') as out:
#     str = text.count('\n') + 1
#     vowels = sum(text.count(i) for i in 'уеыаоэяию')
#     letters = sum(text.count(i) for i in 'йцкнгшщзхфвпрлджчсмтб')
#     numbers = sum(text.count(i) for i in '1234567890')
#     out.write(f'Символы: {len(text)} \n')
#     out.write(f'Строки: {str} \n')
#     out.write(f'Гласные: {vowels} \n')
#     out.write(f'Согласные: {letters} \n')
#     out.write(f'Цифры: {numbers}')


### 3. Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.

# with open('text.txt', 'r', encoding='utf-8') as text:
#     lines = text.readlines()
#
# with open('text1.txt', 'w', encoding='utf-8') as out:
#     for i in lines:
#         new_text = lines[:-1]
#     out.writelines(new_text)


### 4. Дан текстовый файл. Найти длину самой длинной строки.

# with open('text.txt', 'r', encoding='utf-8') as text:
#     lines = text.readlines()
#     str = []
#     for i in lines:
#         str.append(len(i))
#     print(max(str))


### 5. Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.

# with open('text.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     word = input('Введите слово: ')
#     print(f'Слово {word} встречается в тексте: ', text.count(word))


### 6. Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

# with open('text.txt', 'r', encoding='utf-8') as f:
#     file = f.read()
#     word1 = input('Введите слово, которое надо найти: ')
#     word2 = input('Введите слово, на которое надо произвести замену: ')
#     file = file.replace(word1, word2)
#
# with open('text.txt', 'w', encoding='utf-8') as f:
#     f.write(file)