#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 29 Nov 2023 03:49:53 PM CET
# privkit.py
# Description:

from havoc import Demon, RegisterCommand, RegisterModule
import os

def alwaysinstallelevated( demonID, *param ):
    TaskID : str = None
    demon : Demon = None

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to check if programs are always installed as elevated" )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/alwaysinstallelevated.o", b'', False)

    return TaskID

def autologon( demonID, *param ):
    TaskID : str = None
    demon : Demon = None

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to check for autologon registry keys" )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/autologon.o", b'', False)

    return TaskID

def credentialmanager( demonID, *param ):
    TaskID : str = None
    demon : Demon = None

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to enumerate credential manager" )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/credentialmanager.o", b'', False)

    return TaskID

def hijackablepath( demonID, *param ):
    TaskID : str = None
    demon : Demon = None

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to find hijackable paths" )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/hijackablepath.o", b'', False)

    return TaskID

def modifiableautorun( demonID, *param ):
    TaskID : str = None
    demon : Demon = None

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to find modifiable autoruns" )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/modifiableautorun.o", b'', False)

    return TaskID

def tokenprivileges( demonID, *param ):
    TaskID : str = None
    demon : Demon = None

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to check for token privileges" )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/tokenprivileges.o", b'', False)

    return TaskID

def unquotedsvcpath( demonID, *param ):
    TaskID : str = None
    demon : Demon = None

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to look for unquoted service paths" )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/unquotedsvcpath.o", b'', False)

    return TaskID

def all( demonID, *param ):
    TaskID : str = None
    demon : Demon = None
    demon = Demon(demonID)

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Running all of the privkit checks..." )
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/alwaysinstallelevated.o", b'', False)
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/autologon.o", b'', False)
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/credentialmanager.o", b'', False)
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/hijackablepath.o", b'', False)
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/modifiableautorun.o", b'', False)
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/tokenprivileges.o", b'', False)
    demon.InlineExecute(TaskID, "go", "PrivKit/PrivKit/unquotedsvcpath.o", b'', False)

    return TaskID

RegisterModule( "privkit", "Privilege Escalation Module", "", "", "", ""  )
RegisterCommand( all, "privkit", "all", "Run all possible checks.", 0, "", "" )
RegisterCommand( alwaysinstallelevated, "privkit", "elevated", "Check if programs are always installed as elevated.", 0, "", "" )
RegisterCommand( autologon, "privkit", "autologon", "Check for autologon registry keys.", 0, "", "" )
RegisterCommand( credentialmanager, "privkit", "credman", "Enumerate credential manager.", 0, "", "" )
RegisterCommand( hijackablepath, "privkit", "paths", "Enumerate hijackable paths.", 0, "", "" )
RegisterCommand( modifiableautorun, "privkit", "autorun", "Find modifiable autoruns.", 0, "", "" )
RegisterCommand( tokenprivileges, "privkit", "token", "Check for token privileges.", 0, "", "" )
RegisterCommand( unquotedsvcpath, "privkit", "unquoted", "Check unquoted service paths.", 0, "", "" )
