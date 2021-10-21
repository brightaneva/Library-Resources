from PyDictionary import PyDictionary


def dictionary(term):

    syno = PyDictionary().synonym(term)
    anto = PyDictionary().antonym(term)
    mean = PyDictionary().meaning(term)
    
    return {
        "noun": mean["Noun"],
        "verb": mean["Verb"],
        "synonyms": syno,
        "antonym": anto,
    }

def trans(term,lang):
    return PyDictionary().translate(term,lang)

