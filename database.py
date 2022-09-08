import sqlite3



class Database:

    def __init__(self, db_name):
        self.connect_ = sqlite3.connect(db_name)
        self.cursor_ = self.connect_.cursor()
        self.cursor_.execute(f"CREATE TABLE IF NOT EXISTS borderou_electronic (id INTEGER PRIMARY KEY, nume_complet TEXT, domiciliu TEXT, denumirea_speciei_culese TEXT, cantitate INTEGER, pret INTEGER)")
        self.connect_.commit()
        

    def insert(self, nume_complet, domiciliu, denumirea_speciei_culese, cantitate, pret):
        self.cursor_.execute("INSERT INTO borderou_electronic VALUES(NULL,?,?,?,?,?)",(nume_complet, domiciliu, denumirea_speciei_culese, cantitate, pret))
        self.connect_.commit()
        


    def view_all(self):
        self.cursor_.execute("SELECT * FROM borderou_electronic") 
        rows = self.cursor_.fetchall() 
        return rows

     
    def search(self,nume_complet="", domiciliu="", denumirea_speciei_culese="", cantitate="", pret=""):
        self.cursor_.execute(
            "SELECT * FROM borderou_electronic WHERE nume_complet=? OR domiciliu=? OR denumirea_speciei_culese=? OR cantitate=? OR pret=?",
            (nume_complet, domiciliu, denumirea_speciei_culese, cantitate, pret)
            ) 
        rows = self.cursor_.fetchall() 
        return rows

    
    def delete(self, id):                
        self.cursor_.execute("DELETE FROM borderou_electronic WHERE id=?",(id,))
        self.connect_.commit()
        

        
    def update(self, id,nume_complet, domiciliu, denumirea_speciei_culese, cantitate, pret):                 
        self.cursor_.execute(
            f"UPDATE borderou_electronic SET nume_complet=?, domiciliu=?, denumirea_speciei_culese=?, cantitate=?, pret=? WHERE id=?",
            (nume_complet, domiciliu, denumirea_speciei_culese, cantitate, pret, id))
        self.connect_.commit()

    def __del__(self):
        self.connect_.close()