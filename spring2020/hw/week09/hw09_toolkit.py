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