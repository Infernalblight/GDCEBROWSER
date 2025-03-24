import sys ,os ,json ,time ,urllib .request #line:1
from PyQt5 .QtWidgets import (QApplication ,QMainWindow ,QWidget ,QVBoxLayout ,QHBoxLayout ,QLineEdit ,QPushButton ,QTabWidget ,QDialog ,QListWidget ,QCheckBox ,QLabel ,QMessageBox ,QInputDialog )#line:2
from PyQt5 .QtWebEngineWidgets import QWebEngineView #line:3
from PyQt5 .QtWebEngineCore import QWebEngineUrlRequestInterceptor #line:4
from PyQt5 .QtCore import QUrl #line:5
from PyQt5 .QtGui import QIcon #line:6
class AdBlockInterceptor (QWebEngineUrlRequestInterceptor ):#line:7
    def __init__ (O000O000000O0O000 ,enabled =True ,parent =None ):#line:8
        super ().__init__ (parent )#line:9
        O000O000000O0O000 .enabled =enabled #line:10
        O000O000000O0O000 .block_list =["ads.","tracking.","18plus."]#line:11
    def interceptRequest (O00O00OO0O0OOOO00 ,O00OOOO0OO000O0OO ):#line:12
        if O00O00OO0O0OOOO00 .enabled :#line:13
            O00O0O0O00OOOOO00 =O00OOOO0OO000O0OO .requestUrl ().toString ()#line:14
            for O0O00OOO000OOOO00 in O00O00OO0O0OOOO00 .block_list :#line:15
                if O0O00OOO000OOOO00 in O00O0O0O00OOOOO00 :#line:16
                    O00OOOO0OO000O0OO .block (True )#line:17
                    break #line:18
class HistoryDialog (QDialog ):#line:19
    def __init__ (OO00OOOOO0O0000O0 ,OO00OOOOOOOOOO000 ,parent =None ):#line:20
        super ().__init__ (parent )#line:21
        OO00OOOOO0O0000O0 .setWindowTitle ("History")#line:22
        OO00OOOOO0O0000O0 .history_file =OO00OOOOOOOOOO000 #line:23
        OO00OOOOO0O0000O0 .resize (500 ,400 )#line:24
        O000OOOO00O0O0O0O =QVBoxLayout ()#line:25
        OO00OOOOO0O0000O0 .history_list =QListWidget ()#line:26
        OO00OOOOO0O0000O0 .load_history ()#line:27
        OO00OOOOO0O0000O0 .clear_history_button =QPushButton ("Clear History")#line:28
        OO00OOOOO0O0000O0 .clear_history_button .clicked .connect (OO00OOOOO0O0000O0 .clear_history )#line:29
        O000OOOO00O0O0O0O .addWidget (OO00OOOOO0O0000O0 .history_list )#line:30
        O000OOOO00O0O0O0O .addWidget (OO00OOOOO0O0000O0 .clear_history_button )#line:31
        OO00OOOOO0O0000O0 .setLayout (O000OOOO00O0O0O0O )#line:32
    def load_history (OOOO00OOO00O0O0O0 ):#line:33
        OOOO00OOO00O0O0O0 .history_list .clear ()#line:34
        try :#line:35
            with open (OOOO00OOO00O0O0O0 .history_file ,"r")as O00000000O000OO00 :#line:36
                OO0OO0O0OOOOO0O0O =json .load (O00000000O000OO00 )#line:37
        except :#line:38
            OO0OO0O0OOOOO0O0O =[]#line:39
        for OO0OO0OO000OO0O00 in OO0OO0O0OOOOO0O0O :#line:40
            if isinstance (OO0OO0OO000OO0O00 ,dict ):#line:41
                O00OOO0O00O0O00OO =OO0OO0OO000OO0O00 .get ("url","")#line:42
            else :#line:43
                O00OOO0O00O0O00OO =OO0OO0OO000OO0O00 #line:44
            OOOO00OOO00O0O0O0 .history_list .addItem (O00OOO0O00O0O00OO )#line:45
    def clear_history (OOO0OOO0O0O0O0000 ):#line:46
        OOO0OOO0OOOOO00OO =["1 hr","1 d","3 d","7 d","20 d","1 month","1 year","All time"]#line:47
        OO00000OOOO00OOO0 ,OO000000O00OO0O0O =QInputDialog .getItem (OOO0OOO0O0O0O0000 ,"Clear History","Delete history older than:",OOO0OOO0OOOOO00OO ,0 ,False )#line:48
        if OO000000O00OO0O0O :#line:49
            OO000OO0OOOO0O000 =time .time ()#line:50
            OOOO00OOO0000O0OO ={"1 hr":3600 ,"1 d":86400 ,"3 d":3 *86400 ,"7 d":7 *86400 ,"20 d":20 *86400 ,"1 month":30 *86400 ,"1 year":365 *86400 ,"All time":None }#line:51
            O00OOO00OOO00000O =OOOO00OOO0000O0OO .get (OO00000OOOO00OOO0 )#line:52
            try :#line:53
                with open (OOO0OOO0O0O0O0000 .history_file ,"r")as OO00000O0O000OOOO :#line:54
                    OOOOO000O00O00O0O =json .load (OO00000O0O000OOOO )#line:55
            except :#line:56
                OOOOO000O00O00O0O =[]#line:57
            if O00OOO00OOO00000O is None :#line:58
                OOOOO000O00O00O0O =[]#line:59
            else :#line:60
                OOOOO000O00O00O0O =[OO0OO0000OO0000OO for OO0OO0000OO0000OO in OOOOO000O00O00O0O if (OO000OO0OOOO0O000 -(OO0OO0000OO0000OO .get ("timestamp",OO000OO0OOOO0O000 )if isinstance (OO0OO0000OO0000OO ,dict )else OO000OO0OOOO0O000 ))<O00OOO00OOO00000O ]#line:61
            with open (OOO0OOO0O0O0O0000 .history_file ,"w")as OO00000O0O000OOOO :#line:62
                json .dump (OOOOO000O00O00O0O ,OO00000O0O000OOOO )#line:63
            OOO0OOO0O0O0O0000 .load_history ()#line:64
