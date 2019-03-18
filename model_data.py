import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import linear_model

def model(eid):
	#print(psutil.cpu_percent(interval=1))

	list1 = ["keyclicks",
	"Mouseclicks",
	"time",
	"cpu_idle_state",
	"ram_usage",
	"priority",
	"web browser",
	"coding",
	"documentation",
	"uml Diag",
	"others"]
#Prority attribute- The experience level of the developer in the industry.


#Considered random values as there's no data available from the specific industry.
#The data of the above attributes must be collected inorder to use the model for production.
	v = np.c_[np.random.randint(1000,17000,size=1000),np.random.randint(100,9000,size=1000),np.random.randint(1000,15000,size=1000)]
	w = np.c_[np.random.sample(1000)*20,np.random.sample(1000)*10]
	x = np.c_[np.random.randint(1,4,size=1000)]
	y = np.c_[np.random.randint(2,size=1000),np.random.randint(2,size=1000),np.random.randint(2,size=1000),
	np.random.randint(2,size=1000),np.random.randint(2,size=1000)]
	z = np.c_[v,w,x,y]
	#print(z.shape)
	data = pd.DataFrame(z,index = np.arange(1,1001))
	data.columns = list1
	data['Efficiency'] = np.random.uniform(0,2,1000)

	data = data.values

	#print(data)

	x = data[:,0:11]
	y = data[:,11]

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 0) 

	sc_x = StandardScaler()
	x_train = sc_x.fit_transform(x_train)
	x_test = sc_x.transform(x_test)

	''''sc_y = StandardScaler()
	y_train = y_train.reshape((len(y_train), 1))
	y_train = sc_y.fit_transform(y_train)
	y_train = y_train.ravel()
	'''
#Using linear regression as of now once the data is available the data is trained on the several models.
#The model with best acuuracy is considered.

	regression = linear_model.BayesianRidge()
	regression.fit(x_train,y_train)
	y_pred=regression.predict(x_test)
	#print(y_pred)

	lm = LinearRegression()
	lm.fit(x_train,y_train)
	predict=lm.predict(x_test)
	#print(predict)
	result=predict[int(eid/10)] - np.random.randint(low=5,high=50)/100
	if result> 100:
		result -= 5 
	return result
