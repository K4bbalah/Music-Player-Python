from  Display import*
import os
import pygame 




class Mp3Player(DisplayPlayer):

    if not os.path.exists('./musicas'):
        os.makedirs('./musicas')
    
    if not os.path.exists('./imagens'):
        os.makedirs('./imagens')

    local1='./musicas'
    local2='./imagens'
    imgalbum=os.listdir(local2)
    musica=os.listdir(local1)
  
    av=0
    img=1
  
    v=0.5
    vol=5
    m=musica
    N_musicas=len(musica)
    agoravai=N_musicas-1
    logica=0
    stopp=None
    git=0
    auto=0
    Trava=0
    TravaDOStop=0
   


    def __init__(self):
        self.root=Tk()
        self.imagens_codificadas()
        self.Tela()
        self.root.title("Music Player")
        self.root.geometry("400x500")
        self.root.mainloop()
    
   

    def Avançar(self):
        if self.TravaDOStop==1:
            pass
        else:
            if self.av<self.agoravai:
                self.contador_master=0
                self.Trava=0
                self.Keyboard_On=0
                self.contador=380
                self.Stop_Autoimg()
                self.Auto_image()
           
                self.Stop_Timem()
                self.segundos1=0
                self.segundos=0
                self.minuto=0
                self.Loop_Time()
                self.av+=1
                self.img1=PhotoImage(file="./imagens/"+self.imgalbum[self.av])
                self.gif_label.configure(image=self.img1)
             
             
                self.music1=self.m[self.av]
                self.ss.configure(text=self.music1)
                pygame.mixer.music.load("./musicas/"+self.music1)
                pygame.mixer.music.play()
                self.logica=1
          
        
    

        
    
    def Voltar(self):
        if self.TravaDOStop==1:
            pass
        else:
            if self.av>0:
                self.contador_master=0
                self.contador=380
                self.Trava=0
                self.Keyboard_On=0
                self.Stop_Autoimg()
                self.Auto_image()
                self.Stop_Timem()
                self.segundos1=0
                self.segundos=0
                self.minuto=0
                self.Loop_Time()
                self.av-=1
                self.img1=PhotoImage(file="./imagens/"+self.imgalbum[self.av])
                self.gif_label.configure(image=self.img1)
            
                self.music1=self.m[self.av]
                self.ss.configure(text=self.music1)
                pygame.mixer.music.load("./musicas/"+self.music1)
                pygame.mixer.music.play()
                self.logica=1

    def Continuar(self):
        if self.TravaDOStop==1:
            pass
        else:
            if self.Trava==0:
                self.Keyboard_On=0
                pygame.mixer.music.unpause()
        
                self.logica=1
                self.Stop_Timem()
                self.Loop_Time()
                self.Stop_Autoimg()
                self.Auto_image()

    def Pausar(self):
        if self.TravaDOStop==1:
            pass
        else:
            if self.Trava==0:
                self.Keyboard_On=1
                pygame.mixer.music.pause()
                self.Stop_Timem()
                self.Stop_Autoimg()

    def Stop_music(self):
        self.contador_master=0
        self.Keyboard_On=0
        self.TravaDOStop=1
        self.Time_Musica()

        self.Stop_Timem()
        self.label()
        self.logica=0
        self.Stop_Autoimg()
        pygame.quit()

        self.ss.place(width=380)
        self.contador=380
        if self.auto==1:
            self.auto=0
            self.stop_loop()
            self.Auto_ledstop()
            self.automatico.configure(text="")




    def Start(self):
        if self.Keyboard_On==1:
            self.Stop_Autoimg()
       
            self.Keyboard_On=0
            pygame.mixer.music.unpause()

            self.Stop_Timem()
            self.Loop_Time()
            self.Auto_image()
            

        else:
            self.TravaDOStop=0
            pygame.init()
            pygame.mixer.init(44100)
           
            self.contador_master=0
            self.Trava=0
            self.Keyboard_On=0
            self.music1=self.m[self.av]
            pygame.mixer.music.load("./musicas/"+self.music1)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(self.v)
            self.segundos1=0
            self.segundos=0
            self.minuto=0
            self.minuto1=0
            self.contador=380
            if self.logica<1:
         
                self.logica=1
                self.EndMusic()
                self.Auto_image()
                self.Loop_Time()
    '''Quando o modo automatico esta desligado executa isso'''
    
    def EndMusic(self):
      
        self.musica_end=pygame.USEREVENT+1
        pygame.mixer.music.set_endevent(self.musica_end)
        for event in pygame.event.get():
            if event.type == self.musica_end:
                if self.av<=self.agoravai:
                    self.Trava=1
                    
        
                    self.logica=0
                    self.end_musica()
                    self.Stop_Autoimg()
                    self.Time_Musica()
                    
                    self.Stop_Timem()
                    
                   
        self.PararMusica=self.root.after(1000,self.EndMusic)
    
    def end_musica(self):
        self.root.after_cancel(self.PararMusica)

    '''  quando o Modo automatico esta ligado executa isso'''     
    def Auto_loop(self):
        if self.TravaDOStop==1:
            pass
        else:
            if self.auto==0:
                pygame.init()
                self.end_musica()
                self.loop()
                self.auto=1
                self.Auto_led()
            else:
                self.auto=0
                self.Auto_ledstop()
                self.automatico.configure(text="")
                self.stop_loop()
                self.EndMusic()


   



   

        

    ''' O loop que executado quando o modo automatico esta ligado'''
    
    
    def loop(self):
        self.musica_end=pygame.USEREVENT+1
        pygame.mixer.music.set_endevent(self.musica_end)
        for event in pygame.event.get():
            if event.type == self.musica_end:
                if self.av<self.agoravai:
                    self.av+=1
                    self.img1=PhotoImage(file="./imagens/"+self.imgalbum[self.av])
                    self.gif_label.configure(image=self.img1)
                   
                    self.music1=self.m[self.av]
                    self.ss.configure(text=self.music1)
                    pygame.mixer.music.load("./musicas/"+self.music1)
                    pygame.mixer.music.play()
                    self.Stop_Timem()
                    self.segundos1=0
                    self.segundos=0
                    self.minuto=0
                    
    
                    self.Loop_Time()
                  
                    
                else:
                  
                   
                    self.logica=0
                    self.Stop_Autoimg()
                    self.Stop_Timem()
                    self.segundos1=0
                    self.segundos=0
                    self.minuto=0
                    self.minuto1=0
                    self.Trava=1
    

        self.stopp=self.root.after(1000,self.loop)
    def stop_loop(self):
        self.root.after_cancel(self.stopp)



    


    ''' >>>>>>>> Confiuração do VOlume: <<<<<<<<<<<<< '''
    def VolMais(self):
        if self.TravaDOStop==1:
            pass
        else:
            if self.vol<10:
                self.vol+=1
                self.vv.configure(text=self.vol)
            if self.v<0.9:
                self.v+=0.1
                pygame.mixer.music.set_volume(self.v)
        
    
    
    
    def VolMenos(self):
        if self.TravaDOStop==1:
            pass
        else:
            if self.vol>0:
                self.vol-=1
                self.vv.configure(text=self.vol)
            if self.v>0:
                self.v-=0.1
                pygame.mixer.music.set_volume(self.v)


    
    
    

    
Mp3Player()