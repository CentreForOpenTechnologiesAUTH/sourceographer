# Sourceographer project

## Requirements

Install all the requirements before proceeding to next steps:

* Python >= 3.5
* python3-pandas >= 0.22
* python3-numpy >= 1.13.3
* python3-matplotlib >= 2.1.1
* python3-PyGithub (see Useful Links section) 
* python3-tkinter >= 8.6
* python3-xml.etree.ElementTree >= 1.3

You should install all the python3 modules using the `pip3 install *package_name*` command.

(or alternatively using: `sudo apt-get install python3-*package_name*` conmmand)

## Install integrated tools 

* Install the PHPQA (version 1.19) tool through the bash script `phpqa_installation.sh` found in the bash_scripts folder.

To run phpqa's script you need to have: **composer** (see Useful Links section) and the **php-xsl** extension installed (sudo apt-get install php7.2-xls).

More tools to be added in the future.

## How to run it

Steps to run Sourceographer:

* Clone (git clone) or download the project.
* Generate a personal Github API token using the guide included in the Useful Links section.
* Insert the generated token in the `/sourceographer/githubAPI_testers/github_APIInfo.py` script on **line 6**.
* Run Sourceographer by using the command `python3 flowcontroller.py` while being in githubAPI_testers folder.
* Check the results in the outputs folder.

**Note:** The first three steps must be executed only once: the first time you are going to use Sourceographer.

**Note:** Before executing the flowcontroller.py script, make sure that the `indicators.csv` and `input_metrics.csv` files are blank, containing only the column names with no data added.

## Useful Links

* PyGithub lib repo: https://github.com/PyGithub/PyGithub
* Composer installation guide: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-18-04
* PHPQA (v1.19) Github repo: https://github.com/EdgedesignCZ/phpqa/tree/v1.19.0
* Generating a Github API token guide: https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line


## Authors

- Prodromos Polychroniadis (github: [@propol](https://github.com/propol "Prodromos Polychroniadis Github"))
- Apostolos Kritikos (github: [@akritiko](https://github.com/akritiko "Apostolos Kritikos Github"))
