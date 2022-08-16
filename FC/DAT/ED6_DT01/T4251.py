import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4251_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4251   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4251.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
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
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02353._CH', 'ED6_DT07/CH02353P._CP'),
        ('ED6_DT07/CH02603._CH', 'ED6_DT07/CH02603P._CP'),
        ('ED6_DT07/CH02623._CH', 'ED6_DT07/CH02623P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02363._CH', 'ED6_DT07/CH02363P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02033._CH', 'ED6_DT07/CH02033P._CP'),
        ('ED6_DT07/CH02103._CH', 'ED6_DT07/CH02103P._CP'),
        ('ED6_DT06/CH20088._CH', 'ED6_DT06/CH20088P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '索蕾拉',
            x                   = -1020,
            z                   = 0,
            y                   = 85000,
            direction           = 175,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '妮舒',
            x                   = -2500,
            z                   = 0,
            y                   = 76500,
            direction           = 53,
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
            name                = '布莉姆',
            x                   = 2500,
            z                   = 0,
            y                   = 81150,
            direction           = 255,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '艾科尔',
            x                   = -5950,
            z                   = 0,
            y                   = 68110,
            direction           = 272,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65555,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1376275,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179667,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983059,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1376275,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1441811,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245203,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048595,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1441811,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327699,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327699,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327699,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1769491,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1769491,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835027,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835027,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835027,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835027,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xAD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xAD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xAD2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xAD2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_AE0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_07_11B5)

    def _loc_AE0(): pass

    label('loc_AE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B0A',
    )

    ChrSetChipByIndex(0x0000, 9)
    ChrSetChipByIndex(0x0001, 10)
    ChrSetChipByIndex(0x0138, 11)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_B0A(): pass

    label('loc_B0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_B28',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_B89')

    def _loc_B28(): pass

    label('loc_B28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_B3C',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)

    Jump('loc_B89')

    def _loc_B3C(): pass

    label('loc_B3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_B5A',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_B89')

    def _loc_B5A(): pass

    label('loc_B5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_B78',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_B89')

    def _loc_B78(): pass

    label('loc_B78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_B82',
    )

    Jump('loc_B89')

    def _loc_B82(): pass

    label('loc_B82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_B89',
    )

    def _loc_B89(): pass

    label('loc_B89')

    Return()

# id: 0x0001 offset: 0xB8A
@scena.Code('func_01_B8A')
def func_01_B8A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_B9A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B9A(): pass

    label('loc_B9A')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0xBA4
@scena.Code('func_02_BA4')
def func_02_BA4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BB9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_BA4')

    def _loc_BB9(): pass

    label('loc_BB9')

    Return()

# id: 0x0003 offset: 0xBBA
@scena.Code('func_03_BBA')
def func_03_BBA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_BC7',
    )

    Jump('loc_CCB')

    def _loc_BC7(): pass

    label('loc_BC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_C27',
    )

    ChrTalk(
        0x00FE,
        (
            '因为诞辰庆典，\n',
            '今天大街上很热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要不是还有工作，\n',
            '也会出去好好玩玩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_C27(): pass

    label('loc_C27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_C31',
    )

    Jump('loc_CCB')

    def _loc_C31(): pass

    label('loc_C31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_C3B',
    )

    Jump('loc_CCB')

    def _loc_C3B(): pass

    label('loc_C3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_C70',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '茜亚和希尔丹夫人到哪儿去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_C70(): pass

    label('loc_C70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_CCB',
    )

    ChrTalk(
        0x00FE,
        (
            '还要让客人们专程\n',
            '来陪公爵他消磨时间，\n',
            '真是够麻烦的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明大家都那么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCB(): pass

    label('loc_CCB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xCCF
@scena.Code('func_04_CCF')
def func_04_CCF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_CDC',
    )

    Jump('loc_E17')

    def _loc_CDC(): pass

    label('loc_CDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_CE6',
    )

    Jump('loc_E17')

    def _loc_CE6(): pass

    label('loc_CE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_CF0',
    )

    Jump('loc_E17')

    def _loc_CF0(): pass

    label('loc_CF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_CFA',
    )

    Jump('loc_E17')

    def _loc_CFA(): pass

    label('loc_CFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_D50',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '理查德上校实在是帅呆了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和那个公爵相比\n',
            '根本就是天壤之别嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E17')

    def _loc_D50(): pass

    label('loc_D50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_E17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_DA9',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '公爵用那双讨厌的眼睛\n',
            '在我身上转来转去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，太无礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E17')

    def _loc_DA9(): pass

    label('loc_DA9')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '刚才在走廊上\n',
            '和杜南公爵擦肩而过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵他用\n',
            '那双讨厌的眼睛\n',
            '在我身上转来转去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，太无礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E17(): pass

    label('loc_E17')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xE1B
@scena.Code('func_05_E1B')
def func_05_E1B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_E28',
    )

    Jump('loc_ECD')

    def _loc_E28(): pass

    label('loc_E28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_E32',
    )

    Jump('loc_ECD')

    def _loc_E32(): pass

    label('loc_E32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_E3C',
    )

    Jump('loc_ECD')

    def _loc_E3C(): pass

    label('loc_E3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_E46',
    )

    Jump('loc_ECD')

    def _loc_E46(): pass

    label('loc_E46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_E87',
    )

    ChrTalk(
        0x00FE,
        (
            '终于结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快收拾好东西，\n',
            '早点回家去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ECD')

    def _loc_E87(): pass

    label('loc_E87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_ECD',
    )

    ChrTalk(
        0x00FE,
        (
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对不起呀，\n',
            '我现在正忙着晚宴的准备工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ECD(): pass

    label('loc_ECD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xED1
@scena.Code('func_06_ED1')
def func_06_ED1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_EDE',
    )

    Jump('loc_11B1')

    def _loc_EDE(): pass

    label('loc_EDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_FAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_F40',
    )

    ChrTalk(
        0x00FE,
        (
            '特务部队的队长\n',
            '取下面具之后，\n',
            '真是帅呆了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '为何他要戴面具呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FAB')

    def _loc_F40(): pass

    label('loc_F40')

    ChrTalk(
        0x00FE,
        (
            '我悄悄对你们说哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特务部队的队长\n',
            '取下面具之后，\n',
            '真是帅呆了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '为何他要戴面具呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FAB(): pass

    label('loc_FAB')

    Jump('loc_11B1')

    def _loc_FAE(): pass

    label('loc_FAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_FB8',
    )

    Jump('loc_11B1')

    def _loc_FB8(): pass

    label('loc_FB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_FC2',
    )

    Jump('loc_11B1')

    def _loc_FC2(): pass

    label('loc_FC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_10B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1035',
    )

    ChrTalk(
        0x00FE,
        (
            '公爵喝醉之后\n',
            '会变得更加无耻下流……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直不敢相信他和女王陛下\n',
            '还有公主殿下是同一血脉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B1')

    def _loc_1035(): pass

    label('loc_1035')

    ChrTalk(
        0x00FE,
        (
            '我悄悄对你们说哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵喝醉之后\n',
            '会变得更加无耻下流……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直不敢相信他和女王陛下\n',
            '还有公主殿下是同一血脉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B1(): pass

    label('loc_10B1')

    Jump('loc_11B1')

    def _loc_10B4(): pass

    label('loc_10B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_11B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_112E',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然人手已经足够了，\n',
            '但公爵还要叫希尔丹夫人\n',
            '不断增加侍女的数量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正他肯定是\n',
            '不怀什么好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B1')

    def _loc_112E(): pass

    label('loc_112E')

    ChrTalk(
        0x00FE,
        (
            '我悄悄对你们说哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然人手已经足够了，\n',
            '但公爵还要叫希尔丹夫人\n',
            '不断增加侍女的数量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正他肯定是\n',
            '不怀什么好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B1(): pass

    label('loc_11B1')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x11B5
@scena.Code('func_07_11B5')
def func_07_11B5():
    EventBegin(0x00)
    CameraMove(810, 0, 78760, 0)
    OP_67(0, 5340, -10000, 0)
    CameraSetDistance(1850, 0)
    OP_6C(39000, 0)
    OP_6E(492, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x000C, -2450, 200, 82370, 90)
    ChrSetPos(0x000D, -2450, 200, 79820, 90)
    ChrSetPos(0x000E, -2450, 200, 77340, 90)
    ChrSetPos(0x0010, -2450, 200, 74860, 90)
    ChrSetPos(0x000F, -3070, 200, 74030, 90)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0108, 0x0004)
    ChrSetPos(0x0108, 2490, 200, 79820, 270)
    ChrSetPos(0x0102, 2490, 200, 74860, 270)
    ChrSetPos(0x0101, 2490, 200, 77340, 270)
    ChrSetChipByIndex(0x0101, 16)
    ChrSetChipByIndex(0x0102, 17)
    ChrSetChipByIndex(0x0108, 18)
    ChrSetPos(0x0011, 6840, -10000, 80920, 270)
    ChrSetPos(0x0012, 6840, -10000, 79460, 270)
    ChrSetPos(0x0013, 6840, -10000, 77970, 270)
    ChrSetPos(0x0014, 6840, -10000, 76490, 270)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)
    ChrClearFlags(0x002F, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    ChrClearFlags(0x0031, 0x0080)
    ChrClearFlags(0x0032, 0x0080)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrClearFlags(0x003D, 0x0080)
    ChrClearFlags(0x003E, 0x0080)
    ChrClearFlags(0x003F, 0x0080)
    ChrClearFlags(0x0040, 0x0080)
    ChrClearFlags(0x0041, 0x0080)
    ChrClearFlags(0x0042, 0x0080)
    ChrClearFlags(0x0043, 0x0080)
    ChrClearFlags(0x0044, 0x0080)
    ChrClearFlags(0x0045, 0x0080)
    ChrClearFlags(0x0046, 0x0080)
    ChrClearFlags(0x0047, 0x0080)
    ChrClearFlags(0x0048, 0x0080)
    ChrClearFlags(0x0049, 0x0080)
    ChrClearFlags(0x004A, 0x0080)
    ChrSetPos(0x0015, 1600, 650, 82450, 0)
    ChrSetPos(0x0016, 1600, 650, 79950, 0)
    ChrSetPos(0x0017, 1600, 650, 77440, 0)
    ChrSetPos(0x0018, 1600, 650, 74950, 0)
    ChrSetPos(0x0019, -1600, 670, 82350, 0)
    ChrSetPos(0x001A, -1600, 670, 79950, 0)
    ChrSetPos(0x001B, -1600, 670, 77450, 0)
    ChrSetPos(0x001C, -1600, 670, 74850, 0)
    ChrSetPos(0x001D, 0, 650, 83860, 0)
    ChrSetPos(0x004A, -500, 640, 83860, 0)
    ChrSetPos(0x0041, -700, 640, 83860, 0)
    ChrSetPos(0x0038, 200, 640, 83860, 0)
    ChrSetPos(0x002F, 400, 640, 83860, 0)
    ChrSetPos(0x0039, 1600, 640, 82700, 0)
    ChrSetPos(0x003A, 1600, 640, 80200, 0)
    ChrSetPos(0x003B, 1600, 640, 77600, 0)
    ChrSetPos(0x003C, 1600, 640, 75200, 0)
    ChrSetPos(0x002B, -1600, 640, 82700, 0)
    ChrSetPos(0x002C, -1600, 640, 80200, 0)
    ChrSetPos(0x002D, -1600, 640, 77700, 0)
    ChrSetPos(0x002E, -1600, 640, 75200, 0)
    ChrSetPos(0x0042, 1600, 640, 82900, 0)
    ChrSetPos(0x0043, 1600, 640, 80400, 0)
    ChrSetPos(0x0044, 1600, 640, 77800, 0)
    ChrSetPos(0x0045, 1600, 640, 75400, 0)
    ChrSetPos(0x0034, -1600, 640, 82900, 0)
    ChrSetPos(0x0035, -1600, 640, 80400, 0)
    ChrSetPos(0x0036, -1600, 640, 77900, 0)
    ChrSetPos(0x0037, -1600, 640, 75400, 0)
    ChrSetPos(0x0027, 1600, 640, 82000, 0)
    ChrSetPos(0x0028, 1600, 640, 79600, 0)
    ChrSetPos(0x0029, 1600, 640, 77000, 0)
    ChrSetPos(0x002A, 1600, 640, 74500, 0)
    ChrSetPos(0x003D, -1600, 640, 81900, 0)
    ChrSetPos(0x003E, -1600, 640, 79500, 0)
    ChrSetPos(0x003F, -1600, 640, 77000, 0)
    ChrSetPos(0x0040, -1600, 640, 74400, 0)
    ChrSetPos(0x0030, 1600, 640, 81800, 0)
    ChrSetPos(0x0031, 1600, 640, 79400, 0)
    ChrSetPos(0x0032, 1600, 640, 76800, 0)
    ChrSetPos(0x0033, 1600, 640, 74300, 0)
    ChrSetPos(0x0046, -1600, 640, 81700, 0)
    ChrSetPos(0x0047, -1600, 640, 79300, 0)
    ChrSetPos(0x0048, -1600, 640, 76800, 0)
    ChrSetPos(0x0049, -1600, 640, 74200, 0)
    ChrSetSubChip(0x000C, 2)
    ChrSetSubChip(0x000D, 2)
    ChrSetSubChip(0x000E, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0108, 1)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 2)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010120611V#505F唔……\n',
            '这就是传说中的晚宴吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120612V可是为什么餐具摆放好了，\n',
            '那些听说非常好吃的料理却没有呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120613V为什么这些刀子啊叉子啊\n',
            '要这样整整齐齐并排放在一起呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120614V#010F#2P因为这是很正式的晚宴啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120615V先是凉菜，\n',
            '然后接着才上各种各样的料理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120616V还有就是刀子和叉子要从侧边来拿。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120617V#509F真麻烦……\n',
            '这就是所谓的餐桌礼仪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120618V#007F我还真是有些紧张了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120619V#611F嘻嘻……不用那么在意。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120620V因为品尝料理的美味才是最重要的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120621V什么礼仪礼貌的都是其次的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120622V#601F对啊对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120623V更何况，你们两人对\n',
            '在场出席的各位不都是很熟悉的嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120624V没有必要那么拘束哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120625V#001F啊，说的也是啊?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120626V#017F#2P这样一来就没办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120627V#610F对了，请问这位先生\n',
            '对于这里的刀子和叉子习惯吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120628V我听说东方那边主要是使用筷子的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120629V#073F哦，您知道得很清楚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120630V#070F不过俗话说得好，入乡随俗嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120631V虽说用得不好，\n',
            '但还是会一点用刀子和叉子的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120632V#611F啊……很了不起呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120633V不愧是取得武术大会优胜的武术高手，\n',
            '说起话来都和普通人不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120634V#071F哈哈哈……\n',
            '哪里哪里，小姐您过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120635V#506F（确实是对美人没有抵抗力呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120636V#010F#2P（可是我并不觉得\n',
            '　他是一个喜好女色的人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0550120637V#805F话说回来……\n',
            '公爵大人怎么这么慢呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120638V究竟想要做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120639V#600F嗯……的确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120640V而且，如果说上座是公爵大人的，\n',
            '那么那边的座位又是给谁的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0530120641V#783F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120642V大概，科洛蒂娅公主坐在那里的\n',
            '可能性会比较高……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, -250, 0, 62670, 0)
    ChrSetPos(0x0009, 460, 0, 62290, 0)
    ChrSetPos(0x000A, -110, 0, 64099, 0)
    ChrSetPos(0x000B, 10, 0, 62670, 0)

    ChrTalk(
        0x000B,
        (
            '#0660120643V#1P各位……\n',
            '让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E8A')
    def lambda_1E8A():
        CameraMove(370, 0, 72370, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1E8A)

    ChrSetSubChip(0x000C, 2)
    ChrSetSubChip(0x000E, 2)
    Sleep(100)

    ChrSetSubChip(0x0108, 1)
    ChrSetSubChip(0x0010, 2)
    Sleep(100)

    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x000D, 2)
    Sleep(100)

    ChrSetSubChip(0x0102, 1)
    Sleep(700)

    @scena.Lambda('lambda_1ED9')
    def lambda_1ED9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1ED9)

    @scena.Lambda('lambda_1EEB')
    def lambda_1EEB():
        ChrWalkTo(0x00FE, 10, 0, 66950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1EEB)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#0660120644V#720F公爵大人大驾光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F39')
    def lambda_1F39():
        ChrWalkTo(0x00FE, -2190, 0, 67060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1F39)

    WaitForThreadExit(0x000B, 0x0001)
    ChrSetDirection(0x000B, 0, 400)
    Sleep(300)

    @scena.Lambda('lambda_1F65')
    def lambda_1F65():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1F65)

    @scena.Lambda('lambda_1F77')
    def lambda_1F77():
        ChrWalkTo(0x00FE, -140, 0, 69090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1F77)

    Sleep(300)

    @scena.Lambda('lambda_1F97')
    def lambda_1F97():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1F97)

    @scena.Lambda('lambda_1FA9')
    def lambda_1FA9():
        ChrWalkTo(0x00FE, 1080, 0, 68670, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FA9)

    Sleep(600)

    @scena.Lambda('lambda_1FC9')
    def lambda_1FC9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_1FC9)

    @scena.Lambda('lambda_1FDB')
    def lambda_1FDB():
        ChrWalkTo(0x00FE, 400, 0, 67340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1FDB)

    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0640120645V#220F哎呀，诸位亲爱的朋友，\n',
            '让你们等那么久真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120646V因为刚才稍稍有点事要协商一下，\n',
            '所以拖延了一点儿的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 90, 400)

    ChrTalk(
        0x000A,
        (
            '#0640120647V#220F这位是理查德上校，\n',
            '王国军情报部的负责人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120648V为了解决恐怖事件，\n',
            '他日夜操劳、尽心尽力，\n',
            '作为对他工作的奖赏我就邀请他来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0130120649V#110F初次与大家见面。\n',
            '我是王国军情报部的理查德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120650V承蒙公爵大人的好意，\n',
            '我今天得以有幸参加这次晚宴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120651V这身与场合不相称的军服有些失礼了，\n',
            '但还请允许我与各位同席。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000A, 0x01, 0x00, func_0A_455A)
    Sleep(300)

    Sleep(100)

    @scena.Lambda('lambda_220D')
    def lambda_220D():
        CameraMove(810, 0, 78760, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_220D)

    CreateThread(0x0008, 0x01, 0x00, func_08_44CB)
    Sleep(200)

    CreateThread(0x000B, 0x01, 0x00, func_0B_45CD)
    CreateThread(0x0009, 0x01, 0x00, func_09_452A)
    CreateThread(0x0108, 0x01, 0x00, func_0C_4611)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010120652V#509F（竟、竟然会和上校一起在餐桌上用餐……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120653V#012F#2P（虽然猜到了几分，\n',
            '　但果然还是些紧张……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(0, 0, 72440, 0)
    OP_67(0, 9430, -10000, 0)
    CameraSetDistance(1990, 0)
    OP_6C(45000, 0)
    OP_6E(492, 0)
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrSetPos(0x004B, 0, 700, 81230, 0)
    ChrSetPos(0x004C, 0, 700, 78740, 0)
    ChrSetPos(0x004D, 0, 700, 76070, 0)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x001E, 1500, 640, 83150, 0)
    ChrSetPos(0x001F, 1500, 640, 80650, 0)
    ChrSetPos(0x0020, 1500, 640, 78140, 0)
    ChrSetPos(0x0021, 1500, 640, 75650, 0)
    ChrSetPos(0x0022, -1600, 640, 81450, 0)
    ChrSetPos(0x0023, -1600, 640, 79050, 0)
    ChrSetPos(0x0024, -1600, 640, 76650, 0)
    ChrSetPos(0x0025, -1600, 640, 74050, 0)
    ChrSetPos(0x0026, -800, 640, 83860, 0)
    ChrSetSubChip(0x0015, 28)
    ChrSetSubChip(0x0015, 9)
    ChrSetSubChip(0x0016, 9)
    ChrSetSubChip(0x0017, 9)
    ChrSetSubChip(0x0018, 9)
    ChrSetSubChip(0x0019, 9)
    ChrSetSubChip(0x001A, 9)
    ChrSetSubChip(0x001B, 9)
    ChrSetSubChip(0x001C, 9)
    ChrSetSubChip(0x001D, 9)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0029, 0x0080)
    ChrSetFlags(0x002A, 0x0080)
    ChrSetFlags(0x002B, 0x0080)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0039, 0x0080)
    ChrSetFlags(0x003A, 0x0080)
    ChrSetFlags(0x003B, 0x0080)
    ChrSetFlags(0x003C, 0x0080)
    ChrSetFlags(0x003D, 0x0080)
    ChrSetFlags(0x003E, 0x0080)
    ChrSetFlags(0x003F, 0x0080)
    ChrSetFlags(0x0049, 0x0080)
    ChrSetFlags(0x002F, 0x0080)
    ChrSetFlags(0x0041, 0x0080)
    ChrSetPos(0x0011, -3100, 0, 86090, 339)
    ChrSetPos(0x0012, 4910, 0, 72190, 265)
    ChrSetPos(0x0013, -220, 0, 71290, 2)
    ChrSetPos(0x0014, -5050, 0, 78270, 84)
    OP_72(0x000C, 0x0004)
    OP_72(0x000D, 0x0004)
    ChrClearFlags(0x004E, 0x0080)
    ChrClearFlags(0x004F, 0x0080)
    ChrClearFlags(0x0050, 0x0080)
    ChrClearFlags(0x0051, 0x0080)
    ChrClearFlags(0x0052, 0x0080)
    ChrClearFlags(0x0053, 0x0080)
    ChrSetPos(0x004E, -3280, 750, 87230, 0)
    ChrSetPos(0x0050, -2630, 700, 87630, 0)
    ChrSetPos(0x0051, -2470, 700, 87240, 0)
    ChrSetPos(0x004F, 3960, 750, 70260, 0)
    ChrSetPos(0x0052, 3990, 700, 70960, 0)
    ChrSetPos(0x0053, 4440, 700, 70760, 0)
    ChrSetSubChip(0x000C, 0)
    ChrSetSubChip(0x000D, 1)
    ChrSetSubChip(0x000E, 1)
    ChrSetSubChip(0x0010, 1)
    ChrSetSubChip(0x0108, 2)
    ChrSetSubChip(0x0101, 2)
    ChrSetSubChip(0x0102, 2)
    WaitForThreadExit(0x000B, 0x0001)
    Sleep(1000)

    FadeIn(2000, 0)
    CameraMove(-50, 0, 85000, 5000)
    PlaySE(232, 0x00, 0x64)
    Fade(1000)
    CameraMove(1080, 0, 79800, 0)
    OP_67(0, 3950, -10000, 0)
    CameraSetDistance(2113, 0)
    OP_6C(39000, 0)
    OP_6E(492, 0)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0640120654V#221F哈～哈～哈，哎呀，愉快愉快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120655V#220F怎么样，梅贝尔市长。\n',
            '格兰赛尔城这里的厨艺怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120656V与柏斯的『安特洛丝餐厅』相比\n',
            '也毫不逊色对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120657V#610F嗯，很精妙的厨艺呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120658V配上葡萄酒的话可以说是非常完美了，\n',
            '的确是出乎预料的极品佳肴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120659V#221F哈哈哈～～～\n',
            '既然都这么说了肯定就不是吹牛的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120660V#220F对了，你是叫金对吧。\n',
            '东方人对于这些可能会不大合胃口吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120661V#070F哪里，非常美味啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120662V虽说在下的舌头很迟钝，\n',
            '但也能感觉得出其中蕴涵的美味。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120663V品味出了利贝尔料理的精髓所在。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120664V#225F嗯嗯，说得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120665V#220F怎么样啊，两位年轻的游击士？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120666V如此豪华的料理还是第一次品尝到吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120667V#001F#4P唔～～\n',
            '的确非常非常美味啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120668V邀请的人就先不论如何，\n',
            '就这个料理来说还真的很美妙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120669V#221F哈哈哈。\n',
            '说得好、说得好…………啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120670V#223F……唔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020120671V#019F#4P呵呵，没错没错。\n',
            '实在是十分优秀的料理呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120672V而且至今为止我们还没有过这样\n',
            '能够和各界名流一起共聚晚宴的机会，\n',
            '说起来还真是有些不习惯呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120673V#010F承蒙公爵大人您的款待，\n',
            '我们真是感激不尽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120674V#221F哈哈哈。\n',
            '这位小男孩很会说话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120675V#220F不过刚才经管家的提醒，\n',
            '我现在总算是想起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120676V你们两个就是曾经在卢安事件中\n',
            '和我见过一面的小孩嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120677V缘分这个东西真是奇妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120678V#506F#4P哈、哈哈……是～是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120679V#505F（管家没有提醒之前\n',
            '　难道自己就不会想起来吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120680V#221F好啊，今晚不醉不归！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120681V料理和美酒都是应有尽有，\n',
            '不要有顾虑，诸位想享用就尽管说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120682V#110F#2P公爵大人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120683V要不我们先告诉大家\n',
            '刚才商量后达成的决定如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120684V#223F……哦哦！\n',
            '对啊，还有这么回事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120685V#220F事实上把作为王国代表的诸位\n',
            '集中在这里没有什么别的意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120686V就是借这个晚宴的机会\n',
            '向大家宣布一件重大的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120687V#604F#6P重大的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0550120688V#800F这究竟……\n',
            '是什么样的事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120689V#225F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120690V在此首先由理查德上校来为我\n',
            '说明相关的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120691V#115F#2P……惶恐之至。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrSetSubChip(0x0008, 1)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0130120692V#110F#5P女王陛下身体欠佳，\n',
            '是各位之前已知的事实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120693V不过陛下正在缓缓的康复中，\n',
            '很快就会以往日的姿态与人们见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120694V#601F#6P哦……这就好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120695V#611F那去探望陛下也是可以的了？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120696V#115F#5P真是抱歉，照陛下的意向，\n',
            '还是希望暂时先谢绝各位的探望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120697V#110F然而，这几天扰乱王都周边\n',
            '秩序的恐怖组织要先予以铲除。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120698V这件事成功之后，\n',
            '女王陛下的诞辰庆典才能按期顺利进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0530120699V#783F嗯……\n',
            '这真是可喜可贺，\n',
            '毕竟广大市民都很期待这场庆典。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120700V#780F不过……\n',
            '想要说的应该不止是这些吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0550120701V#803F……是啊，如果只是这些的话，\n',
            '联络我们并说明就可以了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120702V#111F#5P呵呵，能察觉到就好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120703V#115F女王陛下的健康状况正在恢复，\n',
            '之前也已经说到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120704V陛下因为这次身体欠佳，\n',
            '所以先前已经做出了一个决定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120705V那个决定就是——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrSetSubChip(0x0008, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0130120706V#112F#5P艾莉茜雅女王陛下自动退位，\n',
            '让在座的杜南公爵大人继承王位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0550120707V#804F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120708V#613F真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120709V#005F#4P（约修亚，这是……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120710V#012F#4P（嗯……\n',
            '阴谋终于浮出水面了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120711V#225F……我也感到有些意外，\n',
            '不过女王陛下确实有些力不从心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120712V这也是陛下迫不得已的决定，\n',
            '一名女性能领导经历了诸多动荡的王国\n',
            '长达４０年已经是实属不易的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120713V#220F所以，陛下打算在诞辰庆典之后，\n',
            '从王国的政务俗事中解放出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120714V转交王位的继承权的决定\n',
            '就是出于这样的一个原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120715V#603F#6P竟然……\n',
            '陛下一直为此而深感苦恼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120716V每年见到她的时候都没感觉到，\n',
            '是我们的不对啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120717V#612F可、可是……\n',
            '怎能在这样一个觥筹交错的宴席上\n',
            '宣布如此重大的决议呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120718V冒昧地问一句，\n',
            '您刚才这番话究竟算不算数的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120719V#222F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0130120720V#110F#5P哼哼，梅贝尔市长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120721V公爵大人的话毫无信用可言，\n',
            '……这就是你的意思吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120722V#614F我、我没有那么说过！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120723V倘若女王陛下真的要退位，\n',
            '也只能通过市长的投票来表决王位继承人，\n',
            '我不解的是为何连这项程序都不执行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0550120724V#803F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120725V可以的话，我们想直接\n',
            '向陛下询问一下刚才那些决议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120726V#226F呜、呜～嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120727V#115F#5P各位不解的情绪我很理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120728V不过还是请冷静下来，\n',
            '暂且先知道就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120729V#110F更进一步地来说，\n',
            '女王陛下本人将会在诞辰庆典之时\n',
            '亲自公布这项重大的决议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120730V是真是假到那时就可以见分晓了对吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0550120731V#805F这、这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120732V#112F#5P问题在于公布这项决议时\n',
            '会给普通市民带来什么样的影响。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120733V为了避免无益的混乱，\n',
            '所以才把各地区的负责人也就是在座的\n',
            '各位召集到这里来传达这项决议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120734V公爵大人也是这么认为的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120735V#225F咳咳……\n',
            '嗯，就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120736V#112F#5P而且陛下如果退位的话，\n',
            '这个消息肯定不止是流传于国内。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120737V大陆诸国，尤其是我们最大的威胁\n',
            '埃雷波尼亚帝国肯定会注意到这个变动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120738V正因为如此，\n',
            '在座的各位应该扶植新的国王陛下，\n',
            '如果不团结起来是绝对不行的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120739V特别是在这样一个关键时期即将来临的时刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000C, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0010, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000D, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010120740V#509F#4P（居、居然说得如此冠冕堂皇……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120741V#015F#4P（嗯……\n',
            '　好一个煽动者啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000E)
    OP_63(0x000C)
    OP_63(0x0010)
    OP_63(0x000D)

    ChrTalk(
        0x000E,
        (
            '#0550120742V#800F正式的决定可以在诞辰庆典时\n',
            '向陛下直接请示……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120743V不过要事先做好心里准备，\n',
            '就是这样对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120744V#111F#5P哼哼……\n',
            '能够理解真是万幸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120745V#603F#6P唔～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120746V一旦这件事情落实了，\n',
            '我们日后的工作就有得忙碌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120747V#615F是呢……\n',
            '还要向市民们宣布。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0530120748V#782F……我还有一事想请教一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120749V公爵大人具有王位的继承权\n',
            '这点我也承认……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120750V我认为具有同样资格的继承者\n',
            '应该还有另外一位吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120751V#226F这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120752V#110F#5P还有陛下的孙女科洛蒂娅殿下。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120753V的确，依据王室典范的规定，\n',
            '她和公爵大人拥有同等资格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120754V但是，毕竟她的年纪尚幼，\n',
            '所以陛下就推选了公爵大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120755V#115F而且之前也说到过……\n',
            '要一位小姑娘来承担一种女性  \n',
            '所不能承担的重责是不可取的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120756V#221F对呀对呀，就是这样的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120757V#220F对了，现在正打算为\n',
            '科洛蒂娅公主寻找良缘佳偶。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120758V虽然是非正式的，但是之前其他国家的王族\n',
            '已经提出过了相关的事宜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120759V如果时机成熟的话，\n',
            '准备在今年年中实现这个婚约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360120760V#613F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0530120761V#783F……唔，您说的话我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120762V#780F这么一来就可以让好事成双了对吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120763V#604F#6P唔……公主殿下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120764V要此时结婚似乎也太过早了吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120765V#070F……打搅一下。\n',
            '我问个问题好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120766V#004F#4P金、金先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120767V#220F哦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120768V没关系，但说无妨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120769V#074F很抱歉，刚才听到那番话之后，\n',
            '本来作为外人的我们是不应该对此多言的，\n',
            '但是有些问题不能不问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120770V况且我并非是王国的国民。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120771V#070F那就是……为何要特地在\n',
            '这样的酒席间发表如此重大的决议？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120772V#110F#5P这是因为取得优胜的几位\n',
            '恰好就是游击士的缘故。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120773V陛下退位这个重大的事情\n',
            '也需要拜托你们传达给游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120774V所以我才给公爵大人提议，\n',
            '让你们参加晚宴来得知这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120775V#073F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120776V在利贝尔王国，军队和协会有着\n',
            '良好的关系的传言看来果真不假。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0130120777V#111F#5P哈哈，和帝国及共和国相比，\n',
            '我国的军力不是很充实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120778V只有携起手来，\n',
            '才能面对苛刻的现实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120779V#110F总之就是这样的，\n',
            '你明白其中的意思了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120780V#070F呼……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120781V我会把今天从宴席中得知的情况\n',
            '转达给王都支部的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4262._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x44CB
@scena.Code('func_08_44CB')
def func_08_44CB():
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 4310, 0, 69570, 3000, 0x00)
    ChrWalkTo(0x00FE, 4370, 0, 80610, 3000, 0x00)
    ChrWalkTo(0x00FE, 2350, 0, 81840, 3000, 0x00)
    ChrSetPos(0x00FE, 2500, 200, 82410, 270)
    ChrSetChipByIndex(0x00FE, 13)
    ChrSetDirection(0x00FE, 270, 0)

    Return()

# id: 0x0009 offset: 0x452A
@scena.Code('func_09_452A')
def func_09_452A():
    ChrWalkTo(0x00FE, 4310, 0, 69570, 3000, 0x00)
    ChrWalkTo(0x00FE, 4470, 0, 83040, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x000A offset: 0x455A
@scena.Code('func_0A_455A')
def func_0A_455A():
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -4380, 0, 71660, 3000, 0x00)
    ChrWalkTo(0x00FE, -4280, 0, 85250, 3000, 0x00)
    ChrWalkTo(0x00FE, -1030, 0, 85250, 3000, 0x00)
    ChrWalkTo(0x00FE, -520, 0, 85000, 2000, 0x00)
    ChrSetPos(0x00FE, -20, 200, 84940, 180)
    ChrSetChipByIndex(0x00FE, 15)
    ChrSetDirection(0x00FE, 180, 0)

    Return()

# id: 0x000B offset: 0x45CD
@scena.Code('func_0B_45CD')
def func_0B_45CD():
    ChrWalkTo(0x00FE, -4380, 0, 71660, 3000, 0x00)
    ChrWalkTo(0x00FE, -4280, 0, 85250, 3000, 0x00)
    ChrWalkTo(0x00FE, -910, 0, 86310, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x000C offset: 0x4611
@scena.Code('func_0C_4611')
def func_0C_4611():
    Sleep(2000)

    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0010, 0)
    Sleep(1000)

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x000E, 0)
    Sleep(1000)

    ChrSetSubChip(0x0108, 0)
    ChrSetSubChip(0x000D, 0)
    Sleep(1000)

    ChrSetSubChip(0x000C, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
