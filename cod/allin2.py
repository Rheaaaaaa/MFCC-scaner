import os
import pandas as pd

# 输入和输出文件夹路径
input_dir = 'C:\\Users\\23367\\Desktop\\voi\\feat2'
output_file = 'C:\\Users\\23367\\Desktop\\voi\\feature_allin2.csv'

# 用于存储所有文件的 DataFrame 列表
dataframes = []

# 遍历目录中的所有 CSV 文件
for file_name in os.listdir(input_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(input_dir, file_name)

        # 读取 CSV 文件
        df = pd.read_csv(file_path)

        # 根据文件名添加额外的列
        df['state'] = file_name[0]
        df['driver'] = file_name[1:3]
        df['point'] = range(1, len(df) + 1)

        # 将 DataFrame 添加到列表中
        dataframes.append(df)

# 合并所有 DataFrame
all_data = pd.concat(dataframes, ignore_index=True)

# 保存到新的 CSV 文件
all_data.to_csv(output_file, index=False)

print(f"All data combined and saved to {output_file}")
