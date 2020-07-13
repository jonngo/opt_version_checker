import json
from subprocess import Popen,PIPE
from texttable import Texttable


def display_table(content):
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t','t','i','t','t','t','t','t'])  # text
    table.set_cols_width([80, 8,10,25,25,40,35,300])

    table.set_cols_align(["l","l","l", "l","l", "l","l", "l"])
    table.add_rows(content)
    print(table.draw())


process = Popen(["jfrog" ,"rt" ,"s","fw-sku-bundles-dev/firmware/sequoia/02.03.0010/"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
s = stdout.decode("utf-8")

b = json.loads(s)

header = ['path','type','size','created','modified','sha1','md5','props']

m = []
m.append(header)

for a in b:
    print(a)
    m.append([a['path'],a['type'],a['size'],a['created'],a['modified'],a['sha1'],a['md5'],a['props']])

display_table(m)

