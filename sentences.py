"""
I added code to add adjectives
"""


#imports
from random import choice

cookbook = {'a':["single","past"],
            'b':["single","present"],
            'c':["single","future"],
            'd':["plural","past"],
            'e':["plural","present"],
            'f':["plural","future"]}

#Functions
def get_adjective():
    return choice(["blue","red","green","white","spotted"])

def get_preposition():
    return choice(["inside","around"])

def get_verb(amount, tence):
    if amount == "single":
        if tence == "past":
            return choice(['ran','walked','jumped'])
        elif tence == "present":
            return choice(['runs','walks','jumps'])
        else:
            return f'will {choice(["run","walk","jump"])}'

    elif amount == "plural":
        if tence == "past":
            return  choice(['ran','walked','jumped'])
        elif tence == "present":
            return choice(['run','walk','jump'])
        else:
            return  f'will {choice(["run","walk","jump"])}'
    else:
        return "Error"

def get_noun(amount):
    if amount == "single":
        return choice(["dog","cat","rat"])
    else:
        return choice(["dogs","cats","rats"])

def get_adj_noun(amount):
    noun = get_noun(amount)
    adjective = get_adjective()
    return f'{adjective} {noun}'


def get_determiner(amount):
    if amount == "single":
        return choice(["the","one",'a'])
    else:
        return choice(["the","two","many"])

def get_prepositional_phrase(amount):
    preposition = get_preposition()
    determiner = get_determiner(amount)
    adj_noun = get_adj_noun(amount)
    return f'{preposition} {determiner} {adj_noun}'

def make_sentence(amount, tence):
    determiner = get_determiner(amount)
    adj_noun = get_adj_noun(amount)
    verb = get_verb(amount, tence)
    phrase = get_prepositional_phrase(amount)
    return f'{determiner} {adj_noun} {verb} {phrase}'

def main(index):
    for i in index:
        amount, tence = index[i]
        sentence = make_sentence(amount, tence)
        print(f'{i}: {sentence}')

#Main Block
main(cookbook)
