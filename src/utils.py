import os
import sys
import pickle

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from src.logger import logging
from src.exception import CustomException

def save_object(file_path,obj):
    """
    This is a function that saves the object to the file path
    """
    try:
        logging.info("Saving the object to the file path")
        dir_path = os.path.dirname(file_path) # get the directory path
        
        os.makedirs(dir_path,exist_ok=True) # create the directory if it does not exist
        
        with open(file_path,'wb') as file_obj:
            
            pickle.dump(obj,file_obj) # save the object to the file path
        
        logging.info("Object saved successfully")
        
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range (len(list(models))):
            model_name = list(models)[i]
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            mse_train = mean_squared_error(y_train, y_pred_train)
            mae_train = mean_absolute_error(y_train, y_pred_train)
            r2_train = r2_score(y_train, y_pred_train)
            mse_test = mean_squared_error(y_test, y_pred_test)
            mae_test = mean_absolute_error(y_test, y_pred_test)
            r2_test = r2_score(y_test, y_pred_test)
            #report[model_name] = {"mse_train": mse_train, "mae_train": mae_train, "r2_train": r2_train}
            #report[model_name] = {"mse_test": mse_test, "mae_test": mae_test, "r2_test": r2_test}
            report[list(models.keys())[i]] = r2_test
        return report
    except:
        pass