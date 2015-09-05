#!/usr/bin/python env

import argparse
import urllib.request
import re
import sys

def indentation_level_of(s):
    return len(s) - len(s.lstrip('#'))

def to_urlpath(s):
    s = re.sub('[.!?/]', '', s)
    s = s.replace(' ', '-')

    return s.lower()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('README', help='path to the README file')
    parser.add_argument('URL', help='URL to the Github respository')
    parser.add_argument('-a', '--append', 
                        help='print the readme after the toc',
                        action='store_true',
                        default=False)
    parser.add_argument('--head', help='', default='# Overview')
    parser.add_argument('--debug', 
                        help='enable debug output (makes toc unusable)',
                        action='store_true')
    
    args = parser.parse_args()
    
    if not args.URL.startswith('http'):
        if args.debug:
            print('*WARNING*: expected \'https://github.com/\' prefix in \'{}\'- prepending it now'.format(args.URL), file=sys.stderr)
        args.URL = 'https://github.com/{}'.format(args.URL)
    
    if args.debug:
        d = { True : 'On', False : 'Off' }
        
        print('--------------------------------------')
        print('README : \'{}\''.format(args.README))
        print('URL    : \'{}\''.format(args.URL))
        print('Head   : \'{}\''.format(args.head))
        print('Append : {}'.format(d[args.append]))
        print('Debug  : {}'.format(d[args.debug]))
        print('--------------------------------------')

    path = args.README
    
    if path.startswith('http') or path.startswith('www'):
        if args.debug:
            print('*INFO*: fetching README from remote host')
            
        path, _ = urllib.request.urlretrieve(readme)

    readme = open(path, mode='r')

    print(args.head)

    code = False

    for line in readme:
        txt = line.strip()
        
        if len(txt) > 2 and txt[:3] == '```':
            code = not code
        elif len(txt) != 0 and txt[0] == '#' and not code:
            level = indentation_level_of(txt)
            name = txt[level:].strip()
            indent = 4 * (level - 1) * ' '
            
            url = '{}#{}'.format(args.URL, to_urlpath(name))
            
            print('{}* [{}]({})'.format(indent, name, url))

    if args.append:
        readme.seek(0)
        
        for line in readme:
            print(line)

if __name__ == '__main__':
    main()
