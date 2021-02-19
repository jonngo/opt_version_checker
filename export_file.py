import pandas as pd
import time

class ExportToFile:
    def __init__(self, path, file_format, content, header, column, title):
        self.path = path
        self.format = file_format
        self.content = content
        self.header = header
        self.column = column
        self.title = title

    def column_index_to_include(self):
        # Return the index of fields to include
        incol = []
        newheader = []
        for n, h in enumerate(self.header):
            a = True
            for key, value in self.column.items():
                if str(key).lower() == str(h).lower():
                    a = False if value else True
                    break
            if a:
                incol.append(n)
                newheader.append(h)
        return incol,newheader

    def export(self):
        #Logic of exporting the content in format to path
        new_content = []
        # new_header = []
        if self.column:
            #Exclude some columns
            incol, new_header = self.column_index_to_include()
            #Remove excluded fields
            for row in self.content:
                new_row = []
                for num, inner_row in enumerate(row):
                    if num in incol:
                        new_row.append(inner_row)
                new_content.append(new_row)
            for a in new_content:
                print(a)
        else:
            #Include all columns
            new_content = self.content
            new_header = self.header

        if self.format == 'HTML':
            self.write_in_html(new_content,new_header)
        elif self.format == 'PDF':
            self.write_in_pdf(new_content,new_header)
        elif self.format == 'CSV':
            self.write_in_csv(new_content,new_header)

    def write_in_html(self,content, header):
        print("\nExport in HTML format to " + self.path)
        for row in content:
            print(row)

    def write_in_pdf(self,content, header):
        print("\nExport in PDF format to " + self.path)
        for row in content:
            print(row)

    def write_in_csv(self,content, header):
        print("\nExport in CSV format to " + self.path)
        rn = [str(c + 1) for c in range(0, len(content))]
        df = pd.DataFrame(content, columns=header, index=rn)
        df.to_csv(self.path+time.strftime("%Y%m%d%H%M%S")+self.title+".csv")
