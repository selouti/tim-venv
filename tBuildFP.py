import nistitl
#Update to AFIS NIST Definition
#FPS M
#Type 1 always exist
msg = nistitl.Message()
msg.TOT = 'FPS'
msg[0].VER = '0501'
msg[0].ORI = 'BE/FPS'
msg[0].TCN = '1600000366G'

# Add 1.0013 and 14
msg[0].DOM = ('EU-SISII', '1.00')
msg[0].GMT = '20250903125959Z'

#Update 2.004
r2 = nistitl.AsciiRecord(2)
msg += r2
r2 += nistitl.Field(2,3,'0100',alias='SYS')
r2 += nistitl.Field(2,4,'20250903',alias='DAR')

#Add a type 14 record
r14 = nistitl.AsciiRecord(14)
msg += r14
r14 += nistitl.Field(14,4,'BE')
r14 += nistitl.Field(14,5,'20250903')
r14 += nistitl.Field(14,13,'10')

# Generate the NIST buffer
buffer = msg.NIST

file_name = 'nist/tbuildFP.nist'

print (msg.__str__())
with open(file_name, 'wb') as binary_file:
    binary_file.write(msg.NIST)
    binary_file.close()