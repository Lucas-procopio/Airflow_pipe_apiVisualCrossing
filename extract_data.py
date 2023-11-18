import os
import subprocess
import pandas as pd
from datetime import datetime, timedelta

def createDate():
    # Setting initial time and last time
    dtStart = datetime.today()
    dtEnd = dtStart + timedelta(days=14)
    dtStart, dtEnd = dtStart.strftime('%Y-%m-%d'), dtEnd.strftime('%Y-%m-%d')
    return dtStart, dtEnd

def run_sh():
    subprocess.run('./variables.sh')

if __name__ == '__main__':
    run_sh()
