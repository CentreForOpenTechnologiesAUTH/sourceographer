# Source-o-grapher Tool [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7080150.svg)](https://doi.org/10.5281/zenodo.7080150)

Source-o-grapher is a tool built with the aim to investigate software resilience aspects of Open Source Software (OSS) projects. The tool uses several metrics from the literature to evaluate an OSS project on four major dimensions: structural (source code), business and legal, integration and social (community of the project). Many of these metrics are automatically acquired by the tool using the Github repository of the project whereas some others are manually input by the expert who performs the analysis.

__NOTE:__ The automatic metrics are calculated - for the time being - only for OSS projects written in PHP Language.

## Requirements & Installation

__Step 1: Install all the requirements before proceeding to next steps:__

* Python >= 3.5
* python3-pandas >= 0.22
* python3-numpy >= 1.13.3
* python3-matplotlib >= 2.1.1
* python3-PyGithub (see Useful Links section) 
* python3-tkinter >= 8.6

You should install all the python3 modules using the `pip3 install *package_name*` command.

(or alternatively using: `sudo apt-get install python3-*package_name*` conmmand)

__Step 2: Install integrated tools:__

* Install the PHPMetrics tool [following the information](https://phpmetrics.github.io/website/getting-started/) you will find in the official project.

## Running the tool

In order to successfully run the tool you need to:

* Clone (git clone) or download the project.
* Generate a personal Github API token using the guide included in the Useful Links section.
* Run Sourceographer by using the command `python3 ossrf.py` after you have prepared the data.csv for your experiment in folder ./data. You can find a detailed description later in this README

## Preparing the __data.csv__ file.

This CSV file hosts the input and the output of the sourceographer analysis. Before you run the script you need to provide information for the following fields:


|Column	|	Name |					Description |
|-------|:-----------------------:|:------------------|
|A 		|	id	|					The id of the project (simple counter)|
|B 		|	project_name	|		The name of the project|
|C 		|	repo_name	|			The github repository name as it appears in the github url|
|D 		|	language	|			The main programming language of the project	|
|E 		|	version_tag		|		The version tag (just number) as it appears on github (i.e. 1.0.0)|
|F		|	version_github_tag	|	The version tag (number with v prefix) (i.e. v1.0.0)	|
|G 		|	repo_url			|	The repository url as it appears on Github |
|H 		|	version_start_date	|	The start date of the version in yyyy-mm-dd format (i.e. 2020-10-10)|
|I 		|	version_end_date	|	The end date of theversion in yyyy-mm-dd format (i.e. 2020-11-11)|

- columns J - BK of the CSV file are used for storing output data so you leave them blank.
- column BL (analysis_complete) is also automatically filled by the script after ossrf has run for the specific record. Every line that has analysis_complete column marked with 1 is ignored by the script in future runs of the algorithm.
- column BM (expert value) is a "helper" column. You can (optionally) put a number there (values between 1 - 5) and it will automatically fill all the expert related indicators of OSSRF with this value. If you have values from an expert, ay this point you need to put those values in the data.csv file manually.


## Theoretical basis

This tool was designed following the theoretical basis of the Resilience Framework for OSS that was first introduced to the following academic work:

_Kritikos A., Stamelos I. (2018) Open Source Software Resilience Framework. In: Stamelos I., Gonzalez-Barahoña J., Varlamis I., Anagnostopoulos D. (eds) Open Source Systems: Enterprise Software and Solutions. OSS 2018. IFIP Advances in Information and Communication Technology, vol 525. Springer, Cham. https://doi.org/10.1007/978-3-319-92375-8_4_

A detailed description of the full framework is available [here](http://users.auth.gr/akritiko/ossrf).

## Useful Links

* PyGithub lib repo: https://github.com/PyGithub/PyGithub
* Composer installation guide: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-18-04
* PHP Metrics installation guide: https://phpmetrics.github.io/website/getting-started/
* Generating a Github API token guide: https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

## Contributors
- Apostolos Kritikos, [e-mail](mailto:akritiko@csd.auth.gr), [Github](https://github.com/akritiko)
- Prodromos Polychroniadis, [e-mail](mailto:prodpoly@csd.auth.gr), [Github](https://github.com/propol)
- Ioannis Stamelos, [e-mail](mailto:stamelos@csd.auth.gr), [Github](https://github.com/Stamelos)
- Petros Kafkias, [Github](https://github.com/kafkiasp)
- Chrysovalantis Vrasidis, [Github](https://github.com/chvrasidis)
