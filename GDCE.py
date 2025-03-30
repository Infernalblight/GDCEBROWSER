import sys #line:1
import os #line:2
import json #line:3
import time #line:4
from PyQt5 .QtWidgets import (QApplication ,QMainWindow ,QWidget ,QVBoxLayout ,QHBoxLayout ,QLineEdit ,QPushButton ,QTabWidget ,QDialog ,QListWidget ,QLabel ,QMessageBox ,QInputDialog )#line:5
from PyQt5 .QtWebEngineWidgets import QWebEngineView #line:6
from PyQt5 .QtCore import QUrl ,Qt #line:7
from PyQt5 .QtGui import QIcon #line:8
class ExtensionsManager :#line:9
    ""#line:10
    def __init__ (O00OOO0OO0O000O00 ):#line:11
        O00OOO0OO0O000O00 .extensions_dir =os .path .join (os .getcwd (),'extensions')#line:12
        if not os .path .exists (O00OOO0OO0O000O00 .extensions_dir ):#line:13
            os .makedirs (O00OOO0OO0O000O00 .extensions_dir )#line:14
        O00OOO0OO0O000O00 .extensions ={}#line:15
        O00OOO0OO0O000O00 .load_extensions ()#line:16
    def load_extensions (O00O000O0OOO0OO00 ):#line:17
        ""#line:18
        for O0O00O00O000O00OO in os .listdir (O00O000O0OOO0OO00 .extensions_dir ):#line:19
            if O0O00O00O000O00OO .endswith ('.js'):#line:20
                with open (os .path .join (O00O000O0OOO0OO00 .extensions_dir ,O0O00O00O000O00OO ),'r')as O0000O000O0O00O00 :#line:21
                    O00O000O0OOO0OO00 .extensions [O0O00O00O000O00OO ]={'script':O0000O000O0O00O00 .read (),'enabled':True }#line:22
    def get_script (OO000OO0OOOOOO0O0 ,OO00OOOO0O00O00OO ):#line:23
        ""#line:24
        return OO000OO0OOOOOO0O0 .extensions .get (OO00OOOO0O00O00OO ,{}).get ('script')#line:25
    def get_installed_extensions (OO00OOOOO00O00OO0 ):#line:26
        ""#line:27
        return list (OO00OOOOO00O00OO0 .extensions .keys ())#line:28
    def toggle_extension (OO0O0OOO000O0000O ,O0O00000OOOO0O0OO ):#line:29
        ""#line:30
        if O0O00000OOOO0O0OO in OO0O0OOO000O0000O .extensions :#line:31
            OO0O0OOO000O0000O .extensions [O0O00000OOOO0O0OO ]['enabled']=not OO0O0OOO000O0000O .extensions [O0O00000OOOO0O0OO ]['enabled']#line:32
    def remove_extension (O0OOOO00OO0OO00O0 ,OO000O00O0O00O00O ):#line:33
        ""#line:34
        if OO000O00O0O00O00O in O0OOOO00OO0OO00O0 .extensions :#line:35
            del O0OOOO00OO0OO00O0 .extensions [OO000O00O0O00O00O ]#line:36
            os .remove (os .path .join (O0OOOO00OO0OO00O0 .extensions_dir ,OO000O00O0O00O00O ))#line:37
class FullScreenWebEngineView (QWebEngineView ):#line:38
    ""#line:39
    def toggle_full_screen (O0O0OOO00O0OO0O0O ):#line:40
        if O0O0OOO00O0OO0O0O .isFullScreen ():#line:41
            O0O0OOO00O0OO0O0O .setWindowState (O0O0OOO00O0OO0O0O .windowState ()&~Qt .WindowFullScreen )#line:42
        else :#line:43
            O0O0OOO00O0OO0O0O .setWindowState (O0O0OOO00O0OO0O0O .windowState ()|Qt .WindowFullScreen )#line:44
    def inject_script (OOO0OO000OOOO0OO0 ,O0O000O00000O00O0 ):#line:45
        ""#line:46
        OOO0OO000OOOO0OO0 .page ().runJavaScript (O0O000O00000O00O0 )#line:47
