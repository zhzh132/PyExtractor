from regex_group import RegexGroup
import json

def get(confFile = None, refresh = False):
    if refresh:
        get.config = None
    if get.config:
        return get.config
    get.config = JsonConfig(confFile)
    return get.config

get.config = None

class JsonConfig():
    def __init__(self, jsonFile="config.json"):
        with open(jsonFile, 'r') as f:
            text = f.read();
        self.config = json.loads(text)
        self.itemRegexGroup = None
        self.fieldMeta = None

    def getFieldMeta(self):
        if not self.fieldMeta:
            self.fieldMeta = self.config["fields"]
            for field in self.fieldMeta:
                field["regexGroup"] = RegexGroup().addRegex(field["regexGroup"])
        return self.fieldMeta

    def getItemRegexGroup(self):
        if not self.itemRegexGroup:
            self.itemRegexGroup = RegexGroup().addRegex(self.config["regexGroupForItem"])
        return self.itemRegexGroup

    def getOptions(self):
        return self.config["options"]

class MemConfig():
    def __init__(self):
        self.config = {
            "options": {
                        "url": r"https://github.com/trending",
                        "encoding": "utf-8"
                        },
            "regexGroupForItem": RegexGroup().addRegex(["""<ol class="repo-list">[\w\W]+?</ol>""",
                                           """<li class="repo-list-item"[\w\W]+?</li>"""]),
            "fields": [
                       {"name": "project",
                        "type": "string",
                        "regexGroup": RegexGroup().addRegex(["""<h3 class="repo-list-name">[\w\W]+?</h3>""",
                                                        """(?<=<a href=").+(?=")"""])
                        },
                       {"name": "url",
                        "type": "string",
                        "prefix": "https://github.com",
                        "regexGroup": RegexGroup().addRegex(["""<h3 class="repo-list-name">[\w\W]+?</h3>""",
                                                        """(?<=<a href=").+(?=")"""])
                        },
                       {"name": "language",
                        "type": "string",
                        "trim": True,
                        "regexGroup": RegexGroup().addRegex(["""(?<=class="repo-list-meta">)[\w\W]+?(?=&#8226;)"""])
                        }
                       ]
                             }

    def getFieldMeta(self):
        return self.config["fields"]

    def getItemRegexGroup(self):
        return self.config["regexGroupForItem"]

    def getOptions(self):
        return self.config["options"]