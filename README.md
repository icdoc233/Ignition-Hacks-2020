# Ignition-Hacks-2020

The general purpose of this program is to estimate one out of 6 academic attribute of a student (first period grade, second period grade, final grade, study time, number of failures, or number of absences) based on his other 5 attributes, as well as the general trend in his class. 

The program does it by reading an csv file which contains the various attributes of a group of students, and building 5 different models (degree 1 - 5) using the polynomial regression algorithm. After the user enters their desired attribute, the program will ask for the remaining 5 attributes, and return the estimated result for each of the five models, as well as their corresponding R-Square Error values for the user to reference. 

The program stores the five models each time after training. It'll reuse the models if the user's next desired attribute is the same as the previous one. Or else, it'll retrain the models, dumping the previously stored one. 

The example data set, student-mat.csv, is an student performance data set from Paulo Cortez, University of Minho, GuimarÃ£es, Portugal. This data approach student achievement in secondary education of two Portuguese schools, which contains 33 different attributes over 349 students. However, this program only utilizes 6 of the attributes (G1 for first period grade, G2 for second period grade, G3 for final grade, studytime, failures, absences).
The example data set can be found at https://archive.ics.uci.edu/ml/datasets/Student+Performance.
