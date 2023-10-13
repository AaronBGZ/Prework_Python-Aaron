#test_calculator uch more simple
import pytest
from Hcalculator import square

def test_positive():
  assert square(2) == 4
def test_negative():
  assert square(-2) == 4
def test_zero(): 
  assert square(0) == 0
def test_str():
  with pytest.raises(TypeError):
    square("cat")