current_index = 0

while True:
    word = input("Input word: ")
    for letter in word:
        current_index = 0
        if letter == "h":
            print("Find 'h' in position:", current_index)
            exit()
        current_index += 1