install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

init:
	poetry run flake8 brain_games

.PHONY: install brain-games build publish package-install init
 
