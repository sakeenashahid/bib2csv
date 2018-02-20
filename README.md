# bib2csv
Convertion of BibTex to CSV file

# Example

```python
import sys
import os.path 
import bib2csv

print 'Converting from: '+sys.argv[1]+' to: '+sys.argv[2]  

if os.path.exists(sys.argv[1]):
    objBib2csv = Bib2csv()    
    objBib2csv.setBibfile( open(sys.argv[1],'r').read() )
    objBib2csv.generate(sys.argv[2])
else:
    print "Error reading file "+sys.argv[1]
```
