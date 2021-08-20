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
total_df.index = total_df.index.astype('datetime64[ns]')
IR_ER_df.index = IR_ER_df.index.astype('datetime64[ns]')




result = pd.merge(total_df,IR_ER_df,how ='outer',left_index= True ,right_index = True)

print(result.head())
print(result.tail())




# 결측치 확인하는 코드
# result_check = result.isnull().values.any()
# print(result_check)
# print(result[result['kb금융_종가'].isnull()])

# 결측치 제거
result.dropna(inplace=True)

# print(result.isnull().sum())

column_list = list(result.columns)
print(column_list)


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


# # 금리 상관관계
# for column in column_list:
#     print(column,"/ 달러환율의 상관관계와 pvalue = ",pearsonr(result[column], result['달러환율']))

print(result.corr(method='pearson'))



# print(pearsonr(result['kb금융_종가'],result['달러환율']))
# print(pearsonr(result['kb금융_종가'],result['금리']))
#

# plt.legend()
# plt.show()