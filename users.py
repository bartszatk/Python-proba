class System:
    def __init__(self, filename):
        self.filename = filename

    def register(self, name, password, age):
        with open(self.filename, "a") as f:
            f.write(f"{name};{password};{age}\n")

    def login(self, name, password):
        with open(self.filename, "r") as f:
            for line in f:
                n, p, a = line.strip().split(";")
                if n == name and p == password:
                    return True
        return False

    def adults(self):
        result = []
        with open(self.filename, "r") as f:
            for line in f:
                n, p, a = line.strip().split(";")
                if int(a) >= 18:
                    result.append(n)
        return result


sys = System("users.txt")

sys.register("Anna", "123", 20)
sys.register("Jan", "abc", 15)

print(sys.login("Anna", "123"))
print(sys.adults())
