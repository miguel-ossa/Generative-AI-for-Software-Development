import pytest
from stack import Stack

@pytest.fixture
def stack():
    return Stack()

# Pruebas básicas
def test_push(stack):
    stack.push(1)
    assert stack.peek() == 1

def test_pop(stack):
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() is None

def test_peek(stack):
    stack.push(1)
    assert stack.peek() == 1
    stack.pop()
    assert stack.peek() is None

def test_is_empty(stack):
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False

def test_size(stack):
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
    stack.push(2)
    assert stack.size() == 2

# Casos límite e inusuales
def test_push_none(stack):
    stack.push(None)
    assert stack.peek() is None

def test_push_different_types(stack):
    stack.push(1)
    stack.push("string")
    stack.push(3.14)
    assert stack.pop() == 3.14
    assert stack.pop() == "string"
    assert stack.pop() == 1

def test_pop_empty(stack):
    assert stack.pop() is None

def test_peek_empty(stack):
    assert stack.peek() is None

def test_size_on_large_number_of_elements(stack):
    for i in range(10000):
        stack.push(i)
    assert stack.size() == 10000
    for i in range(10000):
        stack.pop()
    assert stack.size() == 0

def test_alternating_push_pop(stack):
    stack.push(1)
    assert stack.pop() == 1
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() is None

def test_long_string(stack):
    long_string = "a" * 10000
    stack.push(long_string)
    assert stack.peek() == long_string
    assert stack.pop() == long_string
    assert stack.is_empty() is True
