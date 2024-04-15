import pandas as pd

def hello(w:str) -> None:
    print(f'Hello {w}')

def recursive(w:str) -> int:
    print(f'Hello {w}')
    return 1

hello('World')
