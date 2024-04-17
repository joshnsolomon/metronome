#!/bin/bash

pyinstaller --add-data='../images/*:./images/' \
            --add-data='../fonts/*:./fonts/' \
            --add-data='../sounds/*:./sounds/' \
            --windowed \
            ../main.py