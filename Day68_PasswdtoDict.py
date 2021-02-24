# Day 68:  /etc/passwd to Dict
# Write a function, passwd_to_dict, that reads from a Unix-style “password file,” commonly stored as /etc/passwd, 
# and returns a dict based on it.
# Each line is one user record, divided into colon-separated (:) fields.The first field (index 0) is the username, 
# and the third field(index 2) is the user’s unique ID number.

# Function takes filename (passwd.txt) as argument, iterates over each line.
# If line not startswith '#'(Comment), and not blank line, extract field1 i.e words[0] (Username), field3 i.e 
# words[3] (ID), converts ID field to 'int', store them in userdata dictionary, when EOF, return the dict.

def passwd_to_dict(fname):
    userdata = dict()
    with open(fname) as fhand:
        for line in fhand:
            if not line.startswith(("#", "\n")):
                words = line.split(":")
                userdata[words[0]] = int(words[2])
    return userdata
    
# Main
# Function passwd_to_dict returns a dict with username as Key & ID as Value, result is displayed.

print(passwd_to_dict("passwd.txt"))
                
    

