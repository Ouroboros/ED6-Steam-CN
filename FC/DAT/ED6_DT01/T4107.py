import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4107_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4107   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡露娜'),
    TXT(0x02, '亚妮拉丝'),
    TXT(0x03, '库拉茨'),
    TXT(0x04, '克鲁茨'),
    TXT(0x05, '管家菲利普'),
    TXT(0x06, '杜南公爵'),
    TXT(0x07, '亚鲁瓦教授'),
    TXT(0x08, '朵洛希'),
    TXT(0x09, '芭蒂'),
    TXT(0x0A, '拉尔夫'),
    TXT(0x0B, '蒂库'),
    TXT(0x0C, '拉尔斯'),
    TXT(0x0D, '托伊'),
    TXT(0x0E, '克劳斯市长'),
    TXT(0x0F, '观众'),
    TXT(0x10, '观众'),
    TXT(0x11, '观众'),
    TXT(0x12, '观众'),
    TXT(0x13, '观众'),
    TXT(0x14, '观众'),
    TXT(0x15, '观众'),
    TXT(0x16, '观众'),
    TXT(0x17, '观众'),
    TXT(0x18, '观众'),
    TXT(0x19, '观众'),
    TXT(0x1A, '观众'),
    TXT(0x1B, '观众'),
    TXT(0x1C, '观众'),
    TXT(0x1D, '观众'),
    TXT(0x1E, '观众'),
    TXT(0x1F, '观众'),
    TXT(0x20, '观众'),
    TXT(0x21, '观众'),
    TXT(0x22, '观众'),
    TXT(0x23, '观众'),
    TXT(0x24, '观众'),
    TXT(0x25, '观众'),
    TXT(0x26, '观众'),
    TXT(0x27, '观众'),
    TXT(0x28, '观众'),
    TXT(0x29, '观众'),
    TXT(0x2A, '观众'),
    TXT(0x2B, '观众'),
    TXT(0x2C, '观众'),
    TXT(0x2D, '观众'),
    TXT(0x2E, '观众'),
    TXT(0x2F, '观众'),
    TXT(0x30, '观众'),
    TXT(0x31, '观众'),
    TXT(0x32, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4107.x'
    header.mapIndex       = 1
    header.bgm            = 18
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x26AF
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
    ]

# id: 0x10002 offset: 0x1AA
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002E,
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
            talkScenaIndex      = 0x0031,
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0030,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002F,
        ),
        ScenaNpcData(
            x                   = -12680,
            z                   = 4700,
            y                   = -4790,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            x                   = -12660,
            z                   = 4700,
            y                   = -3750,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = 3290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = 3960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = 4700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            x                   = -14740,
            z                   = 5200,
            y                   = -13430,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -15550,
            z                   = 5450,
            y                   = -5010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = 3270,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -15550,
            z                   = 5450,
            y                   = -9240,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -15550,
            z                   = 5450,
            y                   = 1890,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = -6590,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -12680,
            z                   = 4700,
            y                   = -17670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -14720,
            z                   = 5200,
            y                   = -3720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = 1670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -13550,
            z                   = 4950,
            y                   = -13580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = -8060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -14720,
            z                   = 5200,
            y                   = 510,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -12660,
            z                   = 4700,
            y                   = -9280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -13550,
            z                   = 4950,
            y                   = 4710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -14720,
            z                   = 5200,
            y                   = 4019,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -14520,
            z                   = 5200,
            y                   = -15970,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = -13490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -15610,
            z                   = 5450,
            y                   = -17700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = -15610,
            z                   = 5450,
            y                   = -14800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = -16640,
            z                   = 5700,
            y                   = -13560,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -13520,
            z                   = 4950,
            y                   = -9500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = -13520,
            z                   = 4950,
            y                   = -4800,
            direction           = 91,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -15440,
            z                   = 5450,
            y                   = -5520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = -15440,
            z                   = 5450,
            y                   = -6530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -15440,
            z                   = 5450,
            y                   = 3270,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = 520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = -13520,
            z                   = 4950,
            y                   = 3330,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = -14520,
            z                   = 5200,
            y                   = 1860,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = -13520,
            z                   = 4950,
            y                   = -8039,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = -15440,
            z                   = 5450,
            y                   = 550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = -12660,
            z                   = 4700,
            y                   = 4760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = -13520,
            z                   = 4950,
            y                   = -3700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = -16620,
            z                   = 5700,
            y                   = -3710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = -15440,
            z                   = 5450,
            y                   = 4750,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            x                   = -12730,
            z                   = 4700,
            y                   = -8010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
    )

