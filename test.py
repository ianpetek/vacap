dic = {('123.656.13.6', 65224) : 'test', ('123.sd.13.6', 487) : 'asd'}
cl_str = ''
for key, val in dic.items():
  cl_str += str(key[0]) + ':' + str(key[1]) + '  ' + val +'\n'
print(cl_str)