class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Student inherits name and age from parent class person and is called using super()
    def student(person):
        def __init__(self, name, age, degree):
            super().__init__(name=name, age=age)
            self.degree = degree