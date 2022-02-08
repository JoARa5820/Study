#---------------------------------------------------------------------------------------------
# 경로상의 폴더 존재 유무 확인 후 폴더가 존재하지 않으면 생성하는 함수
# INPUT : str : 폴더 경로
#---------------------------------------------------------------------------------------------
import os

def mkdir_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

#경로 지정
# PRJ_PATH = 'D:/dev/SEP/'
PRJ_PATH = 'C:/Users/aiforpet/Desktop/special_edu/seo_code/'

DATA_PATH = PRJ_PATH + '01_Data/'
RESULT_PATH = PRJ_PATH + '03_Result/'
LOG_PATH = PRJ_PATH + '99_Log/'

RAW_DATA_PATH = DATA_PATH + '01_raw_data/'
PRE_DATA_PATH = DATA_PATH + '02_preprocessing/'

#해당 폴더가 없을 경우 폴더 생성
mkdir_if_not_exists(RESULT_PATH)
mkdir_if_not_exists(LOG_PATH)
mkdir_if_not_exists(PRE_DATA_PATH)

