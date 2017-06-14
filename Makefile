NAME = docker.dev.s-cloud.net/$(shell manifest name)
VERSION_LABEL := $(shell artifact-manager package-version)

.PHONY: clean
clean:
	echo "nothing to do"

.PHONY: build
build:
	docker build --tag=$(NAME) .
	docker tag $(NAME) $(NAME):$(VERSION_LABEL)

.PHONY: test
test: build
	docker run -it -p 5001:5001 $(NAME):$(VERSION_LABEL) bash
	docker tag $(NAME) $(NAME):latest

.PHONY: publish
publish:
	docker push $(NAME):$(VERSION_LABEL)
	docker push $(NAME):latest