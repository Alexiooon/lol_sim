"""Module containing everything regarding Champions.

A few files in this module start with an underscore, e.g. "_champion.py".
Multiple of these are not considered private, thus breaking a standard
convention in Python. However during development I quite prefer it, as there
are 160+ individual champion files and it becomes rather messy to find the more
generic files. Instead, the __all__ list at the bottom defines what is actually
public, and will be imported when using *.
"""
from ._champion import BaseChampion  # noqa: I001 (unsorted import)
from ._common import CHAMPIONS, CHAMPION_DATA_STR

# Import all champions
from .aatrox import Aatrox
from .ahri import Ahri
from .akali import Akali
from .akshan import Akshan
from .alistar import Alistar
from .amumu import Amumu
from .anivia import Anivia
from .annie import Annie
from .aphelios import Aphelios
from .ashe import Ashe
from .aurelionsol import AurelionSol
from .aurora import Aurora
from .azir import Azir
from .bard import Bard
from .belveth import BelVeth
from .blitzcrank import Blitzcrank
from .brand import Brand
from .braum import Braum
from .briar import Briar
from .caitlyn import Caitlyn
from .camille import Camille
from .cassiopeia import Cassiopeia
from .chogath import ChoGath
from .corki import Corki
from .darius import Darius
from .diana import Diana
from .drmundo import DrMundo
from .draven import Draven
from .ekko import Ekko
from .elise import Elise
from .evelynn import Evelynn
from .ezreal import Ezreal
from .fiddlesticks import Fiddlesticks
from .fiora import Fiora
from .fizz import Fizz
from .galio import Galio
from .gangplank import Gangplank
from .garen import Garen
from .gnar import Gnar
from .gragas import Gragas
from .graves import Graves
from .gwen import Gwen
from .hecarim import Hecarim
from .heimerdinger import Heimerdinger
from .hwei import Hwei
from .illaoi import Illaoi
from .irelia import Irelia
from .ivern import Ivern
from .janna import Janna
from .jarvaniv import JarvanIV
from .jax import Jax
from .jayce import Jayce
from .jhin import Jhin
from .jinx import Jinx
from .ksante import KSante
from .kaisa import KaiSa
from .kalista import Kalista
from .karma import Karma
from .karthus import Karthus
from .kassadin import Kassadin
from .katarina import Katarina
from .kayle import Kayle
from .kayn import Kayn
from .kennen import Kennen
from .khazix import KhaZix
from .kindred import Kindred
from .kled import Kled
from .kogmaw import KogMaw
from .leblanc import LeBlanc
from .leesin import LeeSin
from .leona import Leona
from .lillia import Lillia
from .lissandra import Lissandra
from .lucian import Lucian
from .lulu import Lulu
from .lux import Lux
from .malphite import Malphite
from .malzahar import Malzahar
from .maokai import Maokai
from .masteryi import MasterYi
from .milio import Milio
from .missfortune import MissFortune
from .mordekaiser import Mordekaiser
from .morgana import Morgana
from .naafiri import Naafiri
from .nami import Nami
from .nasus import Nasus
from .nautilus import Nautilus
from .neeko import Neeko
from .nidalee import Nidalee
from .nilah import Nilah
from .nocturne import Nocturne
from .nunu import Nunu
from .olaf import Olaf
from .orianna import Orianna
from .ornn import Ornn
from .pantheon import Pantheon
from .poppy import Poppy
from .pyke import Pyke
from .qiyana import Qiyana
from .quinn import Quinn
from .rakan import Rakan
from .rammus import Rammus
from .reksai import RekSai
from .rell import Rell
from .renataglasc import RenataGlasc
from .renekton import Renekton
from .rengar import Rengar
from .riven import Riven
from .rumble import Rumble
from .ryze import Ryze
from .samira import Samira
from .sejuani import Sejuani
from .senna import Senna
from .seraphine import Seraphine
from .sett import Sett
from .shaco import Shaco
from .shen import Shen
from .shyvana import Shyvana
from .singed import Singed
from .sion import Sion
from .sivir import Sivir
from .skarner import Skarner
from .smolder import Smolder
from .sona import Sona
from .soraka import Soraka
from .swain import Swain
from .sylas import Sylas
from .syndra import Syndra
from .tahmkench import TahmKench
from .taliyah import Taliyah
from .talon import Talon
from .taric import Taric
from .teemo import Teemo
from .thresh import Thresh
from .tristana import Tristana
from .trundle import Trundle
from .tryndamere import Tryndamere
from .twistedfate import TwistedFate
from .twitch import Twitch
from .udyr import Udyr
from .urgot import Urgot
from .varus import Varus
from .vayne import Vayne
from .veigar import Veigar
from .velkoz import VelKoz
from .vex import Vex
from .vi import Vi
from .viego import Viego
from .viktor import Viktor
from .vladimir import Vladimir
from .volibear import Volibear
from .warwick import Warwick
from .wukong import Wukong
from .xayah import Xayah
from .xerath import Xerath
from .xinzhao import XinZhao
from .yasuo import Yasuo
from .yone import Yone
from .yorick import Yorick
from .yuumi import Yuumi
from .zac import Zac
from .zed import Zed
from .zeri import Zeri
from .ziggs import Ziggs
from .zilean import Zilean
from .zoe import Zoe
from .zyra import Zyra

