# MFCC-scaner

## 有标签数据

原始数据都在dat文件夹里
处理数据都在voi文件夹中 


**》voi** 

  **》WAV**：裁剪好的音频 
  
    a/b + driver .WAV 
    
  via **mfcc.py** 
  
  》**csv**：提取音频里的MFCC特征 
  
    时间 - 13个MFCC特征
    a/b + driver .csv
    
  via **merge.py**
  
  》**merge**：合并子任务的scaner和时段对应的MFCC
  
    时间 - 13个MFCC - 53个scaner - 1个label
    A/B + driver - task .csv
   
   via **feature.py**
   
  》**feat**：滑动时间窗，提13个MFCC和8个scaner对应的5个指标
  
    13×5个MFCC - 8×5个scaner - 1个label
    A/B + driver - task .csv
  
   via **allin.py**

  》**feature_allin.csv**
  
    13×5个MFCC - 8×5个scaner - 1个label - A/B - driver - task - point

   然后把后4列删掉存储在里dat/input_label.csv

   然后把23-4 28-5 label从4改成5 重新存储为dat/input_label0.csv
   

   **separate.py** 是用来分割训练集和测试集
   

## 无标签数据

   **trans.py** 是用来把unlabel里面分号分隔的csv变成好编辑的逗号分割csv
   
   **》csv**：提取音频里的MFCC特征
    
    时间 - 13个MFCC特征
    a/b + driver .csv
   
   via **merge2.py**
  
  》**merge2**：合并全程scaner和对应的MFCC 
  
    时间 - 13个MFCC - 53个scaner
    A/B + driver .csv
  
   via **feature2.py**
  
  》**feat2**：滑动时间窗，提13个MFCC和8个scaner对应的5个指标
  
    13×5个MFCC - 8×5个scaner
    A/B + driver .csv
  
   via **allin2.py**
   
  》**feature_allin2.csv**
  
    13×5个MFCC - 8×5个scaner - A/B - driver - point
    
   然后把后三列删掉存储在里dat/input_unlabel.csv






    
  
