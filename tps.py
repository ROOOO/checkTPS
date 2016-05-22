# coding: utf-8

__author__ = 'King'

import os
import re

class TPS:
    def __init__(self):
        self.allTpsImgs = []
        self.allFolderImgs = []

    def run(self):
        for dirPath, dirNames, fileNames in os.walk(os.path.join(os.getcwd(), 'icon', 'home', 'cmn')):
            for fileName in fileNames:
                if os.path.splitext(fileName)[1] == '.png' or os.path.splitext(fileName)[1] == '.PNG':
                    # print fileName
                    self.allFolderImgs.append(fileName)
        file = open(os.path.join(os.getcwd(), 'tps', 'cmn.tps'))
        text = file.read()
        items = re.findall(re.compile(r'<filename.*?cmn/(.*?)(\.PNG|\.png)</filename>', re.S), text)
        file.close()
        for item in items:
            self.allTpsImgs.append(item[0] + item[1])

t = TPS()
t.run()
print u'TPS里有而文件夹没有的'
l = list(set(t.allTpsImgs) - set(t.allFolderImgs))
l.sort()
for i in l:
    print i

print u'TPS里没有而文件夹有的'
l = list(set(t.allFolderImgs) - set(t.allTpsImgs))
l.sort()
for i in l:
    print i
