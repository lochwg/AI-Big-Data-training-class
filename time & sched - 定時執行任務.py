import time
import sched
schedule = sched.scheduler(time.time, time.sleep)
def func(string1):
  print("列印順序 %s" %string1)
print ("start")
schedule.enter(2,0,func,(100,))
schedule.enter(2,0,func,(2,))
schedule.enter(3,0,func,(3,))
schedule.enter(4,0,func,(4,))
schedule.run()
print("end")