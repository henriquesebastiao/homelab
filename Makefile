update:
	./scripts/save-config.sh

docker-prune:
	docker system prune -a
	docker system prune -a --volumes

.PHONY: update docker-prune
