import sys

# check if a filename was provided
if len(sys.argv) < 3:
  print("Usage: python3 lowercase.py <input_filename> <output_filename>")
  sys.exit(1)

# open the file for reading
with open(sys.argv[1], "r") as input_file:
  # read the entire file
  text = input_file.read()

# convert the text to lowercase
lowercase_text = text.lower()

# open a new file for writing
with open(sys.argv[2], "w") as output_file:
  # write the lowercase text to the new file
  output_file.write(lowercase_text)
