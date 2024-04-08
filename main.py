from tkinter import *
from tkinter import messagebox
import random,os, tempfile, smtplib

if not os.path.exists('bills'):
    os.mkdir('bills')

def bill_save():
    global billnumber
    result = messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0,END)
        file = open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==BillEntry.get():
            f = open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid bill number')

def bill_print():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def send_email():
    def send_gmail():
        #to establish the connection and send the mail when clicking on send button
        ob=smtplib.SMTP('smtp.gmail.com',587)
        ob.starttls()
        ob.login(gmailidLabelentry.get(),passwordentry.get())
        message = emailtext_area.get(1.0,END)
        ob.sendmail(gmailidLabelentry.get(),receiveremailentry.get(),message)
        ob.quit()
        messagebox.showinfo('Success','Bill is successfully sent')
        root1.destroy()

    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send email')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        
        #Sender details
        senderFrame = LabelFrame(root1,text='Sender',font=('arial',16,'bold'),bd=6,bg='gray20', fg='white')
        senderFrame.pack(fill=X)
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        gmailidLabel = Label(senderFrame,text="Email",font=('arial',14,'bold'),bg='gray20', fg='white')
        gmailidLabel.grid(row=0,column=0,padx=10,pady=8)

        gmailidLabelentry =Entry(senderFrame,font=('arial',14,'bold'),bd=2, width=23, relief=RIDGE)
        gmailidLabelentry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20', fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordentry =Entry(senderFrame,font=('arial',14,'bold'),bd=2, width=23, relief=RIDGE,show='*')
        passwordentry.grid(row=1,column=1,padx=10,pady=8)

        #Recipent details
        RecipentFrame = LabelFrame(root1,text='Recipent',font=('arial',16,'bold'),bd=6,bg='gray20', fg='white')
        RecipentFrame.grid(row=1,column=0,padx=40,pady=20)

        receiveremailLabel = Label(RecipentFrame,text="Receiver's Email",font=('arial',14,'bold'),bg='gray20', fg='white')
        receiveremailLabel.grid(row=0,column=0,padx=10,pady=8)

        receiveremailentry =Entry(RecipentFrame,font=('arial',14,'bold'),bd=2, width=23, relief=RIDGE)
        receiveremailentry.grid(row=0,column=1,padx=10,pady=8)

        receivermessageLabel = Label(RecipentFrame,text="Message",font=('arial',14,'bold'),bg='gray20', fg='white')
        receivermessageLabel.grid(row=1,column=0,padx=10,pady=8)

        emailtext_area = Text(RecipentFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        emailtext_area.grid(row=2,column=0,columnspan=2)
        emailtext_area.delete(1.0,END)
        emailtext_area.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendbutton = Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)
        root1.mainloop()

def clear():
    Hair_cutEntry.delete(0,END)
    Hair_cutEntry.insert(0,0)

    WaxingEntry.delete(0,END)
    WaxingEntry.insert(0,0)

    HairwashEntry.delete(0,END)
    HairwashEntry.insert(0,0)

    FacialEntry.delete(0,END)
    FacialEntry.insert(0,0)

    FacebleachEntry.delete(0,END)
    FacebleachEntry.insert(0,0)

    HairspaEntry.delete(0,END)
    HairspaEntry.insert(0,0)

    MedicureEntry.delete(0,END)
    MedicureEntry.insert(0,0)

    PedicureEntry.delete(0,END)
    PedicureEntry.insert(0,0)

    MassageEntry.delete(0,END)
    MassageEntry.insert(0,0)

    EyebrowEntry.delete(0,END)
    EyebrowEntry.insert(0,0)

    HaircolourEntry.delete(0,END)
    HaircolourEntry.insert(0,0)

    MakeupEntry.delete(0,END)
    MakeupEntry.insert(0,0)

    LorealEntry.delete(0,END)
    LorealEntry.insert(0,0)

    DoveEntry.delete(0,END)
    DoveEntry.insert(0,0)

    PanteneEntry.delete(0,END)
    PanteneEntry.insert(0,0)

    VLCCEntry.delete(0,END)
    VLCCEntry.insert(0,0)

    SunsilkEntry.delete(0,END)
    SunsilkEntry.insert(0,0)

    ClinicplusEntry.delete(0,END)
    ClinicplusEntry.insert(0,0)

    TotalProductPriceEntry.delete(0,END)
    ServicePriceEntry.delete(0, END)
    TotalServicePriceEntry.delete(0,END)
    OtherServicePriceEntry.delete(0,END)
    nameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    AddEntry.delete(0,END)
    textarea.delete(1.0,END)
        


