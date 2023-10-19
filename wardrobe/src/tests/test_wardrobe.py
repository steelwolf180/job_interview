from apps.wardrobe import *

def test_wardrobe_length():
    assert get_wardrobe_length() == 150
    
def test_wardrobe_items():
    items = get_wardrobe_items()
    
    assert len(items) == 4
    assert items['50'] == 59
    assert items['75'] == 62
    assert items['100'] == 90
    assert items['120'] == 111

def test_fill_with_single_item():
    items = list(get_wardrobe_items().keys())
    
    assert get_space_left(items, items[0]) == 0
    assert get_space_left(items, items[1]) == 25
    assert get_space_left(items, items[2]) == 50
    assert get_space_left(items, items[3]) == 30
    assert get_space_left(items, '0') == 0
    
def test_calculate_space_left_with_at_least_one():
    items = list(get_wardrobe_items().keys())
    
    assert len(calculate_items_used(items)) >= 1