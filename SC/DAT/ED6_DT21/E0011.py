import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0011_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0011   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '阿加特'),
    TXT(0x02, '雪拉扎德'),
    TXT(0x03, '奥利维尔'),
    TXT(0x04, '提妲'),
    TXT(0x05, '金'),
    TXT(0x06, '科洛丝'),
    TXT(0x07, '酒杯'),
    TXT(0x08, '船长'),
    TXT(0x09, '操舵手'),
    TXT(0x0A, '副操舵手'),
    TXT(0x0B, '操作员'),
    TXT(0x0C, '乘客'),
    TXT(0x0D, '乘客'),
    TXT(0x0E, '乘客'),
    TXT(0x0F, '乘务员诺拉'),
    TXT(0x10, '鲁特尔'),
    TXT(0x11, '阿尔丹'),
    TXT(0x12, '米拉诺'),
    TXT(0x13, '西蒙'),
    TXT(0x14, '哈尔德'),
    TXT(0x15, '乘务员亚雷克'),
    TXT(0x16, '索斯摩夫'),
    TXT(0x17, '佩特洛夫船长'),
    TXT(0x18, '乘务员罗杰'),
    TXT(0x19, '乘务员库因特'),
    TXT(0x1A, '乘客'),
    TXT(0x1B, '乘客'),
    TXT(0x1C, '乘客'),
    TXT(0x1D, '乘客'),
    TXT(0x1E, '乘客'),
    TXT(0x1F, '乘客'),
    TXT(0x20, '乘客'),
    TXT(0x21, '乘客'),
    TXT(0x22, '凯文神父'),
    TXT(0x23, '布露姆老奶奶'),
    TXT(0x24, '基蒂'),
    TXT(0x25, '乘客'),
    TXT(0x26, '乘客'),
    TXT(0x27, '乘客'),
    TXT(0x28, '乘客'),
    TXT(0x29, '乘客'),
    TXT(0x2A, '乘客'),
    TXT(0x2B, '乘客'),
    TXT(0x2C, '乘客'),
    TXT(0x2D, '乘客'),
    TXT(0x2E, '乘客'),
    TXT(0x2F, '乘客'),
    TXT(0x30, '吉米'),
    TXT(0x31, '阿尔丹'),
    TXT(0x32, '小说'),
    TXT(0x33, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0011.x'
    header.mapIndex       = 1
    header.bgm            = 1
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/E0011_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xAA58
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
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT06/CH20134._CH', 'ED6_DT06/CH20134P._CP'),
        ('ED6_DT07/CH01443._CH', 'ED6_DT07/CH01443P._CP'),
        ('ED6_DT07/CH01453._CH', 'ED6_DT07/CH01453P._CP'),
        ('ED6_DT07/CH01453._CH', 'ED6_DT07/CH01453P._CP'),
        ('ED6_DT07/CH01453._CH', 'ED6_DT07/CH01453P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01163._CH', 'ED6_DT07/CH01163P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01443._CH', 'ED6_DT07/CH01443P._CP'),
        ('ED6_DT07/CH01293._CH', 'ED6_DT07/CH01293P._CP'),
        ('ED6_DT07/CH01293._CH', 'ED6_DT07/CH01293P._CP'),
        ('ED6_DT07/CH01113._CH', 'ED6_DT07/CH01113P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01463._CH', 'ED6_DT07/CH01463P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT26/CH20241._CH', 'ED6_DT26/CH20241P._CP'),
        ('ED6_DT26/CH20291._CH', 'ED6_DT26/CH20291P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH01103._CH', 'ED6_DT07/CH01103P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
    ]

# id: 0x10002 offset: 0x282
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 117300,
            z                   = 0,
            y                   = 1350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 117300,
            z                   = 0,
            y                   = 1350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 88690,
            z                   = -1000,
            y                   = 51250,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 88530,
            z                   = -500,
            y                   = 51980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
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
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0191,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0191,
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
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 116000,
            z                   = 0,
            y                   = 10280,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 117420,
            z                   = 80,
            y                   = 7320,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 51,
            chipIndex           = 51,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 57210,
            z                   = 0,
            y                   = 1140,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 88880,
            z                   = 100,
            y                   = -1240,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 87830,
            z                   = 0,
            y                   = 170,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 89360,
            z                   = 0,
            y                   = 8810,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 86120,
            z                   = 0,
            y                   = 47320,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 27850,
            z                   = 0,
            y                   = -8070,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 59020,
            z                   = -530,
            y                   = 49310,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 56990,
            z                   = -1800,
            y                   = 51970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 59190,
            z                   = -1950,
            y                   = 54200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 88770,
            z                   = 100,
            y                   = -4910,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 115840,
            z                   = 0,
            y                   = -1200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 114590,
            z                   = 100,
            y                   = -2470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = 113550,
            z                   = 80,
            y                   = 1410,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 40,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 87890,
            z                   = 0,
            y                   = -1220,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = 87890,
            z                   = 0,
            y                   = -2410,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 51,
            chipIndex           = 51,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 48,
            chipIndex           = 48,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 49,
            chipIndex           = 49,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 50,
            chipIndex           = 50,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 52,
            chipIndex           = 52,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 56,
            chipIndex           = 56,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 57,
            chipIndex           = 57,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 58,
            chipIndex           = 58,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 55,
            chipIndex           = 55,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            x                   = 116990,
            z                   = 0,
            y                   = 10300,
            direction           = 56,
            word_0E             = 0,
            dword_10            = 54,
            chipIndex           = 54,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            x                   = 57210,
            z                   = 0,
            y                   = 1140,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 55,
            chipIndex           = 55,
            npcIndex            = 0x01B5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 88140,
            z                   = -500,
            y                   = 52020,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703939,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x8C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x8C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x8C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x8C2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8DF',
    )

    OP_89(0x0101, 84860, 130, 5970, 0)

    def _loc_8DF(): pass

    label('loc_8DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_A7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8F7',
    )

    Event(0, 0x0039)

    def _loc_8F7(): pass

    label('loc_8F7')

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 91260, 0, 44910, 90)
    SetChrPos(0x000D, 117350, 100, 3200, 0)
    ClearChrFlags(0x000D, 0x0080)
    SetChrChipByIndex(0x000D, 8)
    TerminateThread(0x000A, 0x00)
    SetChrPos(0x000A, 89280, 80, -3200, 0)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 2)
    SetChrSubChip(0x000A, 0)
    SetChrPos(0x000C, 117350, 100, -850, 0)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0008, 57200, 0, -2270, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 53)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 114820, 0, 5050, 180)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001C, 86270, 0, 46740, 180)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    SetChrPos(0x0021, 113340, 100, 1260, 0)
    ClearChrFlags(0x0022, 0x0080)
    SetChrPos(0x0022, 116650, 0, 10640, 45)
    ClearChrFlags(0x0023, 0x0080)
    SetChrPos(0x0023, 84990, 0, 9250, 180)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 84990, 0, 8270, 0)
    ClearChrFlags(0x0025, 0x0080)
    SetChrPos(0x0025, 86180, 0, 80, 225)
    ClearChrFlags(0x0026, 0x0080)
    SetChrPos(0x0026, 85340, 100, -1250, 0)
    ClearChrFlags(0x0027, 0x0080)
    SetChrPos(0x0027, 117260, 100, 5450, 0)
    ClearChrFlags(0x0028, 0x0080)
    SetChrPos(0x0028, 88620, -1000, 52980, 0)

    Jump('loc_F0F')

    def _loc_A7C(): pass

    label('loc_A7C')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7A',
    )

    SetChrPos(0x0008, 116650, 100, 3200, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0009, 117350, 50, 1200, 0)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x000C, 117350, 100, -850, 0)
    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 1, 0x1809)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AF2',
    )

    SetChrPos(0x000D, 88410, -1000, 53020, 0)
    ClearChrFlags(0x000D, 0x0080)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)

    Jump('loc_B0D')

    def _loc_AF2(): pass

    label('loc_AF2')

    SetChrPos(0x000D, 116650, 100, 5200, 0)
    ClearChrFlags(0x000D, 0x0080)
    SetChrChipByIndex(0x000D, 8)

    def _loc_B0D(): pass

    label('loc_B0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 2, 0x180A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B2E',
    )

    SetChrPos(0x000B, 58800, 0, -2020, 90)
    ClearChrFlags(0x000B, 0x0080)

    Jump('loc_B52')

    def _loc_B2E(): pass

    label('loc_B2E')

    TerminateThread(0x000B, 0x00)
    SetChrPos(0x000B, 117350, 100, 5200, 0)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0010)
    SetChrChipByIndex(0x000B, 9)

    def _loc_B52(): pass

    label('loc_B52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 3, 0x180B)),
            Expr.Return,
        ),
        'loc_B7D',
    )

    TerminateThread(0x000A, 0x00)
    SetChrPos(0x000A, 117350, 80, 3100, 0)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 2)
    SetChrSubChip(0x000A, 0)

    def _loc_B7D(): pass

    label('loc_B7D')

    ClearChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0016, 0x0010)
    SetChrPos(0x0016, 114750, 0, 11170, 180)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x001D, 28120, 0, -8480, 270)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001C, 86270, 0, 46740, 180)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    SetChrPos(0x002C, 117330, 100, 7280, 0)
    ClearChrFlags(0x002D, 0x0080)
    SetChrPos(0x002D, 86280, 0, 1960, 212)
    ClearChrFlags(0x002E, 0x0080)
    SetChrPos(0x002E, 84800, 100, 600, 0)
    ClearChrFlags(0x002F, 0x0080)
    SetChrPos(0x002F, 85460, 100, -3100, 0)
    ClearChrFlags(0x0030, 0x0080)
    SetChrPos(0x0030, 89340, 150, -4890, 0)
    ClearChrFlags(0x0031, 0x0080)
    SetChrPos(0x0031, 113350, 100, -700, 0)
    ClearChrFlags(0x0032, 0x0080)
    SetChrPos(0x0032, 113380, 0, 0, 180)

    Jump('loc_F0F')

    def _loc_C7A(): pass

    label('loc_C7A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006B, 'loc_C8A'),
        (0x0000006D, 'loc_C98'),
        (-1, 'loc_CA6'),
    )

    def _loc_C8A(): pass

    label('loc_C8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C95',
    )

    def _loc_C95(): pass

    label('loc_C95')

    Jump('loc_CA6')

    def _loc_C98(): pass

    label('loc_C98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CA3',
    )

    def _loc_CA3(): pass

    label('loc_CA3')

    Jump('loc_CA6')

    def _loc_CA6(): pass

    label('loc_CA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_E84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CBE',
    )

    Event(0, 0x0039)

    def _loc_CBE(): pass

    label('loc_CBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CFE',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000A, 0x0010)
    SetChrChipByIndex(0x000A, 41)
    SetChrPos(0x0009, 88690, -1000, 51250, 0)
    SetChrPos(0x000A, 88700, -1000, 52960, 180)

    Jump('loc_D2A')

    def _loc_CFE(): pass

    label('loc_CFE')

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x0008, 88690, -1000, 51250, 0)
    SetChrPos(0x000B, 88700, -1000, 52960, 360)

    def _loc_D2A(): pass

    label('loc_D2A')

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 117200, 100, 1100, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 1, 0x1609)),
            Expr.Return,
        ),
        'loc_D4F',
    )

    SetChrSubChip(0x000C, 0)

    Jump('loc_D54')

    def _loc_D4F(): pass

    label('loc_D4F')

    SetChrSubChip(0x000C, 2)

    def _loc_D54(): pass

    label('loc_D54')

    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 114820, 0, 11500, 180)
    ClearChrFlags(0x0037, 0x0080)
    SetChrPos(0x0037, 116990, 0, 10300, 56)
    ClearChrFlags(0x0038, 0x0080)
    SetChrPos(0x0038, 89290, 100, -3120, 0)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, 84670, 100, -1300, 0)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001C, 86270, 0, 46740, 0)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x001D, 28120, 0, -8480, 270)
    ClearChrFlags(0x0021, 0x0080)
    SetChrPos(0x0021, 113220, 100, 1280, 0)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 91080, 0, 48580, 90)
    ClearChrFlags(0x0027, 0x0080)
    SetChrPos(0x0027, 116700, 100, 5250, 0)
    ClearChrFlags(0x0033, 0x0080)
    SetChrPos(0x0033, 88750, 100, 520, 0)
    ClearChrFlags(0x0034, 0x0080)
    SetChrPos(0x0034, 87730, 0, 1190, 135)
    ClearChrFlags(0x0035, 0x0080)
    SetChrPos(0x0035, 85440, 100, -4860, 0)
    ClearChrFlags(0x0036, 0x0080)
    SetChrPos(0x0036, 114160, 100, -2480, 0)

    Jump('loc_F0F')

    def _loc_E84(): pass

    label('loc_E84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 3, 0x1403)),
            Expr.Return,
        ),
        'loc_F0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E9C',
    )

    Event(0, 0x0039)

    def _loc_E9C(): pass

    label('loc_E9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_EAB',
    )

    ClearChrFlags(0x0009, 0x0080)

    Jump('loc_EB0')

    def _loc_EAB(): pass

    label('loc_EAB')

    ClearChrFlags(0x0008, 0x0080)

    def _loc_EB0(): pass

    label('loc_EB0')

    ClearChrFlags(0x000A, 0x0080)
    SetChrSubChip(0x000E, 5)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0039, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)

    def _loc_F0F(): pass

    label('loc_F0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F1E',
    )

    Event(0, 0x002B)

    Jump('loc_113E')

    def _loc_F1E(): pass

    label('loc_F1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_F5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 3, 0x1A03)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 4, 0x1A04)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 6, 0x1A06)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 7, 0x1A07)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 1, 0x1A09)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 3, 0x1A0B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F47',
    )

    Event(1, 0x0010)

    Jump('loc_F57')

    def _loc_F47(): pass

    label('loc_F47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            (Expr.TestScenaFlags, ScenaFlag(0x034F, 1, 0x1A79)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F57',
    )

    Event(1, 0x0006)

    def _loc_F57(): pass

    label('loc_F57')

    Jump('loc_113E')

    def _loc_F5A(): pass

    label('loc_F5A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1000',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F81',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 3, 0x180B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F7E',
    )

    Event(1, 0x0004)

    def _loc_F7E(): pass

    label('loc_F7E')

    Jump('loc_FFD')

    def _loc_F81(): pass

    label('loc_F81')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x73),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FFD',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 7, 0x1807)),
            Expr.Return,
        ),
        'loc_FA8',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_FA8(): pass

    label('loc_FA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 0, 0x1808)),
            Expr.Return,
        ),
        'loc_FB9',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_FB9(): pass

    label('loc_FB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 1, 0x1809)),
            Expr.Return,
        ),
        'loc_FCA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_FCA(): pass

    label('loc_FCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 2, 0x180A)),
            Expr.Return,
        ),
        'loc_FDB',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_FDB(): pass

    label('loc_FDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 3, 0x180B)),
            Expr.Return,
        ),
        'loc_FEC',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_FEC(): pass

    label('loc_FEC')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_FFD',
    )

    Event(1, 0x0005)

    def _loc_FFD(): pass

    label('loc_FFD')

    Jump('loc_113E')

    def _loc_1000(): pass

    label('loc_1000')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_103C'),
        (0x00000066, 'loc_103C'),
        (0x00000067, 'loc_103C'),
        (0x00000068, 'loc_103C'),
        (0x00000069, 'loc_103C'),
        (0x0000006A, 'loc_103C'),
        (0x0000006B, 'loc_103C'),
        (0x0000006D, 'loc_103C'),
        (0x0000006E, 'loc_103C'),
        (0x00000070, 'loc_103C'),
        (0x00000071, 'loc_103C'),
        (0x00000072, 'loc_103C'),
        (0x00000073, 'loc_103C'),
        (-1, 'loc_113E'),
    )

    def _loc_103C(): pass

    label('loc_103C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 1, 0x1681)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_104F',
    )

    Event(0, 0x0031)

    Jump('loc_113E')

    def _loc_104F(): pass

    label('loc_104F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_10C9',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 3, 0x1603)),
            Expr.Return,
        ),
        'loc_1071',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1071(): pass

    label('loc_1071')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 5, 0x1605)),
            Expr.Return,
        ),
        'loc_1082',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1082(): pass

    label('loc_1082')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 7, 0x1607)),
            Expr.Return,
        ),
        'loc_1093',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1093(): pass

    label('loc_1093')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 0, 0x1608)),
            Expr.Return,
        ),
        'loc_10A4',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_10A4(): pass

    label('loc_10A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 2, 0x160A)),
            Expr.Return,
        ),
        'loc_10B5',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_10B5(): pass

    label('loc_10B5')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_10C6',
    )

    Event(0, 0x0036)

    def _loc_10C6(): pass

    label('loc_10C6')

    Jump('loc_113E')

    def _loc_10C9(): pass

    label('loc_10C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 2, 0x122A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0248, 0, 0x1240)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10DC',
    )

    Event(0, 0x002C)

    Jump('loc_113E')

    def _loc_10DC(): pass

    label('loc_10DC')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 4, 0x1404)),
            Expr.Return,
        ),
        'loc_10F7',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_10F7(): pass

    label('loc_10F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 5, 0x1405)),
            Expr.Return,
        ),
        'loc_1108',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1108(): pass

    label('loc_1108')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 6, 0x1406)),
            Expr.Return,
        ),
        'loc_1119',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1119(): pass

    label('loc_1119')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 7, 0x1407)),
            Expr.Return,
        ),
        'loc_112A',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_112A(): pass

    label('loc_112A')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_113B',
    )

    Event(0, 0x0030)

    def _loc_113B(): pass

    label('loc_113B')

    Jump('loc_113E')

    def _loc_113E(): pass

    label('loc_113E')

    Return()

