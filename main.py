import math


def data_introduction():
    """
    citeste o lista
    :return: returneaza lista citita
    """
    lst = []
    givenstring = input("Introduceti lista de numebere insiruite prin virgula: ")
    numersasstring = givenstring.split(",")  # pune in numersasstrings toate numere din given string fara virugla
    for x in numersasstring:
        lst.append(int(x))
    return lst


def is_prime(number):
    """
    returneaza daca number este prim sau nu
    :param number: nr intreg
    :return: daca true dace number este prim , false in caz contrar
    """
    divizors = 2
    if number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            divizors = divizors + 1
    if divizors == 2:
        return True
    return False


def numbar_reversal(number):
    """
    face inversul unui numar
    :param number: nr intreg
    :return: inversului lui number
    """
    newnumber = 0
    while number:
        newnumber = newnumber * 10 + number % 10
        number = number // 10
    return newnumber


def get_longest_concat_is_prime(lst):
    """
    calculeaza si returneaza cel mai lung subsir cu proprietatea ca toate concatenarea numerelor este numar prim
    :param lst: lista de numere intregi
    :return: returneaza lista maxima cu proprietatea de mai sus
    """
    concatnumber = 0
    position = -1
    lstmaxim = []
    finalposition = 0
    maxim = 0
    nr = 0
    for i in range(len(lst)):
        copyoflst = numbar_reversal(lst[i])
        while copyoflst:
            concatnumber = concatnumber * 10 + copyoflst % 10
            copyoflst = copyoflst // 10
        if is_prime(concatnumber):
            nr = nr + 1
        else:
            if nr > maxim:
                maxim = nr
                finalposition = position
            position = i
            nr = 0
            concatnumber = 0
    for i in range(finalposition + 1, finalposition + maxim + 1):
        lstmaxim.append(lst[i])
    return lstmaxim


def is_perfect_square(number):
    """
    verifica daca number este patrat perfect
    :param number:
    :return:
    """
    if int(math.sqrt(number)) * (math.sqrt(number)) == number:
        return True
    else:
        return False


def get_longest_all_perfect_squares(lst):
    """
    calculeaza si returneaza subsirul maxim cu proprietatea ca toate numberele sunt patrate perfecte
    :param lst: lista de numbere intregi
    :return: lista maxima cu proprietatea de mai sus
    """
    position = -1  # incepe de la -1 altfel nu merge pe cazul cand primul numar este pp
    finalposition = 0
    maxim = 0
    lstmaxim = []
    nr = 0
    for i in range(0, len(lst)):
        if is_perfect_square(lst[i]):
            nr = nr + 1
        else:
            if nr > maxim:
                finalposition = position
                maxim = nr
            position = i
            nr = 0
    if nr > maxim:
        finalposition = position
        maxim = nr
        # fara acest if in cazul in care subsirul maxim contine si ultimul element nu considera
    for i in range(finalposition + 1, finalposition + maxim + 1):
        lstmaxim.append(lst[i])
    return lstmaxim


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([]) == []
    assert get_longest_all_perfect_squares([1, 4, 5, 16, 16, 9]) == [16, 16, 9]
    assert get_longest_all_perfect_squares([9]) == [9]
    assert get_longest_all_perfect_squares([1, 4, 16, 9, 25]) == [1, 4, 16, 9, 25]


def test_get_longest_concat_is_prime():
    assert get_longest_concat_is_prime([]) == []
    assert get_longest_concat_is_prime([13, 5, 7]) == [13]
    assert get_longest_concat_is_prime([197, 3, 5, 4, 4]) == [197, 3]
    assert get_longest_concat_is_prime([71, 51, 4, 4]) == [71, 51]
    assert get_longest_concat_is_prime([4, 4, 4]) == []
    assert get_longest_concat_is_prime([3, 3, 3, 3]) == [3]


def main():
    test_get_longest_all_perfect_squares()
    test_get_longest_concat_is_prime()
    lst = []
    while True:
        print("1.Citirea datelor")
        print("2.Determinarea celei mai lungi subsecvente cu proprietatea ca toate numerele sunt patrate perfecte")
        print("3.Determinearea celei mai lungi subsecvente cu proprietatea ca concatenarea nr. este nr prim ")
        print("x.Iesire")
        option = input("Alegeti optiunea: ")
        if option == '1':
            lst = data_introduction()
        elif option == '2':
            print(get_longest_all_perfect_squares(lst))
        elif option == '3':
            print(get_longest_concat_is_prime(lst))
        else:
            break


main()
