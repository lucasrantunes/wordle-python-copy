from view import View
class Game:
    def __init__(self) -> None:
        self.word_vector = [[] for i in range(6)]
        self.current_word = 0
        self.view = View(self.key_event_letter, self.key_event_backspace, self.key_event_enter)
        # view.label_box[0][0].config(text = "M")
        # print(f"{view.get_label_text(0,0)} k")
        self.view.mainloop()

    def key_event_letter(self, letter):
        if len(self.word_vector[self.current_word]) < 5:
            self.word_vector[self.current_word].append(letter)
            self.view.update_label_box(self.current_word, len(self.word_vector[self.current_word]) - 1, letter)
            print(self.word_vector)
    
    def key_event_backspace(self):
        if len(self.word_vector[self.current_word]) > 0:
            self.view.update_label_box(self.current_word, len(self.word_vector[self.current_word]) - 1, "")
            self.word_vector[self.current_word].pop()
            print(self.word_vector)
    
    def key_event_enter(self):
        if len(self.word_vector[self.current_word]) == 5 and self.current_word < 5:
            self.current_word += 1
            self.view.active_label_row(self.current_word)
            print(self.word_vector)

if __name__ == "__main__":
    game = Game()