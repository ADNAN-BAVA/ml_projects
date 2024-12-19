import os
import sys
import pickle

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