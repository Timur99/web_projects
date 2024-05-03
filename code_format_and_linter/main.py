import pandas as pd

def hello(w:str) -> None:
    print(f'Hello {w}')

def recursive(number:int) -> int:
    if number == 0:
        return 1
    else:
        return number + recursive(number - 1)

hello('World')