billnumber=random.randint(500,1000)




#Create the functionality
def validate_input(new_value):
    if new_value.isdigit() and len(new_value) <= 10:
        return True
    elif new_value == "":
        return True
    else:
        return False
    
def bill():    
    if nameEntry.get() == '' or PhoneEntry.get() == '' or AddEntry.get() == '':
        messagebox.showerror('Error','Customer Details are required')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t\t\t***XYZ Saloon***\n\t\t\t\t   ***India***\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\nPhone Number: {PhoneEntry.get()}\n')
        textarea.insert(END,f'\nAddress: {AddEntry.get()}')
        textarea.insert(END,'\n--------------------------------------------------------------------------------')
        textarea.insert(END,'Service\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n================================================================================')
        if Hair_cutEntry.get()!='0':
            textarea.insert(END,f'\nHair Cut\t\t\t{Hair_cutEntry.get()}\t\t\tRs {hair_cutservice_price}')
        if WaxingEntry.get()!='0':
            textarea.insert(END,f'\nWaxing\t\t\t{WaxingEntry.get()}\t\t\tRs {WaxingEntryservice_price}')
        if HairwashEntry.get()!='0':
            textarea.insert(END,f'\nHair Wash\t\t\t{HairwashEntry.get()}\t\t\tRs {HairwashEntryservice_price}')
        if FacialEntry.get()!='0':
            textarea.insert(END,f'\nFacial\t\t\t{FacialEntry.get()}\t\t\tRs {FacialEntryservice_price}')
        if FacebleachEntry.get()!='0':
            textarea.insert(END,f'\nFace Bleach\t\t\t{FacebleachEntry.get()}\t\t\tRs {FacebleachEntryservice_price}')
        if HairspaEntry.get()!='0':
            textarea.insert(END,f'\nHair Spa\t\t\t{HairspaEntry.get()}\t\t\tRs {HairspaEntryservice_price}')
        if MedicureEntry.get()!='0':
            textarea.insert(END,f'\nMedicure\t\t\t{MedicureEntry.get()}\t\t\tRs {MedicureEntryservice_price}')
        if PedicureEntry.get()!='0':
            textarea.insert(END,f'\nPedicure\t\t\t{PedicureEntry.get()}\t\t\tRs {PedicureEntryservice_price}')    
        if MassageEntry.get()!='0':
            textarea.insert(END,f'\nMassage\t\t\t{MassageEntry.get()}\t\t\tRs {MassageEntryservice_price}')       
        if EyebrowEntry.get()!='0':
            textarea.insert(END,f'\nEyebrow\t\t\t{EyebrowEntry.get()}\t\t\tRs {EyebrowEntryservice_price}')   
        if HaircolourEntry.get()!='0':
            textarea.insert(END,f'\nHair Colour\t\t\t{HaircolourEntry.get()}\t\t\tRs {HaircolourEntryservice_price}')   
        if MakeupEntry.get()!='0':
            textarea.insert(END,f'\nMakeup\t\t\t{MakeupEntry.get()}\t\t\tRs {MakeupEntryservice_price}')   
        if  LorealEntry.get()!='0':
            textarea.insert(END,f'\nLoreal Shampoo\t\t\t{LorealEntry.get()}\t\t\tRs {LorealEntry_price}')
        if  DoveEntry.get()!='0':
            textarea.insert(END,f'\nDove Shampoo\t\t\t{DoveEntry.get()}\t\t\tRs {DoveEntry_price}')     
        if  PanteneEntry.get()!='0':
            textarea.insert(END,f'\nPantene Shampoo\t\t\t{PanteneEntry.get()}\t\t\tRs {PanteneEntry_price}')         
        if  VLCCEntry.get()!='0':
            textarea.insert(END,f'\nVLCC Shampoo\t\t\t{VLCCEntry.get()}\t\t\tRs {VLCCEntry_price}') 
        if  SunsilkEntry.get()!='0':
            textarea.insert(END,f'\nSunsilk Shampoo\t\t\t{SunsilkEntry.get()}\t\t\tRs {SunsilkEntry_price}')     
        if  ClinicplusEntry.get()!='0':
            textarea.insert(END,f'\nClinic Plus Shampoo\t\t\t{ClinicplusEntry.get()}\t\t\tRs {ClinicplusEntry_price}')  
        textarea.insert(END,f'\nOther Service\t\t\t\t\t\tRs {OtherServicePriceEntry.get()}') 
        textarea.insert(END,'\n--------------------------------------------------------------------------------')
        textarea.insert(END,f'\nGST\t\t\t\t\t\t10%') 
        textarea.insert(END,f'\nCGST\t\t\t\t\t\t10%') 
        textarea.insert(END,'\n--------------------------------------------------------------------------------')
        textarea.insert(END,f'\nTotal Bill\t\t\t\t\t\tRs {total_bill_button}')
        bill_save()
        

