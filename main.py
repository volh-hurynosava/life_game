import random
import pandas

class Board():
    first_cells = []
    update_cells = []

    def __init__(self):
        super().__init__()
        self.initBoard()
#Рандомом задаются заполненные клетки
    def initBoard(self):
        for i in range(12):
            self.first_cells.append([random.randint(0, 1) for _ in range(12)])
        for i in range(12):
            self.update_cells.append([0 for _ in range(12)])
        self.boardReconstruction()
#Подсчет количества соседей
    def checkNeighbours(self):
        for i in range(12):
            for j in range(12):
                # 1
                if i == 0:
                    if j == 0:
                        self.update_cells[0][0] = self.first_cells[1][1] + self.first_cells[0][1] + self.first_cells[1][
                            0] + self.first_cells[0][11] + self.first_cells[1][11] + self.first_cells[11][0] + \
                                                  self.first_cells[11][1] + self.first_cells[11][11]
                    else:
                        if j != 11:
                            self.update_cells[0][j] = self.first_cells[0][j + 1] + self.first_cells[0][j - 1] + \
                                                      self.first_cells[1][j + 1] + self.first_cells[1][j - 1] + \
                                                      self.first_cells[1][j] + self.first_cells[11][j + 1] + \
                                                      self.first_cells[11][j] + self.first_cells[11][j - 1]
                        else:
                            self.update_cells[0][11] = self.first_cells[0][0] + self.first_cells[0][10] + \
                                                       self.first_cells[1][0] + self.first_cells[1][10] + \
                                                       self.first_cells[1][11] + self.first_cells[11][0] + \
                                                       self.first_cells[11][11] + self.first_cells[11][10]
                # 2
                if i != 0:
                    if j == 0:
                        if i != 11:
                            self.update_cells[i][0] = self.first_cells[i - 1][0] + self.first_cells[i + 1][0] + \
                                                      self.first_cells[i - 1][1] + self.first_cells[i][1] + \
                                                      self.first_cells[i + 1][1] + self.first_cells[i][11] + \
                                                      self.first_cells[i - 1][11] + self.first_cells[i + 1][11]
                        else:
                            self.update_cells[i][0] = self.first_cells[10][0] + self.first_cells[0][0] + \
                                                      self.first_cells[10][1] + self.first_cells[11][1] + \
                                                      self.first_cells[0][1] + self.first_cells[11][11] + \
                                                      self.first_cells[10][11] + self.first_cells[0][11]
                # 3
                if i == 11:
                    if j == 11:
                        self.update_cells[11][11] = self.first_cells[0][0] + self.first_cells[11][0] + \
                                                    self.first_cells[10][0] + self.first_cells[0][10] + \
                                                    self.first_cells[0][11] + self.first_cells[10][10] + \
                                                    self.first_cells[10][11] + self.first_cells[11][10]
                    else:
                        if j != 0:
                            self.update_cells[11][j] = self.first_cells[11][j + 1] + self.first_cells[11][j - 1] + \
                                                       self.first_cells[10][j] + self.first_cells[10][j - 1] + \
                                                       self.first_cells[10][j + 1] + self.first_cells[0][j] + \
                                                       self.first_cells[0][j - 1] + self.first_cells[0][j + 1]

                # 4
                if i != 11 and i != 0:
                    if j == 11:
                        self.update_cells[i][11] = self.first_cells[i - 1][11] + self.first_cells[i + 1][11] + \
                                                   self.first_cells[i][10] + self.first_cells[i - 1][10] + \
                                                   self.first_cells[i + 1][10] + self.first_cells[i][0] + \
                                                   self.first_cells[i - 1][0] + self.first_cells[i + 1][0]

                # 5
                if i != 11 and i != 0 and j != 0 and j != 11:
                    self.update_cells[i][j] = self.first_cells[i + 1][j + 1] + self.first_cells[i][j + 1] + \
                                              self.first_cells[i + 1][j] + self.first_cells[i - 1][j + 1] + \
                                              self.first_cells[i + 1][j - 1] + self.first_cells[i][j - 1] + \
                                              self.first_cells[i - 1][j] + self.first_cells[i - 1][j - 1]
#Обновление поля
    def tableReconstruction(self):
        for i in range(12):
            for j in range(12):
                if self.first_cells[i][j]:
                    if self.update_cells[i][j] == 2 or self.update_cells[i][j] == 3:
                        self.first_cells[i][j] = 1
                    else:
                        self.first_cells[i][j] = 0
                else:
                    if self.update_cells[i][j] == 3:
                        self.first_cells[i][j] = 1
#Вывод поля в консоль
    def boardReconstruction(self):
        global n
        for i in range(12):
            for j in range(12):
                print(self.first_cells[i][j], end=' ')
            print()
        print()
        n -= 1
        self.oneStep()
    def oneStep(self):
        if n > -1:
            self.checkNeighbours()
            self.tableReconstruction()
            self.boardReconstruction()

#Количество итераций обновления поля задается вручную
def main():
    global n
    print('Введите количество итераций')
    n = int(input())
    Board()


if __name__ == '__main__':
    main()

