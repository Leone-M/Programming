def main():
    psbl_code = str(input())    # изначальный код

    numpad = {"1": ["1", "2", "4"], "2": ["1", "2", "3", "5"], "3": ["2", "3", "6"], "4": ["1", "4", "5", "7"],
              "5": ["2", "4", "5", "6", "8"], "6": ["3", "5", "6", "9"], "7": ["4", "7", "8"],
              "8": ["5", "7", "8", "9", "0"], "9": ["6", "8", "9"]}

    def get_pins(code, numpad):
        perm = []
        buf = []
        sub_code = ""

        if len(code) == 1:
            return numpad[code]

        j = 0
        for e in code:
            buf.append([])
            for i in range(len(numpad[e])):
                buf[j].append(numpad[e][i])
            j += 1





        return buf

    print(get_pins(psbl_code, numpad))


if __name__ == "__main__":
    main()