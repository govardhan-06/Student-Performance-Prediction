import os 
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from src.exception import customException
from src.logger import logging

from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifcats","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_arr,test_arr,preprocessor_path):
        try:
            logging.info("Split the train and test input data")

            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models={
                "LinearRegression":LinearRegression(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
                "KNeighborsRegressor":KNeighborsRegressor(),
                "AdaBoostRegressor":AdaBoostRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "RandomForestRegressor":RandomForestRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CatBoost Regressor":CatBoostRegressor()
            }

            params = {
                        "DecisionTreeRegressor": {
                            'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                        },
                        "RandomForestRegressor": {
                            'n_estimators': [8, 16, 32, 64, 128, 256]
                        },
                        "KNeighborsRegressor":{},
                        "GradientBoostingRegressor": {
                            'learning_rate': [.1, .01, .05, .001],
                            'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                            'n_estimators': [8, 16, 32, 64, 128, 256]
                        },
                        "LinearRegression": {},
                        "XGBRegressor": {
                            'learning_rate': [.1, .01, .05, .001],
                            'n_estimators': [8, 16, 32, 64, 128, 256]
                        },
                        "CatBoost Regressor": {
                            'depth': [6, 8, 10],
                            'learning_rate': [0.01, 0.05, 0.1],
                            'iterations': [30, 50, 100]
                        },
                        "AdaBoostRegressor": {
                            'learning_rate': [.1, .01, 0.5, .001],
                            'n_estimators': [8, 16, 32, 64, 128, 256]
                        }
                    }

            model_report:dict=evaluate_model(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                param=params
            )

            #To get the best model score
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise customException("No model is able to explain more than 60% of the variance")
            logging.info(f"Best model found on both training and testing dataset: {best_model_name}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2Score=r2_score(y_test,predicted)

            return r2Score

        except Exception as e:
            raise customException(e, sys)
        