'''
Unit tests for the fizzbuzz program
'''

# import the code to be tested
from fizzbuzz import fizz

def describe_a_fizzbuzz_program_that():

    def has_a_smoke_test():
        '''
        The purpose of a smoke test is to give us
        confidence that our testing infrastructure
        is set up correctly. We do that by creating
        a test that should ALWAYS pass.
        '''
        assert True

    def takes_a_numeric_input_and_returns_fizz_if_it_is_a_multiple_of_3():
        '''
        We need a function that can take a single input and that
        returns a value which could either be "fizz" or just whatever
        the input was to begin with.
        '''
        assert fizz(3) == 'fizz'
        assert fizz(4) == 4
        assert fizz(9) == 'fizz'
        assert fizz(17) == 17
