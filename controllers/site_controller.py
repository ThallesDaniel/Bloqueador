from db.connection import MongoDBConnection
from services.firewall_service import FirewallService
from services.dns_service import DNSService

class SiteController:
    def __init__(self):
        self.db = MongoDBConnection().get_collection("blocked_sites")
    
    def add_site(self, site_url):
        self.db.insert_one({"url": site_url})
        DNSService.block_site(site_url)
    
    def remove_site(self, site_url):
        self.db.delete_one({"url": site_url})
        DNSService.unblock_site(site_url)
    
    def get_all_sites(self):
        return list(self.db.find())
    
    def block_site(self, site_url):
        site = self.db.find_one({"url": site_url})
        if site:
            FirewallService.block_ip(site.get("ip"))
            DNSService.block_site(site_url)
    
    def unblock_site(self, site_url):
        FirewallService.unblock_ip(site_url)
        DNSService.unblock_site(site_url)
