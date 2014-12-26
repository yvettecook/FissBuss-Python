import fissbuss

def test_divisible_by_three():
    result = fissbuss.divisible_by_three(3)
    assert result == True
    print "passed: number is divisible by three"

def test_not_divisible_by_three():
    result = fissbuss.divisible_by_three(1)
    assert result == False
    print "passed: number is not divisible by three"

def test_divisible_by_five():
    result = fissbuss.divisible_by_five(5)
    assert result == True
    print "passed: number is divisible by five"

def test_not_divisible_by_five():
    result = fissbuss.divisible_by_five(1)
    assert result == False
    print "passed: number is not divisible by five"

def test_divisible_by_fifteen():
    result = fissbuss.divisible_by_fifteen(15)
    assert result == True
    print "passed: number is divisible by fifteen"

def test_not_divisible_by_fifteen():
    result = fissbuss.divisible_by_fifteen(1)
    assert result == False
    print "passed: number is not divisible by fifteen"

def test_playing_says_fiss():
    result = fissbuss.play(3)
    assert result == "Fiss"
    print "passed: game says 'Fiss'"

test_divisible_by_three()
test_not_divisible_by_three()
test_divisible_by_five()
test_not_divisible_by_five()
test_divisible_by_fifteen()
test_not_divisible_by_fifteen()
test_playing_says_fiss()
