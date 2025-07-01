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
print("Listing before upload:\n", listing)

# Upload a file named 'I-bestemmer-selv-filnavnet-dato.csv' to the server
upload_filename = 'I-bestemmer-selv-filnavnet-dato.csv'

with open(upload_filename, 'rb') as f:
    upload_curl = pycurl.Curl()
    upload_curl.setopt(upload_curl.URL, f"{HOST}/{upload_filename}")
    upload_curl.setopt(upload_curl.USERPWD, f'{USERNAME}:{PASSWORD}')
    upload_curl.setopt(upload_curl.SSL_VERIFYPEER, 0)
    upload_curl.setopt(upload_curl.SSL_VERIFYHOST, 0)
    upload_curl.setopt(upload_curl.UPLOAD, 1)
    upload_curl.setopt(upload_curl.READDATA, f)
    upload_curl.setopt(upload_curl.FTP_SSL, pycurl.FTPSSL_ALL)
    upload_curl.setopt(upload_curl.FTPSSLAUTH, pycurl.FTPAUTH_TLS)
    upload_curl.setopt(upload_curl.FTP_USE_EPSV, 1)
    upload_curl.perform()
    upload_curl.close()

print(f"Uploaded {upload_filename} to {HOST}")

# List files again to confirm upload
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
print("Listing after upload:\n", listing_after)
