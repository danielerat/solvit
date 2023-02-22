from beautifultable import BeautifulTable
# Our Great class
class Store:
    # And this is how we do constructors in python 
    def __init__(self,stock):
        self.stock=stock #initializing the our constructor

    # Show a given stock
    def show_stock(self):
        print("")
        print("\t Marie's Stock")
        stockKeys=self.stock.keys()
        table = BeautifulTable()
        [table.rows.append(self.stock.get(i).values()) for i in self.stock]
 
        table.columns.header=(stockKeys)
        table.rows.header=(stockKeys)
        print(table)
    
    # Get the whole stock
    def get_stock(self,cylinder,sphere):
        return ("Stock Left for cylinder/Sphere {}/{} : {} glasses".format(cylinder,sphere,self.stock.get(str(cylinder)).get(str(sphere))))
    # Add elements to a given stock 
    def add_stock(self,cylinder,sphere,count):
        current_stock=self.stock.get(str(cylinder)).get(str(sphere))
        self.stock[str(cylinder)][str(sphere)]= current_stock + count
        self.show_stock()

    def reduce_stock(self,cylinder,sphere,count):
        current_stock=self.stock.get(str(cylinder)).get(str(sphere))
        self.stock[str(cylinder)][str(sphere)]=current_stock-count
        self.show_stock()
    
    def get_total_glass(self):
        count=0
        for i in self.stock.values():
            for j in i.values():
                count+=j
        return "Total Glases are: "+count

stock={
    "0":{
        "0":10,
        "1.25":0,
        "2":8,
        "2.25":0
    },
    "1.25":{
         "0":25,
        "1.25":2,
        "2":0,
        "2.25":0
    },
    "2":{
         "0":0,
        "1.25":0,
        "2":9,
        "2.25":0
    },
    "2.25":{
         "0":10,
        "1.25":0,
        "2":11,
        "2.25":0
    },
}

# Our Object
marie=Store(stock)

# Show The stock of marie
marie.show_stock()



