#!/usr/bin/env python3

import csv
import sys


def read_tracklist_csv(filename: str):
    result = list()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                result += [row]
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(f, reader.line_num, e))
    return result


if __name__ == '__main__':
    print(read_tracklist_csv('tracklist_yandex.csv'))
    print(read_tracklist_csv('tracklist_youtube.csv'))
