#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from hypergbm import make_experiment
from hypernets.tabular.metrics import metric_to_scoring


# In[2]:


train_data = pd.read_csv('C:\\Users\\Pro\\Desktop\\0516\\train.csv')
test_data = pd.read_csv('C:\\Users\\Pro\\Desktop\\0516\\test.csv')
X_train = train_data.copy()
y_train = X_train.pop('anger')
X_test = test_data.copy()
y_test = X_test.pop('anger')

X_test


# In[6]:


webui_options = {
    'event_file_dir': "./events",  # persist experiment running events log to './events'
    'server_port': 8888, # http server port
    'exit_web_server_on_finish': False  # exit http server after experiment finished
}
experiment = make_experiment(train_data.copy(), 
                             test_data=X_test.copy(),
                             target='anger',
                             
                             class_balancing='SMOTE',
                             
                             
                             collinearity_detection=True,
                             drift_detection=False,
                             
                             searcher='MCTSSearcher',
                             
                             pseudo_labeling=True,
                             pseudo_labeling_proba_threshold=0.7,
                             
                             random_state=8888, 
                             max_trials=30, 
                             early_stopping_rounds=15,
                             
                             
                             feature_reselection=True, 
                             feature_reselection_threshold=0.005,
                             
                             cv=True, num_folds=3,
                             reward_metric='auc',
                             
                             ensemble_size=0,
                             
                             webui=True,
                             webui_options=webui_options,
                             
                             trial_store='/tmp/trial_store',
                             )

estimator = experiment.run()

#estimator.steps
print(estimator)


# In[7]:


from sklearn.metrics import classification_report

y_pred=estimator.predict(X_test)
print(classification_report(y_test, y_pred, digits=5))


# In[8]:


def classifier_metrics_by_self(y_true, y_pred):

    num_true = 0
    for i in range(len(y_true)):
        if (y_true[i]-y_pred[i])<=1 and (y_true[i]-y_pred[i])>=-1:
            num_true += 1

    accuracy_fuzzy = num_true / len(y_true)

    print('accuracy_fuzzy: {:.10f}'.format(accuracy_fuzzy))
    
if __name__ == '__main__':
    y_true = y_test
    y_pred = y_pred
    classifier_metrics_by_self(y_true, y_pred)


# In[9]:


import numpy as np
y_pred = estimator.predict(X_test).astype(np.float64)

print(y_pred)

from sklearn.metrics import accuracy_score,recall_score,confusion_matrix
accuracy_score(y_test, y_pred)
#recall_score(y_test, y_pred, average='weighted')
conf_mat =confusion_matrix(y_test, y_pred, labels=None, sample_weight=None)
conf_mat


# In[10]:


import seaborn as sns
import csv
figure, axes = plt.subplots(2,2, figsize=(16*1.25, 16))
cf_matrix = confusion_matrix(y_test, y_pred, labels=None, sample_weight=None)

# 混淆矩阵
ax = sns.heatmap(cf_matrix, annot=True, fmt='g', ax=axes[0][0], cmap='Blues', annot_kws={"fontsize":15})
ax.title.set_text("Confusion Matrix")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")
# plt.savefig(csv_path.replace(".csv", "_cf_matrix.png"))
# plt.show()
 
# 混淆矩阵 - 百分比
ax = sns.heatmap(cf_matrix / np.sum(cf_matrix), annot=True, ax=axes[0][1], fmt='.1%', cmap='Blues', annot_kws={"fontsize":15})
ax.title.set_text("Confusion Matrix (percent)")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")

# plt.savefig(csv_path.replace(".csv", "_cf_matrix_p.png"))
# plt.show()
 
# 召回矩阵，行和为1
sum_true = np.expand_dims(np.sum(cf_matrix, axis=1), axis=1)
precision_matrix = cf_matrix / sum_true
ax = sns.heatmap(precision_matrix, annot=True, fmt='.1%', ax=axes[1][0], cmap='Blues', annot_kws={"fontsize":15})
ax.title.set_text("Precision Matrix")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")

# plt.savefig(csv_path.replace(".csv", "_recall.png"))
# plt.show()
 
# 精准矩阵，列和为1
sum_pred = np.expand_dims(np.sum(cf_matrix, axis=0), axis=0)
recall_matrix = cf_matrix / sum_pred
ax = sns.heatmap(recall_matrix, annot=True, fmt='.1%', ax=axes[1][1], cmap='Blues', annot_kws={"fontsize":15})
ax.title.set_text("Recall Matrix")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")
# plt.savefig(csv_path.replace(".csv", "_precision.png"))
# plt.show()
 
# 绘制4张图
plt.autoscale(enable=False)
plt.savefig('C:\\Users\\Pro\\Desktop\\Matrix.png', bbox_inches='tight', pad_inches=0.2)
plt.show()


# In[42]:


data = pd.DataFrame(y_pred)
print("data的type: {}".format(type(data)))
print("data的shape: {}".format(data.shape))
print(data)

data.to_csv('C:\\Users\\Pro\\Desktop\\result.csv', index=False)  # 保存






