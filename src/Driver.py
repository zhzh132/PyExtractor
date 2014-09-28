from config import get as getConfig
from output import ConsoleOutput
from extractor import extract
import logging
import urllib2

class StringDriver():
    def __init__(self, config):
        self.config = config
        self.text = None
        self.outputHandler = None

    def setText(self, text):
        self.text = text

    def setOutputHandler(self, outputHandler):
        self.outputHandler = outputHandler

    def run(self):
        if not self.text:
            logging.warn("Text is EMPTY!")
            return
        itemDataSet = extract(self.text, config.getItemRegexGroup(), config.getFieldMeta())

        if self.outputHandler:
            self.outputHandler.output(itemDataSet, config.getFieldMeta())
        else:
            logging.warn("OutputHandler not found.")

class LocalFileDriver():
    def __init__(self, config):
        self.filePath = config.getOptions()["file"]
        self.encoding = config.getOptions()["encoding"]
        self.stringDriver = StringDriver(config)

    def setOutputHandler(self, outputHandler):
        self.stringDriver.setOutputHandler(outputHandler)

    def run(self):
        with open(self.filePath, "r") as f:
            text = f.read().decode(self.encoding)
        self.stringDriver.setText(text)
        self.stringDriver.run()

class UrlDriver():
    def __init__(self, config):
        self.url = config.getOptions()["url"]
        self.encoding = config.getOptions()["encoding"]
        self.stringDriver = StringDriver(config)

    def setOutputHandler(self, outputHandler):
        self.stringDriver.setOutputHandler(outputHandler)

    def run(self):
        text = urllib2.urlopen(self.url).read().decode(self.encoding)
        self.stringDriver.setText(text)
        self.stringDriver.run()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    config = getConfig("../test/bigbangtheory.json")

    driver = UrlDriver(config)
    driver.setOutputHandler(ConsoleOutput(config.getOptions()["encoding"]))
    driver.run()
