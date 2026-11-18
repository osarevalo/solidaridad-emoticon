# SPDX-License-Identifier: MIT
PYTHON ?= .venv/bin/python
VERSION := 1.3.0
ZIP := ../solidaridad-emoticon_v$(VERSION).zip

.PHONY: setup assets sticker verify preview all zip clean

setup:
	python3 -m venv .venv
	.venv/bin/pip install -q -r scripts/requirements.txt

assets:
	$(PYTHON) scripts/build_assets.py

sticker:
	$(PYTHON) scripts/build_sticker.py

verify:
	$(PYTHON) scripts/verify_geometry.py

preview:
	$(PYTHON) scripts/make_preview.py

all: assets sticker verify preview

zip:
	cd .. && rm -f "solidaridad-emoticon_v$(VERSION).zip" && zip -qr "solidaridad-emoticon_v$(VERSION).zip" solidaridad-emoticon -x 'solidaridad-emoticon/.git/*' 'solidaridad-emoticon/.venv/*' 'solidaridad-emoticon/**/__pycache__/*' 'solidaridad-emoticon/**/*.pyc'
	@echo "OK: $(ZIP)"

clean:
	rm -rf dist/png dist/sticker preview/contact-sheet.png preview/preview.html docs/verificacion-geometrica.md
