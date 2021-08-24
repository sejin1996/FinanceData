import matplotlib.pyplot as plt



import pandas as pd
import numpy as np
import itertools #스피어만 상관계수

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':  # 맥OS
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...  sorry~~~')

df=pd.read_csv("../당기순익_증가율.csv",index_col='결산년도',encoding='euc-kr')
# df

df.index=['16-3','16-4','17-1','17-2','17-3','17-4','18-1','18-2','18-3','18-4','19-1','19-2','19-3','19-4','20-1','20-2','20-3','20-4','21-1']
df.index.name='분기'


list1,list2,list3=[],[],[]
for i in range(1,19):
    l=list(df.iloc[i,26:])
    l.sort(reverse=True)
    print(l[0:3])
    for x in range(3):
        for n in range(1,19):
            for a in range(26,38):
                if df.iloc[n,a] == l[x]:
                    print(df.columns[a])
                    if x==0:
                        list1.append(df.columns[a][:-7])
                    elif x==1:
                        list2.append(df.columns[a][:-7])
                    else:
                        list3.append(df.columns[a][:-7])

df1=pd.DataFrame({'1st':list1,'2nd':list2,'3rd':list3},index=df.index[1:])



do = plt.figure(figsize=(10, 18)) # 차트 생성 및 사이즈 설정



do1=do.add_subplot(3,1,1)
do1.scatter(df1.index,df1['1st'],label='1st')
do1.set_title('증가율 1위', fontsize=15) # 타이틀 설정
do1.set_xlabel('분기',fontsize=10)

do1.legend(loc='best')
do2=do.add_subplot(3,1,2)
do2.scatter(df1.index,df1['1st'],label='1st')
do2.scatter(df1.index,df1['2nd'],c='r',label='2nd')
do2.set_title('증가율 1,2위', fontsize=15) # 타이틀 설정
do2.set_xlabel('분기',fontsize=10)
do2.legend(loc='best')

do3=do.add_subplot(3,1,3)
do3.scatter(df1.index,df1['1st'],label='1st')
do3.scatter(df1.index,df1['2nd'],c='r',label='2nd')
do3.scatter(df1.index,df1['3rd'],c='g',label='3rd')
do3.set_title('증가율 1,2,3위', fontsize=15) # 타이틀 설정
do3.set_xlabel('분기',fontsize=10)
do3.legend(loc='best')

plt.tight_layout(1.5)
plt.show()