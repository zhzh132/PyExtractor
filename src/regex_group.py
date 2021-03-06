import re
import unittest

class RegexGroup():
    def __init__(self):
        self.regex_list = []

    def addRegex(self, regex):
        if type(regex) == str or type(regex) == unicode:
            regexObj = re.compile(regex, re.MULTILINE)
            self.regex_list.append(regexObj)
        elif type(regex) == list:
            for r in regex:
                self.addRegex(r)
        elif hasattr(regex, "findall"):
            self.regex_list.append(regex)
        else:
            raise RuntimeError, regex
        return self

    def getAllMatches(self, text):
        matches = []
        if len(self.regex_list) == 0:
            matches.append(text)
        else:
            self._matchText(matches, text, self.regex_list)
        return matches

    def _matchText(self, resultArr, text, regexList):
        if len(regexList) == 0:
            return
        elif len(regexList) == 1:
            result = regexList[0].findall(text)
            resultArr += result
        else:
            result = regexList[0].findall(text)
            for s in result:
                self._matchText(resultArr, s, regexList[1:])




class Test(unittest.TestCase):
    def testMatch(self):
        text = "abcdefggfedcba";
        rGroup = RegexGroup()
        rGroup.addRegex(["a.*a", "c.*c"])
        result = rGroup.getAllMatches(text)
        self.assertEquals(1, len(result))
        self.assertEquals("cdefggfedc", result[0])

    def testMatch2(self):
        text = "abcdefggfedcba abcd11111dcba abcd22222dcba";
        rGroup = RegexGroup()
        rGroup.addRegex(["a.*a", "c.*c", "e.*?e"])
        result = rGroup.getAllMatches(text)
        self.assertEquals(1, len(result))
        self.assertEquals("efggfe", result[0])

    def testMatch3(self):
        text = "abcdefggfedcba abcd11111dcba abcd22222dcba";
        rGroup = RegexGroup()
        rGroup.addRegex(["a.*?a", "c.*c", "d.*d"])
        result = rGroup.getAllMatches(text)
        self.assertEquals(3, len(result))
        self.assertEquals("defggfed", result[0])
        self.assertEquals("d11111d", result[1])
        self.assertEquals("d22222d", result[2])

    def testEmptyGroup(self):
        text = "abcdefggfedcba abcd11111dcba abcd22222dcba";
        rGroup = RegexGroup()
        result = rGroup.getAllMatches(text)
        self.assertEquals(1, len(result))
        self.assertEquals(text, result[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
