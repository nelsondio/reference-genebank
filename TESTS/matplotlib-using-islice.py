import itertools
import matplotlib.pyplot as plt
import hashlib  
import sys      
import os 
from collections import Counter

#
# source: file with labelMd5 tab fastaMd5
# use counter for counting duplicates and then usie islice to plot
# read test-labelMd5-fastaMd5-chr1-50.txt
# using if, elif pending to use for loop or switch
#
def main(): 
    myPath = '../'
    hardLink = 'OUTPUT_FIGURES/'
    myFile =  'sequence-homo-38-chr22-coding-nucleotides.txt.dict.out'
    filepath = myPath +  hardLink +  myFile
    outpath = myFile
    #sys.argv[1]
    fastaMd5Dict = {}
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    numberOfLines = countLines(filepath)
    print(numberOfLines)
    fastaMd5List = []
    with open(filepath) as fo:
        for i, line in enumerate(fo):
            toParse = line.split() # generate a list
            fastaMd5List.append(toParse[1])
        myDict = dict(Counter(fastaMd5List))
        #print(myDict)
        totalNumOfRecords = (len(myDict)) #2671 chr22  #11378 chr1
        batch = int(len(myDict)/700) # 2671 / 700  len(chr22) / 700 == 3
        print(str(batch) + " ====  " + str(len(myDict)) ) # 3 and 8151
        tmp = {}
        
        for i in range(batch):
            figNumber = 1
            if i == 1:
                tmp = dict(itertools.islice(myDict.items(), 717))
                processBatch(tmp, figNumber, batch, outpath)
            else:
                figNumber = 2
                tmp = dict(itertools.islice(myDict.items(), 718, 1434))
                processBatch(tmp, figNumber, batch, outpath)
                

    #plt.show()

def countLines(filepath):
    fo = open(filepath, 'r').readlines()
    return len(fo)
def countDuplicates(d):
    out = []
    #cnt = Counter()
    for h in d.values():
        out.append(h['fastaMd5'])
    print(type(out))
    dictOfElems = dict(Counter(out))
    return dictOfElems
    
def shortenName(list):
    shortNameList = []
    for n in list:
        tmp = n[:3]
        shortNameList.append(tmp)
    return shortNameList
def processBatch1(i,j,k):
    return False
def processBatch(tmp, fignumber, batch, filepath):
    names = list(tmp.keys())
    x = shortenName(names)
    y = list(tmp.values())
    plt.subplot(batch, 1, fignumber)
    fig = plt.subplots(figsize=(20,10))
    plt.bar(x,y)  ## HERE TO ADD IF Y IS MORE THAN 10 then print shortname only, else nothing
    plt.xlabel("xlabel")
    plt.ylabel("ylabel")
    plt.title(filepath+str(fignumber)+'.png')

    plt.savefig(filepath+str(fignumber)+'.png')
main()
