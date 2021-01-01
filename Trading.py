
import numpy as np
import pandas as pd
import math
import requests


data = pd.read_csv("CF-Insider-Trading-equities-29-09-2020-to-29-12-2020.csv")
final = pd.DataFrame()
x = pd.DataFrame()

final['Symbol']=data['SYMBOL \n']

final['Transaction Type']=data['ACQUISITION/DISPOSAL TRANSACTION TYPE \n']
final['Number of Securities']=pd.to_numeric(data['NO. OF SECURITIES (ACQUIRED/DISPLOSED) \n'])
final['Value']=data['VALUE OF SECURITY (ACQUIRED/DISPLOSED) \n']


