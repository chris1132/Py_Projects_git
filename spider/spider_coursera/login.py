import http.cookiejar as cookielib
import urllib
class Login(object):
    def pack_header(self):
        form_data=urllib.parse.urlencode({
                "refererUrl":"aHR0cDovL3d3dy4xOWxvdS5jb20=",
                "checked":0,
                "validate":"CX-aLk9jmjjHZqqpzNagBfu0ayh7xwrzH6.4f5rN9PYYwS2mv-MjwqSgWdbqz0icjEVxXTgRdK8xF.oODC1PeBqb0C0yU-9UWIYJ-iZDS4WSbDZqufW99mW.9mRzKWJL_l-1GfUnzytQI15XaRIXb-kRu1yiVnBiUD8eUvDC4gpVENZGRTn6h1_8_GFHa-h22UcKDesg.dY0Q-A40MWsn_UUkPpQnKXE-ZAb4VdTvtGtSE059uhgS_-u_FeeGRgmlDgjOMA64r7iHi1X61c2JGYf-xJjWzTXXHedCM76ddM7x9HQVBZSF5DCKaefgl26L0TeZFiekglKV1ETWD0Tw59C_dxvfXxMxHq-12v.CJG8ZJlgVTsL_50rikuNTJjP.BbUvUTQyokezlYdLwj1xlCxkcMGmmnJDPhjoCO8.ywRMdxjiDF44tF985UnknTIN.v92vMkYzYqN76H7WKvcXIacWuIV9lOOMQ8P5OWblpp8O1yZZgnBWeZEnr3",
                "businessId":"login",
                "captchaType":"Netease",
                "userName":"15757129700",
                "userPass":"aec4befe9d15d8f4cfcbdba41f5601cd",
                "remember":1,
                "ssl":"true"
        })
        header={
            "Host":"www.19lou.com", 
            "User-Agent":"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded",
            "Content-Length":709,
            "Referer":"http://www.19lou.com/login",
            "Cookie":"_DM_SID_=9240069678d15d619ffe931828301f69; _dm_tagnames=%5B%7B%22k%22%3A%22%E6%88%91%E4%B9%9F%E6%9D%A5%E4%BE%83%E4%BE%83%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22%E5%92%A8%E8%AF%A2%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22%E5%98%89%E5%85%B4%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22%E5%B7%A5%E4%BD%9C%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22%E5%9F%8E%E5%B8%82%22%2C%22c%22%3A1%7D%5D; JSESSIONID=FBDAA94D101F35D33780586AC45EAF8D; f9big=u64; _DM_S_=a712ebae87a649ae76651850767dd152; screen=879; f8big=ip53; fr_adv_last=captcha_Netease_login_0; fr_adv=; pm_count=%7B%7D; dayCount=%5B%5D; Hm_lvt_5185a335802fb72073721d2bb161cd94=1506648802; Hm_lpvt_5185a335802fb72073721d2bb161cd94=1506656484; gdxidpyhxdE=jd1uWpeoknl%2BjJDl%2BgOZYPSPPuQAEXL3eYsE8E9YCPRRtEZs8NS3SjTCHjR%2FlZ3L5UYMSrKsOAXlvJtCupYk%2Bx9VRS2I8ZZWiDOxTg80PLKaeBJ56QD0bIsjLD%2Bhl4DMiAxhIOE%2Bj17D25sb%5C3zHXZ42i2WUS%2BXM3Uc1wlI4yrPdoNe%5C%3A1506657355354; _9755xjdesxxd_=31",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":1
            }
        return form_data,header

    def simulation_login(self):
        cookie = cookielib.CookieJar()
        openr = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        urllib.request.install_opener(openr)
        form_data, request_header = self.pack_header()
        req = urllib.request.Request("http://www.19lou.com/login", data = form_data, headers = request_header)
        result = urllib.request.urlopen(req).read()
        i=1

if __name__=="__main__":
    login=Login()
    login.simulation_login()