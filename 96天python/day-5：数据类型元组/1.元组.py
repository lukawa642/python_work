import numpy as np
import matplotlib.pyplot as plt

people_number = 5 # 人物生数成设定5
world_size = 11	# 房间长宽11个元胞


class People:

    world = np.zeros((world_size, world_size))
    			# 这里是定义的静态变量 同一类的 实例对象 共享这一个
    door = np.array((0, 3)).reshape((1, 2))
    			 # 可注意到这里的变量名前不用写 self.

    def __init__(self):
        self.position = None       #
        		# 在这里初始化实例对象属性

    def generate(self, x, y):
        People.world[x, y] = 1
        self.position = np.array((x, y)).reshape((1, 2))

    def move(self):
        if (self.position == self.door).all():
            return 1
        else:
            move_matrix = np.array([[-1, -1],
                                    [-1,  0],
                                    [-1,  1],
                                    [ 0, -1],
                                    [ 0,  0],
                                    [ 0,  1],
                                    [ 1, -1],
                                    [ 1,  0],
                                    [ 1,  1]])

            distance = np.zeros(9)  # distance 初始化
            for i in range(9):
                distance[i] = np.sum(np.abs(self.position + move_matrix[i, :] - self.door)) # 路径选择(最近临胞)
            choose = distance.argmin()
            # 房间更新
            People.world[self.position[0, 0], self.position[0, 1]] = 0
            self.position += move_matrix[choose, :]
            People.world[self.position[0, 0], self.position[0, 1]] = 1
            return 0


if __name__ == '__main__':

    a = []
    for i in range(people_number):
        a.append(People())
        a[i].generate(np.random.randint(0, world_size), np.random.randint(0, world_size))  # 随机产生人物时可能重叠

    fig = plt.figure()
    plt.imshow(People.world)
    plt.xticks(())
    plt.yticks(())
    plt.ion()
    plt.show()

    # print(People.world, '\n')    # 类名.属性名 直接访问
    # a[0].world = xxx  # 这样会创建一个同名的 实例对象的属性

    flags = np.zeros((1, people_number))
    while np.sum(flags) < people_number:
        for i in range(people_number):
            flags[0, i] = a[i].move()
            plt.imshow(People.world)
            plt.pause(0.5)


# ————————————————
# 版权声明：本文为CSDN博主「Ackerman19」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_41068726/article/details/99733647