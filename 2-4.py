all_str = input('Введите несколько слов, разделяя их пробелами: ')
for idx, word in enumerate(all_str.split()):
    print(idx + 1, (word, word[:11])[len(word) > 10])