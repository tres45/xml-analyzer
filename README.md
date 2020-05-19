# Smart XML Analyzer

Program that analyzes HTML and finds a specific element, even after changes, using a set of extracted attributes.

### Installation

Clone project from repository

```sh
$ cd xml-analyzer
```

```sh
$ pip install .
```

or

```sh
$ python setup.py install
```



### How to use as python module

```python
import xml_analyzer

analyzer = xml_analyzer.Analyzer('PATH_1', 'PATH_2', 'ID')
print(analyzer.diff_report)
```

Also you can compare passenger with passenger


### How to use as CLI application

```sh
$ xml_analyzer 1.html 2.html
Before:
<a class="btn btn-success" href="#ok" id="make-everything-ok-button" onclick="javascript:window.okDone(); return false;" rel="next" title="Make-Button">
 Make everything OK
</a>
Path: html[0] > body[1] > div[0] > div[1] > div[2] > div[0] > div[0] > div[1] > a[0]

After:
<a class="btn btn-success" href="#check-and-ok" onclick="javascript:window.okDone(); return false;" rel="done" title="Make-Button">
 Make everything OK
</a>
Path: html[0] > body[1] > div[0] > div[1] > div[2] > div[0] > div[0] > div[1] > a[1]
```