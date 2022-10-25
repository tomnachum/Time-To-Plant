from pickle import TRUE
from sched import scheduler

import pymysql
from typing import List
from db_manager import print_users_test
import schedule
import time
import requests

while TRUE:
    print_users_test()
    time.sleep(2)
    print("iteration")
