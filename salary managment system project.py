from tkinter import *
class emloyeesystem :
    def __init__(self,root):
        self.root=root
        self.root.title("employee payroll managment system | devloped by nilesh|webcode")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Emloyee Payroll Managment System", font=("time new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

         #==================== frame 1==========

        self.var_emp_code=StringVar()
        self.var_Designation=StringVar()
        self.var_Name=StringVar()
        self.var_Age=StringVar()
        self.var_Gender=StringVar()
        self.var_Email=StringVar()
        self.var_Hired_location=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_Experience= StringVar()
        self.var_proof_id = StringVar()
        self.var_contact = StringVar()
        self.var_status=StringVar()




        Flame1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Flame1.place(x=10,y=70,width=750,height=620)

        title2=Label(Flame1,text="Emloyee details", font=("time new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        # lb1_code=Label(Flame1,text="Emloyee code", font=("time new roman",20),bg="white",fg="black",).place(x=10,y=70)

        lb1_code=Label(Flame1,text="Emloyee details", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=70)
        txt_code=Entry(Flame1, font=("time new roman",15),textvariable=self.var_emp_code,  bg="lightyellow",fg="black",).place(x=170,y=74,width=200)
        btn_search=Button(Flame1,text="search",font=('time new roman',17),bg='gray',fg='black').place(x=390,y=72,height=30)

 #========= ROW 1===========

        lb1_Designation=Label(Flame1,text="Designation", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=120)
        txt_designation=Entry(Flame1, font=("time new roman",15),textvariable=self.var_Designation ,bg="lightyellow",fg="black",).place(x=170,y=125,width=200)

        lb1_DOB=Label(Flame1,text="D.O.B", font=("time new roman",17),bg="white",fg="black",).place(x=390,y=120)
        txt_DOB=Entry(Flame1, font=("time new roman",15),textvariable=self.var_DOB,bg="lightyellow",fg="black",).place(x=510,y=125)

        # ========= ROW 2===========

        lb1_NAME=Label(Flame1,text="NAME", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=170)
        txt_NAME=Entry(Flame1, font=("time new roman",15),textvariable=self.var_Name,bg="lightyellow",fg="black",).place(x=170,y=175,width=200)

        lb1_DOJ=Label(Flame1,text="D.O.J", font=("time new roman",17),bg="white",fg="black",).place(x=390,y=170)
        txt_DOJ=Entry(Flame1, font=("time new roman",15),textvariable=self.var_DOJ,bg="lightyellow",fg="black",).place(x=510,y=175)

        # ========= ROW 3===========

        lb1_Age=Label(Flame1,text="Age", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=220)
        txt_Age=Entry(Flame1, font=("time new roman",15),textvariable=self.var_Age,bg="lightyellow",fg="black",).place(x=170,y=225,width=200)

        lb1_Experience=Label(Flame1,text="Experience", font=("time new roman",17),bg="white",fg="black",).place(x=390,y=220)
        txt_Experience=Entry(Flame1, font=("time new roman",15),textvariable=self.var_Experience,bg="lightyellow",fg="black",).place(x=510,y=225)

        # ========= ROW 4===========

        lb1_Gender=Label(Flame1,text="Gender", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=270)
        txt_Gender=Entry(Flame1, font=("time new roman",15),textvariable=self.var_Gender,bg="lightyellow",fg="black",).place(x=170,y=275,width=200)

        lb1_proof_id =Label(Flame1,text="Proof ID", font=("time new roman",17),bg="white",fg="black",).place(x=390,y=270)
        txt_proof_id=Entry(Flame1, font=("time new roman",15),textvariable=self.var_proof_id,bg="lightyellow",fg="black",).place(x=510,y=275)

        # ========= ROW 5===========
        lb1_Email=Label(Flame1,text="Email", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=320)
        txt_Email=Entry(Flame1, font=("time new roman",15),textvariable=self.var_Email,bg="lightyellow",fg="black",).place(x=170,y=325,width=200)

        lb1_contact =Label(Flame1,text="Contact", font=("time new roman",17),bg="white",fg="black",).place(x=390,y=320)
        txt_contact=Entry(Flame1, font=("time new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black",).place(x=510,y=325)

        # ========= ROW 6===========

        lb1_Hired=Label(Flame1,text="Hired location", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=370)
        txt_hired=Entry(Flame1, font=("time new roman",15),textvariable=self.var_Hired_location,bg="lightyellow",fg="black",).place(x=170,y=375,width=200)

        lb1_status =Label(Flame1,text="status", font=("time new roman",17),bg="white",fg="black",).place(x=390,y=370)
        txt_status=Entry(Flame1, font=("time new roman",15),textvariable=self.var_status,bg="lightyellow",fg="black",).place(x=510,y=375)

        # ========= ROW 7===========

        lb1_Address=Label(Flame1,text="Address", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=420)
        self.txt_Address=Text(Flame1, font=("time new roman",15),bg="lightyellow",fg="black",)
        self.txt_Address.place(x=170,y=425,width=550,height=130)


        # ==================== frame 2==========
        Flame2=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Flame2.place(x=770,y=70,width=560,height=300)


        self.var_Month=StringVar()
        self.var_Year=StringVar()
        self.var_Salary=StringVar()
        self.var_Days=StringVar()
        self.var_Absent=StringVar()
        self.var_Medical=StringVar()
        self.var_PF=StringVar()
        self.var_Convence=StringVar()
        self.var_Net_salary=StringVar()

        title3=Label(Flame2,text="Emloyee Salary details", font=("time new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lb1_Month=Label(Flame2,text="Month", font=("time new roman",15),bg="white",fg="black",).place(x=10,y=60)
        txt_Month=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Month,bg="lightyellow",fg="black",).place(x=90,y=58,width=100)

        lb1_year=Label(Flame2,text="Year", font=("time new roman",15),bg="white",fg="black",).place(x=200,y=60)
        txt_year=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Year,bg="lightyellow",fg="black",).place(x=260,y=58,width=100)

        lb1_Salary=Label(Flame2,text="Salary", font=("time new roman",15),bg="white",fg="black",).place(x=360,y=60)
        txt_Salary=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Salary,bg="lightyellow",fg="black",).place(x=430,y=58,width=100)



        lb1_Days=Label(Flame2,text="Days", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=120)
        txt_Days=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Days,bg="lightyellow",fg="black",).place(x=130,y=125,width=100)

        lb1_absent=Label(Flame2,text="Absent", font=("time new roman",17),bg="white",fg="black",).place(x=270,y=120)
        txt_absent=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Absent,bg="lightyellow",fg="black",).place(x=380,y=125,width=100)

        # ========= ROW 2===========

        lb1_Medical=Label(Flame2,text="Medical", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=150)
        txt_Medical=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Medical,bg="lightyellow",fg="black",).place(x=130,y=155,width=100)

        lb1_PF=Label(Flame2,text="PF", font=("time new roman",17),bg="white",fg="black",).place(x=270,y=150)
        txt_PF=Entry(Flame2, font=("time new roman",15),textvariable=self.var_PF,bg="lightyellow",fg="black",).place(x=380,y=155,width=100)

        lb1_Convence=Label(Flame2,text="Convence", font=("time new roman",17),bg="white",fg="black",).place(x=10,y=180)
        txt_Convence=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Convence,bg="lightyellow",fg="black",).place(x=130,y=185,width=100)

        lb1_netsalary=Label(Flame2,text="Net salary", font=("time new roman",17),bg="white",fg="black",).place(x=270,y=180)
        txt_netsalary=Entry(Flame2, font=("time new roman",15),textvariable=self.var_Net_salary,bg="lightyellow",fg="black",).place(x=380,y=185,width=100)

        btn_calculate=Button(Flame2,text="calculate",command=self.calculate,font=('time new roman',17),bg='red',fg='black').place(x=130,y=240,height=30,width=120)
        btn_save=Button(Flame2,text="save",font=('time new roman',17),bg='green',fg='black').place(x=260,y=240,height=30,width=120)
        btn_clear=Button(Flame2,text="clear",font=('time new roman',17),bg='grey',fg='black').place(x=400,y=240,height=30,width=120)

        Flame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Flame3.place(x=770,y=380,width=550,height=290)
  #========== calculater============

        cal_Frame=Frame(Flame3,bg="white",bd=2)
        cal_Frame.place(x=2,y=2,width=248,height=400)


        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=""


        def clear_cal():
            self.var_txt.set(" ")
            self.var_operator = ""


        txt_result=Entry(cal_Frame,bg="lightyellow",textvariable=self.var_txt, font=("time to roman",15,'bold'),justify=RIGHT).place(x=0,y=0,relwidth=1,height=40)
        btn_7=Button(cal_Frame,text='7',command=lambda:btn_click(7), font=("times new roman",15,"bold")).place(x=0,y=40,w=60,h=55)
        btn_8=Button(cal_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=40,w=60,h=55)
        btn_9=Button(cal_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=40,w=60,h=55)
        btn_DIV=Button(cal_Frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=183,y=40,w=60,h=55)

        btn_4 = Button(cal_Frame, text='4',command=lambda:btn_click(4), font=("times new roman", 15, "bold")).place(x=0, y=90, w=60, h=55)
        btn_5 = Button(cal_Frame, text='5',command=lambda:btn_click(5), font=("times new roman", 15, "bold")).place(x=61, y=90, w=60, h=55)
        btn_6 = Button(cal_Frame, text='6',command=lambda:btn_click(6), font=("times new roman", 15, "bold")).place(x=122, y=90, w=60, h=55)
        btn_MUL = Button(cal_Frame, text='*',command=lambda:btn_click("*"), font=("times new roman", 15, "bold")).place(x=183, y=90, w=60, h=55)

        btn_3= Button(cal_Frame, text='3', command=lambda:btn_click(3),font=("times new roman", 15, "bold")).place(x=0, y=140, w=60, h=55)
        btn_2 = Button(cal_Frame, text='2',command=lambda:btn_click(2), font=("times new roman", 15, "bold")).place(x=61, y=140, w=60, h=55)
        btn_1 = Button(cal_Frame, text='1', command=lambda:btn_click(1),font=("times new roman", 15, "bold")).place(x=122, y=140, w=60, h=55)
        btn_MIN = Button(cal_Frame, text='-',command=lambda:btn_click("-"), font=("times new roman", 15, "bold")).place(x=183, y=140, w=60, h=55)

        btn_0 = Button(cal_Frame, text='0',command=lambda:btn_click(0), font=("times new roman", 15, "bold")).place(x=0, y=190, w=60, h=55)
        btn_dot = Button(cal_Frame, text='c',command=clear_cal, font=("times new roman", 15, "bold")).place(x=61, y=190, w=60, h=55)
        btn_sum = Button(cal_Frame, text='+', command=lambda:btn_click("+"),font=("times new roman", 15, "bold")).place(x=122, y=190, w=60, h=55)
        btn_equal = Button(cal_Frame, text='=',command=result, font=("times new roman", 15, "bold")).place(x=183, y=190, w=60, h=55)


        sal_Frame=Frame(Flame3,bg="white",bd=2)
        sal_Frame.place(x=252,y=2,width=258,height=400)
        title_sal=Label(sal_Frame,text="salary reciept", font=("time new roman",20,"bold"),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)


        sal_Frame2=Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=35,relwidth=1,height=190)

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept=Text(sal_Frame2,font=('time to roman',15),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview())

        btn_print=Button(sal_Frame,text="print",font=('time new roman',17),bg='blue',fg='black').place(x=150,y=227,height=30,width=120)

    def calculate(self):
        print(self.var_emp_code.get(),
        self.var_Designation.get(),
        self.var_Name.get(),
        self.var_Age.get(),
        self.var_Gender.get(),
        self.var_Email.get(),
        self.var_Hired_location.get(),
        self.var_DOB.get(),
        self.var_DOJ.get(),
        self.var_Experience.get(),
        self.var_proof_id.get(),
        self.var_contact.get(),
        self.var_status.get(),
        self.var_status.get(),
        self.var_status.get(),
        self.var_Month.get(),
        self.var_Year .get(),
        self.var_Salary.get(),
        self.var_Days .get(),
        self.var_Absent.get(),
        self.var_Medical.get(),
        self.var_PF.get(),
        self.var_Convence.get(),
        self.var_Net_salary.get(),
        self.txt_Address.get("1.0",END)
        )

root=Tk()
obj=emloyeesystem(root)
root=mainloop()




