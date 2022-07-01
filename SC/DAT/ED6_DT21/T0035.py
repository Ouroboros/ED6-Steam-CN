import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0035_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0035   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '00400女游击士待机'),
    TXT(0x02, '00401女游击士移动'),
    TXT(0x03, '00402女游击士攻击'),
    TXT(0x04, '00403女游击士被弹开'),
    TXT(0x05, '00404女游击士倒下'),
    TXT(0x06, '00407女游击士魔法咏唱'),
    TXT(0x07, '00408女游击士魔法发射'),
    TXT(0x08, '00390男游击士待机'),
    TXT(0x09, '00391男游击士移动'),
    TXT(0x0A, '00392男游击士攻击'),
    TXT(0x0B, '00393男游击士被弹开'),
    TXT(0x0C, '00394男游击士倒下'),
    TXT(0x0D, '00395男游击士魔法咏唱'),
    TXT(0x0E, '00396男游击士魔法发射'),
    TXT(0x0F, '00370小流氓待机'),
    TXT(0x10, '00371小流氓移动'),
    TXT(0x11, '00372小流氓攻击'),
    TXT(0x12, '00373小流氓被弹开'),
    TXT(0x13, '00374小流氓倒下'),
    TXT(0x14, '00360空贼手下待机'),
    TXT(0x15, '00361空贼手下移动'),
    TXT(0x16, '00362空贼手下攻击'),
    TXT(0x17, '00363空贼手下被弹开'),
    TXT(0x18, '00364空贼手下倒下'),
    TXT(0x19, '00310乔丝特待机'),
    TXT(0x1A, '00311乔丝特移动'),
    TXT(0x1B, '00312乔丝特攻击'),
    TXT(0x1C, '00313乔丝特被弹开'),
    TXT(0x1D, '00314乔丝特倒下'),
    TXT(0x1E, '00315乔丝特魔法咏唱'),
    TXT(0x1F, '00316乔丝特魔法发射'),
    TXT(0x20, '00300吉尔待机'),
    TXT(0x21, '00301吉尔移动'),
    TXT(0x22, '00302吉尔攻击'),
    TXT(0x23, '00303吉尔被弹开'),
    TXT(0x24, '00304吉尔倒下'),
    TXT(0x25, '00305吉尔魔法咏唱'),
    TXT(0x26, '00306吉尔魔法发射'),
    TXT(0x27, '00290多伦待机'),
    TXT(0x28, '00291多伦移动'),
    TXT(0x29, '00292多伦攻击'),
    TXT(0x2A, '00293多伦被弹开'),
    TXT(0x2B, '00294多伦倒下'),
    TXT(0x2C, ''),
]

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

# id: 0xFFFF offset: 0x96E
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00400._CH', 'ED6_DT07/CH00400P._CP'),
        ('ED6_DT07/CH00401._CH', 'ED6_DT07/CH00401P._CP'),
        ('ED6_DT07/CH00402._CH', 'ED6_DT07/CH00402P._CP'),
        ('ED6_DT07/CH00403._CH', 'ED6_DT07/CH00403P._CP'),
        ('ED6_DT07/CH00404._CH', 'ED6_DT07/CH00404P._CP'),
        ('ED6_DT07/CH00405._CH', 'ED6_DT07/CH00405P._CP'),
        ('ED6_DT07/CH00406._CH', 'ED6_DT07/CH00406P._CP'),
        ('ED6_DT07/CH00300._CH', 'ED6_DT07/CH00300P._CP'),
        ('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP'),
        ('ED6_DT07/CH00302._CH', 'ED6_DT07/CH00302P._CP'),
        ('ED6_DT07/CH00303._CH', 'ED6_DT07/CH00303P._CP'),
        ('ED6_DT07/CH00304._CH', 'ED6_DT07/CH00304P._CP'),
        ('ED6_DT07/CH00305._CH', 'ED6_DT07/CH00305P._CP'),
        ('ED6_DT07/CH00306._CH', 'ED6_DT07/CH00306P._CP'),
        ('ED6_DT07/CH00390._CH', 'ED6_DT07/CH00390P._CP'),
        ('ED6_DT07/CH00391._CH', 'ED6_DT07/CH00391P._CP'),
        ('ED6_DT07/CH00392._CH', 'ED6_DT07/CH00392P._CP'),
        ('ED6_DT07/CH00393._CH', 'ED6_DT07/CH00393P._CP'),
        ('ED6_DT07/CH00394._CH', 'ED6_DT07/CH00394P._CP'),
        ('ED6_DT07/CH00395._CH', 'ED6_DT07/CH00395P._CP'),
        ('ED6_DT07/CH00396._CH', 'ED6_DT07/CH00396P._CP'),
        ('ED6_DT07/CH00360._CH', 'ED6_DT07/CH00360P._CP'),
        ('ED6_DT07/CH00361._CH', 'ED6_DT07/CH00361P._CP'),
        ('ED6_DT07/CH00362._CH', 'ED6_DT07/CH00362P._CP'),
        ('ED6_DT07/CH00363._CH', 'ED6_DT07/CH00363P._CP'),
        ('ED6_DT07/CH00364._CH', 'ED6_DT07/CH00364P._CP'),
        ('ED6_DT07/CH00370._CH', 'ED6_DT07/CH00370P._CP'),
        ('ED6_DT07/CH00371._CH', 'ED6_DT07/CH00371P._CP'),
        ('ED6_DT07/CH00372._CH', 'ED6_DT07/CH00372P._CP'),
        ('ED6_DT07/CH00373._CH', 'ED6_DT07/CH00373P._CP'),
        ('ED6_DT07/CH00374._CH', 'ED6_DT07/CH00374P._CP'),
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
        ('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP'),
        ('ED6_DT07/CH00312._CH', 'ED6_DT07/CH00312P._CP'),
        ('ED6_DT07/CH00313._CH', 'ED6_DT07/CH00313P._CP'),
        ('ED6_DT07/CH00314._CH', 'ED6_DT07/CH00314P._CP'),
        ('ED6_DT07/CH00315._CH', 'ED6_DT07/CH00315P._CP'),
        ('ED6_DT07/CH00316._CH', 'ED6_DT07/CH00316P._CP'),
        ('ED6_DT07/CH00290._CH', 'ED6_DT07/CH00290P._CP'),
        ('ED6_DT07/CH00291._CH', 'ED6_DT07/CH00291P._CP'),
        ('ED6_DT07/CH00292._CH', 'ED6_DT07/CH00292P._CP'),
        ('ED6_DT07/CH00293._CH', 'ED6_DT07/CH00293P._CP'),
        ('ED6_DT07/CH00294._CH', 'ED6_DT07/CH00294P._CP'),
    ]

