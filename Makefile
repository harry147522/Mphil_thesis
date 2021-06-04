all: main.pdf

main.pdf: main.tex
	latexmk -pdf $(patsubst %.pdf,%.tex,$@)

clean:
	latexmk -C main.tex
	rm -f main.bib main.bbl *.nav *.snm main.run.xml