class BrowserTab (QWidget ):#line:48
    ""#line:49
    def __init__ (OO0O0OO0OOO0O0O00 ,OO00OO0OOOOOO00OO ,OOO000000O00O000O ):#line:50
        super ().__init__ ()#line:51
        OO0O0OO0OOO0O0O00 .layout =QVBoxLayout (OO0O0OO0OOO0O0O00 )#line:52
        OO0O0OO0OOO0O0O00 .navbar =QHBoxLayout ()#line:53
        OO0O0OO0OOO0O0O00 .back_btn =QPushButton ("Back")#line:54
        OO0O0OO0OOO0O0O00 .forward_btn =QPushButton ("Forward")#line:55
        OO0O0OO0OOO0O0O00 .address_bar =QLineEdit ()#line:56
        OO0O0OO0OOO0O0O00 .address_bar .setPlaceholderText ("Enter URL or Search")#line:57
        OO0O0OO0OOO0O0O00 .go_btn =QPushButton ("Go")#line:58
        OO0O0OO0OOO0O0O00 .go_btn .clicked .connect (OO0O0OO0OOO0O0O00 .load_url )#line:59
        OO0O0OO0OOO0O0O00 .address_bar .returnPressed .connect (OO0O0OO0OOO0O0O00 .load_url )#line:60
        OO0O0OO0OOO0O0O00 .navbar .addWidget (OO0O0OO0OOO0O0O00 .back_btn )#line:61
        OO0O0OO0OOO0O0O00 .navbar .addWidget (OO0O0OO0OOO0O0O00 .forward_btn )#line:62
        OO0O0OO0OOO0O0O00 .navbar .addWidget (OO0O0OO0OOO0O0O00 .address_bar )#line:63
        OO0O0OO0OOO0O0O00 .navbar .addWidget (OO0O0OO0OOO0O0O00 .go_btn )#line:64
        OO0O0OO0OOO0O0O00 .layout .addLayout (OO0O0OO0OOO0O0O00 .navbar )#line:65
        OO0O0OO0OOO0O0O00 .browser =FullScreenWebEngineView ()#line:66
        OO0O0OO0OOO0O0O00 .layout .addWidget (OO0O0OO0OOO0O0O00 .browser )#line:67
        OO0O0OO0OOO0O0O00 .browser .setUrl (QUrl (OO00OO0OOOOOO00OO ))#line:68
        OO0O0OO0OOO0O0O00 .extensions_manager =OOO000000O00O000O #line:69
        OO0O0OO0OOO0O0O00 .inject_extensions ()#line:70
        OO0O0OO0OOO0O0O00 .back_btn .clicked .connect (OO0O0OO0OOO0O0O00 .browser .back )#line:71
        OO0O0OO0OOO0O0O00 .forward_btn .clicked .connect (OO0O0OO0OOO0O0O00 .browser .forward )#line:72
    def inject_extensions (O000OOO0000O0OOOO ):#line:73
        ""#line:74
        for O0OOO0000O000000O in O000OOO0000O0OOOO .extensions_manager .extensions .keys ():#line:75
            if O000OOO0000O0OOOO .extensions_manager .extensions [O0OOO0000O000000O ]['enabled']:#line:76
                OOOOOOO000O00O0O0 =O000OOO0000O0OOOO .extensions_manager .get_script (O0OOO0000O000000O )#line:77
                if OOOOOOO000O00O0O0 :#line:78
                    print (f"Injecting script: {O0OOO0000O000000O}")#line:79
                    O000OOO0000O0OOOO .browser .inject_script (OOOOOOO000O00O0O0 )#line:80
    def load_url (OO0000OOO000O0O0O ):#line:81
        ""#line:82
        OO00O0OOO000OO0OO =OO0000OOO000O0O0O .address_bar .text ().strip ()#line:83
        if OO00O0OOO000OO0OO :#line:84
            if not (OO00O0OOO000OO0OO .startswith ("http://")or OO00O0OOO000OO0OO .startswith ("https://")):#line:85
                OO00O0OOO000OO0OO =f"https://{OO00O0OOO000OO0OO}"#line:86
            OO0000OOO000O0O0O .browser .setUrl (QUrl (OO00O0OOO000OO0OO ))#line:87
            OO0000OOO000O0O0O .address_bar .setText (OO00O0OOO000OO0OO )#line:88
