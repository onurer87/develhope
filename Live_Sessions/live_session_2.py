##%%timeit


class Student:
    def __init__(self,first_name,last_name,id,subjects,grades):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self.subjects=subjects
        self.grades=grades
    def __eq__(self, __o: object) -> bool:
        pass

    def __repr__(self) -> str:
        pass



