string = """To: STANKOVSKI Igor <Igor.Stankovski@thalesgroup.com>; DOBSON Paula <Paula.DOBSON@thalesgroup.com>; KNIAZEV Pavel <Pavel.KNIAZEV@thalesgroup.com>
Cc: Carol Zeng <Carol_Zeng@Jabil.com>; Sharon Tang <Sharon_Tang@Jabil.com>; Nancy Zhan <Nancy_Zhan@Jabil.com>; Patrick Fan <Patrick_Fan@Jabil.com>; Alvin Roxas <Alvin_Roxas@Jabil.com>; Fangwei Cheng <Fangwei_Cheng@Jabil.com>; George Zhu <George_Zhu@Jabil.com>; PURCHASE David <david.purchase@thalesgroup.com>; April Li <April_Li@Jabil.com>; Joseph Duenas <Joseph_Duenas@Jabil.com>; Marry Tian <Marry_Tian@Jabil.com>; FENG Lilly <Lilly.FENG@thalesgroup.com>"""

strings = string.split("<")
strings_final = []

for item in strings:
    for thing in item.split(">"):
        strings_final.append(thing)


for item in strings_final:
    if '@' in item:
        print(item)