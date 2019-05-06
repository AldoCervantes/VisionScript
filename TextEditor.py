from tkinter import *
from gtts import gTTS
import contextlib
with contextlib.redirect_stdout(None):
    from pygame import mixer
import os
import mmap

#text to speech function
def TextToSpeech():
    toBraille = codeArea.get("1.0",'end-1c')
    intab = ' ⠮⠼⠫⠩⠯⠄⠷⠾⠡⠬⠠⠤⠨⠌⠴⠂⠆⠒⠲⠢⠖⠶⠦⠔⠱⠰⠣⠿⠜⠹⠈⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵⠪⠳⠻⠘⠸⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
    outtab = ' !#$%&"()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz'
    transtab = str.maketrans(intab, outtab)
    toSpeech = toBraille.translate(transtab)
    
    tts = gTTS(text= toSpeech, lang='es')
    tts.save('speech.mp3')

    with open('speech.mp3') as f: 
        PlayedMp3File = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) 

    mixer.init()
    mixer.music.load(PlayedMp3File)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue
    PlayedMp3File.close()
    mixer.quit()
    
    if os.path.exists('speech.mp3'):
        os.remove('speech.mp3')

#text to braille function
def TextToBraille():
    toBraille = codeArea.get("1.0",'end-1c')
    intab = ' !#$%&"()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz'
    outtab = ' ⠮⠼⠫⠩⠯⠄⠷⠾⠡⠬⠠⠤⠨⠌⠴⠂⠆⠒⠲⠢⠖⠶⠦⠔⠱⠰⠣⠿⠜⠹⠈⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵⠪⠳⠻⠘⠸⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
    transtab = str.maketrans(intab, outtab)
    result = toBraille.translate(transtab)
    print(result)

#braille to text function
def BrailleToText():
    toBraille = codeArea.get("1.0",'end-1c')
    intab = ' ⠮⠼⠫⠩⠯⠄⠷⠾⠡⠬⠠⠤⠨⠌⠴⠂⠆⠒⠲⠢⠖⠶⠦⠔⠱⠰⠣⠿⠜⠹⠈⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵⠪⠳⠻⠘⠸⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
    outtab = ' !#$%&"()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz'
    transtab = str.maketrans(intab, outtab)
    result = toBraille.translate(transtab)
    print(result)
    
#text to braille function
def SaveFile():
    text = codeArea.get("1.0",'end-1c')
    file_name = 'VisionScriptCode.vs'
    f = open(file_name, 'w')
    f.write(text)
    f.close()
    print("se ejecuto")


#define root
root = Tk(className = " VisionScript Beta")
root.resizable(False, False)

#define code area
codeArea = Text(root, height=30)
codeArea.configure(background='white')
codeArea.pack()

#define console area
console = Text(root, height=15)
console.configure(background='black',foreground="green")

#define icon images
play=PhotoImage(file="play.png")
braille=PhotoImage(file="braille.png")
hear=PhotoImage(file="hear.png")
text=PhotoImage(file="text.png")

#define play button
playButton = Button(root)
playButton.place(x=0,y=400)
playButton.config(image=play,width="50",height="57",command=SaveFile)

#define braille button
brailleButton = Button(root)
brailleButton.place(x=411,y=400)
brailleButton.config(image=braille,width="52",height="57",command=TextToBraille)

#define hear button
hearButton = Button(root)
hearButton.place(x=461,y=400)
hearButton.config(image=hear,width="52",height="57",command=TextToSpeech)

#define text button
textButton = Button(root)
textButton.place(x=511,y=400)
textButton.config(image=text,width="52",height="57",command=BrailleToText)

console.pack()
root.mainloop()
