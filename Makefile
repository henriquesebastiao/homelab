env:
	./scripts/encrypt-env.sh

docker-prune:
	docker system prune -a
	docker system prune -a --volumes

update:
	dotdrop update -f --profile=server

install:
	dotdrop --cfg=/home/hick/homelab/config.yaml --profile=server install -f

compare:
	dotdrop compare --profile=server

.PHONY: env docker-prune update install compare
