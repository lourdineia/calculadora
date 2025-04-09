# importando tkinter
from tkinter import *
from tkinter import ttk

#cores 
cor1="#f542e3"  #rosa
cor2="#fafafa"   #branca
cor3="#1040de"   #azul
cor4="#9c9591"   #cinza
cor5="#fa660a"   #laranja


janela= Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# criando frames 

frame_tela= Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo= Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

txtvalor=StringVar()
valor=''

# def é utilizado para criar uma função: def nome_da_função(parametros-da-função)
def insereValor(valor_entrada):
    global valor
    valor= valor + str(valor_entrada)
    txtvalor.set(valor)

def limpa_tela():
    global valor
    valor=''
    txtvalor.set('')   
def calcular():
    global valor
    resultado= eval(valor)    # transforma a string(texto) em numero e realiza o calculo
    txtvalor.set(str(resultado))
    valor= str(resultado)

# criando label
app_label= Label(frame_tela, textvariable=txtvalor, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 17 bold"), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)



#criando botoes

b1= Button( frame_corpo, command=lambda: limpa_tela(), text="C", width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2= Button( frame_corpo,command=lambda: insereValor('%'),  text="%", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3= Button( frame_corpo,command=lambda: insereValor('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

b4= Button( frame_corpo, command=lambda: insereValor('7'), text="7", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5= Button( frame_corpo,command=lambda: insereValor('8') , text="8", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6= Button( frame_corpo,command=lambda: insereValor('9'), text="9", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7= Button( frame_corpo,command=lambda: insereValor('*') , text="*", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)
b8= Button( frame_corpo,command=lambda: insereValor('4')  ,text="4", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9= Button( frame_corpo,command=lambda: insereValor('5')  ,text="5", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10= Button( frame_corpo,command=lambda: insereValor('6')  ,text="6", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11= Button( frame_corpo,command=lambda: insereValor('-')  ,text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)
b12= Button( frame_corpo,command=lambda: insereValor('1')  ,text="1", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13= Button( frame_corpo,command=lambda: insereValor('2')  ,text="2", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14= Button( frame_corpo,command=lambda: insereValor('3')  ,text="3", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15= Button( frame_corpo,command=lambda: insereValor('+')  ,text="+", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)

b16= Button( frame_corpo,command=lambda: insereValor('0')  ,text="0", width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17= Button( frame_corpo,command=lambda: insereValor('.')  ,text=".", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18= Button( frame_corpo,command=lambda: calcular(), text="=", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)

# criando funções





janela.mainloop()
