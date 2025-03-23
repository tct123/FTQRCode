import os
from mylocale import tr
from flet_localisation import locale
import flet as ft

trfile = f"{os.path.dirname(__file__)}/localisation.csv"


def SCANMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="SCAN",
        langcode=langcode,
    )


def GENERATEBTNMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="GENERATEBTN",
        langcode=langcode,
    )


def GENERATETABMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="GENERATETAB",
        langcode=langcode,
    )
def VALUEMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="VALUE",
        langcode=langcode,
    )
def COMMUTEMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    return tr(
        csv_file=trfile,
        target_key="COMMUTE",
        langcode=langcode,
    )