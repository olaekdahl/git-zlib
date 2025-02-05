# https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
# Git first constructs a header which starts by identifying 
# the type of object — in this case, a blob. To that first 
# part of the header, Git adds a space followed by the size in 
# bytes of the content, and adding a final null byte.

# Git concatenates the header and the original content and then 
# calculates the SHA-1 checksum of that new content.


# Code source: https://stackoverflow.com/questions/70944136/decompressing-git-objects-with-zlib
import zlib

filename = '/home/ola/git-demo/.git/objects/9e/68dfd99058b4be4748809b3229e371c1cbb927' 
compressed_contents = open(filename, 'rb').read() 
decompressed_contents = zlib.decompress(compressed_contents) 
print(decompressed_contents)