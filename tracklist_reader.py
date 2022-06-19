#!/usr/bin/env python3

import csv
import sys
import pipeclient
import ptp


if __name__ == '__main__':
    client = pipeclient.PipeClient()
    client.write("SelectAll:")
    with open('tracklist.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                client.write('Select: Start={} End={}'.format(
                    ptp.colon_to_sec(row[2]), ptp.colon_to_sec(row[3])))
                client.read()
                client.write('AddLabel: ')
                client.read()
                client.write('SetLabel: Label={} Text="{}"'.format(
                    int(row[0]) - 1, row[1]))
                client.read()
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(f, reader.line_num, e))
