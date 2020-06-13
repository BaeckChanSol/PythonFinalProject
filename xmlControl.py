# -*- coding:utf-8 -*-
import os
import sys
import http.client

from xml.etree import ElementTree
# 사용법 (20.05.26 작성)
# loadXmlFromOpenAPI에 params를 넘겨준다. 이 함수의 리턴값을 받는다.
# params는 예시를 사용하여 요청변수 page를 활용한다 했을때
# "&page=10" : 10번째 페이지 조회
# 와 같은 방식으로 한다.
# 여러 개의 인자를 넘길 때에는
# "&page=10&sexdstnDscd=여" 와 같은 방식으로 보내준다.
# id, key, rowSize, xmlUseYn은 함수 내부에 정의되어있음으로 param에 추가할 필요 없다.
# 함수의 리턴값은 [{데이터1}, {데이터 2}, ...] 이런 방식으로 되어있다.
# 해당 리턴값을 BigData라 할 때
# for data in BigData로 루프를 돌면서
#str(data["name"].text) : 이름
#str(data["gender"].text) : 성별
#str(data["age"].text) : 당시 나이
#str(data["ageNow"].text) : 현재 나이
#str(data["dressing"].text) : 당시 옷차림
#str(data["occrde"].text) : 발생 시간
#str(data["occradres"].text) : 발생 장소
#str(data["etc"].text) : 기타 정보
#로 각 정보에 접근할 수 있다.
# 기타 정보 숫자로 되어있으며 구분은 다음과 같이 한다.
# 010 : 정상아동 (18세 미만)
# 020 : 가출인
# 040 : 시설보호무연고자
# 060 : 지적장애인
# 061 : 지적장애인(18세미만)
# 062 : 지적장애인(18세이상)
# 070 : 치매질환자
# 080 : 불상(기타)


class xmlControl:
    def loadXmlFromOpenAPI(params):
        client_id = "10000335"
        client_secret = ""
        conn = http.client.HTTPConnection("safe182.go.kr")
        #conn.set_debuglevel(1) #debug mode �¦ㅼ��
        #headers = {"esntlId": client_id, "authKey": client_secret, "rowSize":"8"}
        headers ={}
        finalparams = "?esntlId=" + client_id +"&authKey="+client_secret+"&rowSize=8"+"&xmlUseYN=Y" + params
        conn.request("POST", "/api/lcm/findChildList.do" + finalparams, None, headers)
        res = conn.getresponse()
        if int(res.status) == 200 :
            print("xml data downloading is complete!")
            return xmlControl.extractData(res.read())
        else:
            print ("HTTP Request is failed :" + res.reason)
            print (res.read().decode('utf-8'))
            return None
        conn.close()


    def extractData(strXml):
        tree = ElementTree.fromstring(strXml)
        itemElements = tree.iter("item")
        data = []
        for item in itemElements:
            name = item.find("nm")
            gender = item.find("sexdstnDscd")
            occrAdres = item.find("occrAdres")
            writngTrgetDscd = item.find("writngTrgetDscd")
            age = item.find("age")
            ageNow = item.find("ageNow")
            dressing = item.find("alldressingDscd")
            occrde = item.find("occrde")
            photo = item.find("tknphotoFile")
            data.append({"name":str(name.text), "gender":str(gender.text), "age":str(age.text), "ageNow":str(ageNow.text), \
                         "dressing":str(dressing.text), "occrde":str(occrde.text), "occrAdres":str(occrAdres.text)\
                            , "etc":str(writngTrgetDscd.text), "photo":str(photo.text)})
        return data


    def test(params):
        datas = xmlControl.loadXmlFromOpenAPI(params)
        for data in datas:
            print("name " +data["name"])
            print("gender " + data["gender"])
            print("age " + data["age"])
            print("ageNow " + data["ageNow"])
            print("dressing " +data["dressing"])
            print("occrde " + data["occrde"])
            print("occrAdres " + data["occrAdres"])
            print("etc " + data["etc"])
            print("=====================================")

xmlControl