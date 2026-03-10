import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# step 1 : Load the dataset

DatasetPath = "Advertising.csv"
df = pd.read_csv(DatasetPath)

print(df.shape)

# Data cleaning 
if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'],inplace = True)

print(df.shape)

# split the data into X and Y

X = df[['TV','radio','newspaper']]
Y = df['sales']


print("independent variables :",X.shape)
print("independent variables :",Y.shape)

# Split the data for training and testing

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("testing data :")
print(X_test)

print("Predicted values :")
print(Y_pred)

print("Actual Values")
print(Y_test)
