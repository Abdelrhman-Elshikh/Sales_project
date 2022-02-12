import pickle
class date:
    def __init__(self,fileName,dumy):
        self.fileName = fileName
        self.dumy = dumy
    def readData(self):
        try:
            dataFile = open(self.fileName, "rb")
            self.items = pickle.load(dataFile)
            dataFile.close()
        except FileNotFoundError:
            dataFile = open(self.fileName, "xb")
            dataFile.close()
            dataFile = open(self.fileName, "wb")
            pickle.dump(self.dumy, dataFile)
            dataFile.close()
            dataFile = open(self.fileName, "rb")
            self.items = pickle.load(dataFile)
            dataFile.close()
        except EOFError:
            dataFile = open(self.fileName, "wb")
            pickle.dump(self.dumy, dataFile)
            dataFile.close()
            dataFile = open(self.fileName, "rb")
            self.items = pickle.load(dataFile)
            dataFile.close()
        return self.items.copy()
    def updateData(self, items):
        try:
            dataFile = open(self.fileName, "wb")
            pickle.dump(items, dataFile)
            dataFile.close()
        except:
            dataFile = open(self.fileName, "xb")
            dataFile.close()
            dataFile = open(self.fileName, "wb")
            pickle.dump(items, dataFile)
            dataFile.close()
    def addData(self,items):
        try:
            dataFile = open(self.fileName, "ab")
            pickle.dump(items, dataFile)
            dataFile.close()
        except:
            dataFile = open(self.fileName, "xb")
            dataFile.close()
            dataFile = open(self.fileName, "wb")
            pickle.dump(items, dataFile)
            dataFile.close()


