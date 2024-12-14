import logging
import os
from datetime import datetime

#Logger in python documentation

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log" # get the current date
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) # get the logs path
os.makedirs(logs_path,exist_ok=True) # create the logs directory if it does not exist if exist overwrites it

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) # get the log file path

logging.basicConfig(filename=LOG_FILE_PATH, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO) # configure the logging module 