# id: 0x10003 offset: 0x7CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x7CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x7CA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x7CA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 0, 0x638)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_85A',
    )

    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000E, -16580, 5700, -9620, 90)
    SetChrPos(0x000F, -10500, 4200, -6510, 90)
    SetChrPos(0x0008, -12710, 4700, -15880, 90)
    SetChrPos(0x0009, -12670, 4700, -15020, 90)
    SetChrPos(0x000A, -12650, 4700, -16690, 90)
    SetChrPos(0x000B, -12650, 4700, -17560, 90)

    def _loc_85A(): pass

    label('loc_85A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_864',
    )

    Jump('loc_A1A')

    def _loc_864(): pass

    label('loc_864')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_86E',
    )

    Jump('loc_A1A')

    def _loc_86E(): pass

    label('loc_86E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_878',
    )

    Jump('loc_A1A')

    def _loc_878(): pass

    label('loc_878')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_882',
    )

    Jump('loc_A1A')

    def _loc_882(): pass

    label('loc_882')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_948',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -12660, 4700, -6420, 90)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -12660, 4700, -5620, 90)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 5, 0x635)),
            Expr.Return,
        ),
        'loc_8E1',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -14490, 5200, 70, 90)

    def _loc_8E1(): pass

    label('loc_8E1')

    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)
    ClearChrFlags(0x0028, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    ClearChrFlags(0x002D, 0x0080)
    ClearChrFlags(0x002E, 0x0080)
    ClearChrFlags(0x002F, 0x0080)
    ClearChrFlags(0x0030, 0x0080)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0033, 0x0080)
    ClearChrFlags(0x0034, 0x0080)
    ClearChrFlags(0x0035, 0x0080)
    ClearChrFlags(0x0036, 0x0080)
    ClearChrFlags(0x0037, 0x0080)
    ClearChrFlags(0x0038, 0x0080)

    Jump('loc_A1A')

    def _loc_948(): pass

    label('loc_948')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_952',
    )

    Jump('loc_A1A')

    def _loc_952(): pass

    label('loc_952')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_9C6',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -13550, 4950, -6540, 90)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 4, 0x624)),
            Expr.Return,
        ),
        'loc_9C3',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrChipByIndex(0x000F, 31)
    SetChrPos(0x000F, -10500, 4200, -6450, 90)

    def _loc_9C3(): pass

    label('loc_9C3')

    Jump('loc_A1A')

    def _loc_9C6(): pass

    label('loc_9C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_9D0',
    )

    Jump('loc_A1A')

    def _loc_9D0(): pass

    label('loc_9D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_A09',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -12690, 4700, -4810, 90)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)

    Jump('loc_A1A')

    def _loc_A09(): pass

    label('loc_A09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_A13',
    )

    Jump('loc_A1A')

    def _loc_A13(): pass

    label('loc_A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_A1A',
    )

    def _loc_A1A(): pass

    label('loc_A1A')

    Return()

