#!/usr/bin/env python3

import csv
import sys
import pipeclient
import ptp


if __name__ == '__main__':
    client = pipeclient.PipeClient()
    client.write("SelectAll:")
    with open('tracklist_youtube.csv', 'r') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                client.write('Select: Start={} End={}'.format(
                    ptp.colon_to_sec(row[2]), ptp.colon_to_sec(row[3])))
                client.write('AddLabel: ')
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(f, reader.line_num, e))
