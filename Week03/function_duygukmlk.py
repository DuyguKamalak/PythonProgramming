square_root = lambda x=16: x ** 0.5


def power_sum(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
   
    """
   This function divides the sum of the 'x' to the power of 'a' and 'y' to the power of 'b' by 'c'.
   :param x: The first number, default is 0.
   :type x: int
   :param y: The second number, default is 0.
   :type y: int
   :param a: The third number, default is 1.
   :type a: int
   :param b: The fourth number, default is 1.
   :type b: int
   :param c: The fifth number, default is 1.
   :type c: int
   :return: The sum of 'x' power 'a' and 'y' power 'b' divided by c.
   :rtype: float
   """
   
    return (x ** a + y ** b) / c

def function_call_counter() -> (int, dict[str, int]):
    
    if not hasattr(function_call_counter, "call_counter"):
        function_call_counter.call_counter = 0
        function_call_counter.caller_counts = {}

    caller_name = __name__
    function_call_counter.call_counter += 1

    if caller_name in function_call_counter.caller_counts:
        function_call_counter.caller_counts[caller_name] += 1
    else:
        function_call_counter.caller_counts[caller_name] = 1
    return function_call_counter.call_counter, function_call_counter.caller_counts


result = square_root(16)
print(result)  #out:4

result = power_sum(2, 3, 2, 3, c=2)
print(result)   #out:15.5

call_count, caller_counts = function_call_counter()
print(call_count)  #out:1
print(caller_counts)  #out:{'__main__': 1}
