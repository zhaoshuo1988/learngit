class Word:
    def __init__(self,filename):
        self.filename=filename
        self.text=None

    def edit_text(self,t):
        self.text =t

    def print_text(self,printer):
        printer.output_text(self.text)

class Printer:
    def __init__(self,model):
        self.model=model

    def output_text(self,t):
        print("打印")

class WBpritner(Printer):
    def __init__(self,model):
        super().__init__(model)

    def output_text(self,t):
        print("print")


class Copritner(Printer):
    def __init__(self,model):
        super().__init__(model)

    def output_text(self,t):
        print("打印")

if __name__='__main__':
    f1=Word('file1')
    f1.edit_text('askldj')
    p1=printer('惠普')
    f1.print_text(p1)

