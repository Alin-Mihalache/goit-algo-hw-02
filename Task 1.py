import queue
import time
queue = queue.Queue()

def generate_request():
    request = f"Request {time.time()}"
    queue.put(request)
    print(f"Request {request} generated")
    
def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request {request}")
        time.sleep(1)
    else:
        print("No request to process")
        
def main():
    try:
        while True:
            generate_request()
            process_request()
    except KeyboardInterrupt:
        print("Exiting")
        
if __name__ == "__main__":
    main()