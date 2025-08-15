class FileHandler:
    def __init__ (self, filename):
        self.filename = filename
        self.file = open(filename, 'r') # Open file for reading

    def read_data(self):
        return self.file.read()
    
    def __del__ (self):
        self.file.close() # Close the file when the object is destroyed
        print("File closed!!")
    
#Create an object of FileHandler
file_obj = FileHandler('daffodils.txt')
print(file_obj.read_data())

# Object is no longer needed, it will be garbage collected, and 
# __del__ method will be called automatically to close the file

    