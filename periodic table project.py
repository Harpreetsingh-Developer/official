'''Thong Nguyen
Programming Project
Periodic Table Search Program'''
from tkinter import *

TITLE_FONT = ("Helvetica", 18, "bold")
TITLE_FONT2 = ("Helvetica", 12)

class Element:
    def __init__(self, FullName, Symbol, AtomicNumb, AtomicW):
        self.FullName = FullName
        self.Symbol = Symbol
        self.AtomicNumb = AtomicNumb
        self.AtomicW = AtomicW
    def display(self):
        print("Full Name    : ", self.FullName)
        print("Symbol       : ", self.Symbol)
        print("Atomic Number: ", self.AtomicNumb)
        print("Atomic Weight: ", self.AtomicW)
        
def PeriodicTable():
    Table = []
    Table.append(Element("Hydrogen", "H", 1, 1.008))
    Table.append(Element("Helium", "He", 2, 4.003))
    Table.append(Element("Lithium", "Li", 3, 6.941))
    Table.append(Element("Beryllium", "Be", 4, 9.012))
    Table.append(Element("Boron", "B", 5, 10.811))
    Table.append(Element("Carbon", "C", 6, 12.011))
    Table.append(Element("Nitrogen", "N", 7, 14.007))
    Table.append(Element("Oxygen", "O", 8, 15.999))
    Table.append(Element("Fluorine", "F", 9, 18.998))
    Table.append(Element("Neon", "Ne", 10, 20.180))
    Table.append(Element("Sodium", "Na", 11, 22.990))
    Table.append(Element("Magnesium", "Mg", 12, 24.305))
    Table.append(Element("Aluminum", "Al", 13, 26.982))
    Table.append(Element("Silicon", "Si", 14, 28.086))
    Table.append(Element("Phosphorus", "P", 15, 30.974))
    Table.append(Element("Sulfur", "S", 16, 32.066))
    Table.append(Element("Chlorine", "Cl", 17, 35.453))
    Table.append(Element("Argon", "Ar", 18, 39.948))
    Table.append(Element("Potassium", "K", 19, 39.098))
    Table.append(Element("Calcium", "Ca", 20, 40.078))
    Table.append(Element("Scandium", "Sc", 21, 44.956))
    Table.append(Element("Titanium", "Ti", 22, 47.867))
    Table.append(Element("Vanadium", "V", 23, 50.942))
    Table.append(Element("Chromium", "Cr", 24, 51.996))
    Table.append(Element("Manganese", "Mn", 25, 54.938))
    Table.append(Element("Iron", "Fe", 26, 55.845))
    Table.append(Element("Cobalt", "Co", 27, 58.933))
    Table.append(Element("Nickel", "Ni", 28, 58.693))
    Table.append(Element("Copper", "Cu", 29, 63.546))
    Table.append(Element("Zinc", "Zn", 30, 65.38))
    Table.append(Element("Gallium", "Ga", 31, 69.723))
    Table.append(Element("Germanium", "Ge", 32, 72.631))
    Table.append(Element("Arsenic", "As", 33, 74.922))
    Table.append(Element("Selenium", "Se", 34, 78.972))
    Table.append(Element("Bromine", "Br", 35, 79.904))
    Table.append(Element("Krypton", "Kr", 36, 84.798))
    Table.append(Element("Rubidium", "Rb", 37, 85.468))
    Table.append(Element("Strontium", "Sr", 38, 87.62))
    Table.append(Element("Yttrium", "Y", 39, 88.906))
    Table.append(Element("Zirconium", "Zr", 40, 91.224))
    Table.append(Element("Niobium", "Nb", 41, 92.906))
    Table.append(Element("Molybdenum", "Mo", 42, 95.95))
    Table.append(Element("Technetium", "Tc", 43, 98.907))
    Table.append(Element("Ruthenium", "Ru", 44, 101.07))
    Table.append(Element("Rhodium", "Rh", 45, 102.906))
    Table.append(Element("Palladium", "Pd", 46, 106.42))
    Table.append(Element("Silver", "Ag", 47, 107.868))
    Table.append(Element("Cadmium", "Cd", 48, 112.411))
    Table.append(Element("Indium", "In", 49, 114.818))
    Table.append(Element("Tin", "Sn", 50, 118.711))
    Table.append(Element("Antimony", "Sb", 51, 121.760))
    Table.append(Element("Tellurium", "Te", 52, 127.6))
    Table.append(Element("Iodine", "I", 53, 126.904))
    Table.append(Element("Xenon", "Xe", 54, 131.294))
    Table.append(Element("Cesium", "Cs", 55, 132.905))
    Table.append(Element("Barium", "Ba", 56, 137.328))
    Table.append(Element("Lanthanum", "La", 57, 138.905))
    Table.append(Element("Cerium", "Ce", 58, 140.116))
    Table.append(Element("Praseodymium", "Pr", 59, 140.908))
    Table.append(Element("Neodymium", "Nd", 60, 144.242))
    Table.append(Element("Promethium", "Pm", 61, 144.913))
    Table.append(Element("Samarium", "Sm", 62, 150.36))
    Table.append(Element("Europium", "Eu", 63, 151.964))
    Table.append(Element("Gadolinium", "Gd", 64, 157.25))
    Table.append(Element("Terbium", "Tb", 65, 158.925))
    Table.append(Element("Dysprosium", "Dy", 66, 162.500))
    Table.append(Element("Holmium", "Ho", 67, 164.930))
    Table.append(Element("Erbium", "Er", 68, 167.259))
    Table.append(Element("Thulium", "Tm", 69, 168.934))
    Table.append(Element("Ytterbium", "Yb", 70, 173.055))
    Table.append(Element("Lutetium", "Lu", 71, 174.967))
    Table.append(Element("Hafnium", "Hf", 72, 178.49))
    Table.append(Element("Tantalum", "Ta", 73, 180.948))
    Table.append(Element("Tungsten", "W", 74, 183.84))
    Table.append(Element("Rhenium", "Re", 75, 186.207))
    Table.append(Element("Osmium", "Os", 76, 190.23))
    Table.append(Element("Iridium", "Ir", 77, 192.217))
    Table.append(Element("Platinum", "Pt", 78, 195.085))
    Table.append(Element("Gold", "Au", 79, 196.967))
    Table.append(Element("Mercury", "Hg", 80, 200.592))
    Table.append(Element("Thallium", "TI", 81, 204.383))
    Table.append(Element("Lead", "Pb", 82, 207.2))
    Table.append(Element("Bismuth", "Bi", 83, 208.980))
    Table.append(Element("Polonium", "Po", 84, 208.982))
    Table.append(Element("Astatine", "At", 85, 209.987))
    Table.append(Element("Radon", "Rn", 86, 222.018))
    Table.append(Element("Francium", "Fr", 87, 223.020))
    Table.append(Element("Radium", "Ra", 88, 226.025))
    Table.append(Element("Actinium", "Ac", 89, 227.028))
    Table.append(Element("Thorium", "Th", 90, 232.038))
    Table.append(Element("Protactinium", "Pa", 91, 231.036))
    Table.append(Element("Uranium", "U", 92, 238.029))
    Table.append(Element("Neptunium", "Np", 93, 237.048))
    Table.append(Element("Plutonium", "Pu", 94, 244.064))
    Table.append(Element("Americium", "Am", 95, 243.061))
    Table.append(Element("Curium", "Cm", 96, 247.070))
    Table.append(Element("Berkelium", "Bk", 97, 247.070))
    Table.append(Element("Californium", "Cf", 98, 251.080))
    Table.append(Element("Einsteinium", "Es", 99, 254))
    Table.append(Element("Fermium", "Fm", 100, 257.095))
    Table.append(Element("Mendelevium", "Md", 101, 258.1))
    Table.append(Element("Nobelium", "No", 102, 259.101))
    Table.append(Element("Lawrencium", "Lr", 103, 262))
    Table.append(Element("Rutherfordium", "Rf", 104, 261))
    Table.append(Element("Dubnium", "Db", 105, 262))
    Table.append(Element("Seaborgium", "Sg", 106, 266))
    Table.append(Element("Bohrium", "Bh", 107, 264))
    Table.append(Element("Hassium", "Hs", 108, 269))
    Table.append(Element("Meitnerium", "Mt", 109, 268))
    Table.append(Element("Darmstadtium", "Ds", 110, 269))
    Table.append(Element("Roentgenium", "Rg", 111, 272))
    Table.append(Element("Copernicium", "Cn", 112, 277))
    Table.append(Element("Ununtrium", "Uut", 113, "unknown"))
    Table.append(Element("Flerovium", "FI", 114, 289))
    Table.append(Element("Ununpentium", "Uup", 115, "unknown"))
    Table.append(Element("Livermorium", "Lv", 116, 298))
    Table.append(Element("Ununseptium", "Uus", 117, 277))
    Table.append(Element("Ununoctium", "Uuo", 118, "unknown"))
    return Table

