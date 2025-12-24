class EvenNumbers:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield i * 2


evens = EvenNumbers(12)
for num in evens:
    print(num)