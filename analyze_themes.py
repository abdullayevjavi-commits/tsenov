# -*- coding: utf-8 -*-
import pdfplumber, re
from collections import Counter

keywords = []
jels = []
with pdfplumber.open("p3096__BMBook1eng2025_87_101.pdf") as pdf:
    pages = [(p.extract_text() or "") for p in pdf.pages]

full = "\n".join(pages)

for m in re.finditer(r'[Kk]ey ?words?\s*:?\s*(.+)', full):
    kw = re.split(r'JEL', m.group(1))[0]
    keywords.append(kw.strip())

for m in re.finditer(r'JEL\s*:?\s*([A-Z0-9 ,\.;]+)', full):
    jels.append(m.group(1).strip())

print("Pages:", len(pages))
print("'Key words' occurrences:", len(keywords))
print("'JEL' occurrences:", len(jels))

jel_codes = []
for j in jels:
    for code in re.findall(r'[A-Z]\d{1,2}', j):
        jel_codes.append(code)
print("\nTotal JEL codes:", len(jel_codes))
print("JEL by category letter:", Counter(c[0] for c in jel_codes).most_common())
print("Top JEL codes:", Counter(jel_codes).most_common(25))

stop = set("the of and in for a to on with an by from as is are at into using based study "
           "toward towards their its case between within under over more new its this that".split())
words = []
for kw in keywords:
    for w in re.findall(r'[A-Za-z\-]{3,}', kw.lower()):
        if w not in stop:
            words.append(w)
print("\nTop keyword terms:")
for w, c in Counter(words).most_common(45):
    print("  %3d  %s" % (c, w))

print("\nAll keyword lines:")
for k in keywords:
    print("  -", k[:120])
