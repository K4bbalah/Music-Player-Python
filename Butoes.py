from tkinter import*
import awesometkinter as atk
import PIL._tkinter_finder





class ButõesPlayer():

    Keyboard_On=0
    def butão(self):
    
        self.b1=atk.Button3d(self.frame_2,bg="#dde",image=self.play1,command=self.Start)
        self.b1.place(x=168,y=100,width=50,height=40)
        self.root.bind('<Return>',lambda event:self.Start())
        self.root.bind('<KeyPress-Return>')
        self.b2=atk.Button3d(self.frame_2,bg="#dde",image=self.next1,command=self.Avançar)
        self.b2.place(x=228,y=100,width=50,height=40)
        self.root.bind('<Right>',lambda event:self.Avançar())
        self.b3=atk.Button3d(self.frame_2,bg="#dde",image=self.voltar1,command=self.Voltar)
        self.b3.place(x=108,y=100,width=50,height=40)
        self.root.bind('<Left>',lambda event:self.Voltar())
        self.b4=atk.Button3d(self.frame_2,bg="#dde",image=self.mais1,command=self.VolMais)
        self.b4.place(x=336,y=20,width=50,height=40)
        self.root.bind('<Up>',lambda event:self.VolMais())
        self.b5=atk.Button3d(self.frame_2,bg="#dde",image=self.menos1,command=self.VolMenos)
        self.b5.place(x=336,y=70,width=50,height=40)
        self.root.bind('<Down>',lambda event:self.VolMenos())
       

        self.b6=atk.Button3d(self.frame_2,bg="#dde",image=self.continuar1,command=self.Continuar)
        self.b6.place(x=198,y=28,width=50,height=40)
        self.b7=atk.Button3d(self.frame_2,bg="#dde",image=self.pausar1,command=self.Pausar)
        self.b7.place(x=138,y=28,width=50,height=40)
        self.b8=atk.Button3d(self.frame_2,bg="#dde",image=self.stop1,command=self.Stop_music)
        self.b8.place(x=2,y=20,width=50,height=40)
        self.root.bind('<Escape>',lambda event:self.Stop_music())
        self.b9=atk.Button3d(self.frame_2,bg="#dde",image=self.auto1,command=self.Auto_loop)
        self.b9.place(x=2,y=70,width=50,height=40)
        self.root.bind('<A>',lambda event:self.Auto_loop())
        self.root.bind('<a>',lambda event:self.Auto_loop())

        self.root.bind('<p>',lambda event:self.Stop_Space())
        self.root.bind('<P>',lambda event:self.Stop_Space())


    # Parar Com a tecla espaço
    def Stop_Space(self):
        if self.Keyboard_On==0:
            self.Pausar()
        
        else:
            self.Continuar()

    
           


        
        
        