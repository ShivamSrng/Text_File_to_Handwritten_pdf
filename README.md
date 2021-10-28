# Text File to Handwritten PDF
## Introduction
This is a project that converts the contents in text file that is passed to PyCharm to a pdf file of your's own handwriting with similar content and also maintains indentation and all other annotations, etc.



## Use of Jupyter Notebook
In Jupyter Notebook, we take the input of user's handwriting which consist of a page which has UpperCase alphabets, LoweCase Alphabets, Numbers and all the other Special Characters in jpg or any other format. Here the image is in jpg format.
And after taking the page as input we indivisually extract all the characters from page and save it in our computer directory. 


Also utmost care is taken while extraction, because the height and width of each character in extracted image should have similar dimensions. ***Even a slight increase or decrease in dimension would throw an error in PyCharm.***

So to sum up, the use of Jupyter Notebook is just for the extraction of User's handwriting from the image that he/she will upload. Here I, have uploaded **Characters.jpg** in Jupyter Notebook and **Fonts** directory has all the extracted characters and code for it is **Letter_Extraction.ipynb**.

#### Characters.jpg:
![Characters](https://user-images.githubusercontent.com/67229090/139209486-344bfe16-52e0-4058-9e89-81fb79a1f5e2.jpg)



## Use of PyCharm
In PyCharm, original **Text File** in **Assignment** folder which has the content is passed as an input and from that text file each characters are exctracted and based of character found its equivalent image is concatenated using numpy hconcat. And also using textwrapper library we ensure that each line has specific length of characters. And to concat vertically we have used numpy vconcat. 

And atlast the final file is converted from Image to PDF using PIL library. And at the end a message is printed for user that indicates completion of the conversion from text file contents to a PDF file that has similar contents but with the handwriting of User, which is saved in **Assignment** folder with name **Shivam.pdf**.
 
 #### Text File:
 [TextFile.txt](https://github.com/ShivamSrng/Text_File_to_Handwritten_pdf/files/7432156/TextFile.txt)
 
 #### The Final PDF result:
 [Shivam.pdf](https://github.com/ShivamSrng/Text_File_to_Handwritten_pdf/files/7432159/Shivam.pdf)
