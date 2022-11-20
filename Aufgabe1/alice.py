#!/usr/bin/env python3

# Für die Übergabe von Kommandozeilenargumenten
import sys

# für reguläre Ausdrücke
import re

def convert_gap_text_to_regex(gap_text):
    """
Converts a gap text to a precompiled regular expression
    """
    re_gap_text = gap_text.strip()
    re_gap_text = re_gap_text.replace(" ","\ ") 
    re_gap_text = re_gap_text.replace("_", "\w+")
    return re.compile(re_gap_text)

def tidy_up_source_book(source_book):
    """
Eliminates special Characters and converts any whitespace to a space char
    """
    clean_source = re.sub("[,.:!?;»«_]*", "", source_book)
    clean_source = re.sub("\s+", " ", clean_source)
    clean_source = clean_source.lower()
    return clean_source
    

def find_all_results(interference, favourite_book):
    """
This function mends the other two into a function that outputs all matches.
    """
    regex = convert_gap_text_to_regex(interference)
    book = tidy_up_source_book(favourite_book)
    return list(set(regex.findall( book)))


def main():
    if len(sys.argv) != 3:
        print("Benutzung: alice.py <Lückentext> <Lieblingsbuch>")
        sys.exit(0)

    with open(sys.argv[1]) as gap_text, open(sys.argv[2]) as favourite_book:
        gap_str = gap_text.read()
        source_str= favourite_book.read()
        print(find_all_results(gap_str,source_str))

if __name__=="__main__":
    main()
