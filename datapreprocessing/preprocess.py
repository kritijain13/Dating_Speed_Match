from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd

class Data:
    def preprocess_data(self,x):
        
       
        cat_col=x.select_dtypes(include='object').columns
        num_col=x.select_dtypes(exclude='object').columns

        print("Categorical columns:", cat_col)
        print("Numeric columns:", num_col)

        cat_pipeline=Pipeline(
            steps=[('impute',SimpleImputer(strategy='most_frequent')),
                   ('encoding',OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=-1))]
        )
        


        num_pipeline=Pipeline(
            steps=[('imputer',SimpleImputer(strategy='median')),
                   ('scaler',StandardScaler())]
        )

        preprocessor=ColumnTransformer(
            transformers=[('numeric',num_pipeline,num_col),
                          ('categorical',cat_pipeline,cat_col)]
        )

       
        return preprocessor
