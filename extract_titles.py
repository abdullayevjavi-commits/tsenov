# -*- coding: utf-8 -*-
import pdfplumber, re

with pdfplumber.open("p3096__BMBook1eng2025_87_101.pdf") as pdf:
    pages = [(p.extract_text() or "") for p in pdf.pages]
full = "\n".join(pages)
lines = full.split("\n")

# A title precedes the author block and an "Abstract:" within ~25 lines.
titles = []
for i, ln in enumerate(lines):
    if ln.strip().startswith("Abstract"):
        # look back up to 20 lines for an all-caps title block
        block = []
        for j in range(i-1, max(i-22, 0), -1):
            s = lines[j].strip()
            if not s:
                if block:
                    break
                continue
            letters = re.sub(r'[^A-Za-z]', '', s)
            if letters and sum(c.isupper() for c in letters)/len(letters) > 0.7 and len(s) > 8:
                block.append(s)
            elif block:
                break
        if block:
            titles.append(" ".join(reversed(block)))

seen = set(); uniq = []
for t in titles:
    key = re.sub(r'\s+', ' ', t).strip()
    if key not in seen and len(key) > 12:
        seen.add(key); uniq.append(key)

print("Detected article titles (%d):\n" % len(uniq))
for t in uniq:
    print(" -", re.sub(r'\s+', ' ', t)[:140])
