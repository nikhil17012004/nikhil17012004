from neo_api_client import NeoAPI
def on_message(message):
    print(message)

def on_error(error_message):
    print(error_message)

client = NeoAPI(consumer_key="ZMJFeKOV9zLgAid_jRD_0yzgfo4a", consumer_secret="lB0qWRDYf6MB08kYGqsXfxM39i4a",
                environment='prod', on_message=on_message, on_error=on_error, on_close=None, on_open=None)

client.login(mobilenumber="+917666924366", password="@Msarode6291")

client.session_2fa(OTP="4836")

client.scrip_master()