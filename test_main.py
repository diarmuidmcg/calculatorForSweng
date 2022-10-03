from app import calculate

def test_with_all_three_operands():
    response = calculate("14+39-15*10+50");
    assert response == "-47"
    
def test_with_addition_and_subtraction_operands():
    response = calculate("564+642-345-613");
    assert response == "248"
    
def test_with_multiplication():
    response = calculate("87*23*53");
    assert response == "106053"
    
# ERROR CHECKING
def test_with_unexpected_string_char():
    response = calculate("87t23*53");
    assert response == "error: unexpected string character: t"
    
def test_with_duplicated_operation():
    response = calculate("87+23**53");
    assert response == "error: duplicate operation: *"