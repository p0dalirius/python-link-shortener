.PHONY: build img

IMGNAME := python_link_shortner
PORT := 5000

all : build

build:
	docker build -t $(IMGNAME):latest -f Dockerfile .

start: build
	docker run --rm -it -p $(PORT):5000 $(IMGNAME)

background:
	docker run --rm -d -p $(PORT):5000 $(IMGNAME)

shell:
	docker exec -it $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}') bash

stop:
	docker stop $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}')
