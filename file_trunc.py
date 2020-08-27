def trunc_file(in_file):
    buffer1 = []

    i = 1
    j = 1
    for line in in_file:
        if j < 12042780 :
            j = j + 1
        elif i < 1720398 :
            buffer1.append(line)
            i = i + 1
        else :
            break

    in_file.close()
    return buffer1


def write_to_file(buffer1, out_file):
    for proxy in buffer1:
        with open(out_file, "a") as res:
            res.write(str(proxy))


if __name__ == '__main__':
    print ("Running....")
    in_file = "results.txt"
    out_file = "results8.txt"
    write_to_file(trunc_file(open(in_file)), out_file)