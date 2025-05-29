import tarfile
import json
import requests

def getEnt(path, entType="json"):
    with tarfile.open(path, 'r') as tar:
        for member in tar.getmembers():
            if member.name.endswith('project.json'):
                f = tar.extractfile(member)
                data = f.read().decode('utf-8')
                if entType == "json":
                    data = json.loads(data)
                return data
    raise FileNotFoundError("올바른 엔트리 파일 형식이 아닙니다.")

def getImage(path):
    return requests.get(path).content

if __name__ == "__main__":
    print(getImage("https://playentry.org/lib/entry-js/images/media/entrybot1.svg"))