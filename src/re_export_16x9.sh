#!/bin/bash

# Esporta tutto con risoluzione 1920x1200 (rapporto 16:10)

for FILE in `find ./ -name *.py`; do
    manim -r 1920,1080 -qh --save-sections $FILE &
    wait $!
done