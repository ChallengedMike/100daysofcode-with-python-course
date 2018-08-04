from datetime import datetime

def convert_to_datetime(line):
    '''Extract date and time from a line of text, return as a datetime object.'''
    
    # Find the part of the string that contains the information about time.
    date_string = line.split()[1]
    date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
    return date

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    
    datetimes_from_log = [convert_to_datetime(line) for line in loglines if line.startswith('INFO')]
    return datetimes_from_log[-1] - datetimes_from_log[0]
