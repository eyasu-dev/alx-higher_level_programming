#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first = ''
    if sentence == '':
        first = 'None'
        return (length, first)
    else:
        length = len(sentence)
        first = sentence[0]
        return (length, first)
