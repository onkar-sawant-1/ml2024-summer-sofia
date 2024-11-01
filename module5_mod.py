class NumberSearch:
    def __init__(self):
        self.numbers = {}
        self.n = 1

    def read_numbers(self):
        count = self.readN("How many numbers would you like to search? ")
        for i in range(count):
            number = self.readN(f"Enter number {i + 1}: ")
            self.numbers[number] = self.n
            self.n += 1

    def search_number(self):
        x = self.readN("Enter number to search: ")
        print(self.numbers[x] if x in self.numbers else -1)

    def readN(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")