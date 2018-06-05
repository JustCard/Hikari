import sqlite3, os
import PIL, time, datetime

class DBManager(object):
        ##Initialize a Connection to a Database
        def __init__(self):
                        self.conn = sqlite3.connect('main.db')
                        self.cursor = self.conn.cursor()
                        
                        
        def CreateTable(self):
                self.tablename = "Main" 
                self.query = ("CREATE TABLE IF NOT EXISTS " + self.tablename + "(Time REAL, datestamp TEXT, Id INTEGER PRIMARY KEY  AUTOINCREMENT, Title VARCHAR(255), Type VARCHAR(255), AuthorStudio VARCHAR(255), Genre VARCHAR(255), Volumes INT, ChaptersEpisodes INT, Status CHAR(10), ImagePath VARCHAR(255));")
                self.cursor.execute(self.query)
                self.conn.commit()
        
        def AddEntryToDataBase(self, Title, Type, AuthorStudio, Genre, Volumes, ChaptersEpisodes, Status, ImagePath):
                Time = time.time()
                Date = str(datetime.datetime.fromtimestamp(Time).strftime("%m-%d-%Y %I:%M:%S %p"))
                self.cursor.execute("INSERT INTO Main (Time, datestamp, Title, Type, AuthorStudio, Genre , Volumes, ChaptersEpisodes, Status, ImagePath) VALUES (?,?,?,?,?,?,?,?,?,?)", (Time, Date, Title, Type, AuthorStudio, Genre, Volumes, ChaptersEpisodes, Status, ImagePath))
                self.conn.commit()

        def EditEntryToDataBase(self, Title, Type, AuthorStudio, Genre, Volumes, ChaptersEpisodes, Status, TitlePointer):
                Time = time.time()
                Date = str(datetime.datetime.fromtimestamp(Time).strftime("%m-%d-%Y %I:%M:%S %p"))
                self.query = "UPDATE Main SET datestamp = ?, Title = ?, Type = ?, AuthorStudio = ?, Genre = ?, Volumes = ?, ChaptersEpisodes = ?, Status = ? WHERE Title = ?;"
                #self.query = "UPDATE Main SET datestamp =" + "'" + Date + "'," + "Title =" + "'" + Title + "'," + "Type =" + "'" + Type + "'," + "AuthorStudio =" + "'" + AuthorStudio + "'," + "Genre = " + "'" + Genre + "'," + "Volumes =" + "'" + Volumes + "'," + "ChaptersEpisodes =" + "'" + ChaptersEpisodes + "'," + "Status =" + "'" + Status + "'" + "WHERE Title = " + "'" + Title + "';"      
                self.cursor.execute(self.query, (Date, Title, Type, AuthorStudio, Genre, Volumes, ChaptersEpisodes, Status, TitlePointer))
                self.conn.commit()

        def DeleteEntryFromDataBase(self, Title):
                self.query = "DELETE FROM Main WHERE Title = ?;"
                self.cursor.execute(self.query, (Title,))
                self.conn.commit()
                self.query2 = "SELECT ImagePath FROM Main WHERE Title = ?"
                self.cursor.execute(self.query2, (Title,))
                imagepath = self.cursor.fetchall()
                for image in imagepath:
                        os.remove("AAnimeimage.jpg")
                self.conn.commit()

        def CustomQuery(self,query):
                return self.cursor.execute(query)

#Initializes an Instance to be used                                
db = DBManager()





                
        
                
                

                










        
