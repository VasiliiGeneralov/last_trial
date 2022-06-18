#!/usr/bin/env python3

import eyed3
from pathlib import Path
import csv
import sys
import os

if __name__ == '__main__':

    num_title = dict()
    with open('tracklist_youtube.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                num_title.update({int(row[0]): row[1]})
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(f, reader.line_num, e))

    AlbumName = 'Последнее Испытание'
    AlbumYear = '2016'

    mp3_files = list(Path(os.getcwd()).glob('*.mp3'))

    for mp3_file in mp3_files:
        track_number = int(mp3_file.name.split('-')[0])
        audiofile = eyed3.load('{}'.format(mp3_file.name))
        audiofile.tag.album = AlbumName
        audiofile.tag.track_num = track_number
        audiofile.tag.year = AlbumYear
        audiofile.tag.save()
