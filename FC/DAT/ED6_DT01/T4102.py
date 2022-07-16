import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '奈尔'),
    TXT(0x02, '士兵'),
    TXT(0x03, '士兵'),
    TXT(0x04, '士兵'),
    TXT(0x05, '士兵'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '鸽子'),
    TXT(0x09, '鸽子'),
    TXT(0x0A, '鸽子'),
    TXT(0x0B, '鸽子'),
    TXT(0x0C, '鸽子'),
    TXT(0x0D, '鸽子'),
    TXT(0x0E, '鸽子'),
    TXT(0x0F, '鸽子'),
    TXT(0x10, '鸽子'),
    TXT(0x11, '鸽子'),
    TXT(0x12, '阿鲁姆'),
    TXT(0x13, '艾娅莉'),
    TXT(0x14, '达丽娅'),
    TXT(0x15, '菲利奥'),
    TXT(0x16, '拉科舒'),
    TXT(0x17, '士兵达登'),
    TXT(0x18, '比卡'),
    TXT(0x19, '夏妮'),
    TXT(0x1A, '士兵'),
    TXT(0x1B, '士兵'),
    TXT(0x1C, '士兵'),
    TXT(0x1D, '特务兵'),
    TXT(0x1E, '特务兵'),
    TXT(0x1F, '莉安妮'),
    TXT(0x20, '游客'),
    TXT(0x21, '游客'),
    TXT(0x22, '游客'),
    TXT(0x23, '游客'),
    TXT(0x24, '游客'),
    TXT(0x25, '游客'),
    TXT(0x26, '游客'),
    TXT(0x27, '游客'),
    TXT(0x28, '游客'),
    TXT(0x29, '鸽子'),
    TXT(0x2A, '鸽子'),
    TXT(0x2B, '鸽子'),
    TXT(0x2C, '鸽子'),
    TXT(0x2D, '鸽子'),
    TXT(0x2E, '鸽子'),
    TXT(0x2F, '鸽子'),
    TXT(0x30, '王都格兰赛尔·北街区'),
    TXT(0x31, '王都格兰赛尔·南街区'),
    TXT(0x32, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4102.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4285
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFEC780,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01731._CH', 'ED6_DT07/CH01731P._CP'),
    ]

# id: 0x10002 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0024,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0025,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0026,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0027,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0028,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0029,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -55940,
            z                   = 250,
            y                   = 30,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = -58170,
            z                   = -3500,
            y                   = -16100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -59550,
            z                   = -3500,
            y                   = -16100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -88950,
            z                   = 0,
            y                   = -3950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -78290,
            z                   = 0,
            y                   = -2530,
            direction           = 180,
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
            x                   = -40940,
            z                   = 0,
            y                   = -5120,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -55400,
            z                   = 0,
            y                   = -3050,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -78990,
            z                   = 1250,
            y                   = 8029,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -62950,
            z                   = -3750,
            y                   = -31290,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -55890,
            z                   = 0,
            y                   = -1830,
            direction           = 185,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -78990,
            z                   = 1250,
            y                   = 8029,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -55990,
            z                   = 250,
            y                   = -1280,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = -58060,
            z                   = -3250,
            y                   = -23920,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -60050,
            z                   = -3250,
            y                   = -24510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = -58590,
            z                   = -3250,
            y                   = -22150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -55610,
            z                   = -3750,
            y                   = -27100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = -60830,
            z                   = -3500,
            y                   = -28840,
            direction           = 204,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = -61010,
            z                   = 250,
            y                   = -870,
            direction           = 189,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = -82230,
            z                   = 250,
            y                   = 4330,
            direction           = 41,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = -79740,
            z                   = 250,
            y                   = 4870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = -78570,
            z                   = 250,
            y                   = 4270,
            direction           = 4,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -39960,
            z                   = 0,
            y                   = 43920,
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
        ScenaNpcData(
            x                   = -7520,
            z                   = 300,
            y                   = -20000,
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

# id: 0x10003 offset: 0x78A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x78A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -82190,
            y           = 0,
            z           = 123740,
            range       = -75710,
            dword_10    = 0x00000BB8,
            dword_14    = 0x0000292C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000002A,
        ),
        ScenaEventData(
            x           = -63040,
            y           = -3750,
            z           = -33480,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000030,
        ),
        ScenaEventData(
            x           = -63390,
            y           = -3750,
            z           = -24940,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000031,
        ),
        ScenaEventData(
            x           = -78840,
            y           = 1250,
            z           = 12430,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000032,
        ),
    )

# id: 0x10005 offset: 0x80A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -76990,
            triggerZ            = -3500,
            triggerY            = -30450,
            triggerRange        = 800,
            actorX              = -76990,
            actorZ              = -2500,
            actorY              = -30450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -92000,
            triggerZ            = 800,
            triggerY            = -4000,
            triggerRange        = 800,
            actorX              = -92000,
            actorZ              = 1800,
            actorY              = -4000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -72220,
            triggerZ            = -3180,
            triggerY            = -15630,
            triggerRange        = 800,
            actorX              = -72220,
            actorZ              = -2000,
            actorY              = -15630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x876
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_884',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0021)

    def _loc_884(): pass

    label('loc_884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_8A0',
    )

    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x002B)

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_8FF',
    )

    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0027, 0x0080)
    ClearChrFlags(0x0028, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002B, 0x0010)
    ClearChrFlags(0x002C, 0x0080)
    ClearChrFlags(0x002D, 0x0080)
    ClearChrFlags(0x002E, 0x0080)
    SetChrFlags(0x002E, 0x0010)
    ClearChrFlags(0x002F, 0x0080)
    SetChrFlags(0x002F, 0x0010)

    Jump('loc_A08')

    def _loc_8FF(): pass

    label('loc_8FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_913',
    )

    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)

    Jump('loc_A08')

    def _loc_913(): pass

    label('loc_913')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_92C',
    )

    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)

    Jump('loc_A08')

    def _loc_92C(): pass

    label('loc_92C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_94A',
    )

    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)

    Jump('loc_A08')

    def _loc_94A(): pass

    label('loc_94A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_963',
    )

    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0026, 0x0080)

    Jump('loc_A08')

    def _loc_963(): pass

    label('loc_963')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_9A8',
    )

    ClearChrFlags(0x0019, 0x0080)
    SetChrPos(0x0019, -85310, 0, -4390, 270)
    ClearChrFlags(0x001A, 0x0080)
    SetChrPos(0x001A, -84980, 0, -3470, 270)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)

    Jump('loc_A08')

    def _loc_9A8(): pass

    label('loc_9A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_9E3',
    )

    ClearChrFlags(0x0019, 0x0080)
    SetChrPos(0x0019, -79040, 500, 6080, 0)
    SetChrFlags(0x0019, 0x0010)
    ClearChrFlags(0x001A, 0x0080)
    SetChrPos(0x001A, -79040, 1250, 7750, 180)

    Jump('loc_A08')

    def _loc_9E3(): pass

    label('loc_9E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_9ED',
    )

    Jump('loc_A08')

    def _loc_9ED(): pass

    label('loc_9ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_9F7',
    )

    Jump('loc_A08')

    def _loc_9F7(): pass

    label('loc_9F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_A01',
    )

    Jump('loc_A08')

    def _loc_A01(): pass

    label('loc_A01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_A08',
    )

    def _loc_A08(): pass

    label('loc_A08')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_A14'),
        (-1, 'loc_A1A'),
    )

    def _loc_A14(): pass

    label('loc_A14')

    SetScenaFlags(ScenaFlag(0x00C4, 2, 0x622))

    Jump('loc_A1A')

    def _loc_A1A(): pass

    label('loc_A1A')

    Return()