# id: 0x0001 offset: 0x113F
@scena.Code('Init')
def Init():
    OP_10(0x00, 0x00)
    OP_22(0x007A, 0x01, 0x46)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0216, 7, 0x10B7)),
            Expr.Return,
        ),
        'loc_1153',
    )

    SetChrFlags(0x0039, 0x0080)

    def _loc_1153(): pass

    label('loc_1153')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1168',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1168(): pass

    label('loc_1168')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11A7',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6D),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_118B',
    )

    Call(0, 0x0037)

    Jump('loc_11A7')

    def _loc_118B(): pass

    label('loc_118B')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A7',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x1),
            (Expr.PushLong, 0x49),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A7',
    )

    Call(0, 0x0038)

    def _loc_11A7(): pass

    label('loc_11A7')

    Return()

# id: 0x0002 offset: 0x11A8
@scena.Code('ReInit')
def ReInit():
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
        'loc_11CD',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_130F')

    def _loc_11CD(): pass

    label('loc_11CD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11E6',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_130F')

    def _loc_11E6(): pass

    label('loc_11E6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11FF',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_130F')

    def _loc_11FF(): pass

    label('loc_11FF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1218',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_130F')

    def _loc_1218(): pass

    label('loc_1218')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1231',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_130F')

    def _loc_1231(): pass

    label('loc_1231')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_124A',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_130F')

    def _loc_124A(): pass

    label('loc_124A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1263',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_130F')

    def _loc_1263(): pass

    label('loc_1263')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_127C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_130F')

    def _loc_127C(): pass

    label('loc_127C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1295',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_130F')

    def _loc_1295(): pass

    label('loc_1295')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12AE',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_130F')

    def _loc_12AE(): pass

    label('loc_12AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12C7',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_130F')

    def _loc_12C7(): pass

    label('loc_12C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12E0',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_130F')

    def _loc_12E0(): pass

    label('loc_12E0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12F9',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_130F')

    def _loc_12F9(): pass

    label('loc_12F9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_130F',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_130F(): pass

    label('loc_130F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1324',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_130F')

    def _loc_1324(): pass

    label('loc_1324')

    Return()

# id: 0x0003 offset: 0x1325
@scena.Code('func_03_1325')
def func_03_1325():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_13FE',
    )

    def _loc_132C(): pass

    label('loc_132C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_13FE',
    )

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_1362',
    )

    SetChrSubChip(0x00FE, 0)
    Sleep(50)

    SetChrSubChip(0x00FE, 1)
    Sleep(50)

    SetChrSubChip(0x00FE, 2)

    Jump('loc_137B')

    def _loc_1362(): pass

    label('loc_1362')

    SetChrSubChip(0x00FE, 0)
    Sleep(150)

    SetChrSubChip(0x00FE, 1)
    Sleep(150)

    SetChrSubChip(0x00FE, 2)

    def _loc_137B(): pass

    label('loc_137B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 7, 0x1F)),
            Expr.Return,
        ),
        'loc_1388',
    )

    OP_A3(0x001F)

    Jump('loc_13C4')

    def _loc_1388(): pass

    label('loc_1388')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x5),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_13C4',
    )

    Sleep(80)

    SetChrSubChip(0x00FE, 3)
    Sleep(100)

    SetChrSubChip(0x00FE, 4)
    Sleep(150)

    SetChrSubChip(0x00FE, 3)
    Sleep(100)

    SetChrSubChip(0x00FE, 2)
    OP_A2(0x001F)

    def _loc_13C4(): pass

    label('loc_13C4')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_13E7',
    )

    Sleep(50)

    SetChrSubChip(0x00FE, 1)
    Sleep(50)

    Jump('loc_13FB')

    def _loc_13E7(): pass

    label('loc_13E7')

    SetChrSubChip(0x00FE, 2)
    Sleep(150)

    SetChrSubChip(0x00FE, 1)
    Sleep(150)

    def _loc_13FB(): pass

    label('loc_13FB')

    Jump('loc_132C')

    def _loc_13FE(): pass

    label('loc_13FE')

    Return()

# id: 0x0004 offset: 0x13FF
@scena.Code('func_04_13FF')
def func_04_13FF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_14B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 3, 0x1A03)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1415',
    )

    Call(1, 0x0007)

    Jump('loc_14AF')

    def _loc_1415(): pass

    label('loc_1415')

    TalkBegin(0x0008)
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '#0050300292V#552F话先说在前头，要回村子\n',
            '等工作解决了再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300293V可别叫我特地带你过去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300294V#1007F小气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 270, 0)
    TalkEnd(0x0008)

    def _loc_14AF(): pass

    label('loc_14AF')

    Jump('loc_15D1')

    def _loc_14B2(): pass

    label('loc_14B2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C5',
    )

    Call(1, 0x0000)

    Jump('loc_15D1')

    def _loc_14C5(): pass

    label('loc_14C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_15CD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 3, 0x1603)),
            Expr.Return,
        ),
        'loc_15C6',
    )

    TalkBegin(0x0008)
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_14F8',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_1513')

    def _loc_14F8(): pass

    label('loc_14F8')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_150E',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_1513')

    def _loc_150E(): pass

    label('loc_150E')

    SetChrSubChip(0x00FE, 1)

    def _loc_1513(): pass

    label('loc_1513')

    OP_8C(0x0008, 360, 0)
    SetChrFlags(0x0008, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0050240383V#555F话说回来军方要求谈话啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240384V特地叫我们去王都\n',
            '可能需要保守秘密吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240385V结社的动向也令人在意,\n',
            '看来暂时还不能放松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Jump('loc_15CA')

    def _loc_15C6(): pass

    label('loc_15C6')

    Call(0, 0x0032)
    def _loc_15CA(): pass

    label('loc_15CA')

    Jump('loc_15D1')

    def _loc_15CD(): pass

    label('loc_15CD')

    Call(0, 0x002D)

    def _loc_15D1(): pass

    label('loc_15D1')

    Return()

# id: 0x0005 offset: 0x15D2
@scena.Code('func_05_15D2')
def func_05_15D2():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_175A',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_166E',
    )

    Jump('loc_16B0')

    def _loc_166E(): pass

    label('loc_166E')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_168A',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_16B0')

    def _loc_168A(): pass

    label('loc_168A')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_16A6',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_16B0')

    def _loc_16A6(): pass

    label('loc_16A6')

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_16B0(): pass

    label('loc_16B0')

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0009, 0x0010)

    ChrTalk(
        0x0009,
        (
            '#0030280391V#027F到达柏斯之前\n',
            '会经过洛连特，\n',
            '时间还挺宽余。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280392V你可以散步或者在座位休息，\n',
            '随便做什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Jump('loc_1871')

    def _loc_175A(): pass

    label('loc_175A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_186D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 7, 0x1607)),
            Expr.Return,
        ),
        'loc_1866',
    )

    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_178D',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_17A8')

    def _loc_178D(): pass

    label('loc_178D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_17A3',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_17A8')

    def _loc_17A3(): pass

    label('loc_17A3')

    SetChrSubChip(0x00FE, 1)

    def _loc_17A8(): pass

    label('loc_17A8')

    OP_8C(0x0009, 360, 0)
    SetChrFlags(0x0009, 0x0010)

    ChrTalk(
        0x0009,
        (
            '#0030240490V#522F话说回来\n',
            '王国军要求谈话啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240491V特地叫我们去王都\n',
            '是不是需要保守秘密呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240492V#022F结社的动向也令人在意\n',
            '看来暂时还不能放松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Jump('loc_186A')

    def _loc_1866(): pass

    label('loc_1866')

    Call(0, 0x0034)
    def _loc_186A(): pass

    label('loc_186A')

    Jump('loc_1871')

    def _loc_186D(): pass

    label('loc_186D')

    Call(0, 0x002E)
    def _loc_1871(): pass

    label('loc_1871')

    Return()

# id: 0x0006 offset: 0x1872
@scena.Code('func_06_1872')
def func_06_1872():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_1A0A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 7, 0x1A07)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1888',
    )

    Call(1, 0x000A)

    Jump('loc_1A07')

    def _loc_1888(): pass

    label('loc_1888')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 6, 0x183E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 0, 0x1A08)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_189B',
    )

    Call(1, 0x000B)

    Jump('loc_1A07')

    def _loc_189B(): pass

    label('loc_189B')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000A)
    ClearChrFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_192B',
    )

    Jump('loc_196D')

    def _loc_192B(): pass

    label('loc_192B')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1947',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_196D')

    def _loc_1947(): pass

    label('loc_1947')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1963',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_196D')

    def _loc_1963(): pass

    label('loc_1963')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_196D(): pass

    label('loc_196D')

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000A, 0x0010)

    ChrTalk(
        0x000A,
        (
            '#0040300462V#030F说起来柏斯有那个美人市长\n',
            '和那清冷眼神的女佣吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300463V#031F呼，真期待能再会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000A, 0)
    TalkEnd(0x000A)

    def _loc_1A07(): pass

    label('loc_1A07')

    Jump('loc_1C45')

    def _loc_1A0A(): pass

    label('loc_1A0A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 3, 0x180B)),
            Expr.Return,
        ),
        'loc_1A21',
    )

    Call(1, 0x0004)

    def _loc_1A21(): pass

    label('loc_1A21')

    Jump('loc_1C45')

    def _loc_1A24(): pass

    label('loc_1A24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_1C41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 7, 0x1607)),
            Expr.Return,
        ),
        'loc_1C3A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B8E',
    )

    TalkBegin(0x000A)
    CreateThread(0x000A, 0x00, 0x00, 0x0003)
    OP_A2(0x0000)

    ChrTalk(
        0x000A,
        (
            '#0040240493V#032F雪拉倒是还好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240494V虽然酒量大但至少还会脸红，\n',
            '也会做出喝醉的举动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240495V#034F但是爱娜……\n',
            '喝多少都不动声色的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240496V结果我轻易地上了钩，\n',
            '每次劝酒就把整杯喝干……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240497V#037F……啊哈哈……哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240498V#1007F（嗯～看来还是\n',
            '不要再问下去了比较好。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Jump('loc_1C37')

    def _loc_1B8E(): pass

    label('loc_1B8E')

    TalkBegin(0x000A)
    CreateThread(0x000A, 0x00, 0x00, 0x0003)

    ChrTalk(
        0x000A,
        (
            '#0040240499V#034F爱娜……\n',
            '喝多少都不动声色的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240496V结果我轻易地上了钩，\n',
            '每次劝酒就把整杯喝干……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240497V#037F……啊哈哈……哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    def _loc_1C37(): pass

    label('loc_1C37')

    Jump('loc_1C3E')

    def _loc_1C3A(): pass

    label('loc_1C3A')

    Call(0, 0x0034)
    def _loc_1C3E(): pass

    label('loc_1C3E')

    Jump('loc_1C45')

    def _loc_1C41(): pass

    label('loc_1C41')

    Call(0, 0x002F)
    def _loc_1C45(): pass

    label('loc_1C45')

    Return()

# id: 0x0007 offset: 0x1C46
@scena.Code('func_07_1C46')
def func_07_1C46():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_1CD9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 4, 0x1A04)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C5C',
    )

    Call(1, 0x0008)

    Jump('loc_1CD6')

    def _loc_1C5C(): pass

    label('loc_1C5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 5, 0x1A05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C6B',
    )

    Call(1, 0x0009)

    Jump('loc_1CD6')

    def _loc_1C6B(): pass

    label('loc_1C6B')

    TalkBegin(0x000B)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0070300343V#060F米夏吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300344V#061F嘿嘿，要是见面了\n',
            '能做好朋友就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)
    OP_8C(0x00FE, 90, 400)

    def _loc_1CD6(): pass

    label('loc_1CD6')

    Jump('loc_1D9C')

    def _loc_1CD9(): pass

    label('loc_1CD9')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CEC',
    )

    Call(1, 0x0003)

    Jump('loc_1D9C')

    def _loc_1CEC(): pass

    label('loc_1CEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 3, 0x1603)),
            Expr.Return,
        ),
        'loc_1D98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 4, 0x1604)),
            Expr.Return,
        ),
        'loc_1D91',
    )

    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '#0070240407V#061F说到这个，之前在王都\n',
            '第一次看到埃尔赛尤号的时候,\n',
            '感觉真是一艘好漂亮的飞船呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240582V嘿嘿……不知道还能再见到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Jump('loc_1D95')

    def _loc_1D91(): pass

    label('loc_1D91')

    Call(0, 0x0033)

    def _loc_1D95(): pass

    label('loc_1D95')

    Jump('loc_1D9C')

    def _loc_1D98(): pass

    label('loc_1D98')

    Call(0, 0x0032)

    def _loc_1D9C(): pass

    label('loc_1D9C')

    Return()

