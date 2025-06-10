import math
import pytest

from lab1 import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    exponentiate,
    floor_divide,
    absolute_value,
    square_root,
    power,
    logarithm,
    factorial,
    gcd,
    lcm,
    is_prime,
)

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-2, -2) == 0
   

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5
    

def test_modulus():
    assert modulus(5, 2) == 1
    assert modulus(10, 3) == 1
   
    with pytest.raises(ZeroDivisionError):
        modulus(1, 0)

def test_exponentiate():
    assert exponentiate(2, 3) == 8
    assert exponentiate(5, 0) == 1

    assert exponentiate(9, 0.5) == 3

def test_floor_divide():
    assert floor_divide(7, 2) == 3
    assert floor_divide(-7, 2) == -4
    with pytest.raises(ZeroDivisionError):
        floor_divide(1, 0)

def test_absolute_value():
    assert absolute_value(5) == 5
    assert absolute_value(-5) == 5
    assert absolute_value(0) == 0
   

def test_square_root():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root(9) == 3
   

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -2) == 0.25
   

def test_logarithm():
    assert logarithm(8, 2) == 3
    assert logarithm(100, 10) == 2

    with pytest.raises(ValueError):
        logarithm(-1, 2)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    with pytest.raises(ValueError):
        factorial(-1)

def test_gcd():
    assert gcd(54, 24) == 6
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
   

def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0
    

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    