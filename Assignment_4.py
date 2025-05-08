#Read a File and Handle Errors

file1=open('sample1.txt', 'r')
read=file1.read()
print(read)
file1.close()

try:
    file1=open('sample.txt', 'r')
    read=file1.read()
    print(read)
    file1.close()

except FileNotFoundError:
    print("The file 'sample.txt' was not found.")



# Write and Append Data to a File

n=int(input('Enter any number:'))
a=input('Enter the text to write to the file:')
file2=open('output.txt','w')
file2.write(a + '\n')
file2.close()
print('Data successfully written to output.txt.')

 #Additional data

b=input('Enter additional text to append:')
file2=open('output.txt','a')
append=file2.write(b)
file2.close()

#Final Output

print('Final content of output.txt:')
file2=open('output.txt','r')
read=file2.read()
print(read)
file2.close()




