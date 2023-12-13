class WindowManger:
    def __init__(self):
        self.window_stack = []

    def push_window(self, window):
        if self.window_stack:
            self.window_stack[-1].withdraw()    #-1 refers to the last element in the list
        self.window_stack.append(window)
        window.deiconify() #.deiconify make new window visible

    def pop_window(self):
        if self.window_stack:
            current_window = self.window_stack.pop()
            current_window.destroy()
        if self.window_stack:
            self.window_stack[-1].deiconify() #opens the previous window

    def delete_stack(self):
        if self.window_stack:
            for window in self.window_stack:
                self.window_stack.pop()
