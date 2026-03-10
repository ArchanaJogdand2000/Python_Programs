import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

#  Step 1 : Load data 

Datasetpath = 'WinePredictor.csv'

df = pd.read_csv(Datasetpath)
print(df.head())

# Step 2  : clean the data by removing empty row

df.dropna(inplace = True)

# Step 3 : Seperate Independent and Dependent Variables

X = df.drop(columns=['Class'])
Y = df['Class']


print("shape of x :",X.shape)
print("shape of y :",Y.shape)

# Step 4 : Split the dataset for training and testing 


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2 , random_state=42,stratify=Y)

print("Information of traning and testing data")
print("X_train shape :",X_train.shape)
print("Xtest shape :",X_test.shape)
print("Y_train shape :",Y_train.shape)
print("Y_test shape :",Y_test.shape)

# training and testing 

model = DecisionTreeClassifier()

model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy is",accuracy *100)
