def text_clean( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Arguments:
        text (str): a piece of text for cleaning
    Returns:
        (str): text with only the characters also found in LETTERS
               lower-case letters in text will be made upper-case  
    """
    
    cleaned_text = ''
    
    for character in text:
        if character.upper() in LETTERS:
            cleaned_text += character.upper()
    
    return cleaned_text

def char_to_int( character, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    """
    Arguments:
        character (str): A single character
    Returns:
        (int): the integer representation of the character
    """
    integer = LETTERS.find(character)
    return integer

def int_to_char( integer, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    """
    Arguments:
        integer (int): An integer between 0 and len(LETTERS)
    Returns:
        (str): a single character representation of the integer
    """
    character = LETTERS[integer]
    return character

def text_block( text, size = 5 ):
    """
    Arguments:
        text (str): text to block
        size (int, optional): # of characters in a block
    Returns:
        (str): text blocked into groups of specified size
    """
    
    blocked_text = ''
    
    for character in text:
        if len(blocked_text.replace(' ', '') ) % size == 0 and len(blocked_text) != 0:
            blocked_text += ' '

        blocked_text += character
    
    return blocked_text

def caesar( message, key, encipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    """
    Arguments:
        message (str): either a plaintext or ciphertext
        key (int): key to use
        encipher (bool, optional): when True, encrypts the message
                                   when False, decrypts the message
    Returns:
        (str): the plaintext or ciphertext formatted appropriately
    """
    
    message = text_clean( message )
    output = ''
    
    if encipher == True:
        # encipher the message
        for plaintext_character in message:
            plaintext_numerical = char_to_int( plaintext_character )
            ciphertext_numerical = (plaintext_numerical + key) % 26
            ciphertext_character = int_to_char( ciphertext_numerical )
            output += ciphertext_character
        
        return text_block( output )
    
    else:
        # decipher the message
        for ciphertext_character in message:
            ciphertext_numerical = char_to_int( ciphertext_character )
            plaintext_numerical = (ciphertext_numerical - key) % 26
            plaintext_character = int_to_char( plaintext_numerical )
            output += plaintext_character
        return output.lower()