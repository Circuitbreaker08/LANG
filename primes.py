import json

with open("prime_table.json") as f: prime_table = json.loads(f.read())

def prime():
    gen = prime_generator()
    return next(gen)

def prime_generator():
    while True:
        for x in prime_table:
            yield x