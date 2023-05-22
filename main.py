from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from rembg import remove
from PIL import Image
root = Tk()
root.geometry("500x300")
root.title("Remove-Bg")
root.config(bg = "light yellow")
filename=""

output_file = ""
def Upload():
    global filename
    global output_file
    f_types = filetypes = (("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"),("All Files", "*.*"))
    filename = filedialog.askopenfilename(multiple=True,filetypes=f_types)
    Label(root,text = filename[0],font = ('Times New Roman',10,'bold'),anchor=CENTER,bg='light yellow',fg='blue').place(x=40,y=200)
    #print(filename)
    lst = filename[0]
    fname = lst.split('/')
    output_file = "Remove_bg_"+fname[-1]
def Remove():
    try:
        print("removing....")
        image = Image.open(filename[0])
        #output.save(output_file)
        #image = Image.open("image.png")  # Replace with your image path
        output = remove(image)
        rgb_image = output.convert("RGB")
        rgb_image.save(output_file, "JPEG")
        print("Image saved at working directory with ",output_file)
        output = Image.open(output_file)
        output.show()
    except Exception as e:
        print(e)
        #break
Label(root,text = "Remove Background",font = ('Times New Roman',40,'bold'),anchor = CENTER,
      bg = "wheat2",fg = "blue",width = 30).pack()
Label(root,text = "Upload Image:",font = ('Times New Roman',15,'bold'),anchor=CENTER,bg='light yellow',fg='black').place(x=200,y=100)
B = Button(root, text ="Upload",font = ('Calibri',12,"bold"),activebackground="sky blue",cursor = "hand2",relief = GROOVE,
           bg = "light green",fg = "black",width=12,height = 1,command = Upload)
B.place(x = 200,y=150)

B = Button(root, text ="Remove",font = ('Calibri',12,"bold"),activebackground="sky blue",cursor = "hand2",relief = GROOVE,
           bg = "green",fg = "white",width=12,height = 1,command = Remove)
B.place(x = 200,y=250)
