from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import data
from data import heroes_dict

# Create thewindow with QML and split it into two equal parts
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AFK Compendium")
        self.setWindowIcon(QIcon("AFK Compendium/images/heroes/afklogo.png"))
        self.setGeometry(0, 0, 1200, 800)
        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.setCentralWidget(self.splitter)
        self.splitter.setStyleSheet("QSplitter::handle {background-color: #1f1f1f;}")
        self.splitter.setStyleSheet("QSplitter::handle:horizontal {width: 1px;}")
        self.splitter.setStyleSheet("QSplitter::handle:vertical {height: 1px;}")
        self.splitter.setStyleSheet("QSplitter::handle:horizontal:hover {width: 1px;}")
        self.splitter.setStyleSheet("QSplitter::handle:vertical:hover {height: 1px;}")

        # Create the left side of the window
        self.left_widget = QWidget()
        self.left_widget.setStyleSheet("background-color: #1f1f1f;")
        self.left_widget.setFixedWidth(200)
        self.splitter.addWidget(self.left_widget)
        self.left_layout = QVBoxLayout()
        self.left_widget.setLayout(self.left_layout)

        # Create the right side of the window
        self.right_widget = QWidget()
        self.right_widget.setStyleSheet("background-color: #1f1f1f;")
        self.splitter.addWidget(self.right_widget)
        self.right_layout = QVBoxLayout()
        self.right_widget.setLayout(self.right_layout)

        # Create the search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search")
        self.search_bar.setStyleSheet("background-color: #1f1f1f; color: #ffffff; border: 1px solid #ffffff; border-radius: 5px; padding: 5px;")
        self.search_bar.textChanged.connect(self.search)
        self.left_layout.addWidget(self.search_bar)

        # Create the list of heroes
        self.heroes_list = QListWidget()
        self.heroes_list.setStyleSheet("background-color: #1f1f1f; color: #ffffff; border: 1px solid #ffffff; border-radius: 5px; padding: 5px;")
        self.left_layout.addWidget(self.heroes_list)
        
        # Create the hero faction image and set it into the right side of the grid
        self.hero_faction_img = QLabel()
        self.hero_faction_img.setPixmap(QPixmap("AFK Compendium/images/factions/afklogo.png"))
        self.hero_faction_img.setAlignment(Qt.AlignCenter)
        self.hero_faction_img.setFixedHeight(50)
        self.hero_faction_img.setFixedWidth(50)
        self.right_layout.addWidget(self.hero_faction_img)
        self.right_layout.setAlignment(self.hero_faction_img, Qt.AlignCenter)
        
        # Create the hero name and align in the center
        self.hero_name = QLabel()
        self.hero_name.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_name.setFont(QFont("Arial", 20, QFont.Bold))
        self.right_layout.addWidget(self.hero_name)
        self.right_layout.setAlignment(self.hero_name, Qt.AlignCenter)
        

        # Create the hero faction and align in the center
        self.hero_faction = QLabel()
        self.hero_faction.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_faction.setFont(QFont("Arial", 15, QFont.Bold))
        self.right_layout.addWidget(self.hero_faction)
        self.right_layout.setAlignment(self.hero_faction, Qt.AlignCenter)

        # Create the hero role and align in the center
        self.hero_role = QLabel()
        self.hero_role.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_role.setFont(QFont("Arial", 15, QFont.Bold))
        self.right_layout.addWidget(self.hero_role)
        self.right_layout.setAlignment(self.hero_role, Qt.AlignCenter)

        # Create the hero image and align in the center
        self.hero_image = QLabel() 
        self.hero_image.setPixmap(QPixmap("AFK Compendium/images/heroes/afklogo.png"))
        self.hero_image.setAlignment(Qt.AlignCenter)
        self.hero_image.setFixedHeight(300)
        self.hero_image.setFixedWidth(300)
        self.right_layout.addWidget(self.hero_image)
        self.right_layout.setAlignment(self.hero_image, Qt.AlignCenter)

        # Create the signature item title and align in the left
        self.sig_item_title = QLabel()
        self.sig_item_title.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.sig_item_title.setFont(QFont("Arial", 15, QFont.Bold))
        self.sig_item_title.setText("Signature Item")
        self.right_layout.addWidget(self.sig_item_title)
        self.right_layout.setAlignment(self.sig_item_title, Qt.AlignRight)
        
        # Create the hero signature item image
        self.hero_sig_img = QLabel()
        self.hero_sig_img.setPixmap(QPixmap("AFK Compendium/images/factions/afklogo.png"))
        self.hero_sig_img.setAlignment(Qt.AlignLeft)
        self.hero_sig_img.setFixedHeight(150)
        self.hero_sig_img.setFixedWidth(150)
        self.right_layout.addWidget(self.hero_sig_img)

        # Set the hero signature item image on the left side of the right side of the window
        self.right_layout.setAlignment(self.hero_sig_img, Qt.AlignRight)

        # Set the hero signature item name and align right
        self.hero_sig_name = QLabel()
        self.hero_sig_name.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_sig_name.setFont(QFont("Arial", 15, QFont.Bold))
        self.right_layout.addWidget(self.hero_sig_name)
        self.right_layout.setAlignment(self.hero_sig_name, Qt.AlignRight)

        # Create a header for the hero skills with a font size of 20
        self.hero_skills_header = QLabel("Hero Skills")
        self.hero_skills_header.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_skills_header.setFont(QFont("Arial", 20))
        self.right_layout.addWidget(self.hero_skills_header)

        # Create the hero skill 1
        self.hero_skill_1 = QLabel()
        self.hero_skill_1.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_skill_1.setFont(QFont("Arial", 15, QFont.Bold))
        self.right_layout.addWidget(self.hero_skill_1)

        # Create the hero skill 2
        self.hero_skill_2 = QLabel()
        self.hero_skill_2.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_skill_2.setFont(QFont("Arial", 15, QFont.Bold))
        self.right_layout.addWidget(self.hero_skill_2)

        # Create the hero skill 3
        self.hero_skill_3 = QLabel()
        self.hero_skill_3.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_skill_3.setFont(QFont("Arial", 15, QFont.Bold))
        self.right_layout.addWidget(self.hero_skill_3)

        # Create the hero skill 4
        self.hero_skill_4 = QLabel()
        self.hero_skill_4.setStyleSheet("background-color: #1f1f1f; color: #ffffff; padding: 5px;")
        self.hero_skill_4.setFont(QFont("Arial", 15, QFont.Bold))
        self.right_layout.addWidget(self.hero_skill_4)

        
        # Add the heroes to the list
        for hero in heroes_dict:
            self.heroes_list.addItem(hero)

        # When a hero is clicked, show its content
        self.heroes_list.itemClicked.connect(self.show_hero_info)
        self.heroes_list.itemClicked.connect(self.show_hero_image)
        # resize the image to fit the label
        self.hero_image.setScaledContents(True)

        # resize the image to fit the label
        self.hero_sig_img.setScaledContents(True)

        # resize the image to fit the label
        self.hero_faction_img.setScaledContents(True)
    
    # Show the hero image when clicked
    def show_hero_image(self):
        hero = self.heroes_list.currentItem().text()
        self.hero_image.setPixmap(QPixmap(heroes_dict[hero]['img']))
        print(heroes_dict[hero]['img'])
        self.hero_sig_img.setPixmap(QPixmap(heroes_dict[hero]['sig_img']))
        print(heroes_dict[hero]['sig_img'])
        self.hero_faction_img.setPixmap(QPixmap(heroes_dict[hero]['fac_img']))
        print(heroes_dict[hero]['fac_img'])

    # Show the dictionary name, faction, role, skill_1, skill_2, and skill_3, and skill_4 of a hero individually when clicked 
    def show_hero_info(self):
        hero = self.heroes_list.currentItem().text()
        self.hero_name.setText(heroes_dict[hero]["name"])
        print(heroes_dict[hero]["name"])
        self.hero_faction.setText(heroes_dict[hero]["fac"])
        self.hero_role.setText(heroes_dict[hero]["role"])
        self.hero_sig_name.setText(heroes_dict[hero]["sig"])
        self.hero_skill_1.setText(heroes_dict[hero]['skills']['skill_1'])
        self.hero_skill_2.setText(heroes_dict[hero]['skills']['skill_2'])
        self.hero_skill_3.setText(heroes_dict[hero]['skills']['skill_3'])
        self.hero_skill_4.setText(heroes_dict[hero]['skills']['skill_4'])

# Search for a hero
    def search(self):
        self.heroes_list.clear()
        for hero in heroes_dict:
            if self.search_bar.text().lower() in hero.lower():
                self.heroes_list.addItem(hero)
            
        
# Run the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


                                 



