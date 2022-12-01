
from influxdb import InfluxDBClient

client = InfluxDBClient('60.205.57.192', 8086, 'admin', '123456', 'test_aemesc')

print(client.get_list_database())
result = client.query('show measurements;') # 显示数据库中的表
points = result.get_points()
for item in points:
	# print(item['name'])
    f = open(item['name'], "a")
    itemsql = ""
    itemsql = "select * from "+item['name']+";"
    result = client.query(itemsql)
    print("Result: {0}".format(result))
    f.write(str(result) + "\n------end--------\n")
    f.close()

# result = client.query('select * from sec_uwb_task_286;')
# print("Result: {0}".format(result))