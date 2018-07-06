#!/usr/bin/bash

MIC_FILE=~/.virtual-mic
CONFIG_FILE=~/.config/pulse/client.conf

if [ -e $CONFIG_FILE ]
then
  echo "Pulse config file exist, cannot proceed - $CONFIG_FILE"
  exit -1
fi

if [ -e $MIC_FILE ]
then
  echo "Microphone file exist, cannot proceed - $MIC_FILE"
  exit -1
fi

# Create a file that will set the default source device to virtmic for all
# PulseAudio client applications.
echo "default-source = virtmic" > $CONFIG_FILE


# Write the audio file to the named pipe virtmic. This will block until the
# named pipe is read.
echo "Writing audio file to virtual microphone."
for filename in samples/ein*.wav
do
  echo "*** Processing sample $filename ***"
  # Load the "module-pipe-source" module to read audio data from a FIFO special
  # file.
  echo "Creating virtual microphone."
  pactl load-module module-pipe-source source_name=virtmic \
    file=$MIC_FILE format=s16le rate=48000 channels=1

  # Set the virtmic as the default source device.
  echo "Set the virtual microphone as the default device."
  pactl set-default-source virtmic

  ./sopare.py -v -t ein &
  sleep 3 && cat $filename > $MIC_FILE

  pactl unload-module module-pipe-source
done

# record ... arecord test.raw -t raw -f S16_LE -c 1 -r 16000

echo "Cleanup"
rm -f $CONFIG_FILE $MIC_FILE

echo "Done"
