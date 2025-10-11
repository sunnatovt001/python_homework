#Homework\
#Lesson-12


# Exercise 1: Threaded Prime Number Checker

#Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_range(start, end, primes):
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)

def main():
    start = 1
    end = 100
    num_threads = 4
    thread_list = []
    primes = []

    # Divide the range among threads
    for i in range(num_threads):
        thread_start = start + i * (end - start) // num_threads
        thread_end = start + (i + 1) * (end - start) // num_threads
        thread = threading.Thread(target=check_range, args=(thread_start, thread_end, primes))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    print("Prime numbers found:", primes)

if __name__ == "__main__":
    main()




# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

import threading
from collections import defaultdict

def process_chunk(chunk, word_count, lock):
    local_count = defaultdict(int)
    for line in chunk:
        words = line.strip().split()
        for word in words:
            local_count[word] += 1

    # Thread-safe qo‘shish
    with lock:
        for word, count in local_count.items():
            word_count[word] += count


def main():
    file_path = "large_text_file.txt"
    num_threads = 4
    word_count = defaultdict(int)
    lock = threading.Lock()

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        chunk_size = len(lines) // num_threads
        threads = []

        for i in range(num_threads):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
            thread = threading.Thread(target=process_chunk, args=(lines[start:end], word_count, lock))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    print("Word occurrences:")
    for word, count in word_count.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()





