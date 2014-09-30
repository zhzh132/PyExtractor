from string import Template

class FileOutput():
    def __init__(self, template, filePath, encoding="utf-8"):
        self.encoding = encoding
        self.template = Template(template)
        self.filePath = filePath

    def output(self, itemDataSet, fieldMeta):
        fobj = open(self.filePath, 'a')
        for item in itemDataSet:
            for i in range(len(fieldMeta)):
                fobj.write(self.template.safe_substitute(key=fieldMeta[i]["name"], value=item[i]).encode(self.encoding))
            fobj.write('\n')
        fobj.close()

class TemplateOutput():
    def __init__(self, template, encoding="utf-8"):
        self.encoding = encoding
        self.template = Template(template)

    def output(self, itemDataSet, fieldMeta):
        for item in itemDataSet:
            for i in range(len(fieldMeta)):
                print self.template.safe_substitute(key=fieldMeta[i]["name"], value=item[i]).encode(self.encoding),
            print

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