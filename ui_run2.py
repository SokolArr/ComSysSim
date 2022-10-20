# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from plot_area_wid import plot_area_wid

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1953, 1024)
        MainWindow.setMinimumSize(QSize(1400, 800))
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionPlot = QAction(MainWindow)
        self.actionPlot.setObjectName(u"actionPlot")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_tab_wid = QTabWidget(self.centralwidget)
        self.left_tab_wid.setObjectName(u"left_tab_wid")
        self.left_tab_wid.setMaximumSize(QSize(600, 16777215))
        self.instruct_tab = QWidget()
        self.instruct_tab.setObjectName(u"instruct_tab")
        self.left_tab_wid.addTab(self.instruct_tab, "")
        self.PSK_tab = QWidget()
        self.PSK_tab.setObjectName(u"PSK_tab")
        self.verticalLayout = QVBoxLayout(self.PSK_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_PSK_wid = QWidget(self.PSK_tab)
        self.main_PSK_wid.setObjectName(u"main_PSK_wid")
        self.main_PSK_wid.setMinimumSize(QSize(0, 600))
        self.verticalLayout_34 = QVBoxLayout(self.main_PSK_wid)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.params_wid_PSK = QGroupBox(self.main_PSK_wid)
        self.params_wid_PSK.setObjectName(u"params_wid_PSK")
        self.params_wid_PSK.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.params_wid_PSK)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.main_params_PSK_wid = QScrollArea(self.params_wid_PSK)
        self.main_params_PSK_wid.setObjectName(u"main_params_PSK_wid")
        self.main_params_PSK_wid.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.main_params_PSK_wid.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.main_params_PSK_wid.setWidgetResizable(True)
        self.scrollAreaWidgetContents_PSK = QWidget()
        self.scrollAreaWidgetContents_PSK.setObjectName(u"scrollAreaWidgetContents_PSK")
        self.scrollAreaWidgetContents_PSK.setGeometry(QRect(0, 0, 519, 457))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_PSK)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.message_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.message_PSK.setObjectName(u"message_PSK")
        self.verticalLayout_36 = QVBoxLayout(self.message_PSK)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.message_PSK_lable = QLabel(self.message_PSK)
        self.message_PSK_lable.setObjectName(u"message_PSK_lable")

        self.verticalLayout_36.addWidget(self.message_PSK_lable)

        self.PSK_input = QLineEdit(self.message_PSK)
        self.PSK_input.setObjectName(u"PSK_input")
        self.PSK_input.setFrame(True)
        self.PSK_input.setClearButtonEnabled(True)

        self.verticalLayout_36.addWidget(self.PSK_input)


        self.verticalLayout_35.addWidget(self.message_PSK)

        self.type_signal_wid_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.type_signal_wid_PSK.setObjectName(u"type_signal_wid_PSK")
        self.type_signal_wid_PSK.setMinimumSize(QSize(0, 60))
        self.verticalLayout_10 = QVBoxLayout(self.type_signal_wid_PSK)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.signal_type_mess_PSK = QLabel(self.type_signal_wid_PSK)
        self.signal_type_mess_PSK.setObjectName(u"signal_type_mess_PSK")
        self.signal_type_mess_PSK.setMinimumSize(QSize(0, 10))

        self.verticalLayout_10.addWidget(self.signal_type_mess_PSK)

        self.combobox_signal_type_PSK = QComboBox(self.type_signal_wid_PSK)
        self.combobox_signal_type_PSK.addItem("")
        self.combobox_signal_type_PSK.addItem("")
        self.combobox_signal_type_PSK.setObjectName(u"combobox_signal_type_PSK")

        self.verticalLayout_10.addWidget(self.combobox_signal_type_PSK)


        self.verticalLayout_35.addWidget(self.type_signal_wid_PSK)

        self.mod_wid_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.mod_wid_PSK.setObjectName(u"mod_wid_PSK")
        self.mod_wid_PSK.setMinimumSize(QSize(0, 60))
        self.verticalLayout_11 = QVBoxLayout(self.mod_wid_PSK)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.mod_label_PSK = QLabel(self.mod_wid_PSK)
        self.mod_label_PSK.setObjectName(u"mod_label_PSK")

        self.verticalLayout_11.addWidget(self.mod_label_PSK)

        self.combobox_coef_PSK = QComboBox(self.mod_wid_PSK)
        self.combobox_coef_PSK.addItem("")
        self.combobox_coef_PSK.addItem("")
        self.combobox_coef_PSK.addItem("")
        self.combobox_coef_PSK.addItem("")
        self.combobox_coef_PSK.addItem("")
        self.combobox_coef_PSK.setObjectName(u"combobox_coef_PSK")

        self.verticalLayout_11.addWidget(self.combobox_coef_PSK)


        self.verticalLayout_35.addWidget(self.mod_wid_PSK)

        self.noise_wid_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.noise_wid_PSK.setObjectName(u"noise_wid_PSK")
        self.noise_wid_PSK.setMinimumSize(QSize(0, 60))
        self.verticalLayout_12 = QVBoxLayout(self.noise_wid_PSK)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.noise_label_PSK = QLabel(self.noise_wid_PSK)
        self.noise_label_PSK.setObjectName(u"noise_label_PSK")

        self.verticalLayout_12.addWidget(self.noise_label_PSK)

        self.combobox_noise_PSK = QComboBox(self.noise_wid_PSK)
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.addItem("")
        self.combobox_noise_PSK.setObjectName(u"combobox_noise_PSK")

        self.verticalLayout_12.addWidget(self.combobox_noise_PSK)


        self.verticalLayout_35.addWidget(self.noise_wid_PSK)

        self.decision_wid_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.decision_wid_PSK.setObjectName(u"decision_wid_PSK")
        self.decision_wid_PSK.setMinimumSize(QSize(0, 60))
        self.verticalLayout_37 = QVBoxLayout(self.decision_wid_PSK)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.decision_label_PSK = QLabel(self.decision_wid_PSK)
        self.decision_label_PSK.setObjectName(u"decision_label_PSK")

        self.verticalLayout_37.addWidget(self.decision_label_PSK)

        self.combobox_decision_PSK = QComboBox(self.decision_wid_PSK)
        self.combobox_decision_PSK.addItem("")
        self.combobox_decision_PSK.addItem("")
        self.combobox_decision_PSK.setObjectName(u"combobox_decision_PSK")

        self.verticalLayout_37.addWidget(self.combobox_decision_PSK)


        self.verticalLayout_35.addWidget(self.decision_wid_PSK)

        self.grey_wid_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.grey_wid_PSK.setObjectName(u"grey_wid_PSK")
        self.grey_wid_PSK.setMinimumSize(QSize(0, 60))
        self.verticalLayout_38 = QVBoxLayout(self.grey_wid_PSK)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.grey_label_PSK = QLabel(self.grey_wid_PSK)
        self.grey_label_PSK.setObjectName(u"grey_label_PSK")

        self.verticalLayout_38.addWidget(self.grey_label_PSK)

        self.combobox_grey_PSK = QComboBox(self.grey_wid_PSK)
        self.combobox_grey_PSK.addItem("")
        self.combobox_grey_PSK.addItem("")
        self.combobox_grey_PSK.setObjectName(u"combobox_grey_PSK")

        self.verticalLayout_38.addWidget(self.combobox_grey_PSK)


        self.verticalLayout_35.addWidget(self.grey_wid_PSK)

        self.phase_wid_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.phase_wid_PSK.setObjectName(u"phase_wid_PSK")
        self.phase_wid_PSK.setMinimumSize(QSize(0, 40))
        self.phase_label_PSK = QLabel(self.phase_wid_PSK)
        self.phase_label_PSK.setObjectName(u"phase_label_PSK")
        self.phase_label_PSK.setGeometry(QRect(10, 10, 51, 21))
        self.combobox_phase_PSK = QComboBox(self.phase_wid_PSK)
        self.combobox_phase_PSK.addItem("")
        self.combobox_phase_PSK.addItem("")
        self.combobox_phase_PSK.addItem("")
        self.combobox_phase_PSK.addItem("")
        self.combobox_phase_PSK.setObjectName(u"combobox_phase_PSK")
        self.combobox_phase_PSK.setGeometry(QRect(60, 10, 431, 22))

        self.verticalLayout_35.addWidget(self.phase_wid_PSK)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer)

        self.main_params_PSK_wid.setWidget(self.scrollAreaWidgetContents_PSK)

        self.horizontalLayout_8.addWidget(self.main_params_PSK_wid)


        self.verticalLayout_34.addWidget(self.params_wid_PSK)

        self.other_prefs_PSK = QTabWidget(self.main_PSK_wid)
        self.other_prefs_PSK.setObjectName(u"other_prefs_PSK")
        self.other_prefs_PSK.setMinimumSize(QSize(0, 400))
        self.other_prefs_PSK.setMaximumSize(QSize(600, 600))
        self.other_prefs_wid_PSK = QWidget()
        self.other_prefs_wid_PSK.setObjectName(u"other_prefs_wid_PSK")
        self.verticalLayout_39 = QVBoxLayout(self.other_prefs_wid_PSK)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.checkBox_show_sig_cons_psk = QCheckBox(self.other_prefs_wid_PSK)
        self.checkBox_show_sig_cons_psk.setObjectName(u"checkBox_show_sig_cons_psk")

        self.verticalLayout_39.addWidget(self.checkBox_show_sig_cons_psk)

        self.sid_PSK = QGroupBox(self.other_prefs_wid_PSK)
        self.sid_PSK.setObjectName(u"sid_PSK")
        self.sid_PSK.setMinimumSize(QSize(0, 200))
        self.verticalLayout_42 = QVBoxLayout(self.sid_PSK)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_length_PSK = QLabel(self.sid_PSK)
        self.label_length_PSK.setObjectName(u"label_length_PSK")

        self.verticalLayout_42.addWidget(self.label_length_PSK)

        self.comboBox_length_PSK = QComboBox(self.sid_PSK)
        self.comboBox_length_PSK.addItem("")
        self.comboBox_length_PSK.addItem("")
        self.comboBox_length_PSK.addItem("")
        self.comboBox_length_PSK.addItem("")
        self.comboBox_length_PSK.addItem("")
        self.comboBox_length_PSK.setObjectName(u"comboBox_length_PSK")

        self.verticalLayout_42.addWidget(self.comboBox_length_PSK)

        self.pushButton_generate_sid_PSK = QPushButton(self.sid_PSK)
        self.pushButton_generate_sid_PSK.setObjectName(u"pushButton_generate_sid_PSK")

        self.verticalLayout_42.addWidget(self.pushButton_generate_sid_PSK)

        self.plainText_sid_PSK = QPlainTextEdit(self.sid_PSK)
        self.plainText_sid_PSK.setObjectName(u"plainText_sid_PSK")

        self.verticalLayout_42.addWidget(self.plainText_sid_PSK)


        self.verticalLayout_39.addWidget(self.sid_PSK)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_2)

        self.other_prefs_PSK.addTab(self.other_prefs_wid_PSK, "")
        self.scheme_PSK = QWidget()
        self.scheme_PSK.setObjectName(u"scheme_PSK")
        self.other_prefs_PSK.addTab(self.scheme_PSK, "")

        self.verticalLayout_34.addWidget(self.other_prefs_PSK)

        self.plot_PSK = QPushButton(self.main_PSK_wid)
        self.plot_PSK.setObjectName(u"plot_PSK")

        self.verticalLayout_34.addWidget(self.plot_PSK)

        self.apply_PSK_but = QCheckBox(self.main_PSK_wid)
        self.apply_PSK_but.setObjectName(u"apply_PSK_but")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        self.apply_PSK_but.setFont(font)

        self.verticalLayout_34.addWidget(self.apply_PSK_but)


        self.verticalLayout.addWidget(self.main_PSK_wid)

        self.left_tab_wid.addTab(self.PSK_tab, "")
        self.QAM_tab = QWidget()
        self.QAM_tab.setObjectName(u"QAM_tab")
        self.verticalLayout_9 = QVBoxLayout(self.QAM_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.main_QAM_wid = QWidget(self.QAM_tab)
        self.main_QAM_wid.setObjectName(u"main_QAM_wid")
        self.main_QAM_wid.setMinimumSize(QSize(0, 600))
        self.verticalLayout_13 = QVBoxLayout(self.main_QAM_wid)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.params_wid_QAM = QGroupBox(self.main_QAM_wid)
        self.params_wid_QAM.setObjectName(u"params_wid_QAM")
        self.params_wid_QAM.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.params_wid_QAM)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.main_params_QAM_wid = QScrollArea(self.params_wid_QAM)
        self.main_params_QAM_wid.setObjectName(u"main_params_QAM_wid")
        self.main_params_QAM_wid.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.main_params_QAM_wid.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.main_params_QAM_wid.setWidgetResizable(True)
        self.scrollAreaWidgetContents_QAM = QWidget()
        self.scrollAreaWidgetContents_QAM.setObjectName(u"scrollAreaWidgetContents_QAM")
        self.scrollAreaWidgetContents_QAM.setGeometry(QRect(0, 0, 519, 411))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_QAM)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.message_QAM = QWidget(self.scrollAreaWidgetContents_QAM)
        self.message_QAM.setObjectName(u"message_QAM")
        self.verticalLayout_15 = QVBoxLayout(self.message_QAM)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.message_QAM_lable = QLabel(self.message_QAM)
        self.message_QAM_lable.setObjectName(u"message_QAM_lable")

        self.verticalLayout_15.addWidget(self.message_QAM_lable)

        self.QAM_input = QLineEdit(self.message_QAM)
        self.QAM_input.setObjectName(u"QAM_input")
        self.QAM_input.setFrame(True)
        self.QAM_input.setClearButtonEnabled(True)

        self.verticalLayout_15.addWidget(self.QAM_input)


        self.verticalLayout_14.addWidget(self.message_QAM)

        self.type_signal_wid_QAM = QWidget(self.scrollAreaWidgetContents_QAM)
        self.type_signal_wid_QAM.setObjectName(u"type_signal_wid_QAM")
        self.type_signal_wid_QAM.setMinimumSize(QSize(0, 60))
        self.verticalLayout_2 = QVBoxLayout(self.type_signal_wid_QAM)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.signal_type_mess_QAM = QLabel(self.type_signal_wid_QAM)
        self.signal_type_mess_QAM.setObjectName(u"signal_type_mess_QAM")
        self.signal_type_mess_QAM.setMinimumSize(QSize(0, 10))

        self.verticalLayout_2.addWidget(self.signal_type_mess_QAM)

        self.combobox_signal_type_QAM = QComboBox(self.type_signal_wid_QAM)
        self.combobox_signal_type_QAM.addItem("")
        self.combobox_signal_type_QAM.addItem("")
        self.combobox_signal_type_QAM.setObjectName(u"combobox_signal_type_QAM")

        self.verticalLayout_2.addWidget(self.combobox_signal_type_QAM)


        self.verticalLayout_14.addWidget(self.type_signal_wid_QAM)

        self.mod_wid_QAM = QWidget(self.scrollAreaWidgetContents_QAM)
        self.mod_wid_QAM.setObjectName(u"mod_wid_QAM")
        self.mod_wid_QAM.setMinimumSize(QSize(0, 60))
        self.verticalLayout_4 = QVBoxLayout(self.mod_wid_QAM)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mod_label_QAM = QLabel(self.mod_wid_QAM)
        self.mod_label_QAM.setObjectName(u"mod_label_QAM")

        self.verticalLayout_4.addWidget(self.mod_label_QAM)

        self.combobox_coef_QAM = QComboBox(self.mod_wid_QAM)
        self.combobox_coef_QAM.addItem("")
        self.combobox_coef_QAM.addItem("")
        self.combobox_coef_QAM.addItem("")
        self.combobox_coef_QAM.addItem("")
        self.combobox_coef_QAM.setObjectName(u"combobox_coef_QAM")

        self.verticalLayout_4.addWidget(self.combobox_coef_QAM)


        self.verticalLayout_14.addWidget(self.mod_wid_QAM)

        self.noise_wid_QAM = QWidget(self.scrollAreaWidgetContents_QAM)
        self.noise_wid_QAM.setObjectName(u"noise_wid_QAM")
        self.noise_wid_QAM.setMinimumSize(QSize(0, 60))
        self.verticalLayout_5 = QVBoxLayout(self.noise_wid_QAM)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.noise_label_QAM = QLabel(self.noise_wid_QAM)
        self.noise_label_QAM.setObjectName(u"noise_label_QAM")

        self.verticalLayout_5.addWidget(self.noise_label_QAM)

        self.combobox_noise_QAM = QComboBox(self.noise_wid_QAM)
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.addItem("")
        self.combobox_noise_QAM.setObjectName(u"combobox_noise_QAM")

        self.verticalLayout_5.addWidget(self.combobox_noise_QAM)


        self.verticalLayout_14.addWidget(self.noise_wid_QAM)

        self.decision_wid_QAM = QWidget(self.scrollAreaWidgetContents_QAM)
        self.decision_wid_QAM.setObjectName(u"decision_wid_QAM")
        self.decision_wid_QAM.setMinimumSize(QSize(0, 60))
        self.verticalLayout_6 = QVBoxLayout(self.decision_wid_QAM)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.decision_label_QAM = QLabel(self.decision_wid_QAM)
        self.decision_label_QAM.setObjectName(u"decision_label_QAM")

        self.verticalLayout_6.addWidget(self.decision_label_QAM)

        self.combobox_decision_QAM = QComboBox(self.decision_wid_QAM)
        self.combobox_decision_QAM.addItem("")
        self.combobox_decision_QAM.addItem("")
        self.combobox_decision_QAM.setObjectName(u"combobox_decision_QAM")

        self.verticalLayout_6.addWidget(self.combobox_decision_QAM)


        self.verticalLayout_14.addWidget(self.decision_wid_QAM)

        self.grey_wid_QAM = QWidget(self.scrollAreaWidgetContents_QAM)
        self.grey_wid_QAM.setObjectName(u"grey_wid_QAM")
        self.grey_wid_QAM.setMinimumSize(QSize(0, 60))
        self.verticalLayout_7 = QVBoxLayout(self.grey_wid_QAM)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.grey_label_QAM = QLabel(self.grey_wid_QAM)
        self.grey_label_QAM.setObjectName(u"grey_label_QAM")

        self.verticalLayout_7.addWidget(self.grey_label_QAM)

        self.combobox_grey_QAM = QComboBox(self.grey_wid_QAM)
        self.combobox_grey_QAM.addItem("")
        self.combobox_grey_QAM.addItem("")
        self.combobox_grey_QAM.setObjectName(u"combobox_grey_QAM")

        self.verticalLayout_7.addWidget(self.combobox_grey_QAM)


        self.verticalLayout_14.addWidget(self.grey_wid_QAM)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.main_params_QAM_wid.setWidget(self.scrollAreaWidgetContents_QAM)

        self.horizontalLayout_6.addWidget(self.main_params_QAM_wid)


        self.verticalLayout_13.addWidget(self.params_wid_QAM)

        self.other_prefs_QAM = QTabWidget(self.main_QAM_wid)
        self.other_prefs_QAM.setObjectName(u"other_prefs_QAM")
        self.other_prefs_QAM.setMinimumSize(QSize(0, 400))
        self.other_prefs_QAM.setMaximumSize(QSize(600, 600))
        self.other_prefs_wid_QAM = QWidget()
        self.other_prefs_wid_QAM.setObjectName(u"other_prefs_wid_QAM")
        self.verticalLayout_40 = QVBoxLayout(self.other_prefs_wid_QAM)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.checkBox_show_sig_cons_qam = QCheckBox(self.other_prefs_wid_QAM)
        self.checkBox_show_sig_cons_qam.setObjectName(u"checkBox_show_sig_cons_qam")

        self.verticalLayout_40.addWidget(self.checkBox_show_sig_cons_qam)

        self.sid_QAM = QGroupBox(self.other_prefs_wid_QAM)
        self.sid_QAM.setObjectName(u"sid_QAM")
        self.sid_QAM.setMinimumSize(QSize(0, 200))
        self.verticalLayout_41 = QVBoxLayout(self.sid_QAM)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.plainText_sid_QAM = QPlainTextEdit(self.sid_QAM)
        self.plainText_sid_QAM.setObjectName(u"plainText_sid_QAM")

        self.verticalLayout_41.addWidget(self.plainText_sid_QAM)


        self.verticalLayout_40.addWidget(self.sid_QAM)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_3)

        self.other_prefs_QAM.addTab(self.other_prefs_wid_QAM, "")
        self.scheme_QAM = QWidget()
        self.scheme_QAM.setObjectName(u"scheme_QAM")
        self.other_prefs_QAM.addTab(self.scheme_QAM, "")

        self.verticalLayout_13.addWidget(self.other_prefs_QAM)

        self.plot_QAM = QPushButton(self.main_QAM_wid)
        self.plot_QAM.setObjectName(u"plot_QAM")

        self.verticalLayout_13.addWidget(self.plot_QAM)

        self.apply_QAM_but = QCheckBox(self.main_QAM_wid)
        self.apply_QAM_but.setObjectName(u"apply_QAM_but")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.apply_QAM_but.setFont(font1)

        self.verticalLayout_13.addWidget(self.apply_QAM_but)


        self.verticalLayout_9.addWidget(self.main_QAM_wid)

        self.left_tab_wid.addTab(self.QAM_tab, "")

        self.horizontalLayout_2.addWidget(self.left_tab_wid)

        self.graphs = QWidget(self.centralwidget)
        self.graphs.setObjectName(u"graphs")
        self.verticalLayout_3 = QVBoxLayout(self.graphs)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_graphs = QLabel(self.graphs)
        self.label_graphs.setObjectName(u"label_graphs")
        self.label_graphs.setMinimumSize(QSize(0, 0))
        self.label_graphs.setMaximumSize(QSize(16777215, 20))
        self.label_graphs.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_graphs)

        self.plot_area_wid = plot_area_wid(self.graphs)
        self.plot_area_wid.setObjectName(u"plot_area_wid")

        self.verticalLayout_3.addWidget(self.plot_area_wid)


        self.horizontalLayout_2.addWidget(self.graphs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1953, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.left_tab_wid.setCurrentIndex(2)
        self.other_prefs_PSK.setCurrentIndex(0)
        self.other_prefs_QAM.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ComSysSim", None))
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionPlot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.left_tab_wid.setTabText(self.left_tab_wid.indexOf(self.instruct_tab), QCoreApplication.translate("MainWindow", u"Instruction", None))
        self.params_wid_PSK.setTitle(QCoreApplication.translate("MainWindow", u"Params", None))
        self.message_PSK_lable.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.PSK_input.setText(QCoreApplication.translate("MainWindow", u"10101010", None))
        self.signal_type_mess_PSK.setText(QCoreApplication.translate("MainWindow", u"Signal type", None))
        self.combobox_signal_type_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"Integers", None))
        self.combobox_signal_type_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"Binary", None))

        self.mod_label_PSK.setText(QCoreApplication.translate("MainWindow", u"Modulation coefficient", None))
        self.combobox_coef_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.combobox_coef_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_coef_PSK.setItemText(2, QCoreApplication.translate("MainWindow", u"8", None))
        self.combobox_coef_PSK.setItemText(3, QCoreApplication.translate("MainWindow", u"16", None))
        self.combobox_coef_PSK.setItemText(4, QCoreApplication.translate("MainWindow", u"32", None))

        self.noise_label_PSK.setText(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.combobox_noise_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.combobox_noise_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.combobox_noise_PSK.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))
        self.combobox_noise_PSK.setItemText(3, QCoreApplication.translate("MainWindow", u"30", None))
        self.combobox_noise_PSK.setItemText(4, QCoreApplication.translate("MainWindow", u"40", None))
        self.combobox_noise_PSK.setItemText(5, QCoreApplication.translate("MainWindow", u"50", None))
        self.combobox_noise_PSK.setItemText(6, QCoreApplication.translate("MainWindow", u"60", None))
        self.combobox_noise_PSK.setItemText(7, QCoreApplication.translate("MainWindow", u"70", None))
        self.combobox_noise_PSK.setItemText(8, QCoreApplication.translate("MainWindow", u"80", None))
        self.combobox_noise_PSK.setItemText(9, QCoreApplication.translate("MainWindow", u"90", None))
        self.combobox_noise_PSK.setItemText(10, QCoreApplication.translate("MainWindow", u"100", None))
        self.combobox_noise_PSK.setItemText(11, QCoreApplication.translate("MainWindow", u"200", None))
        self.combobox_noise_PSK.setItemText(12, QCoreApplication.translate("MainWindow", u"500", None))

        self.decision_label_PSK.setText(QCoreApplication.translate("MainWindow", u"Decision", None))
        self.combobox_decision_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"Not soft", None))
        self.combobox_decision_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"Soft", None))

        self.grey_label_PSK.setText(QCoreApplication.translate("MainWindow", u"Grey code", None))
        self.combobox_grey_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.combobox_grey_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.phase_label_PSK.setText(QCoreApplication.translate("MainWindow", u"Phase: PI/", None))
        self.combobox_phase_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_phase_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"8", None))
        self.combobox_phase_PSK.setItemText(2, QCoreApplication.translate("MainWindow", u"16", None))
        self.combobox_phase_PSK.setItemText(3, QCoreApplication.translate("MainWindow", u"32", None))

        self.checkBox_show_sig_cons_psk.setText(QCoreApplication.translate("MainWindow", u"Show signal constellation", None))
        self.sid_PSK.setTitle(QCoreApplication.translate("MainWindow", u"Sid", None))
        self.label_length_PSK.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.comboBox_length_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_length_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_length_PSK.setItemText(2, QCoreApplication.translate("MainWindow", u"32", None))
        self.comboBox_length_PSK.setItemText(3, QCoreApplication.translate("MainWindow", u"64", None))
        self.comboBox_length_PSK.setItemText(4, QCoreApplication.translate("MainWindow", u"128", None))

        self.pushButton_generate_sid_PSK.setText(QCoreApplication.translate("MainWindow", u"Generate sid", None))
        self.plainText_sid_PSK.setPlainText(QCoreApplication.translate("MainWindow", u"11011101111111000110101010101010101101101010101010110111110101011110111011111110001101010101010101011011010101010101101111101010111101110111111100011010101010101010110110101010101011011111010101111011101111111000110101010101010101101101010101010110111110101011101011011111010101111011101111111000110101010101010101101101010101010110111110101011110111011111110001101010101010110110101010101011011111010101111011101111111000110101010101010101101101010101010110111110101011101011011111010101111011101111111000110101010101010101101101010101010110111110101011101011110111011111110001101010101010110110101010101011011111010101111011101111111000110101010101010101101101010101010110111110101011101011011111010101111011101111111000110101010101010101101101010101010110110111010111101110111111100011010101010101101101010101010110111110101011110111011111110001101010101010101011011010101010101101111101010111010110111110101011110111011111110001101010101010101011011010101010101101011011010101010101101111101010111010111101110111111100011"
                        "01010101010110110101010101011011111010101111011101111111000110101010101010101101101010101010110111110101011101011011111010101111011101111111000110101010101010101101101010101010110110111010111101110111111100011010101010101101101010101", None))
        self.other_prefs_PSK.setTabText(self.other_prefs_PSK.indexOf(self.other_prefs_wid_PSK), QCoreApplication.translate("MainWindow", u"Other prefs", None))
        self.other_prefs_PSK.setTabText(self.other_prefs_PSK.indexOf(self.scheme_PSK), QCoreApplication.translate("MainWindow", u"Scheme", None))
        self.plot_PSK.setText(QCoreApplication.translate("MainWindow", u"Plot graphs with PSK modulation!", None))
        self.apply_PSK_but.setText(QCoreApplication.translate("MainWindow", u"Apply prefs PSK", None))
        self.left_tab_wid.setTabText(self.left_tab_wid.indexOf(self.PSK_tab), QCoreApplication.translate("MainWindow", u"PSK", None))
        self.params_wid_QAM.setTitle(QCoreApplication.translate("MainWindow", u"Params", None))
        self.message_QAM_lable.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.QAM_input.setText(QCoreApplication.translate("MainWindow", u"10101010", None))
        self.signal_type_mess_QAM.setText(QCoreApplication.translate("MainWindow", u"Signal type", None))
        self.combobox_signal_type_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"Integers", None))
        self.combobox_signal_type_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"Binary", None))

        self.mod_label_QAM.setText(QCoreApplication.translate("MainWindow", u"Modulation coefficient", None))
        self.combobox_coef_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_coef_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"16", None))
        self.combobox_coef_QAM.setItemText(2, QCoreApplication.translate("MainWindow", u"64", None))
        self.combobox_coef_QAM.setItemText(3, QCoreApplication.translate("MainWindow", u"256", None))

        self.noise_label_QAM.setText(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.combobox_noise_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.combobox_noise_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.combobox_noise_QAM.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))
        self.combobox_noise_QAM.setItemText(3, QCoreApplication.translate("MainWindow", u"30", None))
        self.combobox_noise_QAM.setItemText(4, QCoreApplication.translate("MainWindow", u"40", None))
        self.combobox_noise_QAM.setItemText(5, QCoreApplication.translate("MainWindow", u"50", None))
        self.combobox_noise_QAM.setItemText(6, QCoreApplication.translate("MainWindow", u"60", None))
        self.combobox_noise_QAM.setItemText(7, QCoreApplication.translate("MainWindow", u"70", None))
        self.combobox_noise_QAM.setItemText(8, QCoreApplication.translate("MainWindow", u"80", None))
        self.combobox_noise_QAM.setItemText(9, QCoreApplication.translate("MainWindow", u"90", None))
        self.combobox_noise_QAM.setItemText(10, QCoreApplication.translate("MainWindow", u"100", None))
        self.combobox_noise_QAM.setItemText(11, QCoreApplication.translate("MainWindow", u"200", None))
        self.combobox_noise_QAM.setItemText(12, QCoreApplication.translate("MainWindow", u"500", None))

        self.decision_label_QAM.setText(QCoreApplication.translate("MainWindow", u"Decision", None))
        self.combobox_decision_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"Not soft", None))
        self.combobox_decision_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"Soft", None))

        self.grey_label_QAM.setText(QCoreApplication.translate("MainWindow", u"Grey code", None))
        self.combobox_grey_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.combobox_grey_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.checkBox_show_sig_cons_qam.setText(QCoreApplication.translate("MainWindow", u"Show signal constellation", None))
        self.sid_QAM.setTitle(QCoreApplication.translate("MainWindow", u"Sid", None))
        self.plainText_sid_QAM.setPlainText(QCoreApplication.translate("MainWindow", u"1111010101010101010101010101010101010101010101010101101010101010101010101010111110101010101010101010111101101010101010101010101010101010101010010101010101010101010", None))
        self.other_prefs_QAM.setTabText(self.other_prefs_QAM.indexOf(self.other_prefs_wid_QAM), QCoreApplication.translate("MainWindow", u"Other prefs", None))
        self.other_prefs_QAM.setTabText(self.other_prefs_QAM.indexOf(self.scheme_QAM), QCoreApplication.translate("MainWindow", u"Scheme", None))
        self.plot_QAM.setText(QCoreApplication.translate("MainWindow", u"Plot graphs with QAM modulation!", None))
        self.apply_QAM_but.setText(QCoreApplication.translate("MainWindow", u"Apply prefs QAM", None))
        self.left_tab_wid.setTabText(self.left_tab_wid.indexOf(self.QAM_tab), QCoreApplication.translate("MainWindow", u"QAM", None))
        self.label_graphs.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
    # retranslateUi

