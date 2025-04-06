import queue
import random
import time


# creates a FIFO queue
request_queue = queue.Queue()


def generate_request():
    request_id = random.randint(1000, 9999)
    # request to queue with current timestamp
    request_data = f"Request #{request_id} - Submitted at {time.strftime('%H:%M:%S')}"
    request_queue.put(request_data)
    print(f"Generated new request: {request_data}")


def process_request():
    if not request_queue.empty():
        # remove and get the request from queue
        current_request = request_queue.get()
        print(f"Processing: {current_request}")
        print(f"Request completed at {time.strftime('%H:%M:%S')}")

        # mark the task as done (for queue management)
        request_queue.task_done()
    else:
        print("Queue is empty - no requests to process")


def main():
    print("\n|     Service Center Simulation (Press Ctrl+C to exit)     |")
    print("|----------------------------------------------------------|")

    try:
        while True:
            # 70% chance each iteration
            if random.random() < 0.7:
                generate_request()

            process_request()

            # processing delay imitation
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nShutting down service center until 8 am tomorrow.")


if __name__ == "__main__":
    main()
