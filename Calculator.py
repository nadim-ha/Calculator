from tkinter import *
import logging as log

class Application(Frame) :

    def _init_(self, master) :
        super(Application, self)._init_(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self) :
        self.user_input = Entry(self, bg="blue", bd= 29,insertwidth = 4, width = 24, font =("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0, "0")



        self.button1 = Button(self, bg = "#98DBC6", bd= 12, text = "7", padx = 33, pady = 25, command = lambda : self.buttonClick(7), font = ("Helvatica", 20, "bold"))
        self.button1.grid(row = 2, column = 0, sticky = W)

        self.button2 = Button(self, bg = "#98DBC6", bd= 12, text = "8", padx = 35, pady = 25, command = lambda : self.buttonClick(8), font = ("Helvatica", 20, "bold"))
        self.button2.grid(row = 2, column = 1, sticky = W)

        self.button3 = Button(self, bg = "#98DBC6", bd= 12, text = "9", padx = 33, pady = 25, command = lambda : self.buttonClick(9), font = ("Helvatica", 20, "bold"))
        self.button3.grid(row = 2, column = 2, sticky = W)

        self.button4 = Button(self, bg = "#98DBC6", bd= 12, text = "4", padx = 33, pady = 25, command = lambda : self.buttonClick(4), font = ("Helvatica", 20, "bold"))
        self.button4.grid(row = 3, column = 0, sticky = W)

        self.button5 = Button(self, bg = "#98DBC6", bd= 12, text = "5", padx = 35, pady = 25, command = lambda : self.buttonClick(5), font = ("Helvatica", 20, "bold"))
        self.button5.grid(row = 3, column = 1, sticky = W)

        self.button6 = Button(self, bg = "#98DBC6", bd= 12, text = "6", padx = 33, pady = 25, command = lambda : self.buttonClick(6), font = ("Helvatica", 20, "bold"))
        self.button6.grid(row = 3, column = 2, sticky = W)

        self.button7 = Button(self, bg = "#98DBC6", bd= 12, text = "1", padx = 33, pady = 25, command = lambda : self.buttonClick(1), font = ("Helvatica", 20, "bold"))
        self.button7.grid(row = 4, column = 0, sticky = W)

        self.button8 = Button(self, bg = "#98DBC6", bd= 12, text = "2", padx = 35, pady = 25, command = lambda : self.buttonClick(2), font = ("Helvatica", 20, "bold"))
        self.button8.grid(row = 4, column = 1, sticky = W)

        self.button9 = Button(self, bg = "#98DBC6", bd= 12, text = "3", padx = 33, pady = 25, command = lambda : self.buttonClick(3), font = ("Helvatica", 20, "bold"))
        self.button9.grid(row = 4, column = 2, sticky = W)

        self.button10 = Button(self, bg = "#98DBC6", bd= 12, text = "0", padx = 35, pady = 25, command = lambda : self.buttonClick(0), font = ("Helvatica", 20, "bold"))
        self.button10.grid(row = 5, column = 1, sticky = W)

        self.button11 = Button(self, bg = "#98DBC6", bd= 12, text = "+", padx = 33, pady = 25, command = lambda : self.buttonClick("+"), font = ("Helvatica", 20, "bold"))
        self.button11.grid(row = 5, column = 0, sticky = W)

        self.button12 = Button(self, bg = "#98DBC6", bd= 12, text = "-", padx = 33, pady = 25, command = lambda : self.buttonClick("-"), font = ("Helvatica", 20, "bold"))
        self.button12.grid(row = 5, column = 2, sticky = W)

        self.button13 = Button(self, bg = "#98DBC6", bd= 12, text = "*", padx = 33, pady = 25, command = lambda : self.buttonClick("*"), font = ("Helvatica", 20, "bold"))
        self.button13.grid(row = 6, column = 0, sticky = W)

        self.button14 = Button(self, bg = "#98DBC6", bd= 12, text = "/", padx = 35, pady = 25, command = lambda : self.buttonClick("/"), font = ("Helvatica", 20, "bold"))
        self.button14.grid(row = 6, column = 1, sticky = W)

        self.button15 = Button(self, bg = "#98DBC6", bd= 12, text = "=", padx = 33, pady = 25, command =self.CalculateTask, font = ("Helvatica", 20, "bold"))
        self.button15.grid(row = 6, column = 2, sticky = W)

        self.button16 = Button(self, bg = "#98DBC6", bd= 12, text = "Clear", padx = 33, pady = 25, command =self.ClearDisplay, font = ("Helvatica", 20, "bold"))
        self.button16.grid(row = 7, columnspan = 3, sticky = W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Sntax!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

    args = self.parse_args()
    if args.verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    log.info("This should be verbose.")
    log.warning("This is a warning.")
    log.error("This is an error.")

calculators = Tk()
calculators.title("Calculator")
app = Application(calculators)

calculators.resizable(width = False, height = False)

calculators.mainloop()
