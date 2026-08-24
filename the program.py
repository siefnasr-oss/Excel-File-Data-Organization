 #* PROJECT |

import pprint
import ExcelData
import census2010

data = pprint.pformat(ExcelData.CountyData)

openfile = open('census2010.py', 'w')

openfile.write(data)

openfile.close()

print('Done.')
