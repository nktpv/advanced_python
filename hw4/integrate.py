import math
import logging
import time
import concurrent.futures

logging.basicConfig(filename='integration_logs.log', level=logging.INFO)

def integrate(func, start, end, *, n_iter=10000):
    logging.info(f"Start integration from {start} to {end}")
    step = (end - start) / n_iter
    area = sum(func(start + i * step) * step for i in range(n_iter))
    logging.info(f"Integration finished with area {area}")
    return area

def run_integration(executor, func, a, b, n_jobs):
    with executor(max_workers=n_jobs) as pool:
        futures = []
        for i in range(n_jobs):
            logging.info(f"Submitting task {i+1} to executor")
            futures.append(pool.submit(integrate, func, a, b))
        
        results = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
    return results

if __name__ == "__main__":
    cpu_num = 4  

    func = math.cos
    a = 0
    b = math.pi / 2

    with open("artifacts/4_2/results.txt", "w", encoding="utf-8") as file:
        file.write("n_jobs;ThreadPoolExecutor;ProcessPoolExecutor\n")
        for n_jobs in range(1, cpu_num * 2 + 1):
            start_time = time.time()
            results_threadpool = run_integration(concurrent.futures.ThreadPoolExecutor, func, a, b, n_jobs)
            threadpool_execution_time = time.time() - start_time
            
            start_time = time.time()
            results_processpool = run_integration(concurrent.futures.ProcessPoolExecutor, func, a, b, n_jobs)
            processpool_execution_time = time.time() - start_time
            
            file.write(f"{n_jobs};{threadpool_execution_time};{processpool_execution_time}\n")
