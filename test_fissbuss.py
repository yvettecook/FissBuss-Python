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

test_divisible_by_three()
test_not_divisible_by_three()
test_divisible_by_five()
