# import binascii
#
#
# def read_byte(file_name):
#     with open(file_name, 'rb') as f:
#         content = f.read()
#         str_content = binascii.hexlify(content)
#         for start in range(len(str_content)//2):
#             end = start + 2
#             print(str_content[start:end], end=' ')
#             start = end
import pefile


def convert(file_name):
    pe = pefile.PE(file_name)
    print(pe)