import mpl_finance
import numpy as np
import pandas as pd
# import mpl_finance
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

import datetime
import os
import platform # plt 폰트처리하기 위해 필요한 package

if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        #!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        #!mv malgun.ttf /usr/share/fonts/truetype/
        #import matplotlib.font_manager as fm
        #fm._rebuild()
        plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False              #한글 폰트 사용시 마이너스 폰트 깨짐 해결




path = 'DATA_FILE/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우

print(file_list_py)
df_list = []
new_df = pd.DataFrame()
df = pd.DataFrame()
ax_list=[]
i=1


def mydate(x,pos):
    try:
        return new_df.index[int(x-0.5)]
    except IndexError:
        return ''


def naming(df):



    return

fig = plt.figure(figsize=(30, 40))

for file in file_list_py:

    df = pd.read_csv(path + file,sep=',',index_col='date')
    new_df = df.loc['20210331':'20160701'].sort_index()
    new_df.index = new_df.index.astype(str)
    new_df.index = new_df.index.str[0:4] + "-" + new_df.index.str[4:6] + "-" + new_df.index.str[6:8]

    new_df.index = new_df.index.astype('datetime64[ns]')

    ax_sub = plt.subplot(3,4,i)
    ax_sub.set_title(file, fontsize=8)
    mpl_finance.candlestick2_ohlc(ax_sub, new_df['open'], new_df['high'],
                                  new_df['low'], new_df['close'], width=0.6)
    ax_sub.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax_sub.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
    fig.autofmt_xdate()

    i = i + 1


plt.show()