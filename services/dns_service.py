import os

class DNSService:
    HOSTS_PATH = "/etc/hosts" if os.name != 'nt' else r"C:\Windows\System32\drivers\etc\hosts"
    
    @staticmethod
    def block_site(url):
        with open(DNSService.HOSTS_PATH, "a") as hosts_file:
            hosts_file.write(f"127.0.0.1 {url}\n")
    
    @staticmethod
    def unblock_site(url):
        with open(DNSService.HOSTS_PATH, "r") as hosts_file:
            lines = hosts_file.readlines()
        with open(DNSService.HOSTS_PATH, "w") as hosts_file:
            for line in lines:
                if url not in line:
                    hosts_file.write(line)
