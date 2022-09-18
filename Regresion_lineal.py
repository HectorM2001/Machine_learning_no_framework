import numpy as np
import pandas as pd
import requests
import io
columns = ["id","date","price","bedrooms","bathrooms","sqft_living","sqft_lot","floors","waterfront","view","condition","grade","sqft_above","sqft_basement","yr_built","yr_renovated","zipcode","lat","long","sqft_living15","sqft_lot15"]
url = "https://raw.githubusercontent.com/HectorM2001/Machine_learning_no_framework/main/kc_house_data.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')), names=columns)
df
x = list(df['sqft_living'])
x.remove('sqft_living')
x=[float(i) for i in x]
x_test=[int(i) for i in x]
y = list(df['price'])
y.remove('price')
y=[float(i) for i in y]
xy=0
xsqrd=0
xsum=sum(x)
xsum=int(xsum)
ysum=sum(y)
n=len(x)
test=list(range(0,max(x_test)+5))
xmean=xsum/n
ymean=ysum/n
for i in range(n):
  xy=xy+(x[i]*y[i])
for i in range(n):
  xsqrd=xsqrd+(x[i]*x[i])
m=((n*xy)-(xsum*ysum))/((n*xsqrd)-(xsum^2))
b=ymean-(m*xmean)
test_n = [((m*i)+b) for i in test]
##Siguiendo este modelo predeciremos el costo que deberia tener una casa con 20000 pies cuadrados de sala
y_pred=((m*20000)+b)
y_pred=str(y_pred)
print("Una casa con 20000 pies cuadrados en la sala deberia de costar "+y_pred)