# id: 0x0001 offset: 0xA1B
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -185000, -131000, 196701)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A60',
    )

    OP_B1('t4102_y')

    Jump('loc_A69')

    def _loc_A60(): pass

    label('loc_A60')

    OP_B1('t4102_n')

    def _loc_A69(): pass

    label('loc_A69')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 2, 0x622)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A82',
    )

    OP_72(0x000A, 0x0010)
    OP_65(0x00, 0x0001)

    def _loc_A82(): pass

    label('loc_A82')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A95',
    )

    OP_1B(0x03, 0x00, 0x002D)

    def _loc_A95(): pass

    label('loc_A95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_ADA',
    )

    OP_72(0x000E, 0x0008)
    OP_72(0x000E, 0x0020)
    OP_72(0x000E, 0x0002)
    OP_6F(0x000E, 0)
    OP_72(0x000B, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0007, 0x0010)
    OP_72(0x000D, 0x0010)
    OP_72(0x0005, 0x0010)
    OP_72(0x0009, 0x0010)
    OP_72(0x000A, 0x0010)

    def _loc_ADA(): pass

    label('loc_ADA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B38',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    CreateThread(0x0009, 0x01, 0x00, 0x0023)
    CreateThread(0x000A, 0x01, 0x00, 0x0023)
    CreateThread(0x000B, 0x01, 0x00, 0x0023)
    CreateThread(0x000C, 0x01, 0x00, 0x0023)
    CreateThread(0x000D, 0x01, 0x00, 0x0023)
    CreateThread(0x000E, 0x01, 0x00, 0x0023)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B38(): pass

    label('loc_B38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_B96',
    )

    OP_72(0x0010, 0x0004)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0x00, 'map\\\\mp016_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -63240, -3240, -25080, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_B96(): pass

    label('loc_B96')

    Return()

# id: 0x0002 offset: 0xB97
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0003,
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
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BBC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_CFE')

    def _loc_BBC(): pass

    label('loc_BBC')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BD5',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_CFE')

    def _loc_BD5(): pass

    label('loc_BD5')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BEE',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_CFE')

    def _loc_BEE(): pass

    label('loc_BEE')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C07',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_CFE')

    def _loc_C07(): pass

    label('loc_C07')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C20',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_CFE')

    def _loc_C20(): pass

    label('loc_C20')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C39',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_CFE')

    def _loc_C39(): pass

    label('loc_C39')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C52',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_CFE')

    def _loc_C52(): pass

    label('loc_C52')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C6B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_CFE')

    def _loc_C6B(): pass

    label('loc_C6B')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C84',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_CFE')

    def _loc_C84(): pass

    label('loc_C84')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C9D',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_CFE')

    def _loc_C9D(): pass

    label('loc_C9D')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB6',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_CFE')

    def _loc_CB6(): pass

    label('loc_CB6')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CCF',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_CFE')

    def _loc_CCF(): pass

    label('loc_CCF')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE8',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_CFE')

    def _loc_CE8(): pass

    label('loc_CE8')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CFE',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_CFE(): pass

    label('loc_CFE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D13',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_CFE')

    def _loc_D13(): pass

    label('loc_D13')

    Return()

# id: 0x0003 offset: 0xD14
@scena.Code('func_03_D14')
def func_03_D14():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D98',
    )

    ChrWalkTo(0x00FE, -39990, 0, -3050, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(1500)

    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -55010, 0, -3050, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -55910, 0, -3050, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(1500)

    SetChrDirection(0x00FE, 270, 400)
    Sleep(1500)

    Jump('func_03_D14')

    def _loc_D98(): pass

    label('loc_D98')

    Return()

# id: 0x0004 offset: 0xD99
@scena.Code('func_04_D99')
def func_04_D99():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E25',
    )

    ChrWalkTo(0x00FE, -76010, 1250, 8029, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -78990, 1250, 8029, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -81900, 1250, 8029, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -78990, 1250, 8029, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    Jump('func_04_D99')

    def _loc_E25(): pass

    label('loc_E25')

    Return()

# id: 0x0005 offset: 0xE26
@scena.Code('func_05_E26')
def func_05_E26():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EB6',
    )

    ChrWalkTo(0x00FE, -57420, -3750, -31290, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    SetChrDirection(0x00FE, 0, 400)
    Sleep(1500)

    SetChrDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -68110, -3750, -31290, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1500)

    SetChrDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -62990, -3750, -31290, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(3000)

    Jump('func_05_E26')

    def _loc_EB6(): pass

    label('loc_EB6')

    Return()

# id: 0x0006 offset: 0xEB7
@scena.Code('func_06_EB7')
def func_06_EB7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EDA',
    )

    OP_8D(0x00FE, -83110, 1920, -74690, -5430, 3000)

    Jump('func_06_EB7')

    def _loc_EDA(): pass

    label('loc_EDA')

    Return()

# id: 0x0007 offset: 0xEDB
@scena.Code('func_07_EDB')
def func_07_EDB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F37',
    )

    ChrWalkTo(0x00FE, -40940, 0, -36580, 2500, 0x00)
    ChrWalkTo(0x00FE, -54190, -3750, -36230, 2500, 0x00)
    ChrWalkTo(0x00FE, -54260, 0, -4990, 2500, 0x00)
    ChrWalkTo(0x00FE, -40940, 0, -5120, 2500, 0x00)

    Jump('func_07_EDB')

    def _loc_F37(): pass

    label('loc_F37')

    Return()

# id: 0x0008 offset: 0xF38
@scena.Code('func_08_F38')
def func_08_F38():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F5B',
    )

    OP_8D(0x00FE, -59380, 250, -52780, -3730, 3000)

    Jump('func_08_F38')

    def _loc_F5B(): pass

    label('loc_F5B')

    Return()

