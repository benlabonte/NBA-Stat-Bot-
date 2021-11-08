from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=3)
def scheduled_job():
    print("running get-player-data")
    os.system("python3 get-player-data.py")
    print("finished running get-player-data")

sched.start()