class HistoryDialog (QDialog ):#line:89
    ""#line:90
    def __init__ (O0O000OOOOO00O00O ,OOO000O00OO0O0O0O ,parent =None ):#line:91
        super ().__init__ (parent )#line:92
        O0O000OOOOO00O00O .setWindowTitle ("History")#line:93
        O0O000OOOOO00O00O .history_file =OOO000O00OO0O0O0O #line:94
        O0O000OOOOO00O00O .resize (500 ,400 )#line:95
        OO0000000OOO0OOOO =QVBoxLayout ()#line:96
        O0O000OOOOO00O00O .history_list =QListWidget ()#line:97
        O0O000OOOOO00O00O .load_history ()#line:98
        O0O000OOOOO00O00O .clear_history_button =QPushButton ("Clear History")#line:99
        O0O000OOOOO00O00O .clear_history_button .clicked .connect (O0O000OOOOO00O00O .clear_history )#line:100
        OO0000000OOO0OOOO .addWidget (O0O000OOOOO00O00O .history_list )#line:101
        OO0000000OOO0OOOO .addWidget (O0O000OOOOO00O00O .clear_history_button )#line:102
        O0O000OOOOO00O00O .setLayout (OO0000000OOO0OOOO )#line:103
    def load_history (O00O0O00O0OOO0OO0 ):#line:104
        ""#line:105
        O00O0O00O0OOO0OO0 .history_list .clear ()#line:106
        try :#line:107
            with open (O00O0O00O0OOO0OO0 .history_file ,"r")as O000OO0OOOO00OOO0 :#line:108
                O00000O0OOO000OOO =json .load (O000OO0OOOO00OOO0 )#line:109
        except :#line:110
            O00000O0OOO000OOO =[]#line:111
        for OOO0O00O0OO000OO0 in O00000O0OOO000OOO :#line:112
            if isinstance (OOO0O00O0OO000OO0 ,dict ):#line:113
                O0O000OO00OOOO00O =OOO0O00O0OO000OO0 .get ("url","")#line:114
            else :#line:115
                O0O000OO00OOOO00O =OOO0O00O0OO000OO0 #line:116
            O00O0O00O0OOO0OO0 .history_list .addItem (O0O000OO00OOOO00O )#line:117
    def clear_history (O0000000OOOO0OOOO ):#line:118
        ""#line:119
        O0OOO0OO000O00O0O =["1 hr","1 d","3 d","7 d","20 d","1 month","1 year","All time"]#line:120
        OOOO0O000000O000O ,O0OOOO00O000O0O00 =QInputDialog .getItem (O0000000OOOO0OOOO ,"Clear History","Delete history older than:",O0OOO0OO000O00O0O ,0 ,False )#line:121
        if O0OOOO00O000O0O00 :#line:122
            O00O0O00000O0000O =time .time ()#line:123
            OO0OO00OOOOO0OO0O ={"1 hr":3600 ,"1 d":86400 ,"3 d":3 *86400 ,"7 d":7 *86400 ,"20 d":20 *86400 ,"1 month":30 *86400 ,"1 year":365 *86400 ,"All time":None }#line:124
            O0OOO00OO00O0OO00 =OO0OO00OOOOO0OO0O .get (OOOO0O000000O000O )#line:125
            try :#line:126
                with open (O0000000OOOO0OOOO .history_file ,"r")as O000O0OOOO0O00O00 :#line:127
                    O00O00OO0O0O00OO0 =json .load (O000O0OOOO0O00O00 )#line:128
            except :#line:129
                O00O00OO0O0O00OO0 =[]#line:130
            if O0OOO00OO00O0OO00 is None :#line:131
                O00O00OO0O0O00OO0 =[]#line:132
            else :#line:133
                O00O00OO0O0O00OO0 =[OOO000O000OOO00O0 for OOO000O000OOO00O0 in O00O00OO0O0O00OO0 if (O00O0O00000O0000O -(OOO000O000OOO00O0 .get ("timestamp",O00O0O00000O0000O )if isinstance (OOO000O000OOO00O0 ,dict )else O00O0O00000O0000O ))<O0OOO00OO00O0OO00 ]#line:134
            with open (O0000000OOOO0OOOO .history_file ,"w")as O000O0OOOO0O00O00 :#line:135
                json .dump (O00O00OO0O0O00OO0 ,O000O0OOOO0O00O00 )#line:136
            O0000000OOOO0OOOO .load_history ()#line:137
