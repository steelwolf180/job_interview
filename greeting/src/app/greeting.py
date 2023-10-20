def get_greeting(name):
    display = 'Hello, '
    
    if type(name) is list and len(name) == 2:
        return display + name[0] + ' and ' + name[1]
    
    elif name.isupper() is True:
        return display.upper() + name
    
    elif len(name) == 0:
        return display + 'my friend'
    
    else:
        return display + name