
all: learn train save run

run:
	./sopare.py -l

learn: clean-samples
	./learn.sh

train: clean
	./train.sh

save:
	./sopare.py -c

clean-samples:
	rm -f samples/*

clean:
	rm -f dict/*.raw && ./sopare.py -d "*"

setup:
	sudo apt-get update && \
		sudo apt-get install build-essential python-pyaudio python-numpy \
		python-scipy python-matplotlib

.PHONY: all run learn train save setup clean-samples clean
