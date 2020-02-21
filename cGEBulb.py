import requests

#When the API should timeout 
API_TIMEOUT = 5

def authenticate(username,password):
    """
    Will return the access token and the user_id

    take the user credientials and throw them to the website

    """

    #The website we need to get the data from 
    API_AUTH = "https://api2.xlink.cn/v2/user_auth"
    #to get the information we must send it as a jason file
    auth_data = {'corp_id': "1007d2ad150c4000", 'email': username,
                 'password': password}
    #This will actually return the authenticaion Data and user_ID
    r = requests.post(API_AUTH, json=auth_data, timeout=API_TIMEOUT)
    try:
        return (r.json()['access_token'], r.json()['user_id'])
    except KeyError:
        raise('API authentication failed')


def get_devices(auth_token,user):
    """ 
    auth_Token - user's authetication Token
    user - the user's Id
    this will return the items the user owns
    """
    #this is the website 
    API_DEVICES = "https://api2.xlink.cn/v2/user/{user}/subscribe/devices"
    #This is the header which tells the sever how to access the date the user wants from the sever
    headers = {'Access-Token':auth_token}
    #------I AM NOT SURE WHY WE ONLY NEED THE ACCESS TOKEN AND NOT THE  Corp-ID,Api-Version,Content-Type-------???
    r = requests.get(API_DEVICES.format(user=user), headers = headers, timeout= API_TIMEOUT)

    return r.json()




def get_properties(auth_token, product_id, device_id):
    """Get properties for a single device."""
    
    API_DEVICE_INFO = "https://api2.xlink.cn/v2/product/{product_id}/device/{device_id}/property"
    headers = {'Access-Token': auth_token}
    r = requests.get(API_DEVICE_INFO.format(product_id=product_id, device_id=device_id), headers=headers, timeout=API_TIMEOUT)
    return r.json()





print("--------testing-----------------")
access_Token,userId = authenticate("joandjest@gmail.com","Bocadetrapo41@")

b = get_devices(access_Token,userId)

product_idd = b[0]['product_id']
other_idd = b[0]['id']

proterties = get_properties(access_Token,product_idd,other_idd)

print(proterties)



print("-----------------testing--------------------")
print("Made it")