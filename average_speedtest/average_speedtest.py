#!/usr/bin/python3
import subprocess
import json
import sys

downloads=[]
uploads=[]
iterations=10

def convertToMbps(bandwidth):
    return bandwidth / 125000

def average(list):
    return sum(list) / len(list)

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Installing speedtest cli tool...")
install("speedtest-cli")

print("Running %d iterations" % iterations)
for x in range(0, iterations):
    print("running iteration #%d..." % (x + 1))
    speedtestData = json.loads(subprocess.getoutput('speedtest-cli --json'))
    downloads.append(convertToMbps(speedtestData['download']))
    uploads.append(convertToMbps(speedtestData['upload']))
    print("Iteration #{} download: {} Mbps".format(x + 1, downloads[x]))
    print("Iteration #{} upload: {} Mbps \n".format(x + 1, uploads[x]))

print("Average download: {}".format(average(downloads)))
print("Average upload: {}".format(average(uploads)))

