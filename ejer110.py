import random

def generar_anagrama(p: str) -> str:
    return ''.join(random.sample(p, k=len(p)))
