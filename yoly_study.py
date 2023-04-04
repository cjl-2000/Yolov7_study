import glob
files = glob.glob("./**/"+"*.py",recursive=True)
print(files)