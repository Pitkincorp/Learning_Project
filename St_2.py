import sys, re

templ = r"\b[aA]+\b"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(templ,'argh',line,count=1))