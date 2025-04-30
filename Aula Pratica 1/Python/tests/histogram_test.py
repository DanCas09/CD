from histogram import showResults

def test1():
    H, list = showResults('./testFiles/test_file_5d.txt')
    if (H != 1.8394910703001344):
        print('Test1 Failed!')
        return
    print('Test1 Succeeded!')

test1()