with open('kid.png', 'rb') as rf:
    with open('kid_copy.png', 'wb') as wf:
        chunk_size = 4
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

    
    # size = 10
    # f_contents = f.read(size)
    # print(f_contents, end="")

    # f.seek(0)

    # f_contents = f.read(size)
    # print(f_contents)
    # while len(f_contents)>0:
    #     print(f_contents, end="@")
    #     f_contents = f.read(size)
    # print(f.tell())

    

    # for line in f:
    #     print(line, end="")

