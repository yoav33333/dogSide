import threading
import time

from jsonGen import jsonGen
from server import Server
from testClass import Dog

if __name__ == "__main__":
    # j = jsonGen()
    print()

    # s = Server()
    # s.run()
    threading.Thread(target=lambda: Server().run(), daemon=True).start()
    while True:
        # print(Dog().age)
        # print(Dog().name)
        # print(jsonGen().mapGen())
        # if time.time() % 1 == 0:
        Dog().age += 0.01