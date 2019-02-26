# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 14:40
# @Author  : Lvpengfei

import pandas as pd
from hyperopt import hp, fmin, rand, tpe, space_eval, Trials, STATUS_OK
from hyperopt.pyll.stochastic import sample


# 第一步：定义要最小化的实数值目标函数，
def q(args):
	x, y = args
	loss = x**2 + y**2
	# return {'loss': loss, 'params': args, 'status': STATUS_OK}
	return loss

# 第二步：指定参数空间
space = [hp.uniform('x', 0, 1),
         hp.normal('y', 0, 1)]

trials = Trials()
# 第三步：运行fmin，得最优参数
best = fmin(q, space, tpe.suggest, max_evals=10, trials=trials)
print(best)
print(space_eval(space, best))

# 第四步：结果分析
# for info in trials.trials:
# 	print(info['tid'], " 1-auc: %.10f"%(info['result']['loss']), " params: ", info['misc']['vals'])
record = {'tid': [], 'loss': []}
sp = ['x', 'y']
for p in sp:
	record[p] = []

for info in trials.trials:
	record['tid'].append(info['tid'])
	record['loss'].append(info['result']['loss'])
	for p in sp:
		record[p].append(info['misc']['vals'][p][0])

pd.DataFrame(data=record).to_csv("record.csv", index=False)