# id: 0x0001 offset: 0xA1B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xA1C
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A4C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_B8E')

    def _loc_A4C(): pass

    label('loc_A4C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A65',
    )

    OP_99(0x00FE, 0x01, 0x07, 1300)

    Jump('loc_B8E')

    def _loc_A65(): pass

    label('loc_A65')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A7E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1250)

    Jump('loc_B8E')

    def _loc_A7E(): pass

    label('loc_A7E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A97',
    )

    OP_99(0x00FE, 0x03, 0x07, 1200)

    Jump('loc_B8E')

    def _loc_A97(): pass

    label('loc_A97')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AB0',
    )

    OP_99(0x00FE, 0x04, 0x07, 1150)

    Jump('loc_B8E')

    def _loc_AB0(): pass

    label('loc_AB0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AC9',
    )

    OP_99(0x00FE, 0x05, 0x07, 1100)

    Jump('loc_B8E')

    def _loc_AC9(): pass

    label('loc_AC9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE2',
    )

    OP_99(0x00FE, 0x06, 0x07, 1050)

    Jump('loc_B8E')

    def _loc_AE2(): pass

    label('loc_AE2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AFB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1355)

    Jump('loc_B8E')

    def _loc_AFB(): pass

    label('loc_AFB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B14',
    )

    OP_99(0x00FE, 0x01, 0x07, 1305)

    Jump('loc_B8E')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B2D',
    )

    OP_99(0x00FE, 0x02, 0x07, 1255)

    Jump('loc_B8E')

    def _loc_B2D(): pass

    label('loc_B2D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B46',
    )

    OP_99(0x00FE, 0x03, 0x07, 1205)

    Jump('loc_B8E')

    def _loc_B46(): pass

    label('loc_B46')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B5F',
    )

    OP_99(0x00FE, 0x04, 0x07, 1155)

    Jump('loc_B8E')

    def _loc_B5F(): pass

    label('loc_B5F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B78',
    )

    OP_99(0x00FE, 0x05, 0x07, 1105)

    Jump('loc_B8E')

    def _loc_B78(): pass

    label('loc_B78')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B8E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1055)

    def _loc_B8E(): pass

    label('loc_B8E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BA3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1200)

    Jump('loc_B8E')

    def _loc_BA3(): pass

    label('loc_BA3')

    Return()

# id: 0x0003 offset: 0xBA4
@scena.Code('func_03_BA4')
def func_03_BA4():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xBC1
@scena.Code('func_04_BC1')
def func_04_BC1():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '不管是谁取得优胜都很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xBE8
@scena.Code('func_05_BE8')
def func_05_BE8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我现在已经开始兴奋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xC0B
@scena.Code('func_06_C0B')
def func_06_C0B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈～哈，因为兴奋过度，\n',
            '来得太早了些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xC3D
@scena.Code('func_07_C3D')
def func_07_C3D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今年为谁加油好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xC5C
@scena.Code('func_08_C5C')
def func_08_C5C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_CAA',
    )

    ChrTalk(
        0x00FE,
        (
            '好、好像觉得后面\n',
            '有股很强的杀气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是、是我多心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0A')

    def _loc_CAA(): pass

    label('loc_CAA')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    OP_62(0x00FE, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '好、好像觉得后面\n',
            '有股很强的杀气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是、是我多心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D0A(): pass

    label('loc_D0A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xD0E
@scena.Code('func_09_D0E')
def func_09_D0E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '完了，\n',
            '导力相机忘带了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xD32
@scena.Code('func_0A_D32')
def func_0A_D32():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '可惜了！\n',
            '今年亲卫队没有出战呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xD5E
@scena.Code('func_0B_D5E')
def func_0B_D5E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '团体赛比想象的要有趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0xD83
@scena.Code('func_0C_D83')
def func_0C_D83():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我想还是特务部队\n',
            '会取得优胜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '穿着一身黑装，\n',
            '看起来就很强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0xDD2
@scena.Code('func_0D_DD2')
def func_0D_DD2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天的对阵\n',
            '会是怎么样的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0xDFA
@scena.Code('func_0E_DFA')
def func_0E_DFA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '游击士的两个小组\n',
            '都还没有出局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两组都要加油啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0xE3E
@scena.Code('func_0F_E3E')
def func_0F_E3E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '特务部队虽然让人觉得有些害怕，\n',
            '但实力相当强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0xE7A
@scena.Code('func_10_E7A')
def func_10_E7A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛怎么还不开始啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0xE9B
@scena.Code('func_11_E9B')
def func_11_E9B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '每年的比赛\n',
            '我都很期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0xEC1
@scena.Code('func_12_EC1')
def func_12_EC1():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天是总决赛的日子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0xEE4
@scena.Code('func_13_EE4')
def func_13_EE4():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哪支小组会取胜呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我心里扑通扑通地响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0xF21
@scena.Code('func_14_F21')
def func_14_F21():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我喜欢游击士组里面\n',
            '那个金色头发的小哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '外表英俊潇洒，\n',
            '而且射击方面也无懈可击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0xF82
@scena.Code('func_15_F82')
def func_15_F82():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我想看那个戴着红色面具的哥哥\n',
            '和那个像熊一样的叔叔\n',
            '打架的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0xFCF
@scena.Code('func_16_FCF')
def func_16_FCF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '真不愧是总决赛的日子，\n',
            '一大早就已经有很多人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x100D
@scena.Code('func_17_100D')
def func_17_100D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '双方都是今年\n',
            '第一次参加比赛，\n',
            '哪一边会取胜的确是决赛的看点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x1058
@scena.Code('func_18_1058')
def func_18_1058():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '游击士小组里面\n',
            '好像有个女孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可真了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x109C
@scena.Code('func_19_109C')
def func_19_109C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛还没有开始吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x10BB
@scena.Code('func_1A_10BB')
def func_1A_10BB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '每年只有我和老头子\n',
            '两个人来看比赛，\n',
            '感到无聊也没有办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x1102
@scena.Code('func_1B_1102')
def func_1B_1102():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '因为太期待今天的比赛了，\n',
            '我昨天一夜都睡不着觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x1140
@scena.Code('func_1C_1140')
def func_1C_1140():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我还是觉得\n',
            '特务部队会取胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一看名字就知道来头不小嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x1188
@scena.Code('func_1D_1188')
def func_1D_1188():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '就算口干舌燥\n',
            '我也要全力为比赛呐喊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x11B8
@scena.Code('func_1E_11B8')
def func_1E_11B8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我支持游击士组哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前我也曾受到\n',
            '游击士的很多关照啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x1200
@scena.Code('func_1F_1200')
def func_1F_1200():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '要是把便当\n',
            '也带来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一大早就过来排队，\n',
            '肚子都饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x124B
@scena.Code('func_20_124B')
def func_20_124B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '武术大会果然很有意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是看就已经爽呆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x1291
@scena.Code('func_21_1291')
def func_21_1291():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '游击士组里的那个男孩子\n',
            '和我儿子的年纪差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何\n',
            '我也要支持游击士组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x12EE
@scena.Code('func_22_12EE')
def func_22_12EE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '如果从综合实力来看的话，\n',
            '不用说也知道\n',
            '那个特务部队是最强的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x1339
@scena.Code('func_23_1339')
def func_23_1339():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '没有想到决赛对阵\n',
            '会是这样的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x136E
@scena.Code('func_24_136E')
def func_24_136E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '王国军和游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得无论哪一方，\n',
            '都是保卫我们市民的、\n',
            '值得大家信赖的好战士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x13D1
@scena.Code('func_25_13D1')
def func_25_13D1():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '比赛快要开始了……\n',
            '我会全力为大家呐喊助威的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0x140B
@scena.Code('func_26_140B')
def func_26_140B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_147F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 5, 0x635)),
            Expr.Return,
        ),
        'loc_147F',
    )

    ChrTalk(
        0x0015,
        (
            '#0340111727V#600F我从年轻的时候就喜欢\n',
            '观看每年一度的武术大会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111677V加油啊。\n',
            '艾丝蒂尔、约修亚，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_147F(): pass

    label('loc_147F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0x1483
@scena.Code('func_27_1483')
def func_27_1483():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_14F9',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120111626V虽说那些对手\n',
            '的确不容易对付，\n',
            '#816F不过我坚信你们一定能够取胜的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120111627V我会给你们加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_158D')

    def _loc_14F9(): pass

    label('loc_14F9')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0120111628V#850F哟，两位新人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120111629V你们决赛的对手相当强劲，\n',
            '不过肯定会有胜算的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120111630V#816F我坚信你们一定能够取胜的！\n',
            '我会给你们加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_158D(): pass

    label('loc_158D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0x1591
@scena.Code('func_28_1591')
def func_28_1591():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_15FC',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320111636V#830F听好，一定要放松，\n',
            '像往常那样出战就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320111635V就连在气势上也要战胜对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1672')

    def _loc_15FC(): pass

    label('loc_15FC')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0320111633V#830F啊，你们好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320111634V听好，一定要放松，\n',
            '像往常那样出战就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320111635V就连在气势上也要战胜对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1672(): pass

    label('loc_1672')

    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0x1676
@scena.Code('func_29_1676')
def func_29_1676():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0x168F
@scena.Code('func_2A_168F')
def func_2A_168F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天我一大早\n',
            '就去叫了那两个人，\n',
            '然后来竞技场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为绝对不能错过总决赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002B offset: 0x16EC
@scena.Code('func_2B_16EC')
def func_2B_16EC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哪个小组会取胜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002C offset: 0x170B
@scena.Code('func_2C_170B')
def func_2C_170B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1718',
    )

    Jump('loc_181F')

    def _loc_1718(): pass

    label('loc_1718')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1722',
    )

    Jump('loc_181F')

    def _loc_1722(): pass

    label('loc_1722')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_172C',
    )

    Jump('loc_181F')

    def _loc_172C(): pass

    label('loc_172C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1736',
    )

    Jump('loc_181F')

    def _loc_1736(): pass

    label('loc_1736')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_17E6',
    )

    ChrTalk(
        0x00FE,
        (
            '想拿个观战的好位置，\n',
            '所以我在门外彻夜排队，\n',
            '不料被那些巡逻的士兵赶回了家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后，我偷偷地从家里溜出来，\n',
            '躲在大街上的草丛里等那些士兵撤走，\n',
            '然后才来排队的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_181F')

    def _loc_17E6(): pass

    label('loc_17E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_17F0',
    )

    Jump('loc_181F')

    def _loc_17F0(): pass

    label('loc_17F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_17FA',
    )

    Jump('loc_181F')

    def _loc_17FA(): pass

    label('loc_17FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1804',
    )

    Jump('loc_181F')

    def _loc_1804(): pass

    label('loc_1804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_180E',
    )

    Jump('loc_181F')

    def _loc_180E(): pass

    label('loc_180E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1818',
    )

    Jump('loc_181F')

    def _loc_1818(): pass

    label('loc_1818')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_181F',
    )

    def _loc_181F(): pass

    label('loc_181F')

    TalkEnd(0x00FE)

    Return()

