import zlib

filename = '/path_to_file' 
compressed_contents = open(filename, 'rb').read() 
decompressed_contents = zlib.decompress(compressed_contents) 
print(decompressed_contents)