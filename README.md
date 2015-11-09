# pilnujemy.github.io

Kod źródłowy strony internetowej Fundacji Pilnujemy.info. 

Do budowy strony wykorzystano generator stron statycznych [Pelican](http://getpelican.com/).

## Instalacja ##

Do zbudowania strony należy:

```sh
git submodule init
git submodule update --recursive
pip install -r requirements.txt
make html
```
## Uruchamianie ##

W celach rozwoju strony warto wykonać ```./develop_server.sh start``` które uruchamia serwer deweloperski Pelican na porcie 8000 i umożliwia bieżący podgląd zmienianych treści.
