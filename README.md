# bib2csv
Convertion of BibTex to CSV file

# How to install (Ubuntu Linux)

```shell
sudo pip install git+https://github.com/ssrinformatica/bib2csv.git
```
It will require installed PIP and GIT

# Example

First, create a file **test.bib** with the bellow content:

```txt
@article{ribeiro2016using,
  title={USING PYTHON WITH SIMPLECV TO DETECT A CORN KERNEL IN DIGITAL IMAGE},
  author={Ribeiro, Sergio Silva and Ferrasa, Adriano and Falate, Rosane},
  journal={Iberoamerican Journal of Applied Computing},
  volume={4},
  number={2},
  year={2016}
}

@article{name2014metadata,
  title={Metadata Extraction for Calculating Object Perimeter in Images},
  author={Name, Marcio Hosoya and Ribeiro, Sergio Silva and Maruyama, Teruo Matos and de Padua Valle, Henrique and Falate, Rosane and Vaz, Maria Salete Marcon Gomes},
  journal={IEEE Latin America Transactions},
  volume={12},
  number={8},
  pages={1566--1571},
  year={2014},
  publisher={IEEE}
}

@book{ribeiro2016metodos,
  title={Metodos computacionais aplicados a agricultura: Python & Weka},
  author={Ribeiro, Sergio Silva},
  year={2016},
  publisher={Novaterra Editora e Distribuidora LTDA}
}
```

Second, create a file **test.py** with the bellow code:

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

