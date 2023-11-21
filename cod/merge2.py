import os
import pandas as pd
import numpy as np
import glob

def round_timestamp(timestamp):
    # 四舍五入到最接近的0.05的倍数
    return round(timestamp / 0.05) * 0.05

# 输入文件夹路径
a_feature_dir = 'C:\\Users\\23367\\Desktop\\voi\\csv'
b_feature_dir = 'C:\\Users\\23367\\Desktop\\dat\\unlabel0'
output_dir = 'C:\\Users\\23367\\Desktop\\voi\\merge2'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 处理每个 A/B 类数据
for a_file in os.listdir(a_feature_dir):
    if a_file.endswith('.csv'):
        category = 'A' if a_file[0] == 'a' else 'B'
        driver_id = a_file[1:3]

        # 读取 A 组特征数据
        a_path = os.path.join(a_feature_dir, a_file)
        a_data = pd.read_csv(a_path)
        a_data['Timestamp'] = a_data['Timestamp'].apply(round_timestamp)

        # 找到对应的 B 组数据
        b_subdir = 'anger' if category == 'A' else 'baseline'
        b_path = os.path.join(b_feature_dir, b_subdir, f"{driver_id}*.csv")
        
        # 可能有多个匹配的文件，这里只选取第一个
        b_files = glob.glob(b_path)
        if not b_files:
            continue
        b_file = b_files[0]
        
        # 读取 B 组特征数据
        b_data = pd.read_csv(b_file, skiprows=[1])
        b_data.rename(columns={b_data.columns[0]: 'Timestamp'}, inplace=True)
        b_data['Timestamp'] = b_data['Timestamp'].apply(round_timestamp)

        # 合并数据
        merged_data = pd.merge(a_data, b_data, on='Timestamp')

        # 保存合并后的数据
        output_file = os.path.join(output_dir, f"{category}{driver_id}.csv")
        merged_data.to_csv(output_file, index=False)

        print(f"Merged data saved to {output_file}")
