import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import missingno

####
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn_features.transformers import DataFrameSelector

###sklearn -- metrics
from sklearn.metrics import mean_squared_error

# skleran ---model
from xgboost import XGBRegressor

###using pandas
TRAIN_DATA_PATH = os.path.join(os.getcwd(), "Data.csv")
df = pd.read_csv(TRAIN_DATA_PATH)
####split
df["Club"] = df["Club"].str.strip("()")

#feature extraction 
df['Minutes_Per_Match'] = df['Mins'] / df['Matches_Played']
df['Shooting_Accuracy'] = df['OnTarget'] / df['Shots']
 
 #drop the null value in colum club 
df = df.dropna(subset=["Club"])

# Reset the index
df= df.reset_index(drop=True)
###target
df["xG"]


###split the feature and target
x = df.drop(columns=["xG"], axis=1)
y = df["xG"]

##split to train and test
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, shuffle=True, random_state=45
)


###Numerical : 'fee million euros', 'fee million sterling', 'Year', 'Born'& imputing (median) & scaling (standrad)
##categorical :'Origin', 'Player', 'From_Country', 'From_Club', 'To_Country', 'To_Club', 'Position'&imputing (mode) & encoding (labelencoding)
num_col = x_train.select_dtypes(include="number").columns.tolist()
categ_col = x_train.select_dtypes(exclude="number").columns.tolist()

print(x_train.columns)

####pipline
num_pipe = Pipeline(
    steps=[
        ("selector", DataFrameSelector(num_col)),
        ##("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)
categ_pipe = Pipeline(
    steps=[
        ("selector", DataFrameSelector(categ_col)),
       ## ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)
all_pipe = FeatureUnion(
    transformer_list=[("categorical", categ_pipe), ("numerical", num_pipe)]
)


_ = all_pipe.fit(x_train)


def process_new(x_new):

    df_new=pd.DataFrame([x_new])
    df_new.columns = x_train.columns

    ####
    df_new["Country"] = df_new["Country"].astype('str')
    df_new["Club"] = df_new["Club"].astype('str')
    df_new["Player Names"] = df_new["Player Names"].astype('str')
    df_new['Matches_Played']=df_new['Matches_Played'].astype('int')
    df_new["Substitution "] = df_new["Substitution "].astype('int')
    df_new["Mins"] = df_new["Mins"].astype('int')
    df_new["Goals"] = pd.to_numeric(df_new["Goals"], errors='coerce')
    df_new["xG Per Avg Match"] = df_new["xG Per Avg Match"].astype('float')
    df_new["Shots"] = df_new["Shots"].astype('int')
    df_new["OnTarget"] = pd.to_numeric(df_new["OnTarget"], errors='coerce').fillna(0).astype(int)
    df_new["Shots Per Avg Match"] = df_new["Shots Per Avg Match"].astype('float')
    df_new["On Target Per Avg Match"] = df_new["On Target Per Avg Match"].astype('float')
    df_new["Year"] = df_new["Year"].astype('int')
    df_new['Minutes_Per_Match']=df_new['Minutes_Per_Match'].astype('float')
    df_new = df_new[pd.to_numeric(df_new['Shooting_Accuracy'], errors='coerce').notnull()]

    

    x_process = all_pipe.transform(df_new)

    return x_process
