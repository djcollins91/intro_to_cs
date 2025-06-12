import math
import pytest
from main import (
    add,
    subtract,
    multiply,
    
    modulus,
    exponentiate,
   
    absolute_value,
    
    power,
    
 )

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5



def test_modulus():
    assert modulus(5, 2) == 1
    assert modulus(9, 3) == 0

def test_exponentiate():
    assert exponentiate(2, 3) == 8
    assert exponentiate(5, 0) == 1


def test_absolute_value():
    assert absolute_value(-5) == 5
    assert absolute_value(3) == 3



def test_power():
    assert power(2, 4) == 16
    assert power(10, 1) == 10



