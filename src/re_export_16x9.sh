#!/bin/bash

find ./ -name "*.py" | while read -r FILE; do
    manim -qh "$FILE" --save_sections -r 1920,1080
done
