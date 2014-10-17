#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wordwrap(text, length):
    if not isinstance(text, basestring):
        raise ValueError('Not a string!')
    elif length <= 0:
        raise ValueError('Negative Value!')

    return "\n".join([_linewrap(line, length) for line in text.split("\n")])


def _linewrap(text, length):
    words = text.split() # split line into words
    temp = ""
    result = []

    for word in words:
        if temp=="" or len(temp + " " + word) <= length:
            temp += " " + word; # add word to line
        else:
            result.append(temp.strip())
            temp = word  # start new line

    if len(temp) != 0:
        result.append(temp.strip())

    return "\n".join(result)

if __name__ == '__main__':
    import nose
    nose.main()
