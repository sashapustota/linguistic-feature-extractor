<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h1 align="center">Cultural Data Science 2023</h1> 
  <h2 align="center">Assignment 1</h2> 
  <h3 align="center">Language Analytics</h3> 


  <p align="center">
    Aleksandrs Baskakovs
  </p>
</p>


<!-- Assignment instructions -->
## Assignment instructions

This assignment concerns using ```spaCy``` to extract linguistic information from a corpus of texts.

The corpus is an interesting one: *The Uppsala Student English Corpus (USE)*. All of the data is included in the folder called ```in``` but you can access more documentation via [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

For this exercise, you should write some code which does the following:

- Loop over each text file in the folder called ```in```
- Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
- For each sub-folder (a1, a2, a3, ...) save a table which shows the following information:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

<!-- ABOUT THE PROJECT -->
## About the project
This repository contains a Python script ```main.py``` that counts the relative frequency of nouns, verbs, adjectives, and adverbs per 10,000 words in the Uppsala Student English Corpus (USE) using the ```en_core_web_md``` model from ```SpaCy``` . The script also counts the total number of unique PER (person), LOC (location), and ORG (organization) entities in each text file. The results are saved in a table and exported as a ```.csv``` file.

<!-- Data -->
## Data
The corpus consists of 1,489 essays written by 440 Swedish university students of English at three different levels, the majority in their first term of full-time studies. The total number of words is 1,221,265, which means an average essay length of 820 words. A typical first-term essay is somewhat shorter, averaging 777 words. There are 14 different categories of essays, ranging from argumentative essays to summaries, and from book reviews to literary analyses. The 14 folders in the ```USEcorpus``` folder represent the 14 categories. More detailed description of the data can be found in the ```readme.md``` file in the ```in``` folder.

<!-- USAGE -->
## Usage
To use the code you need to adopt the following steps.

**NOTE:** Please note that the instructions provided here have been tested on a Mac machine running macOS Ventura 13.1, using Visual Studio Code version 1.76.0 (Universal) and a Unix-based bash terminal. While they should also be compatible with other Unix-based systems like Linux, slight variations may exist depending on the terminal and operating system you are using. To ensure a smooth installation process and avoid potential package conflicts, it is recommended to use the provided ```run.sh``` bash file, which includes the necessary steps to create a virtual environment for the project. However, if you encounter any issues or have questions regarding compatibility on other platforms, please don't hesitate to reach out for assistance.

1. Clone repository
2. Run ``run.sh`` in the terminal

Please note that the script is designed to work with the way data is structured in the ```USEcorpus``` folder, the script may not work if the data is structured differently.

### Clone repository

Clone repository using the following lines in the your terminal:

```bash
git clone https://github.com/sashapustota/linguistic-feature-extractor
cd linguistic-feature-extractor
```

### Run ```run.sh```

The ``run.sh`` script is used to automate the installation of project dependencies and configuration of the environment. By running this script, you ensure consistent setup across different environments and simplify the process of getting the project up and running.

The script performs the following steps:

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the required packages
4. Runs the ```main.py``` script
5. Deactivates the virtual environment

To run the script, run the following line in the terminal:

```bash
bash run.sh
```

The ```main.py``` script perform the following steps:

1. Installs and loads the spaCy model
2. Loops over each folder in the ```USEcorpus``` folder
3. Loops over each file in the folder
4. Extracts the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
5. Saves the results in a table and exports it as a ```.csv``` file in the ```out``` folder per each sub-folder (a1, a2, a3, ...)

<!-- REPOSITORY STRUCTURE -->
## Repository structure
This repository has the following structure:
```
│   .gitignore
│   README.md
│   requirements.txt
│   run.sh
│
├───in
│   └───USEcorpus
│       ├───a1
│       │       0100.a1.txt
│       │       ...
│       ├───a2
│       │       0100.a2.txt
│       │       ...
│       ...
│       └───c1
│               0140.c1.txt
│               ...
│
├───out
│       .gitkeep
│
└───src
        .gitkeep
        main.py

```
<!-- REPRODUCIBILITY -->
## Reproducibility
The following results were obtained for folder ```c1```:

```
|   | text_name    | RelFreq_NOUN | RelFreq_VERB | RelFreq_ADJ | RelFreq_ADV | Unique_PER | Unique_LOC | Unique_ORG |
|---|--------------|--------------|--------------|-------------|-------------|------------|------------|------------|
| 0 | 0140.c1.txt  | 1571.66      | 932.41       | 472.31      | 403.09      | 0          | 0          | 9          |
| 1 | 0165.c1.txt  | 1745.32      | 817.74       | 581.77      | 284.78      | 0          | 0          | 5          |
| 2 | 0200.c1.txt  | 1176.47      | 1020.61      | 648.57      | 507.79      | 0          | 0          | 12         |
| 3 | 0219.c1.txt  | 1377.48      | 973.51       | 562.91      | 483.44      | 0          | 0          | 10         |
| 4 | 0238.c1.txt  | 1088.65      | 1158.63      | 396.58      | 287.71      | 0          | 0          | 8          |
| 5 | 0501.c1.txt  | 1229.4       | 1023.35      | 460.16      | 425.82      | 0          | 0          | 6          |
| 6 | 0502.c1.txt  | 1319.31      | 1217.34      | 433.4       | 407.9       | 0          | 0          | 5          |
```