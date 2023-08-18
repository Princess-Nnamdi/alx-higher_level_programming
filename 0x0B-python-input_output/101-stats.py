#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
import sys


def print_metrics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status, count in sorted(status_counts.items()):
        print("{}: {}".format(status, count))


def process_log_line(line, total_size, status_counts):
    parts = line.strip().split(" ")
    if len(parts) >= 7:
        status = parts[-2]
        size = int(parts[-1])
        total_size += size
        if status in status_counts:
            status_counts[status] += 1
        return total_size, status_counts
    return total_size, status_counts


def main():
    total_size = 0
    status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size, status_counts = process_log_line(line, total_size, status_counts)
            if i % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)


if __name__ == "__main__":
    main()
