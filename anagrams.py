# encoding: utf-8
# import json
from collections import Counter, defaultdict

def anagram(words):
    anagrams = defaultdict(list)
    for word in words:
        histogram = frozenset(Counter(word).items()) # build a hashable histogram
        anagrams[histogram].append(word)
        #print(histogram)
    a = []    
    for i in list(anagrams.values()):
        if len(i) > 8:
            k = []
            for j in i:
                k.append(str(j))
                #k.append(str(j))
            a.append(k)
    return a
"""
keywords = ("hi", "hello", "bye", "helol", "abc", "cab", 
               "bac", "silenced", "licensed", "declines", "апельсин", "спаниель", 
               "брюква")
               """
keywords = []
#with open("russian.txt", "r", encoding="utf-8") as wordsfile:
with open("hywiktionary-latest-all-titles-in-ns0-2020-10-20-armenian-only.txt", "r", encoding="utf-8") as wordsfile:
#with open("word_rus.txt", "r", encoding="utf-8") as wordsfile:
    for line in wordsfile:
        if len(line.strip()) >= 1:
            keywords.append(line.strip())
result = anagram(keywords)
#print(result)
for i in result:
    if i[0][0] != i[1][0]:
        print(i)
#j_res = json.dumps(result, ensure_ascii=False).encode('utf8')
#j_res = json.dumps(result)

# with open("out.txt", "w", encoding="utf-8") as file:
#     file.write(str(j_res))

with open("out.txt", "w", encoding="utf-8") as file:
    for i in result:
        for j in i:
            file.write(j + " ")
        file.write("\n")