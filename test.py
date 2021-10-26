# The following script will parse the gitlog for the latest ticket numbers
# Passing those along with an updated version string into the release script
import subprocess

try:
    # Opening file to read
    file1= open("gitlog-oneline.sh","r")

    # Reading output of gitlog-oneline.sh
    subprocess1 = subprocess.Popen(str(file1.read()), shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess1.stdout.read()

    # Splitting each line
    splitNewLine = str(subprocess_return).split("\\n")
    lineAttributeList = list()

    # Loop to further split each line based on spaces
    for line in splitNewLine:
        lineAttributeList.append(line.split(" "))

    found = False
    ticketNumber = list()
    versionNumber = []

    # Iterating for tickets and versionNumber
    for lineAttribute in lineAttributeList:
        for attribute in lineAttribute:
            if "Merged" == attribute:
                found = True
            if "[" in attribute and found == False:
                # Filtering ticketNumber on the basis of square bracket
                ticket = attribute.replace("[", "")
                ticket = ticket.replace("]", "")
                ticketNumber.append(ticket)
            # Find version number starting from v1, ignore the one that ends with closing round bracket
            if found == True and "v1" in attribute and ")" not in attribute:
                versionNumber.append(attribute)
                break

    # Sending incremented version number string and a list of the filtered ticket numbers as input
    subprocess.call(["bash" , "release-add-tickets.sh", str(versionNumber[0]), str(list(set(ticketNumber)))])

except Exception as err:
    print("Exception found!\n" + str(err))