# id: 0x0009 offset: 0xF5C
@scena.Code('func_09_F5C')
def func_09_F5C():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, -74920, -1510, -82870, 5610, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F90(): pass

    label('loc_F90')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_115E',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1127',
    )

    TerminateThread(0x00FE, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1017',
    )

    @scena.Lambda('lambda_0FFB')
    def lambda_0FFB():
        OP_97(0x00FE, -78980, 14630, 360000, 7000, 0x0001)
        Yield()

        Jump('lambda_0FFB')

    DispatchAsync2(0x00FE, 0x0001, lambda_0FFB)

    Jump('loc_1036')

    def _loc_1017(): pass

    label('loc_1017')

    @scena.Lambda('lambda_101D')
    def lambda_101D():
        OP_97(0x00FE, -78980, 14630, -360000, 7000, 0x0001)
        Yield()

        Jump('lambda_101D')

    DispatchAsync2(0x00FE, 0x0001, lambda_101D)

    def _loc_1036(): pass

    label('loc_1036')

    SetChrChipByIndex(0x00FE, 22)
    ClearChrFlags(0x00FE, 0x0400)
    SetChrFlags(0x00FE, 0x0004)
    def _loc_1045(): pass

    label('loc_1045')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_107D',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xC8),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x2328),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1075',
    )

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

    Jump('loc_107D')

    def _loc_1075(): pass

    label('loc_1075')

    Sleep(15)

    Jump('loc_1045')

    def _loc_107D(): pass

    label('loc_107D')

    SetChrFlags(0x00FE, 0x0080)
    TerminateThread(0x00FE, 0x01)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrPos(0x00FE, -78690, 0, -40, 74)
    def _loc_109C(): pass

    label('loc_109C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1124',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_111C',
    )

    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 23)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, -74920, -1510, -82870, 5610, 0)

    Jump('loc_1124')

    def _loc_111C(): pass

    label('loc_111C')

    Sleep(500)

    Jump('loc_109C')

    def _loc_1124(): pass

    label('loc_1124')

    Jump('loc_115B')

    def _loc_1127(): pass

    label('loc_1127')

    Sleep(100)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x14),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_115B',
    )

    @scena.Lambda('lambda_1143')
    def lambda_1143():
        OP_8D(0x00FE, -74920, -1510, -82870, 5610, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1143)

    def _loc_115B(): pass

    label('loc_115B')

    Jump('loc_F90')

    def _loc_115E(): pass

    label('loc_115E')

    Return()

# id: 0x000A offset: 0x115F
@scena.Code('func_0A_115F')
def func_0A_115F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_11C8',
    )

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军的孙女\n',
            '也被捉去做了人质呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那位理查德上校\n',
            '原来是这么心狠手辣的人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134D')

    def _loc_11C8(): pass

    label('loc_11C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_11D2',
    )

    Jump('loc_134D')

    def _loc_11D2(): pass

    label('loc_11D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1239',
    )

    ChrTalk(
        0x00FE,
        (
            '这家人的女孩子\n',
            '似乎一直未回家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经向本部\n',
            '报告了这个情况，\n',
            '希望早日能找到她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134D')

    def _loc_1239(): pass

    label('loc_1239')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_12D4',
    )

    ChrTalk(
        0x00FE,
        (
            '今天白天难得\n',
            '获得了一次休息机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏这样，\n',
            '我的身体得到了充分休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '为什么只让我休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样很对不起其他人的呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134D')

    def _loc_12D4(): pass

    label('loc_12D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_12DE',
    )

    Jump('loc_134D')

    def _loc_12DE(): pass

    label('loc_12DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_131E',
    )

    ChrTalk(
        0x00FE,
        (
            '据说摩尔根将军\n',
            '为了对付恐怖分子，\n',
            '忙得不可开交。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134D')

    def _loc_131E(): pass

    label('loc_131E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1328',
    )

    Jump('loc_134D')

    def _loc_1328(): pass

    label('loc_1328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1332',
    )

    Jump('loc_134D')

    def _loc_1332(): pass

    label('loc_1332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_133C',
    )

    Jump('loc_134D')

    def _loc_133C(): pass

    label('loc_133C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1346',
    )

    Jump('loc_134D')

    def _loc_1346(): pass

    label('loc_1346')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_134D',
    )

    def _loc_134D(): pass

    label('loc_134D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1351
@scena.Code('func_0B_1351')
def func_0B_1351():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1391',
    )

    ChrTalk(
        0x00FE,
        (
            '王都的戒备果然还是\n',
            '由我们王都守卫队来做合适！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1613')

    def _loc_1391(): pass

    label('loc_1391')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_139B',
    )

    Jump('loc_1613')

    def _loc_139B(): pass

    label('loc_139B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_13F9',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下的病况如何\n',
            '连我们也不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，\n',
            '还是像平常一样继续警戒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1613')

    def _loc_13F9(): pass

    label('loc_13F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1503',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1470',
    )

    ChrTalk(
        0x00FE,
        (
            '就算发现亲卫队的人，\n',
            '我也不想和他们战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来都是王国军的队伍，\n',
            '而且我想我们也打不过他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1500')

    def _loc_1470(): pass

    label('loc_1470')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '就算发现亲卫队的人，\n',
            '我也不想和他们战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来都是王国军的队伍，\n',
            '而且我想我们也打不过他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们要是能投降\n',
            '就帮了我们大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1500(): pass

    label('loc_1500')

    Jump('loc_1613')

    def _loc_1503(): pass

    label('loc_1503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_15B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_154B',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才，这里的一位修女\n',
            '向我打招呼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B2')

    def _loc_154B(): pass

    label('loc_154B')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才，这里的一位修女\n',
            '向我打招呼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好的，为了王都的和平，\n',
            '我也要好好努力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15B2(): pass

    label('loc_15B2')

    Jump('loc_1613')

    def _loc_15B5(): pass

    label('loc_15B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_15E4',
    )

    ChrTalk(
        0x00FE,
        (
            '上头命令\n',
            '要定时巡逻重要的设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1613')

    def _loc_15E4(): pass

    label('loc_15E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_15EE',
    )

    Jump('loc_1613')

    def _loc_15EE(): pass

    label('loc_15EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_15F8',
    )

    Jump('loc_1613')

    def _loc_15F8(): pass

    label('loc_15F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1602',
    )

    Jump('loc_1613')

    def _loc_1602(): pass

    label('loc_1602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_160C',
    )

    Jump('loc_1613')

    def _loc_160C(): pass

    label('loc_160C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1613',
    )

    def _loc_1613(): pass

    label('loc_1613')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1617
@scena.Code('func_0C_1617')
def func_0C_1617():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1670',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的残党\n',
            '有可能会袭击这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这段时间还是要\n',
            '继续加强戒备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1814')

    def _loc_1670(): pass

    label('loc_1670')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_167A',
    )

    Jump('loc_1814')

    def _loc_167A(): pass

    label('loc_167A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_16D2',
    )

    ChrTalk(
        0x00FE,
        (
            '从刚才起这里的员工\n',
            '就一直慌慌张张的，\n',
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真让人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1814')

    def _loc_16D2(): pass

    label('loc_16D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1723',
    )

    ChrTalk(
        0x00FE,
        (
            '已经傍晚了呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '马上就是换班时间了，\n',
            '今晚我还要值班巡逻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1814')

    def _loc_1723(): pass

    label('loc_1723')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_177D',
    )

    ChrTalk(
        0x00FE,
        (
            '我叫刚才出来的女孩\n',
            '帮我拍了一张照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她对我说\n',
            '『叔叔，你很可爱哦』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1814')

    def _loc_177D(): pass

    label('loc_177D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_17E5',
    )

    ChrTalk(
        0x00FE,
        (
            '来这里有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在监控这里的员工。\n',
            '上头不知道出于什么原因\n',
            '下达了这样的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1814')

    def _loc_17E5(): pass

    label('loc_17E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_17EF',
    )

    Jump('loc_1814')

    def _loc_17EF(): pass

    label('loc_17EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_17F9',
    )

    Jump('loc_1814')

    def _loc_17F9(): pass

    label('loc_17F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1803',
    )

    Jump('loc_1814')

    def _loc_1803(): pass

    label('loc_1803')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_180D',
    )

    Jump('loc_1814')

    def _loc_180D(): pass

    label('loc_180D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1814',
    )

    def _loc_1814(): pass

    label('loc_1814')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1818
@scena.Code('func_0D_1818')
def func_0D_1818():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1825',
    )

    Jump('loc_18D4')

    def _loc_1825(): pass

    label('loc_1825')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_187D',
    )

    ChrTalk(
        0x00FE,
        (
            '你们是……\n',
            '好像是武术大会的优胜者吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不要做出什么\n',
            '可疑的行动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18D4')

    def _loc_187D(): pass

    label('loc_187D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1887',
    )

    Jump('loc_18D4')

    def _loc_1887(): pass

    label('loc_1887')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1891',
    )

    Jump('loc_18D4')

    def _loc_1891(): pass

    label('loc_1891')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_189B',
    )

    Jump('loc_18D4')

    def _loc_189B(): pass

    label('loc_189B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_18A5',
    )

    Jump('loc_18D4')

    def _loc_18A5(): pass

    label('loc_18A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_18AF',
    )

    Jump('loc_18D4')

    def _loc_18AF(): pass

    label('loc_18AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_18B9',
    )

    Jump('loc_18D4')

    def _loc_18B9(): pass

    label('loc_18B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_18C3',
    )

    Jump('loc_18D4')

    def _loc_18C3(): pass

    label('loc_18C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_18CD',
    )

    Jump('loc_18D4')

    def _loc_18CD(): pass

    label('loc_18CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_18D4',
    )

    def _loc_18D4(): pass

    label('loc_18D4')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x18D8
@scena.Code('func_0E_18D8')
def func_0E_18D8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_18E5',
    )

    Jump('loc_1992')

    def _loc_18E5(): pass

    label('loc_18E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_193B',
    )

    ChrTalk(
        0x00FE,
        (
            '王城里有洛伦斯队长把守，\n',
            '自然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市街区这里\n',
            '就交给我们吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1992')

    def _loc_193B(): pass

    label('loc_193B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1945',
    )

    Jump('loc_1992')

    def _loc_1945(): pass

    label('loc_1945')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_194F',
    )

    Jump('loc_1992')

    def _loc_194F(): pass

    label('loc_194F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1959',
    )

    Jump('loc_1992')

    def _loc_1959(): pass

    label('loc_1959')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1963',
    )

    Jump('loc_1992')

    def _loc_1963(): pass

    label('loc_1963')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_196D',
    )

    Jump('loc_1992')

    def _loc_196D(): pass

    label('loc_196D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1977',
    )

    Jump('loc_1992')

    def _loc_1977(): pass

    label('loc_1977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1981',
    )

    Jump('loc_1992')

    def _loc_1981(): pass

    label('loc_1981')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_198B',
    )

    Jump('loc_1992')

    def _loc_198B(): pass

    label('loc_198B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1992',
    )

    def _loc_1992(): pass

    label('loc_1992')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1996
