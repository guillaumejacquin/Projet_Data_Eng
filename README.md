# Data Eng Project

## Introduction

1. PROJECT DONE WITH 
	1. Visual Studio code : https://code.visualstudio.com/

## User's guide

### How to run the project

1. First step, you need to clone it : "git clone adresse_publique_de_votre_projet"
2. Second step, you have to run the requirements.txt you can run it with : "python -m pip install -r requirements.txt"
3. Third step, you have a directory nammed kaggle api with a file named kaggle.json.
4. Fourth step, copy the file nammed kaggle.json and paste it on the directory named "C:\Users\[username]\.kaggle" maybe the first letter the "C:" can be different the most important is the directory nammed ".kaggle" go in and paste the kaggle.json in.
5. Fifth step, When you will run the project the data will be download on the directory of the main.py.
6. Sixth step, If you have a bug with the api you have a directory with the source data and the main will execute it automatically.
7. Seventh step, execute it with : "python main.py"

### Packages 

1. All the packages you need will be on the requirements.txt.
2. Ip of our server by the website http://127.0.0.1:8050/

## Developer's guide	

### Main

1. Our main will call the others functions.
	1. Path = os.getcwd() will put the path at the same place of the main.py.
	2. script_download(Path) will execute the download of our data from kaggle website with the kaggle Api and will store it on the path.
	3. data = Initiation_data(Path) will read the csv and do the modification on it.
	4. Histogram_States_Genders_Deaths, Histogram_States_Ethinicity_Deaths, Map = Creation_histogram_Map(data) will create 3 variables who will store the Gaphics and he map.
	5. display_ui_interface(Histogram_States_Genders_Deaths, Histogram_States_Ethinicity_Deaths, Map) will use this 3 variables for the dashboard.

### Packages 

1. All the packages you need will be on the requirements.txt.

### Data

1. DATA OF KAGGLE 

1. url of our dataset : https://www.kaggle.com/kannan1314/innocent-deaths-caused-by-police-all-time
	2. if you want to downloads the data you will need to register yourself on the website kaggle, i will put on the directory the same dataset but you can download it if you want to be sure of the integrity of this last one.

### Ui

1. On this script we will create our interface
2. It will be runned automatically

## Analysis report

1. The three states who have the most innocent killed by the cops are the california (CA), the Texas (TX) and Florida (FL).
2. Most innocent killed are aged between 20 and 40 years.
3. Most of them are Male.
4. Most people who are killed by the cops have an average of 30 years old

## Conclusion

1. Many of the innocent people killed are between 20 and 40 years of age, with a maximum around 30 years of age. 
2. The most dangerous states are the california (CA), the Texas (TX) and Florida (FL).
3. A large majority of the innocent people killed by the police are men.






