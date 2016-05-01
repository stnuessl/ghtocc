# ghtocc - Github Table of Content Creator

Automatically create table of content for your README.md files on github.

## Overview
* [ghtocc - Github Table of Content Creator](README.md#ghtocc---github-table-of-content-creator)
* [Overview](README.md#overview)
    * [Dependencies](README.md#dependencies)
    * [Usage](README.md#usage)
        * [Download the README from a repository](README.md#download-the-readme-from-a-repository)
        * [Specify a local README file](README.md#specify-a-local-readme-file)
    * [Remark](README.md#remark)


## Dependencies

Python 3.x should do. Otherwise there are none. You can simply copy and paste
the raw source (only 1 file) onto your machine and run it!

## Usage

Always checkout 

```
$ python main.py --help
```

### Download the README from a repository 

```
$ python main.py stnuessl/ghtocc
```

which equals

```
$ python main.py https://github.com/stnuessl/ghtocc
```

### Specify a local README file

```
$ python main.py stnuessl/ghtocc /path/to/local/README.md
```

## Remark

Please check the table of content before committing. I bet there are a lot of
corner cases which ghtocc will not consider.
