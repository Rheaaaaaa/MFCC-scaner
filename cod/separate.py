import pandas as pd
from sklearn.model_selection import train_test_split

# 读取数据
file_path = 'C:\\Users\\23367\\Desktop\\dat\\input_label0.csv'
data = pd.read_csv(file_path)

# 分离特征和标签
X = data.drop(columns=['anger score'])  # 假设标签列名为 'anger score'
y = data['anger score']

# 划分训练集和测试集（40%为测试集）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=42)

# 合并特征和标签回到单个 DataFrame
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# 保存训练集和测试集
train_data.to_csv('C:\\Users\\23367\\Desktop\\dat\\train0.csv', index=False)
test_data.to_csv('C:\\Users\\23367\\Desktop\\dat\\test0.csv', index=False)

print("Train and test datasets saved successfully.")
