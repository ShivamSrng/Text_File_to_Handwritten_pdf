import cv2.cv2 as cv2
import numpy as np
import textwrap
from PIL import Image
import os

path = "F:/Py-Charm Projects/Handwritten Text File/Fonts/"
space_path = path + "EmptySpace.jpg"
red_line = path + "RedVLine.jpg"
double_line_path = path + "DoubleLine.jpg"
underscore_path = path + "Line.jpg"
underscore = cv2.imread(underscore_path)
img_redline = cv2.imread(red_line)
n = 55


def header():
    img1 = cv2.imread(space_path)
    title1 = cv2.resize(img1, (25, 60))
    title1 = np.hstack((title1, img1))
    for _ in range(n):
        if _ != 4:
            title1 = np.hstack((title1, img1))
        else:
            title1 = np.hstack((title1, img_redline))
    title1 = np.vstack((title1, title1))
    dlp = cv2.imread(double_line_path)
    li = cv2.resize(dlp, (25, 60))
    li = np.hstack((li, dlp))
    for _ in range(n):
        if _ != 4:
            li = np.hstack((li, dlp))
        else:
            li = np.hstack((li, img_redline))
    title1 = np.vstack((title1, li))
    return title1


def reader_wrapper():
    f = open("Assignment/TextFile.txt", "r")
    data = f.readlines()
    s = ""
    for line in data:
        wrapper = textwrap.TextWrapper(width=n-7)
        line = wrapper.wrap(text=line)
        flag = 1
        for subline in line:
            s += subline + "\n"
            flag = 0
        if flag == 1:
            s += "\n"
    s = s[0:len(s) - 1]
    return s


def img_concat(line):
    dff = n - 3 - len(line)
    redline = cv2.imread(red_line)
    row = cv2.resize(underscore, (25, 60))
    row = np.hstack((row, underscore, underscore, underscore, underscore, underscore, redline))
    temp = []
    lst_characters = ['+', '-', '%', '/', '\\', '.', ',', '"', "'", '$', '=', '!', '^', '&', '*', '(', ')', '_', '-',
                      '{', '}', '[', ']', ':', ';', '|', '?', '~', '#', '<', '>', '@']
    chr_names = ['+', '-', '%', 'Fwdslash', 'BwdSlash', 'FullStop', 'Comma', 'DQ', 'SQ', 'Dollar', 'Equal', 'ExcMark',
                 'Power', 'And', 'Mul', 'OCir', 'CCir', 'Underscore', 'Dash', 'OCur', 'CCur', 'OSqu', 'CSqu', 'Colon',
                 'SemiCol', 'StLine', 'QueMark', 'Air', 'Hash', 'LessThan', 'GreaterThan', 'ARate']
    for ch in line:
        if ch.isalpha():
            if ch.isupper():
                ucase_path = path + "c" + ch + ".jpg"
                temp.append(ucase_path)
            elif ch.islower():
                lcase_path = path + ch.upper() + ".jpg"
                temp.append(lcase_path)
        elif ch.isdigit():
            if ch == "0":
                digit_path = path + "cO.jpg"
                temp.append(digit_path)
            elif ch != "0":
                digit_path = path + ch + ".jpg"
                temp.append(digit_path)
        elif ch.isspace():
            temp.append(underscore_path)
        elif ch in lst_characters:
            ch_name = chr_names[lst_characters.index(ch)]
            chr_path = path + ch_name + ".jpg"
            temp.append(chr_path)
        else:
            temp.append(underscore_path)
    for _ in temp:
        letter_img = cv2.imread(_)
        row = np.hstack((row, letter_img))
    while dff > 2:
        space = cv2.imread(path + "Line.jpg")
        row = np.hstack((row, space))
        dff -= 1
    return row


def img_line(page, txt):
    li = []
    txt_data = txt.split("\n")
    for line in txt_data:
        li.append(img_concat(line))
    page = np.vstack((page, li[0]))
    for row in li[1::]:
        page = np.vstack((page, row))
    return page, len(li)


if __name__ == '__main__':
    image = header()
    txt_file = reader_wrapper()
    pg, l = img_line(image, txt_file)
    diff = n - 23 - l
    underscore = cv2.imread(path + "Line.jpg")
    img = cv2.imread(path + "EmptySpace.jpg")
    title = cv2.resize(underscore, (25, 60))
    title = np.hstack((title, underscore))
    for i in range(n):
        if i < 4:
            title = np.hstack((title, underscore))
        elif i == 4:
            title = np.hstack((title, img_redline))
        else:
            title = np.hstack((title, underscore))
    while diff > 5:
        pg = np.vstack((pg, title))
        diff -= 1
    bottom_lines = cv2.imread(double_line_path)
    bottom_space = cv2.imread(space_path)
    concat = cv2.resize(bottom_lines, (25, 60))
    concat = np.hstack((concat, bottom_lines))
    for _ in range(n):
        if _ != 4:
            concat = np.hstack((concat, bottom_lines))
        else:
            concat = np.hstack((concat, img_redline))
    pg = np.vstack((pg, concat))
    space_concat = cv2.resize(bottom_space, (25, 60))
    space_concat = np.hstack((space_concat, bottom_space))
    for _ in range(n):
        if _ != 4:
            space_concat = np.hstack((space_concat, bottom_space))
        else:
            space_concat = np.hstack((space_concat, img_redline))
    pg = np.vstack((pg, space_concat))
    cv2.imwrite("Assignment/Shivam.jpg", pg)
    image1 = Image.open(r"F:/Py-Charm Projects/Handwritten Text File/Assignment/Shivam.jpg")
    im1 = image1.convert('RGB')
    im1.save(r"F:/Py-Charm Projects/Handwritten Text File/Assignment/Shivam.pdf")
    os.remove(r"F:/Py-Charm Projects/Handwritten Text File/Assignment/Shivam.jpg")
    print("\nCompleted Writing in File, You can now check it..")
