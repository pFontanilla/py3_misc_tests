# Import Error Checks
import os, sys, time, pathlib
from xlrd import open_workbook
from xlwt import Workbook
from datetime import datetime

except ImportError as error:
    print(error, "\n")
    input("Press enter key to exit...\n")
    sys.exit(1)
except:
    print("Failure with imports:\n", sys.exc_info()[0], "\n")
    input("Press Enter Key to exit...\n")
    sys.exit(1)

WBPath = []
# Ensure correct number of input files.
if len(sys.argv) == 3:
    WBPath.append(sys.argv[1])
    WBPath.append(sys.argv[2])
    os.chdir('..')
# If missing any input files, ask User to select from files in current directory.
else:
    os.chdir('..')
    print("Selecting files from current directory of batch file.\n")
    files = [f for f in os.listdir('.') if (os.path.isfile(f) and (f[-3:] == 'xls'))]
    print(os.getcwd(), "\n")

    for fileNumber, file in enumerate(files):
        print(fileNumber, ": ", file)

    print("\n")
    print("Type a number to select one input file then press the Enter Key.")
    choice1 = input()
    if not choice1:
        print("No Input Detected.")
        input("Press Enter Key to exit...\n")
        sys.exit(1)
    try:
        choice1 = int(choice1)
    except ValueError:
        print("Input is not an integer.")
        input("Press Enter Key to exit...\n")
        sys.exit(1)
    if choice1 < 0 or choice1 >= len(files):
        print("Invalid File Number Selected.\nPlease choose a number from above list.")
        input("Press Enter Key to exit...\n")
        sys.exit(1)

    print("Type a number to select the second input file then press the Enter Key.")
    choice2 = input()
    if not choice2:
        print("No Input Detected.")
        input("Press Enter Key to exit...\n")
        sys.exit(1)
    try:
        choice2 = int(choice2)
    except ValueError:
        print("Input is not an integer.")
        input("Press Enter Key to exit...\n")
        sys.exit(1)
    if choice2 < 0 or choice2 >= len(files):
        print("Invalid File Number Selected.\nPlease choose a number from above list.")
        input("Press Enter Key to exit...\n")
        sys.exit(1)

    if choice2 == choice1:
        print("Old and New Files cannot be the same File.")
        input("Press Enter Key to exit...\n")
        sys.exit(1)

    for filenumber, file in enumerate(files):
        if filenumber == choice1:
            WBPath.append(os.getcwd() + "\\" + file)
        if filenumber == choice2:
            WBPath.append(os.getcwd() + "\\" + file)

print("\nFile 1 is: ", os.path.basename(WBPath[0]))
print("File 2 is: ", os.path.basename(WBPath[1]), "\n")

# Ensure input files are of type ".xls"
for inputfile in WBPath:
    if ".xls" not in pathlib.Path(inputfile).suffix:
        print("Input files must have \".xls\" extension.\n")
        input("Press enter key to exit...\n")
        sys.exit(1)

# Ensure input files are correctly labelled.
namecheck = False
for path in WBPath:
    if "old" in os.path.basename(path):
        oldWB = open_workbook(path)
    elif "new" in os.path.basename(path):
        continue
    else:
        # print("Need one input file with containing \"new\"\n and one containing \"old\" (case-sensitive). \n")
        # input("Press enter key to exit...\n")
        namecheck = True
for path in WBPath:
    if "old" in os.path.basename(path):
        continue
    elif "new" in os.path.basename(path):
        newWB = open_workbook(path)
    else:
        # print("Need one input file with containing \"new\"\n and one containing \"old\" (case-sensitive). \n")
        # input("Press enter key to exit...\n")
        namecheck = True

