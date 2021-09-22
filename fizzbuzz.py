'''
A fizzbuzz program
'''

def fizz(x):
  '''
  Takes a single input, returns 'fizz' if that
  input is a multiple of 3, and just returns the
  input "as is" if it is not a multiple of 3.
  '''
  return 'fizz' if x % 3 == 0 else x
