import json

def romanji_to_hirigana(a: str):
    for old, new in {
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
    }:
        a = a.replace(old, new)

def hirigana_to_katakana(a: str):
    pass

def english(seed):
    with open("english-words.json") as f: data = json.loads(f.read())

def russian(seed):
    with open("english-words.json") as f: data = json.loads(f.read())

def japanese_hirigana(seed):
    with open("english-words.json") as f: data = json.loads(f.read())

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