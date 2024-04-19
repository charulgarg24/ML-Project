import logging ##  it is probably for he any execution that happend you hsould be abel t0 log all the error, and information. and tack error that will come logg into the text fel
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ## it will create log file sot his siname of file
logs_path = os.path.join(os.getcwd(), "logs","LOG_FILE") # the logs that will create will be accordignt o current working directory 
os.makedirs(logs_path, exist_ok=True)  # even if there is folder keep on appending or sending the files,cretae the file

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig( 
    filename=LOG_FILE_PATH, # create this file path
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s -  %(message)s", # this is the formate of msg this is how my entire ms will prining
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")


