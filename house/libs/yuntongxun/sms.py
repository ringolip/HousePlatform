# -*- coding:utf-8 -*-  

from CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid= '8a216da86772f10d016786a9e6581313'

# ���ʺ�Token
accountToken= 'f752d4ae6f554d9e8c515807ad2e221a'

# Ӧ��Id
appId='8a216da86772f10d016786a9e6b1131a'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com'

# ����˿� 
serverPort='8883'

# REST�汾��
softVersion='2013-12-26'

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

class CCP(object):
    """�Լ���װ���Ͷ��ŵĸ�����"""
    def __init__(self):
        #��ʼ��REST SDK
        self.rest = REST(serverIP,serverPort,softVersion)
        self.rest.setAccount(accountSid,accountToken)
        self.rest.setAppId(appId)

    def send_template_sms(self,to,datas,tempId):
        # sendTemplateSMS(�ֻ�����,��������,ģ��Id)
        result = self.rest.sendTemplateSMS(to,datas,tempId)

        # ���ض���״̬��
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

    
#     #��ʼ��REST SDK
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
    
   
# #sendTemplateSMS(�ֻ�����,��������,ģ��Id)