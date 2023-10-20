def get_wardrobe_length():
    return 150

def get_wardrobe_items():
    return {'50': 59, '75': 62, '100':90, '120': 111}

def get_space_left(items, item):
    if item == '0':
        return 250
    
    elif item == '50':
        return 0
    
    elif item == '75':
        return 25
    
    elif item == '100':
        return 50
    
    elif item == '120':
        return 30
    

def calculate_items_used(items):
    used = []
    while True:
        used.append('')    
        if len(used) >= 1:
            break
    return used