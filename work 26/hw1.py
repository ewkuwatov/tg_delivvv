from typing import Dict

def add_numbers(a: int, b: int) -> Dict[str, int]:
    result = a + b
    return {"operation": "addition", "result": result}

def subtract_numbers(a: int, b: int) -> Dict[str, int]:
    result = a - b
    return {"operation": "subtraction", "result": result}

def multiply_numbers(a: int, b: int) -> Dict[str, int]:
    result = a * b
    return {"operation": "multiplication", "result": result}


print(add_numbers(5, 3))
print(subtract_numbers(10, 4))
print(multiply_numbers(2, 6))
