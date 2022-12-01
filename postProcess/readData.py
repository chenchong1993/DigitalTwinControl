import json
from influxdb import InfluxDBClient

def readFile(fileName):
    with open(fileName) as f:
        result = f.readline() ##Assume the sample file has 3 lines
    resuList = result[result.find(":")+1:-3].split('},')
    # encoded_string = map(str, resuList)
    # print(list(encoded_string))
    for tmp in resuList:
        x = float(tmp[tmp.find("u'y':")+6:tmp.find("u'y':")+15].replace(',',''))
        y = float(tmp[tmp.find("u'x':")+6:tmp.find("u'x':")+15].replace(',',''))
        print(x)
        print(y)
        with open("loc2.txt", encoding="utf-8", mode="a") as file:
            file.write(str(x)+","+str(y)+"\n")
            # print(resuList)
    # points = result.get_points()
    # model = globals()[result]
    # print(model)
    # for item in points:
    #     # print(item['name'])
    #     f = open(item['name'], "a")
    #     itemsql = ""
    #     itemsql = "select * from " + item['name'] + ";"
    #     result = client.query(itemsql)
    #     print("Result: {0}".format(result))
    #     f.write(str(result) + "\n------end--------\n")
    #     f.close()
readFile("uwb_task_276")