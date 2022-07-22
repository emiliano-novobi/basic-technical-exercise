export PGPASSWORD:=odoo
ODOO_CONTAINER=basic-technical-exercise-odoo-1
DB_CONTAINER=basic-technical-exercise-postgres-1
ODOO_BIN=/opt/odoo/odoo/odoo-bin -c /opt/odoo/odoo.conf
CUSTOM_ADDONS_DIRECTORY=/opt/odoo/customized_addons

up:
	docker-compose up -d

down:
	docker-compose down

addon_scaffold:
	docker exec -it $(ODOO_CONTAINER) $(ODOO_BIN) scaffold $(ADDON_NAME) $(CUSTOM_ADDONS_DIRECTORY)

rebuild:
	docker-compose down
	docker-compose up -d --build

test_module:
	docker exec -t $(ODOO_CONTAINER) $(ODOO_BIN) -d db_test -p 8001 --stop-after-init -i $(module) --test-tags /$(module)

generate_local_coverage_report:
	docker exec -it $(ODOO_CONTAINER) pytest -s --odoo-database=db_test --html=/coverage/local/report.html $(CUSTOM_ADDONS_DIRECTORY)/
	docker cp $(ODOO_CONTAINER):/coverage/local coverage

generate_coverage_report:
	docker exec -it $(ODOO_CONTAINER) coverage run $(ODOO_BIN) -d db_test --test-enable -p 8001 --stop-after-init --log-level=test
	docker exec -it $(ODOO_CONTAINER) coverage html -d /coverage/all
	docker cp $(ODOO_CONTAINER):/coverage/all coverage

init_test_db:
	docker stop $(ODOO_CONTAINER)
	docker exec -t $(DB_CONTAINER) psql -U odoo -d postgres -c "DROP DATABASE IF EXISTS db_test"
	docker exec -t $(DB_CONTAINER) psql -U odoo -d postgres -c "CREATE DATABASE db_test"
	docker start $(ODOO_CONTAINER)
	docker exec -t $(ODOO_CONTAINER) $(ODOO_BIN) -i all -d db_test --stop-after-init
