update:
	./scripts/save-config.sh

docker-prune:
	docker system prune -a
	docker system prune -a --volumes

nextcloud-sync:
	docker exec nextcloud-aio-nextcloud sudo -E -u www-data php occ files:scan --all

.PHONY: update docker-prune nextcloud-sync