def SearchTable(a, b, c, d):
    resultList = []
    Table = PeriodicTable()
    if (a != None):
        a = a.capitalize()
        for i in (Table):
            if i.FullName == a:
                resultList.append(i)
    elif (b != None):
        b = b.capitalize()
        for i in (Table):
            if i.Symbol == b:
                resultList.append(i)
    elif (c != None):
        if (c.isdigit()):
            c = int(c)
            for i in (Table):
                if i.AtomicNumb == c:
                    resultList.append(i)
    elif (d != None):
        for i in (Table):
            if i.AtomicW == d:
                resultList.append(i)
    return resultList

class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Periodic Table Search')
        self.geometry('600x600')
        self.frames = {}
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Periodic Table Search\n Main Menu\n(Select an option)", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Search Using Atomic Number",
                            command=lambda: controller.show_frame("PageOne"),font=TITLE_FONT2)
        button1.config(width=50, height = 4)
        button2 = Button(self, text="Search Using Atomic Weight",
                            command=lambda: controller.show_frame("PageTwo"),font=TITLE_FONT2)
        button2.config(width=50, height = 4)
        button3 = Button(self, text="Search Using Full Name",command=lambda: controller.show_frame("PageThree"), font=TITLE_FONT2)
        button3.config(width=50, height = 4)
        button4 = Button(self, text="Search Using Symbol",command=lambda: controller.show_frame("PageFour"), font=TITLE_FONT2)
        button4.config(width=50, height = 4)
        button5 = Button(self, text="Breaking Down Molecule",command=lambda: controller.show_frame("PageFive"), font=TITLE_FONT2)
        button5.config(width=50, height = 4)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()


