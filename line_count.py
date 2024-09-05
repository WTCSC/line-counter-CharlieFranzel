def line_count():
  file = open('file.txt', 'r') # opens the file to read
  lines = file.readlines()     # defines the line variable
  linelist = []                # creates an empty list
  for line in lines:
    linelist.append((line))    # adds the line to list
  file.close()                 # closes the file
  return(int(len(linelist)))    # prints the final number as integer