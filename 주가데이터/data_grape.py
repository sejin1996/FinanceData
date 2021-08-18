import mpl_finance
import numpy as np
import pandas as pd
# import mpl_finance
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import datetime

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



df_kb = pd.read_csv("DATA_FILE/kb금융.csv",sep=',',index_col='date')

# print(df_kb.head())

new_df_kb = df_kb.loc['20210331':'20160701'].sort_index()


#### 날짜 인덱스를 파이썬 날싸형식에 맞춰서 변경 (ex. 20160701 -> 2016-07-01 )

new_df_kb.index = new_df_kb.index.astype(str)

new_df_kb.index = new_df_kb.index.str[0:4] + "-" + new_df_kb.index.str[4:6] + "-" + new_df_kb.index.str[6:8]

new_df_kb.index = new_df_kb.index.astype('datetime64[ns]')



print(new_df_kb.head())
print(new_df_kb.tail())



# start = datetime.datetime(2016, 7, 1)
# end = datetime.datetime(2016, 7, 31)
#
# fig = plt.figure(figsize=(24, 8))
# ax = fig.add_subplot(111)
#
# mplfinance.candlestick2_ohlc(ax, new_df_kb['open'], new_df_kb['high'], new_df_kb['low'], new_df_kb['close'], width=0.5, colorup='r', colordown='b')
# plt.show()

### 단순 mpf plot을 찍어보는 함수

# mpf.plot(new_df_kb, type='candle')

# 날짜 인덱싱을 위한 함수
def mydate(x,pos):
    try:
        return new_df_kb.index[int(x-0.5)]
    except IndexError:
        return ''


### mpl_finance를이용한 subplot
fig = plt.figure(figsize=(30,40))
ax_sub1 = plt.subplot(341)
ax_sub1.set_title('kb금융 주가',fontsize=8)
plt.xlim(new_df_kb.index[0],new_df_kb.index[-1])
mpl_finance.candlestick2_ohlc(ax_sub1,new_df_kb['open'],new_df_kb['high'],
                  new_df_kb['low'],new_df_kb['close'],width=0.6)

# ax_sub1.xaxis.set_major_locator(ticker.MaxNLocator(10))
# ax_sub1.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))

fig.autofmt_xdate()

plt.show()


# colorset = mpf.make_marketcolors(up='tab:red', down='tab:blue', volume='tab:blue')
# s = mpf.make_mpf_style(marketcolors=colorset)
# mpf.plot(new_df_kb, type='candle', volume=False, style=s)