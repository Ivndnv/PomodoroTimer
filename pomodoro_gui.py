# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pomodoro.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QFrame,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(448, 684)
        icon = QIcon()
        icon.addFile(u"pomodoro_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TimerLabel = QLabel(self.centralwidget)
        self.TimerLabel.setObjectName(u"TimerLabel")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.TimerLabel.setFont(font)
        self.TimerLabel.setFrameShape(QFrame.Shape.Panel)
        self.TimerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TimerLabel.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.TimerLabel)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TimerButtonsLayout = QHBoxLayout()
        self.TimerButtonsLayout.setSpacing(5)
        self.TimerButtonsLayout.setObjectName(u"TimerButtonsLayout")
        self.TimerButtonsLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.StartTimerButton = QPushButton(self.centralwidget)
        self.StartTimerButton.setObjectName(u"StartTimerButton")
        self.StartTimerButton.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u"play.ico", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon1.addFile(u"pause.ico", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.StartTimerButton.setIcon(icon1)
        self.StartTimerButton.setCheckable(True)
        self.StartTimerButton.setChecked(False)

        self.verticalLayout.addWidget(self.StartTimerButton)

        self.Text = QLabel(self.centralwidget)
        self.Text.setObjectName(u"Text")
        self.Text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Text)

        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setAutoFillBackground(False)
        self.timeEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhSensitiveData)
        self.timeEdit.setWrapping(True)
        self.timeEdit.setMaximumTime(QTime(0, 59, 59))
        self.timeEdit.setCurrentSection(QDateTimeEdit.Section.MinuteSection)

        self.verticalLayout.addWidget(self.timeEdit)

        self.StopTimerButton = QPushButton(self.centralwidget)
        self.StopTimerButton.setObjectName(u"StopTimerButton")
        self.StopTimerButton.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"free-icon-restart-3973138.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StopTimerButton.setIcon(icon2)

        self.verticalLayout.addWidget(self.StopTimerButton)

        self.PomodoroTimerButton = QPushButton(self.centralwidget)
        self.PomodoroTimerButton.setObjectName(u"PomodoroTimerButton")
        self.PomodoroTimerButton.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u"pomodoro_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.PomodoroTimerButton.setIcon(icon3)
        self.PomodoroTimerButton.setFlat(False)

        self.verticalLayout.addWidget(self.PomodoroTimerButton)


        self.TimerButtonsLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.TimerButtonsLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VolumeSettingsLabel = QLabel(self.centralwidget)
        self.VolumeSettingsLabel.setObjectName(u"VolumeSettingsLabel")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.VolumeSettingsLabel.setFont(font1)
        self.VolumeSettingsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.VolumeSettingsLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.VolumeSlider = QSlider(self.centralwidget)
        self.VolumeSlider.setObjectName(u"VolumeSlider")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setValue(50)
        self.VolumeSlider.setSliderPosition(50)
        self.VolumeSlider.setOrientation(Qt.Orientation.Horizontal)
        self.VolumeSlider.setInvertedAppearance(False)

        self.horizontalLayout.addWidget(self.VolumeSlider)

        self.VolumeCheckBox = QCheckBox(self.centralwidget)
        self.VolumeCheckBox.setObjectName(u"VolumeCheckBox")
        self.VolumeCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.VolumeCheckBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 448, 33))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        self.StartTimerButton.setDefault(True)
        self.StopTimerButton.setDefault(True)
        self.PomodoroTimerButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pomodoro Timer App", None))
        self.TimerLabel.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.StartTimerButton.setText("")
        self.Text.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0440\u0435\u043c\u044f \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 \u041c:\u0421\u0435\u043a", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"m:ss", None))
        self.StopTimerButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0422\u0430\u0439\u043c\u0435\u0440", None))
        self.PomodoroTimerButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c Pomodoro ", None))
        self.VolumeSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0417\u0432\u0443\u043a\u0430", None))
        self.VolumeCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0437\u0432\u0443\u043a", None))
    # retranslateUi

