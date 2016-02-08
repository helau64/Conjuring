import multiprocessing

import conjuringtext
import conjuringlights

processes = []

for func in [conjuringtext.function, conjuringlights.function]:
    processes.append(multiprocessing.Process(target=func, args=(arg1, arg2)))
    processes[-1].start()

while True:
    time.sleep(600) # sleep for 10 minutes
    living_processes = [p.is_alive() for p in processes]
    if living_processes < 2:
        for p in living_processes:
            p.terminate()

        print("Something went wrong")