def total():
    global hair_cutservice_price, WaxingEntryservice_price, HairwashEntryservice_price, FacialEntryservice_price, FacebleachEntryservice_price, HairspaEntryservice_price
    global MedicureEntryservice_price, PedicureEntryservice_price, MassageEntryservice_price, EyebrowEntryservice_price, HaircolourEntryservice_price, MakeupEntryservice_price
    global LorealEntry_price, DoveEntry_price, PanteneEntry_price, VLCCEntry_price, SunsilkEntry_price, ClinicplusEntry_price
    global total_bill_button
    # Service Calculation
    hair_cutservice_price=int(Hair_cutEntry.get())*100
    WaxingEntryservice_price = int(WaxingEntry.get())*30
    HairwashEntryservice_price = int(HairwashEntry.get())*50
    FacialEntryservice_price = int(FacialEntry.get())*200
    FacebleachEntryservice_price = int(FacebleachEntry.get())*150
    HairspaEntryservice_price = int(HairspaEntry.get())*250
    MedicureEntryservice_price = int(MedicureEntry.get())*30
    PedicureEntryservice_price = int(PedicureEntry.get())*40
    MassageEntryservice_price = int(MassageEntry.get())*500
    EyebrowEntryservice_price = int(EyebrowEntry.get())*50
    HaircolourEntryservice_price = int(HaircolourEntry.get())*1000
    MakeupEntryservice_price = int(MakeupEntry.get())*2500

    totalservice_price = hair_cutservice_price + WaxingEntryservice_price + HairwashEntryservice_price + FacialEntryservice_price + FacebleachEntryservice_price + HairspaEntryservice_price + MedicureEntryservice_price + PedicureEntryservice_price + MassageEntryservice_price + EyebrowEntryservice_price + HaircolourEntryservice_price + MakeupEntryservice_price                      
    ServicePriceEntry.delete(0, END) #it will delete everything before the operation is performed
    ServicePriceEntry.insert(0, 'Rs ' + str(totalservice_price))

    # Product Price Calculation
    LorealEntry_price = int(LorealEntry.get())*150
    DoveEntry_price = int(DoveEntry.get())*120
    PanteneEntry_price = int(PanteneEntry.get())*50
    VLCCEntry_price = int(VLCCEntry.get())*200
    SunsilkEntry_price = int(SunsilkEntry.get())*80
    ClinicplusEntry_price = int(ClinicplusEntry.get())*40
    
    totalproduct_price = LorealEntry_price + DoveEntry_price + PanteneEntry_price + VLCCEntry_price + SunsilkEntry_price + ClinicplusEntry_price
    TotalProductPriceEntry.delete(0,END) #it will delete everything before the operation is performed
    TotalProductPriceEntry.insert(0, 'Rs '+ str(totalproduct_price))    
    Totalotherserviceprice = int(float(OtherServicePriceEntry.get()))

    total = (Totalotherserviceprice + totalproduct_price + totalservice_price)*1.20
    TotalServicePriceEntry.delete(0,END)
    TotalServicePriceEntry.insert(0, 'Rs '+str(total))

    total_bill_button = total
    
