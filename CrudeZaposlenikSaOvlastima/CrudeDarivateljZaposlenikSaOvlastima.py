import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import tkinter as tk

#konekcija

def connection(): 
    conn=pymysql.connect(host='localhost',user='root',password='root',database="baza_banke_krvi")
    return conn

def refreshTable():
    for data in my_tree2.get_children():
        my_tree2.delete(data)
        
    for array in readDarivatelj():
        my_tree2.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
        
    my_tree2.tag_configure('orow',background='#EEEEEE',font=('Arial',9))
    my_tree2.grid(row=12,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
    
#GUI

root = Tk()
root.title("Darivatelj")
root.geometry("1800x900")
root.iconbitmap("krv.ico")
my_tree2 = ttk.Treeview(root)




#rezervirana mjesta za upis
rezmj1Darivatelj=tk.StringVar()
rezmj2Darivatelj=tk.StringVar()
rezmj3Darivatelj=tk.StringVar()
rezmj4Darivatelj=tk.StringVar()
rezmj5Darivatelj=tk.StringVar()
rezmj6Darivatelj=tk.StringVar()
rezmj7Darivatelj=tk.StringVar()
rezmj8Darivatelj=tk.StringVar()
rezmj9Darivatelj=tk.StringVar()
rezmj10Darivatelj=tk.StringVar()
rezmj11Darivatelj=tk.StringVar()
rezmj12Darivatelj=tk.StringVar()
rezmj13Darivatelj=tk.StringVar()
rezmj14Darivatelj=tk.StringVar()
rezmj15Darivatelj=tk.StringVar()
rezmj16Darivatelj=tk.StringVar()
rezmj17Darivatelj=tk.StringVar()
rezmj18Darivatelj=tk.StringVar()


#postavljanje vrijednosti za rez mjesta

def postRezMjDarivatelj(rijecDarivatelj, brojDarivatelj):
    if brojDarivatelj == 1:
        rezmj1Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 2:
        rezmj2Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 3:
        rezmj3Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 4:
        rezmj4Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 5:
        rezmj5Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 6:
        rezmj6Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 7:
        rezmj7Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 8:
        rezmj8Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 9:
        rezmj9Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 10:
        rezmj10Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 11:
        rezmj11Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 12:
        rezmj12Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 13:
        rezmj13Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 14:
        rezmj14Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 15:
        rezmj15Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 16:
        rezmj16Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 17:
        rezmj17Darivatelj.set(rijecDarivatelj)
    if brojDarivatelj == 18:
        rezmj18Darivatelj.set(rijecDarivatelj)
      

#funkcije

def readDarivatelj():
    connDarivatelj=connection()
    cursorDarivatelj=connDarivatelj.cursor()
    cursorDarivatelj.execute("SELECT * FROM darivatelj")
    rezultatDarivatelj=cursorDarivatelj.fetchall()
    connDarivatelj.commit()
    connDarivatelj.close()
    return rezultatDarivatelj

def addDarivatelj():
    id=str(DarivateljIDEntry.get())
    id_kriterij=str(DarivateljIDKriterijEntry.get())
    ime=str(DarivateljImeEntry.get())
    prezime=str(DarivateljPrezimeEntry.get())
    OIB=str(DarivateljOIBEntry.get())
    spol=str(DarivateljSpolEntry.get())
    datum_rodenja=str(DarivateljDatumRodenjaEntry.get())
    adresa=str(DarivateljAdresaEntry.get())
    grad=str(DarivateljGradEntry.get())
    kontakt=str(DarivateljKontaktEntry.get())
    krvna_grupa=str(DarivateljKrvnaGrupaEntry.get())
    dob=str(DarivateljDobEntry.get())
    tjelesna_tezina=str(DarivateljTjelesnaTezinaEntry.get())
    tjelesna_temperatura=str(DarivateljTjelesnaTemperaturaEntry.get())
    sistolicki_krvni_tlak=str(DarivateljSistolickiKrvniTlakEntry.get())
    dijastolicki_krvni_tlak=str(DarivateljDijastolickiKrvniTlakEntry.get())
    puls=str(DarivateljPulsEntry.get())
    hemoglobin=str(DarivateljHemoglobinEntry.get())
    
    if (id=="" or id==" ") or (id_kriterij=="" or id_kriterij==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (OIB=="" or OIB==" ") or (spol=="" or spol==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (krvna_grupa=="" or krvna_grupa==" ") or (dob=="" or dob==" ") or (tjelesna_tezina=="" or tjelesna_tezina==" ") or (tjelesna_temperatura=="" or tjelesna_tezina==" ") or (sistolicki_krvni_tlak=="" or sistolicki_krvni_tlak==" ") or (dijastolicki_krvni_tlak=="" or dijastolicki_krvni_tlak==" ") or (puls=="" or puls==" ") or (hemoglobin=="" or hemoglobin==" "):
        messagebox.showinfo("Pogre??ka!","Molimo upotpunite prazan obrazac!")
        return
    else:
        try:
            connDarivatelj=connection()
            cursorDarivatelj=connDarivatelj.cursor()
            cursorDarivatelj.execute("INSERT INTO darivatelj VALUES ('"+id+"','"+id_kriterij+"','"+ime+"','"+prezime+"','"+OIB+"','"+spol+"','"+datum_rodenja+"','"+adresa+"','"+grad+"','"+kontakt+"','"+krvna_grupa+"','"+dob+"','"+tjelesna_tezina+"','"+tjelesna_temperatura+"','"+sistolicki_krvni_tlak+"','"+dijastolicki_krvni_tlak+"','"+puls+"','"+hemoglobin+"') ")
            connDarivatelj.commit()
            connDarivatelj.close()
        except:
            messagebox.showinfo("Pogre??ka!","Id darivatelja ve?? postoji!")
            return
        
    refreshTable()
    
    
def selectDarivatelj():
        try:
            odabrani_darivatelj=my_tree2.selection()[0]
            id=str(my_tree2.item(odabrani_darivatelj)['values'][0])
            id_kriterij=str(my_tree2.item(odabrani_darivatelj)['values'][1])
            ime=str(my_tree2.item(odabrani_darivatelj)['values'][2])
            prezime=str(my_tree2.item(odabrani_darivatelj)['values'][3])
            OIB=str(my_tree2.item(odabrani_darivatelj)['values'][4])
            spol=str(my_tree2.item(odabrani_darivatelj)['values'][5])
            datum_rodenja=str(my_tree2.item(odabrani_darivatelj)['values'][6])
            adresa=str(my_tree2.item(odabrani_darivatelj)['values'][7])
            grad=str(my_tree2.item(odabrani_darivatelj)['values'][8])
            kontakt=str(my_tree2.item(odabrani_darivatelj)['values'][9])
            krvna_grupa=str(my_tree2.item(odabrani_darivatelj)['values'][10])
            dob=str(my_tree2.item(odabrani_darivatelj)['values'][11])
            tjelesna_tezina=str(my_tree2.item(odabrani_darivatelj)['values'][12])
            tjelesna_temperatura=str(my_tree2.item(odabrani_darivatelj)['values'][13])
            sistolicki_krvni_tlak=str(my_tree2.item(odabrani_darivatelj)['values'][14])
            dijastolicki_krvni_tlak=str(my_tree2.item(odabrani_darivatelj)['values'][15])
            puls=str(my_tree2.item(odabrani_darivatelj)['values'][16])
            hemoglobin=str(my_tree2.item(odabrani_darivatelj)['values'][17])
            
            postRezMjDarivatelj(id,1)
            postRezMjDarivatelj(id_kriterij,2)
            postRezMjDarivatelj(ime,3)
            postRezMjDarivatelj(prezime,4)
            postRezMjDarivatelj(OIB,5)
            postRezMjDarivatelj(spol,6)
            postRezMjDarivatelj(datum_rodenja,7)
            postRezMjDarivatelj(adresa,8)
            postRezMjDarivatelj(grad,9)
            postRezMjDarivatelj(kontakt,10)
            postRezMjDarivatelj(krvna_grupa,11)
            postRezMjDarivatelj(dob,12)
            postRezMjDarivatelj(tjelesna_tezina,13)
            postRezMjDarivatelj(tjelesna_temperatura,14)
            postRezMjDarivatelj(sistolicki_krvni_tlak,15)
            postRezMjDarivatelj(dijastolicki_krvni_tlak,16)
            postRezMjDarivatelj(puls,17)
            postRezMjDarivatelj(hemoglobin,18)
            
        except:
            messagebox.showinfo("Pogre??ka!","Molimo izaberite podatak")
            
def searchDarivatelj():
    id=str(DarivateljIDEntry.get())
    id_kriterij=str(DarivateljIDKriterijEntry.get())
    ime=str(DarivateljImeEntry.get())
    prezime=str(DarivateljPrezimeEntry.get())
    OIB=str(DarivateljOIBEntry.get())
    spol=str(DarivateljSpolEntry.get())
    datum_rodenja=str(DarivateljDatumRodenjaEntry.get())
    adresa=str(DarivateljAdresaEntry.get())
    grad=str(DarivateljGradEntry.get())
    kontakt=str(DarivateljKontaktEntry.get())
    krvna_grupa=str(DarivateljKrvnaGrupaEntry.get())
    dob=str(DarivateljDobEntry.get())
    tjelesna_tezina=str(DarivateljTjelesnaTezinaEntry.get())
    tjelesna_temperatura=str(DarivateljTjelesnaTemperaturaEntry.get())
    sistolicki_krvni_tlak=str(DarivateljSistolickiKrvniTlakEntry.get())
    dijastolicki_krvni_tlak=str(DarivateljDijastolickiKrvniTlakEntry.get())
    puls=str(DarivateljPulsEntry.get())
    hemoglobin=str(DarivateljHemoglobinEntry.get())
    
    if id is None or id == "":
        id = '%'
    if id_kriterij is None or id_kriterij == "":
        id_kriterij = '%'
    if ime is None or ime == "":
        ime = '%'
    if prezime is None or prezime == "":
        prezime = '%'
    if OIB is None or OIB == "":
        OIB = '%'
    if spol is None or spol == "":
        spol = '%'
    if datum_rodenja is None or datum_rodenja == "":
        datum_rodenja = '%'
    if adresa is None or adresa == "":
        adresa = '%'
    if grad is None or grad == "":
        grad = '%'
    if kontakt is None or kontakt == "":
        kontakt = '%'
    if krvna_grupa is None or krvna_grupa == "":
        krvna_grupa = '%'
    if dob is None or dob == "":
        dob = '%'
    if tjelesna_tezina is None or tjelesna_tezina == "":
        tjelesna_tezina = '%'
    if tjelesna_temperatura is None or tjelesna_temperatura == "":
        tjelesna_temperatura = '%'
    if sistolicki_krvni_tlak is None or sistolicki_krvni_tlak == "":
        sistolicki_krvni_tlak = '%'
    if dijastolicki_krvni_tlak is None or dijastolicki_krvni_tlak == "":
        dijastolicki_krvni_tlak = '%'
    if puls is None or puls == "":
        puls = '%'
    if hemoglobin is None or hemoglobin == "":
        hemoglobin = '%'
    
    connDarivatelj=connection()
    cursorDarivatelj=connDarivatelj.cursor()
    query = "SELECT * FROM darivatelj WHERE id like %s or id_kriterij like %s or ime like %s or prezime like %s or OIB like %s or spol like %s or datum_rodenja like %s or adresa like %s or grad like %s or kontakt like %s or krvna_grupa like %s or dob like %s or tjelesna_tezina like %s or tjelesna_temperatura like %s or sistolicki_krvni_tlak like %s or dijastolicki_krvni_tlak like %s or puls like %s or hemoglobin like %s"
    cursorDarivatelj.execute(query, (id, id_kriterij, ime, prezime, OIB, spol, datum_rodenja, adresa, grad, kontakt, krvna_grupa, dob, tjelesna_tezina, tjelesna_temperatura, sistolicki_krvni_tlak, dijastolicki_krvni_tlak, puls, hemoglobin))
    rows = cursorDarivatelj.fetchall()
    match = False
    for row in rows:
        if str(row[0]) == id:
            match = True
            for i in range(0,9):
                postRezMjDarivatelj(row[i],(i+1))
    if not match:
        messagebox.showinfo("Pogre??ka!","Nema odgovaraju??eg podatka!")
    connDarivatelj.commit()
    connDarivatelj.close()
    
def updateDarivatelj():
    try:
        odabrani_darivatelj=my_tree2.selection()[0]
        odabraniDarivatelj=str(my_tree2.item(odabrani_darivatelj)['values'][0])
    except:
        messagebox.showinfo("Pogre??ka!","Odaberite darivatelja!")
        return
        
    id=str(DarivateljIDEntry.get())
    id_kriterij=str(DarivateljIDKriterijEntry.get())
    ime=str(DarivateljImeEntry.get())
    prezime=str(DarivateljPrezimeEntry.get())
    OIB=str(DarivateljOIBEntry.get())
    spol=str(DarivateljSpolEntry.get())
    datum_rodenja=str(DarivateljDatumRodenjaEntry.get())
    adresa=str(DarivateljAdresaEntry.get())
    grad=str(DarivateljGradEntry.get())
    kontakt=str(DarivateljKontaktEntry.get())
    krvna_grupa=str(DarivateljKrvnaGrupaEntry.get())
    dob=str(DarivateljDobEntry.get())
    tjelesna_tezina=str(DarivateljTjelesnaTezinaEntry.get())
    tjelesna_temperatura=str(DarivateljTjelesnaTemperaturaEntry.get())
    sistolicki_krvni_tlak=str(DarivateljSistolickiKrvniTlakEntry.get())
    dijastolicki_krvni_tlak=str(DarivateljDijastolickiKrvniTlakEntry.get())
    puls=str(DarivateljPulsEntry.get())
    hemoglobin=str(DarivateljHemoglobinEntry.get())
    
    if (id=="" or id==" ") or (id_kriterij=="" or id_kriterij==" ") or (ime=="" or ime==" ") or (prezime=="" or prezime==" ") or (OIB=="" or OIB==" ") or (spol=="" or spol==" ") or (datum_rodenja=="" or datum_rodenja==" ") or (adresa=="" or adresa==" ") or (grad=="" or grad==" ") or (kontakt=="" or kontakt==" ") or (krvna_grupa=="" or krvna_grupa==" ") or (dob=="" or dob==" ") or (tjelesna_tezina=="" or tjelesna_tezina==" ") or (tjelesna_temperatura=="" or tjelesna_temperatura==" ") or (sistolicki_krvni_tlak=="" or sistolicki_krvni_tlak==" ") or (dijastolicki_krvni_tlak=="" or dijastolicki_krvni_tlak==" ") or (puls=="" or puls==" ") or (hemoglobin=="" or hemoglobin==" "):
        messagebox.showinfo("Pogre??ka!","Molimo upotpunite prazan obrazac!")
        return
    else:
        try:
            connDarivatelj=connection()
            cursorDarivatelj=connDarivatelj.cursor()
            cursorDarivatelj.execute(f"UPDATE darivatelj SET id='{id}', id_kriterij='{id_kriterij}', ime='{ime}', prezime='{prezime}', OIB='{OIB}', spol='{spol}', datum_rodenja='{datum_rodenja}', adresa='{adresa}', grad='{grad}', kontakt='{kontakt}', krvna_grupa='{krvna_grupa}', dob='{dob}', tjelesna_tezina='{tjelesna_tezina}', tjelesna_temperatura='{tjelesna_temperatura}', sistolicki_krvni_tlak='{sistolicki_krvni_tlak}', dijastolicki_krvni_tlak='{dijastolicki_krvni_tlak}', puls='{puls}', hemoglobin='{hemoglobin}' WHERE id={odabraniDarivatelj}")
            connDarivatelj.commit()
            connDarivatelj.close()
            refreshTable()
        except Exception as e:
            messagebox.showinfo("Pogre??ka!", f"Do??lo je do problema prilikom a??uriranja podataka.\n Razlog: {e}")
        return
    

#GUI

labelDarivatelj = Label(root, text = "Sustav upravljanja darivateljima", font=('Arial Bold',30))
labelDarivatelj.grid(row=0,column=0,columnspan=2,rowspan=2,padx=40,pady=30)

darivateljIDLabel = Label(root,text = "id",font=('Arial',10))
darivateljIDKriterijLabel = Label(root,text = "id_kriterij",font=('Arial',10))
darivateljImeLabel = Label(root,text = "Ime",font=('Arial',10))
darivateljPrezimeLabel = Label(root,text = "Prezime",font=('Arial',10))
darivateljOIBLabel = Label(root,text = "OIB",font=('Arial',10))
darivateljSpolLabel = Label(root,text = "Spol",font=('Arial',10))
darivateljDatumRodenjaLabel = Label(root,text = "Datum ro??enja",font=('Arial',10))
darivateljAdresaLabel = Label(root,text = "Adresa",font=('Arial',10))
darivateljGradLabel = Label(root,text = "Grad",font=('Arial',10))
darivateljKontaktLabel = Label(root,text = "Kontakt",font=('Arial',10))
darivateljKrvnaGrupaLabel = Label(root,text = "Krva grupa",font=('Arial',10))
darivateljDobLabel = Label(root,text = "Dob",font=('Arial',10))
darivateljTjelesnaTezinaLabel = Label(root,text = "Te??ina",font=('Arial',10))
darivateljTjelesnaTemperaturaLabel = Label(root,text = "Temperatura",font=('Arial',10))
darivateljSistolickiKrvniTlakLabel = Label(root,text = "Sistoli??ki tlak",font=('Arial',10))
darivateljDijastolickiKrvniTlakLabel = Label(root,text = "Dijastoli??ki tlak",font=('Arial',10))
darivateljPulsLabel = Label(root,text = "Puls",font=('Arial',10))
darivateljHemoglobinLabel = Label(root,text = "Hemoglobin",font=('Arial',10))
  

darivateljIDLabel.grid(row=2,column=0,columnspan=1,padx=50,pady=5)
darivateljIDKriterijLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
darivateljImeLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
darivateljPrezimeLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
darivateljOIBLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
darivateljSpolLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
darivateljDatumRodenjaLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
darivateljAdresaLabel.grid(row=9,column=0,columnspan=1,padx=50,pady=5)
darivateljGradLabel.grid(row=10,column=0,columnspan=1,padx=50,pady=5)
darivateljKontaktLabel.grid(row=11,column=0,columnspan=1,padx=50,pady=5)
darivateljKrvnaGrupaLabel.grid(row=12,column=0,columnspan=1,padx=50,pady=5)
darivateljDobLabel.grid(row=13,column=0,columnspan=1,padx=50,pady=5)
darivateljTjelesnaTezinaLabel.grid(row=14,column=0,columnspan=1,padx=50,pady=5)
darivateljTjelesnaTemperaturaLabel.grid(row=15,column=0,columnspan=1,padx=50,pady=5)
darivateljSistolickiKrvniTlakLabel.grid(row=16,column=0,columnspan=1,padx=50,pady=5)
darivateljDijastolickiKrvniTlakLabel.grid(row=17,column=0,columnspan=1,padx=50,pady=5)
darivateljPulsLabel.grid(row=18,column=0,columnspan=1,padx=50,pady=5)
darivateljHemoglobinLabel.grid(row=19,column=0,columnspan=1,padx=50,pady=5)

DarivateljIDEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj1Darivatelj)
DarivateljIDKriterijEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj2Darivatelj)
DarivateljImeEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj3Darivatelj)
DarivateljPrezimeEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj4Darivatelj)
DarivateljOIBEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj5Darivatelj)
DarivateljSpolEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj6Darivatelj)
DarivateljDatumRodenjaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj7Darivatelj)
DarivateljAdresaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj8Darivatelj)
DarivateljGradEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj9Darivatelj)
DarivateljKontaktEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj10Darivatelj)
DarivateljKrvnaGrupaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj11Darivatelj)
DarivateljDobEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj12Darivatelj)
DarivateljTjelesnaTezinaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj13Darivatelj)
DarivateljTjelesnaTemperaturaEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj14Darivatelj)
DarivateljSistolickiKrvniTlakEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj15Darivatelj)
DarivateljDijastolickiKrvniTlakEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj16Darivatelj)
DarivateljPulsEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj17Darivatelj)
DarivateljHemoglobinEntry=Entry(root,width=55,bd=5,font=('Arial',15), textvariable=rezmj18Darivatelj)

