import easygui
import json
from threading import Thread
import flask
from envs import Envs
import sys
import os
import builtins as bi
import random
import platform


# Made for Linux, I need a Linux server
r = r"""
  ___   __  __ _          
 / _ \ / _|/ _(_) ___ ___ 
| | | | |_| |_| |/ __/ _ \
| |_| |  _|  _| | (_|  __/
 \___/|_| |_| |_|\___\___|
                          
 __  __                                                   _   
|  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
| |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                          |___/                               
 ____            _                         _   ___  
/ ___| _   _ ___| |_ ___ _ __ ___   __   _/ | / _ \ 
\___ \| | | / __| __/ _ \ '_ ` _ \  \ \ / / || | | |
 ___) | |_| \__ \ ||  __/ | | | | |  \ V /| || |_| |
|____/ \__, |___/\__\___|_| |_| |_|   \_/ |_(_)___/ 
       |___/                                        
"""


os3 = platform.system()
LOW = 0
REGULAR = 1
HIGH = 2
ROOT = 3
SHUTUP = []
env = Envs('hello', 'hi', kwarg='hello')
used_codes_file = open('used_codes.txt', 'a')
used_codes_file_read = open('used_codes.txt')
used_codes = list(used_codes_file_read.readlines())
if used_codes == []:
    print('No codes')
else:
    print('some codes')
used_codes_file_read.close()
try:
    log = open('WebServer_Logs.log', 'x')
except FileExistsError:
    os.remove('WebServer_Logs.log')
    log = open('WebServer_Logs.log', 'x')
log.write('Opened log file\n')
temp_list = []
temp_list_2 = []
log.write('Creating Flask app with __name__\n')
app = flask.Flask(__name__)


class CustomErrors(Exception):
    def __init__(self, *args, purpose):
        super().__init__(*args)
        self.ErrorPurpose = purpose


CanceledError = CustomErrors(purpose='Raised if a step is canceled')
log.write('Creating OfficeManagementSystem class\n')
v = ''
def generatecode():
    for i in range(30):
        code = random.randint(1, 19)
        v = str(code)
        temp_list_2.append(v)
        temp_list.append(code)
    code = ""
    for i in range(30):
        f = temp_list_2[i]
        code += f
    used_codes_file.write(str(code))
    used_codes_file.write('\n')
    return code
code = generatecode()
class OfficeManagementSystem:

    def __init__(self, *args, **kwargs):
        self.code = code
        self.banner = r
        self.creds = env.creds
        self.logonfieldnames = ['Username', 'Password']
        self.requiredfield = ""
        self.username = ''
        self.values = []
        VALUES = []
        self.creds3 = ['regularuser', 'hello']
        self.settings = json.loads(open('settings.json').read())

    def showbanner(self):
        easygui.msgbox(
            msg=self.banner,
            title='Office Program v1.0')


    def changetoPROD(self):
        if os3 == 'Linux':
            os.system("export FLASK_ENV=development")
        elif 
    def logon(self):
        global values3
        while 1:

            values3 = []
            self.creds3 = easygui.multpasswordbox(
                msg='Enter your credentials',
                title='Login',
                fields=self.logonfieldnames,
                values=values3
            )
            # print(values3)
            errmsg = ""
            self.uname = self.creds3[0]

            for i in range(len(self.logonfieldnames)):
                if self.logonfieldnames[i].strip() is None:
                    errmsg = errmsg + ('"%s" is a required field.\n\n' % self.logonfieldnames[i])
                    self.requiredfield = self.logonfieldnames[i]
            if errmsg == "":
                print('Fields: all done')
                log.write('Logged in\n')
                break

    def loggedon(self):
        password3 = self.creds[self.uname]['password']
        self.privs3 = self.creds[self.uname]['privs']
        if self.creds3[0] == password3:
            if self.privs3 == 0:
                self.privs2 = 'low'
            elif self.privs3 == 1:
                self.privs2 = 'root'
            elif self.privs == 2:
                self.privs2 = 'regular'
            else:
                self.privs2 = 'high'
        easygui.msgbox(
            msg='0 privs: low    1 privs: regular\n2 privs: high    3 privs: root'
        )
        easygui.msgbox(
            msg=f'Logged in as {self.uname} with {self.privs3} privileges',
            title=f'Welcome, {self.uname}.'
        )
        # TODO: move to a custom domain
        easygui.msgbox(
            msg=f'Go to your dashboard at http://127.0.0.1/dashboard/{self.uname}/{password3}/{self.code}.',
            title='Go to the dashboard to manage the stuff! (will be changed to nckb.com in the future)',
            ok_button='Start Flask WebServer'
            )

    @staticmethod
    def startws():
        app.run(port=80, debug=True, mode='produ')
        log.write('Started web server')


@app.route('/dashboard/<string:username>/<string:password>/<int:code3>')
def logon(username, password, code3):
    #global username9
    if code3 == code:
        return flask.render_template('wrongcode.html')
    else:
        return flask.render_template('index.html')
    if username == 'style.css' or username == 'index.html' or username == 'licence.html' or \
            username == 'manager.html' or username == 'people.html':
        print('Loaded a page')
    else:
        print(f'{username} just entered the site')


@app.route('/dashboard/<string:username>/manager')
def manager(username):
    print(f'{username} is on the Manager page')
    return flask.render_template('manager.html')


@app.route('/dashboard/<string:username>/people')
def people(username):
    print(f'{username} just went to the People tab')
    return flask.render_template('people.html')

@app.route('/dashboard/<string:username>/404')
def _404error(username):
    print('404 error')
    return flask.render_template('404.html')


@app.route('/licence')
def licence():
    return flask.render_template('licence.html')


def start():
    o = OfficeManagementSystem()
    o.showbanner()
    o.logon()
    o.loggedon()
    o.startws()
    y = generatecode()
    #print(y)
    #print(used_codes)


def main():
    print('Started script!!')
    start()

if __name__ == "__main__":
    main()
