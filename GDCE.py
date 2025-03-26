import sys ,os ,json ,time ,urllib .request #line:1
from PyQt5 .QtWidgets import (QApplication ,QMainWindow ,QWidget ,QVBoxLayout ,QHBoxLayout ,QLineEdit ,QPushButton ,QTabWidget ,QDialog ,QListWidget ,QCheckBox ,QLabel ,QMessageBox ,QInputDialog )#line:2
from PyQt5 .QtWebEngineWidgets import QWebEngineView #line:3
from PyQt5 .QtWebEngineCore import QWebEngineUrlRequestInterceptor #line:4
from PyQt5 .QtCore import QUrl #line:5
from PyQt5 .QtGui import QIcon #line:6
class AdBlockInterceptor (QWebEngineUrlRequestInterceptor ):#line:7
    def __init__ (O0O0OOOO00000O000 ,enabled =True ,parent =None ):#line:8
        super ().__init__ (parent )#line:9
        O0O0OOOO00000O000 .enabled =enabled #line:10
        O0O0OOOO00000O000 .block_list =["ads.","tracking.","18plus."]#line:11
    def interceptRequest (O0O0OO0OOO0000O00 ,OO00OO00O0O00O000 ):#line:12
        if O0O0OO0OOO0000O00 .enabled :#line:13
            OO0OO00OO0O0OOO0O =OO00OO00O0O00O000 .requestUrl ().toString ()#line:14
            for O0O00O000OOO0OOO0 in O0O0OO0OOO0000O00 .block_list :#line:15
                if O0O00O000OOO0OOO0 in OO0OO00OO0O0OOO0O :#line:16
                    OO00OO00O0O00O000 .block (True )#line:17
                    break #line:18
