
install-deps:
	@ poetry install

dev:
	@docker compose -f local.yml up --build -d --remove-orphans
	@./scripts/server.sh

.PHONY: install-deps dev