class ExtensionsManagerDialog (QDialog ):#line:138
    ""#line:139
    def __init__ (O0OOOOOO00O00O0O0 ,O0O0O0OOO0O0OOOOO ,OOOO0O0O000000O0O ):#line:140
        super ().__init__ (O0O0O0OOO0O0OOOOO )#line:141
        O0OOOOOO00O00O0O0 .setWindowTitle ("Extensions Management")#line:142
        O0OOOOOO00O00O0O0 .resize (400 ,300 )#line:143
        O0OOOOOO00O00O0O0 .extensions_manager =OOOO0O0O000000O0O #line:144
        O0OOOOOO00O00O0O0 .layout =QVBoxLayout ()#line:145
        O0OOOOOO00O00O0O0 .list_widget =QListWidget ()#line:146
        O0OOOOOO00O00O0O0 .load_installed_extensions ()#line:147
        O0OOOOOO00O00O0O0 .layout .addWidget (O0OOOOOO00O00O0O0 .list_widget )#line:148
        OO00000O0O000OOO0 =QHBoxLayout ()#line:149
        O000O0OOOOOO00OO0 =QPushButton ("Enable/Disable")#line:150
        O000O0OOOOOO00OO0 .clicked .connect (O0OOOOOO00O00O0O0 .toggle_extension )#line:151
        O000O0O0OOO00O0O0 =QPushButton ("Remove")#line:152
        O000O0O0OOO00O0O0 .clicked .connect (O0OOOOOO00O00O0O0 .remove_extension )#line:153
        OO00000O0O000OOO0 .addWidget (O000O0OOOOOO00OO0 )#line:154
        OO00000O0O000OOO0 .addWidget (O000O0O0OOO00O0O0 )#line:155
        O0OOOOOO00O00O0O0 .layout .addLayout (OO00000O0O000OOO0 )#line:156
        O0OOOOOO00O00O0O0 .setLayout (O0OOOOOO00O00O0O0 .layout )#line:157
    def load_installed_extensions (OO00O00O000O0000O ):#line:158
        ""#line:159
        OO00O00O000O0000O .list_widget .clear ()#line:160
        for OO00OO0O00OOO0000 in OO00O00O000O0000O .extensions_manager .get_installed_extensions ():#line:161
            OOO0OOOOOO000O0O0 ="Enabled"if OO00O00O000O0000O .extensions_manager .extensions [OO00OO0O00OOO0000 ]['enabled']else "Disabled"#line:162
            OO00O00O000O0000O .list_widget .addItem (f"{OO00OO0O00OOO0000} ({OOO0OOOOOO000O0O0})")#line:163
    def toggle_extension (O0O0OOOOO0O000O0O ):#line:164
        ""#line:165
        O0O00OO0O00O00O00 =O0O0OOOOO0O000O0O .list_widget .selectedItems ()#line:166
        if O0O00OO0O00O00O00 :#line:167
            O0OOO000OOOOOO0OO =O0O00OO0O00O00O00 [0 ]#line:168
            OOO000OO0OO0000OO =O0OOO000OOOOOO0OO .text ().split (" (")[0 ]#line:169
            O0O0OOOOO0O000O0O .extensions_manager .toggle_extension (OOO000OO0OO0000OO )#line:170
            O0O0OOOOO0O000O0O .load_installed_extensions ()#line:171
    def remove_extension (O0O00OOO00OOO00O0 ):#line:172
        ""#line:173
        O000OOOO000O0OO0O =O0O00OOO00OOO00O0 .list_widget .selectedItems ()#line:174
        if O000OOOO000O0OO0O :#line:175
            O0O000O0O0000OOOO =O000OOOO000O0OO0O [0 ]#line:176
            OO0O00OO00OOOO0OO =O0O000O0O0000OOOO .text ().split (" (")[0 ]#line:177
            O0O00OOO00OOO00O0 .extensions_manager .remove_extension (OO0O00OO00OOOO0OO )#line:178
            O0O00OOO00OOO00O0 .load_installed_extensions ()#line:179
