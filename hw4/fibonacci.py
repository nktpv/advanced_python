import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_fibonacci(n):
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def run_with_threads(n):
    start_time = time.time()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def run_with_processes(n):
    start_time = time.time()
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

if __name__ == "__main__":
    n = 27

    sync_execution_time = run_fibonacci(n)
    print("Синхронный запуск:", sync_execution_time)

    thread_execution_time = run_with_threads(n)
    print("Потоки:", thread_execution_time)

    process_execution_time = run_with_processes(n)
    print("Процессы:", process_execution_time)

    with open("artifacts/4_1/results.txt", "w", encoding="utf-8") as file:
        file.write("Синхронный запуск: {}\n".format(sync_execution_time))
        file.write("Потоки: {}\n".format(thread_execution_time))
        file.write("Процессы: {}\n".format(process_execution_time))
