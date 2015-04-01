# -*- coding: utf-8 -*-
import os, re, subprocess

'''Sample code shows how to find a line matchs a pattern in a file'''

current_directory = os.path.dirname(os.path.abspath(__file__))
sample_file_path = current_directory + '/../data/regex_sample.sql'
print sample_file_path
lines = open(sample_file_path, "r").readlines()
lines = filter(None, (line.rstrip() for line in lines))

parser = re.compile(r'alter session set current_schema=(.*);')
for line in lines:
    match_object = parser.match(line)
    if match_object:
        print line, match_object.group(1)
        

def getAppName(line):
    parser = re.compile(r'(\W*)Build(\w+)')
    match_object = parser.match(line)
    if match_object:
        print match_object.group(2)

def getSQLFile(line):
    parser = re.compile(r'.*(\W)(\w+\.sql)')
    match_object = parser.match(line)
    if match_object:
        print match_object.group(2)
#    print line.rsplit('/',1)[1]

def validate(line):
    parser = re.compile(r'^[+=].*')
    match_object = parser.match(line)
    if match_object:
        print 'ok'
    else:
        print 'not match'
#print None + 'ok'
#line1 = '/BuildIntelligentForms/templates/SQL/132/IWM_Document_Repository_Update_R13_2_11.sql'
#line2 = '\BuildIntelligentForms\templates\SQL\132\IWM_Document_Repository_Update_R13_2_11.sql'
#line3 = '\BuildIntelligentForms/templates/SQL/132\IWM_Document_Repository_Update_R13_2_11.sql'
#line4 = 'BuildIntelligentForms/templates/SQL/132/IWM_Document_Repository_Update_R13_2_11.sql'
#getAppName(line1)
#getAppName(line2)
#getAppName(line3)
#getAppName(line4)
#
#line5='+asd23.sql'
#line6='kaka.sql'
#validate(line5)
#validate(line6)
#
#parser = re.compile(r'^[+=].*')
#assert not parser.match(line5), 'The items should not start with + or ='
#
#
#getSQLFile(line1)
#getSQLFile(line2)
#getSQLFile(line3)
#getSQLFile(line4) 

def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    pipe = os.popen(cmd + ' 2>&1', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None: sts = 0
    if text[-1:] == '\n': text = text[:-1]
    return sts, text
    
def deleteDir(path):
    """deletes the path entirely"""
    
    cmd = "RMDIR "+ path +" /s /q"
    result = getstatusoutput(cmd)
    if(result[0]!=0):
        raise RuntimeError(result[1])
    
    
def runcmd(cmd):
    process = subprocess.Popen(cmd, shell=True,\
                           stdout=subprocess.PIPE,\
                           stderr=subprocess.PIPE)

    # wait for the process to terminate
    out, err = process.communicate()
    errcode = process.returncode
    print out, err, errcode
    
def is_comments(line):
    """line must be trimmed"""
    parser = re.compile(r'^#.*')
    match_object = parser.match(line)
    return match_object is not None
    
print is_comments('as34=3456#990')
print is_comments(' #as34=3456#990')
print is_comments('###as34=3456#990')

def get_property(line):
    """return key, value pair by splitting key=value with ="""
#    parser = re.compile(r'(.*)=(.*)')
#    match_object = parser.match(line)
#    if match_object:
#        return match_object.group(1),match_object.group(2)
    assert line.find('=') != -1
    line_list = line.split('=', 1)
    return line_list[0], line_list[1]

line1 = 'DMO_INQUIRY_PASSWORD=321oijdsoij23oijlk;jADSFATWWFDasioj32r98pao;kdas;lkjf98ewqp'
line2 = 'BASE_SECURITY_GROUP_SUFFIX=,cn=groups,ou=repsource,o=manulife,c=ca'
print get_property(line1)
print get_property(line2)

def find_all(line):
    parser = re.compile(r'@([\w]+)@')
    iterator = parser.finditer(line)
    return iterator

line1 = '    <parameter name="uid=HeadOffice-MS,cn=role" type="string" update="set"><![CDATA[cn=iwm-ms-adv-relations@BASE_SECURITY_GROUP_SUFFIX@;cn=iwm-ms-call-centre@BASE_SECURITY_GROUP_SUFFIX@;cn=iwm-msil-marketing@BASE_SECURITY_GROUP_SUFFIX@;cn=iwm-msil-operations@BASE_SECURITY_GROUP_SUFFIX@]]></parameter>'
line2 = '<parameter name="uid=HeadOffice-MS,cn=role" type="string" update="set"><![CDATA[cn=iwm-ms-adv-relations@BASE_SECURITY_GROUP_SUFFIX@;'

iter = find_all(line1)
for x in iter:
    print '{} {} {}'.format(x.start(),x.end(), x.group(1))

print line1[103:131]
iter = find_all(line2)
for x in iter:
    print '{} {} {}'.format(x.start(),x.end(), x.group(1))

line3 = line2.replace('@BASE_SECURITY_GROUP_SUFFIX@','XYZ,TTT')
print line2
print line3

import datetime

def check_time_stamp(line):
    parser = re.compile(r'([0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])')
    match_object = parser.match(line)
    return match_object is not None
    
#    try:
#        datetime.datetime.strptime(line, '%Y-%m-%d')
#        return True
#    except ValueError:
#        return False
    
print check_time_stamp('13-2-23')
print check_time_stamp('2013-2-23')
print check_time_stamp('2013-02-23')


for i in [1,2,3,4,5,6,7]:
    print i
    if i == 3:
        break;
#child_path = 'C:\\test\\instantclient-basic-windows.x64-11.2.0.2.0'
#rm_command = 'rmdir ' + child_path + ' /s /q'
#print rm_command
#
#runcmd(rm_command)
##pipe = subprocess.Popen(rm_command, shell=True)
##text = pipe.read()
##sts = pipe.close()
##print sts, text
#print os.path.isdir('c:\\testme'), p


def getBranchName(line):
    parser = re.compile(r'(\w*)P7(\w+)')
    match_object = parser.match(line)
    if match_object:
        print type(match_object.group(1))
        
getBranchName('Common_P7_13-2-2')
getBranchName('IntelligentForms_P7_13-2-2')