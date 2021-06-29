data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 # count = count +1
		if count % 1000 == 0: # %是用來求餘數的
		    print(len(data))

print('檔案讀取完了，總共有',len(data),'筆資料')

sum_len = 0
for d in data:
    sum_len += len(d) # sum_len = sum_len + len(d)
    print(sum_len)

print('留言的平均長度為',sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
# list comprehension(清單快寫法)
# 以上四行可以用以下一行來代替
# good = [d for d in data if 'good' in d]
# or
# bad = ['bad' in d for d in data]
print('一共有',len(good),'筆留言有提到good')
print(good[0])
