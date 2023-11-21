import os
import pandas as pd
import numpy as np

def calculate_statistics(data, feature_name):
    return {
        f'{feature_name}_Mean': data.mean(),
        f'{feature_name}_SD': data.std(),
        f'{feature_name}_CV': data.std() / data.mean() if data.mean() != 0 else np.nan,
        f'{feature_name}_QCV': np.subtract(*np.percentile(data, [75, 25])) / np.median(data) if np.median(data) != 0 else np.nan,
        f'{feature_name}_Amp': data.max() - data.min()
    }

# 文件夹路径
input_dir = 'C:\\Users\\23367\\Desktop\\voi\\merge2'
output_dir = 'C:\\Users\\23367\\Desktop\\voi\\feat2'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 指定特征列及其名称
feature_columns = {
    1: 'MFCC_1', 2: 'MFCC_2', 3: 'MFCC_3', 4: 'MFCC_4', 5: 'MFCC_5', 6: 'MFCC_6', 7: 'MFCC_7', 8: 'MFCC_8', 9: 'MFCC_9', 10: 'MFCC_10', 11: 'MFCC_11', 12: 'MFCC_12', 13: 'MFCC_13',
    22: 'Vx', 23: 'Vy', 25: 'Ax', 26: 'Ay', 15: 'LP', 19: 'TLC'
}

named_feature_columns = {
    'Yaw speed': 'Vyaw', 'Yaw acceleration': 'Ayaw'
    }

# 处理每个 CSV 文件
for file_name in os.listdir(input_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(input_dir, file_name)
        data = pd.read_csv(file_path)

        # 滑动窗口大小和步长（以秒为单位）
        window_size = 3
        step_size = 1

        # 处理每个滑动窗口
        output_data = []
        for start_time in np.arange(data['Timestamp'].min(), data['Timestamp'].max(), step_size):
            end_time = start_time + window_size
            window = data[(data['Timestamp'] >= start_time) & (data['Timestamp'] < end_time)]
            if window.empty:
                continue

            window_features = {}
            # 计算每个特征的统计量
            for col_name, feature_name in feature_columns.items():
                if col_name in data.columns:
                    window_features.update(calculate_statistics(window[col_name], feature_name))
                elif isinstance(col_name, int) and col_name < len(data.columns):
                    window_features.update(calculate_statistics(window.iloc[:, col_name], feature_name))

            output_data.append(window_features)

        # 创建 DataFrame 并保存
        output_df = pd.DataFrame(output_data)
        output_file_path = os.path.join(output_dir, file_name)
        output_df.to_csv(output_file_path, index=False)

        print(f"Processed and saved: {output_file_path}")
