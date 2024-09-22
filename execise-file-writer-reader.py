# This program writes and reads a file.

filename = "user-settings.csv"

# Write to a file
new_user = "Ka Yi, High, 12"
with open(filename, "a") as fWrite: # appending file
    fWrite.write("\n"+new_user)
    fWrite.close()
print(f"'{new_user}' has been added to the file.")

# Read from a file
with open(filename, "r") as fReader:
    text = fReader.read()      
    fReader.close()
splitTxt = text.split("\n")
print(splitTxt)
