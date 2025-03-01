import json

with open("prime_table.json") as f: prime_table = json.loads(f.read())

def prime():
    while True:
        for x in prime_table:
            yield x