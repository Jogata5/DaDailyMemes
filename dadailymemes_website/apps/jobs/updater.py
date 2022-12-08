from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import scheduleEmail, scheduleTimer

def start():
    scheduler = BackgroundScheduler
    scheduler.add_job(scheduleTimer, 'interval', seconds = 5)
    scheduler.start()