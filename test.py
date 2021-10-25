# The following script will parse the gitlog for the latest ticket numbers
# Passing those along with an updated version string into the release script
import subprocess

file1= open("gitlog-oneline.sh","r+")

subprocess1 = subprocess.Popen(str(file1.read()), shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess1.stdout.read()

splitNewLine = str(subprocess_return).split("\\n")
#print (var)
lineAttributeList = list()
for line in splitNewLine:
    # print (i.split(" "))
    lineAttributeList.append(line.split(" "))
#print(lineAttributeList)

found = False
ticketNumber = list()
versionNumber = []

for lineAttribute in lineAttributeList:
    for attribute in lineAttribute:
        #print (k)
        if "Merged" == attribute:
            found = True
        if "[" in attribute and found == False:
            #print (attribute)
            ticket = attribute.replace("[", "")
            ticket = ticket.replace("]", "")
            ticketNumber.append(ticket)
            #print (ticket)
        if found == True and "v1" in attribute and ")" not in attribute:
            #print (k.split(")")[0])
            versionNumber.append(attribute)
            break
    # if found == True:
    #     break 

#print (list(set(ticketNumber)))
#print (versionNumber[0])

# subprocess.call(["ls", "-l"])

subprocess.call(["bash" , "release-add-tickets.sh", str(versionNumber[0]), str(list(set(ticketNumber)))])
#Process = subprocess.Popen('./release-add-tickets.sh %s %s' % (str(versionNumber[0]),str(list(set(ticketNumber))),), shell=True)