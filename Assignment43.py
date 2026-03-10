import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


Border = "-"*40

########################################################################
# Step 1 : Load the dataset
########################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "PlayPredictor.csv"
df = pd.read_csv(DatasetPath)

########################################################################
# Step 2 : Data analysis (EDA)
########################################################################

print(Border)
print("Step 2 : Data analysis")
print(Border)

print("Shape of dataset : ",df.shape)  # shape is a feature it shows numbers of row and colom 
print("Colomn Name  : ",list(df.columns)) 

if 'Unnamed: 0'in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace = True)

print("Missing values(Per Column)")
print(df.isnull().sum())

print("Class Distribution (Whether count)")
print(df["Whether"].value_counts())

print("Statistical Report of dataset")
print(df.describe())

print("Encoding of Independent  and Dependent  variables ")
encoder = LabelEncoder()

#df[Pay_encoded'] = encoder.fit_transform(df['Play']) jar ek col encoding karaycha asel tr

# Merge with original

for col in ['Whether','Temperature','Play']:
    df[col+'_encoded'] = encoder.fit_transform(df[col])

# print(df)


########################################################################
# Step 3 : Seperate Independent and Dependent Variables
########################################################################

print(Border)
print("Step 3 : Seperate Independent and Dependent Variables")
print(Border)

X = df[['Whether_encoded' , 'Temperature_encoded']]
Y = df['Play_encoded']


########################################################################
# Step 3 : split the data for training and testing 
########################################################################

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.5,random_state = 42)
      
model = KNeighborsClassifier(n_neighbors=7)

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)


print("Accuracy is",accuracy *100)





