from list_iterator import LinkedList, list_comp,make_a_tuple 
import pytest 


def test_our_loop(): 
    peeps = LinkedList(("Pookie","RayRay","BooBoo"))
    peeps_list = [] 
    for folk in peeps:
        peeps_list.append(folk)
    assert peeps_list == ["Pookie","RayRay","BooBoo"] 

def test_adding_nums(): 
    list_nums = LinkedList((50,10,30)) 
    list_total = 0 
    for i in list_nums: 
        list_total += i 
    assert list_total == 90

def test_list_comp(): 
    peeps = LinkedList(("Pookie","RayRay","BooBoo"))
    tall_letters = [folk.upper() for folk in peeps]
    assert tall_letters == ['POOKIE','RAYRAY','BOOBOO'] 

def test_str__(): 
    peeps = LinkedList(["Pookie","RayRay","BooBoo"])
    assert str(peeps) == "[ Pookie ] -> [ RayRay ] -> [ BooBoo ] -> None"

def test_range():
    num_range = range(1, 20 + 1)
    nums = LinkedList(num_range)
    assert len(nums) == 20 

def test_switch_to_tuple(): 
    array = list_comp([10,11,12]) 
    actual = make_a_tuple(array) 
    expected = (11,12,13) 
    assert actual == expected

def test_filter():
    nums = LinkedList(range(1, 11))
    odds = [num for num in nums if num % 2]
    assert odds == [1, 3, 5, 7, 9]