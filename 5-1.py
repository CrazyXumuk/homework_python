with open('text_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input('Input new stiring or empty string to done: ')) !='':
        my_file.write(f"{line}\n")