#Create the GUI
#Create window
root = Tk()
root.title('Shopkeeper Retail System')
root.geometry('1480x820')
root.iconbitmap('icon.ico')

#Create the heading lebel and heading
headingLable = Label(root,text='SHOPKEEPER STORE', font=('times new roman',30, 'bold'),bg='magenta4',fg='DarkOliveGreen1',bd=12,relief=GROOVE)

#To add the label in the top
headingLable.pack(fill=X)

#To create Customer label frame and entry details
customer_detail_frame = LabelFrame(root, text='Customer Details',font=('times new roman',15, 'bold'),fg='grey5',bd=8,relief=GROOVE, bg='magenta2')

#To add the label in the top
customer_detail_frame.pack(fill=X)

#To position the Bill 
Bill_label = Label(customer_detail_frame, text='Bill Number', font=('times new roman',15, 'bold'),bg='magenta2',fg='black')
Bill_label.grid(row=0,column=0,padx=20)
BillEntry = Entry(customer_detail_frame,font=('arial',15),bd=7,width=5)
BillEntry.grid(row=0,column=1,padx=6)

#To position the name 
Name_label = Label(customer_detail_frame, text='Name', font=('times new roman',15, 'bold'),bg='magenta2',fg='black')
Name_label.grid(row=0,column=2,padx=10)
nameEntry = Entry(customer_detail_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=3,padx=6)

#To position the phone
Phone_label = Label(customer_detail_frame, text='Phone Number', font=('times new roman',15, 'bold'),bg='magenta2',fg='black')  
Phone_label.grid(row=0,column=4,padx=20)
validate_input_cmd = root.register(validate_input)
PhoneEntry = Entry(customer_detail_frame, font=('arial',15), bd=7, width=18, validate="key", validatecommand=(validate_input_cmd, "%P"))
PhoneEntry.grid(row=0,column=5,padx=6)

#To position the Address
Add_label = Label(customer_detail_frame, text='Address', font=('times new roman',15, 'bold'),bg='magenta2',fg='black') 
Add_label.grid(row=0,column=6,padx=20)
AddEntry = Entry(customer_detail_frame,font=('arial',15),bd=7,width=18)
AddEntry.grid(row=0,column=7,padx=6)

#Add thge search button
Searchbutton=Button(customer_detail_frame,text='SEARCH',font=('arial',12,'bold'),border=7,width=10,command=search_bill)
Searchbutton.grid(row=0,column=8,padx=20,pady=8)

#To create product frame
productsframe = Frame(root)
productsframe.pack(fill=X)

ServiceFrame = LabelFrame(productsframe,text='Services',font=('times new roman',15, 'bold'),bg='magenta2',relief=GROOVE,fg='black')
ServiceFrame.grid(row=0,column=0)

