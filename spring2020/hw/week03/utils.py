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

def calculate_mkey(key, mod=26):
    """
    arguments:
        key (int): represents the multiplicative key
        mod (int, optional): represents the modulus 
    returns
        int: the modular multiplicative inverse of `key`. -1 if there is no inverse
    """
    for i in range(0, mod):
        if (i * key) % mod == 1:
            return i
    return -1