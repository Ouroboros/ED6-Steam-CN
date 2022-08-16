import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1400.x'
    header.mapIndex       = 1
    header.bgm            = 16
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT27/CH03790._CH', 'ED6_DT27/CH03790P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卫兵',
            x                   = 9100,
            z                   = 0,
            y                   = -10190,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '卫兵',
            x                   = -2400,
            z                   = 0,
            y                   = -7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -9000,
            z                   = 11750,
            y                   = 3000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 9000,
            z                   = 11750,
            y                   = 3000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '卡尔科斯',
            x                   = -2100,
            z                   = 0,
            y                   = -20100,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '龙谷',
            x                   = 7620,
            z                   = 10,
            y                   = -18860,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '斯丁克',
            x                   = -12650,
            z                   = 0,
            y                   = -26140,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -4570,
            z                   = 0,
            y                   = -8880,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 80,
            z                   = 0,
            y                   = -10570,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 1900,
            z                   = 0,
            y                   = -9630,
            direction           = 303,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -2620,
            z                   = 0,
            y                   = -11290,
            direction           = 27,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 4010,
            z                   = 0,
            y                   = -9180,
            direction           = 303,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 2430,
            z                   = 0,
            y                   = -11400,
            direction           = 1,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = -14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262144,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = -14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262144,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = -14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262144,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = -14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262144,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = -14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262144,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = -14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262144,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = -14600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262144,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '摩尔根将军',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '钢壁之路方向',
            x                   = 11890,
            z                   = 40,
            y                   = -60460,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x9D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x9D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x9D2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x9D2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A84',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, func_02_B68)
    CreateThread(0x000B, 0x00, 0x00, func_02_B68)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_A81',
    )

    ChrSetPos(0x000F, -1400, 0, -12000, 0)
    ChrSetPos(0x0010, 0, 0, -12000, 0)
    ChrSetPos(0x0011, 1400, 0, -12000, 0)
    ChrSetPos(0x0012, -1400, 0, -13400, 0)
    ChrSetPos(0x0013, 0, 0, -13400, 0)
    ChrSetPos(0x0014, 1400, 0, -13400, 0)

    def _loc_A81(): pass

    label('loc_A81')

    Jump('loc_AC5')

    def _loc_A84(): pass

    label('loc_A84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_A98',
    )

    ChrSetChipByIndex(0x000C, 1)
    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_AC5')

    def _loc_A98(): pass

    label('loc_A98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_AA7',
    )

    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_AC5')

    def _loc_AA7(): pass

    label('loc_AA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AC5',
    )

    ChrClearFlags(0x000E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC5',
    )

    ChrSetFlags(0x000E, 0x0010)

    def _loc_AC5(): pass

    label('loc_AC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_AE4',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_14_2E21)

    Jump('loc_B00')

    def _loc_AE4(): pass

    label('loc_AE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_B00',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_15_37E2)

    def _loc_B00(): pass

    label('loc_B00')

    Return()

