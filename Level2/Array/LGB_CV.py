# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
import lightgbm as lgb
from hyperopt import STATUS_OK, hp, tpe, Trials, fmin
from hyperopt.pyll.stochastic import sample


# train = pd.read_csv("../input/train.csv")
# label = pd.read_csv("../input/label.csv")
# train_set = lgb.Dataset()

def objective(params, train_set):
   cv_results = lgb.cv(params, train_set,
					   num_boost_round=10000,
					   early_stopping_rounds=100, seed=50,
					   nfold=5, stratified=True, shuffle=True,
					   metrics=['auc', 'binary'], verbose_eval=True)
   best_score = max(cv_results['auc-mean'])
   loss = 1 - best_score
   return {'loss': loss, 'params': params, 'status': STATUS_OK}


"""
LGBMClassifier(     objective='binary',
				*boosting_type='gbdt', 
					class_weight=None,
				*colsample_bytree=1.0, 
				*subsample=1.0,
				*subsample_freq=1
				*subsample_for_bin=200000, 
					learning_rate=0.1, 
					max_depth=-1,
				*num_leaves=31,  
				*min_child_samples=20,
					min_child_weight=0.001, 
					min_split_gain=0.0, 
					n_estimators=10000,
					n_jobs=-1, 
					objective=None, 
					random_state=None,
				*reg_alpha=0.0, 
				*reg_lambda=0.0, 
					silent=True)
"""

# Define the search space
space = {
	'is_balance': hp.choice('is_balance', [True, False]),
	'class_weight': hp.choice('class_weight', [None, 'balanced']),
	'boosting_type': hp.choice('boosting_type',
							[{'boosting_type': 'gbdt', 'subsample': hp.uniform('gdbt_subsample', 0.3, 1)},
							 {'boosting_type': 'dart', 'subsample': hp.uniform('dart_subsample', 0.3, 1)},
							 {'boosting_type': 'goss', 'subsample': 1.0}]),
	'learning_rate': hp.loguniform('learning_rate', np.log(0.01), np.log(0.2)),
	'min_child_samples': hp.quniform('min_child_samples', 1, 3000, 10),
	'num_leaves': hp.quniform('num_leaves', 1, 5000, 50),
	'max_bin': hp.quniform('max_bin', 10, 1000, 5),
	'min_data_in_bin': hp.quniform('min_data_in_bin', 2, 50, 2),
	'reg_alpha': hp.uniform('reg_alpha', 0.0, 1.0),
	'reg_lambda': hp.uniform('reg_lambda', 0.0, 1.0),
	'colsample_bytree': hp.uniform('colsample_by_tree', 0.3, 1.0),
	'subsample_freq': hp.quniform('subsample_freq', 1, 10, 1),
	'subsample_for_bin': hp.quniform('subsample_for_bin', 20000, 300000, 20000)
	}

