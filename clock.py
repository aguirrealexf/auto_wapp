# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:36:58 2020

@author: Alex
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from auto_wapp import send_msj

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msj, 'interval', seconds=15)

sched.start()