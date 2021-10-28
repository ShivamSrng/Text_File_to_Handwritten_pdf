# Text File to Handwritten PDF
## Introduction
This is a project that converts the contents in text file that is passed to PyCharm to a pdf file of your's own handwriting with similar content and also maintains indentation and all other annotations, etc.

## Use of Jupyter Notebook
In Jupyter Notebook, we take the input of user's handwriting which consist of a page which has UpperCase alphabets, LoweCase Alphabets, Numbers and all the other Special Characters in jpg or any other format. Here the image is in jpg format.
And after taking the page as input we indivisually extract all the characters from page and save it in our computer directory. 

Also utmost care is taken while extraction, because the height and width of each character in extracted image should have similar dimensions. "Even a slight increase or decrease in dimension would throw an error in PyCharm."

So to sum up, the use of Jupyter Notebook is just for the extraction of User's handwriting from the image that he/she will upload. Here I, have uploaded "Characters.jpg" in Jupyter Notebook and "Fonts" directory has all the extracted characters and code for it is "Letter_Extraction.ipynb".
