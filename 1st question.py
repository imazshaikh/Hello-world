#this is how file open and read.

file1 = open('imaz.txt', 'r+')
text_to_read = file1.read()
print(text_to_read)

#we can also print the file name, mode and so on

print(file.name)
print(file1.mode)


#if we wamt to write in the file

file1.write()

#if we need to close the file.(*we need to close the file other wise it will not open the other file if we want to)

file1.close()


