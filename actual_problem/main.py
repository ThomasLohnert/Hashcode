import file_io
from Hashcode import RideScheduler

f = file_io.read_input("a_example.in")
scheduler = RideScheduler(*f)

vehicles = scheduler.assign_jobs()
print vehicles