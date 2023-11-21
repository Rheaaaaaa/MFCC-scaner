import scipy.io.wavfile as wav
from python_speech_features import mfcc
import pandas as pd
import os

path = 'C:\\Users\\23367\\Desktop\\voi\\'

def extract_mfcc_to_csv(wav_file_path, csv_file_path):
    # 读取 WAV 文件
    sr, audio = wav.read(wav_file_path)

    # 如果是立体声（双声道），只取一个声道
    if audio.ndim > 1:
        audio = audio[:, 0]

    # 计算 MFCC 特征
    mfcc_features = mfcc(audio, samplerate=sr, nfft=2205, winlen=0.05, winstep=0.05, numcep=13)

    # 创建时间戳
    timestamps = [i * 0.05 for i in range(len(mfcc_features))]

    # 转换为 DataFrame
    mfcc_df = pd.DataFrame(mfcc_features, columns=[f'MFCC_{i+1}' for i in range(13)])
    mfcc_df.insert(0, 'Timestamp', timestamps)

    # 保存为 CSV 文件
    mfcc_df.to_csv(csv_file_path, index=False)
    print(f"MFCC features saved to {csv_file_path}")

# 使用示例
allfilenames = os.listdir(path + 'WAV')
list=[]
for i in range (len(allfilenames)):
    filename = allfilenames[i]
    name = filename[0:3]
    wav_file_path = path + 'WAV\\' + filename # 请替换为您的文件路径
    csv_file_path = path + 'csv\\' + name+ '.csv' # 请替换为您想要保存的文件路径
    extract_mfcc_to_csv(wav_file_path, csv_file_path)
    print("FINISH:", name)


