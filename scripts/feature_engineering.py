from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
import numpy as np
import pandas as pd

def encode(categorical_data):
  le = LabelEncoder()
  return le.fit_transform(categorical_data)


def prepare_X_y(X,y):
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, stratify=y, random_state=42)
  return X_train, X_test, y_train, y_test

def calculate_feature_importance(X_train,y_train,X):
  feature_names = [f'feature {i}' for i in range(X.shape[1])]
  forest = RandomForestClassifier(random_state=0)
  forest.fit(X_train, y_train)
  importances = forest.feature_importances_
  std = np.std([
      tree.feature_importances_ for tree in forest.estimators_], axis=0)
  return importances, std

def select_features(X,y,data_x):
  selector = SelectFromModel(estimator=RandomForestClassifier(random_state=0)).fit(X, y)
  selected_features = data_x.columns[(selector.get_support())]
  return selected_features