# id: 0x0001 offset: 0xB01
@scena.Code('func_01_B01')
def func_01_B01():
    OP_16(0x02, 4000, -122000, -130000, 2293829)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B3A',
    )

    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 560)
    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)

    def _loc_B3A(): pass

    label('loc_B3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B4E',
    )

    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 0)

    def _loc_B4E(): pass

    label('loc_B4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 7, 0x208F)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B67',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B67(): pass

    label('loc_B67')

    Return()

# id: 0x0002 offset: 0xB68
@scena.Code('func_02_B68')
def func_02_B68():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B8D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_CCF')

    def _loc_B8D(): pass

    label('loc_B8D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BA6',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_CCF')

    def _loc_BA6(): pass

    label('loc_BA6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BBF',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_CCF')

    def _loc_BBF(): pass

    label('loc_BBF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BD8',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_CCF')

    def _loc_BD8(): pass

    label('loc_BD8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF1',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_CCF')

    def _loc_BF1(): pass

    label('loc_BF1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_CCF')

    def _loc_C0A(): pass

    label('loc_C0A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C23',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_CCF')

    def _loc_C23(): pass

    label('loc_C23')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C3C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_CCF')

    def _loc_C3C(): pass

    label('loc_C3C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C55',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_CCF')

    def _loc_C55(): pass

    label('loc_C55')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C6E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_CCF')

    def _loc_C6E(): pass

    label('loc_C6E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C87',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_CCF')

    def _loc_C87(): pass

    label('loc_C87')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA0',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_CCF')

    def _loc_CA0(): pass

    label('loc_CA0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB9',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_CCF')

    def _loc_CB9(): pass

    label('loc_CB9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CCF',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_CCF(): pass

    label('loc_CCF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CE4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_CCF')

    def _loc_CE4(): pass

    label('loc_CE4')

    Return()

# id: 0x0003 offset: 0xCE5
@scena.Code('func_03_CE5')
def func_03_CE5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D08',
    )

    OP_8D(0x00FE, -7000, -13000, 3500, -25300, 2000)

    Jump('func_03_CE5')

    def _loc_D08(): pass

    label('loc_D08')

    Return()

# id: 0x0004 offset: 0xD09
@scena.Code('func_04_D09')
def func_04_D09():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D55',
    )

    ChrWalkTo(0x00FE, -9000, 11750, 3000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, -2500, 11750, 3000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    Jump('func_04_D09')

    def _loc_D55(): pass

    label('loc_D55')

    Return()

# id: 0x0005 offset: 0xD56
@scena.Code('func_05_D56')
def func_05_D56():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DA2',
    )

    ChrWalkTo(0x00FE, 9000, 11750, 3000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 2500, 11750, 3000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    Jump('func_05_D56')

    def _loc_DA2(): pass

    label('loc_DA2')

    Return()

# id: 0x0006 offset: 0xDA3
@scena.Code('func_06_DA3')
def func_06_DA3():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_DFE',
    )

    ChrTalk(
        0x00FE,
        (
            '国境师团也接到\n',
            '紧急召集命令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是又不能用导力枪，\n',
            '要怎样战斗呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A7')

    def _loc_DFE(): pass

    label('loc_DFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EC1',
    )

    ChrTalk(
        0x00FE,
        (
            '把帝国来的货物搬进来时\n',
            '发生了那个现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '于是就如你所见，\n',
            '大门就开着停住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这，这个状态\n',
            '就等于没有防御力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果帝国军来了，\n',
            '那可真是一刻也撑不住啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_F17')

    def _loc_EC1(): pass

    label('loc_EC1')

    ChrTalk(
        0x00FE,
        (
            '把帝国来的货物搬进来时\n',
            '发生了那个现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这，这个状态\n',
            '就等于没有防御力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F17(): pass

    label('loc_F17')

    Jump('loc_10A7')

    def _loc_F1A(): pass

    label('loc_F1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_F70',
    )

    ChrTalk(
        0x00FE,
        (
            '龙的事件总算\n',
            '平安解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次没有大规模的\n',
            '出动军队真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A7')

    def _loc_F70(): pass

    label('loc_F70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_FBC',
    )

    ChrTalk(
        0x00FE,
        (
            '将军阁下\n',
            '在『埃尔赛尤』上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要亲自指挥\n',
            '龙的捕获作战呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A7')

    def _loc_FBC(): pass

    label('loc_FBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_10A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1044',
    )

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军终于\n',
            '从签字仪式回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说，今天开始\n',
            '不振作精神可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一旦松懈\n',
            '可是会被将军怪罪的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A7')

    def _loc_1044(): pass

    label('loc_1044')

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军终于\n',
            '从签字仪式回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '才刚刚回来\n',
            '就已经开始办公了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是铁人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_10A7(): pass

    label('loc_10A7')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x10AB
@scena.Code('func_07_10AB')
def func_07_10AB():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1191',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1119',
    )

    ChrTalk(
        0x00FE,
        (
            '警戒态势解除了。\n',
            '平静的日子到来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这么紧张…\n',
            '还是自政变事件之后第一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_118E')

    def _loc_1119(): pass

    label('loc_1119')

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警戒态势解除了。\n',
            '平静的日子到来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这么紧张…\n',
            '还是自政变事件之后第一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_118E(): pass

    label('loc_118E')

    Jump('loc_12A0')

    def _loc_1191(): pass

    label('loc_1191')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_11E7',
    )

    ChrTalk(
        0x00FE,
        (
            '因为龙的事件，\n',
            '要塞这也是戒严状态呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望飞行舰队\n',
            '早日捕获龙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A0')

    def _loc_11E7(): pass

    label('loc_11E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_12A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1237',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这道门的那边\n',
            '就是埃雷波尼亚帝国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A0')

    def _loc_1237(): pass

    label('loc_1237')

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这道门的那边\n',
            '就是埃雷波尼亚帝国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要通行的话\n',
            '必须有王国发行的护照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_12A0(): pass

    label('loc_12A0')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x12A4
@scena.Code('func_08_12A4')
def func_08_12A4():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_13D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_135D',
    )

    ChrTalk(
        0x00FE,
        (
            '不能用枪是很头痛，\n',
            '不过飞船是个更大的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国的防卫体系很大部分\n',
            '要依靠飞行舰队的力量嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '失去了最关键的战斗力，\n',
            '对军队来说是最大的不安因素啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_13CD')

    def _loc_135D(): pass

    label('loc_135D')

    ChrTalk(
        0x00FE,
        (
            '王国的防卫体系很大部分\n',
            '要依靠飞行舰队的力量嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '失去了最关键的战斗力，\n',
            '对军队来说是最大的不安因素呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13CD(): pass

    label('loc_13CD')

    Jump('loc_1616')

    def _loc_13D0(): pass

    label('loc_13D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1436',
    )

    ChrTalk(
        0x00FE,
        (
            '大门一直开着，\n',
            '就意味着防壁会被人趁虚而入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '担任放哨任务的人\n',
            '责任也比以往更重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1616')

    def _loc_1436(): pass

    label('loc_1436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_14EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_148D',
    )

    ChrTalk(
        0x00FE,
        (
            '这次龙的事件……\n',
            '似乎是游击士解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉功劳\n',
            '都被抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E8')

    def _loc_148D(): pass

    label('loc_148D')

    ChrTalk(
        0x00FE,
        (
            '我听说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次龙的事件……\n',
            '似乎是游击士解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像功劳都被\n',
            '抢走了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_14E8(): pass

    label('loc_14E8')

    Jump('loc_1616')

    def _loc_14EB(): pass

    label('loc_14EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_15BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1546',
    )

    ChrTalk(
        0x00FE,
        (
            '龙的捕获作战\n',
            '似乎很艰难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '飞行舰队也会陷入苦战\n',
            '实在难以想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15BA')

    def _loc_1546(): pass

    label('loc_1546')

    ChrTalk(
        0x00FE,
        (
            '龙的捕获作战\n',
            '似乎很艰难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有传闻说\n',
            '也派遣了地面部队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，肯定也是什么人\n',
            '闲的无聊瞎说的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_15BA(): pass

    label('loc_15BA')

    Jump('loc_1616')

    def _loc_15BD(): pass

    label('loc_15BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1616',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约的缔结\n',
            '和国境警戒是两回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们还是一如既往\n',
            '严格进行警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1616(): pass

    label('loc_1616')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x161A
@scena.Code('func_09_161A')
def func_09_161A():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1674',
    )

    ChrTalk(
        0x00FE,
        (
            '即使在这种非常时期\n',
            '摩尔根将军还是很镇定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是身经百战的勇将。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19AC')

    def _loc_1674(): pass

    label('loc_1674')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1746',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1702',
    )

    ChrTalk(
        0x00FE,
        (
            '那条古代龙出现之后，\n',
            '我们又被召集起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这次事态\n',
            '好像相当严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为是关系到\n',
            '王国命运的事件嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1743')

    def _loc_1702(): pass

    label('loc_1702')

    ChrTalk(
        0x00FE,
        (
            '这次的事态\n',
            '非常的严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我们士兵的使命也相当重大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1743(): pass

    label('loc_1743')

    Jump('loc_19AC')

    def _loc_1746(): pass

    label('loc_1746')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1817',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_17A7',
    )

    ChrTalk(
        0x00FE,
        (
            '感觉将军阁下的表情\n',
            '好像不太开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事件都解决了，\n',
            '到底怎么回事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1814')

    def _loc_17A7(): pass

    label('loc_17A7')

    ChrTalk(
        0x00FE,
        (
            '刚才见到了\n',
            '将军阁下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事件都已经解决了，\n',
            '但却感觉表情不大开心似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，可能是我多心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1814(): pass

    label('loc_1814')

    Jump('loc_19AC')

    def _loc_1817(): pass

    label('loc_1817')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_192F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_188A',
    )

    ChrTalk(
        0x00FE,
        (
            '国境师团虽然也处在警戒状态，\n',
            '但是并没有什么实质性的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟这里是\n',
            '国境防卫的要地嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_192C')

    def _loc_188A(): pass

    label('loc_188A')

    ChrTalk(
        0x00FE,
        (
            '为龙的事件出动的\n',
            '主要是飞行舰队和王室亲卫队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国境师团虽然也处在警戒状态，\n',
            '但是并没有什么实质性的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，国境防备\n',
            '和往常一样还是万无一失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_192C(): pass

    label('loc_192C')

    Jump('loc_19AC')

    def _loc_192F(): pass

    label('loc_192F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_19AC',
    )

    ChrTalk(
        0x00FE,
        (
            '１０年前的战争中\n',
            '帝国突破了这里，\n',
            '入侵了利贝尔国内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为有这样的历史。\n',
            '站在这里放哨\n',
            '真是令人不禁紧张起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19AC(): pass

    label('loc_19AC')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x19B0
@scena.Code('func_0A_19B0')
def func_0A_19B0():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1BF8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 5, 0x10BD)),
            Expr.Return,
        ),
        'loc_1A74',
    )

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '终于批准退伍了。\n',
            '这下终于该和军服道别了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '虽然时间短暂，\n',
            '但军队生活也很快乐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '嗯，人生就是要这样啊。\n',
            '在军队里我对生活有了新的感悟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BF5')

    def _loc_1A74(): pass

    label('loc_1A74')

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '终于批准退伍了。\n',
            '这下终于该和军服道别了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '作为退伍的纪念，\n',
            '这本书就送给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 ９卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 ９卷'], 1)
    SetScenaFlags(ScenaFlag(0x0217, 5, 0x10BD))
    OP_0D()

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '这本书曾是我\n',
            '小小的乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '回顾起来，虽然时间短暂，\n',
            '但军队生活也很快乐呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '好了～赶快\n',
            '去领通行证吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '卡尔科斯',
        (
            '虽说路程很长，\n',
            '不过终于要出发去帝国旅行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BF5(): pass

    label('loc_1BF5')

    Jump('loc_1DFB')

    def _loc_1BF8(): pass

    label('loc_1BF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1CD3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1C4D',
    )

    ChrTalk(
        0x00FE,
        (
            '入伍到现在的薪水\n',
            '都存起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '退伍批准以后\n',
            '打算就去旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD0')

    def _loc_1C4D(): pass

    label('loc_1C4D')

    ChrTalk(
        0x00FE,
        (
            '旅费也存够了，\n',
            '我想差不多也该\n',
            '退伍了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不巧正碰上警戒状态呢。\n',
            '结果没获得批准。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这次事件\n',
            '总算平安度过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1CD0(): pass

    label('loc_1CD0')

    Jump('loc_1DFB')

    def _loc_1CD3(): pass

    label('loc_1CD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1DFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1D3C',
    )

    ChrTalk(
        0x00FE,
        (
            '我本来是为了去帝国旅行\n',
            '才到这要塞来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中途旅费用完了，\n',
            '没办法才当士兵的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DFB')

    def _loc_1D3C(): pass

    label('loc_1D3C')

    ChrTalk(
        0x00FE,
        (
            '我本来是为了去帝国旅行\n',
            '才到这要塞来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中途旅费用完了，\n',
            '没办法才当士兵的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队生活虽然严格，\n',
            '不过士兵们都是好人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，顺其自然的人生\n',
            '好像也没有以前想象中的那么差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1DFB(): pass

    label('loc_1DFB')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x1DFF
@scena.Code('func_0B_1DFF')
def func_0B_1DFF():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1F70',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1E9C',
    )

    ChrTalk(
        0x00FE,
        (
            '龙好像没受什么伤\n',
            '顺利逃走了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，为什么这次的龙\n',
            '会变得那么凶暴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个问题对于我们研究人员来说\n',
            '依然是个重大的谜题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F6D')

    def _loc_1E9C(): pass

    label('loc_1E9C')

    ChrTalk(
        0x00FE,
        (
            '龙好像没受什么伤\n',
            '顺利逃走了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为古代生物的研究人员\n',
            '对这次的事件也很不解啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有作战中拍摄的照片，\n',
            '研究就能有飞跃性的进展……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是能公开到什么程度，\n',
            '就要看我们研究人员的交涉了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_1F6D(): pass

    label('loc_1F6D')

    Jump('loc_208E')

    def _loc_1F70(): pass

    label('loc_1F70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_208E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1FD5',
    )

    ChrTalk(
        0x00FE,
        (
            '希望捕获作战\n',
            '能慎重地进行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说危害了居民，\n',
            '但龙可是无可替代的生物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_208E')

    def _loc_1FD5(): pass

    label('loc_1FD5')

    ChrTalk(
        0x00FE,
        (
            '听说由于王国军的作战\n',
            '龙逃进迷雾峡谷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想试试看能不能亲眼看到它\n',
            '我们才来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之希望军方对捕获作战\n',
            '能慎重地进行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说危害了居民，\n',
            '但龙可是无可替代的生物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_208E(): pass

    label('loc_208E')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x2092
@scena.Code('func_0C_2092')
def func_0C_2092():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Return,
        ),
        'loc_209F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_209F(): pass

    label('loc_209F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_211B',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇在前篇遇到过斯丁克】\n'),
            TXT(0x01, '【◇在前篇没遇到过斯丁克】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_210F'),
        (0x00000001, 'loc_2115'),
        (-1, 'loc_211B'),
    )

    def _loc_210F(): pass

    label('loc_210F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_211B')

    def _loc_2115(): pass

    label('loc_2115')

    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_211B')

    def _loc_211B(): pass

    label('loc_211B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_23B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Return,
        ),
        'loc_2163',
    )

    ChrTalk(
        0x00FE,
        (
            '库拉茨和亚妮拉丝\n',
            '都不在啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B9')

    def _loc_2163(): pass

    label('loc_2163')

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2231',
    )

    ChrTalk(
        0x0101,
        (
            '#1011F啊、你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '斯丁克……对吧？\n',
            '柏斯支部的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……\n',
            '那时的准游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，看样子已经升任正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2280')

    def _loc_2231(): pass

    label('loc_2231')

    ChrTalk(
        0x0101,
        (
            '#1015F（啊？这个人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（仔细看看的话，\n',
            '　竟然也戴着游击士的徽章啊？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2280(): pass

    label('loc_2280')

    ChrTalk(
        0x0106,
        (
            '#050F很久不见了，斯丁克。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '竟然来到这种地方，\n',
            '是来消灭通缉魔兽的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是来柏斯工作的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F啊啊，暂时是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过目前也只是\n',
            '帮着消灭通缉魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗……\n',
            '这附近的魔兽实在太多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F喔，就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034A, 3, 0x1A53))

    def _loc_23B9(): pass

    label('loc_23B9')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x23BD
@scena.Code('func_0D_23BD')
def func_0D_23BD():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_24A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_245A',
    )

    ChrTalk(
        0x00FE,
        (
            '稍微想了一下，敌人\n',
            '应该也不能使用枪械的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那要是这样的情况，\n',
            '就应该不会攻过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这么说来，\n',
            '只能这样去想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_24A3')

    def _loc_245A(): pass

    label('loc_245A')

    ChrTalk(
        0x00FE,
        (
            '不能使用导力枪的话，\n',
            '敌人也就不能攻过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，应该是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24A3(): pass

    label('loc_24A3')

    Jump('loc_252C')

    def _loc_24A6(): pass

    label('loc_24A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_252C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2507',
    )

    ChrTalk(
        0x00FE,
        (
            '这是怎么回事，\n',
            '到底是什么情况呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可，可恶……\n',
            '今天明明是休假的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_252C')

    def _loc_2507(): pass

    label('loc_2507')

    ChrTalk(
        0x00FE,
        (
            '可，可恶……\n',
            '今天明明是休假的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_252C(): pass

    label('loc_252C')

    TalkEnd(0x000F)

    Return()

# id: 0x000E offset: 0x2530
@scena.Code('func_0E_2530')
def func_0E_2530():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_25C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_259C',
    )

    ChrTalk(
        0x00FE,
        (
            '可恶，为什么帝国军！\n',
            '这么快就来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是没有战争\n',
            '就没有我活跃的机会了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_25C5')

    def _loc_259C(): pass

    label('loc_259C')

    ChrTalk(
        0x00FE,
        (
            '可恶，为什么帝国军！\n',
            '这么快就来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25C5(): pass

    label('loc_25C5')

    Jump('loc_2655')

    def _loc_25C8(): pass

    label('loc_25C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2655',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_262E',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵呵呵呵呵……\n',
            '这个时刻终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂，来吧帝国军！\n',
            '看我怎么收拾你们!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_2655')

    def _loc_262E(): pass

    label('loc_262E')

    ChrTalk(
        0x00FE,
        (
            '呵呵呵呵呵呵……\n',
            '喂，来吧帝国军！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2655(): pass

    label('loc_2655')

    TalkEnd(0x0010)

    Return()

# id: 0x000F offset: 0x2659
@scena.Code('func_0F_2659')
def func_0F_2659():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_26AC',
    )

    ChrTalk(
        0x00FE,
        (
            '旁，旁边这家伙\n',
            '实在是太可疑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '只能先装作听不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_273C')

    def _loc_26AC(): pass

    label('loc_26AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_273C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2715',
    )

    ChrTalk(
        0x00FE,
        (
            '旁，旁边这家伙……\n',
            '看举止好象很危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望不要扯上什么关系，\n',
            '尽量远离他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_273C')

    def _loc_2715(): pass

    label('loc_2715')

    ChrTalk(
        0x00FE,
        (
            '旁，旁边这家伙……\n',
            '看上去好可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_273C(): pass

    label('loc_273C')

    TalkEnd(0x0011)

    Return()

# id: 0x0010 offset: 0x2740
@scena.Code('func_10_2740')
def func_10_2740():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_285F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_280C',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国军来的可能性\n',
            '我想应该不大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们不能用导力兵器，\n',
            '帝国方也应该一样不能用的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且不管怎么说\n',
            '才刚刚缔结互不侵犯条约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有十分的胜算，\n',
            '我想他们不会乱来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_285C')

    def _loc_280C(): pass

    label('loc_280C')

    ChrTalk(
        0x00FE,
        (
            '帝国军来的可能性\n',
            '我想应该不大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有十分的胜算，\n',
            '我想他们不会乱来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_285C(): pass

    label('loc_285C')

    Jump('loc_2951')

    def _loc_285F(): pass

    label('loc_285F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2951',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28F5',
    )

    ChrTalk(
        0x00FE,
        (
            '变成这样的情况\n',
            '我一开始就做好准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事到如今我也\n',
            '不会丢王国军的脸的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基于作为入伍时的志愿，\n',
            '我要尽自己的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_2951')

    def _loc_28F5(): pass

    label('loc_28F5')

    ChrTalk(
        0x00FE,
        (
            '从立下志愿的时候开始\n',
            '我就已经做好准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为如此，\n',
            '我作为士兵要尽自己的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2951(): pass

    label('loc_2951')

    TalkEnd(0x0012)

    Return()

# id: 0x0011 offset: 0x2955
@scena.Code('func_11_2955')
def func_11_2955():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_29E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29B2',
    )

    ChrTalk(
        0x00FE,
        (
            '北面的平原上什么也看不见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想就这样\n',
            '平平安安地结束呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_29E5')

    def _loc_29B2(): pass

    label('loc_29B2')

    ChrTalk(
        0x00FE,
        (
            '北面的平原上有什么呢。\n',
            '从这里什么也看不见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29E5(): pass

    label('loc_29E5')

    Jump('loc_2A70')

    def _loc_29E8(): pass

    label('loc_29E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2A70',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A4F',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，那边开始\n',
            '已经是帝国的领土了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，呼……\n',
            '光是看着我就难以呼吸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_2A70')

    def _loc_2A4F(): pass

    label('loc_2A4F')

    ChrTalk(
        0x00FE,
        (
            '呼，呼……\n',
            '好象有点紧张呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A70(): pass

    label('loc_2A70')

    TalkEnd(0x0013)

    Return()

# id: 0x0012 offset: 0x2A74
@scena.Code('func_12_2A74')
def func_12_2A74():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2B82',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B19',
    )

    ChrTalk(
        0x00FE,
        (
            '现在，\n',
            '好象还没有发现帝国军进攻的动向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是对方的战车也不能动了，\n',
            '所以正不知道该怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，看来我们也\n',
            '开始疑神疑鬼了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_2B7F')

    def _loc_2B19(): pass

    label('loc_2B19')

    ChrTalk(
        0x00FE,
        (
            '现在，\n',
            '好象还没有发现帝国军进攻的动向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是对方的战车也不能动了，\n',
            '所以正不知道该怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B7F(): pass

    label('loc_2B7F')

    Jump('loc_2C36')

    def _loc_2B82(): pass

    label('loc_2B82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2C36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BF9',
    )

    ChrTalk(
        0x00FE,
        (
            '正在搬送物资的时候\n',
            '门停了下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想这时机也\n',
            '实在太巧了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话这太可疑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_2C36')

    def _loc_2BF9(): pass

    label('loc_2BF9')

    ChrTalk(
        0x00FE,
        (
            '正在搬送物资的时候\n',
            '门停了下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，真可疑呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C36(): pass

    label('loc_2C36')

    TalkEnd(0x0014)

    Return()

# id: 0x0013 offset: 0x2C3A
@scena.Code('func_13_2C3A')
def func_13_2C3A():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2CEE',
    )

    ChrTalk(
        0x00FE,
        (
            '虽为了以防万一还在继续警戒，\n',
            '但我觉得不用这样提心吊胆的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们不能用导力兵器，\n',
            '帝国方也应该一样不能用的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算出兵，\n',
            '现在这情况也是不能运送兵力的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E1D')

    def _loc_2CEE(): pass

    label('loc_2CEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2E1D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DB7',
    )

    ChrTalk(
        0x00FE,
        (
            '门一直开着的话\n',
            '在防卫上确实是个大问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个门是用防弹钢板造的。\n',
            '用人力是不可能推动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到导力器的机能恢复之前\n',
            '只能继续这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我们来说\n',
            '只有加强警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_2E1D')

    def _loc_2DB7(): pass

    label('loc_2DB7')

    ChrTalk(
        0x00FE,
        (
            '那个门是用防弹钢板造的。\n',
            '用人力是不可能推动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到导力器的机能恢复之前\n',
            '继续维持这个状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E1D(): pass

    label('loc_2E1D')

    TalkEnd(0x0015)

    Return()

# id: 0x0014 offset: 0x2E21
@scena.Code('func_14_2E21')
def func_14_2E21():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x0047, 0x0080)
    ChrClearFlags(0x0048, 0x0080)
    ChrClearFlags(0x0049, 0x0080)
    ChrClearFlags(0x004A, 0x0080)
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
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
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrClearFlags(0x004E, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0047, -4520, 0, -11180, 180)
    ChrSetPos(0x0016, -5920, 0, -13010, 0)
    ChrSetPos(0x0017, -4880, 0, -13070, 0)
    ChrSetPos(0x0018, -3760, 0, -13080, 0)
    ChrSetPos(0x0019, -6040, 0, -14600, 0)
    ChrSetPos(0x001A, -4880, -10, -14630, 0)
    ChrSetPos(0x001B, -3730, 0, -14620, 0)
    ChrSetPos(0x002E, -5930, 0, -16510, 0)
    ChrSetPos(0x002F, -4820, 0, -16500, 0)
    ChrSetPos(0x0030, -3620, 0, -16520, 0)
    ChrSetPos(0x0048, -1050, 0, -11060, 180)
    ChrSetPos(0x001C, -2210, 0, -13070, 0)
    ChrSetPos(0x001D, -1050, 0, -13020, 0)
    ChrSetPos(0x001E, -10, 0, -13090, 0)
    ChrSetPos(0x001F, -2180, 0, -14600, 0)
    ChrSetPos(0x0020, -1060, 0, -14610, 0)
    ChrSetPos(0x0021, 0, 0, -14650, 0)
    ChrSetPos(0x0031, -2150, 0, -16530, 0)
    ChrSetPos(0x0032, -1020, 0, -16510, 0)
    ChrSetPos(0x0033, 80, 0, -16500, 0)
    ChrSetPos(0x0049, 2240, 0, -11070, 180)
    ChrSetPos(0x0022, 1170, 0, -12720, 0)
    ChrSetPos(0x0023, 2150, 0, -12770, 0)
    ChrSetPos(0x0024, 3180, 0, -12700, 0)
    ChrSetPos(0x0025, 1140, 0, -14640, 0)
    ChrSetPos(0x0026, 2180, 0, -14620, 0)
    ChrSetPos(0x0027, 3210, 0, -14600, 0)
    ChrSetPos(0x0034, 1210, 0, -16570, 0)
    ChrSetPos(0x0035, 2200, 0, -16530, 0)
    ChrSetPos(0x0036, 3260, 0, -16590, 0)
    ChrSetPos(0x004A, 5410, 0, -11150, 180)
    ChrSetPos(0x0028, 4290, 0, -13090, 0)
    ChrSetPos(0x0029, 5340, 0, -13070, 0)
    ChrSetPos(0x002A, 6390, 0, -13060, 0)
    ChrSetPos(0x002B, 4370, 0, -14630, 0)
    ChrSetPos(0x002C, 5370, 0, -14640, 0)
    ChrSetPos(0x002D, 6390, 0, -14610, 0)
    ChrSetPos(0x0037, 4390, 0, -16570, 0)
    ChrSetPos(0x0038, 5310, 0, -16510, 0)
    ChrSetPos(0x0039, 6420, 0, -16530, 0)
    ChrSetPos(0x0015, -2900, 0, -18790, 180)
    ChrSetPos(0x0008, -4150, 0, -20160, 0)
    ChrSetPos(0x0009, -2970, 0, -20180, 0)
    ChrSetPos(0x000A, -1750, -10, -20160, 0)
    ChrSetPos(0x000B, -4100, 0, -22060, 0)
    ChrSetPos(0x000C, -2920, 0, -22000, 0)
    ChrSetPos(0x000F, -1710, 10, -22060, 0)
    ChrSetPos(0x0010, -4110, -10, -23710, 0)
    ChrSetPos(0x0011, -2930, 10, -23790, 0)
    ChrSetPos(0x0012, -1760, 0, -23740, 0)
    CreateThread(0x0015, 0x00, 0x00, func_02_B68)
    CreateThread(0x0009, 0x00, 0x00, func_02_B68)
    CreateThread(0x000A, 0x00, 0x00, func_02_B68)
    CreateThread(0x000B, 0x00, 0x00, func_02_B68)
    CreateThread(0x000C, 0x00, 0x00, func_02_B68)
    CreateThread(0x000F, 0x00, 0x00, func_02_B68)
    CreateThread(0x0010, 0x00, 0x00, func_02_B68)
    CreateThread(0x0011, 0x00, 0x00, func_02_B68)
    CreateThread(0x0012, 0x00, 0x00, func_02_B68)
    ChrSetPos(0x004B, 870, -10, -18600, 180)
    ChrSetPos(0x0013, -360, -30, -20250, 0)
    ChrSetPos(0x0014, 690, -30, -20200, 0)
    ChrSetPos(0x003A, 1960, 0, -20330, 0)
    ChrSetPos(0x003B, -370, 10, -22080, 0)
    ChrSetPos(0x003C, 780, 10, -22010, 0)
    ChrSetPos(0x003D, 1970, 10, -22010, 0)
    ChrSetPos(0x003E, -290, 0, -23840, 0)
    ChrSetPos(0x003F, 820, 0, -23860, 0)
    ChrSetPos(0x0040, 1970, 10, -23820, 0)
    CreateThread(0x0013, 0x00, 0x00, func_02_B68)
    CreateThread(0x0014, 0x00, 0x00, func_02_B68)
    CreateThread(0x0015, 0x00, 0x00, func_02_B68)
    ChrSetPos(0x004C, 4560, 30, -18680, 180)
    ChrSetPos(0x0041, 3390, 20, -20080, 0)
    ChrSetPos(0x0042, 4570, 0, -20160, 0)
    ChrSetPos(0x0043, 5840, 30, -20190, 0)
    ChrSetPos(0x0044, 3430, 10, -22080, 0)
    ChrSetPos(0x0045, 4630, 10, -22040, 0)
    ChrSetPos(0x0046, 5900, 0, -22070, 0)
    ChrSetPos(0x000E, 3410, 10, -23910, 0)
    ChrSetPos(0x004D, 4640, -10, -23920, 0)
    ChrSetPos(0x004E, 5860, 0, -23900, 0)
    ChrSetChipByIndex(0x000E, 0)
    ChrSetChipByIndex(0x004D, 0)
    ChrSetChipByIndex(0x004E, 0)
    OP_4A(0x0047, 255)
    OP_4A(0x0048, 255)
    OP_4A(0x0049, 255)
    OP_4A(0x004A, 255)
    OP_4A(0x004B, 255)
    OP_4A(0x004C, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    OP_4A(0x001F, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0021, 255)
    OP_4A(0x0022, 255)
    OP_4A(0x0023, 255)
    OP_4A(0x0024, 255)
    OP_4A(0x0025, 255)
    OP_4A(0x0026, 255)
    OP_4A(0x0027, 255)
    OP_4A(0x0028, 255)
    OP_4A(0x0029, 255)
    OP_4A(0x002A, 255)
    OP_4A(0x002B, 255)
    OP_4A(0x002C, 255)
    OP_4A(0x002D, 255)
    OP_4A(0x002E, 255)
    OP_4A(0x002F, 255)
    OP_4A(0x0030, 255)
    OP_4A(0x0031, 255)
    OP_4A(0x0032, 255)
    OP_4A(0x0033, 255)
    OP_4A(0x0034, 255)
    OP_4A(0x0035, 255)
    OP_4A(0x0036, 255)
    OP_4A(0x0037, 255)
    OP_4A(0x0038, 255)
    OP_4A(0x0039, 255)
    OP_4A(0x003A, 255)
    OP_4A(0x003B, 255)
    OP_4A(0x003C, 255)
    OP_4A(0x003D, 255)
    OP_4A(0x003E, 255)
    OP_4A(0x003F, 255)
    OP_4A(0x0040, 255)
    OP_4A(0x0041, 255)
    OP_4A(0x0042, 255)
    OP_4A(0x0043, 255)
    OP_4A(0x0044, 255)
    OP_4A(0x0045, 255)
    OP_4A(0x0046, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x004D, 255)
    OP_4A(0x004E, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    ChrSetFlags(0x0047, 0x0040)
    ChrSetFlags(0x0048, 0x0040)
    ChrSetFlags(0x0049, 0x0040)
    ChrSetFlags(0x004A, 0x0040)
    ChrSetFlags(0x004B, 0x0040)
    ChrSetFlags(0x004C, 0x0040)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0018, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x001A, 0x0040)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x001D, 0x0040)
    ChrSetFlags(0x001E, 0x0040)
    ChrSetFlags(0x001F, 0x0040)
    ChrSetFlags(0x0020, 0x0040)
    ChrSetFlags(0x0021, 0x0040)
    ChrSetFlags(0x0022, 0x0040)
    ChrSetFlags(0x0023, 0x0040)
    ChrSetFlags(0x0024, 0x0040)
    ChrSetFlags(0x0025, 0x0040)
    ChrSetFlags(0x0026, 0x0040)
    ChrSetFlags(0x0027, 0x0040)
    ChrSetFlags(0x0028, 0x0040)
    ChrSetFlags(0x0029, 0x0040)
    ChrSetFlags(0x002A, 0x0040)
    ChrSetFlags(0x002B, 0x0040)
    ChrSetFlags(0x002C, 0x0040)
    ChrSetFlags(0x002D, 0x0040)
    ChrSetFlags(0x002E, 0x0040)
    ChrSetFlags(0x002F, 0x0040)
    ChrSetFlags(0x0030, 0x0040)
    ChrSetFlags(0x0031, 0x0040)
    ChrSetFlags(0x0032, 0x0040)
    ChrSetFlags(0x0033, 0x0040)
    ChrSetFlags(0x0034, 0x0040)
    ChrSetFlags(0x0035, 0x0040)
    ChrSetFlags(0x0036, 0x0040)
    ChrSetFlags(0x0037, 0x0040)
    ChrSetFlags(0x0038, 0x0040)
    ChrSetFlags(0x0039, 0x0040)
    ChrSetFlags(0x003A, 0x0040)
    ChrSetFlags(0x003B, 0x0040)
    ChrSetFlags(0x003C, 0x0040)
    ChrSetFlags(0x003D, 0x0040)
    ChrSetFlags(0x003E, 0x0040)
    ChrSetFlags(0x003F, 0x0040)
    ChrSetFlags(0x0040, 0x0040)
    ChrSetFlags(0x0041, 0x0040)
    ChrSetFlags(0x0042, 0x0040)
    ChrSetFlags(0x0043, 0x0040)
    ChrSetFlags(0x0044, 0x0040)
    ChrSetFlags(0x0045, 0x0040)
    ChrSetFlags(0x0046, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x004D, 0x0040)
    ChrSetFlags(0x004E, 0x0040)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    CameraMove(0, -500, -17000, 0)
    OP_67(0, 4980, -10000, 0)
    CameraSetDistance(2100, 0)
    OP_6C(334000, 0)
    OP_6E(538, 0)

    @scena.Lambda('lambda_376B')
    def lambda_376B():
        CameraMove(-3500, 1000, -3000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_376B)

    @scena.Lambda('lambda_3783')
    def lambda_3783():
        OP_67(0, 3500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3783)

    @scena.Lambda('lambda_379B')
    def lambda_379B():
        CameraSetDistance(3000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_379B)

    @scena.Lambda('lambda_37AB')
    def lambda_37AB():
        OP_6E(550, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_37AB)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(4000)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1402._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x37E2
@scena.Code('func_15_37E2')
def func_15_37E2():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    LoadChip('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP', 5)
    LoadChip('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP', 6)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x004D, 5)
    ChrSetChipByIndex(0x004E, 6)
    ChrSetPos(0x004E, -500, 11750, -3000, 180)
    ChrSetPos(0x004D, 500, 11750, -3000, 180)
    ChrClearFlags(0x004D, 0x0080)
    ChrClearFlags(0x004E, 0x0080)
    CameraMove(630, 11750, -1740, 0)
    OP_67(0, 5040, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x004D,
        (
            '#0160381126V#1128F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x004E, 90, 400)
    Sleep(500)

    ChrTalk(
        0x004E,
        (
            '#0600381127V#166F#6P这样好吗……卡西乌斯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600381128V既然那么担心的话，\n',
            '跟着一起去不就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x004D, 270, 400)
    Sleep(400)

    ChrTalk(
        0x004D,
        (
            '#0160381129V#1125F#2P不，还是算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381130V#1122F那个叫怀斯曼的男人……\n',
            '危险程度超乎我的想象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381131V如果我也一起同行的话，\n',
            '恐怕他就会不择手段了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x004E,
        (
            '#0600381132V#163F#6P你是怕他会用最极端的手段吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600381133V#165F……哎呀哎呀。\n',
            '对方似乎很看重你的能力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x004D,
        (
            '#0160381134V#1123F#2P我才不希望被他们看重呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381135V#1120F不过，反过来说，\n',
            '这样我们才有了抓住空隙的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x004E,
        (
            '#0600381136V#163F#6P虚虚实实地互相试探吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600381137V#160F『铁血宰相』那边怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x004D,
        (
            '#0160381138V#1122F#2P那位宰相大人依旧还是\n',
            '那么麻烦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381139V#1125F嗯，不过只要我们不露出破绽，\n',
            '应该也就没什么问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x004E,
        (
            '#0600381140V#166F#6P嗯，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600381141V#163F全部事情就交给\n',
            '『埃尔赛尤』上的那帮人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x004D,
        (
            '#0160381142V#1128F#2P啊…唉…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x004D, 180, 400)

    @scena.Lambda('lambda_3C60')
    def lambda_3C60():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x004E, 0x0001, lambda_3C60)

    Sleep(500)

    ChrTalk(
        0x004D,
        (
            '#0160381143V#1122F#5P（莱娜……还有空之女神呀……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381144V（请为那些孩子\n',
            '  指明前进的方向吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160381145V#1125F（在这广阔的天空下……\n',
            '  希望他们能找到自己的道路。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0411, 7, 0x208F))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x12A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS158._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    CameraMove(-162160, 0, -33060, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x15, 0x0000, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB0',
    )

    ShowSaveMenu()

    def _loc_3DB0(): pass

    label('loc_3DB0')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    OP_20(0x00001388)
    Sleep(2000)

    OP_21()
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    ClearScenaFlags(ScenaFlag(0x0411, 7, 0x208F))
    MapClearFlags(0x00100000)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
