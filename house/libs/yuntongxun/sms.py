# -*- coding:utf-8 -*-  

from CCPRestSDK import REST
import ConfigParser

# 主帐号
accountSid= '8a216da86772f10d016786a9e6581313'

# 主帐号Token
accountToken= 'f752d4ae6f554d9e8c515807ad2e221a'

# 应用Id
appId='8a216da86772f10d016786a9e6b1131a'

# 请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com'

# 请求端口 
serverPort='8883'

# REST版本号
softVersion='2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id

class CCP(object):
    """自己封装发送短信的辅助类"""
    def __init__(self):
        #初始化REST SDK
        self.rest = REST(serverIP,serverPort,softVersion)
        self.rest.setAccount(accountSid,accountToken)
        self.rest.setAppId(appId)

    def send_template_sms(self,to,datas,tempId):
        # sendTemplateSMS(手机号码,内容数据,模板Id)
        result = self.rest.sendTemplateSMS(to,datas,tempId)

        # 返回短信状态码
        sms_status_code = result.get("statusCode")
        if sms_status_code == "000000":
            return 0
        else:
            return 1
        # for k,v in result.iteritems(): 
        #     if k=='templateSMS' :
        #             for k,s in v.iteritems(): 
        #                 print '%s:%s' % (k, s)
        #     else:
        #         print '%s:%s' % (k, v)

if __name__ == "__main__":
    ccp = CCP()
    ret = ccp.send_template_sms("18817568257", ["9527", "1"], "1")
    print(ret)

# def sendTemplateSMS(to,datas,tempId):

    
#     #初始化REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
    
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems(): 
        
#         if k=='templateSMS' :
#                 for k,s in v.iteritems(): 
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
    
   
# #sendTemplateSMS(手机号码,内容数据,模板Id)