class Stock:#class for creating then stock
    cOMPANYName=None
    tNumberofShares=None
    CShareprice=None
    def __init__(self,Stockname,Numberofshare,Shareprice):#initializing the members of the stock
        self.Stockname=Stockname
        self.Numberofshare=Numberofshare
        self.Shareprice=Shareprice
    @classmethod
    def ValueTotal(cls):#giving the stock mvalue of the particular company
        cls.value=cls.NumberofShare*cls.Shareprice
        return cls.value



class StockPortfolio(Stock):#stock potfolio which holds the portfolio of the respective class
    def __init__(self,Numberofstock=int(input("Number of stocks you earn"))):
        self.st = []
        self.Numberofstock=Numberofstock
        for j in range(Numberofstock):
            self.st.append(Stock(Stockname=input("enter the stockname"),Numberofshare=input("enter the share"),Shareprice=input("enter the share price")))
        for i in range(len(self.st)):
            print(self.st[i])
    def getval(self):
        f = open("stockdetails.txt", "r")
        g = f.readlines()
        vals=[]
        for i in g:
            s=i.split()
            vals.append(s)
        for i in vals:
            if i==self.checkShareName:
                Stock.ShareName=i
                Stock.Numberofshare=int(vals[vals.index(i)+1])
                Stock.Shareprice=int(vals[vals.index(i)+2])
                return Stock.Numberofshare


    def calvalue(self):
        self.checkShareName=input("for which share you meed to check the value")
        g=self.getval()
        self.myval=self.st[self.st.index(self.checkShare)+2]/g
        self.amnt=Stock.Shareprice*self.myval


S=StockPortfolio()
S.calvalue()











