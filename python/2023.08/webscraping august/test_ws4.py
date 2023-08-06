import pytest

from ws4 import additions, ip_address

def test_equation():
    assert 3==3
    
# def test_fail():
#     assert 3==4
    
@pytest.mark.parametrize("a,b", [(3,6), (1,8)])
def test_addition_ws4(a,b):
    assert additions(a,b) == 3*3   

def test_host_ip():
    assert ip_address() == "192.168.1.16"
         