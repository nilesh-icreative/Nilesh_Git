
string = " hello how are yoy hello are"

string = string.split()

diff_element = []
comm_element = []

def element_occur(string):

    for i in string:
        if i not in diff_element:
            diff_element.append(i)
        else:
            comm_element.append(i)

    return '#'.join(comm_element)


print("Repeated Element is:",element_occur(string))
