import sqlite3
def createdb():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE ITEM
        (ID INTEGER PRIMARY KEY   AUTOINCREMENT,
        NAME           TEXT     NOT NULL,
        ILVL           INT      NOT NULL,
        TYPE           INT      NOT NULL,
        rarity         INT      NOT NULL,
        slot           INT      NOT NULL,
        damage         real             ,
        APS            real             ,
        mod1           INT              ,
        mod2           INT              ,
        mod3           INT              ,
        mod4           INT              ,
        mod5           INT              ,
        mod6           INT              ,
        );''')
    conn.commit()
    conn.close()

if __name__=="__main__":
    createdb()