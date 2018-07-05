#!/usr/bin/bash

WORD=test

echo "Train from recorded samples"
for time in {1..5}
do
  ./sopare.py -r "samples/sample-$time.raw" -t $WORD
done


