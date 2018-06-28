# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Additem.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PIL import Image
from pathlib import Path
import sys, os, DbManager



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AddDialog(QtGui.QDialog):
    def __init__(self, Title):
        self.Title_ = Title
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.SetData()
        
        self.show()
        
    def setupUi(self, AddDialog):
        AddDialog.setObjectName(_fromUtf8("AddDialog"))
        AddDialog.resize(528, 309)
        AddDialog.setMinimumSize(QtCore.QSize(528, 309))
        AddDialog.setMaximumSize(QtCore.QSize(528, 309))
        AddDialog.setStyleSheet("#AddDialog {background-image: url('Cssbackgrounds/bgcolor.jpg'); background-repeat:repeat-x; background-position: bottom;}QLineEdit {border-radius: 10px; border: 1px solid green;}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Hikarimanlogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddDialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(AddDialog)
        self.buttonBox.setGeometry(QtCore.QRect(440, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.CollectData)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(AddDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 431))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        
        self.QLabelTitle = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.QLabelTitle.setFont(font)
        self.QLabelTitle.setObjectName(_fromUtf8("QLabelTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.QLabelTitle)
        self.IntChecker = QtGui.QIntValidator()
        self.lineEditTitle = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditTitle.setObjectName(_fromUtf8("lineEditTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditTitle)
        
        self.QLabelType = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.QLabelType.setFont(font)
        self.QLabelType.setObjectName(_fromUtf8("QLabelType"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.QLabelType)
        self.comboBoxType = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBoxType.setObjectName(_fromUtf8("comboBoxType"))
        self.comboBoxType.addItem(_fromUtf8(""))
        self.comboBoxType.addItem(_fromUtf8(""))
        self.comboBoxType.addItem(_fromUtf8(""))
        self.comboBoxType.activated[str].connect(self.GetTypeComboBox)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxType)
        
        self.QLabelAuthorStudio = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.QLabelAuthorStudio.setFont(font)
        self.QLabelAuthorStudio.setObjectName(_fromUtf8("QLabelAuthorStudio"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.QLabelAuthorStudio)
        self.lineEditAuthorStudio = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditAuthorStudio.setObjectName(_fromUtf8("lineEditAuthorStudio"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditAuthorStudio)
        self.QLabelGenre = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.QLabelGenre.setFont(font)
        self.QLabelGenre.setObjectName(_fromUtf8("QLabelGenre"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.QLabelGenre)
        self.lineEditGenre = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditGenre.setObjectName(_fromUtf8("lineEditGenre"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditGenre)
        
        self.QLabelVolume = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.QLabelVolume.setFont(font)
        self.QLabelVolume.setObjectName(_fromUtf8("QLabelVolume"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.QLabelVolume)
        self.QLabelChapters = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.QLabelChapters.setFont(font)
        self.QLabelChapters.setObjectName(_fromUtf8("QLabelChapters"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.QLabelChapters)
        self.QLabelStatus = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        
        self.lineEditVolume = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditVolume.setValidator(self.IntChecker)        
        self.lineEditVolume.setObjectName(_fromUtf8("lineEditVolume"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditVolume)
        self.lineEditChapters = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEditChapters.setValidator(self.IntChecker)
        self.lineEditChapters.setObjectName(_fromUtf8("lineEditChapters"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditChapters)        
       
        self.QLabelStatus.setFont(font)
        self.QLabelStatus.setObjectName(_fromUtf8("QLabelStatus"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.QLabelStatus)
        self.comboBoxStatus = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBoxStatus.setObjectName(_fromUtf8("comboBoxStatus"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.comboBoxStatus)
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.comboBoxStatus.addItem(_fromUtf8(""))
        self.comboBoxStatus.activated[str].connect(self.GetStatusComboBox)

        self.QFileDialogLabel = QtGui.QLabel(self.formLayoutWidget)
        self.QFileDialogLabel.setObjectName(_fromUtf8("QFileDialogLabel"))
        self.QFileDialogLabel.setFont(font)
        self.QFileDialogButton = QtGui.QPushButton()
        self.QFileDialogButton.setText("Set an Image")
        self.QFileDialogButton.clicked.connect(self.ImageUploader)
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.QFileDialogLabel)
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.QFileDialogButton)        


        self.retranslateUi(AddDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        AddDialog.setWindowTitle(_translate("AddDialog", "Edit an Entry", None))
        self.QLabelTitle.setText(_translate("AddDialog", "Title", None))
        self.QLabelType.setText(_translate("AddDialog", "Type", None))
        self.comboBoxType.setItemText(0, _translate("AddDialog", "Anime", None))
        self.comboBoxType.setItemText(1, _translate("AddDialog", "Manga", None))
        self.comboBoxType.setItemText(2, _translate("AddDialog", "Light Novel", None))
        self.QLabelStatus.setText(_translate("AddDialog", "Status", None))
        self.comboBoxStatus.setItemText(0, _translate("AddDialog", "Ongoing", None))
        self.comboBoxStatus.setItemText(1, _translate("AddDialog", "Complete", None))
        self.comboBoxStatus.setItemText(2, _translate("AddDialog", "Hiatus", None))    
        self.QLabelAuthorStudio.setText(_translate("AddDialog", "Author/Studio", None))
        self.QLabelGenre.setText(_translate("AddDialog", "Genre", None))
        self.QLabelVolume.setText(_translate("AddDialog", "Volume/Season", None))
        self.QLabelChapters.setText(_translate("AddDialog", "Chapters/Episodes", None))
        self.QFileDialogLabel.setText(_translate("AddDialog","Image", None))
        


    Functionhasbeencalled = "False"

    ##Save All the Edited Information to the DataBase
    def CollectData(self):
        self.TitleData = self.lineEditTitle.text()
        self.typecombobox = self.GetTypeComboBox()
        self.AuthorStudioData = self.lineEditAuthorStudio.text()
        self.GenreData = self.lineEditGenre.text()
        self.VolumeData = self.lineEditVolume.text()
        self.ChaptersData = self.lineEditChapters.text()
        self.statuscombobox = self.GetStatusComboBox()
        if self.Functionhasbeencalled == "True":
            programdirectory = str(Path.cwd())+ "\\Images\\"+self.TitleData+self.typecombobox+"image.jpg"
            if os.path.isfile(programdirectory):
                os.remove(programdirectory)
            openedfile.save(programdirectory,"JPEG")
            DbManager.db.CustomQuery("UPDATE Main SET ImagePath ='{}' WHERE Title = '{}'".format(programdirectory, self.Title_))


            


            

        DbManager.db.EditEntryToDataBase(self.TitleData,self.typecombobox,self.AuthorStudioData,self.GenreData,self.VolumeData,self.ChaptersData,self.statuscombobox, self.Title_)
       
        
    def GetTypeComboBox(self):
        return self.comboBoxType.currentText()


    def GetStatusComboBox(self):
        return self.comboBoxStatus.currentText()
    
    ##Saves an Image to the File System
    def ImageUploader(self):
        dirs = ""
        filters = "Images (*.png *.jpg)"
        file = QtGui.QFileDialog.getOpenFileName(self, "Set an Image", dirs, filters)
        global openedfile
        openedfile = Image.open(file)
        self.Functionhasbeencalled = "True"

    ##Grab the Information of the Selected Item from the Database
    def SetData(self):
        query = "SELECT Title, Type,AuthorStudio,Genre,Volumes,ChaptersEpisodes,Status FROM Main WHERE Title =" + "'" + self.Title_ + "';"
        for items in DbManager.db.CustomQuery(query):
            self.lineEditTitle.setText(items[0])
            typeindex = self.comboBoxType.findText(items[1])
            self.comboBoxType.setCurrentIndex(typeindex)
            self.lineEditAuthorStudio.setText(items[2])
            self.lineEditGenre.setText(items[3])
            self.lineEditVolume.setText(str(items[4]))
            self.lineEditChapters.setText(str(items[5]))
            statusindex = self.comboBoxStatus.findText(items[6])
            self.comboBoxStatus.setCurrentIndex(statusindex)


        



    
    
        
        
            




