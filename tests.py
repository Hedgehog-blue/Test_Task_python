from task import LinkedList

def test_examples():
    lst1 = LinkedList()
    for val in [0, 1, 2]:
        lst1.add(val)
    assert lst1.get_element() == 1

    lst2 = LinkedList()
    for val in [0, 1, 2, 3]:
        lst2.add(val)
    assert lst2.get_element() == 1

    lst3 = LinkedList()
    for val in [0, 1, 2, 3, 4]:
        lst3.add(val)
    assert lst3.get_element() == 2

def test_short_list():
    lst = LinkedList()
    lst.add(0)
    assert lst.get_element() is None

def test_empty_list():
    lst = LinkedList()
    assert lst.get_element() is None

if __name__ == "__main__":
    test_examples()
    test_short_list()
    test_empty_list()
    print("✅ All tests passed!")
