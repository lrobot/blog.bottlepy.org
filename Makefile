.PHONY: clean

build: venv
	. venv/bin/activate; pelican -vs conf.py src/
	echo "change /etc/httpd/conf/httpd.conf's DocumentRoot to this output for blog service"

draft: venv
	. venv/bin/activate; pelican -vs conf.py -o output/draft/ src/

preview: build
	python -m webbrowser ./output/index.html

clean:
	rm -rfv output

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