class PageOne(Frame):
    def __init__(self, parent, controller):
        self.count = 0
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Search using Atomic Number", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label2 = Label(self, text="Enter atomic number: ", font=TITLE_FONT2)
        label2.pack()
        self.atomic = Entry(self)
        self.atomic.pack()
        button1=Button(self, text = "Submit", command= self.Execute)
        button = Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"), font=TITLE_FONT2)
        button.config(width=50, height = 5)
        button1.pack(side = 'top')
        button.pack(side = 'bottom')
        displayList = []
    def Execute(self):
        resultList = []
        if self.count != 0:
            for i in (self.displayList):
                i.destroy()
        self.displayList = []
        resultList = SearchTable(None, None, self.atomic.get(), None)
        if len(resultList) != 0:
            self.displayList.append(Label(self, text = "Found " + str(len(resultList)) + " result(s)"))
            for i in (resultList):
                self.displayList.append(Label(self, text = "\nFull Name: " + i.FullName))
                self.displayList.append(Label(self, text = "Symbol: " + i.Symbol))
                self.displayList.append(Label(self, text = "Atomic Number: " + str(i.AtomicNumb)))
                self.displayList.append(Label(self, text = "Atomic Weight: " + str(i.AtomicW) + "\n"))
        else:
            self.displayList.append(Label(self, text = "Invalid input! No result Found. Enter another value"))
        for i in (self.displayList):
            i.pack()
        self.count += 1


class PageTwo(Frame):
    def __init__(self, parent, controller):
       self.count = 0
       Frame.__init__(self, parent)
       self.controller = controller
       label = Label(self, text="Search using Atomic Weight", font=TITLE_FONT)
       label.pack(side="top", fill="x", pady=10)
       label2 = Label(self, text="Enter atomic weight: ", font=TITLE_FONT2)
       label2.pack()
       self.atomic = Entry(self)
       self.atomic.pack()
       button1=Button(self, text = "Submit", command= self.Execute)
       button = Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"), font=TITLE_FONT2)
       button.config(width=50, height = 5)
       button1.pack(side = 'top')
       button.pack(side = 'bottom')
       displayList = []
    def Execute(self):
        resultList = []
        if self.count != 0:
            for i in (self.displayList):
                i.destroy()
        self.displayList = []
        resultList = SearchTable(None, None, None, float(self.atomic.get()))
        if len(resultList) != 0:
            self.displayList.append(Label(self, text = "Found " + str(len(resultList)) + " result(s)."))
            for i in (resultList):
                self.displayList.append(Label(self, text = "\nFull Name: " + i.FullName))
                self.displayList.append(Label(self, text = "Symbol: " + i.Symbol))
                self.displayList.append(Label(self, text = "Atomic Number: " + str(i.AtomicNumb)))
                self.displayList.append(Label(self, text = "Atomic Weight: " + str(i.AtomicW) + "\n"))
        else:
            self.displayList.append(Label(self, text = "Invalid input! No result Found. Enter another value"))
        for i in (self.displayList):
            i.pack()
        self.count += 1
        
