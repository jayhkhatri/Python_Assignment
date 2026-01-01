"""
we have the following dictionary contains details:


user = {
    'username': 'my_user',
    'password': 'Test@123',
    'email': 'my_user@example.com',
    'address': 'ABC road, 1111',
    'country': 'Australia'
}


delete sensitive_info = ['password','address','phone]
"""
user = {
    'username': 'my_user',
    'password': 'Test@123',
    'email': 'my_user@example.com',
    'address': 'ABC road, 1111',
    'country': 'Australia'
}

sensitive_info = ['password','address','phone']

for key in sensitive_info:
    if key in user:
        print(key, user[key])
        user.pop(key)
    else:
        print(f"{key} is not present in user")


print(user)