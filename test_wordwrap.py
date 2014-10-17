#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from wordwrap import wordwrap

def test_empty():
    result = wordwrap('', 10)
    assert_equal(result, '')

def test_shortword():
    result = wordwrap('einwort', 10)
    assert_equal(result, 'einwort')

def test_longword():
    result = wordwrap('einganzlangeswort', 10)
    assert_equal(result, 'einganzlangeswort')

def test_twowords():
    result = wordwrap('zwei woerter', 10)
    assert_equal(result, 'zwei\nwoerter')

def test_threewords():
    result = wordwrap("eins zwei drei", 10)
    assert_equal(result, "eins zwei\ndrei")

def test_three_lines():
    result = wordwrap("eins zwei drei vier fuenf", 10)
    assert_equal(result, "eins zwei\ndrei vier\nfuenf")

def test_ten_chars():
    result = wordwrap('0123456789', 10)
    assert_equal(result, '0123456789')

def test_two_long_words():
    result = wordwrap('einganzlangeswort undnocheinesdazu', 10)
    assert_equal(result, 'einganzlangeswort\nundnocheinesdazu')

def test_single_chars():
    result = wordwrap('a b c d e f g h i j k', 10)
    assert_equal(result, 'a b c d e\nf g h i j\nk')

def test_blanks():
    result = wordwrap('                    ', 10)
    assert_equal(result, '')

def test_text_none():
    assert_raises(ValueError, lambda: wordwrap(None, 10))

def test_text_none_2():
    def do_it():
        return wordwrap(None, 10)
    assert_raises(ValueError, do_it)

def test_negative():
    assert_raises(ValueError, lambda: wordwrap('test', -5))

def test_length_none():
    assert_raises(ValueError, lambda: wordwrap('test', None))

def test_many_words():
    result = wordwrap('eins zwei drei view fuenf sechs sieben acht neun', 10)
    assert_equal(result, 'eins zwei\ndrei view\nfuenf\nsechs\nsieben\nacht neun')

def test_startwithblanks():
    result = wordwrap('     word', 10)
    assert_equal(result, 'word')

def test_endwithblanks():
    result = wordwrap('word          ', 10)
    assert_equal(result, 'word')

def test_specialchars():
    result = wordwrap(u'!"§$%&/()=?#+* ~öäü', 10)
    assert_equal(result, u'!"§$%&/()=?#+*\n~öäü')

def test_breaks():
    result = wordwrap('Ein Satz.\nUnd noch ein zweiter Satz.\nEnde.', 15)
    assert_equal(result, 'Ein Satz.\nUnd noch ein\nzweiter Satz.\nEnde.')
