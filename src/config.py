from regex_group import RegexGroup

def get(refresh = False):
    if refresh:
        get.config = None
    if get.config:
        return get.config
    get.config = MemConfig()
    return get.config

get.config = None

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