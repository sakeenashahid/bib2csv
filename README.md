# bib2csv
Convertion of BibTex to CSV file

# How to install (Ubuntu Linux)

```shell
sudo pip install git+https://github.com/ssrinformatica/bib2csv.git
```
It will require installed PIP and GIT

# Example

First, create a file test.py with the code bellow:

```python
import sys
import os.path 
from bib2csv import bib2csv

print 'Converting from: '+sys.argv[1]+' to: '+sys.argv[2]  

if os.path.exists(sys.argv[1]):
    objBib2csv = bib2csv.Converter()    
    objBib2csv.setBibfile( open(sys.argv[1],'r').read() )
    objBib2csv.generate(sys.argv[2])
else:
    print "Error reading file "+sys.argv[1]
```

After save the file, in the command line run:

```shell
python test.py file.bib file.csv
```

