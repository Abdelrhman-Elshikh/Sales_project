class datahelper(object):

    def __init__(self):
        self.item = []

    def setData(self, it):
        self.item = self._prepareData(it)

    def getData(self, index=None):
        if index is not None:
            return self.item[index]
        else:
            return (self.item)

    def addData(self, it):
        self.item.append(self._prepareData(it))

    def removeData(self, index):
        self.item.pop(index)

    def clearData(self):
        self.item.clear()

    def increase(self, index):
        try:
            if self.item[index]["sellCount"] < self.item[index]["allCount"]:
                self.item[index]["sellCount"] += 1
                self.item[index]["profit"] = self.item[index]["sellCount"] * self.item[index]["price"]
            else:
                pass
        except:
            pass

    def decrease(self, index):
        if self.item[index]["sellCount"] > 0:
            self.item[index]["sellCount"] -= 1
            self.item[index]["profit"] = self.item[index]["sellCount"] * self.item[index]["price"]
        else:
            pass

    def inList(self):
        inList = []
        for item in self.item:
            inList.append(item["name"])
        return inList

    def _prepareData(self, it):
        mydata = {"allCount": it[0],
               "id": it[1],
               "name": it[2],
               "type": it[3],
               "sellCount": it[4],
               "price": it[5],
               "profit": it[6],
               "fromWhere": it[7]
               }
        return mydata
