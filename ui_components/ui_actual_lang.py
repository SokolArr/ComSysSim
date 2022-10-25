# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actual_lang.ui'
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
    QMainWindow, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from ui_components.plot_area_wid import plot_area_wid
from ui_components.plot_area_wid_21 import plot_area_wid_21
from ui_components.plot_area_wid_22 import plot_area_wid_22
from ui_components.plot_area_wid_23 import plot_area_wid_23
from ui_components.plot_area_wid_24 import plot_area_wid_24

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1470, 1224)
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
        self.left_tab_wid.setMaximumSize(QSize(500, 16777215))
        self.instruct_tab = QWidget()
        self.instruct_tab.setObjectName(u"instruct_tab")
        self.verticalLayout_8 = QVBoxLayout(self.instruct_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.instruct_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

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
        self.scrollAreaWidgetContents_PSK.setGeometry(QRect(0, 0, 419, 506))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_PSK)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.message_PSK = QWidget(self.scrollAreaWidgetContents_PSK)
        self.message_PSK.setObjectName(u"message_PSK")
        self.verticalLayout_36 = QVBoxLayout(self.message_PSK)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.message_PSK_wid = QWidget(self.message_PSK)
        self.message_PSK_wid.setObjectName(u"message_PSK_wid")
        self.horizontalLayout_10 = QHBoxLayout(self.message_PSK_wid)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.message_PSK_lable = QLabel(self.message_PSK_wid)
        self.message_PSK_lable.setObjectName(u"message_PSK_lable")
        font = QFont()
        font.setPointSize(12)
        self.message_PSK_lable.setFont(font)

        self.horizontalLayout_10.addWidget(self.message_PSK_lable)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.message_PSK_wid)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.length_PSK_mes = QLabel(self.message_PSK_wid)
        self.length_PSK_mes.setObjectName(u"length_PSK_mes")

        self.horizontalLayout_10.addWidget(self.length_PSK_mes)


        self.verticalLayout_36.addWidget(self.message_PSK_wid)

        self.PSK_input = QLineEdit(self.message_PSK)
        self.PSK_input.setObjectName(u"PSK_input")
        self.PSK_input.setFont(font)
        self.PSK_input.setFrame(True)
        self.PSK_input.setClearButtonEnabled(True)

        self.verticalLayout_36.addWidget(self.PSK_input)

        self.label_4 = QLabel(self.message_PSK)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setItalic(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_4)


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
        self.combobox_phase_PSK.setGeometry(QRect(70, 10, 321, 22))

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
        self.checkBox_show_sig_cons_psk.setFont(font)

        self.verticalLayout_39.addWidget(self.checkBox_show_sig_cons_psk)

        self.sid_PSK = QGroupBox(self.other_prefs_wid_PSK)
        self.sid_PSK.setObjectName(u"sid_PSK")
        self.sid_PSK.setMinimumSize(QSize(0, 200))
        self.verticalLayout_42 = QVBoxLayout(self.sid_PSK)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_length_PSK = QLabel(self.sid_PSK)
        self.label_length_PSK.setObjectName(u"label_length_PSK")

        self.verticalLayout_42.addWidget(self.label_length_PSK)

        self.spinBox_PSK = QSpinBox(self.sid_PSK)
        self.spinBox_PSK.setObjectName(u"spinBox_PSK")
        self.spinBox_PSK.setMaximum(100000)
        self.spinBox_PSK.setValue(100)

        self.verticalLayout_42.addWidget(self.spinBox_PSK)

        self.all_numbers_PSK = QCheckBox(self.sid_PSK)
        self.all_numbers_PSK.setObjectName(u"all_numbers_PSK")
        font2 = QFont()
        font2.setPointSize(10)
        self.all_numbers_PSK.setFont(font2)

        self.verticalLayout_42.addWidget(self.all_numbers_PSK)

        self.pushButton_generate_sid_PSK = QPushButton(self.sid_PSK)
        self.pushButton_generate_sid_PSK.setObjectName(u"pushButton_generate_sid_PSK")

        self.verticalLayout_42.addWidget(self.pushButton_generate_sid_PSK)

        self.plainText_sid_PSK = QPlainTextEdit(self.sid_PSK)
        self.plainText_sid_PSK.setObjectName(u"plainText_sid_PSK")

        self.verticalLayout_42.addWidget(self.plainText_sid_PSK)


        self.verticalLayout_39.addWidget(self.sid_PSK)

        self.other_prefs_PSK.addTab(self.other_prefs_wid_PSK, "")
        self.scheme_PSK = QWidget()
        self.scheme_PSK.setObjectName(u"scheme_PSK")
        self.horizontalLayout_5 = QHBoxLayout(self.scheme_PSK)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pic_PSK = QLabel(self.scheme_PSK)
        self.pic_PSK.setObjectName(u"pic_PSK")
        self.pic_PSK.setMinimumSize(QSize(400, 400))
        self.pic_PSK.setMaximumSize(QSize(400, 400))
        self.pic_PSK.setPixmap(QPixmap(u"../pictures/psk_mod_schem.png"))
        self.pic_PSK.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.pic_PSK)

        self.other_prefs_PSK.addTab(self.scheme_PSK, "")

        self.verticalLayout_34.addWidget(self.other_prefs_PSK)

        self.plot_PSK = QPushButton(self.main_PSK_wid)
        self.plot_PSK.setObjectName(u"plot_PSK")
        self.plot_PSK.setMinimumSize(QSize(0, 40))
        self.plot_PSK.setFont(font)

        self.verticalLayout_34.addWidget(self.plot_PSK)

        self.widget_2 = QWidget(self.main_PSK_wid)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.apply_PSK_but = QCheckBox(self.widget_2)
        self.apply_PSK_but.setObjectName(u"apply_PSK_but")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setUnderline(False)
        self.apply_PSK_but.setFont(font3)

        self.horizontalLayout_3.addWidget(self.apply_PSK_but)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_34.addWidget(self.widget_2)

        self.progressBar_PSK = QProgressBar(self.main_PSK_wid)
        self.progressBar_PSK.setObjectName(u"progressBar_PSK")
        self.progressBar_PSK.setValue(0)

        self.verticalLayout_34.addWidget(self.progressBar_PSK)


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
        self.scrollAreaWidgetContents_QAM.setGeometry(QRect(0, 0, 419, 460))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_QAM)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.message_QAM = QWidget(self.scrollAreaWidgetContents_QAM)
        self.message_QAM.setObjectName(u"message_QAM")
        self.verticalLayout_15 = QVBoxLayout(self.message_QAM)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_5 = QWidget(self.message_QAM)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.message_QAM_lable = QLabel(self.widget_5)
        self.message_QAM_lable.setObjectName(u"message_QAM_lable")
        font4 = QFont()
        font4.setPointSize(11)
        self.message_QAM_lable.setFont(font4)

        self.horizontalLayout_11.addWidget(self.message_QAM_lable)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_3)

        self.length_QAM_mes = QLabel(self.widget_5)
        self.length_QAM_mes.setObjectName(u"length_QAM_mes")

        self.horizontalLayout_11.addWidget(self.length_QAM_mes)


        self.verticalLayout_15.addWidget(self.widget_5)

        self.QAM_input = QLineEdit(self.message_QAM)
        self.QAM_input.setObjectName(u"QAM_input")
        self.QAM_input.setFont(font)
        self.QAM_input.setFrame(True)
        self.QAM_input.setClearButtonEnabled(True)

        self.verticalLayout_15.addWidget(self.QAM_input)

        self.label_5 = QLabel(self.message_QAM)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 15))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_5)


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
        self.checkBox_show_sig_cons_qam.setFont(font)

        self.verticalLayout_40.addWidget(self.checkBox_show_sig_cons_qam)

        self.sid_QAM = QGroupBox(self.other_prefs_wid_QAM)
        self.sid_QAM.setObjectName(u"sid_QAM")
        self.sid_QAM.setMinimumSize(QSize(0, 200))
        self.verticalLayout_51 = QVBoxLayout(self.sid_QAM)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_length_QAM = QLabel(self.sid_QAM)
        self.label_length_QAM.setObjectName(u"label_length_QAM")

        self.verticalLayout_51.addWidget(self.label_length_QAM)

        self.spinBox_QAM = QSpinBox(self.sid_QAM)
        self.spinBox_QAM.setObjectName(u"spinBox_QAM")
        self.spinBox_QAM.setMaximum(100000)
        self.spinBox_QAM.setValue(100)

        self.verticalLayout_51.addWidget(self.spinBox_QAM)

        self.all_numbers_QAM = QCheckBox(self.sid_QAM)
        self.all_numbers_QAM.setObjectName(u"all_numbers_QAM")
        self.all_numbers_QAM.setFont(font2)

        self.verticalLayout_51.addWidget(self.all_numbers_QAM)

        self.pushButton_generate_sid_QAM = QPushButton(self.sid_QAM)
        self.pushButton_generate_sid_QAM.setObjectName(u"pushButton_generate_sid_QAM")

        self.verticalLayout_51.addWidget(self.pushButton_generate_sid_QAM)

        self.plainText_sid_QAM = QPlainTextEdit(self.sid_QAM)
        self.plainText_sid_QAM.setObjectName(u"plainText_sid_QAM")

        self.verticalLayout_51.addWidget(self.plainText_sid_QAM)


        self.verticalLayout_40.addWidget(self.sid_QAM)

        self.other_prefs_QAM.addTab(self.other_prefs_wid_QAM, "")
        self.scheme_QAM = QWidget()
        self.scheme_QAM.setObjectName(u"scheme_QAM")
        self.horizontalLayout_9 = QHBoxLayout(self.scheme_QAM)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pic_QAM = QLabel(self.scheme_QAM)
        self.pic_QAM.setObjectName(u"pic_QAM")
        self.pic_QAM.setMinimumSize(QSize(400, 400))
        self.pic_QAM.setMaximumSize(QSize(400, 400))
        self.pic_QAM.setPixmap(QPixmap(u"../pictures/qam_mod_schem.png"))
        self.pic_QAM.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.pic_QAM)

        self.other_prefs_QAM.addTab(self.scheme_QAM, "")

        self.verticalLayout_13.addWidget(self.other_prefs_QAM)

        self.plot_QAM = QPushButton(self.main_QAM_wid)
        self.plot_QAM.setObjectName(u"plot_QAM")
        self.plot_QAM.setMinimumSize(QSize(0, 40))
        self.plot_QAM.setFont(font)

        self.verticalLayout_13.addWidget(self.plot_QAM)

        self.widget = QWidget(self.main_QAM_wid)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.apply_QAM_but = QCheckBox(self.widget)
        self.apply_QAM_but.setObjectName(u"apply_QAM_but")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.apply_QAM_but.setFont(font5)

        self.horizontalLayout.addWidget(self.apply_QAM_but)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_13.addWidget(self.widget)

        self.progressBar_QAM = QProgressBar(self.main_QAM_wid)
        self.progressBar_QAM.setObjectName(u"progressBar_QAM")
        self.progressBar_QAM.setValue(0)

        self.verticalLayout_13.addWidget(self.progressBar_QAM)


        self.verticalLayout_9.addWidget(self.main_QAM_wid)

        self.left_tab_wid.addTab(self.QAM_tab, "")

        self.horizontalLayout_2.addWidget(self.left_tab_wid)

        self.graphs = QWidget(self.centralwidget)
        self.graphs.setObjectName(u"graphs")
        self.verticalLayout_3 = QVBoxLayout(self.graphs)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.graphs_tab_wid = QTabWidget(self.graphs)
        self.graphs_tab_wid.setObjectName(u"graphs_tab_wid")
        self.signal_tab = QWidget()
        self.signal_tab.setObjectName(u"signal_tab")
        self.horizontalLayout_7 = QHBoxLayout(self.signal_tab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_3 = QWidget(self.signal_tab)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_16 = QVBoxLayout(self.widget_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.plot_area_wid_21 = plot_area_wid_21(self.widget_3)
        self.plot_area_wid_21.setObjectName(u"plot_area_wid_21")

        self.verticalLayout_16.addWidget(self.plot_area_wid_21)

        self.plot_area_wid_23 = plot_area_wid_23(self.widget_3)
        self.plot_area_wid_23.setObjectName(u"plot_area_wid_23")

        self.verticalLayout_16.addWidget(self.plot_area_wid_23)


        self.horizontalLayout_7.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.signal_tab)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_17 = QVBoxLayout(self.widget_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.plot_area_wid_22 = plot_area_wid_22(self.widget_4)
        self.plot_area_wid_22.setObjectName(u"plot_area_wid_22")

        self.verticalLayout_17.addWidget(self.plot_area_wid_22)

        self.plot_area_wid_24 = plot_area_wid_24(self.widget_4)
        self.plot_area_wid_24.setObjectName(u"plot_area_wid_24")

        self.verticalLayout_17.addWidget(self.plot_area_wid_24)


        self.horizontalLayout_7.addWidget(self.widget_4)

        self.graphs_tab_wid.addTab(self.signal_tab, "")
        self.Sub = QWidget()
        self.Sub.setObjectName(u"Sub")
        self.verticalLayout_20 = QVBoxLayout(self.Sub)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.plot_area_wid = plot_area_wid(self.Sub)
        self.plot_area_wid.setObjectName(u"plot_area_wid")

        self.verticalLayout_20.addWidget(self.plot_area_wid)

        self.graphs_tab_wid.addTab(self.Sub, "")
        self.report_tab = QWidget()
        self.report_tab.setObjectName(u"report_tab")
        self.verticalLayout_18 = QVBoxLayout(self.report_tab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.type_mod = QLabel(self.report_tab)
        self.type_mod.setObjectName(u"type_mod")
        self.type_mod.setFont(font)

        self.verticalLayout_18.addWidget(self.type_mod)

        self.scrollArea_message = QScrollArea(self.report_tab)
        self.scrollArea_message.setObjectName(u"scrollArea_message")
        self.scrollArea_message.setMinimumSize(QSize(0, 0))
        self.scrollArea_message.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_message.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 902, 198))
        self.verticalLayout_52 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_54 = QVBoxLayout(self.groupBox)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.message_template = QLabel(self.groupBox)
        self.message_template.setObjectName(u"message_template")
        self.message_template.setMinimumSize(QSize(0, 100))
        self.message_template.setMaximumSize(QSize(16777215, 200))
        self.message_template.setFont(font)
        self.message_template.setTextFormat(Qt.RichText)
        self.message_template.setWordWrap(True)

        self.verticalLayout_54.addWidget(self.message_template)


        self.verticalLayout_52.addWidget(self.groupBox)

        self.scrollArea_message.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_18.addWidget(self.scrollArea_message)

        self.scrollArea_dmessage = QScrollArea(self.report_tab)
        self.scrollArea_dmessage.setObjectName(u"scrollArea_dmessage")
        self.scrollArea_dmessage.setMinimumSize(QSize(0, 0))
        self.scrollArea_dmessage.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_dmessage.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 902, 198))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 100))
        self.groupBox_2.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_53 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.dmessage_template = QLabel(self.groupBox_2)
        self.dmessage_template.setObjectName(u"dmessage_template")
        self.dmessage_template.setFont(font)
        self.dmessage_template.setTextFormat(Qt.RichText)
        self.dmessage_template.setWordWrap(True)

        self.verticalLayout_53.addWidget(self.dmessage_template)


        self.verticalLayout_19.addWidget(self.groupBox_2)

        self.scrollArea_dmessage.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_18.addWidget(self.scrollArea_dmessage)

        self.label_bit_error = QLabel(self.report_tab)
        self.label_bit_error.setObjectName(u"label_bit_error")
        self.label_bit_error.setFont(font)
        self.label_bit_error.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout_18.addWidget(self.label_bit_error)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.graphs_tab_wid.addTab(self.report_tab, "")

        self.verticalLayout_3.addWidget(self.graphs_tab_wid)


        self.horizontalLayout_2.addWidget(self.graphs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1470, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.left_tab_wid.setCurrentIndex(2)
        self.other_prefs_PSK.setCurrentIndex(0)
        self.other_prefs_QAM.setCurrentIndex(0)
        self.graphs_tab_wid.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ComSysSim", None))
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionPlot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version 0.1 - 2022", None))
        self.left_tab_wid.setTabText(self.left_tab_wid.indexOf(self.instruct_tab), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.params_wid_PSK.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.message_PSK_lable.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432:", None))
        self.length_PSK_mes.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.PSK_input.setText(QCoreApplication.translate("MainWindow", u"1 0 1 0 1 0 1 0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#a81818;\">\u0434\u043b\u0438\u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u043a\u0440\u0430\u0442\u043d\u0430 log2(M)</span></p></body></html>", None))
        self.signal_type_mess_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.combobox_signal_type_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"Only integers", None))
        self.combobox_signal_type_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"Binary code", None))
        self.combobox_signal_type_PSK.setItemText(2, QCoreApplication.translate("MainWindow", u"Message with letters", None))

        self.mod_label_PSK.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u0438 (M)", None))
        self.combobox_coef_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.combobox_coef_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_coef_PSK.setItemText(2, QCoreApplication.translate("MainWindow", u"8", None))
        self.combobox_coef_PSK.setItemText(3, QCoreApplication.translate("MainWindow", u"16", None))
        self.combobox_coef_PSK.setItemText(4, QCoreApplication.translate("MainWindow", u"32", None))

        self.noise_label_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0443\u043c", None))
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

        self.decision_label_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.combobox_decision_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"Not soft", None))
        self.combobox_decision_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"Soft", None))

        self.grey_label_PSK.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0413\u0440\u0435\u044f", None))
        self.combobox_grey_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.combobox_grey_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.phase_label_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0437\u0430: PI/", None))
        self.combobox_phase_PSK.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_phase_PSK.setItemText(1, QCoreApplication.translate("MainWindow", u"8", None))
        self.combobox_phase_PSK.setItemText(2, QCoreApplication.translate("MainWindow", u"16", None))
        self.combobox_phase_PSK.setItemText(3, QCoreApplication.translate("MainWindow", u"32", None))

        self.checkBox_show_sig_cons_psk.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u0438\u0433\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0437\u0432\u0435\u0437\u0434\u0438\u0435", None))
        self.sid_PSK.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0434", None))
        self.label_length_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.all_numbers_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0431\u0438\u043d\u0430\u0440\u043d\u043e\u0433\u043e \u0432\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.pushButton_generate_sid_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0441\u0438\u0434\u0430", None))
        self.plainText_sid_PSK.setPlainText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438 \u0441\u0438\u0434\u0430", None))
        self.other_prefs_PSK.setTabText(self.other_prefs_PSK.indexOf(self.other_prefs_wid_PSK), QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.pic_PSK.setText("")
        self.other_prefs_PSK.setTabText(self.other_prefs_PSK.indexOf(self.scheme_PSK), QCoreApplication.translate("MainWindow", u"\u0421\u0445\u0435\u043c\u0430", None))
        self.plot_PSK.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438 \u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432 PSK \u043c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u0438!", None))
        self.apply_PSK_but.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 PSK", None))
        self.left_tab_wid.setTabText(self.left_tab_wid.indexOf(self.PSK_tab), QCoreApplication.translate("MainWindow", u"PSK \u041c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.params_wid_QAM.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.message_QAM_lable.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432:", None))
        self.length_QAM_mes.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.QAM_input.setText(QCoreApplication.translate("MainWindow", u"1 0 1 0 1 0 1 0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#a81818;\">\u0434\u043b\u0438\u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u0440\u0430\u0432\u043d\u0430 2 \u0432 \u0441\u0442\u0435\u043f\u0435\u043d\u0438 (M-1)</span></p></body></html>", None))
        self.signal_type_mess_QAM.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.combobox_signal_type_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"Only integers", None))
        self.combobox_signal_type_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"Binary code", None))
        self.combobox_signal_type_QAM.setItemText(2, QCoreApplication.translate("MainWindow", u"Message with letters", None))

        self.mod_label_QAM.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u0438 (M)", None))
        self.combobox_coef_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_coef_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"16", None))
        self.combobox_coef_QAM.setItemText(2, QCoreApplication.translate("MainWindow", u"64", None))
        self.combobox_coef_QAM.setItemText(3, QCoreApplication.translate("MainWindow", u"256", None))

        self.noise_label_QAM.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0443\u043c", None))
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

        self.decision_label_QAM.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.combobox_decision_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"Not soft", None))
        self.combobox_decision_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"Soft", None))

        self.grey_label_QAM.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0413\u0440\u0435\u044f", None))
        self.combobox_grey_QAM.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.combobox_grey_QAM.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.checkBox_show_sig_cons_qam.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u0438\u0433\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0437\u0432\u0435\u0437\u0434\u0438\u0435", None))
        self.sid_QAM.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0434", None))
        self.label_length_QAM.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430", None))
        self.all_numbers_QAM.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0431\u0438\u043d\u0430\u0440\u043d\u043e\u0433\u043e \u0432\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.pushButton_generate_sid_QAM.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0441\u0438\u0434\u0430", None))
        self.plainText_sid_QAM.setPlainText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438 \u0441\u0438\u0434\u0430", None))
        self.other_prefs_QAM.setTabText(self.other_prefs_QAM.indexOf(self.other_prefs_wid_QAM), QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.pic_QAM.setText("")
        self.other_prefs_QAM.setTabText(self.other_prefs_QAM.indexOf(self.scheme_QAM), QCoreApplication.translate("MainWindow", u"\u0421\u0445\u0435\u043c\u0430", None))
        self.plot_QAM.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0441\u0438\u043c\u0443\u043b\u044f\u0446\u0438\u0438 \u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432 QAM \u043c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u0438!", None))
        self.apply_QAM_but.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 QAM", None))
        self.left_tab_wid.setTabText(self.left_tab_wid.indexOf(self.QAM_tab), QCoreApplication.translate("MainWindow", u"QAM \u041c\u043e\u0434\u0443\u043b\u044f\u0446\u0438\u044f", None))
        self.graphs_tab_wid.setTabText(self.graphs_tab_wid.indexOf(self.signal_tab), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0433\u043d\u0430\u043b\u044b", None))
        self.graphs_tab_wid.setTabText(self.graphs_tab_wid.indexOf(self.Sub), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0442\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u0433\u043d\u0430\u043b", None))
        self.type_mod.setText(QCoreApplication.translate("MainWindow", u"Type modulation: start simulation first!", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u043d\u0438\u0435", None))
        self.message_template.setText(QCoreApplication.translate("MainWindow", u"Message: start simulation first!", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043c\u043e\u0434\u0443\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.dmessage_template.setText(QCoreApplication.translate("MainWindow", u"Demodulated message: start simulation first!", None))
        self.label_bit_error.setText(QCoreApplication.translate("MainWindow", u"Bits erorrs: start simulation first!", None))
        self.graphs_tab_wid.setTabText(self.graphs_tab_wid.indexOf(self.report_tab), QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442", None))
    # retranslateUi

