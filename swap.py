#### Original Files read & capture contents in respective string variables - START###
F1Content = ""
F2Content = ""
File1 = open("File1.txt")
File2 = open("File2.txt")
for f1 in File1:
    F1Content = F1Content + f1
print("\n----Original File1 Contents are:---- \n" + F1Content)
for f2 in File2:
    F2Content = F2Content + f2
print("\n----Original File2 Contents are:---- \n" + F2Content)
#### Original Files read and capture contents in respective string variables - END###
#### Files write/swap contents - START###
File1 = open("File1.txt", "w+")
File2 = open("File2.txt", "w+")
File1.write(F2Content)
File2.write(F1Content)
#### Files write/swap contents - START###
print("\n----Content Swaping Finished!! Let us now see updated contents:---- \n")
#### Updated Files read and capture contents in respective string variables - START###
F1Content = ""
F2Content = ""
File1 = open("File1.txt")
File2 = open("File2.txt")
for f1 in File1:
    F1Content = F1Content + f1
print("\n----Updated File1 Contents are:---- \n" + F1Content)
for f2 in File2:
    F2Content = F2Content + f2
print("\n----Updated File2 Contents are:----\n" + F2Content)
File1.close()
File2.close()
#### Updated Files read and capture contents in respective string variables - END###