# client.py
import rpyc

if __name__ == "__main__":
    conn = rpyc.connect("localhost", 18861)
    try:
        result = conn.root.exposed_add(4, 5)
        print(f"Result: {result}")
    finally:
        conn.close()
