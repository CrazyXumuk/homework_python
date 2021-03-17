with open('text_3.txt', 'r', encoding='utf-8') as f:
    empoyees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f"Average salary = {round(sum(empoyees_dict.values()) / len(empoyees_dict), 3)}\n"
          f"Employees with salary less than 20000 {[e[0] for e in empoyees_dict.items() if e[1] < 20000]}")