server:
	cd test && python -m http.server & sleep 5 & open http://localhost:8000/pagina1.html

test0:
	rm -fr data
	python spider.py http://localhost:8000/pagina1.html     

test1:
	rm -fr data
	python spider.py -r  http://localhost:8000/pagina1.html   

test2:
	rm -fr data
	python spider.py -r -l http://localhost:8000/pagina1.html   

test3:
	rm -fr data
	python spider.py -r -l 3 http://localhost:8000/pagina1.html   

test4:
	rm -fr data
	python spider.py -r -l 7 http://localhost:8000/pagina1.html   

test5:
	rm -fr data
	python spider.py -r -l 12 http://localhost:8000/pagina1.html   

test6:
	rm -fr data
	python spider.py -p http://localhost:8000/pagina1.html   

test7:
	rm -fr data2
	python spider.py -p data2 http://localhost:8000/pagina1.html   

test8:
	rm -fr data3
	python spider.py -r -l 4 -p data3 http://localhost:8000/pagina1.html   

test9:
	rm -fr externo
	python spider.py -r -l 2 -p externo https://github.com/ianare/exif-samples
