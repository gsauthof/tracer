#-*- coding: utf-8 -*-
# applications.py
# Manager for applications file
#
# Copyright (C) 2014 Jakub Kadlčík
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from bs4 import BeautifulSoup
from os.path import dirname, realpath
parentdir = dirname(dirname(realpath(__file__)))

class Applications:

	DEFINITIONS = parentdir + "/data/applications.xml"

	TYPES = {
		"DAEMON" : "daemon",
		"STATIC" : "static",
	}

	@staticmethod
	def find(app_name):
		f = open(Applications.DEFINITIONS)
		soup = BeautifulSoup(f.read())

		app = soup.find("app", {"name" : app_name})
		if not app:
			return None

		return app.attrs

	@staticmethod
	def all():
		apps = []
		f = open(Applications.DEFINITIONS)
		soup = BeautifulSoup(f.read())

		for app in soup.find_all("app"):
			apps.append(app.attrs)

		f.close();
		return apps
