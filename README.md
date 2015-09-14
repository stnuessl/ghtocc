# Overview
* [ghtocc - Github Table of Content Creator](https://github.com/stnuessl/ghtocc#ghtocc---github-table-of-content-creator)
    * [Dependencies](https://github.com/stnuessl/ghtocc#dependencies)
    * [Usage](https://github.com/stnuessl/ghtocc#usage)
        * [Download the README from a repository and create a table of content](https://github.com/stnuessl/ghtocc#download-the-readme-from-a-repository-and-create-a-table-of-content)
        * [Specify a local README file and create a table of content](https://github.com/stnuessl/ghtocc#specify-a-local-readme-file-and-create-a-table-of-content)
        * [Remark](https://github.com/stnuessl/ghtocc#remark)

# ghtocc - Github Table of Content Creator

Automatically create table of content for your README.md files on github.

## Dependencies

Python 3.x should do. Otherwise there are none. You can simply copy and paste
the raw source (only 1 file) onto your machine and run it!

## Usage

Always checkout 

```
$ python main.py --help
```

### Download the README from a repository and create table of content

```
$ python main.py stnuessl/ghtocc
```

which equals

```
$ python main.py https://github.com/stnuessl/ghtocc
```

### Specify a local README file and create table of content

```
$ python main.py stnuessl/ghtocc --readme /path/to/local/file
```

## Remark

Please check the table of content before committing. I bet there are a lot of
corner cases which ghtocc will not consider.