# server.py
import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print("Client connected")

    def on_disconnect(self, conn):
        print("Client disconnected")

    def exposed_add(self, x, y):
        print(f"Adding {x} and {y}")
        return x + y

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(MyService, port=18861)
    server.start()