# id: 0x0008 offset: 0x1D9D
@scena.Code('func_08_1D9D')
def func_08_1D9D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_1F31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 3, 0x1A0B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DB3',
    )

    Call(1, 0x000E)

    Jump('loc_1F2E')

    def _loc_1DB3(): pass

    label('loc_1DB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0308, 0, 0x1840)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 4, 0x1A0C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DC6',
    )

    Call(1, 0x000F)

    Jump('loc_1F2E')

    def _loc_1DC6(): pass

    label('loc_1DC6')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000C)
    ClearChrFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1E56',
    )

    Jump('loc_1E98')

    def _loc_1E56(): pass

    label('loc_1E56')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1E72',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E98')

    def _loc_1E72(): pass

    label('loc_1E72')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1E8E',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E98')

    def _loc_1E8E(): pass

    label('loc_1E8E')

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1E98(): pass

    label('loc_1E98')

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000C, 0x0010)

    ChrTalk(
        0x000C,
        (
            '#0080300567V#070F接下来的柏斯地区\n',
            '是靠近帝国的地方吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300568V真想看一次\n',
            '传说中的哈肯大门啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000C, 0)
    TalkEnd(0x000C)

    def _loc_1F2E(): pass

    label('loc_1F2E')

    Jump('loc_1F48')

    def _loc_1F31(): pass

    label('loc_1F31')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F44',
    )

    Call(1, 0x0001)

    Jump('loc_1F48')

    def _loc_1F44(): pass

    label('loc_1F44')

    Call(0, 0x0035)

    def _loc_1F48(): pass

    label('loc_1F48')

    Return()

# id: 0x0009 offset: 0x1F49
@scena.Code('func_09_1F49')
def func_09_1F49():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_20ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 1, 0x1A09)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F5F',
    )

    Call(1, 0x000C)

    Jump('loc_20EA')

    def _loc_1F5F(): pass

    label('loc_1F5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 7, 0x183F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 2, 0x1A0A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F72',
    )

    Call(1, 0x000D)

    Jump('loc_20EA')

    def _loc_1F72(): pass

    label('loc_1F72')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000D)
    ClearChrFlags(0x000D, 0x0010)
    ChrTurnDirection(0x000D, 0x0000, 0)

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2002',
    )

    Jump('loc_2044')

    def _loc_2002(): pass

    label('loc_2002')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_201E',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2044')

    def _loc_201E(): pass

    label('loc_201E')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_203A',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2044')

    def _loc_203A(): pass

    label('loc_203A')

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2044(): pass

    label('loc_2044')

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000D, 0x0010)

    ChrTalk(
        0x000D,
        (
            '#0060300511V#048F呵呵，话说回来\n',
            '好久没去柏斯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300512V自从和乔儿一起去柏斯超市\n',
            '买东西以后就再也没去过了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000D, 0)
    TalkEnd(0x000D)

    def _loc_20EA(): pass

    label('loc_20EA')

    Jump('loc_20F1')

    def _loc_20ED(): pass

    label('loc_20ED')

    Call(1, 0x0002)
    def _loc_20F1(): pass

    label('loc_20F1')

    Return()

# id: 0x000A offset: 0x20F2
@scena.Code('func_0A_20F2')
def func_0A_20F2():
    TalkBegin(0x0016)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2163',
    )

    ChrTalk(
        0x00FE,
        (
            '现在右手边\n',
            '正好能看到迷雾峡谷哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这迷雾高峰的深处，\n',
            '就是和帝国之间的国境线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F7')

    def _loc_2163(): pass

    label('loc_2163')

    ChrTalk(
        0x00FE,
        (
            '哎呀，客人……\n',
            '感谢您经常选择我们的服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在右手边\n',
            '正好能看到迷雾峡谷哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特的雾虽然散了，\n',
            '但那里的雾却是一年到头都是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_21F7(): pass

    label('loc_21F7')

    Jump('loc_24D9')

    def _loc_21FA(): pass

    label('loc_21FA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_230C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2270',
    )

    ChrTalk(
        0x00FE,
        (
            '本船现在正在\n',
            '神秘森林上空飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在抵达下一个停靠地洛连特市之前，\n',
            '请尽情享受空中之旅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2309')

    def _loc_2270(): pass

    label('loc_2270')

    ChrTalk(
        0x00FE,
        (
            '……各位，请看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '右手边能看到的是\n',
            '利贝尔王国最大的森林地帯，\n',
            '神秘森林。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在林业也非常繁荣，\n',
            '国内消费木材的七成\n',
            '据说都是产自这座森林。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_2309(): pass

    label('loc_2309')

    Jump('loc_24D9')

    def _loc_230C(): pass

    label('loc_230C')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_241A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_236E',
    )

    ChrTalk(
        0x00FE,
        (
            '本船现在正在\n',
            '托兰特平原上空飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到达王都之前的时间\n',
            '请轻松度过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2417')

    def _loc_236E(): pass

    label('loc_236E')

    ChrTalk(
        0x00FE,
        (
            '现在右手边前方\n',
            '可以看到\n',
            '亚宁堡的长城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它的历史悠久，\n',
            '据说可以追溯到\n',
            '利贝尔王室诞生之前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一种说法其为古代塞姆利亚文明\n',
            '的遗迹，\n',
            '其真伪程度则无法判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_2417(): pass

    label('loc_2417')

    Jump('loc_24D9')

    def _loc_241A(): pass

    label('loc_241A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2476',
    )

    ChrTalk(
        0x00FE,
        (
            '本船现在正在\n',
            '卡鲁迪亚丘陵上空飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '预计将会\n',
            '准时抵达蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D9')

    def _loc_2476(): pass

    label('loc_2476')

    ChrTalk(
        0x00FE,
        (
            '现在右手边能看到的是\n',
            '南部广阔的特迪斯海。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然天气有点阴，\n',
            '但还是能看到海岸线的形状。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_24D9(): pass

    label('loc_24D9')

    TalkEnd(0x0016)

    Return()

# id: 0x000B offset: 0x24DD
@scena.Code('func_0B_24DD')
def func_0B_24DD():
    TalkBegin(0x0017)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2532',
    )

    ChrTalk(
        0x00FE,
        (
            '这次和共和国大使\n',
            '有大规模的贸易谈判。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能顺利进行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25F0')

    def _loc_2532(): pass

    label('loc_2532')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_258E',
    )

    ChrTalk(
        0x00FE,
        (
            '最近一直工作，\n',
            '都没时间休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回到蔡斯后\n',
            '打算先放松一阵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25F0')

    def _loc_258E(): pass

    label('loc_258E')

    ChrTalk(
        0x00FE,
        (
            '我现在正要\n',
            '回蔡斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一直工作，\n',
            '都没时间休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回到家后\n',
            '打算先放松一阵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_25F0(): pass

    label('loc_25F0')

    TalkEnd(0x0017)

    Return()

# id: 0x000C offset: 0x25F4
@scena.Code('func_0C_25F4')
def func_0C_25F4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_265A',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵……\n',
            '等一下哦，『埃尔赛尤』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要把那雪白的机体\n',
            '统统收入这台相机里～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2768')

    def _loc_265A(): pass

    label('loc_265A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2768',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2705',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈，接下来是蔡斯吗～\n',
            '工房船要是在飞船坪就好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '运气好的话，说不定\n',
            '『埃尔赛尤』也会来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔呼～我太兴奋了，\n',
            '拿相机的手都在颤抖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2768')

    def _loc_2705(): pass

    label('loc_2705')

    ChrTalk(
        0x00FE,
        (
            '好了～到达之前\n',
            '要好好准备相机才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有着陆的时候是从上方\n',
            '拍摄飞船坪的唯一机会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2768(): pass

    label('loc_2768')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x276C
@scena.Code('func_0D_276C')
def func_0D_276C():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_27DB',
    )

    ChrTalk(
        0x00FE,
        (
            '这次的互不侵犯条约是关键。\n',
            '若是签定的话行情也会上涨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这之前能买多少\n',
            '导力器就买多少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2834')

    def _loc_27DB(): pass

    label('loc_27DB')

    ChrTalk(
        0x00FE,
        (
            '西蒙，导力器那边\n',
            '确实都准备好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在帝国商人们来之前\n',
            '必须全部准备好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2834(): pass

    label('loc_2834')

    TalkEnd(0x0019)

    Return()

# id: 0x000E offset: 0x2838
@scena.Code('func_0E_2838')
def func_0E_2838():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2899',
    )

    ChrTalk(
        0x00FE,
        (
            '应、应该是按照这边提出的\n',
            '预算量准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再多的库存\n',
            '就要看今后的交涉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2904')

    def _loc_2899(): pass

    label('loc_2899')

    ChrTalk(
        0x00FE,
        (
            '是、是的，已经向中央工房的\n',
            '负责人传达过我们的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后只要办理具体的买卖合约\n',
            '手续就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2904(): pass

    label('loc_2904')

    TalkEnd(0x001A)

    Return()

# id: 0x000F offset: 0x2908
@scena.Code('func_0F_2908')
def func_0F_2908():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2982',
    )

    ChrTalk(
        0x00FE,
        (
            '这次的互不侵犯条约，\n',
            '是王国，帝国，共和国三大国\n',
            '之间所缔结的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真希望以此为契机\n',
            '三国的关系也得到发展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A2C')

    def _loc_2982(): pass

    label('loc_2982')

    ChrTalk(
        0x00FE,
        (
            '虽然卢安上下都在忙着选举，\n',
            '不过王国整体来说还是签字仪式最热门。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '毕竟是要和１０年前百日战役中\n',
            '战斗过的帝国缔结互不侵犯条约嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '希望以此为契机\n',
            '能够真正冰释前嫌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_2A2C(): pass

    label('loc_2A2C')

    TalkEnd(0x001B)

    Return()

# id: 0x0010 offset: 0x2A30
@scena.Code('func_10_2A30')
def func_10_2A30():
    TalkBegin(0x001C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2A8F',
    )

    ChrTalk(
        0x00FE,
        (
            '在洛连特\n',
            '给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样的雾，我们也是\n',
            '第一次经历呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AFA')

    def _loc_2A8F(): pass

    label('loc_2A8F')

    ChrTalk(
        0x00FE,
        (
            '啊啊，是客人您啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在洛连特\n',
            '给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再怎么说，要在那种浓雾下\n',
            '升空也太危险了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2AFA(): pass

    label('loc_2AFA')

    Jump('loc_2FBF')

    def _loc_2AFD(): pass

    label('loc_2AFD')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 1, 0x1809)),
            Expr.Return,
        ),
        'loc_2BE5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2B6C',
    )

    ChrTalk(
        0x00FE,
        (
            '孩提时代我也憧憬过\n',
            '王立学院呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在看来那里的制服\n',
            '设计依然十分出色哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BE2')

    def _loc_2B6C(): pass

    label('loc_2B6C')

    ChrTalk(
        0x00FE,
        (
            '孩提时代我也很向往\n',
            '王立学院呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然只是单纯\n',
            '想穿那个制服而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个……当然是男生穿的\n',
            '制服啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2BE2(): pass

    label('loc_2BE2')

    Jump('loc_2CB3')

    def _loc_2BE5(): pass

    label('loc_2BE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2C3D',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，名校的学生\n',
            '气质果然就是不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定接受了\n',
            '严格的教育吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CB3')

    def _loc_2C3D(): pass

    label('loc_2C3D')

    ChrTalk(
        0x00FE,
        (
            '那边的客人……\n',
            '是王立学院的学生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，不愧是名校的\n',
            '学生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一举一动之间\n',
            '都能透露出不凡的气质呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2CB3(): pass

    label('loc_2CB3')

    Jump('loc_2FBF')

    def _loc_2CB6(): pass

    label('loc_2CB6')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2D80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2D11',
    )

    ChrTalk(
        0x00FE,
        (
            '我是独生子，\n',
            '感觉真是寂寞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想要个\n',
            '弟弟或妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D7D')

    def _loc_2D11(): pass

    label('loc_2D11')

    ChrTalk(
        0x00FE,
        (
            '那边的\n',
            '客人是兄妹吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为兄妹来说\n',
            '感觉又不太一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，关系那么好\n',
            '让人不禁莞尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2D7D(): pass

    label('loc_2D7D')

    Jump('loc_2E94')

    def _loc_2D80(): pass

    label('loc_2D80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2DEC',
    )

    ChrTalk(
        0x00FE,
        (
            '那位弹鲁特琴的客人……\n',
            '怎么说呢，令人感觉到他对自身的爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就叫做\n',
            'Ｉ ＬＯＶＥ ＭＥ吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E94')

    def _loc_2DEC(): pass

    label('loc_2DEC')

    ChrTalk(
        0x00FE,
        (
            '那位弹鲁特琴的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅是吟唱诗歌的内容，\n',
            '连唱歌说话的方式都是那么独特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么说呢……\n',
            '令人感觉到他对自身的爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就叫做\n',
            'Ｉ ＬＯＶＥ ＭＥ吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2E94(): pass

    label('loc_2E94')

    Jump('loc_2FBF')

    def _loc_2E97(): pass

    label('loc_2E97')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FBF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2F26',
    )

    ChrTalk(
        0x00FE,
        (
            '这个观景席平时总是\n',
            '很受大家欢迎的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道为什么今天\n',
            '客人们都不在席上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这果然……\n',
            '都是因为那位客人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBF')

    def _loc_2F26(): pass

    label('loc_2F26')

    ChrTalk(
        0x00FE,
        (
            '那位客人，现在倒是\n',
            '很老实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过刚才还在弹奏鲁特琴\n',
            '大声唱歌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果还强求\n',
            '我去唱二重唱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，世上居然也有\n',
            '这么强人所难的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2FBF(): pass

    label('loc_2FBF')

    TalkEnd(0x001C)

    Return()

# id: 0x0011 offset: 0x2FC3
@scena.Code('func_11_2FC3')
def func_11_2FC3():
    TalkBegin(0x001D)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3099',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3022',
    )

    ChrTalk(
        0x00FE,
        (
            '起雾的洛连特\n',
            '也真是怪异。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也好久没能\n',
            '好好享受到自然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3096')

    def _loc_3022(): pass

    label('loc_3022')

    ChrTalk(
        0x00FE,
        (
            '哎呀～又是客人您啊。\n',
            '最近常常见到呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '起雾的洛连特\n',
            '也真是怪异。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也好久没能\n',
            '好好享受到自然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_3096(): pass

    label('loc_3096')

    Jump('loc_3306')

    def _loc_3099(): pass

    label('loc_3099')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_316D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_30F6',
    )

    ChrTalk(
        0x00FE,
        (
            '那位穿白色外套的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一个人在嘀嘀咕咕的\n',
            '到底是什么事呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_316A')

    def _loc_30F6(): pass

    label('loc_30F6')

    ChrTalk(
        0x00FE,
        (
            '刚才那边\n',
            '穿白色外套的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一个人在嘀嘀咕咕，\n',
            '到底是什么事呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '突然又笑出声来\n',
            '感觉真是危险啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_316A(): pass

    label('loc_316A')

    Jump('loc_3306')

    def _loc_316D(): pass

    label('loc_316D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_324F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_31D5',
    )

    ChrTalk(
        0x00FE,
        (
            '到王都可要早点做好\n',
            '卸货的准备啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次要卸下的货物量\n',
            '可不是普通的多哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_324C')

    def _loc_31D5(): pass

    label('loc_31D5')

    ChrTalk(
        0x00FE,
        (
            '呀，接下来是王都吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话就得早点做好\n',
            '卸货的准备才行啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在王都要卸下的货物量\n',
            '可不是普通的多哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_324C(): pass

    label('loc_324C')

    Jump('loc_3306')

    def _loc_324F(): pass

    label('loc_324F')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3306',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_32BF',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是货舱哦～\n',
            '很危险，要多加小心～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '操舵室在这个上面一层。\n',
            '十分推荐进去参观哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3306')

    def _loc_32BF(): pass

    label('loc_32BF')

    ChrTalk(
        0x00FE,
        (
            '哎呀～客人。\n',
            '怎么了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里是货舱哦～\n',
            '很危险，要多加小心～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_3306(): pass

    label('loc_3306')

    TalkEnd(0x001D)

    Return()

# id: 0x0012 offset: 0x330A
@scena.Code('func_12_330A')
def func_12_330A():
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_332C',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_333F')

    def _loc_332C(): pass

    label('loc_332C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_333F',
    )

    SetChrSubChip(0x00FE, 2)

    def _loc_333F(): pass

    label('loc_333F')

    OP_8C(0x00FE, 0, 0)
    SetChrFlags(0x00FE, 0x0010)
    TalkBegin(0x001E)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3481',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_33BE',
    )

    ChrTalk(
        0x00FE,
        (
            '这么浓的雾\n',
            '连我也是第一次看见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然打开灯之后\n',
            '也只是照出眼前白茫茫一片而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_347E')

    def _loc_33BE(): pass

    label('loc_33BE')

    ChrTalk(
        0x00FE,
        (
            '哟，出港延迟给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我干这工作这么久了\n',
            '这样的浓雾还是头一次见到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然打开灯之后\n',
            '也只是照出眼前白茫茫一片而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在这种状况下飞行\n',
            '就算是我也办不到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_347E(): pass

    label('loc_347E')

    Jump('loc_3708')

    def _loc_3481(): pass

    label('loc_3481')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3562',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_34DF',
    )

    ChrTalk(
        0x00FE,
        (
            '从这里望去的洛连特，\n',
            '满眼翠绿的风景很特别哦。\n',
            '感觉心灵都被治愈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355F')

    def _loc_34DF(): pass

    label('loc_34DF')

    ChrTalk(
        0x00FE,
        (
            '哦，来操舵室\n',
            '看风景吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这里望去的洛连特，\n',
            '满眼翠绿的风景很特别哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '眺望着雄伟的森林，\n',
            '感觉心灵都被治愈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_355F(): pass

    label('loc_355F')

    Jump('loc_3708')

    def _loc_3562(): pass

    label('loc_3562')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3643',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_35C6',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正在托兰特平原\n',
            '上空飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天气又好，到甲板上\n',
            '去看看风景怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3640')

    def _loc_35C6(): pass

    label('loc_35C6')

    ChrTalk(
        0x00FE,
        (
            '哦，不是在参观船内部吗？\n',
            '觉得无聊了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在托兰特平原\n',
            '上空飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天气又好，到甲板上\n',
            '看看风景怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_3640(): pass

    label('loc_3640')

    Jump('loc_3708')

    def _loc_3643(): pass

    label('loc_3643')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3708',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_36A7',
    )

    ChrTalk(
        0x00FE,
        (
            '天空也很平静，\n',
            '应该能准时到达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然这么悠闲，\n',
            '到船内散散步怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3708')

    def _loc_36A7(): pass

    label('loc_36A7')

    ChrTalk(
        0x00FE,
        (
            '哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天空也很平静，\n',
            '应该能准时到达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，再悠闲地\n',
            '享受一下空中旅行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_3708(): pass

    label('loc_3708')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x001E)

    Return()

# id: 0x0013 offset: 0x3711
@scena.Code('func_13_3711')
def func_13_3711():
    TalkBegin(0x001F)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3782',
    )

    ChrTalk(
        0x00FE,
        (
            '麻烦避开山脉边缘，\n',
            '将航向往南稍微修正一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉靠近东柏斯街道\n',
            '正上方的路线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37D5')

    def _loc_3782(): pass

    label('loc_3782')

    ChrTalk(
        0x00FE,
        (
            '操舵手。\n',
            '稍微偏西北了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于山脉边缘有乱流，\n',
            '太靠近的话就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_37D5(): pass

    label('loc_37D5')

    Jump('loc_39F8')

    def _loc_37D8(): pass

    label('loc_37D8')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_383E',
    )

    ChrTalk(
        0x00FE,
        (
            '操舵手，麻烦暂时\n',
            '固定在现在的航向上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～今天\n',
            '洛连特的风也很平静呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38A4')

    def _loc_383E(): pass

    label('loc_383E')

    ChrTalk(
        0x00FE,
        (
            '没必要修正航向。\n',
            '操舵手，舵保持这样就ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '保持航向……\n',
            '很快就会走上\n',
            '进入洛连特的路线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_38A4(): pass

    label('loc_38A4')

    Jump('loc_39F8')

    def _loc_38A7(): pass

    label('loc_38A7')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3962',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3910',
    )

    ChrTalk(
        0x00FE,
        (
            '今天感觉上面有点风\n',
            '吹下来似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这附近的风\n',
            '经常变化，\n',
            '要时时注意才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_395F')

    def _loc_3910(): pass

    label('loc_3910')

    ChrTalk(
        0x00FE,
        (
            '操舵手，高度好像稍微\n',
            '下降了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要离开气流，\n',
            '尽快修正高度吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_395F(): pass

    label('loc_395F')

    Jump('loc_39F8')

    def _loc_3962(): pass

    label('loc_3962')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_39B3',
    )

    ChrTalk(
        0x00FE,
        (
            '好像又吹海风了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这附近的空域\n',
            '总是不能放松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39F8')

    def _loc_39B3(): pass

    label('loc_39B3')

    ChrTalk(
        0x00FE,
        (
            '操舵手，麻烦\n',
            '修正一下线路吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '船尾感觉稍微\n',
            '偏北了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_39F8(): pass

    label('loc_39F8')

    TalkEnd(0x001F)

    Return()

# id: 0x0014 offset: 0x39FC
@scena.Code('func_14_39FC')
def func_14_39FC():
    TalkBegin(0x0020)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AB9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3A6B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦～⊙\n',
            '天空的～男人～哟～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这城～到那镇～⊙\n',
            '旅行的～乌鸦～～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AB6')

    def _loc_3A6B(): pass

    label('loc_3A6B')

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦～⊙\n',
            '是～明白了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '路线向南修正～\n',
            '呼啦啦呼啦啦～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3AB6(): pass

    label('loc_3AB6')

    Jump('loc_3C3C')

    def _loc_3AB9(): pass

    label('loc_3AB9')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B42',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3AF2',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦～⊙\n',
            '呼啦呼啦啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B3F')

    def _loc_3AF2(): pass

    label('loc_3AF2')

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦～⊙\n',
            '啊～明白了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就这样保持路线～\n',
            '呼啦啦呼啦啦～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3B3F(): pass

    label('loc_3B3F')

    Jump('loc_3C3C')

    def _loc_3B42(): pass

    label('loc_3B42')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3B7B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦⊙\n',
            '呼啦啦呼啦啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BC2')

    def _loc_3B7B(): pass

    label('loc_3B7B')

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦⊙\n',
            '是～明白了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '立即恢复高度～\n',
            '呼啦啦呼啦啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3BC2(): pass

    label('loc_3BC2')

    Jump('loc_3C3C')

    def _loc_3BC5(): pass

    label('loc_3BC5')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C3C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3BF1',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C3C')

    def _loc_3BF1(): pass

    label('loc_3BF1')

    ChrTalk(
        0x00FE,
        (
            '呼啦啦呼啦啦～⊙\n',
            '啊～明白了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '立即修正路线～\n',
            '呼啦啦呼啦啦～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3C3C(): pass

    label('loc_3C3C')

    TalkEnd(0x0020)

    Return()

# id: 0x0015 offset: 0x3C40
@scena.Code('func_15_3C40')
def func_15_3C40():
    TalkBegin(0x0021)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3C7C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，还真是\n',
            '夸张的大雾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CEC')

    def _loc_3C7C(): pass

    label('loc_3C7C')

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，还真是\n',
            '夸张的雾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还突然就\n',
            '消散得无影无踪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么诡异的雾\n',
            '连我都是第一次见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_3CEC(): pass

    label('loc_3CEC')

    Jump('loc_3EF5')

    def _loc_3CEF(): pass

    label('loc_3CEF')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3D61',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然说发布了安全宣告，\n',
            '却还是忍不住心惊肉跳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在坐在飞船上\n',
            '倒还算安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DE1')

    def _loc_3D61(): pass

    label('loc_3D61')

    ChrTalk(
        0x00FE,
        (
            '不过，蔡斯的\n',
            '地震也真是吓人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全部都是局部地震，\n',
            '而且还发生在很多地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我活了这么久，\n',
            '这还是头一次见到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_3DE1(): pass

    label('loc_3DE1')

    Jump('loc_3EF5')

    def _loc_3DE4(): pass

    label('loc_3DE4')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EF5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3E50',
    )

    ChrTalk(
        0x00FE,
        (
            '若不是通晓技术的人，\n',
            '是不可能统领蔡斯市的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让工房长兼任市长\n',
            '真是个好主意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EF5')

    def _loc_3E50(): pass

    label('loc_3E50')

    ChrTalk(
        0x00FE,
        (
            '卢安市正热衷于\n',
            '市长选举……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在要去的蔡斯市\n',
            '却没有市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '取而代之的是由中央工房\n',
            '的工房长统领整个地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是个适合工房都市的\n',
            '管理架构啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_3EF5(): pass

    label('loc_3EF5')

    TalkEnd(0x0021)

    Return()

# id: 0x0016 offset: 0x3EF9
@scena.Code('func_16_3EF9')
def func_16_3EF9():
    TalkBegin(0x0022)

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约的签字仪式\n',
            '似乎顺利结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，希望以此为契机\n',
            '来促进三国的融洽关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0022)

    Return()

# id: 0x0017 offset: 0x3F5C
@scena.Code('func_17_3F5C')
def func_17_3F5C():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_3F94',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯有家著名的\n',
            '餐厅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FE3')

    def _loc_3F94(): pass

    label('loc_3F94')

    ChrTalk(
        0x00FE,
        (
            '柏斯有家著名的\n',
            '餐厅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，妈妈～\n',
            '去那里吃饭嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    def _loc_3FE3(): pass

    label('loc_3FE3')

    TalkEnd(0x0023)

    Return()

# id: 0x0018 offset: 0x3FE7
@scena.Code('func_18_3FE7')
def func_18_3FE7():
    TalkBegin(0x0024)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_4046',
    )

    ChrTalk(
        0x00FE,
        (
            '我家的孩子居然说\n',
            '想去那个安特洛丝\n',
            '吃饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小孩子真是天真。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40AF')

    def _loc_4046(): pass

    label('loc_4046')

    ChrTalk(
        0x00FE,
        (
            '真是的，我家这孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然说想去那个安特洛丝\n',
            '吃饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真好。\n',
            '小孩子就是这么天真。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    def _loc_40AF(): pass

    label('loc_40AF')

    Jump('loc_41CB')

    def _loc_40B2(): pass

    label('loc_40B2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_4122',
    )

    ChrTalk(
        0x00FE,
        (
            '艾德尔百货商店里的\n',
            '商品质量确实好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近，那家百货店\n',
            '似乎也成为流行的发源地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41CB')

    def _loc_4122(): pass

    label('loc_4122')

    ChrTalk(
        0x00FE,
        (
            '说到要去王都购物的话，\n',
            '首选就是艾德尔百货店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然好像比柏斯超市\n',
            '规模要小，\n',
            '但是商品质量的确很好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～啊，要是有时间和钱的话，\n',
            '真想顺路去购物啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    def _loc_41CB(): pass

    label('loc_41CB')

    TalkEnd(0x0024)

    Return()

# id: 0x0019 offset: 0x41CF
@scena.Code('func_19_41CF')
def func_19_41CF():
    TalkBegin(0x0025)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4289',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_4226',
    )

    ChrTalk(
        0x00FE,
        (
            '这阵子\n',
            '柏斯好像很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，柏斯超市\n',
            '想必很热闹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4286')

    def _loc_4226(): pass

    label('loc_4226')

    ChrTalk(
        0x00FE,
        (
            '这阵子\n',
            '柏斯好像很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯上\n',
            '没什么特别的报道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，真应该\n',
            '感到高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_4286(): pass

    label('loc_4286')

    Jump('loc_4365')

    def _loc_4289(): pass

    label('loc_4289')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4365',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_42E9',
    )

    ChrTalk(
        0x00FE,
        (
            '这次的互不侵犯条约，\n',
            '我原则上是支持的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能重归于好\n',
            '总是件好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4365')

    def _loc_42E9(): pass

    label('loc_42E9')

    ChrTalk(
        0x00FE,
        (
            '这次的互不侵犯条约，\n',
            '我原则上是支持的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于帝国，老实说\n',
            '感觉依然很复杂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之能重归于好\n',
            '还是件好事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_4365(): pass

    label('loc_4365')

    TalkEnd(0x0025)

    Return()

# id: 0x001A offset: 0x4369
@scena.Code('func_1A_4369')
def func_1A_4369():
    TalkBegin(0x0026)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_445F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_43E6',
    )

    ChrTalk(
        0x00FE,
        (
            '那个艾德尔百货店的店长\n',
            '好像也是超市的爱好者呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在店长所写的巡礼札记里\n',
            '好像提过这样的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_445C')

    def _loc_43E6(): pass

    label('loc_43E6')

    ChrTalk(
        0x00FE,
        (
            '柏斯的超市\n',
            '简直是购物的天堂……\n',
            '对女性来说是个向往之地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个艾德尔百货店的店长\n',
            '也是私底下的爱好者呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_445C(): pass

    label('loc_445C')

    Jump('loc_44D1')

    def _loc_445F(): pass

    label('loc_445F')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44D1',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约好像是三国之间\n',
            '所缔结的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能维持帝国和共和国的关系\n',
            '真不愧是艾莉茜雅女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44D1(): pass

    label('loc_44D1')

    TalkEnd(0x0026)

    Return()

# id: 0x001B offset: 0x44D5
@scena.Code('func_1B_44D5')
def func_1B_44D5():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x27, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x05,
        (
            (Expr.GetChrWork, 0x27, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0027)
    ClearChrFlags(0x0027, 0x0010)
    ChrTurnDirection(0x0027, 0x0000, 0)

    ExecExpressionWithValue(
        0x0027,
        0x04,
        (
            (Expr.GetChrWork, 0x27, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x04,
        (
            (Expr.GetChrWork, 0x27, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x27, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x05,
        (
            (Expr.GetChrWork, 0x27, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x27, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x27, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x27, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x27, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4565',
    )

    Jump('loc_45A7')

    def _loc_4565(): pass

    label('loc_4565')

    If(
        (
            (Expr.GetChrWork, 0x27, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4581',
    )

    ExecExpressionWithValue(
        0x0027,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_45A7')

    def _loc_4581(): pass

    label('loc_4581')

    If(
        (
            (Expr.GetChrWork, 0x27, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_459D',
    )

    ExecExpressionWithValue(
        0x0027,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_45A7')

    def _loc_459D(): pass

    label('loc_459D')

    ExecExpressionWithValue(
        0x0027,
        0x08,
        (
            (Expr.GetChrWork, 0x27, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_45A7(): pass

    label('loc_45A7')

    ExecExpressionWithValue(
        0x0027,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0027, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4625',
    )

    ChrTalk(
        0x00FE,
        (
            '瓦雷利亚湖畔\n',
            '好像有不错的旅店哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近在钓客之间\n',
            '似乎很流行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4877')

    def _loc_4625(): pass

    label('loc_4625')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4750',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_469B',
    )

    ChrTalk(
        0x00FE,
        (
            '当天，签字仪式会场的离宫\n',
            '好像一律禁止民间人士入内呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想亲眼目睹\n',
            '条约缔结的瞬间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_474D')

    def _loc_469B(): pass

    label('loc_469B')

    ChrTalk(
        0x00FE,
        (
            '这次的互不侵犯条约签字仪式……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当天，会场艾尔贝离宫\n',
            '好像一律禁止民间人士入内呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟刚刚发生过政变，\n',
            '这也是没办法的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想亲眼目睹\n',
            '条约缔结的瞬间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_474D(): pass

    label('loc_474D')

    Jump('loc_4877')

    def _loc_4750(): pass

    label('loc_4750')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4877',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_47EB',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，旧情报部的残党\n',
            '好像还没有抓到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然大家可能都忘了，\n',
            '但实在是非常可怕的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，和平这种东西\n',
            '真是容易破坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4877')

    def _loc_47EB(): pass

    label('loc_47EB')

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约的签字仪式\n',
            '似乎在艾尔贝离宫进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到艾尔贝离宫……\n',
            '就想起理查德的事件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙似乎被拘禁在\n',
            '雷斯顿要塞里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_4877(): pass

    label('loc_4877')

    SetChrSubChip(0x0027, 0)
    TalkEnd(0x0027)

    Return()

# id: 0x001C offset: 0x4880
@scena.Code('func_1C_4880')
def func_1C_4880():
    TalkBegin(0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_48FD',
    )

    ChrTalk(
        0x00FE,
        (
            '对士兵们来说\n',
            '帝国的存在似乎还是\n',
            '相当大的心理负担啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的互不侵犯条约\n',
            '最支持的人，\n',
            '说不定是他们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_498A')

    def _loc_48FD(): pass

    label('loc_48FD')

    ChrTalk(
        0x00FE,
        (
            '我的朋友是驻扎在\n',
            '哈肯大门的士兵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国的存在似乎还是\n',
            '相当大的心理负担啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的互不侵犯条约\n',
            '最支持的\n',
            '说不定是士兵们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0014)

    def _loc_498A(): pass

    label('loc_498A')

    TalkEnd(0x0028)

    Return()

# id: 0x001D offset: 0x498E
@scena.Code('func_1D_498E')
def func_1D_498E():
    TalkBegin(0x002A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 5, 0x1D)),
            Expr.Return,
        ),
        'loc_49F9',
    )

    ChrTalk(
        0x00FE,
        (
            '遗憾的是这女孩\n',
            '似乎很快要去柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是这孩子的话，我儿子里农\n',
            '应该也会喜欢的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A9D')

    def _loc_49F9(): pass

    label('loc_49F9')

    ChrTalk(
        0x00FE,
        (
            '呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果，王都也找不到\n',
            '能做里农新娘的女孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回来的船上能遇到谈得来的女孩\n',
            '可以说是捡到救命稻草了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的孩子我儿子里农\n',
            '一定会喜欢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001D)

    def _loc_4A9D(): pass

    label('loc_4A9D')

    TalkEnd(0x002A)

    Return()

# id: 0x001E offset: 0x4AA1
@scena.Code('func_1E_4AA1')
def func_1E_4AA1():
    TalkBegin(0x002B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 6, 0x1E)),
            Expr.Return,
        ),
        'loc_4B19',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然很想去看看\n',
            '婆婆的店……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在利用休假\n',
            '正要去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得能够彼此认识，\n',
            '真有点可惜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BC0')

    def _loc_4B19(): pass

    label('loc_4B19')

    ChrTalk(
        0x00FE,
        (
            '这位婆婆似乎在洛连特\n',
            '经营商店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也在王都的百货店工作\n',
            '所以很谈得来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '个人经营的商店…\n',
            '实在是很不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪怕是家很小的店，\n',
            '我也想自己开店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001E)

    def _loc_4BC0(): pass

    label('loc_4BC0')

    TalkEnd(0x002B)

    Return()

# id: 0x001F offset: 0x4BC4
@scena.Code('func_1F_4BC4')
def func_1F_4BC4():
    TalkBegin(0x002C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_4C3A',
    )

    ChrTalk(
        0x00FE,
        (
            '呀～神秘森林的\n',
            '风景虽然很不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但那边的女乘务员\n',
            '也毫不逊色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～越来越不想\n',
            '下船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CCB')

    def _loc_4C3A(): pass

    label('loc_4C3A')

    ChrTalk(
        0x00FE,
        (
            '呀～从飞船上看\n',
            '神秘森林真是壮观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看见这片大森林\n',
            '就能感受到洛连特地区\n',
            '多么受大自然的眷顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～真想就这样\n',
            '一直眺望下去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    def _loc_4CCB(): pass

    label('loc_4CCB')

    TalkEnd(0x002C)

    Return()

# id: 0x0020 offset: 0x4CCF
@scena.Code('func_20_4CCF')
def func_20_4CCF():
    TalkBegin(0x002D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_4D34',
    )

    ChrTalk(
        0x00FE,
        (
            '洛连特好像也有\n',
            '很不错的钓场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不是很出名，\n',
            '感觉是个罕为人知的好地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DBC')

    def _loc_4D34(): pass

    label('loc_4D34')

    ChrTalk(
        0x00FE,
        (
            '洛连特好像也有\n',
            '很不错的钓场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不是很出名，\n',
            '感觉是个罕为人知的好地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～真想在到站之后\n',
            '先去挑战一下试试啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0016)

    def _loc_4DBC(): pass

    label('loc_4DBC')

    TalkEnd(0x002D)

    Return()

# id: 0x0021 offset: 0x4DC0
@scena.Code('func_21_4DC0')
def func_21_4DC0():
    TalkBegin(0x002E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_4E3F',
    )

    ChrTalk(
        0x00FE,
        (
            '洛连特地区是我很想好好\n',
            '游览一下的地方之一呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '美味的食物加上清新的空气……\n',
            '真是个雕琢美丽的最佳环境啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EF7')

    def _loc_4E3F(): pass

    label('loc_4E3F')

    ChrTalk(
        0x00FE,
        (
            '下一个停靠港是洛连特啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次虽然不去，\n',
            '但以后真想去农场住一阵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '美味的食物加上清新的空气……\n',
            '真是个雕琢美丽的最佳环境啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，他也想钓鱼\n',
            '下次约他看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0017)

    def _loc_4EF7(): pass

    label('loc_4EF7')

    TalkEnd(0x002E)

    Return()

# id: 0x0022 offset: 0x4EFB
@scena.Code('func_22_4EFB')
def func_22_4EFB():
    TalkBegin(0x002F)

    ChrTalk(
        0x00FE,
        (
            '明天终于就是\n',
            '那个互不侵犯条约的签字仪式了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '百日战役终结\n',
            '已经过了１０年了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许是该和帝国\n',
            '重归于好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x002F)

    Return()

# id: 0x0023 offset: 0x4F7F
@scena.Code('func_23_4F7F')
def func_23_4F7F():
    TalkBegin(0x0030)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_4FDE',
    )

    ChrTalk(
        0x00FE,
        (
            '和帝国和解的时候\n',
            '总算要真正到来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样回想起来\n',
            '１０年真是转眼即逝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_506C')

    def _loc_4FDE(): pass

    label('loc_4FDE')

    ChrTalk(
        0x00FE,
        (
            '不久前还完全无法想象\n',
            '能够和帝国和解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个时刻\n',
            '总算要真正到来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是不断踏实地进行外交努力的\n',
            '艾莉茜雅女王陛下的胜利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0019)

    def _loc_506C(): pass

    label('loc_506C')

    TalkEnd(0x0030)

    Return()

# id: 0x0024 offset: 0x5070
@scena.Code('func_24_5070')
def func_24_5070():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5100',
    )

    Jump('loc_5142')

    def _loc_5100(): pass

    label('loc_5100')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_511C',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5142')

    def _loc_511C(): pass

    label('loc_511C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_5138',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5142')

    def _loc_5138(): pass

    label('loc_5138')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5142(): pass

    label('loc_5142')

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Return,
        ),
        'loc_51C7',
    )

    ChrTalk(
        0x00FE,
        (
            '得赶快把事情办完，\n',
            '赶快回家才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我老婆只会使唤人，\n',
            '还啰嗦…真是受够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5223')

    def _loc_51C7(): pass

    label('loc_51C7')

    ChrTalk(
        0x00FE,
        (
            '今天也是老婆叫我\n',
            '非去趟柏斯超市\n',
            '不可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我老婆只会使唤人，\n',
            '还啰嗦…真是受够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001A)

    def _loc_5223(): pass

    label('loc_5223')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x522C
@scena.Code('func_25_522C')
def func_25_522C():
    TalkBegin(0x0032)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，我要去柏斯超市\n',
            '帮爸爸买东西哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买东西，买东西，好开心～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0032)

    Return()

# id: 0x0026 offset: 0x527E
@scena.Code('func_26_527E')
def func_26_527E():
    TalkBegin(0x0033)

    ChrTalk(
        0x00FE,
        (
            '说不行就是不行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你啊，之前也是这么说\n',
            '结果又爬上甲板栏杆的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何，\n',
            '都要给我乖乖待在这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0033, 0)
    TalkEnd(0x0033)
    TalkEnd(0x0033)

    Return()

# id: 0x0027 offset: 0x52FD
@scena.Code('func_27_52FD')
def func_27_52FD():
    TalkBegin(0x0034)

    ChrTalk(
        0x00FE,
        (
            '来啦，姐姐～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别老是坐着，\n',
            '出去外面啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我绝对会\n',
            '乖乖听话的啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0034)

    Return()

# id: 0x0028 offset: 0x5352
@scena.Code('func_28_5352')
def func_28_5352():
    TalkBegin(0x0035)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Return,
        ),
        'loc_53A9',
    )

    ChrTalk(
        0x00FE,
        (
            '听说政变的主谋\n',
            '全都抓住了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过说不定有人\n',
            '已经逃亡到国外了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5438')

    def _loc_53A9(): pass

    label('loc_53A9')

    ChrTalk(
        0x00FE,
        (
            '唔，接下来是艾莉茜雅女王的\n',
            '所在地，花之都格兰赛尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然内心是雀跃不已,\n',
            '但总忍不住\n',
            '想起政变的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望别再发生第二次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001B)

    def _loc_5438(): pass

    label('loc_5438')

    TalkEnd(0x0035)

    Return()

# id: 0x0029 offset: 0x543C
@scena.Code('func_29_543C')
def func_29_543C():
    TalkBegin(0x0036)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 4, 0x1C)),
            Expr.Return,
        ),
        'loc_5495',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，卢安\n',
            '好像有什么\n',
            '出现幽灵的奇怪传言……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之后怎样了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_554E')

    def _loc_5495(): pass

    label('loc_5495')

    ChrTalk(
        0x00FE,
        (
            '……说起来，很快就是\n',
            '卢安市的市长选举了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅游业推进派的诺曼氏\n',
            '和港湾地区代表的波尔多斯氏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果到底会是哪位候选人\n',
            '当选呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算不是卢安市民\n',
            '也非常地关心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001C)

    def _loc_554E(): pass

    label('loc_554E')

    TalkEnd(0x0036)

    Return()

# id: 0x002A offset: 0x5552
@scena.Code('func_2A_5552')
def func_2A_5552():
    TalkBegin(0x0037)

    ChrTalk(
        0x00FE,
        (
            '哦哦～那就是\n',
            '传说中的长城吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是遗迹的话，说不定有\n',
            '不为人知的宝物沉眠在地下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0037)

    Return()

# id: 0x002B offset: 0x55B7
@scena.Code('func_2B_55B7')
def func_2B_55B7():
    EventBegin(0x00)
    ClearMapFlags(0x02000000)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0029, 0x0040)
    ClearChrFlags(0x0029, 0x0080)
    SetChrPos(0x0101, 87690, -1000, 52960, 90)
    SetChrPos(0x0029, 88760, -1000, 52950, 270)
    OP_6D(88640, -1000, 48310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(27000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0021, 0x0080)
    SetChrPos(0x0021, 91200, 200, 47000, 0)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 86380, 0, 45000, 0)
    ClearChrFlags(0x0018, 0x0080)
    SetChrPos(0x0018, 86380, 0, 46350, 180)
    FadeIn(1500, 0)

    @scena.Lambda('lambda_567D')
    def lambda_567D():
        OP_6D(88300, -1000, 52980, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_567D)

    @scena.Lambda('lambda_5695')
    def lambda_5695():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5695)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010190204V#007F#6P嗯……\n',
            '是凯文先生吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190205V对不起……\n',
            '我失态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190206V#1061F没关系，没关系。\n',
            '把胸膛借给女孩子真是赚到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190207V#1060F怎样，镇定一点了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190208V#008F#6P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190209V我叫艾丝蒂尔。\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190210V隶属于游击士协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190211V#1061F艾丝蒂尔吗～\n',
            '名字也这么可爱啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190212V………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190213V#1064F……嗯，游击士协会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190214V#006F#6P嗯，我可是个游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190215V#506F嘿嘿，让你看到那么丢脸的样子\n',
            '可能很难相信吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190216V#1060F不，没这种事。\n',
            '仔细一看确实是很相称的打扮。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190217V你应该是练什么武术的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190218V#501F#6P是棒术，练了一点而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190219V#006F这么说来凯文先生\n',
            '真的是教会的神父吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190220V怎么看都不像。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190221V#1068F哎呀，真过分呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190222V#1066F不过，我是巡回神父……\n',
            '性质上倒是真的有些不同啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190223V#505F#6P巡回神父？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190224V#1060F有些村子没有礼拜堂对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190225V我就是定期造访这些村子\n',
            '并进行礼拜和主日学校教学的神父。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190226V嗯，就相当于教会的外派服务啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190227V#000F#6P原来如此……\n',
            '还有这样的神父啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190228V#1061F嗯，和在礼拜堂任职的神父不同，\n',
            '很多人对法衣什么的都很随便的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190229V就是这样，别太认真啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190230V#506F#6P嗯～也罢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190231V#501F那么，凯文先生\n',
            '现在要去哪个村子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190232V#1060F呀～其实我\n',
            '才刚刚来到利贝尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190233V巡回神父的人手似乎不足，\n',
            '所以才被总部派过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190234V#501F#6P啊，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190235V#505F教会的总部……\n',
            '我还不知道在哪里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190236V#1060F塞姆里亚大陆中部的国家——\n',
            '亚尔特利亚法典国。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190237V#1061F所以呢，去格兰赛尔大圣堂\n',
            '向大主教做上任报告之前\n',
            '打算先四处逛一下啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190238V然后就这样像闲逛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190239V#007F#6P这…………这怎么行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190240V#509F真是个散漫的神父啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190241V#1062F这没什么啦。\n',
            '只是先视察一下将来要巡回的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190242V而且还能像这样碰上\n',
            '有烦恼的可爱女孩～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190243V#1071F嗯嗯，这一定是女神的指引。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190244V#506F#6P你还真油嘴滑舌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190245V#006F不过……谢谢你。\n',
            '哭出来就好受多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190246V不行啊，嗯。\n',
            '一定要相信约修亚才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190247V#1064F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190248V#008F#6P啊，约修亚是像我\n',
            '弟弟一样的男孩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190249V但突然就失踪了，\n',
            '我有点惊慌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190250V#1063F突然失踪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190251V是离家出走吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190252V#506F#6P不，不是的。\n',
            '只是先我一步回家了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190253V因为我们是一家人嘛。\n',
            '不可能随便走掉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190254V#1063F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190255V#503F#6P不过，我还真是失败啊。\n',
            '可能是告白的时机太差了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190256V见到约修亚之后\n',
            '可要好好蒙混过去才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190257V#1063F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190258V#1065F……对了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190259V#004F#6P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0180190260V#1067F不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190261V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190262V#1060F刚才说过了，\n',
            '我正在旅行中没什么要事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190263V所以，到了洛连特我就下船\n',
            '送艾丝蒂尔回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190264V#004F#6P#3S咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0029, 0)
    NewScene('ED6_DT21/T0700._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002C offset: 0x6280
@scena.Code('func_2C_6280')
def func_2C_6280():
    EventBegin(0x00)
    FadeIn(1000, 0)
    OP_A2(0x1240)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x002D offset: 0x6292
@scena.Code('func_2D_6292')
def func_2D_6292():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 4, 0x1404)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68AB',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x0101, 116400, 0, 1690, 90)
    SetChrSubChip(0x0008, 1)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0050220227V#052F#2P怎么，艾丝蒂尔。\n',
            '还在船里闲逛呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220228V#1016F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220229V我以前都\n',
            '不太常搭乘飞船，\n',
            '感觉挺新鲜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050220230V#051F#2P正游击士经常出差，\n',
            '会经常乘坐飞船的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220231V差不多和交易商的\n',
            '乘坐频率一样高吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220232V#1015F#6P我老爸确实也\n',
            '经常出差呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220233V他现在在干什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050220234V#051F#2P被推上军队领导层后\n',
            '应该忙得团团转吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220235V呵，他平时一副从容不迫的样子，\n',
            '这下真是活该。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220236V#1016F#6P嗯～忙碌的老爸\n',
            '真是难以想象……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220237V#1011F不过阿加特，基本上对\n',
            '老爸的评价还是肯定的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220238V那为什么总是\n',
            '说得好像很讨厌他？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050220239V#551F#2P……也不是说\n',
            '讨厌他啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220240V#555F追根究底，失礼的人\n',
            '怎么说都应该是你老爸吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220241V每次看到别人老是说\n',
            '『辛苦了』『厉害厉害』之类的，\n',
            '把别人当成小孩子看待……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220242V#1007F#6P嗯～老爸确实\n',
            '喜欢捉弄人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220243V不过，他总是那么口没遮拦\n',
            '所以我也没怎么在意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050220244V#051F#2P你啊，幸好是女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220245V要是儿子的话\n',
            '现在可是正值叛逆期呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220246V#1008F#6P是、是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050220247V#551F#2P所谓老爸，对儿子来说\n',
            '是一道必须逾越的障壁嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220248V要是有那样高得离谱的障壁,\n',
            '搞不好会陷入自卑情结之中无法自拔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220249V#1016F#6P嗯～……\n',
            '虽然我不太能理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220250V#1006F不过说穿了就是阿加特\n',
            '对老爸感到有自卑情结？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050220251V#052F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220252V#1004F#6P咦，猜中了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050220253V#552F#2P……啰嗦，真是有其父必有其女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1404)
    EventEnd(0x00)
    SetChrSubChip(0x0008, 0)

    Jump('loc_6959')

    def _loc_68AB(): pass

    label('loc_68AB')

    TalkBegin(0x0008)
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_68D0',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_68EB')

    def _loc_68D0(): pass

    label('loc_68D0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_68E6',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_68EB')

    def _loc_68E6(): pass

    label('loc_68E6')

    SetChrSubChip(0x00FE, 1)

    def _loc_68EB(): pass

    label('loc_68EB')

    OP_8C(0x0008, 360, 0)
    SetChrFlags(0x0008, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0050220254V#552F真是的，下一站是蔡斯啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220255V马上就要到了\n',
            '别再到处乱晃啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    TalkEnd(0x0008)

    def _loc_6959(): pass

    label('loc_6959')

    Return()

# id: 0x002E offset: 0x695A
@scena.Code('func_2E_695A')
def func_2E_695A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 5, 0x1405)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_705E',
    )

    EventBegin(0x00)
    EventBegin(0x00)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x0101, 116400, 0, 1690, 90)
    SetChrSubChip(0x0009, 1)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0030220256V#526F#2P哎呀，艾丝蒂尔。\n',
            '还在船里散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220228V#1016F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220258V我以前都\n',
            '没怎么坐过飞船，\n',
            '感觉挺新鲜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030220259V#021F#2P记得我因工作而\n',
            '刚刚开始乘坐飞船的时候，\n',
            '每次都很兴奋呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220260V因为在以前的旅途中，\n',
            '我一次也没坐过飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220261V#1011F#6P说起来，雪拉姐\n',
            '原来是旅行艺人剧团里的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220262V是用导力装置的\n',
            '车子来代步旅行的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030220263V#027F#2P呵呵，怎么可能。\n',
            '几乎所有的车都是马车。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220264V只有团长\n',
            '有辆二手的导力驱动车。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220265V#1015F#6P嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220266V这么说来，很久以前，\n',
            '雪拉姐的剧团来镇上的时候\n',
            '就排了好多辆大蓬马车呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030220267V#021F#2P哎呀，亏你还记得呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220268V#526F不过飞船啊，在利贝尔以外\n',
            '似乎还完全没有普及。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220269V除此以外的导力驱动交通工具\n',
            '现在好像正在大量使用呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220270V埃雷波尼亚听说使用导力铁路\n',
            '来连接主要都市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220271V相邻的卡尔瓦德共和国则是\n',
            '有『导力汽车』在街道上跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220272V#1004F#6P导力……巴士？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220273V#1015F那是怎样的交通工具？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030220274V#020F#2P是大型的共乘导力车。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220275V和飞船一样，支付车费之后\n',
            '就可以从这个城市坐到另一个城市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220276V虽然不是很快，\n',
            '不过也别有一番悠闲的风情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220277V#1001F#6P哟～\n',
            '真有点想坐坐看呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220278V#1006F这么说来雪拉姐\n',
            '曾经去过共和国吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220279V听说是在那个时候认识金先生的，\n',
            '是为了什么事情而去的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030220280V#027F#2P是帮卡西乌斯老师的忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220281V代替老师把某文件\n',
            '送去卡尔瓦德的东方人街。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220282V就是在那里认识了金先生的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210884V#1011F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220284V#1015F东方人街……\n',
            '无法想象是个怎样的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030220285V#021F#2P呵呵，文化和街景都不一样，\n',
            '是个很刺激的地方哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220286V你要是有机会的话，\n',
            '去一次也挺不错的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1405)
    EventEnd(0x00)
    SetChrSubChip(0x0009, 0)

    Jump('loc_710F')

    def _loc_705E(): pass

    label('loc_705E')

    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7083',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_709E')

    def _loc_7083(): pass

    label('loc_7083')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7099',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_709E')

    def _loc_7099(): pass

    label('loc_7099')

    SetChrSubChip(0x00FE, 1)

    def _loc_709E(): pass

    label('loc_709E')

    OP_8C(0x0009, 360, 0)
    SetChrFlags(0x0009, 0x0010)

    ChrTalk(
        0x0009,
        (
            '#0030220287V#020F接下来是蔡斯，\n',
            '很快就会到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220288V别到处乱晃而\n',
            '错过了下船哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0009, 0)
    TalkEnd(0x0009)

    def _loc_710F(): pass

    label('loc_710F')

    Return()

# id: 0x002F offset: 0x7110
@scena.Code('func_2F_7110')
def func_2F_7110():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 6, 0x1406)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_797F',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(89060, -1000, 51690, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 89560, -1000, 51470, 270)
    SetChrSubChip(0x000A, 2)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0040220289V#030F哎呀，艾丝蒂尔。\n',
            '在享受空中之旅吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220290V#031F看吧……\n',
            '这雄伟的天空的颜色！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220291V简直是最棒的\n',
            '佐酒佳肴啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220292V#1016F嗯，天气这么好\n',
            '我也认为景色很美……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220293V不过很快就要到蔡斯了，\n',
            '喝酒是不是不太好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220294V#030F呼……\n',
            '别这么说嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220295V#034F在这天空下的某处\n',
            '有那可爱的约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220296V啊啊，他现在想着什么\n',
            '继续着他的旅程呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220297V#030F一想到这种事，\n',
            '就忍不住要喝酒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220298V#1019F……这个，完全是\n',
            '我的台词吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220299V#1007F真是的，有奥利维尔在\n',
            '话题就深刻不了，不过还真是得救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220300V#031F呵呵……\n',
            '得您称誉实在是光荣至极。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220301V#030F……不过，我稍微放心点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220302V#1004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220303V#035F『漆黒之牙』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220304V我还以为听了那怪盗留下的话\n',
            '你会有所动摇呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220305V#030F不过，你的决心似乎\n',
            '比我想象中的更加坚定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220306V#1025F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220307V#1016F嘿嘿，奥利维尔真是的……\n',
            '你在为我担心吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220308V#031F呵呵，因为我是寻求着爱而彷徨\n',
            '的诗人兼演奏家嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220309V是恋爱中少女的伙伴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220310V#1013F啊，呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220311V#030F哦。\n',
            '棒术就免了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220312V不过是开个玩笑嘛。\n',
            '只是觉得有些令人莞尔而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220313V就是那身衣服\n',
            '也是为了让约修亚看\n',
            '而新换的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220314V#031F嗯，非常适合你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220315V#1017F谢，谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220316V#1007F真是的……不要突然\n',
            '认真地说出这么让人难为情的事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220317V还有这身衣服，是雪拉姐\n',
            '送给我作为贺礼的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220318V#1013F想让约修亚看……\n',
            '……虽，虽然是有想过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220319V#033F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220320V#1019F怎、怎么了，不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220321V#035F呵呵……\n',
            '没什么，只是觉得有些超乎预想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220322V#030F嗯，这话题\n',
            '就到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220323V艾丝蒂尔也来一杯怎么样？\n',
            '请你喝鸡尾酒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220324V#1015F嗯～我心领了。\n',
            '马上就要到蔡斯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220325V#1006F奥利维尔也要适可而止，\n',
            '不然会醉倒错过下船的哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220326V#031F呼，不必担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220327V我奥利维尔，除了美女劝酒以外\n',
            '从来就没有醉倒过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220328V#1007F这也没什么好得意的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1406)
    EventEnd(0x00)
    SetChrSubChip(0x000A, 0)

    Jump('loc_7D47')

    def _loc_797F(): pass

    label('loc_797F')

    TalkBegin(0x000A)
    ClearChrFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_79A4',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_79BF')

    def _loc_79A4(): pass

    label('loc_79A4')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_79BA',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_79BF')

    def _loc_79BA(): pass

    label('loc_79BA')

    SetChrSubChip(0x00FE, 1)

    def _loc_79BF(): pass

    label('loc_79BF')

    OP_8C(0x000A, 360, 0)
    SetChrFlags(0x000A, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0216, 7, 0x10B7)),
            Expr.Return,
        ),
        'loc_7A72',
    )

    ChrTalk(
        0x000A,
        (
            '#0040220329V#031F那么，接下来是蔡斯地区吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220330V上次是直接跑去亚尔摩温泉，\n',
            '都没好好逛过其它的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220331V趁这次机会\n',
            '可要好好观光一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D3F')

    def _loc_7A72(): pass

    label('loc_7A72')

    ChrTalk(
        0x000A,
        (
            '#0040220332V#033F对了，艾丝蒂尔。\n',
            '不介意的话读一下这本书吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220333V#031F这个虽然很有趣，\n',
            '不过在帝国却是禁止发行的书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220334V#1019F禁止发行……是什么\n',
            '可疑的书啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220335V#030F不是不是，是卡尔瓦德共和国\n',
            '作为舞台的娱乐小说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220336V出于不利于教育的理由，\n',
            '所以没有在帝国出版。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220337V#1013F啊，原来如此……\n',
            '帝国还真是严格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220338V#030F虽然曾经听过评论，\n',
            '但这次总算是看过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220339V#035F和传闻不同，内容\n',
            '相当值得一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220340V#1011F哦～是怎样的故事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040220341V#030F唔，反正我也看完了，\n',
            '不介意的话就给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220342V#1001F可以吗？\n',
            '那我就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0039, 0x0080)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 ３卷']),
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
    AddItem(ItemTable['牌技师杰克 ３卷'], 1)
    OP_A2(0x10B7)

    def _loc_7D3F(): pass

    label('loc_7D3F')

    SetChrSubChip(0x000A, 0)
    TalkEnd(0x000A)

    def _loc_7D47(): pass

    label('loc_7D47')

    Return()

# id: 0x0030 offset: 0x7D48
@scena.Code('func_30_7D48')
def func_30_7D48():
    EventBegin(0x00)
    OP_22(0x00A6, 0x00, 0x64)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200720V……久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880220374V本船即将\n',
            '抵达蔡斯市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200722V着陆时会有少许摇晃，\n',
            '请尽快回到座位上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_7E0F',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_7E13')

    def _loc_7E0F(): pass

    label('loc_7E0F')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_7E13(): pass

    label('loc_7E13')

    FormationAddMember(ChrTable['科洛丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    NewScene('ED6_DT21/T3102._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0031 offset: 0x7E25
@scena.Code('func_31_7E25')
def func_31_7E25():
    EventBegin(0x00)
    OP_6D(88630, 0, 2860, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 88630, 0, 2860, 270)
    FadeIn(1000, 0)
    OP_A2(0x1681)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0032 offset: 0x7E85
@scena.Code('func_32_7E85')
def func_32_7E85():
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x000B, 255)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, 87980, -1000, 53080, 153)
    SetChrPos(0x0101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0070240330V#061F啊，姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240331V#051F#6P怎么，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240332V还～在船内\n',
            '到处闲逛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240333V#1007F真是的，别说得人\n',
            '像野猫一样啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240334V#1008F一直坐着等待，\n',
            '感觉静不下心来嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240335V#051F#6P你去过卢·洛克尔的\n',
            '训练场了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240336V坐飞船也要花半天时间，\n',
            '不是很无聊吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240337V#1016F那次啊，去和回来\n',
            '都是一下子就睡着了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240338V去的时候因为紧张而睡眠不足，\n',
            '回来是因为训练太疲劳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240339V#551F#6P真拿你没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240340V#061F嘻嘻……\n',
            '很像是姐姐的风格吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240341V#066F不过，我也好想\n',
            '去外国一次啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240342V那样说不定也可以\n',
            '去见爸爸妈妈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240343V#1025F啊，是哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240344V提妲的爸爸妈妈\n',
            '好像因工作出国去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240345V#560F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240346V到导力器还没有普及的国家\n',
            '去做技术指导了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240347V已经快两年都没回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240348V#1015F嗯～还真久啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240349V有互通书信吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240350V#061F嗯，一个月一次吧⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240351V#060F前不久我写了姐姐们的事，\n',
            '收到了爸妈的回信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240352V要我代他们向你们问好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240353V#1016F嘿嘿，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240354V#1006F话说回来提妲的父母\n',
            '是怎样的人呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240355V妈妈一定像提妲吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240356V#064F嗯～很难说吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240357V#060F性格嘛，特别有精神的一个人，\n',
            '很有活力的感觉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240358V#061F总是马上就和爷爷\n',
            '扭在一起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240359V#1004F扭、扭在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240360V#067F啊，其实并不是\n',
            '关系不好哦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240361V爸爸说，那也是\n',
            '亲子关系好的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240362V#1016F是、是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240363V#1011F那么\n',
            '爸爸是怎样的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240364V#560F嗯，是个很沉静\n',
            '又很壮实的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240365V听说十多年前\n',
            '曾经当过游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240366V#1004F咦，这是样吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240367V#051F#6P听老爷子说\n',
            '好像还相当厉害哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240368V由于受伤引退，\n',
            '之后好像转职当设计技师了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240369V#1006F哦～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240370V#1001F嗯～等他们回来之后\n',
            '真想见见两人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240371V#061F嗯，我也想介绍给姐姐认识，\n',
            '等他们回来以后记得来玩哦⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240372V#560F啊，当然\n',
            '阿加特哥哥也是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0050240373V#055F#6P啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240374V慢着，为什么我！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240375V#061F因为阿加特哥哥\n',
            '和爷爷关系很好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240376V而且我写了很多阿加特哥哥\n',
            '的事，他们回信说\n',
            '很想见你一面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240377V#552F#6P……真的假的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240378V#1006F啊哈哈，这就叫做\n',
            '年终算总帐吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240379V#063F那个，不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240380V#555F#6P不……\n',
            '也没什么不好的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240381V#551F算了，要是去蔡斯工作的话，\n',
            '我就去顺便打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240382V#061F嘿嘿，是吗⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x000B, 88700, -1000, 52960, 0)
    SetChrPos(0x0101, 89770, -1000, 52480, 270)
    OP_4B(0x000B, 255)
    OP_0D()
    OP_A2(0x1603)
    EventEnd(0x00)

    Return()

# id: 0x0033 offset: 0x893C
@scena.Code('func_33_893C')
def func_33_893C():
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x000B, 255)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, 87980, -1000, 53080, 153)
    SetChrPos(0x0101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0070240386V#560F对了姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240387V你知道这甲板上的风\n',
            '为什么会这么平静吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240388V#1004F因为风本来就很平静……\n',
            '是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240389V#060F不是。\n',
            '其实这个速度和高度\n',
            '应该会引起很大的风的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240390V不要说聊天了,\n',
            '连站都会站不稳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240391V#1015F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0050240392V#052F#6P也就是说，有什么装置\n',
            '可以克服这一点对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240393V#560F是的，这就是让飞船浮上天空的\n',
            '『飞翔引擎』它另外的作用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240394V#061F这个机关运转的时候，\n',
            '反重力的力场\n',
            '会覆盖整条船……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240395V据说这个力场同时也会\n',
            '缓和风与惯性的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240396V#1019F（……阿加特，你懂吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240397V#552F#6P（懂才有鬼……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240398V#060F不过，要启动飞翔引擎\n',
            '需要大量的导力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240399V为此就需要\n',
            '高输出功率的『导力引擎』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240400V#1006F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240401V决定飞船性能的就是引擎，\n',
            '原来指的是这个意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050240402V#051F#6P这么说来，王室的船上搭载的\n',
            '新型引擎好像完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240403V性能似乎相当厉害吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070240404V#061F是的，我看了性能表，\n',
            '感觉和以前真的有天壤之别。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240405V我想这都是多亏了开发小组和\n',
            '维修班各位的努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240406V#1016F呵呵，感觉真是辛苦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x000B, 88700, -1000, 52960, 0)
    SetChrPos(0x0101, 89770, -1000, 52480, 270)
    OP_4B(0x000B, 255)
    OP_0D()
    OP_A2(0x1604)
    EventEnd(0x00)

    Return()

# id: 0x0034 offset: 0x8EAB
@scena.Code('func_34_8EAB')
def func_34_8EAB():
    EventBegin(0x00)
    OP_20(0x000003E8)
    Fade(1000)
    OP_4A(0x000A, 255)
    SetChrChipByIndex(0x000A, 42)
    SetChrSubChip(0x000A, 0)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000A, 87980, -1000, 53080, 153)
    SetChrPos(0x0101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0040240409V#031F呀，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240410V欢迎来到我奥利维尔·朗海姆的\n',
            '独奏会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240466V#1007F你在装模作样些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240467V#1019F话说回来在这种地方\n',
            '弹奏乐器没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040240468V#035F呼……\n',
            '这真是愚蠢的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240469V就像游击士以保护人民，\n',
            '军人以保护国家为己任一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240470V像我这样的艺术家\n',
            '则是以将涌现而出的激情\n',
            '当场化为有形之物为己任的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030240471V#020F#6P好歹也算是笼络了\n',
            '客室乘务员之后取得许得的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240472V请随意弹奏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040240473V#036F哎哎，雪拉！\n',
            '你真是冷淡啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240474V#034F难得约你去温泉旅行\n',
            '却一口回绝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240475V我为了你，早已有\n',
            '沉醉不醒的觉悟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0009, 1)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0030240476V#021F#6P嗯，要是有空的话\n',
            '倒也可以考虑考虑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240477V#027F不说这个，喝到\n',
            '醉倒这种话可别胡说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240478V只不过希望你能和我步调一致，\n',
            '慢慢享受酒的美味……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240479V#021F我的要求仅此而已㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0040240480V#033F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240481V#1007F我说啊，奥利维尔。\n',
            '雪拉姐是没什么自觉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240482V对自己酒量大成什么样子，\n',
            '喝酒的步调多乱来是没有概念的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030240483V#025F#6P什么啊，真失礼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240484V#027F不过，要找我搭讪\n',
            '就得有这种程度的觉悟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240485V而且我的门坎\n',
            '应该还没爱娜高呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000A, 0x00000014, 0x00000000, 0x000001F4, 0x00000FA0)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0040240486V#036F她，她的事就不要提了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240487V#034F光是想起那时候的事，\n',
            '我现在还感到轻微地眩晕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030240488V#021F#6P呵呵，这也难怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240489V#1016F（到底发生了什么事……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000A, 88700, -1000, 52960, 0)
    SetChrPos(0x0101, 89770, -1000, 52480, 270)
    OP_8C(0x000A, 180, 0)
    SetChrSubChip(0x0009, 0)
    SetChrChipByIndex(0x000A, 41)
    SetChrSubChip(0x000A, 0)
    OP_4B(0x000A, 255)
    OP_1D(0x49)
    OP_0D()
    OP_A2(0x1607)
    EventEnd(0x00)

    Return()

# id: 0x0035 offset: 0x953F
@scena.Code('func_35_953F')
def func_35_953F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 1, 0x1609)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A366',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x0101, 116400, 0, 1690, 90)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0080240243V#572F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240244V#1015F#6P……金先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x00FE, 0)
    Sleep(75)

    SetChrSubChip(0x00FE, 1)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0080240245V#070F#2P哦哦，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240246V怎么了，找我有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240247V#1016F#6P啊，不是。\n',
            '倒没有什么事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240248V#1025F你好像在想什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240249V#074F#2P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240250V#070F稍微想起一些往事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240251V#1015F#6P果然还是……\n',
            '那个戴墨镜的男人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240252V#070F#2P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240253V自从最后道别以来已经６年了……\n',
            '感觉既漫长又短暂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240254V#1025F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240255V#1002F那个人，是金先生的\n',
            '师兄吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240256V是什么类型的武术家呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240257V#074F#2P这个啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_AD(0x0024007B, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    OP_1D(0x53)
    Sleep(500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080240258V#070F一言以蔽之，就是『天才』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240259V压倒性的格斗感觉和反射神经。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240260V兼备力量与速度的肉体。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240261V以及爆发性的『气』的使用方法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240262V无论任何一点都是出类拔萃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010240263V#1007F确实，那动作太厉害了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240264V单论力量和速度的话，\n',
            '说不定还在那个洛伦斯少尉之上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080240265V#070F……或许是这样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240266V#074F在道场的时候，我非常\n',
            '向往他的强大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240267V直到六年前──他对老师\n',
            '龙牙老师出手为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010240268V#1020F！！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240269V对自己的老师……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000003E8)
    Sleep(1000)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080240270V#070F虽说如此,\n',
            '但那也是双方同意的比试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240271V#074F师父从很久以前\n',
            '就看穿了他心底的黑暗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240272V沉醉于自己压倒性的实力\n',
            '而贪图追求更高的力量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240273V在训诫这种危险的同时，\n',
            '也藉此来说明武术之心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240274V#070F通过战斗来提高自己的精神境界，\n',
            '这才是泰斗流『活人拳』的精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010240275V#1006F『活人拳』……\n',
            '听起来好响亮的名字哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080240276V#072F然而结果，这精神\n',
            '却没能传达给瓦鲁特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240277V他就像被诱惑了一样，\n',
            '投入了武术的黑暗面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010240278V#1004F武，武术的黑暗面……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080240279V#074F就是武术作为战斗的技术时\n',
            '绝对无法否定的一面的极端……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240280V将自己化为魔鬼，单纯以\n',
            '夺取对手性命为目的的拳法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240281V#072F亦即『杀人拳』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010230783V#1020F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD(0x0024007C, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080240283V#072F师父向为了追求这个\n',
            '而意图脱离道场的他\n',
            '进行挑战……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240284V决斗的结果，是丢了性命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240285V#074F……我身为决斗的见证人，\n',
            '只能眼睁睁看着它发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010240286V#1026F……金先生…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_AE(0x000003E8)
    Sleep(1500)

    ChrTalk(
        0x000C,
        (
            '#0080240287V#070F#2P嗯，因为这样的事情，\n',
            '我一直在找寻瓦鲁特\n',
            '的踪迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240288V没想到会在这利贝尔\n',
            '再次见到他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240289V这或许也是女神的指引吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240290V#1003F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240291V#073F#2P哦，抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240292V让你听了这些\n',
            '无聊的往事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240293V#1007F#6P不……\n',
            '谢谢你告诉我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240294V#1002F不过，金先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240295V你寻找那个男人，\n',
            '是为了给师父报仇吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240296V#070F#2P哈哈，刚才我也说了\n',
            '那是相互同意的比试结果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240297V报仇就说不过去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240298V#1016F#6P是，是吗……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240299V#1026F但是为什么\n',
            '还要找他呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240300V#074F#2P……啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240301V#572F我想确认一件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240302V#1015F#6P确认一件事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240303V#071F#2P哈哈，说出来太难为情了，\n',
            '我看还是算了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240304V#070F无论如何，\n',
            '要确认这件事情\n',
            '我还远远不够成熟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240305V于是就藉由协助你\n',
            '来努力地修行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240306V#1012F#6P是吗……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240307V#1018F我也要继续努力，\n',
            '不能拖金先生的后腿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240308V#071F#2P哦，彼此都要努力进步啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()
    OP_A2(0x1609)
    EventEnd(0x00)
    SetChrSubChip(0x000C, 0)
    OP_1D(0x01)

    Jump('loc_A857')

    def _loc_A366(): pass

    label('loc_A366')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 2, 0x160A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A575',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x0101, 116400, 0, 1690, 90)
    SetChrSubChip(0x000C, 1)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010240309V#1004F#6P啊，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240310V#1025F那男人和金先生的关系\n',
            '我大致明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240311V那么雾香小姐\n',
            '又是什么关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240312V#073F#2P啊～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240313V#074F详情我无法跟你说，\n',
            '不过可以告诉你一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240314V雾香，是死去的\n',
            '龙牙师父的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200268V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240316V#070F#2P现在你知道这个就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240317V总有一天，或许也能从那家伙口中\n',
            '问出些什么来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240318V#1006F#6P嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x160A)
    EventEnd(0x00)
    SetChrSubChip(0x000C, 0)

    Jump('loc_A857')

    def _loc_A575(): pass

    label('loc_A575')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A79C',
    )

    OP_A2(0x0001)
    TalkBegin(0x000C)
    ClearChrFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A5A5',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_A5C0')

    def _loc_A5A5(): pass

    label('loc_A5A5')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A5BB',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_A5C0')

    def _loc_A5BB(): pass

    label('loc_A5BB')

    SetChrSubChip(0x00FE, 1)

    def _loc_A5C0(): pass

    label('loc_A5C0')

    OP_8C(0x000C, 0, 0)
    SetChrFlags(0x000C, 0x0010)

    ChrTalk(
        0x000C,
        (
            '#0080240319V#070F那么，到了王都\n',
            '得去大使馆露个脸才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240320V太晚过去的话\n',
            '会被大使为难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240321V#1015F我记得大使是……\n',
            '那个戴眼镜看起来很严厉的女人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240322V#073F怎么，你知道啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240323V#1006F只是见过一次而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240324V她和帝国大使那位大叔\n',
            '吵得很激烈呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080240325V#075F唔，她还是那么\n',
            '讨厌埃雷波尼亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240326V平时倒是给人一种相当\n',
            '从容不迫的才女气质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240327V#1011F哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000C, 0)
    TalkEnd(0x000C)

    Jump('loc_A857')

    def _loc_A79C(): pass

    label('loc_A79C')

    TalkBegin(0x000C)
    ClearChrFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A7C1',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_A7DC')

    def _loc_A7C1(): pass

    label('loc_A7C1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A7D7',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_A7DC')

    def _loc_A7D7(): pass

    label('loc_A7D7')

    SetChrSubChip(0x00FE, 1)

    def _loc_A7DC(): pass

    label('loc_A7DC')

    OP_8C(0x000C, 0, 0)
    SetChrFlags(0x000C, 0x0010)

    ChrTalk(
        0x000C,
        (
            '#0080240319V#070F那么，到了王都\n',
            '得去大使馆露个脸才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240320V太晚过去的话\n',
            '会被大使为难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000C, 0)
    TalkEnd(0x000C)

    def _loc_A857(): pass

    label('loc_A857')

    Return()

# id: 0x0036 offset: 0xA858
@scena.Code('func_36_A858')
def func_36_A858():
    EventBegin(0x00)
    OP_22(0x00A6, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200720V……久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880240586V本船即将\n',
            '到达王都格兰赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200722V着陆时会有少许摇晃，\n',
            '请尽快回到座位上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene('ED6_DT21/T4106._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0037 offset: 0xA921
@scena.Code('func_37_A921')
def func_37_A921():
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x49),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_21()
    OP_1D(0x49)

    Return()

# id: 0x0038 offset: 0xA938
@scena.Code('func_38_A938')
def func_38_A938():
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_21()
    OP_1D(0x01)

    Return()

# id: 0x0039 offset: 0xA94F
@scena.Code('func_39_A94F')
def func_39_A94F():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_A9CB'),
        (0x00000001, 'loc_A9D1'),
        (-1, 'loc_A9D7'),
    )

    def _loc_A9CB(): pass

    label('loc_A9CB')

    OP_A2(0x1200)

    Jump('loc_A9D7')

    def _loc_A9D1(): pass

    label('loc_A9D1')

    OP_A2(0x1201)

    Jump('loc_A9D7')

    def _loc_A9D7(): pass

    label('loc_A9D7')

    FadeIn(1000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
