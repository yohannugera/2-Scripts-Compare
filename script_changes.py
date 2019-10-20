###########################################################################
# Name      : script_checkup.py
# Function  : Accepts two files (unencrypted) and will compare for missing
# Comment   : run in cmd "python script_checkup.py <older file> <new file>         
###########################################################################

import sys

if __name__ == '__main__':
    fileout=sys.stdout
    from sys import argv, stdin
    if len(argv) == 3:
        file1 = open(argv[1],'r')
        list1 = []
        list2 = []
        for x in file1:
            tmp = x.lstrip().split(" ")
            if tmp[0] == "edit":
                list1.append(eval(tmp[2]))
        file2 = open(argv[2],'r')
        for x in file2:
            tmp = x.lstrip().split(" ")
            if tmp[0] == "edit":
                list2.append(eval(tmp[1]))
        changes = set(file1).difference(set(file2))
        new_changes = set(list1).difference(set(list2))
        for x in sorted(new_changes):
            print x
        file1.close()
        file2.close()
        with open('mismatch.txt', 'w') as file_out:
            for line in changes:
                file_out.write(line)

    else:
        print 'Please provide both files...'
