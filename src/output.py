
class ConsoleOutput():
    def __init__(self, encoding="utf-8"):
        self.encoding = encoding

    def output(self, itemDataSet, fieldMeta):
        for item in itemDataSet:
            for i in range(len(fieldMeta)):
                print ("{'%s': '%s'}" % (fieldMeta[i]["name"], item[i])).encode(self.encoding),
            print

class DatabaseOutput():
    def output(self, item, fieldMeta):
        pass