class HistoryDialog (QDialog ):#line:19
    def __init__ (O0O00O0O0OO0O0O0O ,O0O0O00O00OOOO0O0 ,parent =None ):#line:20
        super ().__init__ (parent )#line:21
        O0O00O0O0OO0O0O0O .setWindowTitle ("History")#line:22
        O0O00O0O0OO0O0O0O .history_file =O0O0O00O00OOOO0O0 #line:23
        O0O00O0O0OO0O0O0O .resize (500 ,400 )#line:24
        O0OO000OOOOO000OO =QVBoxLayout ()#line:25
        O0O00O0O0OO0O0O0O .history_list =QListWidget ()#line:26
        O0O00O0O0OO0O0O0O .load_history ()#line:27
        O0O00O0O0OO0O0O0O .clear_history_button =QPushButton ("Clear History")#line:28
        O0O00O0O0OO0O0O0O .clear_history_button .clicked .connect (O0O00O0O0OO0O0O0O .clear_history )#line:29
        O0OO000OOOOO000OO .addWidget (O0O00O0O0OO0O0O0O .history_list )#line:30
        O0OO000OOOOO000OO .addWidget (O0O00O0O0OO0O0O0O .clear_history_button )#line:31
        O0O00O0O0OO0O0O0O .setLayout (O0OO000OOOOO000OO )#line:32
    def load_history (OO00O0OOO00OOOOOO ):#line:33
        OO00O0OOO00OOOOOO .history_list .clear ()#line:34
        try :#line:35
            with open (OO00O0OOO00OOOOOO .history_file ,"r")as O0O00000OOOO00OO0 :#line:36
                OO00OO0OO0O00O000 =json .load (O0O00000OOOO00OO0 )#line:37
        except :#line:38
            OO00OO0OO0O00O000 =[]#line:39
        for O00O000OO0OO0OOOO in OO00OO0OO0O00O000 :#line:40
            if isinstance (O00O000OO0OO0OOOO ,dict ):#line:41
                OOOO00OO00OOOO0O0 =O00O000OO0OO0OOOO .get ("url","")#line:42
            else :#line:43
                OOOO00OO00OOOO0O0 =O00O000OO0OO0OOOO #line:44
            OO00O0OOO00OOOOOO .history_list .addItem (OOOO00OO00OOOO0O0 )#line:45
    def clear_history (OO00000O0000O000O ):#line:46
        O000O0O0000OO00OO =["1 hr","1 d","3 d","7 d","20 d","1 month","1 year","All time"]#line:47
        O0O000O0O00000O00 ,O00OOO00O0O0OOOO0 =QInputDialog .getItem (OO00000O0000O000O ,"Clear History","Delete history older than:",O000O0O0000OO00OO ,0 ,False )#line:48
        if O00OOO00O0O0OOOO0 :#line:49
            OOOOO0OO000000O0O =time .time ()#line:50
            OOO0O0OOO0OOO0O0O ={"1 hr":3600 ,"1 d":86400 ,"3 d":3 *86400 ,"7 d":7 *86400 ,"20 d":20 *86400 ,"1 month":30 *86400 ,"1 year":365 *86400 ,"All time":None }#line:51
            O0OOOOO0O0O00OOOO =OOO0O0OOO0OOO0O0O .get (O0O000O0O00000O00 )#line:52
            try :#line:53
                with open (OO00000O0000O000O .history_file ,"r")as O000OOOO000OOO0O0 :#line:54
                    OOO00O0O000000O0O =json .load (O000OOOO000OOO0O0 )#line:55
            except :#line:56
                OOO00O0O000000O0O =[]#line:57
            if O0OOOOO0O0O00OOOO is None :#line:58
                OOO00O0O000000O0O =[]#line:59
            else :#line:60
                OOO00O0O000000O0O =[O0O0OOO000OO00O00 for O0O0OOO000OO00O00 in OOO00O0O000000O0O if (OOOOO0OO000000O0O -(O0O0OOO000OO00O00 .get ("timestamp",OOOOO0OO000000O0O )if isinstance (O0O0OOO000OO00O00 ,dict )else OOOOO0OO000000O0O ))<O0OOOOO0O0O00OOOO ]#line:61
            with open (OO00000O0000O000O .history_file ,"w")as O000OOOO000OOO0O0 :#line:62
                json .dump (OOO00O0O000000O0O ,O000OOOO000OOO0O0 )#line:63
            OO00000O0000O000O .load_history ()#line:64
