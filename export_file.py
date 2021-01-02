class ExportToFile:
    def __init__(self, path, file_format, content):
        self.path = path
        self.format = file_format
        self.content = content

    def export(self):
        #TODO work on the logic below
        #Logic of exporting the content in format to path
        print("\nExport in " + self.format + " format to " + self.path+"\n")
        for row in self.content:
            print(row)
