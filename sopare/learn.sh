#!/usr/bin/bash

WORD=test

echo "Record 5 samples"
for time in {1..5}
do
  ./sopare.py -v -w "samples/sample-$time.raw" -t $WORD
done

