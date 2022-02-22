#!/bin/bash

wget https://github.com/EdgedesignCZ/phpqa/archive/v1.19.0.zip -O phpqa-1.19.zip && unzip phpqa-1.19.zip;
rm phpqa-1.19.zip; 
cd phpqa-1.19.0 && composer install --no-dev
echo 'export PATH="$PATH:$HOME/phpqa-1.19.0/"' >> ~/.bashrc
