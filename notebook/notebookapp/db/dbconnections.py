#!/usr/bin/env python3
import sys
import sqlite3
import string

import Note

def getNotes(user):
	dbname = 'notes.sqlite'
	conn = sqlite3.connect(dbname)
	cursor = conn.cursor()
	response = cursor.execute('SELECT * FROM Notes WHERE name = ?', user.name).fetchall()
	
	print('Found entries:')
	for r in response:
		print(r[0])
	
	return response

def getNotes2(user):
	return Note.objects.get(person = user)
