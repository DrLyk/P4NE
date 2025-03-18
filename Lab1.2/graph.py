from openpyxl import load_workbook
from matplotlib import pyplot
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
def getvalue(x):
    return x.value
year = list (map(getvalue, sheet['A'][1:]))
temp = list(map(getvalue, sheet['C'][1:]))
sun = list(map(getvalue, sheet['D'][1:]))
pyplot.plot(year, temp, label="Температура")
pyplot.plot(year, sun, label="Солнце")
pyplot.show()