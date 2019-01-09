from tkinter import *
import backend_roadworks
import backend_inventory

# This is my first program and I look forward to your feedback.

# CONTENTS
### 1. RoadWorks functions
### 2a. Stock Buttons with commands
### 2b. Roadwork buttons with commands
### 3. Search bar
### 4a. Road work Main view window with scroll bar
### 4b. Stock Main view window with scroll bar
### 5a. DATAFIELDS AND ENTRY BOXES
### 5b. ADDITIONAL DATA
###         Length in KM, Countdown till startdate OR enddate,
###         print off paperwork function??

### 1. ROADWORKS FUNCTIONS
### Click an item in the main window and have it return its values
### to the fields below the main window for appending
def get_selected_roadwork(event):
    global selected_roadworks
    index = list1.curselection()[0]
    selected_roadworks = list1.get(index)
    Location_Entry.delete(0, END)
    Location_Entry.insert(END, selected_roadworks[1])
    Client_Entry.delete(0, END)
    Client_Entry.insert(END, selected_roadworks[2])
    Start_Date_Entry.delete(0, END)
    Start_Date_Entry.insert(END, selected_roadworks[3])
    End_Date_Entry.delete(0, END)
    End_Date_Entry.insert(END, selected_roadworks[4])
    return(selected_roadworks)


def get_selected_item(event):
    global selected_item
    index = stocklist.curselection()[0]
    selected_item = stocklist.get(index)
    ITEM_STOCK_Entry.delete(0, END)
    ITEM_STOCK_Entry.insert(END, selected_item[1])
    ITEM_Amount_Entry.delete(0, END)
    ITEM_Amount_Entry.insert(END, selected_item[2])
    ITEM_Weight_Entry.delete(0, END)
    ITEM_Weight_Entry.insert(END, selected_item[3])
    ITEM_Warning_Entry.delete(0, END)
    ITEM_Warning_Entry.insert(END, selected_item[4])
    return(selected_item)


### FUNCTIONS for buttons
def view_roadworks():
    # Deleteing from index 0 to the end so we dont duplicate items on dispay
    list1.delete(0, END)
    for row in backend_roadworks.view():
        list1.insert(END, row) # END means every new row is added at the end

### Displays Stock items from inventory DB and displays them on seperate listbox
def view_inventory():
    stocklist.delete(0, END)
    for row in backend_inventory.view():
        stocklist.insert(END, row)


### Currently only searches location column
def search_roadworks():
    list1.delete(0, END)
    for row in backend_roadworks.search(search_text.get()):
        list1.insert(END, row)

###
def delete_roadworks():
    backend_roadworks.delete(selected_roadworks[0])
    list1.delete(0, END)
    for row in backend_roadworks.view():
        list1.insert(END, row)

def delete_inventory():
    backend_inventory.delete(selected_item[0])
    stocklist.delete(0, END)
    for row in backend_inventory.view():
        stocklist.insert(END, row)

### Adds info in the Entry boxes to the database
def Add_To_Roadworks():
    backend_roadworks.insert(Location_Text.get(), Client_Text.get(),
                            Start_Date_Text.get(), End_Date_Text.get())
    list1.delete(0, END)
    # list1.insert(END, (Location_Text.get(), Client_Text.get(),
    #                         Start_Date_Text.get(), End_Date_Text.get()))
    for row in backend_roadworks.view():
        list1.insert(END, row)


def Add_To_Inventory():
    backend_inventory.insert(ITEM_Name_Text.get(), ITEM_Amount_Text.get(),
                            ITEM_Weight_Text.get(), ITEM_Warning_Text.get())
    stocklist.delete(0, END)
    for row in backend_inventory.view():
        stocklist.insert(END, row)


# Update function takes items in the entry fields and uses
# the UPDATE function from backend to edit the rows
def Update_Roadworks():
    backend_roadworks.update(selected_roadworks[0],Location_Text.get(),
            Client_Text.get(), Start_Date_Text.get(), End_Date_Text.get())
    list1.delete(0, END)
    for row in backend_roadworks.view():
        list1.insert(END, row)


