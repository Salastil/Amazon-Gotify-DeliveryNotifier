#!/bin/bash
srcdir=$PWD
install -dm755 ${pkgdir}/usr/bin
install -dm755 ${pkgdir}/usr/lib
cp -a ${srcdir} ${pkgdir}/usr/lib/amazongotifynotifier
ln -s /usr/lib/amazongotifynotifier/amazongotifynotifier.py ${pkgdir}/usr/bin/amazongotifynotifier.py
