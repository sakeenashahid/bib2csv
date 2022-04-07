class Converter:
    bibfile    = ''
    attributes = []
    datas      = []
    
    def __init__(self):
        self.attributes = ['journal','title','author','volume','doi', 'url','number','publisher','booktitle','school','organization','address','year','month','pages']
        self.datas      = []
        
    def setBibfile( self,bibfile ):
            self.bibfile = bibfile
	    __data = 'type,id'
            for att in self.attributes:
                __data += ','+att
	    
	    self.datas.append(__data)

    	    for bib in self.bibfile.split('@'):
                __data = '"'+bib[ 0:bib.find('{') ]+'"'
                __data += ',"'+bib[ bib.find('{')+1 :bib.find(',',bib.find('{'))]+'"'

		for att in self.attributes:
		    __att = att + '={'
		    if bib.find(__att)>=0:
		        __data += ',"'+bib[ bib.find( __att )+len(__att)  :bib.find('}',bib.find(__att))]+'"'
		    else:
                        __data += ',""'

	        self.datas.append(__data)	    
                
    def setAttribute( self,att ):
            self.attributes = att

    def addAttribute( self,att ):
            self.attributes.append(att)

    def addData( self,data ):
            self.datas.append(data)

    def generate( self,file ):
            f2w = open(file,"w")

            for data in self.datas:
                f2w.write( data+"\n" )

            f2w.close()