def Update_Inventory():
    backend_inventory.update(selected_item[0],ITEM_Name_Text.get(),
            ITEM_Amount_Text.get(), ITEM_Weight_Text.get(),
            ITEM_Warning_Text.get())
    stocklist.delete(0, END)
    for row in backend_inventory.view():
        stocklist.insert(END, row)


### Main
window=Tk()
window.title("TM Organiser")


### 2. BUTTONS WITH FUNCTIONS
# Inventory Buttons
view_stk_b = Button(window, text= "View Stock", width=14,
                    command = view_inventory)
view_stk_b.grid(row=25, column=0)

Create_Stock_Button = Button(window, text= "Create Stock Entry", width=14,
                    command = Add_To_Inventory)
Create_Stock_Button.grid(row=20, column=4)

Remove_Stock_Button = Button(window, text= "Remove Stock", width=14,
                    command = delete_inventory)
Remove_Stock_Button.grid(row=27, column=0)

update_stock_button = Button(window, text= "Update Stock", width=14,
                            command = Update_Inventory)
update_stock_button.grid(row=21, column=4)


# Road works Buttons on the right side NOW ON LEFT
view_wrks_b = Button(window, text= "View Road Works", width=14,
                command = view_roadworks)
view_wrks_b.grid(row = 4, column = 0)

Delete_Roadworks_Button = Button(window, text= "Del Road Works", width=14,
                command = delete_roadworks)
Delete_Roadworks_Button.grid(row= 6, column = 0)

Create_Roadworks_Button = Button(window, text= "Create New Entry", width=14,
                            command = Add_To_Roadworks)
Create_Roadworks_Button.grid(row = 17, column = 4)

Print_Out_Button = Button(window, text= "Print Details", width = 14)
Print_Out_Button.grid(row=15, column= 0)

### PLUS Data Update using the same boxes as add to database.
Update_RDatabaseButton = Button(window, text= "Update Entry", width=14,
                            command = Update_Roadworks)
Update_RDatabaseButton.grid(row = 18, column = 4)


# This button will be used for adding inventory items to the road works
# using start date and end date you can give a stock forcast to see what
# inventory will look like 5 months from now and when your going to struggle
# CREATE TABLE in ROADWORKS selected_Roadworks[] + selected_item[]
ItemsToRoadworksBUTTON = Button(window, text = "Assign Stock", width=14)
ItemsToRoadworksBUTTON.grid(row = 14, column = 0)




### 3. SEARCH BAR
# Search bar at the top with an entry box to type into
# search_label = Label(window, text= "")
# search_label.grid(row=0, column=1)

search_text = StringVar()
e1=Entry(window, textvariable= search_text)
e1.grid(row=0, column=1)

search_button = Button(window, text= "Search", width = 8,
                    command = search_roadworks)
search_button.grid(row=0, column=2)


### 4a. MAINVIEW BOX FOR ROADWORKS WITH SCROLL BAR
# Main view box listing items with scroll bar
list1 = Listbox(window, height=12,width=70)
list1.grid(row =1, column =1, rowspan = 15, columnspan = 15)

sb1= Scrollbar(window)
sb1.grid(row=3 ,column=16, rowspan = 4)

list1.bind('<<ListboxSelect>>', get_selected_roadwork)

# Verticle scroll set to sb1
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)



### 4b. MAINVIEW BOX FOR STOCK ITEMS
Stock_list_label = Label(window, text="")
Stock_list_label.grid(row=22 , column=2)

stocklist = Listbox(window, height=12, width = 70)
stocklist.grid(row=23, column=1, rowspan = 15, columnspan = 15)

CREATED_By_Jesus = Label(window, text= "+")
CREATED_By_Jesus.grid(row =40, column= 0)

sb2 = Scrollbar(window)
sb2.grid(row=25, column=16, rowspan = 4)

