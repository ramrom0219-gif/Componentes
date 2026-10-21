from tkinter import *
import subprocess, json

vent = Tk()
vent.geometry("500x500")

out = subprocess.getoutput("powershell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName | ConvertTo-Json}\"")

el= Label(vent, text= "Estado", font=('Helvatica', 10,'bold'))
el.grid(row=0,column=0,padx=5,pady=5)

el= Label(vent, text= "Clase", font=('Helvatica', 10,'bold'))
el.grid(row=0,column=1,padx=5,pady=5)

el= Label(vent, text= "Nombre Descriptivo", font=('Helvatica', 10,'bold'))
el.grid(row=0,column=2,padx=5,pady=5)

count =1
json_data = json.loads(out)

for dev in json_data:
    if count<=27:
        lst=[[dev['Status'], dev['Class'], dev['FriendlyName']]]
        print(lst)
        total_rows= len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):

                e = Entry(vent,width=35,fg='blue',font=('A  rial',10,('bold')))
                e.grid(row=count, column=j, ipadx=5,ipady=5, columnspan=2)
                e.insert(END, lst[i][j])

        count=count+1


vent.mainloop()