class MainWindow (QMainWindow ):#line:180
    ""#line:181
    def __init__ (OO0OO0000000OO000 ):#line:182
        super ().__init__ ()#line:183
        OO0OO0000000OO000 .setWindowTitle ("GDCE Browser")#line:184
        OO0OO0000000OO000 .resize (1280 ,800 )#line:185
        OO0OO0000000OO000 .appdata_dir =OO0OO0000000OO000 .get_appdata_dir ()#line:186
        OO0OO0000000OO000 .history_file =os .path .join (OO0OO0000000OO000 .appdata_dir ,"history.json")#line:187
        OO0OO0000000OO000 .ensure_history_file ()#line:188
        OO0OO0000000OO000 .homepage ="https://gamedigitalcurrencyexchange.cc"#line:189
        OO0OO0000000OO000 .extensions_manager =ExtensionsManager ()#line:190
        OO0OO0000000OO000 .init_ui ()#line:191
    def get_appdata_dir (O00OOO0000O0OOOOO ):#line:192
        OO0000O00OO00O00O =os .getenv ("APPDATA")if os .name =="nt"else os .path .expanduser ("~")#line:193
        OO0O0OOOO00O00OO0 =os .path .join (OO0000O00OO00O00O ,"GDCEBROWSER")#line:194
        if not os .path .exists (OO0O0OOOO00O00OO0 ):#line:195
            os .makedirs (OO0O0OOOO00O00OO0 )#line:196
        return OO0O0OOOO00O00OO0 #line:197
    def ensure_history_file (OO00OO0O0OOO0000O ):#line:198
        if not os .path .exists (OO00OO0O0OOO0000O .history_file ):#line:199
            with open (OO00OO0O0OOO0000O .history_file ,"w")as O0OOOOOOOOOO0O0O0 :#line:200
                json .dump ([],O0OOOOOOOOOO0O0O0 )#line:201
    def init_ui (O0OOOOOOOOOOO000O ):#line:202
        OOO000O0OO00OOOOO =QVBoxLayout ()#line:203
        OOOOO0000000OO0OO =QHBoxLayout ()#line:204
        OOO00000O0OOOO0OO =QPushButton ("New Tab")#line:205
        OOO00000O0OOOO0OO .clicked .connect (O0OOOOOOOOOOO000O .add_browser_tab )#line:206
        O000OOO0O000OO00O =QPushButton ("History")#line:207
        O000OOO0O000OO00O .clicked .connect (O0OOOOOOOOOOO000O .open_history )#line:208
        O0OOOOO0OO0OOOOO0 =QPushButton ("Extensions")#line:209
        O0OOOOO0OO0OOOOO0 .clicked .connect (O0OOOOOOOOOOO000O .open_extensions_manager )#line:210
        OOOOO0000000OO0OO .addWidget (OOO00000O0OOOO0OO )#line:211
        OOOOO0000000OO0OO .addWidget (O000OOO0O000OO00O )#line:212
        OOOOO0000000OO0OO .addWidget (O0OOOOO0OO0OOOOO0 )#line:213
        OOO000O0OO00OOOOO .addLayout (OOOOO0000000OO0OO )#line:214
        O0OOOOOOOOOOO000O .browser_tabs =QTabWidget ()#line:215
        O0OOOOOOOOOOO000O .browser_tabs .setTabsClosable (True )#line:216
        O0OOOOOOOOOOO000O .browser_tabs .tabCloseRequested .connect (O0OOOOOOOOOOO000O .close_browser_tab )#line:217
        OOO000O0OO00OOOOO .addWidget (O0OOOOOOOOOOO000O .browser_tabs )#line:218
        O0OOO00OO000O0O00 =QWidget ()#line:219
        O0OOO00OO000O0O00 .setLayout (OOO000O0OO00OOOOO )#line:220
        O0OOOOOOOOOOO000O .setCentralWidget (O0OOO00OO000O0O00 )#line:221
        O0OOOOOOOOOOO000O .add_browser_tab ()#line:222
    def add_browser_tab (OOO0O0000000O0000 ):#line:223
        OO0000OO0O0O0OOOO =BrowserTab (OOO0O0000000O0000 .homepage ,OOO0O0000000O0000 .extensions_manager )#line:224
        OOO0OOO00O0OO0OOO =OOO0O0000000O0000 .browser_tabs .addTab (OO0000OO0O0O0OOOO ,"New Tab")#line:225
        OOO0O0000000O0000 .browser_tabs .setCurrentIndex (OOO0OOO00O0OO0OOO )#line:226
    def close_browser_tab (OO0OO0000000OO00O ,OOOO0O0O0OO00OOOO ):#line:227
        if OO0OO0000000OO00O .browser_tabs .count ()>1 :#line:228
            OO0OO0000000OO00O .browser_tabs .removeTab (OOOO0O0O0OO00OOOO )#line:229
    def open_history (O0OO0O00O00O00O00 ):#line:230
        OO0OO0OO0O0O0O00O =HistoryDialog (O0OO0O00O00O00O00 .history_file ,O0OO0O00O00O00O00 )#line:231
        OO0OO0OO0O0O0O00O .exec_ ()#line:232
    def open_extensions_manager (OO0O0OO000OO00O00 ):#line:233
        OO0OOO0OOOOO0O0OO =ExtensionsManagerDialog (OO0O0OO000OO00O00 ,OO0O0OO000OO00O00 .extensions_manager )#line:234
        OO0OOO0OOOOO0O0OO .exec_ ()#line:235
def check_update_status ():#line:236
    pass #line:237
if __name__ =="__main__":#line:238
    app =QApplication (sys .argv )#line:239
    app .setStyleSheet ("""
        QMainWindow { background-color: #1e1e2e; }
        QTabWidget::pane { background: #2a2a3d; }
        QTabBar::tab { background: #3c3c4f; color: #000000; padding: 10px; }
        QTabBar::tab:selected { background: #4e4e6b; color: #000000; }
        QLineEdit { background-color: #ffffff; color: #000000; padding: 8px; border: 1px solid #4e4e6b; border-radius: 4px; }
        QPushButton { background-color: #ff80ab; color: #000000; padding: 8px; border: none; border-radius: 4px; }
        QPushButton:hover { background-color: #ff4081; }
        QCheckBox { color: #000000; }
        QListWidget { background-color: #ffffff; color: #000000; }
        QLabel { color: #ffffff; }
    """)#line:251
    window =MainWindow ()#line:252
    window .show ()#line:253
    sys .exit (app .exec_ ())
