class DrawFigures:
    def __init__(self):
        DrawFigures.start(self)

    def start(self):
        try:
            chooce_figure = input('Привет, это Draw Figures - программа для рисования фигур в консоли\n\nСоздайте запрос в формате название_фигуры размер\nК примеру square 5 ').split(' ')

            figure = chooce_figure[0]
            size = int(chooce_figure[1])

            self.draw_figure(figure,size)

        except ValueError:
            print('Размер должен быть указан цифрами')
        except KeyError:
            print('Такой фигуры нет!')
        except IndexError:
            print('Формат не верный!')

    def draw_figure(self,figure,size):
        figures = {
            'square' : self.draw_square,
            'square_hollow' : self.draw_square_hollow,
            'pyramid' : self.draw_pyramid,
            'cross' : self.draw_cross
        }
        figures[figure](size)
    def draw_square(self,size):
        for _ in range(size):
            for _ in range(size):
                print('# ',end = '')
            print('')

    def draw_square_hollow(self,size):
        print('#' * size)
        for _ in range(size):
            print('#' + (' ' * (size - 2)) + '#')
        print('#' * size)

    def draw_pyramid(self,size):
        for el in range(size + 1):
            print(' ' * (size - el),end='')
            for zel in range(el):
                print('# ',end='')
            print('')

    def draw_cross(self, size):
        for _ in range(size):
            print(' ' * size + '*' * size + ' ' * size)
        for _ in range(size):
            print('***' * size)
        for _ in range(size):
            print(' ' * size + '*' * size + ' ' * size)

if __name__ == '__main__':
    DrawFigures()
