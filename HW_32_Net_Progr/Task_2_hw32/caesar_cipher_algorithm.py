def caesar_encoder(text, shift):
    """
    This function takes in a string of text and a shift value
    and returns the text encrypted using the Caesar Cipher algorithm.
    """
    result = ""
    # Loop through each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the new character value after the shift
            new_char = chr((ord(char) + shift - 65) % 26 + 65)
            # Append the new character to the result string
            result += new_char
        else:
            # If the character is not a letter, append it unchanged
            result += char
    return result


def caesar_decoder(text, shift):
    """
    This function takes in a string of text that has been encoded
    using the Caesar Cipher algorithm with a given shift value and
    returns the decoded text.
    """
    result = ""
    # Loop through each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the new character value after the shift
            new_char = chr((ord(char) - shift - 65) % 26 + 65)
            # Append the new character to the result string
            result += new_char
        else:
            # If the character is not a letter, append it unchanged
            result += char
    return result


if __name__ == "__main__":
    print(caesar_encoder('HELLO, WORLD!', 3))

    print(caesar_decoder("KHOOR, ZRUOG!", 3))

