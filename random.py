import random


def gen(a, b, n):
    i = 0
    while i < n:
        yield random.choice(a)  + random.choice(b)
        i += 1


for i in gen(["hard", "ball"], ["Alan", "Ajinjal", "cat"],  5):
    print(i)