stocklist.configure(yscrollcommand =sb2.set)
sb2.configure(command = stocklist.yview)

stocklist.bind('<<ListboxSelect>>', get_selected_item)


### 5a. DATAFIELDS AND ENTRY BOXES
# data entry to use add roadworks using labels instead of buttons
# so we can rig all of them up to the "Add to database" button
HEYlisten_ADD = Label(window, text="""
                        Fill in the fields, press CREATE for a new entry""")
HEYlisten_ADD.grid(row=16 , column= 0, columnspan = 4)


Location_Text = StringVar()

Location_Label = Label(window, text="Location")
Location_Label.grid(row= 17, column=0)
Location_Entry = Entry(window, textvariable= Location_Text)
Location_Entry.grid(row= 17, column=1 )

Client_Text = StringVar()

Client_Label = Label(window, text= "Client")
Client_Label.grid(row = 18, column =0 )
Client_Entry = Entry(window, textvariable= Client_Text)
Client_Entry.grid(row = 18, column =1 )


Start_Date_Text = StringVar()

Start_Date_Label = Label(window, text="Start Date \nYY-MM-DD 00:00")
Start_Date_Label.grid(row = 17, column = 2)
Start_Date_Entry = Entry(window, textvariable = Start_Date_Text)
Start_Date_Entry.grid(row= 17, column = 3)

End_Date_Text = StringVar()

End_Date_Label = Label(window, text="End Date \nYY-MM-DD 00:00")
End_Date_Label.grid(row = 18, column = 2)
End_Date_Entry = Entry(window, textvariable = End_Date_Text)
End_Date_Entry.grid(row= 18, column = 3)


### Info for the user to edit or create new entry in the database
HEYlisten_UPDATE = Label(window, text="""
                           Or press the Update button to change info""")
HEYlisten_UPDATE.grid(row = 19, column = 0, columnspan = 4)


### STOCK ENTRY
ITEM_Name_Text = StringVar()

ITEM_Name_Label = Label(window, text="Stock item\nname")
ITEM_Name_Label.grid(row=20, column=0)
ITEM_STOCK_Entry = Entry(window, textvariable =ITEM_Name_Text)
ITEM_STOCK_Entry.grid(row=20,column=1)


ITEM_Amount_Text= StringVar()

ITEM_Amount_Label = Label(window, text="Amount")
ITEM_Amount_Label.grid(row=21, column=0)
ITEM_Amount_Entry = Entry(window, textvariable =ITEM_Amount_Text)
ITEM_Amount_Entry.grid(row=21, column=1)


ITEM_Weight_Text= StringVar()

ITEM_Weight_Label= Label(window, text="Weight")
ITEM_Weight_Label.grid(row= 20, column=2)
ITEM_Weight_Entry = Entry(window, textvariable=ITEM_Weight_Text)
ITEM_Weight_Entry.grid(row=20,column=3)


ITEM_Warning_Text= StringVar()

ITEM_Warning_Label = Label(window, text="Warning %")
ITEM_Warning_Label.grid(row=21, column=2)
ITEM_Warning_Entry = Entry(window, textvariable=ITEM_Warning_Text)
ITEM_Warning_Entry.grid(row=21, column=3)
### Stock interface section will be merged into the main window alongside
### The roadworks interface.. but for ease of reading I will have it seperated
### In the code.

### 5b. ADDITIONAL DATA
###         Length in KM, Countdown till startdate OR enddate,
###         print off paperwork function??
## Additional_Data = Label(window, text="ADDITIONAL DATA")
## Additional_Data.grid(row = 20, column = 2)

# Help_Button = Button(window, text="Need help?", width=14)
# Help_Button.grid(row = 19, column = 0)

## Length_KM = Label(window, text="Length(km)")
## Length_KM.grid(row = 21, column = 0)

## Traffic_lights_required = Label(window, text="Traffic lights?")
## Traffic_lights_required.grid(row = 21, column = 2)





window.mainloop()
