 #* PROJECT |

import pprint
import ExcelData

data = pprint.pformat(ExcelData.CountyData)

openfile = open('census2010.py', 'w')

openfile.write(data)

openfile.close()

print('Done.')