class SettingsDialog (QDialog ):#line:65
    def __init__ (OO0O00O000OO0OO00 ,O000OOO0O0O0O0O0O ,OO00O0O000OOO0O0O ,O0OOOOO0O000OOO0O ,OOOO00O00O000O0OO ,O0000O00OOO0O0OO0 ):#line:66
        super ().__init__ (O000OOO0O0O0O0O0O )#line:67
        OO0O00O000OO0OO00 .setWindowTitle ("Settings")#line:68
        OO0O00O000OO0OO00 .resize (300 ,200 )#line:69
        OO0O00O000OO0OO00 .private_mode_enabled =OO00O0O000OOO0O0O #line:70
        OO0O00O000OO0OO00 .vpn_enabled =O0OOOOO0O000OOO0O #line:71
        OO0O00O000OO0OO00 .adblock_enabled =OOOO00O00O000O0OO #line:72
        OO0O00O000OO0OO00 .antivirus_enabled =O0000O00OOO0O0OO0 #line:73
        O00OOOO000O00O00O =QVBoxLayout ()#line:74
        OO0O00O000OO0OO00 .private_checkbox =QCheckBox ("Private Mode")#line:75
        OO0O00O000OO0OO00 .private_checkbox .setChecked (OO0O00O000OO0OO00 .private_mode_enabled )#line:76
        OO0O00O000OO0OO00 .vpn_checkbox =QCheckBox ("VPN")#line:77
        OO0O00O000OO0OO00 .vpn_checkbox .setChecked (OO0O00O000OO0OO00 .vpn_enabled )#line:78
        OO0O00O000OO0OO00 .adblock_checkbox =QCheckBox ("AdBlock")#line:79
        OO0O00O000OO0OO00 .adblock_checkbox .setChecked (OO0O00O000OO0OO00 .adblock_enabled )#line:80
        OO0O00O000OO0OO00 .antivirus_checkbox =QCheckBox ("AntiVirus")#line:81
        OO0O00O000OO0OO00 .antivirus_checkbox .setChecked (OO0O00O000OO0OO00 .antivirus_enabled )#line:82
        O00OOOO000O00O00O .addWidget (QLabel ("Toggle Features:"))#line:83
        O00OOOO000O00O00O .addWidget (OO0O00O000OO0OO00 .private_checkbox )#line:84
        O00OOOO000O00O00O .addWidget (OO0O00O000OO0OO00 .vpn_checkbox )#line:85
        O00OOOO000O00O00O .addWidget (OO0O00O000OO0OO00 .adblock_checkbox )#line:86
        O00OOOO000O00O00O .addWidget (OO0O00O000OO0OO00 .antivirus_checkbox )#line:87
        OO0O000O0O00000O0 =QHBoxLayout ()#line:88
        O0OO000O00O0000O0 =QPushButton ("OK")#line:89
        O0OO000O00O0000O0 .clicked .connect (OO0O00O000OO0OO00 .accept )#line:90
        O0O0OO00O0OOOO0O0 =QPushButton ("Cancel")#line:91
        O0O0OO00O0OOOO0O0 .clicked .connect (OO0O00O000OO0OO00 .reject )#line:92
        OO0O000O0O00000O0 .addWidget (O0OO000O00O0000O0 )#line:93
        OO0O000O0O00000O0 .addWidget (O0O0OO00O0OOOO0O0 )#line:94
        O00OOOO000O00O00O .addLayout (OO0O000O0O00000O0 )#line:95
        OO0O00O000OO0OO00 .setLayout (O00OOOO000O00O00O )#line:96