@scena.Code('func_0F_1996')
def func_0F_1996():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1A14',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下和科洛蒂娅公主，\n',
            '她们二位看起来都很有精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过没有见到\n',
            '杜南公爵的身影啊，\n',
            '这是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1A14(): pass

    label('loc_1A14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1A3A',
    )

    ChrTalk(
        0x00FE,
        (
            '发、发生了什么事吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1A3A(): pass

    label('loc_1A3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1AB1',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典上至少\n',
            '要见一见科洛蒂娅公主的\n',
            '美妙英姿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她非常乖巧可爱哦。\n',
            '我要是有这么一个女儿就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1AB1(): pass

    label('loc_1AB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1B0C',
    )

    ChrTalk(
        0x00FE,
        (
            '今年因为到处有士兵的缘故，\n',
            '所以没有什么闹事的人出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样倒也不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1B0C(): pass

    label('loc_1B0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1B63',
    )

    ChrTalk(
        0x00FE,
        (
            '每年大会的最后一天，\n',
            '大街肯定会非常的热闹的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道今年会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1B63(): pass

    label('loc_1B63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1BB6',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，已经傍晚了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，年纪一大，\n',
            '觉得一天过得都很快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1BB6(): pass

    label('loc_1BB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1C20',
    )

    ChrTalk(
        0x00FE,
        (
            '在武术大会进行的时候，\n',
            '我就去百货商店看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比赛期间店里面比较清静，\n',
            '感觉很舒畅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1C20(): pass

    label('loc_1C20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1C49',
    )

    ChrTalk(
        0x00FE,
        (
            '必须快点\n',
            '回家准备晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1C49(): pass

    label('loc_1C49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1CAD',
    )

    ChrTalk(
        0x00FE,
        (
            '今年武术大会的门票不打折，\n',
            '这可怎么办好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买不起门票，\n',
            '这次就只有不去看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1CAD(): pass

    label('loc_1CAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1D61',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下身体欠佳，\n',
            '却要召开武术大会，\n',
            '乐趣也会减半。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '主办人又是那个差劲的杜南公爵，\n',
            '有种让人说不出来的滋味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校还要当这种人的助手，\n',
            '真是难为他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBC')

    def _loc_1D61(): pass

    label('loc_1D61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1DBC',
    )

    ChrTalk(
        0x00FE,
        (
            '听说有恐怖事件，\n',
            '是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我而言，\n',
            '只要不导致物价上涨就万事大吉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DBC(): pass

    label('loc_1DBC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1DC0
@scena.Code('func_10_1DC0')
def func_10_1DC0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1E00',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～诞辰庆典顺利举行了，\n',
            '终于让我松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B6')

    def _loc_1E00(): pass

    label('loc_1E00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1EF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1E6D',
    )

    ChrTalk(
        0x00FE,
        (
            '据说亲卫队的人\n',
            '都藏在王都里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐怖事件的传闻难道是真的。\n',
            '我最好还是去避难吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EEF')

    def _loc_1E6D(): pass

    label('loc_1E6D')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '啊呀呀，\n',
            '我听那些士兵说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说亲卫队的人\n',
            '都藏在王都里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐怖事件的传闻难道是真的。\n',
            '我最好还是去避难吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EEF(): pass

    label('loc_1EEF')

    Jump('loc_23B6')

    def _loc_1EF2(): pass

    label('loc_1EF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1F4D',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上\n',
            '我和一位大圣堂的\n',
            '修女擦肩而过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么一大清早\n',
            '究竟是去哪里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B6')

    def _loc_1F4D(): pass

    label('loc_1F4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1F9A',
    )

    ChrTalk(
        0x00FE,
        (
            '以往总有\n',
            '通宵吵闹的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今年在这种情况下也不会再有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B6')

    def _loc_1F9A(): pass

    label('loc_1F9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2029',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天晚上开始，\n',
            '巡逻的士兵增加了不少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得武术大会能够搞得热热闹闹的，\n',
            '结果什么店铺都要早早关门，\n',
            '想提高营业额也不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B6')

    def _loc_2029(): pass

    label('loc_2029')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_206B',
    )

    ChrTalk(
        0x00FE,
        (
            '巡逻的士兵数量增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得世道不太平啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B6')

    def _loc_206B(): pass

    label('loc_206B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_20CD',
    )

    ChrTalk(
        0x00FE,
        (
            '王城、离宫、港口，\n',
            '全都被封锁了，\n',
            '总觉得心里憋得慌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是去看看武术大会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B6')

    def _loc_20CD(): pass

    label('loc_20CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_21DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_213F',
    )

    ChrTalk(
        0x00FE,
        (
            '这附近的大圣堂\n',
            '也是个观光胜地呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在人们都\n',
            '跑去看武术大会了，\n',
            '平时这里要更热闹一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21DB')

    def _loc_213F(): pass

    label('loc_213F')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这附近的大圣堂\n',
            '也是个观光胜地呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说那是王国中\n',
            '所有七耀教会的建筑里\n',
            '年代最久远的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在人们都\n',
            '跑去看武术大会了，\n',
            '平时这里要更热闹一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21DB(): pass

    label('loc_21DB')

    Jump('loc_23B6')

    def _loc_21DE(): pass

    label('loc_21DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2245',
    )

    ChrTalk(
        0x00FE,
        (
            '著名的利贝尔通讯社\n',
            '就在这个街区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在附近的咖啡厅里\n',
            '时常可以看到记者们\n',
            '在商讨工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B6')

    def _loc_2245(): pass

    label('loc_2245')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2352',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_22BD',
    )

    ChrTalk(
        0x00FE,
        (
            '因为摩尔根将军很忙，\n',
            '所以很少看到他\n',
            '回到在王都这里的家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '每年的诞辰庆典他都会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234F')

    def _loc_22BD(): pass

    label('loc_22BD')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这个西街区的住宅很多，\n',
            '那位摩尔根将军的家也在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为将军很忙，\n',
            '所以很少看到他回家一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '每年的诞辰庆典他都会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_234F(): pass

    label('loc_234F')

    Jump('loc_23B6')

    def _loc_2352(): pass

    label('loc_2352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_23B6',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有几个戴手铐的家伙\n',
            '被士兵押送过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来好像是\n',
            '从封锁了的港口\n',
            '那边过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23B6(): pass

    label('loc_23B6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x23BA
@scena.Code('func_11_23BA')
def func_11_23BA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2423',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '竟然是这次政变的幕后黑手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果早知道是这样，\n',
            '我们就不会协助他了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_2423(): pass

    label('loc_2423')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_249E',
    )

    ChrTalk(
        0x00FE,
        (
            '还没弄清楚是怎么回事，\n',
            '王都守卫队就撤离了，\n',
            '然后情报部的特务兵就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王城那边究竟\n',
            '发生了什么事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_249E(): pass

    label('loc_249E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_250B',
    )

    ChrTalk(
        0x00FE,
        (
            '有传闻说恐怖分子打着\n',
            '游击士的名义到处逃亡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们在突破\n',
            '蔡斯关所的盘查后，\n',
            '目前行踪不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_250B(): pass

    label('loc_250B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_255F',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会\n',
            '已经平安结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大会上没有发生恐怖袭击\n',
            '可真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_255F(): pass

    label('loc_255F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2693',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_25ED',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，国境守备队那些兄弟\n',
            '为了参加这次的武术大会，\n',
            '也来了王都这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和摩尔根将军联络不上，\n',
            '真是不知道该怎么办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2690')

    def _loc_25ED(): pass

    label('loc_25ED')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '说起来，国境守备队那些兄弟\n',
            '为了参加这次的武术大会，\n',
            '也来了王都这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和摩尔根将军联络不上，\n',
            '真是不知道该怎么办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说帝国方面\n',
            '有什么动静吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2690(): pass

    label('loc_2690')

    Jump('loc_2A5B')

    def _loc_2693(): pass

    label('loc_2693')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_27C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2717',
    )

    ChrTalk(
        0x00FE,
        (
            '自从理查德上校\n',
            '进入格兰赛尔城之后，\n',
            '就再也没出现过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然是为了对付恐怖分子，\n',
            '不在艾尔贝离宫本部行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C0')

    def _loc_2717(): pass

    label('loc_2717')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '自从理查德上校\n',
            '进入格兰赛尔城之后，\n',
            '就再也没出现过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然是为了对付恐怖分子，\n',
            '不在艾尔贝离宫本部行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个公爵也不可靠，\n',
            '所以只能相信女王陛下了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27C0(): pass

    label('loc_27C0')

    Jump('loc_2A5B')

    def _loc_27C3(): pass

    label('loc_27C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2827',
    )

    ChrTalk(
        0x00FE,
        (
            '听说特务部队是从\n',
            '情报部里培养出来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之物色的成员\n',
            '似乎都是很有本事的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_2827(): pass

    label('loc_2827')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2894',
    )

    ChrTalk(
        0x00FE,
        (
            '提到拉赛尔博士，\n',
            '他是那位发明导力器的\n',
            '高人的徒弟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绑架了博士，\n',
            '亲卫队到底意欲何为呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_2894(): pass

    label('loc_2894')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2911',
    )

    ChrTalk(
        0x00FE,
        (
            '被通缉的犯人\n',
            '全部都是亲卫队的成员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然正被通缉，\n',
            '他们肯定就不会穿着亲卫队的队服\n',
            '在街道上招摇过市了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_2911(): pass

    label('loc_2911')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2A1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_297B',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '真是好酷啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '头脑又聪明，\n',
            '武艺又精通，\n',
            '不用说当然会有很高的人气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A17')

    def _loc_297B(): pass

    label('loc_297B')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '几天前\n',
            '理查德上校到王城来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是从雷斯顿要塞\n',
            '到这个港口来的，\n',
            '真是个好酷的人啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '头脑又聪明，\n',
            '武艺又精通，\n',
            '不用说当然会有很高的人气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A17(): pass

    label('loc_2A17')

    Jump('loc_2A5B')

    def _loc_2A1A(): pass

    label('loc_2A1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2A5B',
    )

    ChrTalk(
        0x00FE,
        (
            '前面是港口，\n',
            '出于防止恐怖活动的原因，\n',
            '现在禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A5B(): pass

    label('loc_2A5B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x2A5F
@scena.Code('func_12_2A5F')
def func_12_2A5F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '为何那么有名的军人\n',
            '会发动政变呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，幸好大街这边\n',
            '没有被卷进事端里去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x2ABC
@scena.Code('func_13_2ABC')
def func_13_2ABC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '等大街安静下来之后，\n',
            '一定要叫我老公\n',
            '去找工作才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x2AFB
@scena.Code('func_14_2AFB')
def func_14_2AFB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '莉安妮小姐～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你在哪儿啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x2B28
@scena.Code('func_15_2B28')
def func_15_2B28():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2B35',
    )

    Jump('loc_2CA5')

    def _loc_2B35(): pass

    label('loc_2B35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2B3F',
    )

    Jump('loc_2CA5')

    def _loc_2B3F(): pass

    label('loc_2B3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2B49',
    )

    Jump('loc_2CA5')

    def _loc_2B49(): pass

    label('loc_2B49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2B53',
    )

    Jump('loc_2CA5')

    def _loc_2B53(): pass

    label('loc_2B53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2B5D',
    )

    Jump('loc_2CA5')

    def _loc_2B5D(): pass

    label('loc_2B5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2B97',
    )

    ChrTalk(
        0x00FE,
        (
            '港口那边似乎不能去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CA5')

    def _loc_2B97(): pass

    label('loc_2B97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2C80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2BED',
    )

    ChrTalk(
        0x00FE,
        (
            '以大圣堂为背景，\n',
            '伫立在王都街道上的你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～就像一幅画。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7D')

    def _loc_2BED(): pass

    label('loc_2BED')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '以大圣堂为背景，\n',
            '伫立在王都街道上的你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～就像一幅画。\n',
            '如果有一台导力相机该多好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少也要将这幅光景\n',
            '深深地印在脑海中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C7D(): pass

    label('loc_2C7D')

    Jump('loc_2CA5')

    def _loc_2C80(): pass

    label('loc_2C80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2C8A',
    )

    Jump('loc_2CA5')

    def _loc_2C8A(): pass

    label('loc_2C8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2C94',
    )

    Jump('loc_2CA5')

    def _loc_2C94(): pass

    label('loc_2C94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2C9E',
    )

    Jump('loc_2CA5')

    def _loc_2C9E(): pass

    label('loc_2C9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2CA5',
    )

    def _loc_2CA5(): pass

    label('loc_2CA5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x2CA9
@scena.Code('func_16_2CA9')
def func_16_2CA9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2CB6',
    )

    Jump('loc_2E3A')

    def _loc_2CB6(): pass

    label('loc_2CB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2CC0',
    )

    Jump('loc_2E3A')

    def _loc_2CC0(): pass

    label('loc_2CC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2CCA',
    )

    Jump('loc_2E3A')

    def _loc_2CCA(): pass

    label('loc_2CCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2CD4',
    )

    Jump('loc_2E3A')

    def _loc_2CD4(): pass

    label('loc_2CD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2CDE',
    )

    Jump('loc_2E3A')

    def _loc_2CDE(): pass

    label('loc_2CDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2D2E',
    )

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔港的夜景\n',
            '相当漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就连观光手册上\n',
            '都有它的介绍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E3A')

    def _loc_2D2E(): pass

    label('loc_2D2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2E15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2D9D',
    )

    ChrTalk(
        0x00FE,
        (
            '所有这些\n',
            '都是头一次见到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在洛连特约会地点都是一成不变的，\n',
            '所以感觉这儿很新鲜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E12')

    def _loc_2D9D(): pass

    label('loc_2D9D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '所有这些\n',
            '都是头一次见到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在洛连特约会地点都是一成不变的，\n',
            '所以感觉这儿很新鲜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅行真不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E12(): pass

    label('loc_2E12')

    Jump('loc_2E3A')

    def _loc_2E15(): pass

    label('loc_2E15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2E1F',
    )

    Jump('loc_2E3A')

    def _loc_2E1F(): pass

    label('loc_2E1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2E29',
    )

    Jump('loc_2E3A')

    def _loc_2E29(): pass

    label('loc_2E29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2E33',
    )

    Jump('loc_2E3A')

    def _loc_2E33(): pass

    label('loc_2E33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2E3A',
    )

    def _loc_2E3A(): pass

    label('loc_2E3A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x2E3E
@scena.Code('func_17_2E3E')
def func_17_2E3E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今年爷爷都没有回来呢，\n',
            '而且也没看到他在武术大会上出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太无聊了，所以我自己一个人出来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x2EAA
@scena.Code('func_18_2EAA')
def func_18_2EAA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哇哇，五彩纸屑飘到杯子里来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x2ED5
@scena.Code('func_19_2ED5')
def func_19_2ED5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '恰好这里有空座位，\n',
            '真不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x2EFF
@scena.Code('func_1A_2EFF')
def func_1A_2EFF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '王都的咖啡香浓得无可匹敌啊，\n',
            '的确很高级。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x2F3A
@scena.Code('func_1B_2F3A')
def func_1B_2F3A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这家酒廊气氛很不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还不是很累，\n',
            '但也想进去休息一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x2F8A
@scena.Code('func_1C_2F8A')
def func_1C_2F8A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呵呵，那就是有名的\n',
            '利贝尔通讯社大楼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道能不能\n',
            '去里面参观学习一下呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x2FE7
@scena.Code('func_1D_2FE7')
def func_1D_2FE7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '不愧是格兰赛尔，\n',
            '连住宅区也是那么优雅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x301B
@scena.Code('func_1E_301B')
def func_1E_301B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '你们今天\n',
            '去教堂祈祷了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在女王的诞辰庆典日做礼拜\n',
            '是一个很好的纪念呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x3074
@scena.Code('func_1F_3074')
def func_1F_3074():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊，这里就是格兰赛尔大圣堂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x309F
@scena.Code('func_20_309F')
def func_20_309F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '咦～这里就是\n',
            '格兰赛尔大～圣～堂呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x30CF
@scena.Code('func_21_30CF')
def func_21_30CF():
    EventBegin(0x00)
    CameraMove(-63290, -3220, -25240, 0)
    OP_67(0, 12660, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(269000, 0)
    OP_6E(442, 0)

    @scena.Lambda('lambda_3114')
    def lambda_3114():
        OP_67(0, 9500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3114)

    @scena.Lambda('lambda_312C')
    def lambda_312C():
        CameraSetDistance(2800, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_312C)

    @scena.Lambda('lambda_313C')
    def lambda_313C():
        OP_6C(315000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_313C)

    @scena.Lambda('lambda_314C')
    def lambda_314C():
        OP_6E(262, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_314C)

    SetChrPos(0x0101, -61850, -3500, -25070, 270)
    SetChrPos(0x0102, -62010, -3500, -26170, 270)
    SetChrPos(0x0008, -63080, -3500, -25100, 270)
    ClearChrFlags(0x0008, 0x0080)
    Sleep(6000)

    ChrTalk(
        0x0101,
        (
            '#0010110505V#000F哎～这家店的气氛真不错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110506V与其说是酒馆，\n',
            '不如称为咖啡店更好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110507V#010F这种香气，就是咖啡的味道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#140F这可是老板\n',
            '按照自己的兴趣布置的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110509V用玻璃器具煮出来的咖啡，\n',
            '不能不说是绝品呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '另外，用本地产的调料做的咖喱饭\n',
            '也很值得推荐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咖喱……\n',
            '吃起来应该很辣吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F虽然是有点辣，\n',
            '不过就是这样才香呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '以前我吃过，\n',
            '留下了很深的印象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咕嘟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#140F呵呵，只要吃一次\n',
            '就会上瘾的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110511V不过，吃饭和喝咖啡的事\n',
            '一会儿再说，我们先……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们比赛已经很累了，\n',
            '肚子都快饿扁啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F就是这样，\n',
            '我们能不能先吃晚饭呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#140F呼呼……\n',
            '你们这些孩子真是不讨人喜欢啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哼，算了，\n',
            '你们想吃多少就吃多少吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '待会儿取材的时候，\n',
            '可要给我把你们知道的通通说出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F果然是为了这个来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F对了，\n',
            '朵洛希今天没有一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#140F嗯，\n',
            '她去做别的工作去了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110521V不说这个了，我们赶快进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4130._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0022 offset: 0x3539
@scena.Code('func_22_3539')
def func_22_3539():
    If(
        (
            (Expr.Eval, "OP_40(0x036D)"),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3598',
    )

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Jump('loc_375A')

    def _loc_3598(): pass

    label('loc_3598')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36F3',
    )

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 2, 0x622)),
            Expr.Return,
        ),
        'loc_3668',
    )

    ChrTalk(
        0x0102,
        (
            '#0020110434V#010F今天已经很晚了，\n',
            '就不要到地下水路去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110435V明天再和金大哥他们\n',
            '一起进去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36ED')

    def _loc_3668(): pass

    label('loc_3668')

    ChrTalk(
        0x0102,
        (
            '#0020110430V#010F看起来这里就是\n',
            '『渡鸦帮』那些家伙说的\n',
            '地下水路的入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金大哥他们\n',
            '一起进去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36ED(): pass

    label('loc_36ED')

    TalkEnd(0x00FF)

    Jump('loc_375A')

    def _loc_36F3(): pass

    label('loc_36F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 2, 0x622)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_375A',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(115, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '使用了',
            (TxtCtl.SetColor, 0x2),
            '地下水路的钥匙Ａ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x00C4, 2, 0x622))
    OP_71(0x000A, 0x0010)
    OP_64(0x00, 0x0001)
    TalkEnd(0x00FF)

    def _loc_375A(): pass

    label('loc_375A')

    Return()

# id: 0x0023 offset: 0x375B
@scena.Code('func_23_375B')
def func_23_375B():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39B4',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_378E',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_378E(): pass

    label('loc_378E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_37B4',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_37B4(): pass

    label('loc_37B4')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_37DA',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_37DA(): pass

    label('loc_37DA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3801',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_3801(): pass

    label('loc_3801')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3827',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_3827(): pass

    label('loc_3827')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_384D',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_384D(): pass

    label('loc_384D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3872',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_3872(): pass

    label('loc_3872')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3897',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_38AB')

    def _loc_3897(): pass

    label('loc_3897')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_38AB(): pass

    label('loc_38AB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_39B1',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    OP_69(0x00FE, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39A2',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（糟了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（被发现了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39A2(): pass

    label('loc_39A2')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_39B1(): pass

    label('loc_39B1')

    Jump('func_23_375B')

    def _loc_39B4(): pass

    label('loc_39B4')

    Return()

# id: 0x0024 offset: 0x39B5
@scena.Code('func_24_39B5')
def func_24_39B5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39FA',
    )

    SetChrPos(0x00FE, -43700, 250, -8520, 0)
    ChrWalkTo(0x00FE, -43700, 250, -33510, 3000, 0x00)
    ChrWalkTo(0x00FE, -43700, 250, -8520, 3000, 0x00)

    Jump('func_24_39B5')

    def _loc_39FA(): pass

    label('loc_39FA')

    Return()

# id: 0x0025 offset: 0x39FB
@scena.Code('func_25_39FB')
def func_25_39FB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A40',
    )

    SetChrPos(0x00FE, -39120, 0, -7690, 180)
    ChrWalkTo(0x00FE, -39120, 0, -33190, 3000, 0x00)
    ChrWalkTo(0x00FE, -39120, 0, -7690, 3000, 0x00)

    Jump('func_25_39FB')

    def _loc_3A40(): pass

    label('loc_3A40')

    Return()

# id: 0x0026 offset: 0x3A41
@scena.Code('func_26_3A41')
def func_26_3A41():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AAE',
    )

    SetChrPos(0x00FE, -54990, -3750, -18870, 180)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)

    Jump('func_26_3A41')

    def _loc_3AAE(): pass

    label('loc_3AAE')

    Return()

# id: 0x0027 offset: 0x3AAF
@scena.Code('func_27_3AAF')
def func_27_3AAF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B1C',
    )

    SetChrPos(0x00FE, -74820, -3500, -19000, 180)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)

    Jump('func_27_3AAF')

    def _loc_3B1C(): pass

    label('loc_3B1C')

    Return()

# id: 0x0028 offset: 0x3B1D
@scena.Code('func_28_3B1D')
def func_28_3B1D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B8A',
    )

    SetChrPos(0x00FE, -74820, -3500, -30850, 180)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)

    Jump('func_28_3B1D')

    def _loc_3B8A(): pass

    label('loc_3B8A')

    Return()

# id: 0x0029 offset: 0x3B8B
@scena.Code('func_29_3B8B')
def func_29_3B8B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3BF8',
    )

    SetChrPos(0x00FE, -54990, -3750, -30850, 180)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)

    Jump('func_29_3B8B')

    def _loc_3BF8(): pass

    label('loc_3BF8')

    Return()

# id: 0x002A offset: 0x3BF9
@scena.Code('func_2A_3BF9')
def func_2A_3BF9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D8B',
    )

    SetScenaFlags(ScenaFlag(0x00C5, 6, 0x62E))
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -78280, 1760, 11580, 0)
    SetChrPos(0x0102, -79290, 1760, 11770, 45)

    @scena.Lambda('lambda_3C37')
    def lambda_3C37():
        OP_6C(350000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C37)

    CameraMove(-79030, 1760, 13490, 2000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F（太好了，终于到了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（不要丧失警惕，艾丝蒂尔……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111308V（我先进去，\n',
            '你跟在我后面。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（嗯，好的……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, -79100, 1760, 12480, 2000, 0x00)
    SetChrDirection(0x0102, 0, 400)
    OP_70(0x000C, 60)
    OP_73(0x000C)

    @scena.Lambda('lambda_3D0F')
    def lambda_3D0F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3D0F)

    @scena.Lambda('lambda_3D21')
    def lambda_3D21():
        ChrWalkTo(0x00FE, -78920, 1760, 13980, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3D21)

    Sleep(300)

    FadeOut(2000, 0, -1)
    ChrWalkTo(0x0101, -78630, 1760, 12450, 1000, 0x00)

    @scena.Lambda('lambda_3D5F')
    def lambda_3D5F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D5F)

    ChrWalkTo(0x0101, -78920, 1760, 13980, 1000, 0x00)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4134._SN', 100, 0, 0)
    IdleLoop()

    def _loc_3D8B(): pass

    label('loc_3D8B')

    Return()

# id: 0x002B offset: 0x3D8C
@scena.Code('func_2B_3D8C')
def func_2B_3D8C():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    CameraMove(-79450, 4770, 11320, 0)
    OP_67(0, 6680, -10000, 0)
    CameraSetDistance(2460, 0)
    OP_6C(39000, 0)
    OP_6E(478, 0)
    SetChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrFlags(0x000F, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0014, 0x0004)
    SetChrFlags(0x0015, 0x0004)
    SetChrFlags(0x0016, 0x0004)
    SetChrFlags(0x0030, 0x0080)
    SetChrFlags(0x0031, 0x0080)
    SetChrFlags(0x0032, 0x0080)
    SetChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0034, 0x0080)
    SetChrFlags(0x0035, 0x0080)
    SetChrFlags(0x0036, 0x0080)
    SetChrPos(0x000F, -80280, 1520, 11070, 218)
    SetChrPos(0x0010, -77730, 1490, 10600, 146)
    SetChrPos(0x0011, -81930, 1250, 9130, 327)
    SetChrPos(0x0012, -79450, 1250, 9450, 44)
    SetChrPos(0x0013, -76040, 1250, 8290, 156)
    SetChrPos(0x0014, -81880, 750, 6280, 145)
    SetChrPos(0x0015, -79420, 250, 5000, 190)
    SetChrPos(0x0016, -77590, 750, 6270, 7)

    @scena.Lambda('lambda_3EE0')
    def lambda_3EE0():
        OP_67(0, 11700, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3EE0)

    @scena.Lambda('lambda_3EF8')
    def lambda_3EF8():
        OP_6C(351000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3EF8)

    @scena.Lambda('lambda_3F08')
    def lambda_3F08():
        OP_6E(544, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3F08)

    CreateThread(0x0101, 0x00, 0x00, 0x002C)

    @scena.Lambda('lambda_3F1F')
    def lambda_3F1F():
        ChrMoveToRelative(0x00FE, -5000, 10160, -20000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3F1F)

    Sleep(500)

    PlaySE(141, 0x00, 0x64)

    @scena.Lambda('lambda_3F44')
    def lambda_3F44():
        ChrMoveToRelative(0x00FE, -2500, 26160, -21000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3F44)

    @scena.Lambda('lambda_3F5F')
    def lambda_3F5F():
        ChrMoveToRelative(0x00FE, 10000, 20160, -10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3F5F)

    Sleep(200)

    @scena.Lambda('lambda_3F7F')
    def lambda_3F7F():
        ChrMoveToRelative(0x00FE, 15000, 15160, -15000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3F7F)

    Sleep(200)

    @scena.Lambda('lambda_3F9F')
    def lambda_3F9F():
        ChrMoveToRelative(0x00FE, 15000, 20160, -15000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3F9F)

    @scena.Lambda('lambda_3FBA')
    def lambda_3FBA():
        ChrMoveToRelative(0x00FE, -5000, 15160, -10000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3FBA)

    Sleep(500)

    @scena.Lambda('lambda_3FDA')
    def lambda_3FDA():
        ChrMoveToRelative(0x00FE, 15000, 15160, -5000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_3FDA)

    Sleep(300)

    @scena.Lambda('lambda_3FFA')
    def lambda_3FFA():
        ChrMoveToRelative(0x00FE, -10000, 15160, -15000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_3FFA)

    Sleep(6000)

    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4130._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002C offset: 0x4021
@scena.Code('func_2C_4021')
def func_2C_4021():
    PlaySE(180, 0x00, 0x64)
    Sleep(2500)

    PlaySE(180, 0x00, 0x64)
    Sleep(2500)

    PlaySE(180, 0x00, 0x64)
    Sleep(2500)

    PlaySE(180, 0x00, 0x64)

    Return()

# id: 0x002D offset: 0x4045
@scena.Code('func_2D_4045')
def func_2D_4045():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 2, 0x622)),
            Expr.Return,
        ),
        'loc_40BD',
    )

    ChrTalk(
        0x0102,
        (
            '#0020110434V#010F今天已经很晚了，\n',
            '就不要到地下水路去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110435V明天再和金大哥他们\n',
            '一起进去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4142')

    def _loc_40BD(): pass

    label('loc_40BD')

    ChrTalk(
        0x0102,
        (
            '#0020110430V#010F看起来这里就是\n',
            '『渡鸦帮』那些家伙说的\n',
            '地下水路的入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金大哥他们\n',
            '一起进去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4142(): pass

    label('loc_4142')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x002E offset: 0x415E
@scena.Code('func_2E_415E')
def func_2E_415E():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　前面是港湾区　　　　\n',
            '※为强化警备体制，禁止通行',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x002F offset: 0x41C6
@scena.Code('func_2F_41C6')
def func_2F_41C6():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　 房屋出租\n',
            '※可以经营饭店',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0030 offset: 0x4213
@scena.Code('func_30_4213')
def func_30_4213():
    OP_13(0x00B8)

    Return()

# id: 0x0031 offset: 0x4217
@scena.Code('func_31_4217')
def func_31_4217():
    OP_13(0x00B7)

    Return()

# id: 0x0032 offset: 0x421B
@scena.Code('func_32_421B')
def func_32_421B():
    OP_13(0x00AF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
