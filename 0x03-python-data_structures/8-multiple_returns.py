#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        length, first = 0, None
    else:
        length, first = len(sentence), sentence[0]
    return (length, first)
