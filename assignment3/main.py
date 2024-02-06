import timeit

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def benchmark_algorythm(algorythm, haystack, needle1, needle2):

    time_success = timeit.timeit(lambda: algorythm(haystack, needle1), number=10)
    time_fail = timeit.timeit(lambda: algorythm(haystack, needle2), number=10)

    return (time_success, time_fail)


def benchmark_searches(haystack, needle1, needle2):

    print(f"{'| Algorithm': <20} | {'Time (s) successful': <20} | {'Time (s) failed': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")

    (time_success, time_fail) = benchmark_algorythm(boyer_moore_search, haystack, needle1, needle2)
    print(f"{'| Boyer-Moore': <20} | {time_success:<20.5f} | {time_fail:<20.5f}")

    (time_success, time_fail) = benchmark_algorythm(rabin_karp_search, haystack, needle1, needle2)
    print(f"{'| Rabin-Karp': <20} | {time_success:<20.5f} | {time_fail:<20.5f}")

    (time_success, time_fail) = benchmark_algorythm(kmp_search, haystack, needle1, needle2)
    print(f"{'| KMP Search': <20} | {time_success:<20.5f} | {time_fail:<20.5f}")


if __name__ == '__main__':
    with open('text1.txt', 'r', encoding='Windows-1251') as f:
        text1 = f.read()

    with open('text2.txt', 'r', encoding='Windows-1251') as f:
        text2 = f.read()

    needle1 = "element"
    needle2 = "виглядііііііі"

    print("\nText 1\n")
    benchmark_searches(text1, needle1, needle2)
    print("\n\nText 2\n")
    benchmark_searches(text2, needle1, needle2)
