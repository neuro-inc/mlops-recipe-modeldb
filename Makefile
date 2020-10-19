.PHONY: all
all:
	$(MAKE) init
	$(MAKE) modeldb-up
	$(MAKE) modeldb-example
	$(MAKE) modeldb-down


.PHONY: init
init:
	pip install -U neuro-flow neuro-extras neuromation
	neuro login
	neuro config switch-cluster neuro-public


.PHONY: sync-up
sync-up:
	neuro cp -ru .  -T storage:my-project

.PHONY: modeldb-up
modeldb-up: sync-up
	neuro-flow run modeldb_backend
	neuro-flow run modeldb_proxy
	neuro-flow run modeldb_postgres
	neuro-flow run modeldb_graphql
	neuro-flow run modeldb_frontend

.PHONY: modeldb-example
modeldb-example:
	neuro-flow run modeldb_example
	neuro job browse my-project-modeldb-frontend

.PHONY: modeldb-down
modeldb-down:
	neuro-flow kill modeldb_backend
	neuro-flow kill modeldb_proxy
	neuro-flow kill modeldb_postgres
	neuro-flow kill modeldb_graphql
	neuro-flow kill modeldb_frontend
