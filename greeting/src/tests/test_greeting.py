from app.greeting import *

def test_greeting():
    name = 'bob'
    assert 'Hello, bob' == get_greeting(name)

def test_no_name():
    name = ''
    assert 'Hello, my friend' == get_greeting(name)

def test_greeting_isupper():
    name = 'BOB' 
    assert get_greeting(name).isupper() is True 
    
def test_greeting_use_two_names():
    name = ['Jill', 'Jane']
    assert 'Hello, Jill and Jane' in get_greeting(name)