class SettingsDialog (QDialog ):#line:65
    def __init__ (OOO000OOO0OOO0O0O ,O00OO0000O000OOOO ,OO00OO00O0OO0OOOO ,O0OO00O0O000O00O0 ,O00O0OOO00O00O000 ,OO0OOOOOO0O0OO0OO ):#line:66
        super ().__init__ (O00OO0000O000OOOO )#line:67
        OOO000OOO0OOO0O0O .setWindowTitle ("Settings")#line:68
        OOO000OOO0OOO0O0O .resize (300 ,200 )#line:69
        OOO000OOO0OOO0O0O .private_mode_enabled =OO00OO00O0OO0OOOO #line:70
        OOO000OOO0OOO0O0O .vpn_enabled =O0OO00O0O000O00O0 #line:71
        OOO000OOO0OOO0O0O .adblock_enabled =O00O0OOO00O00O000 #line:72
        OOO000OOO0OOO0O0O .antivirus_enabled =OO0OOOOOO0O0OO0OO #line:73
        O0O00O0OOOO00O0OO =QVBoxLayout ()#line:74
        OOO000OOO0OOO0O0O .private_checkbox =QCheckBox ("Private Mode")#line:75
        OOO000OOO0OOO0O0O .private_checkbox .setChecked (OOO000OOO0OOO0O0O .private_mode_enabled )#line:76
        OOO000OOO0OOO0O0O .vpn_checkbox =QCheckBox ("VPN")#line:77
        OOO000OOO0OOO0O0O .vpn_checkbox .setChecked (OOO000OOO0OOO0O0O .vpn_enabled )#line:78
        OOO000OOO0OOO0O0O .adblock_checkbox =QCheckBox ("AdBlock")#line:79
        OOO000OOO0OOO0O0O .adblock_checkbox .setChecked (OOO000OOO0OOO0O0O .adblock_enabled )#line:80
        OOO000OOO0OOO0O0O .antivirus_checkbox =QCheckBox ("AntiVirus")#line:81
        OOO000OOO0OOO0O0O .antivirus_checkbox .setChecked (OOO000OOO0OOO0O0O .antivirus_enabled )#line:82
        O0O00O0OOOO00O0OO .addWidget (QLabel ("Toggle Features:"))#line:83
        O0O00O0OOOO00O0OO .addWidget (OOO000OOO0OOO0O0O .private_checkbox )#line:84
        O0O00O0OOOO00O0OO .addWidget (OOO000OOO0OOO0O0O .vpn_checkbox )#line:85
        O0O00O0OOOO00O0OO .addWidget (OOO000OOO0OOO0O0O .adblock_checkbox )#line:86
        O0O00O0OOOO00O0OO .addWidget (OOO000OOO0OOO0O0O .antivirus_checkbox )#line:87
        OOO0O0O00O0OOO0OO =QHBoxLayout ()#line:88
        OO0O0O0O0O0O00OO0 =QPushButton ("OK")#line:89
        OO0O0O0O0O0O00OO0 .clicked .connect (OOO000OOO0OOO0O0O .accept )#line:90
        O0O00O0O0O0000O00 =QPushButton ("Cancel")#line:91
        O0O00O0O0O0000O00 .clicked .connect (OOO000OOO0OOO0O0O .reject )#line:92
        OOO0O0O00O0OOO0OO .addWidget (OO0O0O0O0O0O00OO0 )#line:93
        OOO0O0O00O0OOO0OO .addWidget (O0O00O0O0O0000O00 )#line:94
        O0O00O0OOOO00O0OO .addLayout (OOO0O0O00O0OOO0OO )#line:95
        OOO000OOO0OOO0O0O .setLayout (O0O00O0OOOO00O0OO )#line:96
class BrowserTab (QWidget ):#line:97
    def __init__ (OO0OO0O0O00000000 ,OO0OOO00OOOOOO000 ,O00O0OOOOO0000OO0 ):#line:98
        super ().__init__ ()#line:99
        OO0OO0O0O00000000 .layout =QVBoxLayout (OO0OO0O0O00000000 )#line:100
        OO0OO0O0O00000000 .navbar =QHBoxLayout ()#line:101
        OO0OO0O0O00000000 .back_btn =QPushButton ("Back")#line:102
        OO0OO0O0O00000000 .forward_btn =QPushButton ("Forward")#line:103
        OO0OO0O0O00000000 .address_bar =QLineEdit ()#line:104
        OO0OO0O0O00000000 .address_bar .setPlaceholderText ("Enter URL")#line:105
        OO0OO0O0O00000000 .go_btn =QPushButton ("Go")#line:106
        OO0OO0O0O00000000 .go_btn .clicked .connect (OO0OO0O0O00000000 .load_url )#line:107
        OO0OO0O0O00000000 .address_bar .returnPressed .connect (OO0OO0O0O00000000 .load_url )#line:108
        OO0OO0O0O00000000 .navbar .addWidget (OO0OO0O0O00000000 .back_btn )#line:109
        OO0OO0O0O00000000 .navbar .addWidget (OO0OO0O0O00000000 .forward_btn )#line:110
        OO0OO0O0O00000000 .navbar .addWidget (OO0OO0O0O00000000 .address_bar )#line:111
        OO0OO0O0O00000000 .navbar .addWidget (OO0OO0O0O00000000 .go_btn )#line:112
        OO0OO0O0O00000000 .layout .addLayout (OO0OO0O0O00000000 .navbar )#line:113
        OO0OO0O0O00000000 .browser =QWebEngineView ()#line:114
        OO0OO0O0O00000000 .browser .page ().profile ().setUrlRequestInterceptor (OO0OOO00OOOOOO000 )#line:115
        OO0OO0O0O00000000 .back_btn .clicked .connect (OO0OO0O0O00000000 .browser .back )#line:116
        OO0OO0O0O00000000 .forward_btn .clicked .connect (OO0OO0O0O00000000 .browser .forward )#line:117
        OO0OO0O0O00000000 .layout .addWidget (OO0OO0O0O00000000 .browser )#line:118
        OO0OO0O0O00000000 .browser .setUrl (QUrl (O00O0OOOOO0000OO0 ))#line:119
    def load_url (OOOO0O0O0OO0000OO ):#line:120
        O0O0O00O000000000 =OOOO0O0O0OO0000OO .address_bar .text ().strip ()#line:121
        if O0O0O00O000000000 and not O0O0O00O000000000 .startswith ("http"):#line:122
            O0O0O00O000000000 ="https://"+O0O0O00O000000000 #line:123
        OOOO0O0O0OO0000OO .browser .setUrl (QUrl (O0O0O00O000000000 ))#line:124
