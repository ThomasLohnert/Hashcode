import file_io
from Hashcode import RideScheduler

for dataset in ["a.in", "b.in", "c.in", "d.in", "e.in"]:
    f = file_io.read_input(dataset)
    scheduler = RideScheduler(*f)

    vehicles = scheduler.assign_jobs()
    file_io.write_output(dataset + ".txt", vehicles)
