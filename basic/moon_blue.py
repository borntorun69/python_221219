import pyupbit
#prophet 불러옴
from fbprophet import Prophet


#매수 시점의 가격
# nowValue = pyupbit.get_current_price("KRW-BTC")
nowValue = pyupbit.get_current_price("KRW-DOGE")


#최근 200시간의 데이터 불러옴
#df = pyupbit.get_ohlcv("KRW-BTC", count=600, period=1)
df = pyupbit.get_ohlcv("KRW-DOGE", interval="minute60")

#시간(ds)와 종가(y)값만 남김
df = df.reset_index()
df['ds'] = df['index']
df['y'] = df['close']
data = df[['ds','y']]
data


#학습
#model = Prophet()
model = Prophet()

model.fit(data)


#24시간 미래 예측
future = model.make_future_dataframe(periods=24, freq='H')
forecast = model.predict(future)

#그래프1
fig1 = model.plot(forecast)

#그래프2
fig2 = model.plot_components(forecast)

#종가의 가격을 구함

#현재 시간이 자정 이전
closeDf = forecast[forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9)]

#현재 시간이 자정 이후
if len(closeDf) == 0:
  closeDf = forecast[forecast['ds'] == data.iloc[-1]['ds'].replace(hour=9)]

#어쨋든 당일 종가
closeValue = closeDf['yhat'].values[0]
# closeValue

#구체적인 가격
print("현재가: ", nowValue)
print("예측가: ", closeValue)

forecast