class MainWindow (QMainWindow ):#line:125
    def __init__ (OOOO0O0OO00O0OOOO ):#line:126
        super ().__init__ ()#line:127
        OOOO0O0OO00O0OOOO .setWindowTitle ("GDCE Browser")#line:128
        OOOO0O0OO00O0OOOO .setWindowIcon (QIcon ("logo.png"))#line:129
        OOOO0O0OO00O0OOOO .resize (1280 ,800 )#line:130
        OOOO0O0OO00O0OOOO .appdata_dir =OOOO0O0OO00O0OOOO .get_appdata_dir ()#line:131
        OOOO0O0OO00O0OOOO .history_file =os .path .join (OOOO0O0OO00O0OOOO .appdata_dir ,"history.json")#line:132
        OOOO0O0OO00O0OOOO .ensure_history_file ()#line:133
        OOOO0O0OO00O0OOOO .homepage ="https://gamedigitalcurrencyexchange.cc"#line:134
        OOOO0O0OO00O0OOOO .adblock_enabled =True #line:135
        OOOO0O0OO00O0OOOO .private_mode_enabled =False #line:136
        OOOO0O0OO00O0OOOO .vpn_enabled =False #line:137
        OOOO0O0OO00O0OOOO .antivirus_enabled =True #line:138
        OOOO0O0OO00O0OOOO .ad_interceptor =AdBlockInterceptor (OOOO0O0OO00O0OOOO .adblock_enabled )#line:139
        OOOO0O0OO00O0OOOO .init_ui ()#line:140
    def get_appdata_dir (OOO0000OO0OO0O0OO ):#line:141
        OOOO000O0O0O00O00 =os .getenv ("APPDATA")if os .name =="nt"else os .path .expanduser ("~")#line:142
        OO0O00OOOOO00OO00 =os .path .join (OOOO000O0O0O00O00 ,"GDCEBROWSER")#line:143
        if not os .path .exists (OO0O00OOOOO00OO00 ):#line:144
            os .makedirs (OO0O00OOOOO00OO00 )#line:145
        return OO0O00OOOOO00OO00 #line:146
    def ensure_history_file (O0OO0OOOO0OO0O00O ):#line:147
        if not os .path .exists (O0OO0OOOO0OO0O00O .history_file ):#line:148
            with open (O0OO0OOOO0OO0O00O .history_file ,"w")as O000O0000OO00O0O0 :#line:149
                json .dump ([],O000O0000OO00O0O0 )#line:150
    def init_ui (OOOOO000OO0OO0000 ):#line:151
        OOOOOO000OO0000O0 =QVBoxLayout ()#line:152
        OO0OOOO000O00OOOO =QHBoxLayout ()#line:153
        O0OO00O00O000OO0O =QPushButton ("New Tab")#line:154
        O0OO00O00O000OO0O .clicked .connect (OOOOO000OO0OO0000 .add_browser_tab )#line:155
        O0000000O00OOO0OO =QPushButton ("History")#line:156
        O0000000O00OOO0OO .clicked .connect (OOOOO000OO0OO0000 .open_history )#line:157
        O000O00O0OOO0000O =QPushButton ("Settings")#line:158
        O000O00O0OOO0000O .clicked .connect (OOOOO000OO0OO0000 .open_settings )#line:159
        OO0OOOO000O00OOOO .addWidget (O0OO00O00O000OO0O )#line:160
        OO0OOOO000O00OOOO .addWidget (O0000000O00OOO0OO )#line:161
        OO0OOOO000O00OOOO .addWidget (O000O00O0OOO0000O )#line:162
        OOOOOO000OO0000O0 .addLayout (OO0OOOO000O00OOOO )#line:163
        OOOOO000OO0OO0000 .browser_tabs =QTabWidget ()#line:164
        OOOOO000OO0OO0000 .browser_tabs .setTabsClosable (True )#line:165
        OOOOO000OO0OO0000 .browser_tabs .tabCloseRequested .connect (OOOOO000OO0OO0000 .close_browser_tab )#line:166
        OOOOOO000OO0000O0 .addWidget (OOOOO000OO0OO0000 .browser_tabs )#line:167
        OO00O0O0O0OOO0OOO =QWidget ()#line:168
        OO00O0O0O0OOO0OOO .setLayout (OOOOOO000OO0000O0 )#line:169
        OOOOO000OO0OO0000 .setCentralWidget (OO00O0O0O0OOO0OOO )#line:170
        OOOOO000OO0OO0000 .add_browser_tab ()#line:171
    def add_browser_tab (O0OOO0OOO0OO000OO ):#line:172
        O00OO00O00OOOOO00 =BrowserTab (O0OOO0OOO0OO000OO .ad_interceptor ,O0OOO0OOO0OO000OO .homepage )#line:173
        O0OOO000O0OO0O000 =O0OOO0OOO0OO000OO .browser_tabs .addTab (O00OO00O00OOOOO00 ,"New Tab")#line:174
        O0OOO0OOO0OO000OO .browser_tabs .setCurrentIndex (O0OOO000O0OO0O000 )#line:175
        O00OO00O00OOOOO00 .go_btn .clicked .connect (lambda :O0OOO0OOO0OO000OO .log_history (O00OO00O00OOOOO00 .address_bar .text ().strip ()))#line:176
        O00OO00O00OOOOO00 .address_bar .returnPressed .connect (lambda :O0OOO0OOO0OO000OO .log_history (O00OO00O00OOOOO00 .address_bar .text ().strip ()))#line:177
    def close_browser_tab (O00OO00O0O00O00O0 ,O0000O0000O0O0O00 ):#line:178
        if O00OO00O0O00O00O0 .browser_tabs .count ()>1 :#line:179
            O00OO00O0O00O00O0 .browser_tabs .removeTab (O0000O0000O0O0O00 )#line:180
    def open_history (OOOO000OOO0OOOOOO ):#line:181
        O0OO000O00OOO0O00 =HistoryDialog (OOOO000OOO0OOOOOO .history_file ,OOOO000OOO0OOOOOO )#line:182
        O0OO000O00OOO0O00 .exec_ ()#line:183
    def open_settings (OO000OO0OOOO0O000 ):#line:184
        O00O00O000OO00OOO =SettingsDialog (OO000OO0OOOO0O000 ,OO000OO0OOOO0O000 .private_mode_enabled ,OO000OO0OOOO0O000 .vpn_enabled ,OO000OO0OOOO0O000 .adblock_enabled ,OO000OO0OOOO0O000 .antivirus_enabled )#line:185
        if O00O00O000OO00OOO .exec_ ():#line:186
            OO000OO0OOOO0O000 .private_mode_enabled =O00O00O000OO00OOO .private_checkbox .isChecked ()#line:187
            OO000OO0OOOO0O000 .vpn_enabled =O00O00O000OO00OOO .vpn_checkbox .isChecked ()#line:188
            OO000OO0OOOO0O000 .adblock_enabled =O00O00O000OO00OOO .adblock_checkbox .isChecked ()#line:189
            OO000OO0OOOO0O000 .antivirus_enabled =O00O00O000OO00OOO .antivirus_checkbox .isChecked ()#line:190
            OO000OO0OOOO0O000 .ad_interceptor .enabled =OO000OO0OOOO0O000 .adblock_enabled #line:191
    def log_history (O0OO0OO0OOO0OO000 ,O00OO0O0OOOOOO000 ):#line:192
        if O00OO0O0OOOOOO000 :#line:193
            OO00O0O0000O0000O ={"url":O00OO0O0OOOOOO000 ,"timestamp":time .time ()}#line:194
            try :#line:195
                with open (O0OO0OO0OOO0OO000 .history_file ,"r")as O0O00O000OOO0OO0O :#line:196
                    OOO00OOOOO0OO0O0O =json .load (O0O00O000OOO0OO0O )#line:197
            except :#line:198
                OOO00OOOOO0OO0O0O =[]#line:199
            OOO00OOOOO0OO0O0O .append (OO00O0O0000O0000O )#line:200
            with open (O0OO0OO0OOO0OO000 .history_file ,"w")as O0O00O000OOO0OO0O :#line:201
                json .dump (OOO00OOOOO0OO0O0O ,O0O00O000OOO0OO0O )#line:202
