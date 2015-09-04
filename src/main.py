#!/usr/bin/python env

import argparse
import re

def indentation_level_of(s):
    
    cnt = 0
    
    for c in s:
        if c == '#':
            cnt += 1
        else:
            break
    
    return cnt

def sanitize_link(link):
    link = re.sub('[.!?/]', '', link)
    link = link.replace(' ', '-')
    
    return link.lower()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('README', help='path to the README file')
    parser.add_argument('URL', help='URL to the Github respository')
    parser.add_argument('-a', '--append', 
                        help='print the readme after the toc',
                        action='store_true',
                        default=False)
    parser.add_argument('--head', help='', default='# Overview')
    
    args = parser.parse_args()
    
    if not args.URL.startswith('https://github.com/'):
        args.URL = 'https://github.com/{}'.format(args.URL)
    
    readme = open(args.README, mode='r')
    
    print(args.head)

    code = False
    
    for line in readme:
        txt = line.strip()
        
        if len(txt) > 2 and txt[:3] == '```':
            code = not code
        elif len(txt) != 0 and txt[0] == '#' and not code:
            level = indentation_level_of(txt)
            link = txt[level:].strip()
            indent = 4 * (level - 1) * ' '
            
            url = '{}#{}'.format(args.URL, sanitize_link(link))
            
            print('{}* [{}]({})'.format(indent, link, url))

    if args.append:
        readme.seek(0)
        
        for line in readme:
            print(line)

if __name__ == '__main__':
    main()