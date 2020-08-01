import json
from subprocess import Popen,PIPE

class JfrogArtifactory:
    def load_artifact(self,build):
        process = Popen(["jfrog", "rt", "s", "fw-sku-bundles-dev/firmware/sequoia/"+build+"/"], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        s = stdout.decode("utf-8")

        build_json = json.loads(s)

        # header = ['Path', 'Type', 'Size', 'Created', 'Modified', 'sha1', 'md5', 'Props']
        header = ['Path', 'Size', 'Created', 'Modified', 'sha1', 'md5']

        build_list = []
        build_list.append(header)

        for row in build_json:
            print(row)
            # build_list.append([row['path'], row['type'], row['size'], row['created'], row['modified'], row['sha1'], row['md5'], row['props']])
            build_list.append([row['path'], row['size'], row['created'], row['modified'], row['sha1'], row['md5']])

        return build_list
