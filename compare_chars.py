import sys

# check if both filenames were provided
if len(sys.argv) < 3:
  print("Usage: python3 compare.py <file1> <file2>")
  sys.exit(1)

# open the first file for reading
with open(sys.argv[1], "r") as file1:
  # read the entire file
  text1 = file1.read()

# open the second file for reading
with open(sys.argv[2], "r") as file2:
  # read the entire file
  text2 = file2.read()

# compare the lengths of the two files
if len(text1) != len(text2):
  print("The two files have different lengths.")

# compare the characters in the two files
files_are_identical = True
for i in range(min(len(text1), len(text2))):
  if text1[i] != text2[i]:
    files_are_identical = False
    print(f"The two files have different characters at index {i}: {text1[i]} vs {text2[i]}.")

# if the files are identical, print a message
if files_are_identical:
  print("The two files are identical.")

# print the length of the files
print(f"The length of the first file is {len(text1)} characters.")
print(f"The length of the second file is {len(text2)} characters.")