# id: 0x10002 offset: 0x202
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
    )

# id: 0x10003 offset: 0x762
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x762
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x762
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x762
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x763
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x764
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_779',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000009C4)

    Jump('ReInit')

    def _loc_779(): pass

    label('loc_779')

    Return()

# id: 0x0003 offset: 0x77A
@scena.Code('func_03_77A')
def func_03_77A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_78F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

    Jump('func_03_77A')

    def _loc_78F(): pass

    label('loc_78F')

    Return()

# id: 0x0004 offset: 0x790
@scena.Code('func_04_790')
def func_04_790():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7AA',
    )

    OP_99(0x00FE, 0x00, 0x00, 0x000005DC)
    Sleep(500)

    Jump('func_04_790')

    def _loc_7AA(): pass

    label('loc_7AA')

    Return()

# id: 0x0005 offset: 0x7AB
@scena.Code('func_05_7AB')
def func_05_7AB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7C5',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    Sleep(500)

    Jump('func_05_7AB')

    def _loc_7C5(): pass

    label('loc_7C5')

    Return()

# id: 0x0006 offset: 0x7C6
@scena.Code('func_06_7C6')
def func_06_7C6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7E0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000003E8)
    Sleep(500)

    Jump('func_06_7C6')

    def _loc_7E0(): pass

    label('loc_7E0')

    Return()

# id: 0x0007 offset: 0x7E1
@scena.Code('func_07_7E1')
def func_07_7E1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_804',
    )

    OP_8D(0x00FE, 4000, 20000, 24000, 28000, 1500)

    Jump('func_07_7E1')

    def _loc_804(): pass

    label('loc_804')

    Return()

# id: 0x0008 offset: 0x805
@scena.Code('func_08_805')
def func_08_805():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_81A',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_08_805')

    def _loc_81A(): pass

    label('loc_81A')

    Return()

# id: 0x0009 offset: 0x81B
@scena.Code('func_09_81B')
def func_09_81B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_851',
    )

    SetChrChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_09_81B')

    def _loc_851(): pass

    label('loc_851')

    Return()

# id: 0x000A offset: 0x852
@scena.Code('func_0A_852')
def func_0A_852():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_867',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_0A_852')

    def _loc_867(): pass

    label('loc_867')

    Return()

# id: 0x000B offset: 0x868
@scena.Code('func_0B_868')
def func_0B_868():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_89E',
    )

    SetChrChipByIndex(0x00FE, 12)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 13)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_0B_868')

    def _loc_89E(): pass

    label('loc_89E')

    Return()

# id: 0x000C offset: 0x89F
@scena.Code('func_0C_89F')
def func_0C_89F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8B4',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_0C_89F')

    def _loc_8B4(): pass

    label('loc_8B4')

    Return()

# id: 0x000D offset: 0x8B5
@scena.Code('func_0D_8B5')
def func_0D_8B5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8EB',
    )

    SetChrChipByIndex(0x00FE, 19)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 20)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_0D_8B5')

    def _loc_8EB(): pass

    label('loc_8EB')

    Return()

# id: 0x000E offset: 0x8EC
@scena.Code('func_0E_8EC')
def func_0E_8EC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_901',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_0E_8EC')

    def _loc_901(): pass

    label('loc_901')

    Return()

# id: 0x000F offset: 0x902
@scena.Code('func_0F_902')
def func_0F_902():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_938',
    )

    SetChrChipByIndex(0x00FE, 36)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 37)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_0F_902')

    def _loc_938(): pass

    label('loc_938')

    Return()

# id: 0x0010 offset: 0x939
@scena.Code('func_10_939')
def func_10_939():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呜喵。',
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
