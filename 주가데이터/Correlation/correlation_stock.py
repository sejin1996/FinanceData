import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import *


####<!--------------matplotlib 한글처리 ----->
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



path = '../PTM_DATA_FILE/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.csv')]  ## 파일명 끝이 .csv인 경우

print(type(file_list_py[0]))  # file_list가 잘 들어왔는지 확인

total_df = pd.DataFrame()

# 주가데이터의 종가만 DF로 가져옴

for file in file_list_py:
    df = pd.read_csv(path + file, sep=',', index_col='date')

    # total_df = pd.concat([total_df, df["close"]])
    # total_df.rename(columns={"close": file[0:-8] + "종가"}, inplace=True)

    total_df[file[0:-8] + "_종가"] = df["close"]

    # print(total_df.head())
    # print("-----------------")

# print(total_df.head())

IR_ER_df = pd.read_csv("../../매출액,금리,환율/금리,환율_전처리.csv",index_col='일자',encoding='euc-kr')

# print(IR_ER_df.head())
# total_df.index = total_df.index.astype('datetime64[ns]')
# IR_ER_df.index = IR_ER_df.index.astype('datetime64[ns]')




result = pd.merge(total_df,IR_ER_df,how ='outer',left_index= True ,right_index = True)

# print(result.head())
# print(result.tail())




# # 결측치 확인하는 코드
# result_check = result.isnull().values.any()
# print(result_check)
# print(result[result['kb금융_종가'].isnull()])

# 결측치 (매년 마지막날 장 개장 안함)
result_dp = result.dropna(thresh =3)

#삼성바이오로직스 상장전 주가 결측치 변경
result =result.fillna(0)

# print(result.isnull().sum())

column_list = list(result.columns)
# print(column_list)
print(result.head())


# 결측치 확인하는 코드
result_check = result.isnull().values.any()
print(result_check)
print(result[result['kb금융_종가'].isnull()])


# plt 를 이용하여 그래프 생성
# plt.figure(figsize=(10,6))
# plt.plot(result['kb금융_종가'],label ='Kb금융')
# plt.plot(result['금리'],label = '금리')
#
# plt.legend()
# plt.show()

# fig, ax1 = plt.subplots()
# ax1.plot(result['kb금융_종가'],label="kb금융" ,color = 'green')
#
# ax2 = ax1.twinx()
# ax2.plot(result['달러환율'],label="달러환율", color = 'yellow')

# plt.scatter(result['kb금융_종가'],result['금리'])

# plt.legend()
# plt.show()



# # 금리 상관관계------------------------------------------------


# for column in column_list:
#     print(column,"/ 달러환율의 상관관계와 pvalue = ",pearsonr(result[column], result['달러환율']))

# print(result.corr(method='pearson'))




# print(pearsonr(result['kb금융_종가'],result['달러환율']))
# print(pearsonr(result['kb금융_종가'],result['금리']))
#


# print((result.index[0]))

## 주가 종가데이터 분기별 평균 주가

total1,total2,total3,total4 =0,0,0,0
len1,len2,len3,len4 = 0,0,0,0
temp =[]
qtr_stock = pd.DataFrame()
#
for col in column_list:
    for year in range(2016,2022):

        for i in range(len(result.index)):
            if result.index[i][0:4]==str(year):
                if  result.index[i][5:7] in ('01','02','03'):
                    total1 += result[col][i]
                    len1 += 1
                    # print(total1,len1)
                elif  result.index[i][5:7] in ('04', '05', '06'):
                    total2 += result[col][i]
                    len2 += 1
                elif  result.index[i][5:7] in ('07', '08', '09'):
                    total3 += result[col][i]
                    len3 += 1
                elif  result.index[i][5:7] in ('10', '11', '12'):
                    total4 += result[col][i]
                    len4 += 1
        if len1!=0:
            print(year,'년 1Q : ',total1/len1)
            temp.append(total1/len1)
        else:
            print(year,'년 1분기는 데이터가 없습니다')
            temp.append(0)
        if len2!=0:
            print(year,'년 2Q : ',total2/len2)
            temp.append(total2/len2)

        else:
            print(year,'년 2분기는 데이터가 없습니다')
            temp.append(0)
        if len3!=0:
            print(year,'년 3Q :',total3/len3)
            temp.append(total3/len3)

        else:
            print(year,'년 3분기는 데이터가 없습니다')
            temp.append(0)
        if len4!=0:
            print(year,'년 4Q : ',total4/len4)
            temp.append(total4/len4)
        else:
            print(year,'년 4분기는 데이터가 없습니다')
            temp.append(0)
        total1, total2, total3, total4 = 0, 0, 0, 0
        len1, len2, len3, len4 = 0,0,0,0
        # print(temp)
    qtr_stock[col] = temp
    temp.clear()




# print(qtr_stock[column_list[0]])



qtr_stock = qtr_stock.drop([qtr_stock.index[0],qtr_stock.index[1],qtr_stock.index[21],qtr_stock.index[22],qtr_stock.index[23]])




# NI 당기순이익 DF
NI_DF = pd.read_csv("../../매출액,금리,환율/당기순익_merge.csv",index_col='결산년도',encoding='euc-kr')

# print(NI_DF.head())

# 분기별 주가 데이터 인덱싱
qtr_stock.set_index(NI_DF.index, inplace = True)


# print(qtr_stock.head())
# print(qtr_stock.tail())

xs = []
ys = []

# print(type(qtr_stock.index))

# xs = qtr_stock.index.tolist()
# ys = qtr_stock[column_list[0]].tolist()
#
# plt.figure(figsize=(10,6))
# plt.bar(xs,ys,width = 0.6, color = 'gray')
#
# plt.show()

do = plt.figure(figsize=(40, 16)) # 차트 생성 및 사이즈 설정
# xtick = ['21_1','20_4','20_3','20_2','20_1','19_4','19_3','19_2','19_1','18_4','18_3','18_2','18_1','17_4','17_3','17_2','17_1','16_4','16_3']
xtick = ['16_3', '16_4', '17_1', '17_2', '17_3', '17_4', '18_1', '18_2', '18_3', '18_4', '19_1', '19_2', '19_3', '19_4', '20_1', '20_2', '20_3', '20_4', '21_1']
# xtick.reverse()
# print(xtick)

for i in range(len(NI_DF.columns)):
    do1=do.add_subplot(3,4,i+1) # subplot 생성
    do1.bar(xtick,NI_DF[NI_DF.columns[i]], color='#'+str(i)*3)

    do2 = do1.twinx()
    do2.plot(xtick,qtr_stock[qtr_stock.columns[i]],label="주가", color = 'red')

    do1.set_title(NI_DF.columns[i], fontsize=15) # 타이틀 설정
    do1.set_ylabel('순이익', fontsize=10) # x축 설정
    do1.set_xlabel('분기',fontsize=10) # y축 설정
    # do1.invert_xaxis()
plt.show()


for i in range(12):
    print(qtr_stock.columns[i],"와 당기순이익의 상관관계, pvalue = ",spearmanr(qtr_stock[qtr_stock.columns[i]], NI_DF[NI_DF.columns[i]]))
#
# print(qtr_stock[qtr_stock.columns[0]])
#
# print(NI_DF[NI_DF.columns[0]])


