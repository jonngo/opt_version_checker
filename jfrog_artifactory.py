import json
from subprocess import Popen,PIPE

class JfrogArtifactory:
    def __init__(self,path):
        self.path = path
        self.load_all()

    def load_all(self):
        process = Popen(["jfrog", "rt", "s", self.path], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        self.all_repo_info = json.loads(stdout.decode("utf-8"))

    def unique_build_number(self):
        try:
            build_num = []
            for row in self.all_repo_info:
                build_num.append(row['props']['build.number'][0])
            return list(set(build_num))
        except Exception as e:
            return []

    def filter_artifact(self, build_num):
        content = []

        for row in self.all_repo_info:
            if row['props']['build.number'][0] == build_num:
                content.append([row['path'], row['type'], row['size'], row['created'], row['modified'], row['sha1'], row['md5'], row['props']])

        content.sort()
        content.insert(0, ['Path', 'Type', 'Size', 'Created', 'Modified', 'SHA1', 'MD5', 'Props'])
        return content

# if __name__ == "__main__":
#     jfrog_art = JfrogArtifactory('fw-sku-release-dev/firmware/sequoia/')
#     # result_of_jfrog_list = jfrog_art.load_artifact('02.01.0058.0')
#     print (jfrog_art.unique_build_number())
