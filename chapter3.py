import sys
import optparse

def wordcount(readtxt):
    dict = {}
    readlist = readtxt.split()
    for everyword in readlist:
        if everyword in dict:
            dict[everyword]+=1
        else:
            dict[everyword] = 1
    return dict

def testcmp(stext, dtext):
    cmplist = []
    sLinesList = []
    for line in stext.splitlines():
        if not line.isspace() and line != "":
            sLinesList.append(line)
    dLinesList = []
    for line in dtext.splitlines():
        if not line.isspace() and line != "":
            dLinesList.append(line)
    sLen = len(sLinesList)
    dLen = len(dLinesList)
    for step in range(max(sLen, dLen)):
        try:
            sWordList = sLinesList[step].split()
        except IndexError as e:
            print("dFile is end")
            sLinesList.append("")
        try:
            dWordList = dLinesList[step].split()
        except IndexError as e:
            print("dFile is end")
            dLinesList.append("")
        if sWordList != dWordList:
            cmplist.append((step, sLinesList[step], dLinesList[step]))
    return cmplist

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-s", "--sFile", action="store", type="string", dest="sFileName")
    parser.add_option("-d", "--dFile", action="store", type="string", dest="dFileName")
    (options, args) = parser.parse_args()
    with open(options.sFileName, 'r') as sFile, open(options.dFileName, 'r') as dFile:
        sText = sFile.read()
        dText = dFile.read()

        print("文件: %s" %options.sFileName)
        print("词汇总数: %d" %len(wordcount(sText)))
        print("各词汇统计: %s" %wordcount(sText))

        print("文件: %s" % options.dFileName)
        print("词汇总数: %d" % len(wordcount(dText)))
        print("各词汇统计: %s" % wordcount(dText))

        cmpList = testcmp(sText, dText)
        for diff in cmpList:
            print("%s %s: %s" %(options.sFileName, diff[0], diff[1]))
            print("%s %s: %s" %(options.dFileName, diff[0], diff[2]))

