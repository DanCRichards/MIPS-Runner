#!/usr/bin/env python3
import sys
import time
# Title Sequence
print("███╗   ███╗██╗██████╗ ███████╗      ██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗ \n████╗ ████║██║██╔══██╗██╔════╝      ██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗\n██╔████╔██║██║██████╔╝███████╗█████╗██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝\n██║╚██╔╝██║██║██╔═══╝ ╚════██║╚════╝██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗\n██║ ╚═╝ ██║██║██║     ███████║      ██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║\n╚═╝     ╚═╝╚═╝╚═╝     ╚══════╝      ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

if len(sys.argv) > 1:
    importFile = sys.argv[1]
    exportFile = sys.argv[1] + ".converted"
else:
    importFile = input("Filename: ")
    exportFile = importFile + ".converted"


items = list(range(0, 10))
l = len(items)

# So you want to give the code a bit of a looksy? The progress bar literally does nothing. :) 
# They suggest that if you have a progress bar in your applications it makes the user happy. 

printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    time.sleep(0.1)
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

f = open(importFile,"r")
o = open(exportFile, "w")
for line in f.readlines():
    try:
        if line.strip() == "":
            continue

        o.write("mipsInst.assembler.addInstruction('" + line.replace("\n","") + "')\n")
    except:
        print("Beep Boop error occured with line:")
        print(line)
        continue

print()
print("File output at: " + exportFile)
    