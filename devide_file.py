import os,time
def  devide_file(inventory_file_path,inventory_dir_path):
	files_record={}
	with open(inventory_file_path,encoding='utf-8',errors='ignore') as f:
		f.readline()
		for line in f:
			try:
				sku,asin,price,quantity=line.strip().split('\t')
			except:
				continue
			if '-' in sku:
				code,series=sku[::-1].split('-',1)
				code=code[::-1]
				series='%s-%s' % (series[::-1],code[0])
			else:
				series='other'
			if series not in files_record:
				files_record[series]=open('%s/%s.txt' % (inventory_dir_path,series),'w')
			files_record[series].write(line)

accounts=open('accounts.txt','r').read().splitlines()
region=accounts.pop(0)
region=region.upper()
for account in accounts:
	account=account.strip()
	if os.path.isdir('%s/%s' % ('.',account)):
		inventory_dir_path='%s/%s' % ('.',account)
		inventory_file_path='%s/%s.txt' % (inventory_dir_path,region)
		if not os.path.isfile(inventory_file_path):
			continue
		else:
			devide_file(inventory_file_path,inventory_dir_path)
