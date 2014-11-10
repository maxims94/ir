#!/usr/bin/python3

import json
import re
import irlib


def learnData(): 
    with open('database', 'r') as f:
        db = json.load(f)

    rules = {}

    for item in db:
        if not "class" in item:
            continue

        if item["class"] == 1:
            kw = irlib.get_keywords(item['title'])

            for k in kw:
                if k in rules:
                    rules[k] += 1
                else:
                    rules[k] = 1

    print("Rules:")
    print(rules)

    print("Save to file 'rules'.")

    with open('rules', 'w') as f:
        json.dump(rules, f)