# id: 0x002D offset: 0x1823
@scena.Code('func_2D_1823')
def func_2D_1823():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1830',
    )

    Jump('loc_1A07')

    def _loc_1830(): pass

    label('loc_1830')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_183A',
    )

    Jump('loc_1A07')

    def _loc_183A(): pass

    label('loc_183A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1844',
    )

    Jump('loc_1A07')

    def _loc_1844(): pass

    label('loc_1844')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_184E',
    )

    Jump('loc_1A07')

    def _loc_184E(): pass

    label('loc_184E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_18C6',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天真是辛苦我丈夫了，\n',
            '帮我拿到这么一个好位子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说我的要求很任性，\n',
            '不过没想到他能为我做到这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A07')

    def _loc_18C6(): pass

    label('loc_18C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_18D0',
    )

    Jump('loc_1A07')

    def _loc_18D0(): pass

    label('loc_18D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_19BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1935',
    )

    ChrTalk(
        0x00FE,
        (
            '最前排正中央\n',
            '明明一直是我的位子啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来明天的决赛\n',
            '我必须来早一点才行！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19BA')

    def _loc_1935(): pass

    label('loc_1935')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_62(0x00FE, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '唉～遗憾啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最前排正中央\n',
            '明明一直是我的位子啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来明天的决赛\n',
            '我必须来早一点才行！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19BA(): pass

    label('loc_19BA')

    Jump('loc_1A07')

    def _loc_19BD(): pass

    label('loc_19BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_19C7',
    )

    Jump('loc_1A07')

    def _loc_19C7(): pass

    label('loc_19C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_19F6',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '今年又到了这个时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A07')

    def _loc_19F6(): pass

    label('loc_19F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1A00',
    )

    Jump('loc_1A07')

    def _loc_1A00(): pass

    label('loc_1A00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1A07',
    )

    def _loc_1A07(): pass

    label('loc_1A07')

    TalkEnd(0x00FE)

    Return()

# id: 0x002E offset: 0x1A0B
@scena.Code('func_2E_1A0B')
def func_2E_1A0B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1A18',
    )

    Jump('loc_1AE8')

    def _loc_1A18(): pass

    label('loc_1A18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1A22',
    )

    Jump('loc_1AE8')

    def _loc_1A22(): pass

    label('loc_1A22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1A2C',
    )

    Jump('loc_1AE8')

    def _loc_1A2C(): pass

    label('loc_1A2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1A36',
    )

    Jump('loc_1AE8')

    def _loc_1A36(): pass

    label('loc_1A36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1AAF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310111631V#820F今天大家都来到竞技场\n',
            '为你们呐喊助威。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310111632V作为游击士协会的代表，\n',
            '你们一定要为荣誉而战哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE8')

    def _loc_1AAF(): pass

    label('loc_1AAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1AB9',
    )

    Jump('loc_1AE8')

    def _loc_1AB9(): pass

    label('loc_1AB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1AC3',
    )

    Jump('loc_1AE8')

    def _loc_1AC3(): pass

    label('loc_1AC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1ACD',
    )

    Jump('loc_1AE8')

    def _loc_1ACD(): pass

    label('loc_1ACD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1AD7',
    )

    Jump('loc_1AE8')

    def _loc_1AD7(): pass

    label('loc_1AD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1AE1',
    )

    Jump('loc_1AE8')

    def _loc_1AE1(): pass

    label('loc_1AE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1AE8',
    )

    def _loc_1AE8(): pass

    label('loc_1AE8')

    TalkEnd(0x00FE)

    Return()

# id: 0x002F offset: 0x1AEC
@scena.Code('func_2F_1AEC')
def func_2F_1AEC():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1D00',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 3, 0x633)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CC0',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 3, 0x633))

    ChrTalk(
        0x000F,
        (
            '#0280111583V#151F啊，是小艾你们啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111584V真厉害～！\n',
            '你们打进决赛了～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111585V我真是兴奋得都要跳起来了～！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111586V#506F哈哈，别这么激动嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111587V#010F如果不静下心来集中精神的话，\n',
            '说不定会错过很多精彩的画面哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0280111588V#150F哎嘿，不用担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111589V因为我只有在静不下心的时候\n',
            '才能拍下一些好的照片呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111590V这样才有自然感哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111591V#019F是、是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111592V#007F不愧是朵洛希……\n',
            '完全是个另类的天才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CFD')

    def _loc_1CC0(): pass

    label('loc_1CC0')

    ChrTalk(
        0x000F,
        (
            '#0280111593V#151F小艾你们的精彩表现，\n',
            '我一定会好好拍下来的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CFD(): pass

    label('loc_1CFD')

    Jump('loc_1D73')

    def _loc_1D00(): pass

    label('loc_1D00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 4, 0x624)),
            Expr.Return,
        ),
        'loc_1D73',
    )

    ChrTalk(
        0x000F,
        (
            '#0280111594V#150F嘿嘿，\n',
            '因为我是负责报道的记者，\n',
            '所以拿到了特等席位哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111595V好了，\n',
            '要快点把相机准备好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D73(): pass

    label('loc_1D73')

    TalkEnd(0x000F)

    Return()

# id: 0x0030 offset: 0x1D77
@scena.Code('func_30_1D77')
def func_30_1D77():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 2, 0x632)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2040',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 2, 0x632))

    ChrTalk(
        0x000E,
        (
            '#0150111565V#130F你们好啊。\n',
            '艾丝蒂尔、约修亚，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111566V#004F哎，是亚鲁瓦教授！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111567V#014F您也来观看比赛吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0150111568V#130F哈哈，\n',
            '因为受了你们好多的照顾嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111569V今天是恩人出战决赛的日子，\n',
            '我想无论如何也要来看一看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111570V#001F嘿嘿，谢谢啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111571V#006F不过，买决赛的门票\n',
            '肯定花了不少米拉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0150111572V#130F哈哈，那也不是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111573V资料馆的馆长突然有急事，\n',
            '不能前来观看比赛了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111574V所以就把这张票免费转让给了我。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111575V#506F什～么啊，果然还是没付钱嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0150111576V#130F哈哈……真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111577V不过，我支持你们的信念\n',
            '是绝对不会输给其他人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111578V请你们一定要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111579V#006F嗯，包在我们身上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111580V#010F我们必定全力出战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_209F')

    def _loc_2040(): pass

    label('loc_2040')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_209F',
    )

    ChrTalk(
        0x000E,
        (
            '#0150111581V#130F我支持你们的信念\n',
            '是绝对不会输给其他人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150111578V请你们一定要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_209F(): pass

    label('loc_209F')

    TalkEnd(0x000E)

    Return()

# id: 0x0031 offset: 0x20A3
@scena.Code('func_31_20A3')
def func_31_20A3():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 4, 0x634)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2606',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 4, 0x634))
    SetChrDirection(0x000B, 90, 0)

    ChrTalk(
        0x000B,
        (
            '#0330111596V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111597V#004F哎……\n',
            '克鲁茨前辈，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000B, 15, 0, 300, 4000)
    ChrTurnDirection(0x000B, 0x0000, 400)

    ChrTalk(
        0x000B,
        (
            '#0330111598V#840F哎……啊，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111599V终于到了决赛呢。\n',
            '我很期待你们的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111600V#006F嗯，看我的吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111601V#505F……不过，克鲁茨前辈，\n',
            '你的脸色好像有点不对劲啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111602V#012F是啊。\n',
            '脸色铁青铁青呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330111603V#845F没什么……\n',
            '只是从刚才开始就觉得有点头晕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111604V#844F不过奇怪的是……\n',
            '我的身体没有什么事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111605V……难道是那个时候留下的后遗症……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111606V#580F后、后遗症……\n',
            '难道是说昨天的比赛吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330111607V#841F哈哈，不是不是。\n',
            '是三个月之前的一次事故。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111608V那时候我好像执行任务失败了，\n',
            '还弄得自己伤痕累累。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111609V#505F好像执行任务失败了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111610V#012F好像是很模糊的说法啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330111611V#845F啊啊，不好意思。\n',
            '因为那次事故的记忆确实很模糊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111612V连那是件什么样的工作\n',
            '也完全记不起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111613V虽然医生说，\n',
            '这是因事故所受的刺激……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111614V#012F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111615V#003F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111616V#002F不过，以这样的状态来参加比赛，\n',
            '不会有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330111617V#841F我刚才已经说了，\n',
            '其实这不是身体上的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111618V嗯，跟你们说了一会儿话，\n',
            '我感觉比刚才舒服多了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111619V已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111620V#505F是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111621V#010F看起来脸色确实好些了呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111622V不过……\n',
            '请不要勉强硬撑着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330111623V#841F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330111624V你们今天一定要\n',
            '全力出战获取冠军哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000B, 90, 400)

    Jump('loc_2647')

    def _loc_2606(): pass

    label('loc_2606')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2647',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330111625V要连我们的份也一起加油，\n',
            '全力出战获取冠军哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2647(): pass

    label('loc_2647')

    TalkEnd(0x000B)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
