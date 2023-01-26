from .. import loader, utils
def register(cb):
	cb(NeofetchMod())
class NeofetchMod(loader.Module):
	"""neofetch"""
	strings = {'name': 'neofetch'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def neocmd(self, message):
		"""neofetch"""
		await message.edit("""<code>
vadymyem@AuthorChe`s
------------------- 
OS: Ubuntu 20.04.5 LTS aarch64 
Host: KVM Virtual Machine virt-4.2 
Kernel: 5.15.0-1027-oracle 
Uptime: 3 days, 18 hours, 57 mins 
Packages: 1378 (dpkg), 7 (snap) 
Shell: bash 5.0.17 
Resolution: 1024x768 
CPU: (4) 
GPU: 00:01.0 Red Hat, Inc. Virtio GPU 
Memory: 8040MiB / 23988MiB</code>
""")


		