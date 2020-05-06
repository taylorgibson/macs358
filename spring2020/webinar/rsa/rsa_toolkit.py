def charToBinary(char):
    if len(char)>1:
        char = char[0]
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return '{:06b}'.format( ord(char) - 65 )
    elif char in 'abcdefghijklmnopqrstuvwxyz':
        return '{:06b}'.format( ord(char) - 71 )
    elif char in '0123456789':
        return '{:06b}'.format( ord(char) + 4 )
    elif char == '+':
        return '{:06b}'.format( 62 )
    elif char == '/':
        return '{:06b}'.format( 63 )
    else:
        return ''
    
def binaryToChar(binary):
    binary = binary.replace(' ','')
    if len(binary) < 6:
        binary = binary.zfill(6)
    if len(binary) > 6:
        return ''
    num = int(binary,2)
    if (num >= 0) and (num <= 25):
        return chr(num + 65)
    elif (num >= 26) and (num <= 51):
        return chr(num + 71)
    elif (num >= 52) and (num <= 61):
        return chr(num - 4)
    elif num == 62:
        return '+'
    elif num == 63:
        return '/'
    else:
        return ''
    
def text_to_integer( text ):
    """
    Arguments:
      text (str): a string containing base64 characters
    
    Returns:
      (int): an integer representation of text
    """
    binaryMessage = ''
    for char in text:
        binaryMessage += charToBinary(char)
    return int(binaryMessage, 2)

def integer_to_text( integer ):
    """
    Arguments:
      integer (int): an integer that represents a base64 message
    
    Returns:
      (str): a string that contains the base64 characters
    """    
    text = ''
    binary = '{0:b}'.format(integer)
    while len(binary) % 6 != 0:
        binary = '0' + binary
    for i in range(0, len(binary), 6):
        text += binaryToChar( binary[i:i+6] )
    return text

def gcd(x, y): 
    """
    Arguments:
        x (int): an integer
        y (int): an integer
    Returns:
        (int): the greatest commond divisor of x and y
    """
    while(y): 
        x, y = y, x % y 
  
    return x

def egcd(a, b):
    """
    Performs the Extended Euclidean Algorithm on inputs a and b
    
    Arguments:
        a (int): an integer
        b (int): an integer
    Returns:
        (list): a list of 3 integers (g, y, x) where g is the gcd(a,b) and y and x are the coefficients such that gcd(a,b) = ax + by
    """    
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(e, n):
    """
    Arugments:
      e (int): represents a value in modulo n
      n (int): represents the modulus in which you are working
    Returns:
      (int): if e has a multiplicative inverse in mod n, then this value will be return
      (str): if e does NOT have a multiplicative inverse in mod n, the empty string will be returned
    """
    g, x, y = egcd(e, n)
    if g != 1:
        return ''
    else:
        return x % n