DarivateljIDEntry.grid(row=2,column=1,columnspan=4,padx=5,pady=0)
DarivateljIDKriterijEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
DarivateljImeEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
DarivateljPrezimeEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
DarivateljOIBEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
DarivateljSpolEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
DarivateljDatumRodenjaEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
DarivateljAdresaEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)
DarivateljGradEntry.grid(row=10,column=1,columnspan=4,padx=5,pady=0)
DarivateljKontaktEntry.grid(row=11,column=1,columnspan=4,padx=5,pady=0)
DarivateljKrvnaGrupaEntry.grid(row=12,column=1,columnspan=4,padx=5,pady=0)
DarivateljDobEntry.grid(row=13,column=1,columnspan=4,padx=5,pady=0)
DarivateljTjelesnaTezinaEntry.grid(row=14,column=1,columnspan=4,padx=5,pady=0)
DarivateljTjelesnaTemperaturaEntry.grid(row=15,column=1,columnspan=4,padx=5,pady=0)
DarivateljSistolickiKrvniTlakEntry.grid(row=16,column=1,columnspan=4,padx=5,pady=0)
DarivateljDijastolickiKrvniTlakEntry.grid(row=17,column=1,columnspan=4,padx=5,pady=0)
DarivateljPulsEntry.grid(row=18,column=1,columnspan=4,padx=5,pady=0)
DarivateljHemoglobinEntry.grid(row=19,column=1,columnspan=4,padx=5,pady=0)


