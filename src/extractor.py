import re

def extract(text, itemRegexGroup, fieldMeta):
    itemDataSet = extractText(text, itemRegexGroup, fieldMeta)
    itemDataSet = postProcess(itemDataSet, fieldMeta)
    return itemDataSet

def extractText(content, itemRegexGroup, fieldMeta):
    items = itemRegexGroup.getAllMatches(content)
    itemDataSet = []
    for item in items:
        itemData = []
        for field in fieldMeta:
            matches = field["regexGroup"].getAllMatches(item)
            if len(matches) > 0:
                itemData.append(matches[0])
            else:
                itemData.append(None)
        itemDataSet.append(itemData)
    return itemDataSet

def postProcess(itemDataSet, fieldMeta):
    for item in itemDataSet:
        for i in range(len(fieldMeta)):
            if fieldMeta[i].has_key("prefix") and fieldMeta[i]["prefix"]:
                item[i] = fieldMeta[i]["prefix"] + item[i]
            if fieldMeta[i].has_key("removeHTMLTag") and fieldMeta[i]["removeHTMLTag"]:
                item[i] = re.sub("</?[A-Za-z][A-Za-z0-9]*[^<>]*>", "", item[i])
            if fieldMeta[i].has_key("replace") and len(fieldMeta[i]["replace"]) > 0:
                for rep in fieldMeta[i]["replace"]:
                    item[i] = item[i].replace(rep[0], rep[1])
            if fieldMeta[i].has_key("trim") and fieldMeta[i]["trim"]:
                if item[i]:
                    item[i] = item[i].strip()
    return itemDataSet