def check_update_status ():#line:203
    OOO00OO000OO0OO0O ="https://raw.githubusercontent.com/Infernalblight/GDCEBROWSER/refs/heads/main/Status"#line:204
    try :#line:205
        with urllib .request .urlopen (OOO00OO000OO0OO0O ,timeout =5 )as OO0OO00O00000OOOO :#line:206
            O0000OOO0OOO00O0O =OO0OO00O00000OOOO .read ().decode ("utf-8").strip ()#line:207
    except Exception as OOOO0OO00O00O0OO0 :#line:208
        O0000OOO0OOO00O0O ="False"#line:209
    if O0000OOO0OOO00O0O !="True":#line:210
        QMessageBox .information (None ,"Update Required","A new update is available!\n\nPlease visit the GDCE Discord server and check the announcements for the latest version.\n\nThe browser will now exit.")#line:211
        sys .exit (0 )#line:212
if __name__ =="__main__":#line:213
    app =QApplication (sys .argv )#line:214
    check_update_status ()#line:215
    window =MainWindow ()#line:216
    window .setStyleSheet ("""
        QMainWindow { background-color: #1e1e2f; }
        QTabWidget::pane { border: 1px solid #3e3e5e; background: #2e2e3e; }
        QTabBar::tab { background: #3e3e5e; color: #ffffff; padding: 10px; }
        QTabBar::tab:selected { background: #5e5e7e; }
        QLineEdit { background-color: #2e2e3e; color: #ffffff; padding: 8px; border: 1px solid #3e3e5e; border-radius: 4px; }
        QPushButton { background-color: #3e3e5e; color: #ffffff; padding: 8px; border: 1px solid #5e5e7e; border-radius: 4px; }
        QPushButton:hover { background-color: #5e5e7e; }
        QCheckBox { color: #ffffff; }
        QCheckBox::indicator { width: 20px; height: 20px; }
        QCheckBox::indicator:unchecked { background-color: #2e2e3e; border: 1px solid #ffffff; }
        QCheckBox::indicator:checked { background-color: #5e5e7e; border: 1px solid #ffffff; }
        QListWidget { background-color: #2e2e3e; color: #ffffff; }
        QLabel { color: #ffffff; }
    """)#line:231
    window .show ()#line:232
    sys .exit (app .exec_ ())#line:233
