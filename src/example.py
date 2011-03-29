from lpod.document import odf_new_document
from lpod.table import odf_create_table, odf_create_cell

from random import randrange

#import lpod_vle
from syntax import of_formula, of_intro
from stats import of_average, of_min, of_max

#We create a spreadsheet just for the example
doc = odf_new_document('spreadsheet')
body = doc.get_body()
table = odf_create_table(u"Data", width=5, height=5)
body.append(table)
c=0
l=0
for c in range(5):
    for l in range(5):
        v = randrange(0,1000)
        table.set_value((c, l), v)

#Then, we write some statistics about the data in a new sheet
table = odf_create_table('Stats', width=3, height=2)
body.append(table)
table.set_value((0,0), "Average")
table.set_value((1,0), "Maximum")
table.set_value((2,0), "Minimum")

#average
formula=of_formula(of_intro(), of_average(u'Data.A1:E5'))
cell = odf_create_cell()
cell.set_formula(formula)
table.set_cell((0,1), cell)

#maximum
formula=of_formula(of_intro(), of_max(u'Data.A1:E5'))
cell = odf_create_cell()
cell.set_formula(formula)
table.set_cell((1,1), cell)

#minimum
formula=of_formula(of_intro(), of_min('Data.A1:E5'))
cell = odf_create_cell()
cell.set_formula(formula)
table.set_cell((2,1), cell)

doc.save("out.ods")
