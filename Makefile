env:
	./scripts/encrypt-env.sh

docker-prune:
	docker system prune -a
	docker system prune -a --volumes

.PHONY: env docker-prune
