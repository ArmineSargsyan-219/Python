import re
import time
from collections import Counter
from threading import Thread, Lock
from multiprocessing import Pool


def read_file_in_chunks(filename, num_chunks):
    with open(filename, "r") as file:
        lines = file.readlines()
    chunk_size = len(lines) // num_chunks
    return [lines[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


def count_words(lines):
    word_count = Counter()
    for line in lines:
        word_count.update(tokenize(line))
    return word_count


def count_words_sequential(filename):
    with open(filename, "r") as file:
        return count_words(file.readlines())


def count_words_multithreading(filename, num_threads=4):
    def worker(chunk, shared_counter, lock):
        local_count = count_words(chunk)
        with lock:
            shared_counter.update(local_count)

    chunks = read_file_in_chunks(filename, num_threads)
    shared_counter = Counter()
    lock = Lock()
    threads = [Thread(target=worker, args=(chunk, shared_counter, lock)) for chunk in chunks]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return shared_counter


def count_words_multiprocessing(filename, num_processes=4):
    chunks = read_file_in_chunks(filename, num_processes)

    with Pool(num_processes) as pool:
        results = pool.map(count_words, chunks)

    combined_count = Counter()
    for result in results:
        combined_count.update(result)

    return combined_count


def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    elapsed_time = time.time() - start_time
    return result, elapsed_time


def main():
    filename = "input_text.txt"

    print("\nMeasuring performance...")

    _, seq_time = measure_execution_time(count_words_sequential, filename)
    print(f"Sequential Execution Time: {seq_time:.2f} seconds")

    _, mt_time = measure_execution_time(count_words_multithreading, filename)
    print(f"Multithreading Execution Time: {mt_time:.2f} seconds")

    _, mp_time = measure_execution_time(count_words_multiprocessing, filename)
    print(f"Multiprocessing Execution Time: {mp_time:.2f} seconds")

    print("\nSpeedups:")
    print(f"Multithreading Speedup: {seq_time / mt_time:.2f}x")
    print(f"Multiprocessing Speedup: {seq_time / mp_time:.2f}x")


if __name__ == "__main__":
    main()
