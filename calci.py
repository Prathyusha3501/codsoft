from tkinter import *

pink="#FF8080"
large_font=("Arial",40,"bold")
label_color="#0F0F0F"
small_font=("Arial",16)
digit_font=("Arial",24,"bold")
white="#FFFFFF"
default_font=("Arial",20)
off_white="#F8FAFF"
light_grey="#F5F5F5"
class Calculator:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Simple Calculator")
        self.total_expression = ""
        self.current_expression = ""


        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_label,self.label=self.create_display_labels()
        self.digits = {
            7: (1,1), 8: (1,2) , 9: (1,3),
            4: (2,1), 5: (2,2) , 6: (2,3),
            1: (3,1), 2: (3,2) , 3: (3,3),
            0: (4,2), ".":(4,1) 
        }
        self.operations = {"/": "\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()
        self.buttons_frame.rowconfigure(0,weight=1)
        for i in range(1,5):
            self.buttons_frame.rowconfigure(i,weight=1)
            self.buttons_frame.columnconfigure(i,weight=1)
    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.total_expression,anchor = E,bg=pink,fg=label_color,padx=24,font=small_font)
        total_label.pack(expand=True,fill="both")
        label = Label(self.display_frame,text=self.current_expression,anchor = E,bg=pink,fg=label_color,padx=24,font=large_font)
        label.pack(expand=True,fill="both")
        return total_label,label
    def adding_to_expression(self,value):
        self.current_expression += str(value)
        self.update_label()
    def create_remove_button(self):
        button=Button(self.buttons_frame,text="r",bg=light_grey,fg=label_color,font=default_font,borderwidth=0)
        button.grid(row=0,column=2,sticky=NSEW)
    def create_display_frame(self):
        frame=Frame(self.window, height = 221, bg=pink)
        frame.pack(expand=True, fill="both")
        return frame
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_squareroot_button()
    def create_operator_buttons(self):
        i=1
        for operator,symbol in self.operations.items():
            button=Button(self.buttons_frame,text=symbol,bg=light_grey,fg=label_color,font=default_font,borderwidth=0,command=lambda i=operator: self.append_operator(i))
            button.grid(row=i-1,column=4,sticky=NSEW)
            i+=1
    
    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_total_label()
        self.update_label()
    def create_clear_button(self):
        button=Button(self.buttons_frame,text="CLEAR",bg=light_grey,fg=label_color,font=default_font,borderwidth=0,command=self.clear)
        button.grid(row=0,column=1,sticky=NSEW)
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()
    def create_square_button(self):
        button=Button(self.buttons_frame,text="\u00b2",bg=light_grey,fg=label_color,font=default_font,borderwidth=0,command=self.square)
        button.grid(row=0,column=2,sticky=NSEW)
    def squareroot(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
    def create_squareroot_button(self):
        button=Button(self.buttons_frame,text="\u221ax",bg=light_grey,fg=label_color,font=default_font,borderwidth=0,command=self.squareroot)
        button.grid(row=0,column=3,sticky=NSEW)
    def create_equals_button(self):
        button=Button(self.buttons_frame,text="=",bg=off_white,fg=label_color,font=default_font,borderwidth=0,command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2,sticky=NSEW)
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = Button(self.buttons_frame,text=str(digit),bg=white,fg=label_color,font=digit_font,borderwidth=0,command=lambda i=digit: self.adding_to_expression(i))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=NSEW)
    def append_operator(self,operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression=str(eval(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()
    def create_buttons_frame(self):
        frame=Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    def update_total_label(self):
        expression=self.total_expression
        for operator,symbol in self.operations.items():
            expression=expression.replace(operator,f'{symbol}')
        self.total_label.config(text=expression)
    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop() 
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event,digit=key: self.adding_to_expression(digit))
        for key in self.operations:
            self.window.bind(key,lambda event, operator=key:self.append_operator(operator))
    
if __name__=="__main__":
    calci= Calculator()
    calci.run()
