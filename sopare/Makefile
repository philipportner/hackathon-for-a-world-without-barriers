NAME=hugo

run:
	./sopare.py -l

learn:
	./sopare.py -v -t $(NAME)

save:
	./sopare.py -c

setup:
	sudo apt-get update && \
		sudo apt-get install build-essential python-pyaudio python-numpy \
		python-scipy python-matplotlib

clean:
	rm -f dict/*.raw && ./sopare.py -d "*"
