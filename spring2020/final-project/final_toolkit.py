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

def multiplicative( message, m_key, encipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    """
    Arguments:
        message (str): either a plaintext or ciphertext
        m_key (int): multiplicative key
        encipher (bool, optional): when True, encrypts the message
                                   when False, decrypts the message
    Returns:
        (str): the plaintext or ciphertext formatted appropriately
    """
    
    message = text_clean( message )
    output = ''
    
    m_inverse = calculate_mkey( m_key )
    
    if m_inverse == -1:
        return ('Invalid Key')
    
    if encipher == True:
        # encipher the message
        for plaintext_character in message:
            plaintext_numerical = char_to_int( plaintext_character )
            ciphertext_numerical = (plaintext_numerical * m_key) % 26
            ciphertext_character = int_to_char( ciphertext_numerical )
            output += ciphertext_character
        
        return text_block( output )
    
    else:
        # decipher the message
        for ciphertext_character in message:
            ciphertext_numerical = char_to_int( ciphertext_character )
            plaintext_numerical = (ciphertext_numerical * m_inverse) % 26
            plaintext_character = int_to_char( plaintext_numerical )
            output += plaintext_character
        return output.lower()

def affine( message, m_key, a_key, encipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    """
    Arguments:
        message (str): either a plaintext or ciphertext
        m_key (int): multiplicative key
        a_key (int): additive key
        encipher (bool, optional): when True, encrypts the message
                                   when False, decrypts the message
    Returns:
        (str): the plaintext or ciphertext formatted appropriately
    """
    
    message = text_clean( message )
    output = ''
    
    m_inverse = calculate_mkey( m_key )
    
    if m_inverse == -1:
        return ('Invalid Key')
    
    if encipher == True:
        # encipher the message
        for plaintext_character in message:
            plaintext_numerical = char_to_int( plaintext_character )
            ciphertext_numerical = (plaintext_numerical * m_key + a_key) % 26
            ciphertext_character = int_to_char( ciphertext_numerical )
            output += ciphertext_character
        
        return text_block( output )
    
    else:
        # decipher the message
        for ciphertext_character in message:
            ciphertext_numerical = char_to_int( ciphertext_character )
            plaintext_numerical = ((ciphertext_numerical - a_key) * m_inverse) % 26
            plaintext_character = int_to_char( plaintext_numerical )
            output += plaintext_character
        return output.lower()

def trithemius_keygen(text, offset, step, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    
    text = text_clean(text)
    running_key = ''
    
    i = offset
    
    while len( running_key ) < len( text ):
        running_key += LETTERS[i]
        i = (i + step) % len(LETTERS)
    
    return running_key

def vigenere_keygen(text, keyword, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    
    text = text_clean(text)
    keyword = text_clean(keyword)
    running_key = ''
    
    i = 0
    
    while len( running_key ) < len( text ):
        running_key += keyword[i]
        i = (i + 1) % len(keyword)
    
    return running_key

def tabula_recta( text, key, encipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Arguments:
      text (str): represent a single letter
      key (str): represent a single letter
      encipher (bool, optional): determines if encipher (True) or decipher (False)
      LETTERS (str, optional): alphabet that the text is written in
    Return:
      string
    """
    
    text = text_clean( text )
    key = text_clean( key )
    
    if encipher == True:
        numerical_plaintext = char_to_int(text)
        numerical_key = char_to_int( key )
        numerical_ciphertext = ( numerical_plaintext + numerical_key) % len( LETTERS )
        ciphertext = int_to_char( numerical_ciphertext )
        
        return ciphertext
    
    else:
        numerical_ciphertext = char_to_int(text)
        numerical_key = char_to_int(key)
        numerical_plaintext = ( numerical_ciphertext - numerical_key) % len( LETTERS )
        plaintext = int_to_char( numerical_plaintext )
        return plaintext

def trithemius( text, offset, step, encipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    text = text_clean(text)
    running_key = trithemius_keygen(text, offset, step)
    
    output = '' 
    
    if encipher:
        for i in range(0, len(text)):
            output += tabula_recta( text[i], running_key[i], True, LETTERS )
        
        return text_block(output)
    else:
        for i in range(0, len(text)):
            output += tabula_recta( text[i], running_key[i], False, LETTERS )
        
        return output.lower()

def vigenere(text, keyword, encipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    running_key = vigenere_keygen(text, keyword)
    
    output = '' 
    
    if encipher:
        for i in range(0, len(text)):
            output += tabula_recta( text[i], running_key[i], True, LETTERS )
        
        return text_block(output)
    else:
        for i in range(0, len(text)):
            output += tabula_recta( text[i], running_key[i], False, LETTERS )
        
        return output.lower()
    
def autokey( text, primer, encipher = True, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    running_key = text_clean(primer)
    
    output = ''
    
    if encipher:
        for i in range(0, len(text)):
            running_key += text[i]
            output += tabula_recta( text[i], running_key[i], True, LETTERS)
        
        return text_block(output)
    else:
        for i in range(0, len(text)):
            output += tabula_recta( text[i], running_key[i], False, LETTERS)
            running_key += output[i]
        
        return output.lower()

def character_frequency( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    text = text_clean( text )
    frequency_list = []
    # Your code goes below here
    length = len(text)

    for char in LETTERS:
        frequency_list.append( text.count(char) / length ) 
    
    # Your code goes above here
    return frequency_list

def character_count( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    text = text_clean( text )
    values = []
    
    for char in LETTERS:
        values.append( text.count(char) )
    
    return values

def expected_count(text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    length = len(text)
    output = []
    dist = [0.08167, 0.01492, 0.02202, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.01292, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09356, 0.02758, 0.00978, 0.02560, 0.00150, 0.01994, 0.00077]    
    
    for i in dist:
        output.append( i*length )

    return output

def chi_squared_score( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean( text )
    norm_errors = []
    expected = expected_count( text )
    actual = character_count( text )
        
    for i in range(0, len(LETTERS)):
        norm_errors.append( (actual[i] - expected[i])**2 / expected[i] )
    
    return sum(norm_errors)

def caesar_scorer( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    
    text = text_clean( text )
    list_of_scores = []
    
    for key in range(0, len(LETTERS)):
        candidate = caesar( text, key, False )
        list_of_scores.append( chi_squared_score( candidate ) )
    
    return list_of_scores

def index_of_coincidence( text, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text_clean(text)
    
    the_count = character_count( text, LETTERS )
    
    ioc = 0
    n = len(text)
    
    for i in the_count:
        ioc += (i / n) * ((i-1)/(n-1))
    
    return ioc

def text_split( text, num_of_groups ):
    text = text_clean(text)
    groups_of_text = ['']*num_of_groups
      
    for i in range(0, len(text)):
        groups_of_text[i % num_of_groups] += text[i]
    
    return groups_of_text

def get_keyword_length( ciphertext, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    ciphertext = text_clean( ciphertext )
    
    guessed_length = 1
    average_ioc = 0
    
    while average_ioc < 0.06:
        ioc_total = 0
        groups = text_split( ciphertext, guessed_length)
        
        for group in groups:
            ioc_total += index_of_coincidence(group)
        
        average_ioc = ioc_total / guessed_length
        guessed_length += 1
    
    return guessed_length - 1

def get_keyword( ciphertext, keylength, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    ciphertext = text_clean( ciphertext )
    keyword = ''
    groups = text_split( ciphertext, keylength )
    
    for group in groups:
        caesar_scores = caesar_scorer(group)
        lowest_score = min( caesar_scores )
        key_value = caesar_scores.index(lowest_score)
        keyword += int_to_char( key_value )
    
    return keyword

def crack_vigenere( ciphertext, LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    ciphertext = text_clean( ciphertext )
    keyword_length = get_keyword_length( ciphertext )
    keyword = get_keyword( ciphertext, keyword_length )
    
    return vigenere(ciphertext, keyword, False)