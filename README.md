# project-python-project-lvl2

[![Build Status](https://travis-ci.org/alexofechoes/python-project-lvl2.svg?branch=master)](https://travis-ci.org/alexofechoes/python-project-lvl2)[![Maintainability](https://api.codeclimate.com/v1/badges/2c4dd79cf807b39e106e/maintainability)](https://codeclimate.com/github/alexofechoes/python-project-lvl2/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/2c4dd79cf807b39e106e/test_coverage)](https://codeclimate.com/github/alexofechoes/python-project-lvl2/test_coverage)

### Installation
```bash
$ pip3 install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple alexofechoes_gendiff
```
[![asciicast](https://asciinema.org/a/MQCGkOXYwIKoHQW29YgILsTpc.svg)](https://asciinema.org/a/MQCGkOXYwIKoHQW29YgILsTpc)


### Diff between two files (json or yaml) with text format output
```bash
$ gendiff before.json after.yaml
```
or  

```bash
$ gendiff before.json after.yaml --format text
```
[![asciicast](https://asciinema.org/a/quS272TlNTcvYnrkmMdqSBvrE.svg)](https://asciinema.org/a/quS272TlNTcvYnrkmMdqSBvrE)


### Diff between two files (json or yaml) with plain format output
```bash
$ gendiff before.json after.yaml --format plain
```
[![asciicast](https://asciinema.org/a/SKtObZMVpvoXNPDbcro9zC9xi.svg)](https://asciinema.org/a/SKtObZMVpvoXNPDbcro9zC9xi)


### Diff between two files (json or yaml) with json format output
```bash
$ gendiff before.json after.yaml --format json
```
[![asciicast](https://asciinema.org/a/xsHk3WjhIopECslecNUxjaQXT.svg)](https://asciinema.org/a/xsHk3WjhIopECslecNUxjaQXT)
