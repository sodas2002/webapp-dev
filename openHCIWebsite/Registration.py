# -*- coding: utf-8 -*-
import os
import datetime

from google.appengine.dist import use_library
use_library("django", "1.2")
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from Constants import debugMode

class RegistrationPage(webapp.RequestHandler):
    def get(self):
        pageContent = {"false": False,
                       "namelist": [{"name": "管哲楓", "dept": "台科大工設商設系"},
                                    {"name": "黃莉婷", "dept": "台大資工所"},
                                    {"name": "牟偉豪", "dept": "台大資工所"},
                                    {"name": "鄭群萌", "dept": "台科大工設商設系"},
                                    {"name": "甘泰瑋", "dept": "台大網媒所"},
                                    {"name": "郭冠宏", "dept": "台大資工系"},
                                    {"name": "李依書", "dept": "台大資工所"},
                                    {"name": "高新綠", "dept": "台大網媒所"},
                                    {"name": "蕭方儀", "dept": "台大資工系"},
                                    {"name": "林自均", "dept": "台大資工系"},
                                    {"name": "黃凱蘭", "dept": "台科大工設所"},
                                    {"name": "林書漾", "dept": "台大網媒所"},
                                    {"name": "何柏樟", "dept": "台大資工系"},
                                    {"name": "李奎翰", "dept": "台大資工所"},
                                    {"name": "林君轂", "dept": "台大資工系"},
                                    {"name": "黃新雅", "dept": "台科大工設所"},
                                    {"name": "林逸辰", "dept": "台大Global MBA"},
                                    {"name": "邱鈴媛", "dept": "台科大工設所"},
                                    {"name": "張明芳", "dept": "台大電機所自動控制組"},
                                    {"name": "林韻嘉", "dept": "台科大工設所", "break": True},
                                    {"name": "林君達", "dept": "台大資工所"},
                                    {"name": "林宏祥", "dept": "台大網媒所"},
                                    {"name": "菲爾德", "dept": "台大電機所 (CS組)"},
                                    {"name": "丁建文", "dept": "台大資工所"},
                                    {"name": "江欣倩", "dept": "台大資工所"},
                                    {"name": "林玉芯", "dept": "台大資管所"},
                                    {"name": "李良一", "dept": "中央資工系"},
                                    {"name": "楊勝傑", "dept": "台大資工博士班"},
                                    {"name": "高鈞雅", "dept": "台科大工設商設系"},
                                    {"name": "何信億", "dept": "台大資工所"},
                                    {"name": "余士元", "dept": "台大資工系"},
                                    {"name": "潘柔", "dept": "成大心理系"},
                                    {"name": "吳義誠", "dept": "台科大工設所"},
                                    {"name": "蔡孟璇", "dept": "台大心理系"},
                                    {"name": "廖英棋", "dept": "台大心理系"},
                                    {"name": "朱庭萱", "dept": "台大心理系"},
                                    {"name": "林宇軒", "dept": "台大工程科學及海洋工程學系"},
                                    {"name": "許婷婷", "dept": "台科大工設商設系"},
                                    {"name": "黃聿凱", "dept": "台大電子所 (EDA)"},
                                    {"name": "林冠宇", "dept": "台大資工所", "break": True},
                                    {"name": "許宏賓", "dept": "交大建築所"},
                                    {"name": "林憲駿", "dept": "師大資工所"},
                                    {"name": "駱豊儒", "dept": "台科大資設所"},
                                    {"name": "黃瀞瑩", "dept": "台大圖資所"},
                                    {"name": "許嘉妤", "dept": "交大網工所"},
                                    {"name": "范惠婷", "dept": "世新大學傳播管理所"},
                                    {"name": "林佑達", "dept": "Harvard Graduate School of Design"},
                                    {"name": "鄭明郡", "dept": "台中教育大學數位內容所"},
                                    {"name": "陳亭汝", "dept": "台大資工系"},
                                    {"name": "洪毅軍", "dept": "台科大工設商設系"},
                                    {"name": "施宛妤", "dept": "台科大工設商設系"},
                                    {"name": "崔恩銓", "dept": "台科大工設所"},
                                    {"name": "林岑縈", "dept": "台科大工設所"},
                                    {"name": "陳泳勳", "dept": "台科大工設所"},
                                    {"name": "李昀臻", "dept": "師大物理所"},
                                    {"name": "顏新晨", "dept": "台大電子所"}
                                    ],
                        "sublist": [{"name": "羅尹聰", "dept": "清大資工碩士班"},
                                    {"name": "張明旭", "dept": "台大網媒所"}],
                        "teamList":[{"leader": {"name": "蔡雙伃", "dept": "台科大工設所"},
                                     "member": [{"name": "林自均", "dept": "台大資工系"},
                                                {"name": "林書漾", "dept": "台大網媒所"},
                                                {"name": "高新綠", "dept": "台大網媒所"},
                                                {"name": "廖英棋", "dept": "台大心理系"},
                                                {"name": "李昀臻", "dept": "師大物理所畢"},
                                                {"name": "許宏賓", "dept": "交大建築所"}]},
                                    {"leader": {"name": "黃怡靜", "dept": "台大網媒所"},
                                     "member": [{"name": "郭冠宏", "dept": "台大資工系"},
                                                {"name": "菲爾德", "dept": "台大電機所 (CS組)"},
                                                {"name": "何信億", "dept": "台大資工所"},
                                                {"name": "邱鈴媛", "dept": "台科大工設所"},
                                                {"name": "林逸辰", "dept": "台大Global MBA"},
                                                {"name": "范惠婷", "dept": "世新傳播管理所"}]},
                                    {"leader": {"name": "蕭喬尹", "dept": "台大資工所"},
                                     "member": [{"name": "張明旭", "dept": "台大網媒所"},
                                                {"name": "林玉芯", "dept": "台大資管所"},
                                                {"name": "林岑縈", "dept": "台科大工設所"},
                                                {"name": "黃聿凱", "dept": "台大電子所(EDA)"},
                                                {"name": "施宛妤", "dept": "台科大工設商設系"}]},
                                    {"leader": {"name": "黃大源", "dept": "台大網媒所"},
                                     "member": [{"name": "陳亭汝", "dept": "台大資工系"},
                                                {"name": "楊勝傑", "dept": "台大資工所"},
                                                {"name": "林冠宇", "dept": "台大資工所"},
                                                {"name": "蔡孟璇", "dept": "台大心理系"},
                                                {"name": "林韻嘉", "dept": "台科大工設所"},
                                                {"name": "鄭群萌", "dept": "台科大工設商設系"}]}, 
                                    {"leader": {"name": "蔡典哲", "dept": "台大網媒所"},
                                     "member": [{"name": "林憲駿", "dept": "師大資工所"},
                                                {"name": "余士元", "dept": "台大資工系"},
                                                {"name": "高鈞雅", "dept": "台科大工設商設系"},
                                                {"name": "黃瀞瑩", "dept": "台大圖資所"},
                                                {"name": "崔恩銓", "dept": "台科大工設所"},
                                                {"name": "江欣倩", "dept": "台大資工所"}]},
                                    {"leader": {"name": "蘇兆懷", "dept": "台大資管所"},
                                     "member": [{"name": "林君轂", "dept": "台大資工系"},
                                                {"name": "李良一", "dept": "中央資工系"},
                                                {"name": "許婷婷", "dept": "台科大工設所"},
                                                {"name": "駱豊儒", "dept": "台科大資設所"},
                                                {"name": "丁建文", "dept": "台大資工所"}]},
                                    {"leader": {"name": "李泓其", "dept": "台大資工所"},
                                     "member": [{"name": "蕭方儀", "dept": "台大資工系"},
                                                {"name": "林宏祥", "dept": "台大網媒所"},
                                                {"name": "吳義誠", "dept": "台科大工設所"},
                                                {"name": "陳泳勳", "dept": "台科大工設所"},
                                                {"name": "黃莉婷", "dept": "台大資工所"}]},
                                    {"leader": {"name": "何宇傑", "dept": "台大資工所"},
                                     "member": [{"name": "何柏樟", "dept": "台大資工系"},
                                                {"name": "林宇軒", "dept": "台大工科海洋所"},
                                                {"name": "黃凱蘭", "dept": "台科大工設所"},
                                                {"name": "朱庭萱", "dept": "台大心理系"},
                                                {"name": "鄭明郡", "dept": "中教大數位內容所"},
                                                {"name": "林君達", "dept": "台大資工所"}]},
                                   ]
                       }
        pagePath = os.path.join(os.path.dirname(__file__), "html/registration.html")
        self.response.out.write(template.render(pagePath, pageContent))
    
application = webapp.WSGIApplication([('/registration/', RegistrationPage)], debug=debugMode)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()

