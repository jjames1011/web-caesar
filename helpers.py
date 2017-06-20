def alphabet_position(letter):
    """recieves a letter and returns the 0-based numerical position """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    for char in alphabet:
        if char == letter:
            return alphabet.find(char)



def rotate_character(char, rot):
    """recieves a character, and an integer, and rotates through the alphabet from char rot amount of times."""
    #make sure its a string
    char = str(char)
    #make string lower
    lowerChar = char.lower()
    myalphabet = 'abcdefghijklmnopqrstuvwxyz'
    #if not a letter:
    if char.lower() not in myalphabet:
        return char

    #find the current index of the letter and add rot to that
    index = myalphabet.find(lowerChar)

    rotate = index + rot
    #if rotate is > 26 then use modulo to loop back around
    if rotate >= 26:
        rotate = rotate % 26

    #if the original input char was uppercase then make the new output uppercase aswell
    if char == char.upper():
        upperCase = myalphabet[rotate].upper()
        return upperCase

    return myalphabet[rotate]
