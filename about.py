# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QWidget)

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.setWindowModality(Qt.WindowModality.WindowModal)
        AboutWindow.resize(432, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(AboutWindow.sizePolicy().hasHeightForWidth())
        AboutWindow.setSizePolicy(sizePolicy)
        AboutWindow.setMinimumSize(QSize(432, 560))
        AboutWindow.setMaximumSize(QSize(432, 560))
        icon = QIcon()
        icon.addFile(u"pomodoro_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AboutWindow.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(AboutWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.AboutText = QLabel(AboutWindow)
        self.AboutText.setObjectName(u"AboutText")
        self.AboutText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.AboutText, 1, 0, 1, 1)

        self.AboutLabel = QLabel(AboutWindow)
        self.AboutLabel.setObjectName(u"AboutLabel")
        self.AboutLabel.setMinimumSize(QSize(391, 100))
        self.AboutLabel.setScaledContents(False)
        self.AboutLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.AboutLabel, 0, 0, 1, 1)

        self.pushButton = QPushButton(AboutWindow)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(100, 25))
        self.pushButton.setMaximumSize(QSize(100, 25))
        self.pushButton.setBaseSize(QSize(50, 50))
        self.pushButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 50)
        self.gridLayout.setRowStretch(2, 20)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.AboutText.setText(QCoreApplication.translate("AboutWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u0430 \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043f\u0435\u0442-\u043f\u0440\u043e\u0435\u043a\u0442\u0430. </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        ">\u0412\u0441\u0435 \u0438\u043a\u043e\u043d\u043a\u0438 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a \u0432\u0437\u044f\u0442\u044b \u0438\u0437 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0445 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u043e\u0432 (www.flaticon.com).</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u044f\u0435\u0442\u0441\u044f \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041c\u043e\u0439 <a href=\"https://github.com/Ivndnv\"><sp"
                        "an style=\" text-decoration: underline; color:#8f7024;\">github</span></a></p></body></html>", None))
        self.AboutLabel.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700;\">\u041e \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("AboutWindow", u"OK", None))
    # retranslateUi

