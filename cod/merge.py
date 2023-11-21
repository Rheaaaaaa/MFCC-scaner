import os
import pandas as pd

# 文件夹路径
csv_dir = 'C:\\Users\\23367\\Desktop\\voi\\csv'
xls_dir = 'C:\\Users\\23367\\Desktop\\dat\\label'
output_dir = 'C:\\Users\\23367\\Desktop\\voi\\merge'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取并处理每个 CSV 文件
for csv_file in os.listdir(csv_dir):
    if csv_file.endswith('.csv'):
        # 数据类别（A或B）
        data_category_csv = 'A' if csv_file[0] == 'a' else 'B'

        # 驾驶员编号
        driver_id_csv = csv_file[1:3]

        # 读取 CSV 文件
        csv_path = os.path.join(csv_dir, csv_file)
        csv_data = pd.read_csv(csv_path)

        # 匹配并处理相应的 XLS 文件
        for xls_file in os.listdir(xls_dir):
            if xls_file.endswith('.xls') and xls_file[2:4] == driver_id_csv:
                # XLS 文件的数据类别
                data_category_xls = 'A' if len(xls_file.rstrip('.xls')) == 7 else 'B'
                
                # 仅当 CSV 和 XLS 文件的数据类别匹配时处理
                if data_category_csv == data_category_xls:
                    # 时段序号
                    segment_number = xls_file[5:7] if data_category_xls == 'A' else xls_file[6:8]

                    # 读取 XLS 文件
                    xls_path = os.path.join(xls_dir, xls_file)
                    xls_data = pd.read_excel(xls_path)

                    # 将 "Time" 列的数据转换为最接近的 0.05 的整数倍
                    xls_data['Time'] = xls_data['Time'].apply(lambda x: round(x / 0.05) * 0.05)

                    # 获取 XLS 文件的时间范围
                    time_start = xls_data['Time'].min()
                    time_end = xls_data['Time'].max()

                    # 筛选 CSV 文件中对应的时间段
                    csv_segment = csv_data[(csv_data['Timestamp'] >= time_start) & (csv_data['Timestamp'] <= time_end)]

                    # 合并数据
                    merged_data = pd.merge(csv_segment, xls_data, left_on='Timestamp', right_on='Time', how='inner')

                    # 删除重复的时间列
                    merged_data.drop(columns=['Time'], inplace=True)

                    # 保存合并后的数据
                    output_filename = f"{data_category_csv}{driver_id_csv}{segment_number}.csv"
                    output_path = os.path.join(output_dir, output_filename)
                    merged_data.to_csv(output_path, index=False)

                    print(f"Processed and saved: {output_filename}")
