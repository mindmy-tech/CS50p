file_name = input("file name :").lower().strip().split('.')
types = {
"gif" : "image/gif",
"jpg" : "image/jpeg",
"jpeg" : "image/jpeg",
"png" : "image/png",
"pdf" : "application/pdf",
"txt" : "text/plain",
"zip" : "application/zip",
}
if file_name[len(file_name) -1 ] in types:
    print(types[file_name[len(file_name) -1 ]])
else:
    print("application/octet-stream")