__all__ = [

    "CHAMPIONS",
    "CHAMPION_DATA_STR",

    "Aatrox",
    "Ahri",
    "Akali",
    "Akshan",
    "Alistar",
    "Amumu",
    "Anivia",
    "Annie",
    "Aphelios",
    "Ashe",
    "AurelionSol",
    "Aurora",
    "Azir",
    "Bard",
    "BaseChampion",
    "BelVeth",
    "Blitzcrank",
    "Brand",
    "Braum",
    "Briar",
    "Caitlyn",
    "Camille",
    "Cassiopeia",
    "ChoGath",
    "Corki",
    "Darius",
    "Diana",
    "DrMundo",
    "Draven",
    "Ekko",
    "Elise",
    "Evelynn",
    "Ezreal",
    "Fiddlesticks",
    "Fiora",
    "Fizz",
    "Galio",
    "Gangplank",
    "Garen",
    "Gnar",
    "Gragas",
    "Graves",
    "Gwen",
    "Hecarim",
    "Heimerdinger",
    "Hwei",
    "Illaoi",
    "Irelia",
    "Ivern",
    "Janna",
    "JarvanIV",
    "Jax",
    "Jayce",
    "Jhin",
    "Jinx",
    "KSante",
    "KaiSa",
    "Kalista",
    "Karma",
    "Karthus",
    "Kassadin",
    "Katarina",
    "Kayle",
    "Kayn",
    "Kennen",
    "KhaZix",
    "Kindred",
    "Kled",
    "KogMaw",
    "LeBlanc",
    "LeeSin",
    "Leona",
    "Lillia",
    "Lissandra",
    "Lucian",
    "Lulu",
    "Lux",
    "Malphite",
    "Malzahar",
    "Maokai",
    "MasterYi",
    "Milio",
    "MissFortune",
    "Mordekaiser",
    "Morgana",
    "Naafiri",
    "Nami",
    "Nasus",
    "Nautilus",
    "Neeko",
    "Nidalee",
    "Nilah",
    "Nocturne",
    "Nunu",
    "Olaf",
    "Orianna",
    "Ornn",
    "Pantheon",
    "Poppy",
    "Pyke",
    "Qiyana",
    "Quinn",
    "Rakan",
    "Rammus",
    "RekSai",
    "Rell",
    "RenataGlasc",
    "Renekton",
    "Rengar",
    "Riven",
    "Rumble",
    "Ryze",
    "Samira",
    "Sejuani",
    "Senna",
    "Seraphine",
    "Sett",
    "Shaco",
    "Shen",
    "Shyvana",
    "Singed",
    "Sion",
    "Sivir",
    "Skarner",
    "Smolder",
    "Sona",
    "Soraka",
    "Swain",
    "Sylas",
    "Syndra",
    "TahmKench",
    "Taliyah",
    "Talon",
    "Taric",
    "Teemo",
    "Thresh",
    "Tristana",
    "Trundle",
    "Tryndamere",
    "TwistedFate",
    "Twitch",
    "Udyr",
    "Urgot",
    "Varus",
    "Vayne",
    "Veigar",
    "VelKoz",
    "Vex",
    "Vi",
    "Viego",
    "Viktor",
    "Vladimir",
    "Volibear",
    "Warwick",
    "Wukong",
    "Xayah",
    "Xerath",
    "XinZhao",
    "Yasuo",
    "Yone",
    "Yorick",
    "Yuumi",
    "Zac",
    "Zed",
    "Zeri",
    "Ziggs",
    "Zilean",
    "Zoe",
    "Zyra",
]
