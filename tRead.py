import sys
import io
import nistitl

# read .nist file

if __name__ == '__main__':
    if len(sys.argv) != 2:
        file_name = 'nist/sample.nist'
    else:
        file_name = sys.argv[1]

    print('Reading ' + file_name)

    msgParsed = nistitl.Message()

    with io.open(file_name, 'rb') as binary_file:
        msgParsed.parse(binary_file.read())
        binary_file.close()

    # print less
    print(msgParsed.TOT)
    for record in msgParsed.iter(2):
        print("Field 2.003 is ",record._3)

    # print everything
    print(msgParsed.__str__())