# -*- coding: utf-8 -*-
"""
Launch all UIs for game session.

@author: phill
"""

import subprocess

subprocess.Popen('python region_ui.py --region empire')
subprocess.Popen('python region_ui.py --region redbank')
subprocess.Popen('python region_ui.py --region settled')

subprocess.Popen('python character_ui.py --c1 Keel --c2 Fuscus')
subprocess.Popen('python character_ui.py --c1 Menas --c2 Thea')