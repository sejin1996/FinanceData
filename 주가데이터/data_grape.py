import numpy as np
import pandas as pd
# import mpl_finance
import mplfinance as mpf
import matplotlib.pyplot as plt
import datetime


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

mpf.plot(new_df_kb, type='candle')
# colorset = mpf.make_marketcolors(up='tab:red', down='tab:blue', volume='tab:blue')



# colorset = mpf.make_marketcolors(up='tab:red', down='tab:blue', volume='tab:blue')
# s = mpf.make_mpf_style(marketcolors=colorset)
# mpf.plot(new_df_kb, type='candle', volume=False, style=s)