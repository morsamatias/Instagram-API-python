#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("jnqov4", "MjYads9Yd22upWi")
InstagramAPI.login()  # login

photo_path = '0001.jpg'
caption = "#dank #dankmeme #dankest #dankmemesargentina #dankentina"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
