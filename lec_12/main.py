import random
import time
from concurrent.futures import ThreadPoolExecutor

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def create_file(filename, num_lines, numbers_per_line, random_range):
    try:
        with open(filename, "w") as file:
            for _ in range(num_lines):
                numbers = [str(random.randint(*random_range)) for _ in range(numbers_per_line)]
                file.write(" ".join(numbers) + "\n")
        print(f"File '{filename}' created with {num_lines} lines of random numbers.")
    except Exception as e:
        print(f"Error while creating the file: {e}")

def process_line(line, threshold):
    try:
        numbers = list(map(int, line.split()))
        filtered_numbers = list(filter(lambda x: x > threshold, numbers))
        return " ".join(map(str, filtered_numbers))
    except Exception as e:
        print(f"Error while processing line: {e}")
        return ""

@measure_time
def process_file(filename, threshold):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with ThreadPoolExecutor() as executor:
            processed_lines = list(executor.map(lambda line: process_line(line, threshold), lines))

        with open(filename, "w") as file:
            file.writelines(line + "\n" for line in processed_lines if line.strip())
        print(f"File '{filename}' processed to keep numbers > {threshold}.")
    except Exception as e:
        print(f"Error while processing the file: {e}")

@measure_time
def read_file_generator(filename, threshold=0):
    try:
        with open(filename, "r") as file:
            for line in file:
                numbers = list(map(int, line.strip().split()))
                filtered_numbers = [n for n in numbers if n > threshold]
                yield filtered_numbers
    except Exception as e:
        print(f"Error while reading the file: {e}")
        return

if __name__ == "__main__":
    print("Configure file creation:")
    num_lines = int(input("Enter the number of lines: "))
    numbers_per_line = int(input("Enter the number of numbers per line: "))
    random_range = (
        int(input("Enter the minimum random number: ")),
        int(input("Enter the maximum random number: ")),
    )

    filename = "advanced_filtered_random_numbers.txt"
    threshold = int(input("Enter the threshold for filtering numbers: "))

    create_file(filename, num_lines, numbers_per_line, random_range)

    process_file(filename, threshold)

    print("\nReading the processed file as a generator (showing first 5 lines):")
    generator = read_file_generator(filename, threshold=threshold)
    for i, line in enumerate(generator):
        print(line)
        if i >= 4: 
            break
