import pytest

from ws4 import additions, ip_address, myUpper, gameCharacter

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
    
def test_Aatrox():
    character_Aatrox = gameCharacter(1000, 20, 50, ("Warrior", "Darkin"))
    character_Teemo = gameCharacter(600, 100, 40, (10))
    assert character_Aatrox.health == 1000 and character_Teemo.traits == 10
    
         