#!/usr/bin/env python3

import csv
import sys
import pipeclient
import ptp


class ReadWriteSequenceHandler:
    def __init__(self, client: pipeclient.PipeClient):
        self.__pipe_client = client

    def run(self, cmd: str):
        self.__pipe_client.write(cmd)
        self.__pipe_client.read()


if __name__ == '__main__':
    client = pipeclient.PipeClient('utf-8')
    handler = ReadWriteSequenceHandler(client)
    handler.run('SelectAll:')
    with open('tracklist.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                handler.run('Select: Start={} End={}'.format(
                    ptp.colon_to_sec(row[2]), ptp.colon_to_sec(row[3])))
                handler.run('AddLabel: ')
                handler.run('SetLabel: Label={} Text="{}"'.format(
                    int(row[0]) - 1, row[1]))
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(f, reader.line_num, e))
