from jsonGen import jsonGen
from server import Server
from testClass import Dog

if __name__ == "__main__":
    # j = jsonGen()
    print(jsonGen().getJson())

    s = Server()
    s.run()