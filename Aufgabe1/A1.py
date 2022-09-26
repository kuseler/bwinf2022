import re

def create_regex_from_pattern(pattern):
    re_pattern = "\ ".join(pattern.split(" "))
    re_pattern = re_pattern.replace("_", "\w+")
    comp = re.compile(re_pattern, flags=re.I)
    return comp

def find_all(stoerung, lieblingsbuch):
    comp = create_regex_from_pattern(stoerung)
    return comp.findall(lieblingsbuch)

def main():
    for i in range(6):
        with open("stoerung{}.txt".format(str(i))) as file, open("Alice_im_Wunderland.txt") as base:
            a = file.read()
            b = base.read().lower()
            print(a)
            print(find_all(a,b))


if __name__=="__main__":
    main()