class BrowserTab (QWidget ):#line:97
    def __init__ (O00OOOOO00O0O0OO0 ,O0O0000OO0O00OOOO ,OO00000OOO0OO000O ):#line:98
        super ().__init__ ()#line:99
        O00OOOOO00O0O0OO0 .layout =QVBoxLayout (O00OOOOO00O0O0OO0 )#line:100
        O00OOOOO00O0O0OO0 .navbar =QHBoxLayout ()#line:101
        O00OOOOO00O0O0OO0 .back_btn =QPushButton ("Back")#line:102
        O00OOOOO00O0O0OO0 .forward_btn =QPushButton ("Forward")#line:103
        O00OOOOO00O0O0OO0 .address_bar =QLineEdit ()#line:104
        O00OOOOO00O0O0OO0 .address_bar .setPlaceholderText ("Enter URL")#line:105
        O00OOOOO00O0O0OO0 .go_btn =QPushButton ("Go")#line:106
        O00OOOOO00O0O0OO0 .go_btn .clicked .connect (O00OOOOO00O0O0OO0 .load_url )#line:107
        O00OOOOO00O0O0OO0 .address_bar .returnPressed .connect (O00OOOOO00O0O0OO0 .load_url )#line:108
        O00OOOOO00O0O0OO0 .navbar .addWidget (O00OOOOO00O0O0OO0 .back_btn )#line:109
        O00OOOOO00O0O0OO0 .navbar .addWidget (O00OOOOO00O0O0OO0 .forward_btn )#line:110
        O00OOOOO00O0O0OO0 .navbar .addWidget (O00OOOOO00O0O0OO0 .address_bar )#line:111
        O00OOOOO00O0O0OO0 .navbar .addWidget (O00OOOOO00O0O0OO0 .go_btn )#line:112
        O00OOOOO00O0O0OO0 .layout .addLayout (O00OOOOO00O0O0OO0 .navbar )#line:113
        O00OOOOO00O0O0OO0 .browser =QWebEngineView ()#line:114
        O00OOOOO00O0O0OO0 .browser .page ().profile ().setUrlRequestInterceptor (O0O0000OO0O00OOOO )#line:115
        O00OOOOO00O0O0OO0 .back_btn .clicked .connect (O00OOOOO00O0O0OO0 .browser .back )#line:116
        O00OOOOO00O0O0OO0 .forward_btn .clicked .connect (O00OOOOO00O0O0OO0 .browser .forward )#line:117
        O00OOOOO00O0O0OO0 .layout .addWidget (O00OOOOO00O0O0OO0 .browser )#line:118
        O00OOOOO00O0O0OO0 .browser .setUrl (QUrl (OO00000OOO0OO000O ))#line:119
    def load_url (OO0OOOOOOO000O0OO ):#line:120
        O0OO0O0OOOO000000 =OO0OOOOOOO000O0OO .address_bar .text ().strip ()#line:121
        if O0OO0O0OOOO000000 and not O0OO0O0OOOO000000 .startswith ("http"):#line:122
            O0OO0O0OOOO000000 ="https://"+O0OO0O0OOOO000000 #line:123
        OO0OOOOOOO000O0OO .browser .setUrl (QUrl (O0OO0O0OOOO000000 ))#line:124
