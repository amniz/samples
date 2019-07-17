#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: implements Node class
class Dnode:#creating the node class
    def __init__(self,data=None,nexp=None,prev=None):
        self.data=data  # entering the data
        self.nexp=nexp  # pointing to the next pointer
        self.prev=prev  # pointing to the previous pointer
        
        
