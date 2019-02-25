# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 15:51
# @Author  : Lvpengfei

import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import GridSearchCV


train = pd.read_csv("../input/train.csv")
label = pd.read_csv("../input/label.csv")

# 首先固定一些参数
params = {"boosting_type": "gbdt",
          "learning_rate": 0.1,
          "n_estimators": 10000,
          "max_depth": -1,
		  "subsample": 0.75,
		  "colsample_bytree": 0.75,
          "early_stopping_round": 50,
          "n_thread": -1,
          }

print("[1]>>> tunning: num_leaves、min_data_in_leaf")
params_1 = {"num_leaves": [2**9, 2**12],
           "min_data_in_leaf": [50, 500]}
gs1 = GridSearchCV(estimator=lgb.Booster(params),
                   param_grid=params_1,
                   scoring='roc_auc',
                   iid=False,
                   cv=5,
                   refit=True,
                   verbose=10)
gs1.fit(train, label)
print("gs1 score...\n", gs1.cv_results_)
print("gs1 param...\n", gs1.best_params_)
print("gs1 best score...", gs1.best_score_)
