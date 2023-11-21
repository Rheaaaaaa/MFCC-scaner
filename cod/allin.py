import os
import pandas as pd

# 输入和输出文件夹路径
input_dir = 'C:\\Users\\23367\\Desktop\\voi\\feat'
output_file = 'C:\\Users\\23367\\Desktop\\voi\\feature_allin.csv'

# 用于存储所有文件的 DataFrame 列表
dataframes = []

# 遍历目录中的所有 CSV 文件
for file_name in os.listdir(input_dir):
    if file_name.endswith('.csv'):
        file_path = os.path.join(input_dir, file_name)

        # 检查文件是否为空或存在格式问题
        if os.stat(file_path).st_size == 0:
            print(f"Skipping empty or invalid file: {file_name}")
            continue

        try:
            # 读取 CSV 文件
            df = pd.read_csv(file_path)

            # 根据文件名添加额外的列
            df['state'] = file_name[0]
            df['driver'] = file_name[1:3]
            df['task'] = file_name[3:5]

            # 为每行添加 point 列（行号）
            df['point'] = range(1, len(df) + 1)

            # 将 DataFrame 添加到列表中
            dataframes.append(df)
        except pd.errors.EmptyDataError:
            print(f"Error reading file: {file_name}, skipping.")

# 合并所有 DataFrame
all_data = pd.concat(dataframes, ignore_index=True)

# 保存到新的 CSV 文件
all_data.to_csv(output_file, index=False)

print(f"All data combined and saved to {output_file}")