addBtn=Button(root, text="Dodaj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=addDarivatelj)
updateBtn=Button(root, text="A??uriraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=updateDarivatelj)
searchBtn=Button(root, text="Pretra??i",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=searchDarivatelj)
selectBtn=Button(root, text="Izaberi",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red", command=selectDarivatelj)

addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

frame = tk.Frame(root)
frame.grid(column=1, row=30)

style=ttk.Style()
my_tree2['columns']=("id","id_kriterij","ime","prezime","OIB","spol","datum_rodenja","adresa","grad","kontakt","krvna_grupa","dob","tjelesna_tezina","tjelesna_temperatura","sistolicki_krvni_tlak","dijastolicki_krvni_tlak","puls","hemoglobin")
my_tree2.grid(column=1, row=2)
my_tree2.column('#0',width=0,stretch=NO)

my_tree2.column("id",anchor=W,width=80)
my_tree2.column("id_kriterij",anchor=W,width=80)
my_tree2.column("ime",anchor=W,width=80)
my_tree2.column("prezime",anchor=W,width=80)
my_tree2.column("OIB",anchor=W,width=80)
my_tree2.column("spol",anchor=W,width=80)
my_tree2.column("datum_rodenja",anchor=W,width=80)
my_tree2.column("adresa",anchor=W,width=80)
my_tree2.column("grad",anchor=W,width=80)
my_tree2.column("kontakt",anchor=W,width=80)
my_tree2.column("krvna_grupa",anchor=W,width=80)
my_tree2.column("dob",anchor=W,width=80)
my_tree2.column("tjelesna_tezina",anchor=W,width=80)
my_tree2.column("tjelesna_temperatura",anchor=W,width=80)
my_tree2.column("sistolicki_krvni_tlak",anchor=W,width=80)
my_tree2.column("dijastolicki_krvni_tlak",anchor=W,width=80)
my_tree2.column("puls",anchor=W,width=80)
my_tree2.column("hemoglobin",anchor=W,width=80)

my_tree2.heading("id",text="id",anchor=W)
my_tree2.heading("id_kriterij",text="id_kriterij",anchor=W)
my_tree2.heading("ime",text="ime",anchor=W)
my_tree2.heading("prezime",text="prezime",anchor=W)
my_tree2.heading("OIB",text="OIB",anchor=W)
my_tree2.heading("spol",text="spol",anchor=W)
my_tree2.heading("datum_rodenja",text="datum_rodenja",anchor=W)
my_tree2.heading("adresa",text="adresa",anchor=W)
my_tree2.heading("grad",text="grad",anchor=W)
my_tree2.heading("kontakt",text="kontakt",anchor=W)
my_tree2.heading("krvna_grupa",text="krvna_grupa",anchor=W)
my_tree2.heading("dob",text="dob",anchor=W)
my_tree2.heading("tjelesna_tezina",text="tjelesna_tezina",anchor=W)
my_tree2.heading("tjelesna_temperatura",text="tjelesna_temperatura",anchor=W)
my_tree2.heading("sistolicki_krvni_tlak",text="sistolicki_krvni_tlak",anchor=W)
my_tree2.heading("dijastolicki_krvni_tlak",text="dijastolicki_krvni_tlak",anchor=W)
my_tree2.heading("puls",text="puls",anchor=W)
my_tree2.heading("hemoglobin",text="hemoglobin",anchor=W)

refreshTable()

root.mainloop()