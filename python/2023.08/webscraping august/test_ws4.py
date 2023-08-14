import pytest
from ws4 import additions, ip_address, myUpper, gameCharacter, NumberAlgo

def test_equation():
    assert 3==3

# parametrization  
@pytest.mark.parametrize("a,b", [(3,6), (1,8)])
def test_addition_ws4(a,b):
    assert additions(a,b) == 3*3   

def test_host_ip():
    assert ip_address() == "192.168.1.16"

@pytest.mark.parametrize("word", [("gold"), ("POLITE"), ("NeIghborhood"), ("Last time i saw you")])
def test_myUpper(word):
    assert myUpper(word).isupper()
    
def test_character():
    character_1 = gameCharacter(1000, 20, 50, ("Warrior", "Darkin"))
    character_2 = gameCharacter(600, 100, 40, ("Yordle", "Cruel"))
    assert (character_1.health == 1000) and ("Cruel" in character_2.traits) 

@pytest.mark.parametrize("my_list", [[102,50,45,87,12,3,17,94], [105,50,45,87,12,3,17,94]])
def test_NumberAlgo(my_list):
    test_list = NumberAlgo(my_list)
    assert test_list.max() == 102 and test_list.min() == 3 and test_list.avg() == 51.25
