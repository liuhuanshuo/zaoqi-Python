'''
Created on Jan 6, 2017
Apriori modified script
@author: Zengke
'''
# -*- coding: utf-8 -*-

from numpy import *
import pandas as pd

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
    return map(frozenset, C1)#use frozen set so we
                            #can use it as a key in a dict   

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not can in ssCnt: 
                    ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    return retList                            

def apriori(dataSet, minSupport = 0.5):
    C1 = list(createC1(dataSet))
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData
    
def generateRules(L, supportData, minConf=0.7):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf: 
            print (freqSet-conseq,'-->',conseq,'conf:',conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

    
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)    
    
def dataconvert(arulesdata,tidvar='tid',itemvar='item',data_type = 'BOOL'):
    
    if data_type == 'BOOL':
        print('BOOL type dataSet!')
        dataSet=[]            
        for i in range(len(arulesdata)):
            item=arulesdata.columns[arulesdata.ix[i,:].values==True].tolist()
            if item:
                dataSet.append(item)
        return dataSet
        
    elif data_type == 'inverted':
        print('inverted index type dataSet')
        group_index=list(arulesdata.groupby(tidvar).groups.values())
        dataSet=[]
        for i in range(len(group_index)):
            item=arulesdata.ix[group_index[i],itemvar].values.tolist()
            if item:
                dataSet.append(item)
        return dataSet
    
    else:
        raise ValueError('data_type not understood')


def arules(dataset,minSupport=0.1,minConf=0.5,minlen=1,maxlen=10):
    
    L,supportData=apriori(dataset,minSupport = minSupport)
    ruleList=generateRules(L, supportData, minConf= minConf)
    
    temp=[]
    for rules in ruleList:
        lhs=rules[0];rhs=rules[1]
        if minlen<=len(lhs.union(rhs))<=maxlen:
            confidence=rules[2];support=supportData[lhs.union(rhs)];benchmark=supportData[rhs]
            lift=confidence/benchmark
            row={'lhs':lhs,'':'==>','rhs':rhs,'support':support,'confidence':confidence,'lift':lift}
            temp.append(row)
    
    res=pd.DataFrame(temp)
    res=res.reindex_axis(['lhs','','rhs','support','confidence','lift'],axis=1)
    
    return res
