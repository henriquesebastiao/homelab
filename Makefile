update:
	./scripts/save-config.sh

docker-prune:
	docker system prune -a
	docker system prune -a --volumes

nextcloud-sync:
	sudo chmod -R 777 /mnt/hd_externo/nextcloud/
	docker exec nextcloud-aio-nextcloud sudo -E -u www-data php occ files:scan --all

.PHONY: update docker-prune nextcloud-sync
