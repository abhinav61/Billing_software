from tkinter import *
from tkinter import messagebox
import random

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
        textarea.insert(END,'\t\t\t\tXYZ Saloon\n\t\t\t\t   India\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\nPhone Number: {PhoneEntry.get()}\n')
        textarea.insert(END,f'\nAddress: {AddEntry.get()}')
        textarea.insert(END,'\n------------------------------------------------------------------------')
        textarea.insert(END,'Service\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n========================================================================')
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

def total():
    global hair_cutservice_price, WaxingEntryservice_price, HairwashEntryservice_price, FacialEntryservice_price, FacebleachEntryservice_price, HairspaEntryservice_price
    global MedicureEntryservice_price, PedicureEntryservice_price, MassageEntryservice_price, EyebrowEntryservice_price, HaircolourEntryservice_price, MakeupEntryservice_price
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




    
#Create the GUI
#Create window
root = Tk()
root.title('Shopkeeper Retail System')
root.geometry('1420x820')
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
Searchbutton=Button(customer_detail_frame,text='SEARCH',font=('arial',12,'bold'),border=7,width=10)
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

textarea = Text(billframe,height=18,width=72,yscrollcommand=Scroll_bar.set)
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

Totalbutton=Button(buttonFrame,text='Total',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=8,pady=10,command=total)
Totalbutton.grid(row=0,column=0,pady=20,padx=5)

totalbill=Button(buttonFrame,text='Total Bill',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=8,pady=10,command=bill)
totalbill.grid(row=0,column=1,pady=20,padx=5)

EmailButton=Button(buttonFrame,text='Email',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=8,pady=10)
EmailButton.grid(row=0,column=2,pady=20,padx=5)

PrintButton=Button(buttonFrame,text='Print',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=8,pady=10)
PrintButton.grid(row=0,column=3,pady=20,padx=5)

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

