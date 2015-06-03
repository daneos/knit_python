#!/usr/bin/env python

import socket
import re

re_category = r"\b#(.*)\b"
re_preson = r"\b@(.*)\b"

class rest:
	def __init__(self, host, port):
		pass

	def handle_input(self, method, body):
		if method == "PUT":
			pass
		elif method == "GET":
			pass
		else:
			pass

	def insert(self, category, person, s):
		pass

	def get(self, category, person):
		pass

	def run(self):
		pass

#------------------------------------------------------------------------------
if __name__ == "__main__":
	rest("localhost", 8080).run()