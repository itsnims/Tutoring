import os.path

def filter_comments(in_file, out_file):

    #first we need to check if it fullfills the criterias
    if not os.path.exists(in_file):
        raise Exception("File " + in_file + " does not exist!")
    if not in_file.endswith(".py"):
        raise Exception("Invalid filename: " + in_file)

    #we need to open the reading file and the writting file
    with open(in_file, "r") as input, open(out_file, "w") as output:
        #if there is no hash in the line, copy it as it is
        for line in input:
            if "#" not in line:
                output.write(line)
            #if it starts with hash, there cant be any code anyway so omit
            elif line.startswith("#"):
                continue
            #if the hash comes at the end, read till the hash and then break
            else:
                index = 0
                for ch in line:
                    if ch == "#":
                        break
                index += 1
                output.write(line[0: index] + "\n")