#!/bin/bash

pyinstaller --name 'Metronome' \
            --icon '../images/icon.png' \
            --windowed \
            --add-data='../images/*:./images/' \
            --add-data='../fonts/*:./fonts/' \
            --add-data='../sounds/*:./sounds/' \
            --windowed \
            ../main.py
