import openpyxl

CountyData = {}

wb = openpyxl.load_workbook('censuspopdata.xlsx')

st = wb['Population by Census Tract']

for row in range(2, st.max_row + 1):

    tract  = st['A' + str(row)].value
    state  = st['B' + str(row)].value
    county = st['C' + str(row)].value
    pop    = st['D' + str(row)].value

    CountyData.setdefault(state, {})

    CountyData[state].setdefault(county, {'Pop':0,'Tracts': 0})
    CountyData[state][county]['Pop'] += int(pop)
    CountyData[state][county]['Tracts'] += 1