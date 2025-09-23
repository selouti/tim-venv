import sys
import io
import nistitl

if __name__ == '__main__':
    if len(sys.argv) != 2:
        file_name = 'nist/sample.nist'
    else:
        file_name = sys.argv[1]
# todo file_name generator (currently overwrites)

# generate NIST file
# todo values read through

print (f'Generating {file_name}')

msgCreated = nistitl.Message()
msgCreated.TOT = 'MY_TOT'

r2 = nistitl.AsciiRecord(2)
r2 += nistitl.Field(2,3,'value Timmy', alias='Tim')
msgCreated += r2

buffer = msgCreated.NIST

print (msgCreated.__str__())
with open(file_name, 'wb') as binary_file:
    binary_file.write(msgCreated.NIST)
    binary_file.close()
