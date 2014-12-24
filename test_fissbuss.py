import fissbuss

def test_divisible_by_three():
    number = 3
    result = fissbuss.divisible_by_three(number)
    assert result == True
    print "passed: number is divisible by three"


test_divisible_by_three()
