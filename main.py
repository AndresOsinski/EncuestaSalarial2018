import csv
import numpy as np

relevant_columns = [0, 1, 3, 5, 7, 8]
data = []
header = None

def developerish(title):
    return title in (
        'Analista programador',
        'Analista/Programador',
        'Analista programador ETL',
        'Analista Programador SQL',
        'DBA, Developer, Help Desk, Networking, Storage / Backup, SysAdmin',
        'Developer',
        'Developer, analista, consultor',
        'Developer,  Analista, Recruiter ',
        'developer,database,networking',
        'Developer, Designer, Architect, Tester, SysAdmin, HelpDesk',
        'Developer / SysAdmin / DevOps',
        'Development lead, DevOp',
        'Especialista de Software (Mix de Developer, DBA, SysAdmin)',
        'Front end',
        'Full Stack',
        'Fullstack Dev',
        'Full-Stack Developer',
        'Ingenieria',
        'ingeniero',
        'Lead Developer',
        'ML Engineer',
        'Networking, SysAdmin, HelpDesk, Storage, Developer, Designer',
        'PROGRAMADOR PLC/SCADA/HMI',
        'Programmer / DevOps',
        'Swift',
        'Team Lead',
        'Team leader',
        'Team Leader',
        'Team Leader - Complex',
        'Todas las opciones anteriores',
    )

def is_tec(tecs, in_tecs):
    for tec in tecs:
        if tec in in_tecs:
            return True
    return False

def is_web(tecs):
    return is_tec(tecs, (x.strip() for x in '''
angular
angular 1 y 2
angular 2
angular 5
angular 5.0
angular 5. sass. typescript
angular en menor medida
angular ionic android studio
angularjs
angular reactjs
bootstrap
coffeescript
frameworks de javascript (react
html
javascript
jquery
knockout
less
nativescript
react
reactjs
react js
react.js
redux
redux saga
redux-saga
riot.js
rxjs
sas
sass
typescript
vue
vue)
vue 2
    '''.split('\n')))

def is_mobile(tecs):
    return is_tec(tecs, (x.strip() for x in '''
android
cordova
ionic
kotlin
objective-c
phonegap/cordova
react native
swift
    '''.split('\n')))

def is_back(tec):
    return is_tec(tecs, (x.strip() for x in '''
4gl
abap
actionscript
adf angular pl sql
algo de cobol
ansible
apex
as400 / rpg400
asp
asp.net
assembler
aws
bash
bi
bi (el universo de herramientas)
bpm oracle
c
c#
c++
clarion
cobol
cobol85
cobol - as400
crystal
css
delphi
django
docker
drupal
elasticsearch
elixir
erlang
esb
esb ibm (toolkit
ethereum virtual machine
etl
foxpro
gdscript
genexus
go
golang
gosu
grails
grails/groovy angular
groovy
guidewire
hibernate - sql
hp non stop
informix sql
integracion de datos
java
jdedwards
jsp
k8s
laravel
lua
magento
magento 2
meta4
microstrategy
mongodb
mssql
mysql
.net
nodejs
octopus deploy tool
oracle
oracle forms
oracle plsql
oracle pl-sql
oracle sql
osb
peoplecode
peoplenet
perl
php
plsql
pl sql
pl-sql
pl/sql
postgres
postgresql
power builder
powercenter
powershell
progress
python
qt
r
rocket universe u2
ruby
ruby on rails
rust
saleforce
salesforce
scala
shell
shellscript
siebel
sitecore
smalltalk
soa
softlayer
solidity
sql
sql server
symfony
tal
tomcat
tsql
twig
unix
vb *
vba
vfp
visual foxpro
visual fox pro
visual fox+sql
windows
wordpress
x++
xamarin
xml
    '''.split('\n')))

with open('argentina-2018.1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if header is None:
            header = row
            print(dict((x, y) for (x, y) in enumerate(header)))
        else:
            if not developerish(row[11]):
                continue
            sex = {
                'Hombre': 0,
                'Mujer': 1,
            }.get(row[0], None)
            age = {
                '18 - 20': 19,
                '21 - 23': 22,
                '24 - 26': 25,
                '27 - 30': 28.5,
                '31 - 33': 32,
                '34 - 36': 35.5,
                '37 - 40': 38.5,
                '41 - 45': 43,
                '46 - 49': 47.5,
                '50+': 65,
                'Menos de 18 años': 17,
            }.get(row[1], None)
            experience = {
                '1': 1,
                '10+': 15,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                'Menos de un año': 0,
            }.get(row[3], None)
            managing = {
                'No': 0,
                'Sí': 1,
            }.get(row[5], None)
            degree = {
                'Primario Completado': 1,
                'Primario En curso': 0.5,
                'Primario Incompleto': 0.5,
                'Secundario Completado': 2,
                'Secundario En curso': 1.5,
                'Secundario Incompleto': 1.5,
                'Terciario Completado': 3,
                'Terciario En curso': 2.5,
                'Terciario Incompleto': 2.5,
                'Universitario Completado': 4,
                'Universitario En curso': 3.5,
                'Universitario Incompleto': 3.5,
                'Posgrado Completado': 5,
                'Posgrado En curso': 4.5,
                'Posgrado Incompleto': 4.5,
                'Doctorado Completado': 6,
                'Doctorado En curso': 5.5,
                'Doctorado Incompleto': 5.5,
            }.get('{} {}'.format(row[7], row[8]))
            tecs = [x.strip().lower() for x in row[13].split(',')]
            for t in tecs:
                print(t)
            web = is_web(tecs)
            back = is_back(tecs)
            mobile = is_mobile(tecs)
            rowdata = (sex, age, experience, managing, degree, web, back)
            if None in rowdata:
                continue
            data.append(rowdata)
            # break

# print(data)

#x = np.asarray([[1,3,6,1,4,6,8,9,2,2],
#                [2,7,6,1,5,6,3,9,5,7],
#                [1,3,4,7,4,8,5,1,8,2],
#                [1,1,1,1,1,1,1,1,1,1]]).T
#y = np.asarray([1,2,3,4,5,6,7,8,9,10]).T
#
#a,b,c,d = np.linalg.pinv((x.T).dot(x)).dot(x.T.dot(y))
#print(a,b,c,d)
