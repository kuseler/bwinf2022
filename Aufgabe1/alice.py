#!/usr/bin/env python3

# Für die Übergabe von Kommandozeilenargumenten
import sys

# für reguläre Ausdrücke
import re

if len(sys.argv) != 3:
    print("Benutzung: alice.py <Lückentext> <Lieblingsbuch>")
    sys.exit(0)

def create_regex_from_gap_text(gap_text):
    re_gap_text = gap_text.replace(" ","\ ")
    re_gap_text = re_gap_text.replace("_", "\w+") # w+ steht für [jeder Buchstabe] mindestens ein mal
    print(re_gap_text)
    regex = re.compile(re_gap_text, flags=re.I)   
    return regex

def find_all_results(stoerung, lieblingsbuch):
    regex = create_regex_from_gap_text(stoerung)
    return regex.findall(lieblingsbuch)

def main():
    with open(sys.argv[1]) as gap_text, open(sys.argv[2]) as favourite_book:
        gap_str = gap_text.read()
        source_str= favourite_book.read()
        print(find_all_results(gap_str,source_str))

if __name__=="__main__":
    main()
