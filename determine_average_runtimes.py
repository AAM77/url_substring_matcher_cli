import datetime

from substring_matcher.constants import (
    NUMBER_OF_DESIRED_RUNS,
    SHORTEST_URL,
    THREE_HUNDRED_CHARS_URL,
    TWO_THOUSAND_CHARS_URL,
    ELEVEN_THOUSAND_CHARS_URL
)
from substring_matcher.trie_builder import TrieBuilder


def determine_average_runtime_for_matching_keywords(url: str) -> int:
    """
    Determines the average time it takes (in milliseconds)
    to iterate through a url and retrieve the matching
    keywords using the find_matching_substrings method.
    """
    trie_builder = TrieBuilder()
    trie_builder.file_name = 'runtime_test_keywords.txt'
    # build the trie
    new_trie = trie_builder.build_trie_from_file()[0]
    # print(new_trie.find_matching_substrings(url))

    # run the method a specified number of times.
    # collect the runtime from each method call.
    # calculate and return the average runtime.
    runtimes = []

    for _ in range(NUMBER_OF_DESIRED_RUNS):
        start_time = datetime.datetime.now()
        new_trie.find_matching_substrings(url)
        end_time = datetime.datetime.now()

        runtime = (end_time - start_time).total_seconds() * 1000
        runtimes.append(runtime)

    average_runtime = sum(runtimes)/(len(runtimes))

    return average_runtime


def print_average_runtimes():
    average_runtime_short = determine_average_runtime_for_matching_keywords(
        SHORTEST_URL)

    average_runtime_medium = determine_average_runtime_for_matching_keywords(
        THREE_HUNDRED_CHARS_URL)

    average_runtime_long = determine_average_runtime_for_matching_keywords(
        TWO_THOUSAND_CHARS_URL)

    average_runtime_super_long = determine_average_runtime_for_matching_keywords(
        ELEVEN_THOUSAND_CHARS_URL)

    print(
        f"The Average Runtime for a short url is: {average_runtime_short} ms")
    print(
        f"The Average Runtime for a medium url is: {average_runtime_medium} ms")
    print(f"The Average Runtime for a long url is: {average_runtime_long} ms")
    print(
        f"The Average Runtime for a super long url is: {average_runtime_super_long} ms")


print_average_runtimes()
print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")

# print_average_runtimes()
# print("\n-------------------------------------\n")
