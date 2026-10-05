






if choice == '5':
    file = open('calculations.txt', encoding='utf-8')  # указываем кодировку при открытии файла параметром encoding
    content = file.read()
    print(content)
    file.close()