# Introduction to Research Methods - Final Project

# General information
This repository contains the files used for my quantitative analysis for the course Introduction to Research Methods. For this research I studied the frequency with which the words 'OK' is being used by both men and women, as opposed to the longer versions such as 'okay', 'oke', and 'oké'. To do this, I had to annotate the Tweets from the Dutch Twitter Corpus, and for that I wrote a Python Script, that would generate a CSV-file. 

# Dutch Twitter Corpus
The Tweets are available on the server of the University of Groningen. To transfer the preferred files, copy them by typing in the terminal:
`scp -r <studentnumber>@karora.let.rug.nl:/net/corpora/twitter2/Tweets/<year>/<month>/<day>/<hour-file> <target-directory-on-local-storage>`

Watch out, the files contain millions of tweets and are incredibly large. The files should then be saved in a folder called 'dataset', which should be in the same folder as the Python script. 

# Python Script
The user should use at least Python 3.6+. The libraries that are used are internal to Python, so no external libraries need to be installed. The Python script asks for words to look for in the tweets. These should be provided, separated by a space. Then a file-name is asked from the user. The program then loops through all the files and filters according to the words that have been put in. The Tweet is shown, together with the username, the screenname, and the description. If the Tweet belongs to a woman, you should type 'f'. If the Tweet belongs to a man, you should type 'm'. If not clear, any key is allowed and will skip the Tweet. Meanwhile a CSV-file is created. 

# Notebook
To count the occurrences in the CSV-file, I used the pandas library in Jupyter notebook. For this, it is necessary to install both the Numpy library and the Pandas library. The very short program is only used to make a crosstable.

# CSV File
For every Tweet, the CSV file contains the name of the file it was found in, so that one can copy these files from the corpus and achieve the same results. 
