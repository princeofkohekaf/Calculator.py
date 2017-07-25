import math
import cmath
import binascii


def apple():
    print "\n\nWhat you want to do?"
    print "\n(1).Add\n(2).Subtract\n(3).Multiply\n(4).Divide\n(5).root\n(6).square\n(7).Taking Power"
    print "(8).Find sin\n(9).Find tan\n(10).Find cos"
    print "(11).Find acos\n(12)Convert to ASCII"
    print "(13).Find asin\n(14).Find atan\n(15).Find PI\n(16)Find e\n(17).Find log10"
    print "(18).Find length of the vector from the origin to point (x, y)\n(19).Convert angle x into degrees"
    print "(20).Convert angle x into radians from degrees"
    print "(21).Find the complex number x with polar coordinates r and phi"
    print "(22).Find the representation of x in polar coordinates\n(23).Find the gamma function at x: "
    print "(24).Find log(x[, base])\n(25).Find  mantissa and exponent of x as the pair (m, e)"
    print "(26).Find Factorial\n(27).Find inverse of (25)\n(28).Convert hexadecimal to decimal"
    print "(29).Convert binary to decimal\n(30).Convert hexadecimal into binary"
    print "(31).Convert text to binary\n(32).Convert binary to text"
    q = raw_input("(33).Convert to GBs\n(34).Convert to MBs\n(35).Convert to TBs\n\n: ")
    if q == "Add" or q == "+" or q == "add" or q == "1":
        ask = raw_input("Enter 1st Number: ")
        again_ask = raw_input("Enter 2nd Number: ")
        asked = float(ask) + float(again_ask)
        print "\nTotal numbers in 1st input are %d" % (len(ask))
        print "\nTotal numbers in 2nd input are %d" % (len(again_ask))
        print "\nAns = %s" % asked
        q1 = raw_input("Do you want to add more: ")
        if q1 == "yes":
            again_ask_again = raw_input("Enter 1 more number: ")
            again_asked = float(asked) + float(again_ask_again)
            print "\nResult = %s" % again_asked
        else:
            print "\nResult: %s" % asked
    elif q == "Subtract" or q == "Sub" or q == "-" or q == "2":
        ask1 = raw_input("Enter 1st Number: ")
        again_ask1 = raw_input("Enter 2nd Number: ")
        asked1 = float(ask1) - float(again_ask1)
        print "\nTotal numbers in 1st number are: %d" % (len(ask1))
        print "\nTotal numbers in 2nd number are: %d" % (len(again_ask1))
        print "\nResult: %s" % asked1
    elif q == "3" or q == "Multiply" or q == "Multi" or q == "*" or q == "x":
        ask2 = raw_input("Enter 1s Number: ")
        again_ask2 = raw_input("Enter 2nd Number: ")
        asked2 = float(ask2) * float(again_ask2)
        print "\nTotal numbers in 1st Number are: %d" % (len(ask2))
        print "\nTotal numbers in 2nd Number are %d" % (len(again_ask2))
        print "\nResult: %s" % asked2
    elif q == "4" or q == "Divide" or q == "divide" or q == "div" or q == "/":
        ask3 = raw_input("Enter 1st Number: ")
        again_ask3 = raw_input("Enter 2nd Number: ")
        asked3 = float(ask3) / float(again_ask3)
        print "\nTotal numbers in 1st Number are %s" % (len(ask3))
        print "\nTotal numbers in 2nd Number are %s" % (len(again_ask3))
        print "\nResult = %s " % asked3
    elif q == "Square Root" or q == "square root" or q == "square" or q == "Square" or q == "root"or q == "5":
        ask4 = raw_input("Enter a number: ")
        asked4 = math.sqrt(float(ask4))
        print "\nresult = %s" % asked4
    elif q == "Square" or q == "square" or q == "6":
        ask6 = raw_input("Enter a Number: ")
        asked6 = float(ask6) ** 2
        print "\nTotal numbers in input are: %d" % (len(ask6))
        print "\nResult: %d" % asked6
    elif q == "Taking Power" or q == "Power" or q == "power" or q == "taking power" or q == "7":
        ask7 = raw_input("Enter a Number: ")
        again_ask7 = raw_input("Enter a Number: ")
        asked7 = float(ask7) ** float(again_ask7)
        print "\nTotal numbers in 1st number are: %d" % (len(ask7))
        print "\nTotal numbers in 2nd number are: %d" % (len(again_ask7))
        print "\nResult: %s" % asked7
    elif q == "sin" or q == "Sin" or q == "8":
        ask_apple = raw_input("Enter a value: ")
        answer_apple = cmath.sin(float(ask_apple))
        print "\nAnswer = %s" % answer_apple
    elif q == "9":
        ask_apple1 = raw_input("Enter a value: ")
        answer_apple1 = cmath.tan(float(ask_apple1))
        print "\nAnswer = %s" % answer_apple1
    elif q == "10":
        ask_apple2 = raw_input("Enter a value: ")
        answer_apple2 = cmath.cos(float(ask_apple2))
        print "\nAnswer = %s" % answer_apple2
    elif q == "11":
        ask_apple3 = raw_input("Enter a value: ")
        answer_apple3 = cmath.acos(float(ask_apple3))
        print "\nAnswer = %s" % answer_apple3
    elif q == "13":
        ask_me_apple = raw_input("Enter a value: ")
        answer_me_apple = cmath.asin(float(ask_me_apple))
        print "\nAnswer = %s" % answer_me_apple
    elif q == "14":
        hanker = raw_input("Enter a value: ")
        ans_hanker = cmath.atan(float(hanker))
        print "\nAnswer = %s" % ans_hanker
    elif q == "15":
        print "\nValue of PI = %s" % cmath.pi
    elif q == "16":
        print "\nValue of e = %s" % cmath.e
    elif q == "17":
        ask_hanker1 = raw_input("Enter a value: ")
        ans_hanker1 = cmath.log10(float(ask_hanker1))
        print "\nanswer: %s " % ans_hanker1
    elif q == "Convert" or q == "12":

        ime = raw_input("Enter your name: \n\n")
        lngth = len(ime)

        for x in range(0, lngth):
            c = ime[x]
            c = c.upper()
            if c == "A":
                print("..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
            elif c == "B":
                print("..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n\n")
            elif c == "C":
                print("..######..\n..#.......\n..#.......\n..#.......\n..######..\n\n")
            elif c == "D":
                print("..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n\n")
            elif c == "E":
                print("..######..\n..#.......\n..#####...\n..#.......\n..######..\n\n")
            elif c == "F":
                print("..######..\n..#.......\n..#####...\n..#.......\n..#.......\n\n")
            elif c == "G":
                print("..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n\n")
            elif c == "H":
                print("..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
            elif c == "I":
                print("..######..\n....##....\n....##....\n....##....\n..######..\n\n")
            elif c == "J":
                print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")
            elif c == "K":
                print("..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n\n")
            elif c == "L":
                print("..#.......\n..#.......\n..#.......\n..#.......\n..######..\n\n")
            elif c == "M":
                print("..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n\n")
            elif c == "N":
                print("..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n\n")
            elif c == "O":
                print("..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
            elif c == "P":
                print("..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n")
            elif c == "Q":
                print("..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n\n")
            elif c == "R":
                print("..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n\n")
            elif c == "S":
                print("..######..\n..#.......\n..######..\n.......#..\n..######..\n\n")
            elif c == "T":
                print("..######..\n....##....\n....##....\n....##....\n....##....\n\n")
            elif c == "U":
                print("..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
            elif c == "V":
                print("..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n\n")
            elif c == "W":
                print("..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n\n")
            elif c == "X":
                print("..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n\n")
            elif c == "Y":
                print("..#....#..\n...#..#...\n....##....\n....##....\n....##....\n\n")
            elif c == "Z":
                print("..######..\n......#...\n.....#....\n....#.....\n..######..\n\n")
            elif c == " ":
                print("..........\n..........\n..........\n..........\n\n")
            elif c == ".":
                print("----..----\n\n")
            elif c == "1":
                print("..####....\n....##....\n....##....\n....##....\n..######..\n\n")
            elif c == "2":
                print("########..\n##..##..##\n....##....\n....##..##\n....######")
    elif q == "18":
        ask_from_hanker = raw_input("Enter a value: ")
        ask_from_apple = raw_input("Enter a value: ")
        answer_from_apple = math.hypot(float(ask_from_hanker), float(ask_from_apple))
        print "\nAnswer = %s" % answer_from_apple
    elif q == "19":
        ask_to_apple = raw_input("Enter a value: ")
        ans_apple = math.degrees(float(ask_to_apple))
        print "\nAnswer in degrees = %s" % ans_apple
    elif q == "20":
        ask_to_hanker = raw_input("Enter a value: ")
        ans_from_hanker = math.degrees(float(ask_to_hanker))
        print "\nAnswer in degrees = %s" % ans_from_hanker
    elif q == "21":
        r = raw_input("Enter the value of r: ")
        phi = raw_input("Enter the value of phi: ")
        answer_from_hanker = cmath.rect(float(r), float(phi))
        print "\nAnswer = %s" % answer_from_hanker
    elif q == "22":
        z = raw_input("Enter a number: ")
        ans_x = cmath.polar(float(z))
        print "\nAnswer:"
        print ans_x
    elif q == "23":
        asked_apple = raw_input("Enter a value: ")
        answered = math.gamma(float(asked_apple))
        print "\nValue of gamma = %s" % answered
    elif q == "24":
        x = float(raw_input("Enter the value of x: "))
        base = float(raw_input("Enter the value of base: "))
        ans = math.log(x, base)
        print "\nAnswer in form x = %s" % ans
    elif q == "25":
        apples = float(raw_input("Enter a number: "))
        apples1 = math.frexp(apples)
        print "\nAns:"
        print apples1
    elif q == "26":
        applee = float(raw_input("Enter a number: "))
        appleee = math.factorial(applee)
        print "\nValue of Factorial = %d" % appleee
    elif q == "27":
        appleeee = int(raw_input("Enter a number: "))
        hankerr = int(raw_input("Enter a number: "))
        anss = math.ldexp(appleeee, hankerr)
        print "\nValue of x = %d" % anss
    elif q == "28":
        appleeeeeeee = raw_input("Enter: ")
        print
        oyeeeeeeeee = int(appleeeeeeee, 16)
        print oyeeeeeeeee
    elif q == "29":
        m = raw_input("Enter a decimal: ")
        if len(m) == 4:
            a = m[3]
            power = 0
            apple65 = int(a) * (2 ** power)
            apple1 = m[2]
            power1 = 1
            answer = int(apple1) * (2 ** power1)
            hanker = m[1]
            power2 = 2
            answer1 = int(hanker) * (2 ** power2)
            hanker1 = m[0]
            power3 = 3
            answer2 = int(hanker1) * (2 ** power3)
            last = apple65 + answer + answer1 + answer2
            print
            print "\nResult = %s" % last
        elif len(m) == 3:
            apple1 = m[2]
            power1 = 0
            answer = int(apple1) * (2 ** power1)
            hanker = m[1]
            power2 = 1
            answer1 = int(hanker) * (2 ** power2)
            hanker1 = m[0]
            power3 = 2
            answer2 = int(hanker1) * (2 ** power3)
            last = answer + answer1 + answer2
            print
            print "\nResult = %s" % last
        elif len(m) == 2:
            hanker = m[1]
            power2 = 0
            answer1 = int(hanker) * (2 ** power2)
            hanker1 = m[0]
            power3 = 1
            answer2 = int(hanker1) * (2 ** power3)
            last = answer1 + answer2
            print
            print "\nResult = %s" % last
        elif len(m) == 5:
            a1 = m[4]
            powr = 0
            aple = int(a1) * (2 ** powr)
            a = m[3]
            power = 1
            apple56 = int(a) * (2 ** power)
            apple1 = m[2]
            power1 = 2
            answer = int(apple1) * (2 ** power1)
            hanker = m[1]
            power2 = 3
            answer1 = int(hanker) * (2 ** power2)
            hanker1 = m[0]
            power3 = 4
            answer2 = int(hanker1) * (2 ** power3)
            last = aple + apple56 + answer + answer1 + answer2
            print "\nResult = %s" % last
        elif len(m) == 6:
            oyyee = m[5]
            oye = 0
            oyee = int(oyyee) * (2 ** oye)
            a1 = m[4]
            powr = 1
            aple = int(a1) * (2 ** powr)
            a = m[3]
            power = 2
            apple78 = int(a) * (2 ** power)
            apple1 = m[2]
            power1 = 3
            answer = int(apple1) * (2 ** power1)
            hanker = m[1]
            power2 = 4
            answer1 = int(hanker) * (2 ** power2)
            hanker1 = m[0]
            power3 = 5
            answer2 = int(hanker1) * (2 ** power3)
            last = oyee + aple + apple78 + answer + answer1 + answer2
            print "\nResult = %s" % last
        elif len(m) == 7:
            hii = m[6]
            hoye = 0
            hay = int(hii) * (2 ** hoye)
            oyyee = m[5]
            oye = 1
            oyee = int(oyyee) * (2 ** oye)
            a1 = m[4]
            powr = 2
            aple = int(a1) * (2 ** powr)
            a = m[3]
            power = 3
            apple78 = int(a) * (2 ** power)
            apple1 = m[2]
            power1 = 4
            answer = int(apple1) * (2 ** power1)
            hanker = m[1]
            power2 = 5
            answer1 = int(hanker) * (2 ** power2)
            hanker1 = m[0]
            power3 = 6
            answer2 = int(hanker1) * (2 ** power3)
            last = hay + oyee + aple + apple78 + answer + answer1 + answer2
            print "\nResult = %s" % last
        elif len(m) == 8:
            hiii = m[7]
            hoyee = 0
            hayye = int(hiii) * (2 ** hoyee)
            hii = m[6]
            hoye = 1
            hay = int(hii) * (2 ** hoye)
            oyyee = m[5]
            oye = 2
            oyee = int(oyyee) * (2 ** oye)
            a1 = m[4]
            powr = 3
            aple = int(a1) * (2 ** powr)
            a = m[3]
            power = 4
            apple78 = int(a) * (2 ** power)
            apple1 = m[2]
            power1 = 5
            answer = int(apple1) * (2 ** power1)
            hanker = m[1]
            power2 = 6
            answer1 = int(hanker) * (2 ** power2)
            hanker1 = m[0]
            power3 = 7
            answer2 = int(hanker1) * (2 ** power3)
            last = hayye + hay + oyee + aple + apple78 + answer + answer1 + answer2
            print "\nResult = %s" % last
        else:
            print "\nnot allowed"
    elif q == "30":
        def byte_to_binary(n):
            return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

        def hex_to_binary(h):
            return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))

        raw = raw_input()
        print "\nResult = %s" % hex_to_binary(raw)
    elif q == "32":
        staaaa = raw_input("Enter any binary numbers: ")
        hj = int(staaaa, 2)
        hbc = binascii.unhexlify('%x' % hj)
        print hbc
    elif q == "31":
        staa = raw_input("Enter any text: ")
        hbca = bin(int(binascii.hexlify(staa), 16))
        print hbca
    elif q == "33":
        rrr = raw_input("Enter you number with unit like: 2 gb : ")
        sizes = [rrr]
        defs = {'kb': 1024, 'mb': 1024 * 1024, 'gb': 1024 * 1024 * 1024, 'tb': 1024 ** 4}
        bytes1 = [float(lh) * defs[rh] for lh, rh in [e.split() for e in sizes]]
        sd = 'gb'
        applew = ['{:0.2} {}'.format(e / defs[sd], sd) for e in bytes1]
        print applew
    elif q == "34":
        rrr = raw_input("Write: ")
        sizes = [rrr]
        defs = {'kb': 1024, 'mb': 1024 * 1024, 'gb': 1024 * 1024 * 1024, 'tb': 1024 ** 4}
        bytes1 = [float(lh) * defs[rh] for lh, rh in [e.split() for e in sizes]]
        sd = 'mb'
        applew1 = ['{:0.2} {}'.format(e / defs[sd], sd) for e in bytes1]
        print applew1
    elif q == "35":
        rrr = raw_input("Write: ")
        sizes = [rrr]
        defs = {'kb': 1024, 'mb': 1024 * 1024, 'gb': 1024 * 1024 * 1024, 'tb': 1024 ** 4}
        bytes1 = [float(lh) * defs[rh] for lh, rh in [e.split() for e in sizes]]
        sd = 'tb'
        applew2 = ['{:0.2} {}'.format(e / defs[sd], sd) for e in bytes1]
        print applew2
    else:
        print "Error number not found."
apple()
print "\n\n-------------------------"
print "-------------------------"
print "Made by Prince Of Kohekaf"
print "-------------------------"
print "-------------------------"
