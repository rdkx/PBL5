import datetime 
import time

elapsedTime = datetime.datetime.now() - datetime.datetime.now()

record = open("Output.txt", "w")

for i in range(1, 100):
    start = datetime.datetime.now()
    time.sleep(0.01)
    end = datetime.datetime.now()
    elapsedTime = elapsedTime + (end - start)
    print(elapsedTime)
    record.write("Elapsed Time: %s \n" % elapsedTime)

record.close()