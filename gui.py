import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from encoding import *


class App(QMainWindow):
    left = 400
    top = 100
    width = 700
    height = 740

    leftAlign = 20
    topAlign = 20
    bufferX = 20
    bufferY = 30

    passwordLabelX = leftAlign
    passwordLabelY = topAlign
    labelHeight = 30

    passwordBoxX = leftAlign
    passwordBoxY = passwordLabelY + labelHeight
    passwordBoxWidth = width - leftAlign * 2
    passwordBoxHeight = labelHeight

    textLabelX = leftAlign
    textLabelY = passwordBoxY + passwordBoxHeight + 2 * bufferY

    messageBoxX = leftAlign
    messageBoxY = textLabelY + bufferY
    messageBoxWidth = width - leftAlign * 2
    messageBoxHeight = passwordBoxHeight * 5

    buttonX = leftAlign
    buttonY = messageBoxY + messageBoxHeight + bufferY
    buttonWidth = int(width / 3) - bufferX * 2
    buttonHeight = 40
    buttonX2 = buttonX + buttonWidth + bufferX
    buttonX3 = buttonX2 + buttonWidth + bufferX
    buttonY2 = buttonY + buttonHeight + bufferY

    resultLabelX = leftAlign
    resultLabelY = buttonY2 + buttonHeight + 2 * bufferY

    resultBoxX = leftAlign
    resultBoxY = resultLabelY + bufferY
    resultBoxWidth = width - leftAlign * 2
    resultBoxHeight = passwordBoxHeight * 5

    def __init__(self):
        super().__init__()
        self.title = 'Password Ciphers'
        self.encrypt = True
        self.encyrpter = Encrypting()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Password text Line
        self.PasswordText = QLabel(self)
        self.PasswordText.move(self.passwordLabelX, self.passwordLabelY)
        self.PasswordText.setText("Password")

        # Create textbox for Password
        self.passwordBox = QLineEdit(self)
        self.passwordBox.move(self.passwordBoxX, self.passwordBoxY)
        self.passwordBox.resize(self.passwordBoxWidth, self.passwordBoxHeight)

        # Create Message text line
        self.textLabel = QLabel(self)
        self.textLabel.move(self.textLabelX, self.textLabelY)
        self.textLabel.setText("Text")

        # Create textbox for message
        self.textboxIn = QPlainTextEdit(self)
        self.textboxIn.move(self.messageBoxX, self.messageBoxY)
        self.textboxIn.resize(self.messageBoxWidth, self.messageBoxHeight)

        # Create a button in the window
        self.button1 = QPushButton('Caesar', self)
        self.button1.move(self.buttonX, self.buttonY2)
        self.button1.resize(self.buttonWidth, self.buttonHeight)

        self.button2 = QPushButton('Password', self)
        self.button2.move(self.buttonX2, self.buttonY2)
        self.button2.resize(self.buttonWidth, self.buttonHeight)

        self.button3 = QPushButton('Hybrid', self)
        self.button3.move(self.buttonX3, self.buttonY2)
        self.button3.resize(self.buttonWidth, self.buttonHeight)

        # Create toggle button
        self.buttonE = QPushButton('Encrypt Mode - Click to change', self)
        self.buttonE.move(self.buttonX, self.buttonY)
        self.buttonE.resize(self.buttonWidth * 3 + 2 * self.bufferX, self.buttonHeight)
        self.buttonE.setStyleSheet("background-color: red")

        # connect button to function on_click
        self.button1.clicked.connect(self.caesarClicked)
        self.button2.clicked.connect(self.passwordClicked)
        self.button3.clicked.connect(self.hybridClicked)
        self.buttonE.clicked.connect(self.toggle)

        # Create result text Line
        self.resultText = QLabel(self)
        self.resultText.move(self.resultLabelX, self.resultLabelY)
        self.resultText.setText("Result")

        # Create textbox for result
        self.resultBox = QPlainTextEdit(self)
        self.resultBox.move(self.resultBoxX, self.resultBoxY)
        self.resultBox.resize(self.resultBoxWidth, self.resultBoxHeight)

        self.show()

    @pyqtSlot()
    def caesarClicked(self):
        textboxValue = self.textboxIn.toPlainText()
        pw = self.passwordBox.text()
        print(pw)
        if pw == '':
            pw = '0'

        if not pw.isdigit():
            QMessageBox.question(self, 'Error incorrect password type', "Caesar passwords must be numberic",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if self.encrypt is True:
            result = self.encyrpter.caesarEncrypt(textboxValue, pw)
        else:
            result = self.encyrpter.caesarDecrypt(textboxValue, pw)
        self.resultBox.setPlainText(result)

    def passwordClicked(self):
        textboxValue = self.textboxIn.toPlainText()
        pw = self.passwordBox.text()
        if self.encrypt is True:
            result = self.encyrpter.passwordEncrypt(textboxValue, pw)
        else:
            result = self.encyrpter.passwordDecrypt(textboxValue, pw)
        self.resultBox.setPlainText(result)

    def hybridClicked(self):
        textboxValue = self.textboxIn.toPlainText()
        pw = self.passwordBox.text()
        if self.encrypt is True:
            result = self.encyrpter.hybridEncrypt(textboxValue, pw)
        else:
            result = self.encyrpter.hybridDecrypt(textboxValue, pw)
        self.resultBox.setPlainText(result)

    def toggle(self):
        self.encrypt = not self.encrypt
        if self.encrypt is True:
            self.buttonE.setText("Encrypt Mode  - Click to change")
            self.buttonE.setStyleSheet("background-color: red")
        else:
            self.buttonE.setText("Decrypt Mode  - Click to change")
            self.buttonE.setStyleSheet("background-color: green")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
