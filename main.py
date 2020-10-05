
from tkinter import Tk, Canvas, Frame, BOTH
import random

n = 0


class Board(Frame):
    first_cells = []
    update_cells = []

    def __init__(self):
        super().__init__()
        self.initBoard()

    def initBoard(self):
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        for i in range(0, 600, 50):
            canvas.create_line(0, i, 600, i)
            canvas.create_line(i, 0, i, 600)
        for i in range(12):
            self.first_cells.append([random.randint(0, 1) for _ in range(12)])
        for i in range(12):
            self.update_cells.append([0 for _ in range(12)])
        self.boardReconstruction()
        canvas.pack(fill=BOTH, expand=1)

    def checkNeighbours(self):
        for i in range(12):
            for j in range(12):
                # 1
                if i == 0:
                    if j == 0:
                        self.update_cells[0][j] = self.first_cells[i + 1][j + 1]
                    else:

                # 2
                elif:
                    if j == 0:

                # 3
                elif:
                    if i == 11:
                        if j == 11:

                    else:

                # 4
                elif:
                    if j == 11:

                # 5
                else:
                    self.update_cells[i][j] = self.first_cells[i + 1][j + 1] + self.first_cells[i][j + 1] + \
                                              self.first_cells[i + 1][j] + self.first_cells[i - 1][j + 1] + \
                                              self.first_cells[i + 1][j - 1] + self.first_cells[i][j - 1] + \
                                              self.first_cells[i - 1][j] + self.first_cells[i - 1][j - 1]

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

    def boardReconstruction(self):
        global n
        canvas = Canvas(self)
        for i in range(12):
            for j in range(12):
                print(self.first_cells[i][j], end=' ')
            print()
        print()
        for i in range(12):
            for j in range(12):
                if self.first_cells[i][j] == 1:
                    canvas.create_rectangle(
                        i * 50, j * 50, (i + 1) * 50, (j + 1) * 50,
                        outline="#05f", fill="#f50"
                    )
        n += 1
        self.after(5, self.oneStep())

    def oneStep(self):
        if n < 10:
            self.checkNeighbours()
            self.tableReconstruction()
            self.boardReconstruction()


def main():
    root = Tk()
    ex = Board()
    root.geometry("600x600+600+600")
    root.mainloop()


if __name__ == '__main__':
    main()

