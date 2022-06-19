#!/usr/bin/env python3

import eyed3
from pathlib import Path
import os

if __name__ == '__main__':

    AlbumName = u'Последнее Испытание'
    AlbumYear = u'2016'

    mp3_files = list(Path(os.getcwd()).glob('*.mp3'))

    for mp3_file in mp3_files:
        audiofile = eyed3.load('{}'.format(mp3_file.name))
        audiofile.tag.album = AlbumName
        audiofile.tag.year = AlbumYear
        audiofile.tag.save()
