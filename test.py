
import pandas as pd
import matplotlib as plot

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz = 360)

kw_list = ["Jeff Bezos", "Divorce"]

pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y') 

data = pytrends.interest_over_time() 
data = data.reset_index() 


import plotly.express as px

fig = px.line(data, x="date", y=['Jeff Bezos', 'Divorce'], title='Keyword Web Search Interest Over Time')
fig.show()