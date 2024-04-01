from tkinter import *


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
PhoneEntry = Entry(customer_detail_frame,font=('arial',15),bd=7,width=18)
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

#To add waxing
Waxing = Label(ServiceFrame, text='Waxing',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Waxing.grid(row=1,column=0,sticky=W)
WaxingEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
WaxingEntry.grid(row=1,column=1,padx=10,pady=9)

#to add Hair wash
Hairwash = Label(ServiceFrame, text='Hair Wash',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Hairwash.grid(row=2,column=0,sticky=W)
HairwashEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
HairwashEntry.grid(row=2,column=1,padx=10,pady=9)

#To add the Facial
Facial = Label(ServiceFrame, text='Facial',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Facial.grid(row=3,column=0,sticky=W)
FacialEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
FacialEntry.grid(row=3,column=1,padx=10,pady=9)

#To add Facebleach
Facebleach = Label(ServiceFrame, text='Face Bleach',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Facebleach.grid(row=4,column=0,sticky=W)
FacebleachEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
FacebleachEntry.grid(row=4,column=1,padx=10,pady=9)

#To add Hairspa
Hairspa = Label(ServiceFrame, text='Hair Spa',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Hairspa.grid(row=5,column=0,sticky=W)
HairspaEntry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
HairspaEntry.grid(row=5,column=1,padx=10,pady=9)

#Service Section
ServiceFrame = LabelFrame(productsframe,text='Services',font=('times new roman',15, 'bold'),bg='magenta2',relief=GROOVE,fg='black')
ServiceFrame.grid(row=0,column=1)

#To add the services
Medicure  = Label(ServiceFrame, text='Medicure',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Medicure.grid(row=0,column=0,sticky=W)
Medicure.Entry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
Medicure.Entry.grid(row=0,column=1,padx=10,pady=9)

Pedicure  = Label(ServiceFrame, text='Pedicure',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Pedicure.grid(row=1,column=0,sticky=W)
Pedicure.Entry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
Pedicure.Entry.grid(row=1,column=1,padx=10,pady=9)

Massage = Label(ServiceFrame, text='Massage',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Massage.grid(row=2,column=0,sticky=W)
Massage.Entry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
Massage.Entry.grid(row=2,column=1,padx=10,pady=9)

Eyebrow = Label(ServiceFrame, text='Eyebrow',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Eyebrow.grid(row=3,column=0,sticky=W)
Eyebrow.Entry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
Eyebrow.Entry.grid(row=3,column=1,padx=10,pady=9)

Haircolour = Label(ServiceFrame, text='Hair colour',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Haircolour.grid(row=4,column=0,sticky=W)
Haircolour.Entry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
Haircolour.Entry.grid(row=4,column=1,padx=10,pady=9)

Makeup = Label(ServiceFrame, text='Makeup',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Makeup.grid(row=5,column=0,sticky=W)
Makeup.Entry = Entry(ServiceFrame,font=('arial',15,'bold'),width=10,bd=5)
Makeup.Entry.grid(row=5,column=1,padx=10,pady=9)

#To create the product frame
ProductFrame = LabelFrame(productsframe,text='Products',font=('times new roman',15, 'bold'),bg='magenta2',relief=GROOVE,fg='black')
ProductFrame.grid(row=0,column=2)

#To add all the different products
Loreal = Label(ProductFrame, text='Loreal',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Loreal.grid(row=0,column=0,sticky=W)
LorealEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
LorealEntry.grid(row=0,column=1,padx=10,pady=9)

Dove = Label(ProductFrame, text='Dove',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Dove.grid(row=1,column=0,sticky=W)
DoveEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
DoveEntry.grid(row=1,column=1,padx=10,pady=9)

Pantene = Label(ProductFrame, text='Pantene',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Pantene.grid(row=2,column=0,sticky=W)
PanteneEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
PanteneEntry.grid(row=2,column=1,padx=10,pady=9)

VLCC = Label(ProductFrame, text='VLCC',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
VLCC.grid(row=3,column=0,sticky=W)
VLCCEntry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
VLCCEntry.grid(row=3,column=1,padx=10,pady=9)

Sunsilk  = Label(ProductFrame, text='Sunsilk',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Sunsilk.grid(row=4,column=0,sticky=W)
Sunsilk.Entry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
Sunsilk.Entry.grid(row=4,column=1,padx=10,pady=9)

Clinicplus  = Label(ProductFrame, text='Clinic Plus',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
Clinicplus.grid(row=5,column=0,sticky=W)
Clinicplus.Entry = Entry(ProductFrame,font=('arial',15,'bold'),width=10,bd=5)
Clinicplus.Entry.grid(row=5,column=1,padx=10,pady=9)

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
ServicePrice.Entry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
ServicePrice.Entry.grid(row=0,column=1,padx=10,pady=9)

OtherServicePrice = Label(BillmenuFrame, text='Other Services Price',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
OtherServicePrice.grid(row=1,column=0,sticky=W)
OtherServicePrice.Entry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
OtherServicePrice.Entry.grid(row=1,column=1,padx=10,pady=9)

TotalProductPrice = Label(BillmenuFrame, text='Total Product Price',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
TotalProductPrice.grid(row=0,column=2,sticky=W)
TotalProductPrice.Entry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
TotalProductPrice.Entry.grid(row=0,column=3,padx=10,pady=9)

TotalServicePrice = Label(BillmenuFrame, text='Total Services Cost',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
TotalServicePrice.grid(row=1,column=2,sticky=W)
TotalServicePrice.Entry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
TotalServicePrice.Entry.grid(row=1,column=3,padx=10,pady=9)

GST = Label(BillmenuFrame, text='GST',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
GST.grid(row=0,column=4,sticky=W)
GST.Entry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
GST.Entry.grid(row=0,column=5,padx=10,pady=9)

CGST = Label(BillmenuFrame, text='CGST',font=('times new roman',15, 'bold'),fg='grey5',bd=8, bg='magenta2')
CGST.grid(row=1,column=4,sticky=W)
CGST.Entry = Entry(BillmenuFrame,font=('arial',15,'bold'),width=10,bd=5)
CGST.Entry.grid(row=1,column=5,padx=10,pady=9)

#Add button
buttonFrame = Frame(BillmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=6,rowspan=3)

Totalbutton=Button(buttonFrame,text='Total Bill',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=8,pady=10)
Totalbutton.grid(row=0,column=0,pady=20,padx=5)

SaveButton=Button(buttonFrame,text='Save',font=('arial',16, 'bold'),bg='magenta2',fg='grey5',bd=5,width=8,pady=10)
SaveButton.grid(row=0,column=1,pady=20,padx=5)

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

