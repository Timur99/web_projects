import pandas as pd

def hello(w:str) -> None:
    print(f'Hello {w}')

def recursive(w:str) -> None:
    print(f'Hello {w}')
    recursive()

hello('World')
