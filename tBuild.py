import nistitl

msg = nistitl.Message()
msg.TOT = 'MY_TOT'
msg[0].TCN = 'TCN'

# --- Add a type 2 record
r2 = nistitl.AsciiRecord(2)
msg += r2
r2.IDC = 1
# Add field 2.003, long notation used to specify an alias
r2 += nistitl.Field(2,3,alias='TEST')
# Add field 2.004, with 2 subfields) using the short notation
r2._4 = ('SF1', 'SF2')

# --- Add a type 4 record
r4 = nistitl.BinaryRecord(4)
msg += r4
r4.IDC = 2
# Set all fields in one step, image and headers
r4.pack("!BBBBBBBBHHB",             # format for ANSI/NIST-ITL 1-2011: UPDATE 2015
    1,                              # impression type (rolled contact)
    1, 255, 255, 255, 255, 255,     # finger position (right thumb)
    0,                              # image scanning resolution (500 ppi)
    500, 500,                       # width & height
    1,                              # compression algo (WSQ)
    b'image')                       # the image buffer

# --- Add a type 10 record
r10 = nistitl.AsciiRecord(10)
msg += r10
r10.IDC = 3
# Used pre-defined alias
r10.SRC = 'my src'
r10.DATA = b'image'

# Generate the NIST buffer
buffer = msg.NIST

file_name = 'nist/tbuild.nist'

print (msg.__str__())
with open(file_name, 'wb') as binary_file:
    binary_file.write(msg.NIST)
    binary_file.close()