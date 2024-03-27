import requests

def sms(numero_telefono, mensaje):
    url = "https://api-sms.masivapp.com/send-message"
    payload = {
        "to": numero_telefono,
        "text": mensaje,
        "customData": "CUST_ID_0125",
        "isPremium": False,
        "isFlash": False,
        "isLongMessage": False,
        "isRandomRoute": False
    }
    auth = ("asd_iq_sena_api_15350", "LneCrvLKUlWsKqbRLs37.Z2UKk1KRN")
    
    try:
        response = requests.post(url, json=payload, auth=auth)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al enviar el SMS: {str(e)}")
        return False

# Define la función send_sms si aún no está definida
def send_sms(numero_telefono, mensaje):
    # Lógica para enviar el SMS
    pass