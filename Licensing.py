import uuid
import hashlib
from datetime import datetime
from AESCrypto import PrpCrypt

# from common.aes_encrypt import get_aes
class LicenseHelper(object):

    def generate_license(self, end_date, mac_addr):
        print("Received end_date: {}, mac_addr: {}".format(end_date, mac_addr))
        psw = self.hash_msg('smartant' + str(mac_addr))
        license_str = {}
        license_str['mac'] = mac_addr
        license_str['time_str'] = end_date
        license_str['psw'] = psw
        s = str(license_str)
        # print(s)
        # licence_result = pc.encrypt(s)
        return s
        
    def get_mac_address(self):
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
        
    def hash_msg(self, msg):
        sha256 = hashlib.sha256()
        sha256.update(msg.encode('utf-8'))
        res = sha256.hexdigest()
        return res
        
    def read_license(self, license_result):
#         lic_msg = bytes(str(license_result), encoding="utf8")
#         lic_msg=license_result
        # license_str = pc.decrypt(license_result)
        license_dic = eval(license_result)
        
        return license_dic
        
    def check_license_date(self, lic_date):
        current_time = datetime.strftime(datetime.now() ,"%Y-%m-%d %H:%M:%S")
        current_time_array = datetime.strptime(current_time,"%Y-%m-%d %H:%M:%S")
        lic_date_array = datetime.strptime(lic_date, "%Y-%m-%d %H:%M:%S")
        remain_days = lic_date_array - current_time_array
        remain_days = remain_days.days
        if remain_days < 0 or remain_days == 0:
            return False
        else:
            return True
            
    def check_license_psw(self, psw):
        mac_addr = self.get_mac_address()
        hashed_msg = self.hash_msg('smartant' + str(mac_addr))
        if psw == hashed_msg:
            return True
        else:
            return False