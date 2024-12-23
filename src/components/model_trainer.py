import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    RandomForestRegressor,
    AdaBoostRegressor,
    GradientBoostingRegressor
)
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', "model.pkl") # Path to save the model

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_arr,test_arr):
        '''
        This function is responsible for initiating the model training process
        '''
        try:
            logging.info('Splitting the data into features and target for test and train')
            X_train, y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            
            models = {
                "RandomForestRegressor": RandomForestRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "CatBoostRegressor": CatBoostRegressor(verbose=False),
                "LinearRegression": LinearRegression(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "XGBRegressor": XGBRegressor()
            }
            
            models_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                                 models=models)
            
            best_model_score = max(sorted(models_report.values()))  # Get the best model score
            best_model_name = list(models_report.keys())[
                list(models_report.values()).index(best_model_score)]   # Get the best model name
            
            best_model = models[best_model_name]  # Get the best model
            
            if best_model_score < 0.6:
                raise CustomException("The best model score is less than 0.6 good model not found", sys)
            logging.info(f"Best model found: {best_model_name}")
            
            save_object(self.model_trainer_config.trained_model_file_path,best_model)
            
            predicted_values = best_model.predict(X_test)
            r2_score_value = r2_score(y_test,predicted_values)
            
            return r2_score_value
            
        except Exception as e:
            raise CustomException(e,sys)
            