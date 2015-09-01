#!/usr/bin/python env

import argparse

#https://github.com/stnuessl/tq#query-top-played-games

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('README', help='path to the README file')
    parser.add_argument('-u', '--url', help='URL to the Github respository')
    
    args = parser.parse_args()

    readme = open(args.README, mode='r')
    
    code = False

    for line in readme:
        txt = line.strip(' ')
        
        if len(txt) > 2 and txt[:3] == '```':
            code = not code
        elif len(txt) != 0 and txt[0] == '#' and not code:
            cnt = 0
            
            for c in txt:
                if c == '#':
                    cnt += 1
                else:
                    break

            txt = txt[cnt:-1].strip(' ')
            
            if len(txt) != 0:
                intent = cnt * '\t'
                
                url = '{}#{}'.format(args.url, txt.replace(' ', '-'))
                
                print('{}* [{}]({})'.format(intent, txt, url))

    readme.seek(0)
    
    for line in readme:
        print(line)

if __name__ == '__main__':
    main()