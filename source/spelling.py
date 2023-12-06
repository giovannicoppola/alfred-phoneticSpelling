#!/usr/bin/env python3
# Tuesday, April 13, 2021, 2:10 PM
# migrated to Python 3 and Alfred 5
# Light rain and snow, mist 🌧   🌡️+34°F (feels +25°F, 92%) 🌬️→13mph 🌗 Tue Mar 14 08:39:42 2023
# W11Q1 – 73 ➡️ 291 – 307 ❇️ 57


import json
import sys
import os
import unicodedata

DICTIONARY = 'dictionaries/'+ os.path.expanduser(os.getenv('DICTIONARY', ''))
WF_BUNDLE = os.getenv('alfred_workflow_bundleid')
CUSTOM_DIC_FOLDER = os.path.expanduser('~')+"/Library/Application Support/Alfred/Workflow Data/"+WF_BUNDLE
CUSTOM_DIC_FILE = f"{CUSTOM_DIC_FOLDER}/custom.txt"

if DICTIONARY == 'dictionaries/custom.txt':
    DICTIONARY = CUSTOM_DIC_FILE

if not os.path.exists(CUSTOM_DIC_FOLDER):
    os.makedirs(CUSTOM_DIC_FOLDER)
if os.path.exists('dictionaries/custom.txt') and not os.path.exists(CUSTOM_DIC_FILE):
    os.rename('dictionaries/custom.txt', CUSTOM_DIC_FILE)


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)


myInput = sys.argv[1]

myInput = myInput.replace('"', '\"')



myInputN = unicodedata.normalize("NFC", myInput)
myLetters = list(myInputN.upper())

#log (myLetters)




d = {}
with open(DICTIONARY) as f:
    next (f)
    for line in f:
        if line.startswith(" "):
            key = '- -'
            val = line.lstrip() 
        else: 
            (key, val) = line.split(" ",1)
        
    
        d[key] = val.strip()
        
        #log (f'key:{key}, value: {val}')
        


finalResult=""
result = {"items": []}
for myL in myLetters:
    #log (myL)
    if myL == " ":
        finalResult = finalResult + myL + ' -- as in Space'+ '\n'
        currItem = f" {myL}  -- as in Space"
        
    elif myL in d.keys():
        myString = d[myL]
        
        finalResult = finalResult + myL + ' -- as in ' + d[myL] + '\n'
        currItem = f" {myL} -- as in {d[myL]}"

    
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