class PageThree(Frame):
    def __init__(self, parent, controller):
       self.count = 0
       Frame.__init__(self, parent)
       self.controller = controller
       label = Label(self, text="Search using Element Name", font=TITLE_FONT)
       label.pack(side="top", fill="x", pady=10)
       label2 = Label(self, text="Enter the element name: ", font=TITLE_FONT2)
       label2.pack()
       self.atomic = Entry(self)
       self.atomic.pack()
       button1=Button(self, text = "Submit", command= self.Execute)
       button = Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"), font=TITLE_FONT2)
       button.config(width=50, height = 5)
       button1.pack(side = 'top')
       button.pack(side = 'bottom')
       displayList = []
    def Execute(self):
        resultList = []
        if self.count != 0:
            for i in (self.displayList):
                i.destroy()
        self.displayList = []
        resultList = SearchTable(self.atomic.get(),None, None, None)
        if len(resultList) != 0:
            self.displayList.append(Label(self, text = "Found " + str(len(resultList)) + " result(s)."))
            for i in (resultList):
                self.displayList.append(Label(self, text = "\nFull Name: " + i.FullName))
                self.displayList.append(Label(self, text = "Symbol: " + i.Symbol))
                self.displayList.append(Label(self, text = "Atomic Number: " + str(i.AtomicNumb)))
                self.displayList.append(Label(self, text = "Atomic Weight: " + str(i.AtomicW) + "\n"))
        else:
            self.displayList.append(Label(self, text = "Invalid input! No result Found. Enter another value"))
        for i in (self.displayList):
            i.pack()
        self.count += 1
        
class PageFour(Frame):
    def __init__(self, parent, controller):
       self.count = 0
       Frame.__init__(self, parent)
       self.controller = controller
       label = Label(self, text="Search using Element Symbol", font=TITLE_FONT)
       label.pack(side="top", fill="x", pady=10)
       label2 = Label(self, text="Enter the element symbol: ", font=TITLE_FONT2)
       label2.pack()
       self.atomic = Entry(self)
       self.atomic.pack()
       button1=Button(self, text = "Submit", command= self.Execute)
       button = Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"), font=TITLE_FONT2)
       button.config(width=50, height = 5)
       button1.pack(side = 'top')
       button.pack(side = 'bottom')
       displayList = []
    def Execute(self):
        resultList = []
        if self.count != 0:
            for i in (self.displayList):
                i.destroy()
        self.displayList = []
        resultList = SearchTable(None, self.atomic.get(), None, None)
        if len(resultList) != 0:
            self.displayList.append(Label(self, text = "Found " + str(len(resultList)) + " result(s)."))
            for i in (resultList):
                self.displayList.append(Label(self, text = "\nFull Name: " + i.FullName))
                self.displayList.append(Label(self, text = "Symbol: " + i.Symbol))
                self.displayList.append(Label(self, text = "Atomic Number: " + str(i.AtomicNumb)))
                self.displayList.append(Label(self, text = "Atomic Weight: " + str(i.AtomicW) + "\n"))
        else:
            self.displayList.append(Label(self, text = "Invalid input! No result Found. Enter another value"))
        for i in (self.displayList):
            i.pack()
        self.count += 1
class PageFive(Frame):
    def __init__(self, parent, controller):
       self.count = 0
       Frame.__init__(self, parent)
       self.controller = controller
       label = Label(self, text="Breaking Down Molecule", font=TITLE_FONT)
       label.pack(side="top", fill="x", pady=10)
       label2 = Label(self, text="Enter the molecule: ", font=TITLE_FONT2)
       label2.pack()
       self.atomic = Entry(self)
       self.atomic.pack()
       button1=Button(self, text = "Submit", command= self.Execute)
       button = Button(self, text="Back to Main Menu",
                           command=lambda: controller.show_frame("StartPage"), font=TITLE_FONT2)
       button.config(width=50, height = 5)
       button1.pack(side = 'top')
       button.pack(side = 'bottom')
       displayList = []
    def Execute(self):
        Mol = self.atomic.get()
        letterList = []
        digitList = []
        resultList = []
        if self.count != 0:
            for i in (self.displayList):
                i.destroy()
        self.displayList = []
        Table = PeriodicTable()
        letterList.append(Mol[0])
        for i in range(1, len(Mol)):
            if (Mol[i].isdigit()):
                digitList.append(int(Mol[i]))
            elif (Mol[i].isupper()):
                if (Mol[i-1].isdigit() == False):
                    digitList.append(1)
                letterList.append(Mol[i])
            elif (Mol[i].islower()):
                letterList[len(letterList)-1]=letterList[len(letterList)-1] + Mol[i]
        if (Mol[len(Mol)-1].isdigit() == False):
            digitList.append(1)
        for i in letterList:
            for j in Table:
                if (i == j.Symbol):
                    resultList.append(j.FullName)
        self.displayList.append(Label(self, text = "The molecule contains " + str(len(resultList)) + " Element(s):"))
        for i in range(0, len(resultList)):
            self.displayList.append(Label(self, text="- "+str(digitList[i])+" " +resultList[i]+" ("+letterList[i]+")"))
        for i in (self.displayList):
            i.pack()
        self.count += 1

if __name__ == "__main__":
    app = Window()
    app.mainloop()
