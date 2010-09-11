# -*- coding: utf-8 -*-

# WebPyMail - IMAP python/django web mail client
# Copyright (C) 2008 Helder Guerreiro

## This file is part of WebPyMail.
##
## WebPyMail is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## WebPyMail is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with WebPyMail.  If not, see <http://www.gnu.org/licenses/>.

#
# Helder Guerreiro <helder@paxjulia.com>
#
# $Id$
#

"""Base URL definitions
"""

# Global imports:
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Root:
    (r'^$','webpymail.mailapp.views.message.index'),

    # Mail Interface:
    (r'^mail/', include('webpymail.mailapp.urls')),

    # Authentication interface:
    (r'^auth/', include('webpymail.wpmauth.urls')),

    # Admin Interface:
    (r'^admin/(.*)', admin.site.root),

    # Generic:
    url(r'^not_implemented/$', 'webpymail.mailapp.views.message.not_implemented',
        name='not_implemented'),
)

urlpatterns += patterns('',
    # DEVELOPMENT
    # The site wide media folder:
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': 'media/'}),
)