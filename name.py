
from datetime import datetime

now=datetime.now()

def tt():

    current_time = now.strftime("%H:%M:%S")

    return("Current Time =", current_time)

print(tt())