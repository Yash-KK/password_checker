import hashlib
import requests
import sys

def return_api_data(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error Fetching: {res.status_code}, check API and try again.")
    else:
        return res

def get_password_count_leaks(hashes,hash_to_check):    #responses,tail of the password hash
     hashes = (item.split(":") for item in hashes.text.splitlines())
     for h,count in hashes:
        if h == hash_to_check:
            return count
     return 0   



def password_encoder(password):
    shah1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_char, tail = shah1password[0:5], shah1password[5:]
    response = return_api_data(first_char)
    
    return get_password_count_leaks(response,tail)







def main(args):
    for password in args:
        count = password_encoder(password)
        if count:
            print(f"{password} has been found {count} times")
        else:
            print(f"{password} has not found!")    
    
sys.exit(main(sys.argv[1:]))