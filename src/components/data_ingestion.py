import os
import sys
import pandas as pd

#Add file path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.exception import customException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifcats','train_csv')
    test_data_path: str=os.path.join('artifcats','test_csv')
    raw_data_path: str=os.path.join('artifcats','data_csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data regression method or component")
        try:
            df=pd.read_csv('notebook/data/StudentsPerformance.csv')
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train-test split intiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
           
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is compeleted")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise customException(e,sys)

    