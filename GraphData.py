from xmlControl import *
class GraphData:
    def __init__(self, page, param):
        self.Data = xmlControl.loadPageFromOpenAPI("&page="+str(page)+param)

        if self.Data == None:
            print("xml 파일을 로드할 수 없습니다")
            return None

    def getPage(self):
        return int(self.Data)