# If one of the files is not named correctly, then have the user input the corresponding dates of each file.
Date1 = False
Date2 = False
if namecheck:
    print(
        "One or more files could not be determine as new or old.\nFor this functionality, one file must be named \"OldAMPL\" and the other as \"NewAMPL\".\n")
    timeformat = "%m.%d.%Y"
    loopCheck = False
    while not loopCheck:
        Date1 = input(
            "Input the date which represents the following file, in the form \"MM.DD.YYYY\" then press Enter\n{}\n".format(
                os.path.basename(WBPath[0])))
        if Date1.startswith('"'):
            Date1 = Date1[1:]
        if Date1.endswith('"'):
            Date1 = Date1[:-1]
        if len(Date1.split(".")) is not 3:
            print("Input \"", Date1, "\" was not correctly formatted.\nPlease try again.\n")
            continue
        if len(Date1.split(".")[0]) is not 2:
            print("Month \"", Date1.split(".")[0], "\" was not correctly formatted.\nPlease try again.\n")
            continue
        if len(Date1.split(".")[1]) is not 2:
            print("Day \"", Date1.split(".")[1], "\" was not correctly formatted.\nPlease try again.\n")
            continue
        if len(Date1.split(".")[2]) is not 4:
            print("Year \"", Date1.split(".")[2], "\" was not correctly formatted.\nPlease try again.\n")
            continue
        for count, period in enumerate(Date1.split(".")):
            try:
                intthing = int(period)
            except ValueError:
                print(period, "is not a valid number.")
                input("Press enter key to exit...\n")
                sys.exit(1)
        try:
            trueDate1 = datetime.strptime(Date1, timeformat)
        except ValueError:
            Date1 = Date1.split(".")
            if Date1[0] < 0 or 12 < Date1[0]:
                print(Date1[0], "is not a valid month.\nPlease try again.")
                continue
            if Date1[1] < 0 or 31 < Date1[1]:
                print(Date1[0], "is not a valid day.\nPlease try again.")
                continue
            if Date1[2] < 0 or 30 < Date1[2]:
                print(Date1[2],
                      "is not a valid year.\nThe program built to not accept the year (20)30 as there must be new technologies available and the script can be updated).\nPlease try again.")
                continue
        loopCheck = True
        print("\n")
    loopCheck = False

    while not loopCheck:
        Date2 = input(
            "Input the date which represents the 2nd file using the same format as above \"MM.DD.YYYY\" then press Enter\n{}\n".format(
                os.path.basename(WBPath[1])))
        if Date2.startswith('"'):
            Date2 = Date2[1:]
        if Date2.endswith('"'):
            Date2 = Date2[:-1]
        if len(Date2.split(".")) is not 3:
            print("Input \"", Date2, "\" was not correctly formatted.\nPlease try again.\n")
            continue
        if len(Date2.split(".")[0]) is not 2:
            print("Input \"", Date2.split(".")[0], "\" was not correctly formatted.\nPlease try again.\n")
            continue
        if len(Date2.split(".")[1]) is not 2:
            print("Input \"", Date2.split(".")[1], "\" was not correctly formatted.\nPlease try again.\n")
            continue
        if len(Date2.split(".")[2]) is not 4:
            print("Input \"", Date2.split(".")[2], "\" was not correctly formatted.\nPlease try again.\n")
            continue
        for count, period in enumerate(Date2.split(".")):
            try:
                intthing = int(period)
            except ValueError:
                print(period, "is not a valid number.")
                input("Press enter key to exit...\n")
                sys.exit(1)
        try:
            trueDate2 = datetime.strptime(Date2, timeformat)
        except ValueError:
            Date2 = Date2.split(".")
            if Date2[0] < 0 or 12 < Date2[0]:
                print(Date2.split(".")[0], "is not a valid month.\nPlease try again.")
                continue
            if Date2[1] < 0 or 31 < Date2[1]:
                print(Date2.split(".")[1], "is not a valid day for this month.\nPlease try again.")
                continue
            if Date2[2] < 0 or 30 < Date2[2]:
                print(Date2.split(".")[2],
                      "is not a valid year.\nNote: The program built to not accept the year (20)30 as there must be new technologies available and the script can be updated).\nPlease try again.")
                continue
        loopCheck = True

    if trueDate1 == trueDate2:
        print("You put the same date for both files.. :()", sys.exc_info()[0])
        input("Press enter key to exit...\n")
        sys.exit(1)
    elif trueDate1 < trueDate2:
        oldDate = Date1
        newDate = Date2
        oldWB = open_workbook(WBPath[0])
        newWB = open_workbook(WBPath[1])
    elif trueDate1 > trueDate2:
        oldDate = Date2
        newDate = Date1
        oldWB = open_workbook(WBPath[1])
        newWB = open_workbook(WBPath[0])

oldWS = oldWB.sheet_by_index(0)
newWS = newWB.sheet_by_index(0)

# Ensure new file has at least all of the columns of the old file.
try:
    missingHeaders = AMPLfuncs.header_check(oldWS, newWS)
except:
    print("Error when checking headers:", sys.exc_info()[0])
    input("Press enter key to exit...\n")
    sys.exit(1)
