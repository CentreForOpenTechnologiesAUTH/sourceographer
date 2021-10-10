# Source-o-grapher Tool

Source-o-grapher is a tool built with the aim to investigate software resilience aspects of Open Source Software (OSS) projects. The tool uses several metrics from the literature to evaluate an OSS project on four major dimensions: structural (source code), business and legal, integration and social (community of the project). Many of these metrics are automatically acquired by the tool using the Github repository of the project whereas some others are manually input by the expert who performs the analysis.

## Requirements & Installation

__Step 1: Install all the requirements before proceeding to next steps:__

* Python >= 3.5
* python3-pandas >= 0.22
* python3-numpy >= 1.13.3
* python3-matplotlib >= 2.1.1
* python3-PyGithub (see Useful Links section) 
* python3-tkinter >= 8.6
* python3-xml.etree.ElementTree >= 1.3

You should install all the python3 modules using the `pip3 install *package_name*` command.

(or alternatively using: `sudo apt-get install python3-*package_name*` conmmand)

__Step 2: Install integrated tools:__

* Install the PHPQA (version 1.19) tool through the bash script `phpqa_installation.sh` found in the bash_scripts folder.

To run phpqa's script you need to have: **composer** (see Useful Links section) and the **php-xsl** extension installed (sudo apt-get install php7.2-xls).

More tools to be added in the future.

## Running the tool

In order to successfully run the tool you need to:

* Clone (git clone) or download the project.
* Generate a personal Github API token using the guide included in the Useful Links section.
* Insert the generated token in the `/sourceographer/githubAPI_testers/github_APIInfo.py` script on **line 6**.
* Run Sourceographer by using the command `python3 flowcontroller.py` while being in githubAPI_testers folder.
* Check the results in the outputs folder.

**Note #1:** The first three steps must be executed only once: the first time you are going to use Sourceographer.

**Note #2:** Before executing the flowcontroller.py script, make sure that the `indicators.csv` and `input_metrics.csv` files are blank, containing only the column names with no data added.

## Theoretical basis

This tool was designed following the theoretical basis of the Resilience Framework for OSS that was first introduced to the following academic work:

_Kritikos A., Stamelos I. (2018) Open Source Software Resilience Framework. In: Stamelos I., Gonzalez-Barahoña J., Varlamis I., Anagnostopoulos D. (eds) Open Source Systems: Enterprise Software and Solutions. OSS 2018. IFIP Advances in Information and Communication Technology, vol 525. Springer, Cham. https://doi.org/10.1007/978-3-319-92375-8_4_

A detailed description of the full framework is available [here](http://users.auth.gr/akritiko/ossrf).

## Useful Links

* PyGithub lib repo: https://github.com/PyGithub/PyGithub
* Composer installation guide: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-18-04
* PHPQA (v1.19) Github repo: https://github.com/EdgedesignCZ/phpqa/tree/v1.19.0
* Generating a Github API token guide: https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

## Authors
- Apostolos Kritikos, [e-mail](mailto:akritiko@csd.auth.gr), [github](https://github.com/akritiko)
- Prodromos Polychroniadis, [e-mail](mailto:prodpoly@csd.auth.gr), [github](https://github.com/propol)
- Ioannis Stamelos, [e-mail](mailto:stamelos@csd.auth.gr), [github](https://github.com/Stamelos)
