all: ../gen/article.css index.html

../gen/article.css: ../article.styl
	stylus < ../article.styl > ../gen/article.css.tmp
	mv ../gen/article.css.tmp ../gen/article.css

index.html: index.rst
	ruby -rrbst -e 'puts RbST.convert("index.rst")' > index.html.tmp
	mv index.html.tmp index.html
