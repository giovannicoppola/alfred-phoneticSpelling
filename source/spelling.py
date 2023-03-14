#!/usr/bin/env python3
# Tuesday, April 13, 2021, 2:10 PM
# migrated to Python 3 and Alfred 5
#Light rain and snow, mist 🌧   🌡️+34°F (feels +25°F, 92%) 🌬️→13mph 🌗 Tue Mar 14 08:39:42 2023
# W11Q1 – 73 ➡️ 291 – 307 ❇️ 57


import json
import sys
import os
DICTIONARY = 'dictionaries/'+ os.path.expanduser(os.getenv('DICTIONARY', ''))

myInput = sys.argv[1]

myInput = myInput.replace('"', '\"')

myLetters = list(myInput.upper())
def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)

d = {}
with open(DICTIONARY) as f:
    next (f)
    for line in f:
        (key, val) = line.split(" ",1)
        d[key] = val.strip()
        #log (key)
        #print (key)
        #print (d[key])


finalResult=""
result = {"items": []}
for myL in myLetters:
    if myL in d.keys():
        myString = d[myL]
        if myL == " ":
            finalResult = finalResult + myL + ' -- as in Space'+ '\n'
            currItem = f" {myL}  -- as in Space"
            continue
        finalResult = finalResult + myL + ' -- as in ' + d[myL] + '\n'
        currItem = f" {myL} -- as in {d[myL]}"

        result["items"].append({
            "title": f"{currItem}",
            "subtitle": f"",
            "arg": finalResult
                })
    else:
        finalResult = finalResult + myL + ' -- as in ⁉️\n'
        currItem = f" {myL} -- as in ⁉️"

        result["items"].append({
            "title": f"{currItem}",
            "subtitle": f"",
            "arg": finalResult
                })
    
result['variables'] = {"mySpelling": finalResult} 
print (json.dumps(result))
#print (finalResult)



