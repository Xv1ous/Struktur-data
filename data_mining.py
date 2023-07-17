import time
import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US')

all_keywords = ['TikTok']
keywords = []
timeframes = ['today 12-m', 'today 5-y']

cat = '0'
geo = 'ID'
gprop = ''


def check_trends():
    for kw in all_keywords:
        keywords = [kw]
        pytrends.build_payload(keywords, cat, timeframes[0], geo, gprop)
        data = pytrends.interest_over_time()
        mean = round(data.mean(), 2)
        avg = round(data[kw][-52:].mean(), 2)
        avg2 = round(data[kw][:52].mean(), 2)
        trend = round(((avg / mean) - 1) * 100, 2)
        trend2 = round(((avg / avg2) - 1) * 100, 2)
        print(data)
        
        filename = f"{kw}_trends.csv"
        data.to_csv(filename)
        print(f"Data for {kw} saved to {filename}")
        
        time.sleep(10)

check_trends()
