from PyQt4 import QtGui , QtCore
import HikariUI, Additem, Edititem, DbManager, itertools, sys, os
from pathlib import Path


class MainApplication(HikariUI.Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        
        ##Create A Table if it does not exist
        DbManager.db.CreateTable()
        self.FilteredListResult()
        
    def PopulateList(self, query):     
        ##Initialize a Model for the Qlistview
        model = QtGui.QStandardItemModel(self.listView)
                
        ##Initialize List Icon
        listicon = QtGui.QIcon()
        listicon.addPixmap(QtGui.QPixmap("Icons\listicon.png"))


        ##Initialize a List for Qlistview
        titlelist = []
        typelist = []
        
        
        ##Converts Tupple coming from the Database into a List
        self.query = str(query)
        for item in DbManager.db.CustomQuery(self.query):
            titlelist.append(item[0])
            typelist.append(item[1])
    
    
        ##Add each item to Qlistview
        for listitems, typeitems in list(itertools.zip_longest(titlelist,typelist)):
                items = QtGui.QStandardItem(listitems+ " | " + typeitems)
                items.setIcon(listicon)
                model.appendRow(items)
    
    
        self.listView.setModel(model)
    
    ##Get Information of the Selected item on the List
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def GetData(self, index):
        ItemSelected = str(index.data())
        
        global Title,Type
        Title, Type = ItemSelected.split(" | ", 1)
        query = 'SELECT AuthorStudio,Genre,Volumes,ChaptersEpisodes,Status,ImagePath FROM Main WHERE Title = "'+ Title +'" AND Type= '+ '"' + Type + '"'
       
        for items in DbManager.db.CustomQuery(str(query)):
            if Type == "Anime":
                self.volumesLabel.setText("Seasons")
                self.chaptersLabel.setText("Episodes")
            else:
                self.volumesLabel.setText("Volumes")
                self.chaptersLabel.setText("Chapters")                
            self.TitleLineEdit.setText(Title)
            self.TypeLineEdit.setText(Type)
            self.AuthorStudioLineEdit.setText(items[0])
            self.GenreLineEdit.setText(items[1])
            self.VolumesLineEdit.setText(str(items[2]))
            self.ChaptersLineEdit.setText(str(items[3]))
            self.StatusLineEdit.setText(items[4])
            self.picture = QtGui.QPixmap(items[5])
            self.picturesmall = self.picture.scaled(480, 360, QtCore.Qt.KeepAspectRatio)
            
            self.ImageHolder.setPixmap(self.picturesmall)
            
    ##Filter Items on the List by Type
    def FilteredListResult(self):
        ##Filtered Search Results
        if self.actionSelectAll.isChecked():
             ##Default Query for Initial Launch of the Program(Query will Show All Types)
            query = "SELECT Title, Type FROM Main"
            self.PopulateList(query)
            
        if self.actionSelectAnime.isChecked():       
            query = "SELECT Title, Type FROM Main WHERE Type = 'Anime'" 
            self.PopulateList(query)        
        
        if self.actionSelectManga.isChecked() == True:
            query = "SELECT Title, Type FROM Main WHERE Type = 'Manga'" 
            self.PopulateList(query)

        if self.actionSelectLightWebNovel.isChecked() == True:           
            query = "SELECT Title, Type FROM Main WHERE Type = 'Light Novel'" 
            self.PopulateList(query)

    
    ##Brings out the Dialog Box for Adding Entry to the Database
    def AddItem(self):
        self.Window = Additem.Ui_AddDialog()
        
    ##Delete the Current selected item on the list
    def Deletebutton(self):
        quitmessage = "Are you sure you want to delete this entry?".format(Title)
        reply = QtGui.QMessageBox.question(self, "Message", quitmessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
                DbManager.db.DeleteEntryFromDataBase(Title)
                filetoremove = str(Path.cwd())+"\\Images\\"+Title+Type+"image.jpg"
                os.remove(filetoremove)

    ##Edit the information current selected item on the list
    def Editbutton(self):
        self.Window = Edititem.Ui_AddDialog(Title)
            
        
    ##Close the Application
    def ExitApp(self):
        sys.exit()
        

        
##Start Main Application Loop
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Window = MainApplication()
    Window.show()
    app.exec_()