if missingHeaders:
    print("New file is missing columns from the old file.\nMissing headers:\n")
    for header in missingHeaders:
        print(header.rjust(8, ' '))
    print("")
    input("Press enter key to exit...\n")
    sys.exit(1)

print(time.perf_counter(), "seconds to setup.\n")
# ---------------------------------------------------------------------------------------------------

# Gather index of Valid To and MS Column
try:
    oldThalesPN = AMPLfuncs.find_header(oldWS, "Thales P/N")
    newThalesPN = AMPLfuncs.find_header(newWS, "Thales P/N")
    oldMPNMaterial = AMPLfuncs.find_header(oldWS, "MPN Material")
    newMPNMaterial = AMPLfuncs.find_header(newWS, "MPN Material")
    oldValidto = AMPLfuncs.find_header(oldWS, "Valid To")
    newValidto = AMPLfuncs.find_header(newWS, "Valid To")
    oldMS = AMPLfuncs.find_header(oldWS, "MS")
    newMS = AMPLfuncs.find_header(newWS, "MS")
# print("oldValidto Column is:", oldValidto)
# print("newValidto Column is:", newValidto)
# print("oldMS Column is:", oldMS)
# print("newMS Column is:", newMS)
except:
    print(sys.exc_info()[0])
    print("Error When Collecting Column Locations")
    input("Press enter key to exit...\n")
    sys.exit(1)

try:
    print("Total Number of Rows in New AMPL: ", newWS.nrows)
    newDataFilteredRows = [row for row in range(1, newWS.nrows) if (newWS.cell(row, newValidto).value != "12/31/9999")]
    newDataFilteredRows = [row for row in newDataFilteredRows if (
            newWS.cell(row, newMS).value == "RS"
            or newWS.cell(row, oldMS).value == "DQ"
            or newWS.cell(row, oldMS).value == "SD"
            or newWS.cell(row, oldMS).value == "MD")]
    print("Filtered by date and MS: ", len(newDataFilteredRows), "\n")
except:
    print(sys.exc_info()[0])
    print("Error applying filters to newAMPL.")
    input("Press enter key to exit...\n")
    sys.exit(1)

# Find rows that are obsolete (MD or SD), but with Valid-To Date being Infinity
try:
    invalidRows1 = [(row - 1) for row in range(1, newWS.nrows) if (
            newWS.cell(row, newValidto).value == "12/31/9999"
            and (newWS.cell(row, newMS).value == "MD"
				 or newWS.cell(row, newMS).value == "SD"
                 or newWS.cell(row, newMS).value == "DQ"))]
except:
    print(sys.exc_info()[0])
    print("Error finding invalid Data in newAMPL.")
    input("Press enter key to exit...\n")
    sys.exit(1)

# Find rows that are active (VM) but with Valid-To Date being non-infinity
try:
    invalidRows2 = [(row - 1) for row in range(1, newWS.nrows) if (
            newWS.cell(row, newValidto).value != "12/31/9999"
            and (newWS.cell(row, newMS).value == "VM"
				 or newWS.cell(row,newMS).value == "RS"))]
except:
    print(sys.exc_info()[0])
    print("Error finding invalid Data in newAMPL.")
    input("Press enter key to exit...\n")
    sys.exit(1)

# OldDataHash uses (ROH,HERS) as key, (ValidTo) as value.
# NewDataHash uses (ROH,HERS) as key, (row# in excel) as value.
# OldDataHash is Old AMPL Valid-To Values
# OldDataHash2 is Old AMPL MS Values
# NewDataHash created via filtered data.

# oldDataHash does not pre-filter for everything with a "Valid-to" of "12/31/9999", as the current logic of the program will capture any part in the FilteredNewDatahash which is not found in the oldDataHash.
oldDataHash = {
    (oldWS.cell(row, oldThalesPN).value, oldWS.cell(row, oldMPNMaterial).value): oldWS.cell(row, oldValidto).value for
row in range(1, oldWS.nrows)}

oldDataHash2 = {
    (oldWS.cell(row, oldThalesPN).value, oldWS.cell(row, oldMPNMaterial).value): oldWS.cell(row, oldMS).value for
row in range(1, oldWS.nrows)}

newDataHashFiltered = {(newWS.cell(row, newThalesPN).value, newWS.cell(row, newMPNMaterial).value)
                       : row for row in newDataFilteredRows}

print(time.perf_counter(), "seconds to pre-filter & hash.\n")

# newObsoleteHash uses (ROH,HERS) as key, (row# in Excel as value)
# Cross references Old and New AMPLs
newObsoleteHash = {}

