#!/usr/bin/env python

import re

with open('./session_names.txt') as f:
    lines = f.read().splitlines()

    lines_processed = []
    
    for session in lines:
        session = re.sub(r'\s','_',session)
        session = re.sub(r'[#{}(),\!\.&]','_',session)
        session = re.sub(r'\'','',session)
        session = re.sub(r'\[','',session)
        session = re.sub(r'\]','',session)
        lines_processed.append(session)
        print session 
