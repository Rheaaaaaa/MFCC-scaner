import os
import pandas as pd

# 输入和输出文件夹路径
input_dir = 'C:\\Users\\23367\\Desktop\\dat\\unlabel'
output_dir = 'C:\\Users\\23367\\Desktop\\dat\\unlabel0'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历 unlabel 文件夹中的所有子文件夹
for subdir in os.listdir(input_dir):
    subdir_path = os.path.join(input_dir, subdir)
    if os.path.isdir(subdir_path):
        # 为每个子目录创建对应的输出目录
        output_subdir = os.path.join(output_dir, subdir)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # 处理子目录中的每个 CSV 文件
        for file_name in os.listdir(subdir_path):
            if file_name.endswith('.csv'):
                file_path = os.path.join(subdir_path, file_name)
                output_file_path = os.path.join(output_subdir, file_name)

                # 读取 CSV 文件，跳过第二行
                df = pd.read_csv(file_path, sep=';', skiprows=[1])

                # 保存为以逗号分隔的格式
                df.to_csv(output_file_path, index=False)

                print(f"Processed and saved: {file_name}")

print("All files have been processed and saved in the new format.")
