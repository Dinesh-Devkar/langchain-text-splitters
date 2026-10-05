from langchain_text_splitters import RecursiveCharacterTextSplitter,Language,PythonCodeTextSplitter

text="""
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

    def climb(self):
        print(f"{self.name} is climbing the tree.")


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Tweet! Tweet!")

    def fly(self):
        print(f"{self.name} is flying in the sky.")


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says: Moo!")

    def give_milk(self):
        print(f"{self.name} is giving milk.")


# Create objects
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1)
cow = Cow("Daisy", 5)


# Dog
print("----- DOG -----")
dog.show_info()
dog.eat()
dog.sleep()
dog.make_sound()
dog.fetch()

# Cat
print("\n----- CAT -----")
cat.show_info()
cat.eat()
cat.sleep()
cat.make_sound()
cat.climb()

# Bird
print("\n----- BIRD -----")
bird.show_info()
bird.eat()
bird.sleep()
bird.make_sound()
bird.fly()

# Cow
print("\n----- COW -----")
cow.show_info()
cow.eat()
cow.sleep()
cow.make_sound()
cow.give_milk()

"""

splitter=RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON,
                                                      chunk_size=300,
                                                      chunk_overlap=10)

docs=splitter.split_text(text)

print(len(docs))

print(docs)