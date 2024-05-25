import time

def stopwatch():
    print("Press Enter to start the stopwatch and Ctrl+C to stop it.")

    while True:
        try:
            
            input()  # Wait for the user to press Enter
            start_time = time.time()
            print("Stopwatch started... Press Ctrl+C to stop.")
            
            while True:
                elapsed_time = time.time() - start_time
                print(f"Elapsed time: {elapsed_time:.2f} seconds", end="\r")
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"\nStopwatch stopped. Total time: {elapsed_time:.2f} seconds")
            break

if __name__ == "__main__":
    stopwatch()
