#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from codecs import open
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
