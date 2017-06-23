from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    """receives a string(text) and an integer(rot) and rotates the string rot amount of times"""
    myAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    newStr = ''
    for char in text:
        newStr += rotate_character(char, rot)

    return newStr



def main():
    from sys import argv, exit
    if len(argv) != 2:
        print('usage: python caesar.py n')
        exit()
    rotation = argv[1]

    if rotation.isdigit() == True:
        string = str(input('Type a message:'))
        print(encrypt(string, int(rotation)))
    else:
        print('usage: python caesar.py n')






if __name__ == '__main__':
    main()
