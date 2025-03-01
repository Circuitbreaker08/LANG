import hashlib

import grammatical_archetype

seed = int(hashlib.sha512(input("Enter Language Seed: ").encode()).hexdigest(), base=16)

archetype_collection = {
    "characterset": grammatical_archetype.characterset(seed),
    "nouns": grammatical_archetype.nouns(seed),
    "pronouns": grammatical_archetype.pronouns(seed),
    "verbs": grammatical_archetype.verbs(seed),
    "adjectives": grammatical_archetype.adjectives(seed),
}

print(seed)