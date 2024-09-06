import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Aplikasi PyQt")

exit_button = QPushButton("Exit", window)
exit_button.clicked.connect(QApplication.quit)
exit_button.resize(100,30)
exit_button.move(50,50)

window.setGeometry(100, 100, 200, 100)
window.show()

sys.exit(app.exec_())