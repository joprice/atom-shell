#!/usr/bin/env python

import platform
import sys

BASE_URL = 'http://gh-contractor-zcbenz.s3.amazonaws.com/libchromiumcontent'
LIBCHROMIUMCONTENT_COMMIT = 'f1ad1412461ba3345a27cfe935ffc872dba0ac5b'

ARCH = {
    'cygwin': '32bit',
    'darwin': '64bit',
    'linux2': platform.architecture()[0],
    'win32': '32bit',
}[sys.platform]
DIST_ARCH = {
    '32bit': 'ia32',
    '64bit': 'x64',
}[ARCH]

TARGET_PLATFORM = {
  'cygwin': 'win32',
  'darwin': 'darwin',
  'linux2': 'linux',
  'win32': 'win32',
}[sys.platform]

verbose_mode = False

def enable_verbose_mode():
  print 'Running in verbose mode'
  global verbose_mode
  verbose_mode = True

def is_verbose_mode():
  return verbose_mode
