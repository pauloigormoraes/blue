# session = MarketSession()
# session.login("pauloigormoraes@gmail.com", "amorepaz94")


import time, sys

for i in range(0, 10):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(1)

print ("\nFim")
