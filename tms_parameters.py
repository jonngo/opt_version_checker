import csv
from texttable import Texttable

class TmsExtraction:
    def load_tms_parameters(self,tms_param_file):
        try:
            with open(tms_param_file, 'r') as f:
                reader = csv.reader(f)
                mlist = [row for row in reader if len(row) == 2 if ".ver" in row[0]]
        except(IOError):
            print('IOError')
        except(ValueError):
            print('ValueError')

        mlist.insert(0,['TAG','VALUE'])

        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_dtype(['t', 't'])  # text
        table.set_cols_width([50, 200])
        table.set_cols_align(["l", "l"])
        table.add_rows(mlist)
        print(table.draw())
        return mlist