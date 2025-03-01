from primes import prime

def characterset(seed: int) -> dict:
    match (seed * prime()) % 4:
        case 0:
            script = "latin"
        case 1:
            script = "cyrillic"
        case 2:
            script = "hirigana"
        case 3:
            script = "katakana"

    return {
        "script": script
    }

def nouns(seed: int) -> dict:
    match (seed * prime()) % 2:
        case 0:
            cased = True
        case 1:
            cased = False

    declensions_num = (seed * prime()) % 6 + 1

    return {
        "cased": cased,
        "declensions_num": declensions_num
    }

def pronouns(seed: int) -> dict:
    match (seed * prime()) % 2:
        case 0:
            gendered = True
        case 1:
            gendered = False

    num_demonstratives = (seed * prime()) % 4 + 1
    return {
        "gendered": gendered,
        "num_demonstratives": num_demonstratives
    }

def verbs(seed: int) -> dict:
    return {}

def adjectives(seed: int) -> dict:
    return {}