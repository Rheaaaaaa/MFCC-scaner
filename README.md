# MFCC-scaner

## 有标签数据

数据都在voi文件夹中 


**》voi** 

  **》WAV**：裁剪好的音频 
  
    a/b + driver .WAV 
  | 
  | **mfcc.py** 
  ↓ 
  》**csv**：提取音频里的MFCC特征
    时间 - 13个MFCC特征
    a/b + driver .csv
  |
  | **merge.py**
  ↓
  》**merge**：合并子任务的scaner和时段对应的MFCC
    时间 - 13个MFCC - 53个scaner - 1个label
    A/B + driver - task .csv
  |
  | **feature.py**
  ↓
  》**feat**：滑动时间窗，提13个MFCC和8个scaner对应的5个指标
    13×5个MFCC - 8×5个scaner - 1个label
    A/B + driver - task .csv
  |
  | **allin.py**
  ↓
  》**feature_allin.csv**
    13×5个MFCC - 8×5个scaner - 1个label - A/B - driver - task - point

## 无标签数据

**》voi**
    》**csv**：提取音频里的MFCC特征
    时间 - 13个MFCC特征
    a/b + driver .csv
  |
  | **merge2.py**
  ↓
  》**merge2**：合并全程scaner和对应的MFCC
    时间 - 13个MFCC - 53个scaner
    A/B + driver .csv
  |
  | **feature2.py**
  ↓
  》**feat2**：滑动时间窗，提13个MFCC和8个scaner对应的5个指标
    13×5个MFCC - 8×5个scaner
    A/B + driver .csv
  |
  | **allin2.py**
  ↓
  》**feature_allin2.csv**
    13×5个MFCC - 8×5个scaner - A/B - driver - point
    
  
