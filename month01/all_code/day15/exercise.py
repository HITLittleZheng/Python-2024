# 适合面向过程
import module_exercise

module_exercise.data = 10
module_exercise.func01()

# 调用类方法使用类名
module_exercise.MyClass.func03()
m = module_exercise.MyClass()
# 调用实例方法使用对象
m.func02()  # func02(m)

# 适合面向对象
from module_exercise import *

print(data)
func01()
MyClass.func03()
m = MyClass()
m.func02()

print(__name__)