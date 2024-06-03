from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from sem4.audio import Audio_Item


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,400)


        mainLayout = QHBoxLayout()
        verticalLayout = QVBoxLayout()
        mainLayout.addLayout(verticalLayout)
        self.setLayout(mainLayout)
        self.myLable = QLabel('X')
        myLable2 = QLabel('z')
        myLable3 = QLabel('X1')

        select_file_button = QPushButton('Vybrat FILE')
        spectre_button = QPushButton('Pokazat spectr')
        osc_button = QPushButton('Pokazat Oscillogrammy')

        verticalLayout.addWidget(self.myLable)
        verticalLayout.addWidget(select_file_button)
        verticalLayout.addWidget(spectre_button)
        verticalLayout.addWidget(osc_button)

        mainLayout.addWidget(myLable2)

        
        select_file_button.clicked.connect(self.select_file)

        self.clicks_counter = 0
        
        
    
    def select_file_button_clicked(self):
        print('Najata knopka select_file_button')
    def count_clicks(self):
        self.clicks_counter +=1
        self.myLable.setText(f'Количество нажатий на кнопку = {self.clicks_counter} ')
    def select_file(self):
        filename, filter =QFileDialog.getOpenFileName()
        self.audio_item = Audio_Item(filename)
        self.myLable.setText(f'Выбранный файл: {filename} ')




app =QApplication([])
mainWidget = MyWidget()
mainWidget.show()
app.exec()
