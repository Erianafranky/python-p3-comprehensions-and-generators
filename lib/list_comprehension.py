#!/usr/bin/env python3
"""
function return_evens() returns empty list when num_list has no evens
function return_evens() returns evens from num_list
function make_exclamation() returns empty list when sentence_list is empty
function make_exclamation() returns list of sentences with exclamation marks
"""
def return_evens(num_list):
    even_lc = [n for n in num_list if n % 2 == 0]
    return even_lc

def make_exclamation(sentence_list):
    exclamation_lc = [f"{n}!" for n in sentence_list]
    return exclamation_lc
print(make_exclamation(["I like computers", "I require coffee", "Live long and prosper"]))