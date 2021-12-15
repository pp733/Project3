import logging
#from datetime import datetime, timezone

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')
fileHandler = logging.FileHandler('testlog.log')
fileHandler.setFormatter(format)
logger.addHandler(fileHandler)
logging.info("Process Started")
#pylint: disable=logging-fstring-interpolation
#pylint: disable=unspecified-encoding
#pylint: disable=f-string-without-interpolation

#def log_data_to_logfile(time,record_num,filename, col1, operation, col2, result):
def logging_data(filename, operation, counter):
    counter = counter+1

    #unixtime = int(time.time())
    #time1 = datetime.fromtimestamp(unixtime, tz=timezone.utc)
    with open('testlog.log','a') as appendFile:
        appendFile.write(f'Filename: {filename} -Record Number: {counter} -TestRan: {operation}\n ')
        #append.write(f'Time:{time1} - RecordNum:{record_num} - FileName:{filename} - Values:{col1}{operation}{col2} = Results:{result}\n')


    return appendFile
logger.info(f"Test Saved successfully")