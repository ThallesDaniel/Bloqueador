import os

class FirewallService:
    @staticmethod
    def block_ip(ip_address):
        os.system(f"netsh advfirewall firewall add rule name=\"Block {ip_address}\" dir=out action=block remoteip={ip_address}")
    
    @staticmethod
    def unblock_ip(ip_address):
        os.system(f"netsh advfirewall firewall delete rule name=\"Block {ip_address}\"")
