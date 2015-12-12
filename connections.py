import socket


ipList = socket.gethostbyname_ex(socket.gethostname())

'''
�ж�IP��ַ�Ƿ�����Ч��IPv4��ַ
'''
def is_valid_ipv4_address(address):
    try:
        addr= socket.inet_pton(socket.AF_INET, address)
    except AttributeError: # no inet_pton here, sorry
        try:
            addr= socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error: # not a valid address
        return False
    return True

'''
�ж�IP��ַ�Ƿ�����Ч��IPv6��ַ
'''
def is_valid_ipv6_address(address):
    try:
        addr= socket.inet_pton(socket.AF_INET6, address)
    except socket.error: # not a valid address
        return False
    return True

print str(ipList[2][0])

