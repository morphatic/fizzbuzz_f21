'''
Unit tests for the fizzbuzz program
'''

# import the code to be tested
from fizzbuzz import fizz, buzz, fibu

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
        assert fizz(3.0) == 'fizz'
        assert fizz(4) == 4
        assert fizz(9) == 'fizz'
        assert fizz(17) == 17
        assert fizz(15) == 'fizz'
        assert fizz(5) == 5

    def takes_a_numeric_input_and_returns_buzz_if_it_is_a_multiple_of_5():
        '''
        We need a function that can take a single input and that
        returns a value which could either be "buzz" or just whatever
        the input was to begin with.
        '''
        assert buzz(5) == 'buzz'
        assert buzz(5.0) == 'buzz'
        assert buzz(4) == 4
        assert buzz(10) == 'buzz'
        assert buzz(17) == 17
        assert buzz(15) == 'buzz'
        assert buzz(3) == 3

    def takes_a_numeric_input_and_returns_fizzbuzz_if_it_is_a_multiple_of_15():
        '''
        We need a function that can take a single input and that
        returns a value which could either be "fizzbuzz" or just whatever
        the input was to begin with.
        '''
        assert fibu(15) == 'fizzbuzz'
        assert fibu(3) == 3
        assert fibu(4) == 4
        assert fibu(5) == 5

    def passes_non_numeric_inputs_through_as_is():
        '''
        If the input to fizz(), buzz(), and fibu() is non-numeric,
        return the value "as is" without transform
        '''
        assert fizz('abc') == 'abc'
        assert buzz('abc') == 'abc'
        # assert fibu('abc') == 'abc'
