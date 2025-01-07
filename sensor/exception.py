import sys
import os


def error_message_detail(error,error_detail:sys):
    # to get the filename where the error wil occur
    _,_,exc_tb=error_detail.exc_info() #exc_info return tuple in set of 3
    filename = exc_tb.tb_frame.f_code.co_filename
    # To capture line number
    error_message = "error occured in file [{0}] and line number is [{1}] and error is [{2}]".format(filename,exc_tb.tb_lineno,str(error))

    return error_message

class SensorException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message =error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message