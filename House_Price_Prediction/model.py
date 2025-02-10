import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("minihomeprices.csv")

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df["bedrooms"].fillna(df["bedrooms"].median(), inplace=True) #we use median to fill the missing part
df["bedrooms"] = df["bedrooms"].astype("int64") #ensure the bedroom column is an integer 64

sns.pairplot(df, diag_kind='kde') #Creates pairplots of all numeric variables to visualize relationships
plt.show() #KDE = Kernel Density Estimation


X = df.drop(["price"], axis=1) 
y = df["price"] #target = price

mdl = LinearRegression() #create a linear regression model
mdl.fit(X, y) #trains the model 

y_pred = mdl.predict(X) #predicts the price  using the model

print("Intercept:", mdl.intercept_) 
print("Coefficients:", mdl.coef_) # effect on each feature on the price
print("R-squared score:", mdl.score(X, y)) #Measures how well the model explains the data (higher is better)

plt.figure(figsize=(12, 5))
plt.scatter(y, y_pred, color="green", alpha=0.5)
plt.plot([min(y), max(y)], [min(y), max(y)], linestyle="dashed", color="black")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")

plt.show()