try:
    # For each item in the New Month with both: 1) A Valid-To date which is non-infinity; 2)An "MS" that is not VM or EX;
    for key, value in newDataHashFiltered.items():
        # If the part was active last month, then capture the row index of this part in the AMPL.
        if key in oldDataHash:
            if oldDataHash[key] == "12/31/9999":
                newObsoleteHash[key] = (value - 1)
        # Alternatively, if the part did even not exist last month, then capture the row index of this part in the AMPL.
        else:
            newObsoleteHash[key] = (value - 1)
except:
    print(sys.exc_info()[0])
    input("Press enter key to exit...\n")
    sys.exit(1)

# To be filled to reflect an AMPL containing only newly discovered obsolete components.
newObsoleteData = []
invalidData1 = []
invalidData2 = []

try:
    newData, newHeaders = AMPLfuncs.read_ws(newWS, newWB)
except:
    print("Error reading  and storing Worksheet")
    print(sys.exc_info()[0])
    input("Press enter key to exit...\n")
    sys.exit(1)

# Modify the headers to reflect information from two reports
modifiedHeaders = [header for header in newHeaders]
modifiedHeaders = [header.replace("Valid To", "New Valid To") for header in modifiedHeaders]
modifiedHeaders = [header.replace("MS", "New MS") for header in modifiedHeaders]

modifiedHeaders.insert(modifiedHeaders.index("New Valid To"), "Old Valid To")
modifiedHeaders.insert(modifiedHeaders.index("New MS"), "Old MS")
modifiedHeaders.append("Internal Comments")
modifiedHeaders.append("Category for Metrics")

# Add headers to sheet for obsolescence metrics
newObsoleteData.append(modifiedHeaders)

# Add relevant available data for obsolescence metrics
for key, row in newObsoleteHash.items():
    if key in oldDataHash2:
        modifiedRow = [data for data in newData[row]]
        modifiedRow.insert(modifiedHeaders.index("Old MS"), oldDataHash2[key])
        modifiedRow.insert(modifiedHeaders.index("Old Valid To"), oldDataHash[key])
        modifiedRow.append("")
        modifiedRow.append("")
        newObsoleteData.append(modifiedRow)

# Add headers to sheets for AMPL/Valid-To cleanup
invalidData1.append(newHeaders)
invalidData2.append(newHeaders)

# Add to sheets for AMPL/Valid-To cleanup
for row in invalidRows1:
    invalidData1.append(newData[row])
for row in invalidRows2:
    invalidData2.append(newData[row])

summaryData = []
summaryData.extend(
    [
        ['Summary'],
        [''],
        ['No FFF Replacement/Alternate Under Review'],
        ['FFF Alternate Available (RoHS, MFG Suggested Alternate, MFG Acquisition Name Change'],
        ['No Action Required (Not Used or Maintained. Other Sources Available)'],
        ['Total:']
    ]
)

'''
for item in newObsoleteData:
	print(item)
'''

# Create workbook objects and add worksheets using previously generated data
try:
    finalWB = Workbook(encoding='utf-8')
    summaryWS = finalWB.add_sheet("Summary")
    finalWS = finalWB.add_sheet("New Obsolescences")
    invalidValidToWS1 = finalWB.add_sheet("Obsolete MS and Active Valid-To")
    invalidValidToWS2 = finalWB.add_sheet("Active MS and EOL Valid-To")
    AMPLfuncs.write_ws(summaryWS, summaryData)
    AMPLfuncs.write_ws(finalWS, newObsoleteData)
    AMPLfuncs.write_ws(invalidValidToWS1, invalidData1)
    AMPLfuncs.write_ws(invalidValidToWS2, invalidData2)
except:
    print("Error writing new sheets.")
    print("Please ensure destination file to be overwritten is not open.")
    print(sys.exc_info()[0])
    input("Press enter key to exit...\n")
    sys.exit(1)

# Name file using dates if available, otherwise use generic title
try:
    if Date1 and Date2:
        finalWB.save("New Obsolete Components {} to {}.xls".format(oldDate, newDate))
    else:
        finalWB.save("New Obsolete Components.xls")
except:
    print("Error writing new sheets.")
    print("Please ensure destination file to be overwritten is not open.")
    print(sys.exc_info()[0])
    input("Press enter key to exit...\n")
    sys.exit(1)

print(time.perf_counter(), "seconds to create new workbook.\n")

input("Completed all currently created code. Press Enter")
sys.exit(1)
