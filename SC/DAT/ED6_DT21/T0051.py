import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0051_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0051   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0030.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10620._CH', 'ED6_DT09/CH10620P._CP'),
        ('ED6_DT09/CH10621._CH', 'ED6_DT09/CH10621P._CP'),
        ('ED6_DT09/CH10622._CH', 'ED6_DT09/CH10622P._CP'),
        ('ED6_DT09/CH10623._CH', 'ED6_DT09/CH10623P._CP'),
        ('ED6_DT09/CH10624._CH', 'ED6_DT09/CH10624P._CP'),
        ('ED6_DT09/CH10630._CH', 'ED6_DT09/CH10630P._CP'),
        ('ED6_DT09/CH10631._CH', 'ED6_DT09/CH10631P._CP'),
        ('ED6_DT09/CH10632._CH', 'ED6_DT09/CH10632P._CP'),
        ('ED6_DT09/CH10633._CH', 'ED6_DT09/CH10633P._CP'),
        ('ED6_DT09/CH10634._CH', 'ED6_DT09/CH10634P._CP'),
        ('ED6_DT09/CH10640._CH', 'ED6_DT09/CH10640P._CP'),
        ('ED6_DT09/CH10641._CH', 'ED6_DT09/CH10641P._CP'),
        ('ED6_DT09/CH10642._CH', 'ED6_DT09/CH10642P._CP'),
        ('ED6_DT09/CH10643._CH', 'ED6_DT09/CH10643P._CP'),
        ('ED6_DT09/CH10644._CH', 'ED6_DT09/CH10644P._CP'),
        ('ED6_DT09/CH10650._CH', 'ED6_DT09/CH10650P._CP'),
        ('ED6_DT09/CH10651._CH', 'ED6_DT09/CH10651P._CP'),
        ('ED6_DT09/CH10652._CH', 'ED6_DT09/CH10652P._CP'),
        ('ED6_DT09/CH10653._CH', 'ED6_DT09/CH10653P._CP'),
        ('ED6_DT09/CH10654._CH', 'ED6_DT09/CH10654P._CP'),
        ('ED6_DT09/CH10660._CH', 'ED6_DT09/CH10660P._CP'),
        ('ED6_DT09/CH10661._CH', 'ED6_DT09/CH10661P._CP'),
        ('ED6_DT09/CH10662._CH', 'ED6_DT09/CH10662P._CP'),
        ('ED6_DT09/CH10663._CH', 'ED6_DT09/CH10663P._CP'),
        ('ED6_DT09/CH10664._CH', 'ED6_DT09/CH10664P._CP'),
        ('ED6_DT09/CH10670._CH', 'ED6_DT09/CH10670P._CP'),
        ('ED6_DT09/CH10671._CH', 'ED6_DT09/CH10671P._CP'),
        ('ED6_DT09/CH10672._CH', 'ED6_DT09/CH10672P._CP'),
        ('ED6_DT09/CH10673._CH', 'ED6_DT09/CH10673P._CP'),
        ('ED6_DT09/CH10674._CH', 'ED6_DT09/CH10674P._CP'),
        ('ED6_DT09/CH10680._CH', 'ED6_DT09/CH10680P._CP'),
        ('ED6_DT09/CH10681._CH', 'ED6_DT09/CH10681P._CP'),
        ('ED6_DT09/CH10682._CH', 'ED6_DT09/CH10682P._CP'),
        ('ED6_DT09/CH10683._CH', 'ED6_DT09/CH10683P._CP'),
        ('ED6_DT09/CH10684._CH', 'ED6_DT09/CH10684P._CP'),
        ('ED6_DT09/CH10690._CH', 'ED6_DT09/CH10690P._CP'),
        ('ED6_DT09/CH10691._CH', 'ED6_DT09/CH10691P._CP'),
        ('ED6_DT09/CH10692._CH', 'ED6_DT09/CH10692P._CP'),
        ('ED6_DT09/CH10693._CH', 'ED6_DT09/CH10693P._CP'),
        ('ED6_DT09/CH10694._CH', 'ED6_DT09/CH10694P._CP'),
    ]

# id: 0x10001 offset: 0x1EA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '10620待机',
            x                   = 4000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10621移动',
            x                   = 4000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10622攻击',
            x                   = 4000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10623被弹开',
            x                   = 4000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10624倒下',
            x                   = 4000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10630待机',
            x                   = 8000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10631移动',
            x                   = 8000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10632攻击',
            x                   = 8000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10633被弹开',
            x                   = 8000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10634倒下',
            x                   = 8000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10640待机',
            x                   = 12000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10641移动',
            x                   = 12000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10642攻击',
            x                   = 12000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10643被弹开',
            x                   = 12000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10644倒下',
            x                   = 12000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10650待机',
            x                   = 16000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10651移动',
            x                   = 16000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10652攻击',
            x                   = 16000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10653被弹开',
            x                   = 16000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10654倒下',
            x                   = 16000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10660待机',
            x                   = 20000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10661移动',
            x                   = 20000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10662攻击',
            x                   = 20000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10663被弹开',
            x                   = 20000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10664倒下',
            x                   = 20000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10670待机',
            x                   = 24000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10671移动',
            x                   = 24000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10672攻击',
            x                   = 24000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10673被弹开',
            x                   = 24000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10674倒下',
            x                   = 24000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10680待机',
            x                   = 28000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10681移动',
            x                   = 28000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10682攻击',
            x                   = 28000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10683被弹开',
            x                   = 28000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10684倒下',
            x                   = 28000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10690移动',
            x                   = 32000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10691待机',
            x                   = 32000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10692攻击',
            x                   = 32000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10693被弹开',
            x                   = 32000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '10694倒下',
            x                   = 32000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x6EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x6EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x6EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x6EA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x6EB
@scena.Code('func_01_6EB')
def func_01_6EB():
    Return()

# id: 0x0002 offset: 0x6EC
@scena.Code('func_02_6EC')
def func_02_6EC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_701',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_6EC')

    def _loc_701(): pass

    label('loc_701')

    Return()

# id: 0x0003 offset: 0x702
@scena.Code('func_03_702')
def func_03_702():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_717',
    )

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('func_03_702')

    def _loc_717(): pass

    label('loc_717')

    Return()

# id: 0x0004 offset: 0x718
@scena.Code('func_04_718')
def func_04_718():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_73B',
    )

    OP_8D(0x00FE, 4000, 20000, 24000, 30000, 1500)

    Jump('func_04_718')

    def _loc_73B(): pass

    label('loc_73B')

    Return()

# id: 0x0005 offset: 0x73C
@scena.Code('func_05_73C')
def func_05_73C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗷—',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
