import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


dataset = pd.read_csv('Ice_cream_selling_data.csv')


dataset


dataset.shape


X = dataset.iloc[:,0].values.reshape(-1,1)


y = dataset.iloc[:,1].values


plt.scatter(X,y)
plt.title('Temperature vs Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales (units)')
plt.show()


from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0,test_size=0.2)


X_train.shape


X_test.shape


from sklearn.linear_model import LinearRegression


model = LinearRegression()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


from sklearn.metrics import mean_squared_error


print(mean_squared_error(y_test,y_pred))


from sklearn.metrics import r2_score


print(r2_score(y_test, y_pred))


plt.scatter(X,y)
plt.plot(X,model.predict(X))
plt.title('Temperature vs Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales (units)')
plt.show()


model.predict([[30]])


from sklearn.preprocessing import PolynomialFeatures


poly_Features = PolynomialFeatures(degree=2)


trasform_poly = poly_Features.fit_transform(X_train)


poly_model = LinearRegression()


poly_model.fit(trasform_poly, y_train)


poly_model.score(trasform_poly,y_train)


transform_poly_test = poly_Features.transform(X_test)


y_pred_poly = poly_model.predict(transform_poly_test)


print("MSE:", mean_squared_error(y_test, y_pred_poly))
print("R2 Score:", r2_score(y_test, y_pred_poly))


poly_model.score(trasform_poly,y_train)


X_poly = poly_Features.transform(X)

y_poly_pred = poly_model.predict(X_poly)


plt.scatter(dataset['Temperature (°C)'],dataset['Ice Cream Sales (units)'])
plt.plot(X, y_poly_pred)
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales (units)')
plt.show()
