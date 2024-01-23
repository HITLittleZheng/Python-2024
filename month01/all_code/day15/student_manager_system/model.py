class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid

    # 直接打印当前对象所使用的格式
    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},成绩是{self.score}"

    # 两个学生对象,学号相同即对象相同
    def __eq__(self, other):
        return self.sid == other.sid
