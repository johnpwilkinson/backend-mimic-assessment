#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise
Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all
the words in the file.
Rather than read the file line by line, it's
easier to read it into
one giant string and split it once.
Note: the standard python module 'random' includes a
random.choice(list)
method which picks a random element from a non-empty
list.
You can try adding in line breaks around 70 columns
so the output looks
better.
"""

__author__ = "John Wilkinson, youtube, Daniel Demos, https://www.geeksforgeeks.org/enumerate-in-python/, Udemy Python Course, stackOverflow"

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    # +++your code here+++
    word_dict = {"":[]} #initializing the dict with empty string to take care of first word seed
    with open(filename) as f:
        text = f.read()
        text_to_list = text.split()
        word_dict[""].append(text_to_list[0])
        for num, word in enumerate(text_to_list):
            # prevent index overflow
            if num < len(text_to_list)-1:
                # if word is all ready in dict, then add word that comes after it to its list (value)
                if word in word_dict:
                    word_dict[word].append(text_to_list[num+1])
                else:
                    # if no, then make that word a ket in the dict
                    word_dict[word] = [text_to_list[num+1]]
    for each in word_dict:
        print(each, ":", word_dict[each])
    return word_dict
    


 # """Given a previously created mimic_dict and start_word,
    # prints 200 random words from mimic_dict as follows:
    #     - Print the start_word
    #     - Look up the start_word in your mimic_dict and get its next-list
    #     - Randomly select a new word from the next-list
    #     - Repeat this process 200 times
    # """

def print_mimic(mimic_dict, start_word):
    i=0
    output_text = start_word
    while i<200:
        if start_word in mimic_dict:
            # pick random word from dict
            random_word = random.choice(mimic_dict[start_word])
            # add that word to the output text stream
            output_text += " " + random_word + " "
            # update start_word to current random_word
            start_word = random_word
            # increase iterator
            i+=1
        else:
            start_word = ""
            i+=1
    print(output_text)
    
    


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()