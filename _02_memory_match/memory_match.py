"""
Create a memory match game!
"""
import random
import time
x = random.randint(300, 3030)
time.sleep(1)
import tkinter as tk

# TODO: First, run this code. You should see a grid with 52 buttons.
#   Your task is to:
#   1. Create a dictionary with each button as a key and a number from 1 to 13
#      as the corresponding value. There are 52 buttons, so there should be EXACTLY
#      4 copies of each number from 1 ot 13.
#   2. Show the value of the button (a number from 1 to 13) when it's clicked.
#   3. After the second button is clicked, check if the number from the first button
#      matches the number of the second button.
#      a. If they match, show the two numbers and disable them so they can't be clicked again.
#         There is an example of how to disable the button in the code below.
#      b. If they don't match, remove the text from the two buttons. The two buttons should
#         still be clickable.
#   4. End the game with a congratulations message when all the numbers have been matched.
#   5. See 'memory_match_example.png' in this folder for an example of what the game should
#      look like.
class MemoryMatch(tk.Tk):
    WIDTH = 1090
    HEIGHT = 500
    TOTAL_BUTTONS = 52

    def __init__(self):
        super().__init__()

        # 4 copies of each value
        num_copies_each_value = 4
        buttons_per_row = MemoryMatch.TOTAL_BUTTONS / 4
        button_width, button_height = self.setup_buttons(buttons_per_row)
        self.button_pressed = ""
        self.button_num = 0
        self.past_button_num = 0
        self.past_button_press = ''
        self.used_dic = {}
        self.dic = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13}
        for i in range(MemoryMatch.TOTAL_BUTTONS):
            row_num = int(i / buttons_per_row)
            col_num = int(i % buttons_per_row)
            row_y = row_num * button_height
            col_x = col_num * button_width

            button = tk.Button(self, text='', fg='black', font=('arial', 24, 'bold'))
            button.place(x=col_x, y=row_y, width=button_width, height=button_height)

            button.bind('<ButtonPress>', self.on_button_press)

    def check_match(self):
        if self.button_pressed in self.used_dic:
            if self.used_dic[self.button_pressed] == self.used_dic[self.button_pressed]:
                self.button_pressed.configure(state=tk.DISABLED, text=self.button_num)
                self.past_button_press.configure(state=tk.DISABLED, text=self.button_num)
            else:
                self.button_pressed.configure(state=tk.NORMAL, text='')
                self.past_button_press.configure(state=tk.NORMAL, text='')
        else:
            pass
        print(self.used_dic)

    def on_button_press(self, event):
        self.button_pressed = event.widget
        while True:
            self.button_num = random.randint(1, 13)
            if self.button_num not in self.used_dic:
                self.used_dic.update({self.button_pressed: self.button_num})
                break
            else:
                pass
        self.past_button_press = self.button_pressed
        MemoryMatch.check_match(self)
        print('Button ' + str(self.button_pressed) + ' was pressed')

        if self.button_pressed['state'] == tk.DISABLED:
            self.button_pressed.configure(state=tk.NORMAL, text=self.button_num)
        elif self.button_pressed['state'] == tk.NORMAL:
            self.button_pressed.configure(state=tk.DISABLED, text='')



    def setup_buttons(self, buttons_per_row):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('%sx%s' % (MemoryMatch.WIDTH, MemoryMatch.HEIGHT))
        self.update_idletasks()

        num_rows = int(MemoryMatch.TOTAL_BUTTONS / buttons_per_row)
        if MemoryMatch.TOTAL_BUTTONS % buttons_per_row != 0:
            num_rows += 1

        button_width = int(self.winfo_width() / buttons_per_row)
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height

if __name__ == '__main__':
    game = MemoryMatch()
    game.title('League Python Memory Game')
    game.mainloop()
