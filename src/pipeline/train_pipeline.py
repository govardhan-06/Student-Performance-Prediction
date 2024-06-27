import os
import sys

from src.exception import customException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        pass

    def initiate_training_phase(self):
        try:
            logging.info("Initiated Training pipeline...")
            data_ingestion=DataIngestion()
            train_data,test_data=data_ingestion.initiate_data_ingestion()

            data_transformation=DataTransformation()
            train_array,test_array,preprocessor=data_transformation.initiate_data_transformation(train_data,test_data)

            modelTrainer=ModelTrainer()
            print(modelTrainer.initiate_model_trainer(train_array,test_array,preprocessor))
            logging.info("Model Training complete")
        except Exception as e:
            raise customException(e,sys)
    