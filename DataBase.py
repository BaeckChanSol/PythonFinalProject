from xmlControl import *
class DataBase:
    def __init__(self, page, param):
        self.Data = xmlControl.loadXmlFromOpenAPI("&page="+str(page)+param)
        if self.Data == None:
            print("xml 파일을 로드할 수 없습니다")
            return None

    def toStringData(self, num):
        if(len(self.Data) <= num):
            return None
        stringTmp = ["이름 : " + self.Data[num]["name"] , "성 : " + self.Data[num]["gender"] , \
                      "나이 : " + self.Data[num]["age"] + "->" + self.Data[num]["ageNow"]\
                      ,"지역: "+ self.Data[num]["occrAdres"]]
        return stringTmp

    def getData(self, num):
        return self.Data[num]