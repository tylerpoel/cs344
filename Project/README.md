Computer Generated Star Wars Script.

For the final project in CS344 at Calvin University. Tyler Poel, May 20, 2020

This project goal is to create a LSTM network that, when fed
a text file, will generate new text, based off of the text
it was fed. Specifically, I wished to give the model the script for 
the Star Wars Original Trilogy (A New Hope (1977), The Empire Strikes Back (1980), and
Return of the Jedi (1983)), and was interested in how the "script"
the model gave back would read. For comparative purposes, I also ran the 
model on the text "Little Women", by Louisa May Alcott.

In this repo:
draft.txt and proposal.ipynb are both earlier submission steps for this project. Most of what they contain can be seen
in the final submission.

SW_model.ipynb - a Jupyter notebook containing the LSTM newtork used,
along with code for reading in and preparing the Star Wars text.

LittleWomenModel.ipynb - a Jupyter notebook containing the LSTM newtork used,
along with code for reading in and preparing the Little Women text.

To run both of the notebooks above, one needs to first download the .txt files, and when reading in 
the text, change the file path to match where the files are.
The implementation of the LSTM network used in both of these notebooks is the same.

OriginalTirlogy_script.txt and LittleWomen.txt are the files that contain the text needed to train the models 
on the respective data.  

The Star Wars scripts were found at: http://www.scifiscripts.com/scripts_n_z.html

The Little Women text was found at: https://www.planetebook.com/free-ebooks/little-women.pdf

A bulk of the code used to create this project comes from Chapter 8, Section 1 of
"Deep Learning with Python", by François Chollet. The code
can be found here:
https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/8.1-text-generation-with-lstm.ipynb
