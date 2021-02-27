# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:07:08 2020

@author: sayers
"""
import pandas as pd
import csv
import pyperclip

def giveyes(emplid):
    if emplid in x:
        return("Yes")
    else:
        return("No")


with open("s:\\downloads\\SR727---_40233658.txt") as f:
    counter=0
    rd = csv.reader(f, delimiter="\t", quotechar='"')
    maindf= pd.DataFrame(columns=['emplid', 'campus', 'efftdt', 'accdorg','advisor','instr_type'])
    for row in rd:
        if counter<10:
            counter+=1
            continue
        else:
            try:
                x=row[0].split()
                if len(x)>6:
                    x[3] = ' '.join([x[3],x[4]])
                    x[4] = x[5]
                    x[5]=x[6]
                    x.remove(x[6])
                xdf = pd.DataFrame([x],columns=['emplid', 'campus', 'efftdt', 'accdorg','advisor','instr_type'])
                maindf = maindf.append(xdf)
            except:
                pass

x= maindf[maindf.campus=='YRK01'].emplid.unique()
maindf['status'] = maindf.emplid.apply(giveyes)
dones = maindf[maindf.status=='Yes']
dones = dones[dones.campus=='YRK01']
dones = dones[dones.efftdt.str.contains('7/1/2')]
df1 = maindf[maindf.status=='Yes']
df1[(df1.efftdt.str.contains("7/1/20"))&(df1.emplid.isin(list(df[df.empl_stat_cd.isin(['A','S','L'])].empl_id.unique())))].emplid.unique()
df1[(df1.efftdt.str.contains("/190"))&(df1.campus=="YRK01")]
df1[df1.campus=='YRK01'].efftdt.unique()
xyzed= list(df1[(df1.efftdt.str.contains("7/1/20"))&(df1.campus=="YRK01")].emplid.unique())
df1 = df1[~df1.emplid.isin(xyzed)]
#df1 = df1[~df1.emplid.isin(dfx.empl_id.unique())]
df1 =df1[~df1.emplid.isin(list(df[df.empl_stat_cd.isin(['A','S','L'])].empl_id.unique()))]
actions = df1[~df1.emplid.str.contains("blahblah")]
actions[(actions.efftdt.str.contains("/190"))&(actions.campus=="YRK01")]
dolist = list(actions[actions.campus=="YRK01"].emplid.unique())
dfy = pd.read_excel('s:\\downloads\\CrystalReportViewer1 (37).xlsx')
firstlist=list(set(list(dfy.emplid.values)))
dfy = pd.read_excel('s:\\downloads\\CrystalReportViewer1 (38).xlsx')
seclist=list(set(list(dfy.emplid.values)))
dfy = pd.read_excel('s:\\downloads\\CrystalReportViewer1 (39).xlsx')
thirdlist=list(set(list(dfy.emplid.values)))
lastlist= firstlist+seclist+thirdlist
lastlist = list(set(lastlist))


dolist = [i for i in dolist if i not in lastlist]
