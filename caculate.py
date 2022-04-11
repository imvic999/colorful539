import json
from main import updateStatus

fp = open('data.json', 'r')
datas = json.load(fp)
fp.close()

count = [0 for n in range(40)]
for data in datas:
    for number in data['numbers']:
        count[number] = count[number]+1
    
print(count)  


hTotal = [0 for n in range(4)]
tTotal = [0 for n in range(10)]
for j in range(0, 4):
    for i in range(0, 10):
        idx = j*10+i
        hTotal[j] = hTotal[j] + count[idx]
        tTotal[i] = tTotal[i] + count[idx]

result = {}
result['date'] = datas[len(datas)-1]['date']
result['all'] = count
result['head'] = hTotal
result['tail'] = tTotal

print(result)
    
fp = open('result.json', 'w')
fp.write(json.dumps(result))
fp.flush()
fp.close() 
    
    
    
    
    