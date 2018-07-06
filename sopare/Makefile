
all: learn train save run

run:
	./sopare.py -l

learn: clean-samples
	./learn.sh

# ./train.sh
train: clean
	./sopare.py -v -t ein && \
	./sopare.py -v -t ein && \
	./sopare.py -v -t ein && \
	./sopare.py -v -t aus && \
	./sopare.py -v -t aus && \
	./sopare.py -v -t aus

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
