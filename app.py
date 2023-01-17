import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import webbrowser


class PrivateBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('Private Browser')

        # Create the back button
        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.back)

        # Create the forward button
        self.forward_button = QPushButton('Forward')
        self.forward_button.clicked.connect(self.forward)

        # Create the zoom in button
        self.zoom_in_button = QPushButton('Zoom In')
        self.zoom_in_button.clicked.connect(self.zoom_in)

        # Create the zoom out button
        self.zoom_out_button = QPushButton('Zoom Out')
        self.zoom_out_button.clicked.connect(self.zoom_out)

        # Create the bookmark button
        self.bookmark_button = QPushButton('Bookmark')
        self.bookmark_button.clicked.connect(self.bookmark)

        # Create the search button
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search)

        # Create the address bar
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_page)

        # Create the tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create the top layout
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addWidget(self.forward_button)
        top_layout.addWidget(self.zoom_in_button)
        top_layout.addWidget(self.zoom_out_button)
        top_layout.addWidget(self.bookmark_button)
        top_layout.addWidget(self.search_button)
        top_layout.addWidget(self.address_bar)

        # Add the top layout to the main layout
        main_layout.addLayout(top_layout)

        # Add the tab widget to the main layout
        main_layout.addWidget(self.tab_widget)

        # Create the central widget and set its layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # Create a new tab with a web view
        self.new_tab()

        # Create a list to store the bookmarks
        self.bookmarks = []

    def back(self):
        # Get the current web view
        web_view = self.tab_widget.currentWidget()

        # Go back in the web view's history
        web_view.back()

    def forward(self):
        # Get the current web view
        web_view = self.tab_widget.currentWidget()

        # Go forward in the web view's history
        web_view.forward()

    def zoom_in(self):
        # Get the current web view
        web_view = self.tab_widget.currentWidget()

        # Zoom in on the web view
        web_view.setZoomFactor(web_view.zoomFactor() + 0.1)

    def zoom_out(self):
        # Get the current web view
        web_view = self.tab_widget.currentWidget()

        # Zoom out on the web view
        web_view.setZoomFactor(web_view.zoomFactor() - 0.1)

    def bookmark(self):
        # Get the current web view
        web_view = self.tab_widget.currentWidget()

        # Get the current URL
        url = web_view.url().toString()

        # Add the URL to the bookmarks list
        self.bookmarks.append(url)

        # Print the bookmarks list
        print(self.bookmarks)

    def search(self):
        pass

    def close_tab(self, index):
        # Close the tab at the given index
        self.tab_widget.removeTab(index)
if name == 'main':
    app = QApplication(sys.argv)
    browser = PrivateBrowser()
    browser.show()
    sys.exit(app.exec_())
