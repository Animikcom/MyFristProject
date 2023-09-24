import time
import os
faka = 0
strime = time.time()
while True:
    # time.sleep(0.1)
    faka +=  1
    # print(strime)
    print(faka)
    if faka == 100:
        print('fakacha')
        hi = os.system('start chrome')
        # print(hi)
        break