#To add Hair cut
Hair_cut = Label(ServiceFrame, text='Hair Cut',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Hair_cut.grid(row=0,column=0,sticky=W)
Hair_cutEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
Hair_cutEntry.grid(row=0,column=1,padx=10,pady=9)
Hair_cutEntry.insert(0,0)

#To add waxing
Waxing = Label(ServiceFrame, text='Waxing',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Waxing.grid(row=1,column=0,sticky=W)
WaxingEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
WaxingEntry.grid(row=1,column=1,padx=10,pady=9)
WaxingEntry.insert(0,0)

#to add Hair wash
Hairwash = Label(ServiceFrame, text='Hair Wash',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Hairwash.grid(row=2,column=0,sticky=W)
HairwashEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
HairwashEntry.grid(row=2,column=1,padx=10,pady=9)
HairwashEntry.insert(0,0)

#To add the Facial
Facial = Label(ServiceFrame, text='Facial',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Facial.grid(row=3,column=0,sticky=W)
FacialEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
FacialEntry.grid(row=3,column=1,padx=10,pady=9)
FacialEntry.insert(0,0)

#To add Facebleach
Facebleach = Label(ServiceFrame, text='Face Bleach',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Facebleach.grid(row=4,column=0,sticky=W)
FacebleachEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
FacebleachEntry.grid(row=4,column=1,padx=10,pady=9)
FacebleachEntry.insert(0,0)

#To add Hairspa
Hairspa = Label(ServiceFrame, text='Hair Spa',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Hairspa.grid(row=5,column=0,sticky=W)
HairspaEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
HairspaEntry.grid(row=5,column=1,padx=10,pady=9)
HairspaEntry.insert(0,0)

#Service Section
ServiceFrame = LabelFrame(productsframe,text='Services',font=('times new roman',15, 'bold'),bg='magenta2',relief=GROOVE,fg='black')
ServiceFrame.grid(row=0,column=1)

#To add the services
Medicure  = Label(ServiceFrame, text='Medicure',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Medicure.grid(row=0,column=0,sticky=W)
MedicureEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
MedicureEntry.grid(row=0,column=1,padx=10,pady=9)
MedicureEntry.insert(0,0)

Pedicure  = Label(ServiceFrame, text='Pedicure',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Pedicure.grid(row=1,column=0,sticky=W)
PedicureEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
PedicureEntry.grid(row=1,column=1,padx=10,pady=9)
PedicureEntry.insert(0,0)

Massage = Label(ServiceFrame, text='Massage',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Massage.grid(row=2,column=0,sticky=W)
MassageEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
MassageEntry.grid(row=2,column=1,padx=10,pady=9)
MassageEntry.insert(0,0)

Eyebrow = Label(ServiceFrame, text='Eyebrow',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Eyebrow.grid(row=3,column=0,sticky=W)
EyebrowEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
EyebrowEntry.grid(row=3,column=1,padx=10,pady=9)
EyebrowEntry.insert(0,0)

Haircolour = Label(ServiceFrame, text='Hair colour',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Haircolour.grid(row=4,column=0,sticky=W)
HaircolourEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
HaircolourEntry.grid(row=4,column=1,padx=10,pady=9)
HaircolourEntry.insert(0,0)

Makeup = Label(ServiceFrame, text='Makeup',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Makeup.grid(row=5,column=0,sticky=W)
MakeupEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
MakeupEntry.grid(row=5,column=1,padx=10,pady=9)
MakeupEntry.insert(0,0)

#To create the product frame
ProductFrame = LabelFrame(productsframe,text='Products',font=('times new roman',15, 'bold'),bg='magenta2',relief=GROOVE,fg='black')
ProductFrame.grid(row=0,column=2)

#To add all the different products
Loreal = Label(ProductFrame, text='Loreal',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Loreal.grid(row=0,column=0,sticky=W)
LorealEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
LorealEntry.grid(row=0,column=1,padx=10,pady=9)
LorealEntry.insert(0,0)

Dove = Label(ProductFrame, text='Dove',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Dove.grid(row=1,column=0,sticky=W)
DoveEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
DoveEntry.grid(row=1,column=1,padx=10,pady=9)
DoveEntry.insert(0,0)

Pantene = Label(ProductFrame, text='Pantene',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Pantene.grid(row=2,column=0,sticky=W)
PanteneEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
PanteneEntry.grid(row=2,column=1,padx=10,pady=9)
PanteneEntry.insert(0,0)

VLCC = Label(ProductFrame, text='VLCC',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
VLCC.grid(row=3,column=0,sticky=W)
VLCCEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
VLCCEntry.grid(row=3,column=1,padx=10,pady=9)
VLCCEntry.insert(0,0)

Sunsilk  = Label(ProductFrame, text='Sunsilk',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Sunsilk.grid(row=4,column=0,sticky=W)
SunsilkEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
SunsilkEntry.grid(row=4,column=1,padx=10,pady=9)
SunsilkEntry.insert(0,0)

Clinicplus  = Label(ProductFrame, text='Clinic Plus',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Clinicplus.grid(row=5,column=0,sticky=W)
ClinicplusEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
ClinicplusEntry.grid(row=5,column=1,padx=10,pady=9)
ClinicplusEntry.insert(0,0)

#To create the bill frame
billframe = Frame(productsframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=20)

billarea_label = Label(billframe, text='Bill Summary',font=('times new roman',15, 'bold'),bd=7,relief=GROOVE)
billarea_label.pack(fill=X)

Scroll_bar = Scrollbar(billframe,orient=VERTICAL)
Scroll_bar.pack(side=RIGHT,fill=Y)

textarea = Text(billframe,height=18,width=80,yscrollcommand=Scroll_bar.set)
textarea.pack()
Scroll_bar.config(command=textarea.yview)

#To create the bill menu
BillmenuFrame = LabelFrame(root,text='Bill Menu',font=('times new roman',15, 'bold'),bg='magenta2',relief=GROOVE,fg='black')
BillmenuFrame.pack(fill=X)

ServicePrice = Label(BillmenuFrame, text='Service Price',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
ServicePrice.grid(row=0,column=0,sticky=W)
ServicePriceEntry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
ServicePriceEntry.grid(row=0,column=1,padx=10,pady=9)

OtherServicePrice = Label(BillmenuFrame, text='Other Services Price',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
OtherServicePrice.grid(row=1,column=0,sticky=W)
OtherServicePriceEntry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
OtherServicePriceEntry.grid(row=1,column=1,padx=10,pady=9)

TotalProductPrice = Label(BillmenuFrame, text='Total Product Price',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
TotalProductPrice.grid(row=0,column=2,sticky=W)
TotalProductPriceEntry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
TotalProductPriceEntry.grid(row=0,column=3,padx=10,pady=9)

TotalServicePrice = Label(BillmenuFrame, text='Total Cost',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
TotalServicePrice.grid(row=1,column=2,sticky=W)
TotalServicePriceEntry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
TotalServicePriceEntry.grid(row=1,column=3,padx=10,pady=9)

GST = Label(BillmenuFrame, text='GST',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
GST.grid(row=0,column=4,sticky=W)
GSTEntry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
GSTEntry.grid(row=0,column=5,padx=10,pady=9)
GSTEntry.insert(0,10)

CGST = Label(BillmenuFrame, text='CGST',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
CGST.grid(row=1,column=4,sticky=W)
CGSTEntry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
CGSTEntry.grid(row=1,column=5,padx=10,pady=9)
CGSTEntry.insert(0,10)


#Add button
buttonFrame = Frame(BillmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=6,rowspan=3)

Totalbutton=Button(buttonFrame,text='Total',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=7,pady=10,command=total)
Totalbutton.grid(row=0,column=0,pady=20,padx=5)

totalbill=Button(buttonFrame,text='Generate',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=7,pady=10,command=bill)
totalbill.grid(row=0,column=1,pady=20,padx=5)

EmailButton=Button(buttonFrame,text='Email',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=7,pady=10,command=send_email)
EmailButton.grid(row=0,column=2,pady=20,padx=5)

PrintButton=Button(buttonFrame,text='Print',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=7,pady=10,command=bill_print)
PrintButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=7,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

#To Display the service provide
ServiceProvider= LabelFrame(root,text='Shop Details',font=('times new roman',15, 'bold'),bg='magenta2',relief=GROOVE,fg='black')
ServiceProvider.pack(fill=X)

shopname = Label(ServiceProvider, text='XYZ',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
shopname.grid(row=0,column=0,sticky=W)

date_label = Label(ServiceProvider, text='Date:', font=('times new roman', 12, 'bold'), fg='grey5', bg='magenta2')
date_label.grid(row=1,column=0,sticky=W)

#To Display the product authorizer 
authorisation= LabelFrame(root)
authorisation.pack(fill=X)

auth_name = Label(authorisation, text='abhi@gmail.com', font=('times new roman', 15, 'bold'))
auth_name.grid(row=0, column=0)

# Configure the column to expand and fill the available space
authorisation.grid_columnconfigure(0, weight=1)



root.mainloop()

