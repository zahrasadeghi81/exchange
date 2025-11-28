from config import KAVENEGAR_API_KEY , rules
from kavenegar import *

def send_sms(msg):
    try:
        api = KavenegarAPI(KAVENEGAR_API_KEY)
        params = {  
            'sender': '',#optional
            'receptor': rules['notification']['receiver'] ,
            'message': msg,
        } 
        response = api.sms_send(params)
        print(str(response))
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)