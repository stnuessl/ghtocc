#!/usr/bin/python env

#
# The MIT License (MIT)
# Copyright (c) 2016 stnuessl
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
#

import argparse
import urllib.request
import re
import sys
import base64
import json
import os


class Readme():
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @staticmethod
    def from_path(path):
        name = os.path.basename(path);
        content = open(path, mode='r').read()
        
        return Readme(name, content)
    
    @staticmethod
    def from_json(data):
        content = base64.b64decode(data['content']).decode('utf-8')
    
        return Readme(data['name'], content)
    
    @staticmethod
    def from_url(url):
        url = url.rstrip('/')
        
        # Find user and repository name
        if 'github.com/' in url:
            i = url.find('github.com/') + len('github.com/')
            url = url[i:]
            
        url = 'https://api.github.com/repos/{}/readme'.format(url)
        
        print('URL: {}'.format(url))

        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/vnd.github.v3+json')
    
        data = urllib.request.urlopen(req).read().decode('utf-8')

        return Readme.from_json(json.loads(data))
    
    def name(self):
        return self._name
    
    def content(self):
        return self._content


def indentation_level_of(s):
    return len(s) - len(s.lstrip('#'))

def to_urlpath(s):
    s = re.sub('[.!?/\'+_]', '', s)
    s = s.replace(' ', '-')

    return s.lower()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('README', help='Path or URL to the local README file')
    parser.add_argument('-a', '--append', 
                        help='print the readme after the toc',
                        action='store_true',
                        default=False)
    parser.add_argument('--head', 
                        help='Set the caption for the table of content', 
                        default='## Overview')
    
    args = parser.parse_args()
    
    if os.path.isfile(args.README):
        readme = Readme.from_path(args.README)
    else:
        readme = Readme.from_url(args.README)
    
    print(args.head)

    code = False

    for line in readme.content().splitlines():
        if len(line) > 0 and line[0] == '\t':
            continue
        
        txt = line.strip()
        
        if len(txt) > 2 and txt[:3] == '```':
            code = not code
        elif len(txt) != 0 and txt[0] == '#' and not code:
            level = indentation_level_of(txt)
            name = txt[level:].strip()
            indent = 4 * (level - 1) * ' '
            
            url = '{}#{}'.format(readme.name(), to_urlpath(name))
            
            print('{}* [{}]({})'.format(indent, name, url))

    if args.append:
        print(readme.content())

if __name__ == '__main__':
    main()
