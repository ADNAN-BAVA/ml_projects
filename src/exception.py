import sys
import logging

#custom exception handling in python documenation

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # get the traceback object
    filename = exc_tb.tb_frame.f_code.co_filename # get the filename from the traceback object
    error_message = "Error occured in python file: {}, at line number: {}, error message: {}".format(
        filename,exc_tb.tb_lineno,str(error)) # create the error message
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message:str,error_detail:sys):
        super().__init__(error_message) # call the parent class constructor
        self.error_message = error_message_detail(error_message,error_detail=error_detail) # get the error message
    
    def __str__(self):
        return self.error_message