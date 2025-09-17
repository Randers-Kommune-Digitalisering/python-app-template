import sys
import io
import pycurl

if len(sys.argv) != 2:
    print("Usage: python ftps.py <PASSWORD>")
    sys.exit(1)

PASSWORD = sys.argv[1]

USERNAME = 'randers'
HOST = 'ftps://vps123.basicserver.io'

buffer = io.BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, HOST)
c.setopt(c.USERPWD, f'{USERNAME}:{PASSWORD}')
c.setopt(c.SSL_VERIFYPEER, 0)
c.setopt(c.SSL_VERIFYHOST, 0)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.FTP_SSL, pycurl.FTPSSL_ALL)
c.setopt(c.FTPSSLAUTH, pycurl.FTPAUTH_TLS)
c.setopt(c.FTP_USE_EPSV, 1)
c.setopt(c.DIRLISTONLY, False)
c.perform()
c.close()

listing = buffer.getvalue().decode('utf-8')
print("Listing before deletion:\n", listing)

# Delete file named 'I-bestemmer-selv-filnavnet-dato.csv' from the server
filename = 'I-bestemmer-selv-filnavnet-dato.csv'

delete_curl = pycurl.Curl()
delete_curl.setopt(delete_curl.URL, f"{HOST}/{filename}")
delete_curl.setopt(delete_curl.USERPWD, f'{USERNAME}:{PASSWORD}')
delete_curl.setopt(delete_curl.SSL_VERIFYPEER, 0)
delete_curl.setopt(delete_curl.SSL_VERIFYHOST, 0)
delete_curl.setopt(delete_curl.FTP_SSL, pycurl.FTPSSL_ALL)
delete_curl.setopt(delete_curl.FTPSSLAUTH, pycurl.FTPAUTH_TLS)
delete_curl.setopt(delete_curl.FTP_USE_EPSV, 1)
delete_curl.setopt(delete_curl.QUOTE, [f"DELE {filename}"])
delete_curl.perform()
delete_curl.close()

print(f"Deleted {filename} from {HOST}")

# List files again to confirm deletion
buffer_after = io.BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, HOST)
c.setopt(c.USERPWD, f'{USERNAME}:{PASSWORD}')
c.setopt(c.SSL_VERIFYPEER, 0)
c.setopt(c.SSL_VERIFYHOST, 0)
c.setopt(c.WRITEDATA, buffer_after)
c.setopt(c.FTP_SSL, pycurl.FTPSSL_ALL)
c.setopt(c.FTPSSLAUTH, pycurl.FTPAUTH_TLS)
c.setopt(c.FTP_USE_EPSV, 1)
c.setopt(c.DIRLISTONLY, False)
c.perform()
c.close()

listing_after = buffer_after.getvalue().decode('utf-8')
print("Listing after deletion:\n", listing_after)
