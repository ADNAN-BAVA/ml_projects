import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    DataIngestionConfig is a dataclass that holds the configuration for the data ingestion process
    """
    train_path: str = os.path.join('artifacts','train.csv') # path to the train data
    test_path: str = os.path.join('artifacts','test.csv') # path to the test data
    raw_path: str = os.path.join('artifacts','data.csv') # path to the raw data

class DataIngestion:
    """
    DataIngestion is a class that is responsible for ingesting the data
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # get the configuration
        
    def initiate_data_ingestion(self):
        """
        This is a method that reads the data from the path
        """
        logging.info("Reading the data from the raw path")
        try:
            df = pd.read_csv('notebook\data\students.csv') # read the data from the raw path (This location can be from any source)
            logging.info("Data read successfully")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok=True) # create the directory if it does not exist

            df.to_csv(self.ingestion_config.raw_path,index=False,header=True) # save the data to the raw path
            
            logging.info("Train test split initiated successfully")
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42) # split the data into train and test data
            
            train_set.to_csv(self.ingestion_config.train_path,index=False,header=True) # save the train data
            test_set.to_csv(self.ingestion_config.test_path,index=False,header=True) # save the test data
            
            logging.info("Data ingestion is successfully")
            
            return (self.ingestion_config.train_path,self.ingestion_config.test_path) # return the train and test data path
            
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()