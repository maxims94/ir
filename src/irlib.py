#!/usr/bin/python

import re

def get_keywords(str):
      kw = str.split(" ")
      kw = list(filter(lambda x: len(x)>3, map((lambda x: re.sub('[^a-zA-Zöäüß]', '', x.lower().strip())), kw)))
      return kw
