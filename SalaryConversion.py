import requests, json

data1 = requests.get("http://jsonplaceholder.typicode.com/users").json()
currencyConverter = requests.get("https://api.exchangeratesapi.io/latest").json() #EUR based
USD_IDR = currencyConverter["rates"]["IDR"]/currencyConverter["rates"]["USD"] #USD based

url = open("salary_data.json","r")
data2 = json.loads(url.read())

mergedData = data1
for i in range(len(data1)):
    del(mergedData[i]['website'])
    del(mergedData[i]['company'])
    for j in range(len(data2["array"])):
        if data1[i]["id"] == data2["array"][j]["id"]:
            mergedData[i]["salaryInIDR"] = data2["array"][j]["salaryInIDR"]
    mergedData[i]["salaryInUSD"] = mergedData[i]["salaryInIDR"] / USD_IDR

print(mergedData)