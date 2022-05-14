import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd


# Модуль для установки таймзоны
import pytz

# установим подключение к терминалу MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Установка таймзоны
time_zone = pytz.timezone("Etc/UTC")
utc_from = datetime(2016, 9, 13, tzinfo=time_zone)
utc_to = datetime(2020, 12, 16, tzinfo=time_zone)

# Данные курса
wti_ticks = mt5.copy_rates_range("WTI", mt5.TIMEFRAME_H1, utc_from, utc_to)
usdrub_ticks = mt5.copy_rates_range("USDRUB", mt5.TIMEFRAME_H1, utc_from, utc_to)
usdjpy_ticks = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_H1, utc_from, utc_to)
usdchf_ticks = mt5.copy_rates_range("USDCHF", mt5.TIMEFRAME_H1, utc_from, utc_to)
usdgbp_ticks = mt5.copy_rates_range("GBPUSD", mt5.TIMEFRAME_H1, utc_from, utc_to)
usdeur_ticks = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_H1, utc_from, utc_to)
mt5.shutdown()

# Из полученных в Dataframe
ticks_frame_usdrub = pd.DataFrame(usdrub_ticks)
ticks_frame_wti = pd.DataFrame(wti_ticks)
ticks_frame_usdjpy = pd.DataFrame(usdjpy_ticks)
ticks_frame_usdchf = pd.DataFrame(usdchf_ticks)
ticks_frame_usdgbp = pd.DataFrame(usdgbp_ticks)
ticks_frame_usdeur = pd.DataFrame(usdeur_ticks)

# Данные в секундах
ticks_frame_wti['time'] = pd.to_datetime(ticks_frame_wti['time'], unit='s')
ticks_frame_usdrub['time'] = pd.to_datetime(ticks_frame_usdrub['time'], unit='s')
ticks_frame_usdjpy['time'] = pd.to_datetime(ticks_frame_usdjpy['time'], unit='s')
ticks_frame_usdchf['time'] = pd.to_datetime(ticks_frame_usdchf['time'], unit='s')
ticks_frame_usdgbp['time'] = pd.to_datetime(ticks_frame_usdgbp['time'], unit='s')
ticks_frame_usdeur['time'] = pd.to_datetime(ticks_frame_usdeur['time'], unit='s')

# Всё в csv
ticks_frame_usdrub.to_csv('data/data_usdrub.csv', sep=';', encoding='utf-8')
ticks_frame_wti.to_csv('data/data_wti.csv', sep=';', encoding='utf-8')
ticks_frame_usdjpy.to_csv('data/data_usdjpy.csv', sep=';', encoding='utf-8')
ticks_frame_usdchf.to_csv('data/data_usdchf.csv', sep=';', encoding='utf-8')
ticks_frame_usdgbp.to_csv('data/data_usdgbp.csv', sep=';', encoding='utf-8')
ticks_frame_usdeur.to_csv('data/data_usdeur.csv', sep=';', encoding='utf-8')



