.PHONY: clean build docker

dist/inkbird-*.tar.gz: build

build:
	@poetry build

docker: dist/inkbird-*.tar.gz
	@docker build . -t hichtakk/inkbird-exporter:0.1.0

clean:
	@rm -rf ./dist