from pandas.core.base import DataError
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
import numpy as np
import pandas as pd
import seaborn as sn



def encode(categorical_data):
  """ Encode labels """
  le = LabelEncoder()
  return le.fit_transform(categorical_data)

class FeatureEngineering:
  def __init__(self,df):
    self.df = df 

  def execute_feature_engineering(self):
    """ execute feature engineering by calling
    prepare_data function and select important
    features using select_features fun"""
    self.prepare_data()
    self.select_features()

  def prepare_data(self):
    """ prepare data by calling prepare_X_y 
    and split_X_y
    """
    self.prepare_X_y()
    self.split_X_y()

  def prepare_X_y(self):
    """ Prepare X and y from a given dataframe
    by encoding categorical columns and converting
    to numpy """
    y= encode([[val]for val in self.df["diagnosis"]])
    self.df_x = self.df.drop(columns=["id","diagnosis"])
    self.X = np.array(self.df_x)
    self.y = y.reshape(-1,)


  def split_X_y(self):
    """ Split X and y using sklearn train_test_split """
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
        self.X, self.y, stratify=self.y, random_state=42)

  def return_X_y(self):
    """ return X and y """
    return self.X,self.y

  def return_split_X_y(self):
    """ return X_train, X_test, y_train and y_test """
    return self.X_train, self.X_test, self.y_train, self.y_test

  def calculate_feature_importance(self):
    """ Calculate feature importance of features by fitting 
        a randomforest classifier 
    """
    feature_names = [f'feature {i}' for i in range(self.X.shape[1])]
    forest = RandomForestClassifier(n_estimators=100)
    forest.fit(self.X_train, self.y_train)
    self.importances = forest.feature_importances_
    std = np.std([
        tree.feature_importances_ for tree in forest.estimators_], axis=0)
    return self.importances, std

  def display_feature_importance(self):
    """ Display feature importance """
    feature_df = pd.DataFrame({"features":self.df_x.columns,"feature_importance": self.importances})
    g = sn.catplot(data=feature_df,y="features",x="feature_importance",kind="bar")
    return feature_df,g

  def select_features(self):
    """ select features from a random forest estimator using 
        sklearn SelectFromModel 
    """
    selector = SelectFromModel(estimator=RandomForestClassifier(n_estimators=100)).fit(self.X, self.y)
    self.selected_features = self.df_x.columns[(selector.get_support())]
    return self.selected_features

  def data_with_selected_features(self):
    """ select data with only the features selected"""
    data_selected = self.df[self.selected_features]
    data_selected['diagnosis'] = encode(self.df['diagnosis'])
    return data_selected