class MainWindow (QMainWindow ):#line:125
    def __init__ (OOOO0OOO0O0OO00O0 ):#line:126
        super ().__init__ ()#line:127
        OOOO0OOO0O0OO00O0 .setWindowTitle ("GDCE Browser")#line:128
        OOOO0OOO0O0OO00O0 .setWindowIcon (QIcon ("logo.png"))#line:129
        OOOO0OOO0O0OO00O0 .resize (1280 ,800 )#line:130
        OOOO0OOO0O0OO00O0 .appdata_dir =OOOO0OOO0O0OO00O0 .get_appdata_dir ()#line:131
        OOOO0OOO0O0OO00O0 .history_file =os .path .join (OOOO0OOO0O0OO00O0 .appdata_dir ,"history.json")#line:132
        OOOO0OOO0O0OO00O0 .ensure_history_file ()#line:133
        OOOO0OOO0O0OO00O0 .homepage ="https://gamedigitalcurrencyexchange.cc"#line:134
        OOOO0OOO0O0OO00O0 .adblock_enabled =True #line:135
        OOOO0OOO0O0OO00O0 .private_mode_enabled =False #line:136
        OOOO0OOO0O0OO00O0 .vpn_enabled =False #line:137
        OOOO0OOO0O0OO00O0 .antivirus_enabled =True #line:138
        OOOO0OOO0O0OO00O0 .ad_interceptor =AdBlockInterceptor (OOOO0OOO0O0OO00O0 .adblock_enabled )#line:139
        OOOO0OOO0O0OO00O0 .init_ui ()#line:140
    def get_appdata_dir (O0OO0000O0OO0OO00 ):#line:141
        O0O0OOO0O0O00O0O0 =os .getenv ("APPDATA")if os .name =="nt"else os .path .expanduser ("~")#line:142
        OOO000OOO00O0OOO0 =os .path .join (O0O0OOO0O0O00O0O0 ,"GDCEBROWSER")#line:143
        if not os .path .exists (OOO000OOO00O0OOO0 ):#line:144
            os .makedirs (OOO000OOO00O0OOO0 )#line:145
        return OOO000OOO00O0OOO0 #line:146
    def ensure_history_file (OO0OOO00OOO0000OO ):#line:147
        if not os .path .exists (OO0OOO00OOO0000OO .history_file ):#line:148
            with open (OO0OOO00OOO0000OO .history_file ,"w")as OO0O0OOO00O0O00O0 :#line:149
                json .dump ([],OO0O0OOO00O0O00O0 )#line:150
    def init_ui (OO0OOO0O000O00O0O ):#line:151
        OOO00O00000O0OO0O =QVBoxLayout ()#line:152
        O0OO00O0O0OOO0OO0 =QHBoxLayout ()#line:153
        O0OOOO0000000OO0O =QPushButton ("New Tab")#line:154
        O0OOOO0000000OO0O .clicked .connect (OO0OOO0O000O00O0O .add_browser_tab )#line:155
        OOO0000OO00O0000O =QPushButton ("History")#line:156
        OOO0000OO00O0000O .clicked .connect (OO0OOO0O000O00O0O .open_history )#line:157
        OO0O0O0000OO0O0OO =QPushButton ("Settings")#line:158
        OO0O0O0000OO0O0OO .clicked .connect (OO0OOO0O000O00O0O .open_settings )#line:159
        O0OO00O0O0OOO0OO0 .addWidget (O0OOOO0000000OO0O )#line:160
        O0OO00O0O0OOO0OO0 .addWidget (OOO0000OO00O0000O )#line:161
        O0OO00O0O0OOO0OO0 .addWidget (OO0O0O0000OO0O0OO )#line:162
        OOO00O00000O0OO0O .addLayout (O0OO00O0O0OOO0OO0 )#line:163
        OO0OOO0O000O00O0O .browser_tabs =QTabWidget ()#line:164
        OO0OOO0O000O00O0O .browser_tabs .setTabsClosable (True )#line:165
        OO0OOO0O000O00O0O .browser_tabs .tabCloseRequested .connect (OO0OOO0O000O00O0O .close_browser_tab )#line:166
        OOO00O00000O0OO0O .addWidget (OO0OOO0O000O00O0O .browser_tabs )#line:167
        O00OO0OOO00OO00O0 =QWidget ()#line:168
        O00OO0OOO00OO00O0 .setLayout (OOO00O00000O0OO0O )#line:169
        OO0OOO0O000O00O0O .setCentralWidget (O00OO0OOO00OO00O0 )#line:170
        OO0OOO0O000O00O0O .add_browser_tab ()#line:171
    def add_browser_tab (O00000000O00OO00O ):#line:172
        O00O0OO0OOO0OOOO0 =BrowserTab (O00000000O00OO00O .ad_interceptor ,O00000000O00OO00O .homepage )#line:173
        OO0OOO0O0OOOO0OOO =O00000000O00OO00O .browser_tabs .addTab (O00O0OO0OOO0OOOO0 ,"New Tab")#line:174
        O00000000O00OO00O .browser_tabs .setCurrentIndex (OO0OOO0O0OOOO0OOO )#line:175
        O00O0OO0OOO0OOOO0 .go_btn .clicked .connect (lambda :O00000000O00OO00O .log_history (O00O0OO0OOO0OOOO0 .address_bar .text ().strip ()))#line:176
        O00O0OO0OOO0OOOO0 .address_bar .returnPressed .connect (lambda :O00000000O00OO00O .log_history (O00O0OO0OOO0OOOO0 .address_bar .text ().strip ()))#line:177
    def close_browser_tab (OOOOO0000OOO00O00 ,OO00OOO0000O00OOO ):#line:178
        if OOOOO0000OOO00O00 .browser_tabs .count ()>1 :#line:179
            OOOOO0000OOO00O00 .browser_tabs .removeTab (OO00OOO0000O00OOO )#line:180
    def open_history (O0OOO000OO000O000 ):#line:181
        OO00OOOOO0000OO00 =HistoryDialog (O0OOO000OO000O000 .history_file ,O0OOO000OO000O000 )#line:182
        OO00OOOOO0000OO00 .exec_ ()#line:183
    def open_settings (OOO0OO00OO00O0O0O ):#line:184
        O000OOO00OOO0O000 =SettingsDialog (OOO0OO00OO00O0O0O ,OOO0OO00OO00O0O0O .private_mode_enabled ,OOO0OO00OO00O0O0O .vpn_enabled ,OOO0OO00OO00O0O0O .adblock_enabled ,OOO0OO00OO00O0O0O .antivirus_enabled )#line:185
        if O000OOO00OOO0O000 .exec_ ():#line:186
            OOO0OO00OO00O0O0O .private_mode_enabled =O000OOO00OOO0O000 .private_checkbox .isChecked ()#line:187
            OOO0OO00OO00O0O0O .vpn_enabled =O000OOO00OOO0O000 .vpn_checkbox .isChecked ()#line:188
            OOO0OO00OO00O0O0O .adblock_enabled =O000OOO00OOO0O000 .adblock_checkbox .isChecked ()#line:189
            OOO0OO00OO00O0O0O .antivirus_enabled =O000OOO00OOO0O000 .antivirus_checkbox .isChecked ()#line:190
            OOO0OO00OO00O0O0O .ad_interceptor .enabled =OOO0OO00OO00O0O0O .adblock_enabled #line:191
    def log_history (OO00O0OOO0000OO0O ,O00OO0000O00OOO00 ):#line:192
        if O00OO0000O00OOO00 :#line:193
            OO0OO0O0O0O0OO00O ={"url":O00OO0000O00OOO00 ,"timestamp":time .time ()}#line:194
            try :#line:195
                with open (OO00O0OOO0000OO0O .history_file ,"r")as OOOO00O0OO000OOOO :#line:196
                    O00OO0O0O0OO0OOOO =json .load (OOOO00O0OO000OOOO )#line:197
            except :#line:198
                O00OO0O0O0OO0OOOO =[]#line:199
            O00OO0O0O0OO0OOOO .append (OO0OO0O0O0O0OO00O )#line:200
            with open (OO00O0OOO0000OO0O .history_file ,"w")as OOOO00O0OO000OOOO :#line:201
                json .dump (O00OO0O0O0OO0OOOO ,OOOO00O0OO000OOOO )#line:202
def check_update_status ():#line:203
    O0O0OOO0O000O0OOO ="https://raw.githubusercontent.com/Infernalblight/GDCEBROWSER/refs/heads/main/Status"#line:204
    try :#line:205
        with urllib .request .urlopen (O0O0OOO0O000O0OOO ,timeout =5 )as O0O0OO00OO000O0O0 :#line:206
            O0OOO0O0O00OO000O =O0O0OO00OO000O0O0 .read ().decode ("utf-8").strip ()#line:207
    except Exception as O00OO0OOO0OOO000O :#line:208
        O0OOO0O0O00OO000O ="False"#line:209
    if O0OOO0O0O00OO000O !="True":#line:210
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
