#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymisp import PyMISP
from keys import misp_url, misp_key, misp_verifycert
import argparse
import os
import json
import re

# Usage for pipe masters: ./last.py -l 5h | jq .

proxies = {
    'http': 'http://127.0.0.1:8123',
    'https': 'http://127.0.0.1:8123',
}

proxies = None


def init(url, key):
    return PyMISP(url, key, misp_verifycert, 'json', proxies=proxies)


def get_event(m, event):
    result = m.get_event(event)
    return result

def rules(types=['meta']):
    r = []
    for t in types:
        rule_file = os.path.join(rule_path, "{0}{1}".format(t,".json"))
        f = open(rule_file)
        r.append(json.load(f))
        f.close()
    return r

def apply_rules(rules=None, event=None, lang='en', format='markdown'):
    if (rules is None) or (event is None):
        return False
    metadata = {}
    pre = ''
    output = ''
    # meta
    for key in rules[0]['fields']:
        r = rules[0]['fields'][key][lang]
        r = replace_event(event=event, string=r)
        if not re.search(':', key):
            output += '{}'.format(str(r).format(event['Event'][key]))
        else:
            (k, v) = key.split(':')
            output += '{}'.format(str(r).format(event['Event'][k][v]))
        if key in rules[0]['metadata']:
            metadata[rules[0]['metadata'][key]] = event['Event'][key]
        output += '\n'
    for k in metadata:
        if k == 'title':
            pre = '# {}'.format(metadata[k].replace('\n', ' ').replace('\r', ''))
        pre += '\n'

    pre += "\n{}".format(output)
    return pre

def replace_event(event=None, string=None):
    if (event is None) or (string is None):
        return False
    values = (re.findall ( '%(.*?)%', string, re.DOTALL))
    for v in values:
        string = re.sub('%{0}%'.format(v), event['Event'][v], string)
    return string

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Create a human-readable report out of a MISP event')
    parser.add_argument("-e", "--event", required=True, help="Event ID to get.")
    parser.add_argument("-f", "--format", default="markdown", help="output format, default is markdown")
    parser.add_argument("-l", "--lang", default="en", help="output language, default is en")

    args = parser.parse_args()
    rule_path = '../rules/'

    misp = init(misp_url, misp_key)

    print(apply_rules(rules=rules(),event=get_event(misp, args.event)))
