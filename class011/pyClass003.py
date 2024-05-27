def find_ascii_value(character):
    for i in range(len(character)):
        print(i, character[i], ord(character[i]))


find_ascii_value("Hello World")
