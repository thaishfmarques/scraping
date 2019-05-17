
>**#Instalar o pip - instalador de pacotes python**
>
>**#Pacote do Pip para python 3**
>>   $ sudo apt-get install python3-pip
>**#pacote do pip para python 2**
>>   $ sudo apt-get install python-pip
>
>**# se instalar o pip para python3, tem que chamar o gerenciador com o pip3**
>
>**# Instala o scrapy**
>>   $ pip install scrapy
>
>**# inicia o projeto no diretorio atual**
>>   $ scrapy startproject teste_spider
>
>**# navega ate a pasta do projeto**
>>   $ cd ./teste_spider/
>
>**# cria a spider**
>>   $ scrapy genspider SejaLivre sejalivre.org
>
>**# executa a spider**
>>   $ scrapy runspider SejaLivre.py
>
>**# abre o shell do scrapy para o site**
>>   $ scrapy shell http://sejalivre.org/
>
>**# exporta o crawler para um arquivo**
>>   $ scrapy crawl SejaLivre -o teste.csv
