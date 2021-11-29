import os
import time

log_dir = os.path.dirname(os.getcwd()) + '/logs'
print(log_dir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
else:
    pass
now_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
print(now_time)
log_file = log_dir + now_time + '.log'
print(log_file)
