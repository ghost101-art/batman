print("WELCOME TO MY CREATE TASK PROJECT TITLED 'SIMPLE CIPHER MAKER'")
print("\nThis create task will create two different ciphers")

cipher_choice = int(
    input("Do you want your word to be a shift (please type 1) or turn into symbols (please type 2)?: "))
word = input('What is your word? (all lower case please): ')

if cipher_choice == 1:
    shift_amount = int(input("What is your number of shift? (between 1-26): "))


    def shift(word, num):
        shifted_word = ''
        for char in word:
            if char.isalpha():
                shifted_char = chr((ord(char) - 97 + num) % 26 + 97)
                shifted_word += shifted_char
            else:
                shifted_word += char
        return shifted_word


    print(shift(word, shift_amount))

elif cipher_choice == 2:
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', ']', '{', '}', '|', ':', ';', '"',
               "'", '<', '>', ',', '.', '?', '/']


    def symbols_word(word):
        new_word = ''
        for char in word:
            if char.isalpha():
                symbol = symbols[(ord(char) - 97) % len(symbols)]
                new_word += symbol
            else:
                new_word += char
        return new_word


    print(symbols_word(word))

elif word == '10008$' and cipher_choice == 3:
    riddle = input(
        '\nTell me. It can be cruel, poetic, or blind. But when it\'s denied, it\'s violence you may find?: ')
    if riddle.lower() == 'justice':
        print('\nhttps://www.rataalada.com/')
    else:
        print('BETTER LUCK NEXT TIME BATMAN')

elif word == 'THE BATMAN' and cipher_choice == 3:
    riddle = input(
        '\nTell me. It can be cruel, poetic, or blind. But when it\'s denied, it\'s violence you may find?: ')
    if riddle.lower() == 'justice':
        print('\nhttps://www.rataalada.com/')
    else:
        print('BETTER LUCK NEXT TIME BATMAN')

else:
    print("ERROR: SOMETHING WENT WRONG?!?!?!?!")
