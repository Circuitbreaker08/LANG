import json
import os

os.chdir(os.path.dirname(__file__))

def romanji_to_hirigana(a: str):
    mappings = {
        "chiji": "ちぢ",
        "suzu": "すづ",

        "ka": "か",
        "ki": "き",
        "ku": "く",
        "ke": "け",
        "ko": "こ",

        "ga": "が",
        "gi": "ぎ",
        "gu": "ぐ",
        "ge": "げ",
        "go": "ご",

        "sa": "さ",
        "shi": "し",
        "su": "す",
        "se": "せ",
        "so": "そ",

        "za": "ざ",
        "ji": "じ",
        "zu": "ず",
        "ze": "ぜ",
        "zo": "ぞ",

        "ta": "た",
        "chi": "ち",
        "tsu": "つ",
        "ta": "た",
        "to": "と",

        "da": "だ",
        "di": "ぢ",
        
        "da": "だ",
        "do": "ど",

        "na": "な",
        "ni": "に",
        "nu": "ぬ",
        "ne": "ね",
        "no": "の",
        
        "ha": "は",
        "hi": "ひ",
        "fu": "ふ",
        "he": "へ",
        "ho": "ほ",

        "ba": "ば",
        "bi": "び",
        "bu": "ぶ",
        "be": "べ",
        "bo": "ぼ",

        "pa": "ぱ",
        "pi": "ぴ",
        "pu": "ぷ",
        "pe": "ぺ",
        "po": "ぽ",

        "ma": "ま",
        "mi": "み",
        "mu": "む",
        "me": "め",
        "mo": "も",

        "ya": "や",
        "yu": "ゆ",
        "yo": "よ",

        "ra": "ら",
        "ri": "り",
        "ru": "る",
        "re": "れ",
        "ro": "ろ",

        "wa": "わ",
        "wo": "を",
        "n": "ん",

        "a": "あ",
        "e": "え",
        "i": "い",
        "o": "お",
        "u": "う"
    }
    for old, new in zip(mappings.keys(), mappings.values()):
        a = a.replace(old, new)

    return a

def hirigana_to_katakana(a: str):
    pass

def english(seed):
    with open("english-words.json") as f: data = json.loads(f.read())

def russian(seed):
    with open("english-words.json") as f: data = json.loads(f.read())

def japanese_hirigana():
    with open("english-words.json") as f: data = json.loads(f.read())
    with open("out.txt", "w") as f:
        for x in data:
            f.write(romanji_to_hirigana(x) + "\n")

def japanese_katakana(seed):
    pass

def latin(seed):
    pass

def cyrillic(seed):
    pass

def hirigana(seed):
    pass

def katakana(seed):
    pass

if __name__ == "__main__":
    japanese_hirigana()