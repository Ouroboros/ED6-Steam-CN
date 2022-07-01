import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1131   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雷克多主管'),
    TXT(0x02, '罗宋厨师长'),
    TXT(0x03, '格露娜'),
    TXT(0x04, '斯托隆'),
    TXT(0x05, '莉诺'),
    TXT(0x06, '赫雷思老人'),
    TXT(0x07, '阿尔妲婆婆'),
    TXT(0x08, '卡洛塔'),
    TXT(0x09, '沙库'),
    TXT(0x0A, '奥维德'),
    TXT(0x0B, '芙拉瑟'),
    TXT(0x0C, '蕾娜'),
    TXT(0x0D, '管家'),
    TXT(0x0E, '帝国贵族'),
    TXT(0x0F, '青年管家'),
    TXT(0x10, '罗卡斯'),
    TXT(0x11, '爱蕾吉娅'),
    TXT(0x12, '雷塔'),
    TXT(0x13, '法娜'),
    TXT(0x14, '维尔纳'),
    TXT(0x15, '普拉达'),
    TXT(0x16, '龙谷'),
    TXT(0x17, '卡特丽亚'),
    TXT(0x18, '芬尼尔'),
    TXT(0x19, '科尔娜'),
    TXT(0x1A, '哈尔德'),
    TXT(0x1B, '索斯摩夫'),
    TXT(0x1C, '料理'),
    TXT(0x1D, '汤勺'),
    TXT(0x1E, '刚茨'),
    TXT(0x1F, '梅贝尔市长'),
    TXT(0x20, '莉拉'),
    TXT(0x21, '汤碗'),
    TXT(0x22, '汤勺'),
    TXT(0x23, '餐具'),
    TXT(0x24, '餐具'),
    TXT(0x25, '小刀'),
    TXT(0x26, '小刀'),
    TXT(0x27, '汤碗'),
    TXT(0x28, '葡萄酒'),
    TXT(0x29, '汤勺'),
    TXT(0x2A, '杯子'),
    TXT(0x2B, '茶壶'),
    TXT(0x2C, '茶壶'),
    TXT(0x2D, '茶壶'),
    TXT(0x2E, '瓶子'),
    TXT(0x2F, '酒杯'),
    TXT(0x30, '茶壶'),
    TXT(0x31, '杯子'),
    TXT(0x32, '杯子'),
    TXT(0x33, '汤碗'),
    TXT(0x34, '汤勺'),
    TXT(0x35, '瓶子'),
    TXT(0x36, '酒杯'),
    TXT(0x37, '甜点'),
    TXT(0x38, '甜点'),
    TXT(0x39, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1131.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x0000
    header.importTable    = ['ED6_DT21/T1131._SN', 'ED6_DT21/T1131_1._SN', 'ED6_DT21/T1131_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA8D5
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
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01223._CH', 'ED6_DT07/CH01223P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01093._CH', 'ED6_DT07/CH01093P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01453._CH', 'ED6_DT07/CH01453P._CP'),
    ]

# id: 0x10002 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -42600,
            z                   = 0,
            y                   = 1700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -35500,
            z                   = 0,
            y                   = 46700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -47450,
            z                   = 0,
            y                   = 44160,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -42610,
            z                   = 0,
            y                   = 41570,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -53300,
            z                   = 1500,
            y                   = 200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -48300,
            z                   = 1650,
            y                   = 10950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -36300,
            z                   = 1650,
            y                   = -1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -54970,
            z                   = 1600,
            y                   = 5570,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -55100,
            z                   = 1600,
            y                   = 2970,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -33640,
            z                   = 0,
            y                   = 42550,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -32930,
            z                   = 1600,
            y                   = 2650,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -33800,
            z                   = 1500,
            y                   = 1300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -31760,
            z                   = 1500,
            y                   = 1300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = -33060,
            z                   = 1750,
            y                   = 5350,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = -32560,
            z                   = 1500,
            y                   = 6200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -51940,
            z                   = 1500,
            y                   = 6490,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -46030,
            z                   = 0,
            y                   = -1790,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -40300,
            z                   = 1650,
            y                   = 5950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = -39100,
            z                   = 1650,
            y                   = 7340,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 2970,
            z                   = 0,
            y                   = 3650,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = 1400,
            z                   = 0,
            y                   = 1500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = 5480,
            z                   = 0,
            y                   = 1480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = -2790,
            z                   = 0,
            y                   = -5200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = -2790,
            z                   = 0,
            y                   = -3690,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = 4400,
            z                   = 0,
            y                   = 1480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 4480,
            z                   = 0,
            y                   = 1520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            x                   = -7160,
            z                   = 1580,
            y                   = -4250,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            x                   = -6140,
            z                   = 2250,
            y                   = -4000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262169,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -6480,
            z                   = 2250,
            y                   = -4300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1114137,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 3200,
            z                   = 0,
            y                   = -3980,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            x                   = -980,
            z                   = 0,
            y                   = -2730,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -230,
            z                   = 0,
            y                   = -1730,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35500,
            z                   = 2150,
            y                   = -1060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196633,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35750,
            z                   = 2150,
            y                   = -1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1114137,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35670,
            z                   = 2150,
            y                   = -950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1376281,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35670,
            z                   = 2150,
            y                   = -830,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1376281,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35550,
            z                   = 2150,
            y                   = -1350,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1441817,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35550,
            z                   = 2150,
            y                   = -1490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1441817,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -47350,
            z                   = 2150,
            y                   = 11000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196633,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -47200,
            z                   = 2150,
            y                   = 11400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327704,
            chipIndex           = 24,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -47650,
            z                   = 2150,
            y                   = 11050,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1114137,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -46400,
            z                   = 2200,
            y                   = 11000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638425,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -55000,
            z                   = 2200,
            y                   = 4250,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703961,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -55000,
            z                   = 2200,
            y                   = 4750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638425,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -55000,
            z                   = 2200,
            y                   = 3550,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638425,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -6490,
            z                   = 2100,
            y                   = -3560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835033,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -6360,
            z                   = 2100,
            y                   = -4420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65560,
            chipIndex           = 24,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -33100,
            z                   = 2200,
            y                   = 4100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703961,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -33000,
            z                   = 2200,
            y                   = 4600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638425,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -33000,
            z                   = 2200,
            y                   = 3400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638425,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -53250,
            z                   = 2250,
            y                   = -950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 524313,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -53750,
            z                   = 2150,
            y                   = -1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1114137,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -52920,
            z                   = 2250,
            y                   = -630,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1835033,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -53500,
            z                   = 2150,
            y                   = -630,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327704,
            chipIndex           = 24,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -39550,
            z                   = 2250,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589849,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -38990,
            z                   = 2250,
            y                   = 6430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589849,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
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
        ScenaActorData(
            triggerX            = 3050,
            triggerZ            = 0,
            triggerY            = 1520,
            triggerRange        = 400,
            actorX              = 2970,
            actorZ              = 1500,
            actorY              = 3650,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x8E6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_905',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(1, 0x0006)

    Jump('loc_92E')

    def _loc_905(): pass

    label('loc_905')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_91B',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 0x000A)

    Jump('loc_92E')

    def _loc_91B(): pass

    label('loc_91B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_92E',
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(2, 0x0004)

    def _loc_92E(): pass

    label('loc_92E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_99D',
    )

    SetChrFlags(0x0037, 0x0080)
    SetChrFlags(0x0038, 0x0080)
    SetChrFlags(0x0039, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0011, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_98B',
    )

    SetChrFlags(0x0032, 0x0080)
    SetChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0034, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)

    Jump('loc_99A')

    def _loc_98B(): pass

    label('loc_98B')

    ClearChrFlags(0x0023, 0x0080)
    SetChrSubChip(0x0023, 8)
    ClearChrFlags(0x0024, 0x0080)

    def _loc_99A(): pass

    label('loc_99A')

    Jump('loc_E1F')

    def _loc_99D(): pass

    label('loc_99D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_A5A',
    )

    SetChrPos(0x002E, -47250, 2250, 11000, 90)
    SetChrSubChip(0x002E, 8)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x003E, 0x0080)
    ClearChrFlags(0x003F, 0x0080)
    SetChrPos(0x000B, -38500, 1500, 14200, 180)
    SetChrFlags(0x0037, 0x0080)
    SetChrFlags(0x0038, 0x0080)
    SetChrFlags(0x0039, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrPos(0x001C, -1230, 0, 4400, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A57',
    )

    ClearChrFlags(0x0020, 0x0080)
    SetChrPos(0x0020, 2400, 0, 1370, 0)
    ClearChrFlags(0x0038, 0x0080)
    SetChrPos(0x0038, 2250, 700, 2330, 0)

    def _loc_A57(): pass

    label('loc_A57')

    Jump('loc_E1F')

    def _loc_A5A(): pass

    label('loc_A5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_B07',
    )

    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, -45760, 1550, 11100, 270)
    SetChrChipByIndex(0x0017, 22)
    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x0017, 0x0010)
    SetChrFlags(0x0017, 0x0004)
    ClearChrFlags(0x0017, 0x0001)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    SetChrPos(0x0018, -54180, 1600, -1120, 90)
    SetChrChipByIndex(0x0018, 21)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0018, 0x0010)
    SetChrFlags(0x0018, 0x0004)
    ClearChrFlags(0x0018, 0x0001)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    SetChrPos(0x001E, -2790, 0, -4580, 90)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001F, -2790, 0, -3690, 90)

    Jump('loc_E1F')

    def _loc_B07(): pass

    label('loc_B07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_B9D',
    )

    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, -42360, 0, -1790, 0)
    CreateThread(0x0017, 0x00, 0x06, 0x0002)
    ClearChrFlags(0x0018, 0x0080)
    SetChrPos(0x0018, -54180, 1650, -1120, 90)
    SetChrChipByIndex(0x0018, 21)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0018, 0x0010)
    SetChrFlags(0x0018, 0x0004)
    ClearChrFlags(0x0018, 0x0001)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    SetChrPos(0x001E, -2790, 0, -4580, 90)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001F, -2790, 0, -3690, 90)

    Jump('loc_E1F')

    def _loc_B9D(): pass

    label('loc_B9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_D4B',
    )

    ClearChrFlags(0x0017, 0x0080)
    CreateThread(0x0017, 0x00, 0x06, 0x0002)
    ClearChrFlags(0x0018, 0x0080)
    CreateThread(0x0018, 0x00, 0x00, 0x0005)
    SetChrPos(0x000D, -52150, 1500, 8020, 180)
    SetChrChipByIndex(0x000D, 19)
    ClearChrFlags(0x000D, 0x0040)
    ClearChrFlags(0x000D, 0x0010)
    ClearChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000D, 0x0001)
    CreateThread(0x000D, 0x00, 0x06, 0x0002)
    SetChrPos(0x000E, -36410, 1500, 90, 225)
    SetChrChipByIndex(0x000E, 20)
    ClearChrFlags(0x000E, 0x0040)
    ClearChrFlags(0x000E, 0x0010)
    ClearChrFlags(0x000E, 0x0004)
    SetChrFlags(0x000E, 0x0001)
    CreateThread(0x000E, 0x00, 0x06, 0x0002)
    SetChrPos(0x000F, -53390, 1500, 3430, 132)
    SetChrChipByIndex(0x000F, 23)
    ClearChrFlags(0x000F, 0x0040)
    ClearChrFlags(0x000F, 0x0010)
    ClearChrFlags(0x000F, 0x0004)
    SetChrFlags(0x000F, 0x0001)
    CreateThread(0x000F, 0x00, 0x06, 0x0002)
    SetChrPos(0x0010, -53720, 1500, 2050, 135)
    SetChrChipByIndex(0x0010, 9)
    ClearChrFlags(0x0010, 0x0040)
    ClearChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0010, 0x0001)
    CreateThread(0x0010, 0x00, 0x06, 0x0002)
    SetChrPos(0x000C, -46440, 1500, 12150, 180)
    CreateThread(0x000C, 0x00, 0x06, 0x0002)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001C, 140, 0, 1780, 180)
    CreateThread(0x001C, 0x00, 0x06, 0x0002)
    SetChrPos(0x0012, -33720, 1500, 2810, 261)
    SetChrChipByIndex(0x0012, 33)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0012, 0x0040)
    ClearChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0012, 0x0001)
    CreateThread(0x0012, 0x00, 0x06, 0x0002)
    SetChrPos(0x0015, -35370, 1500, 2950, 103)
    SetChrChipByIndex(0x0015, 11)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0015, 0x0040)
    ClearChrFlags(0x0015, 0x0004)
    SetChrFlags(0x0015, 0x0001)
    CreateThread(0x0015, 0x00, 0x06, 0x0002)
    SetChrPos(0x0014, -31820, 1500, 2029, 270)
    SetChrPos(0x0013, -40690, 0, -510, 180)
    SetChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0025, 0x0080)

    Jump('loc_E1F')

    def _loc_D4B(): pass

    label('loc_D4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_E1F',
    )

    ClearChrFlags(0x001D, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D9E',
    )

    SetChrPos(0x0013, -33800, 1500, 1300, 0)
    SetChrPos(0x0014, -31760, 1500, 1300, 0)
    SetChrPos(0x0012, -32930, 1600, 2650, 0)

    Jump('loc_E1F')

    def _loc_D9E(): pass

    label('loc_D9E')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DE4',
    )

    SetChrPos(0x0013, -47400, 0, -1660, 90)
    SetChrPos(0x0014, -33780, 1500, 2840, 0)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0016, 0x0010)
    SetChrFlags(0x0014, 0x0010)

    Jump('loc_E1F')

    def _loc_DE4(): pass

    label('loc_DE4')

    SetChrPos(0x0013, -47400, 0, -1660, 180)
    SetChrPos(0x0014, -47400, 0, -2880, 0)
    SetChrFlags(0x0013, 0x0010)
    SetChrFlags(0x0014, 0x0010)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0016, 0x0010)
    SetChrFlags(0x0039, 0x0080)

    def _loc_E1F(): pass

    label('loc_E1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E2E',
    )

    ClearChrFlags(0x0011, 0x0080)

    Jump('loc_E55')

    def _loc_E2E(): pass

    label('loc_E2E')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E45',
    )

    SetChrFlags(0x000A, 0x0010)

    def _loc_E45(): pass

    label('loc_E45')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_E55',
    )

    ClearChrFlags(0x0011, 0x0080)

    def _loc_E55(): pass

    label('loc_E55')

    Return()

# id: 0x0001 offset: 0xE56
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 2, 0x1A12)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E6E',
    )

    OP_10(0x00, 0x00)
    OP_10(0x04, 0x01)
    OP_10(0x01, 0x00)
    OP_10(0x05, 0x01)

    def _loc_E6E(): pass

    label('loc_E6E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E8E',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)

    def _loc_E8E(): pass

    label('loc_E8E')

    Return()

# id: 0x0002 offset: 0xE8F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EB2',
    )

    OP_8D(0x00FE, -48200, 42570, -46450, 46500, 1000)

    Jump('ReInit')

    def _loc_EB2(): pass

    label('loc_EB2')

    Return()

# id: 0x0003 offset: 0xEB3
@scena.Code('func_03_EB3')
def func_03_EB3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_114B',
    )

    OP_8E(0x00FE, -54020, 1500, 3000, 2000, 0x00)
    OP_8C(0x00FE, 315, 200)
    Sleep(5000)

    OP_8E(0x00FE, -52400, 1500, 3300, 2000, 0x00)
    OP_8E(0x00FE, -51700, 1500, 4000, 2000, 0x00)
    OP_8E(0x00FE, -51700, 1500, 8700, 2000, 0x00)
    OP_8E(0x00FE, -44200, 1500, 9600, 2000, 0x00)
    OP_8E(0x00FE, -44200, 1500, 12000, 2000, 0x00)
    OP_8E(0x00FE, -45800, 1500, 12000, 2000, 0x00)
    OP_8C(0x00FE, 225, 200)
    Sleep(5000)

    OP_8E(0x00FE, -45700, 1500, 12700, 2000, 0x00)
    OP_8E(0x00FE, -41000, 1500, 12700, 2000, 0x00)
    OP_8C(0x00FE, 180, 200)
    Sleep(5000)

    OP_8E(0x00FE, -34900, 1500, 12500, 2000, 0x00)
    OP_8E(0x00FE, -34900, 1500, 11900, 2000, 0x00)
    OP_8C(0x00FE, 180, 200)
    Sleep(5000)

    OP_8E(0x00FE, -34900, 1500, 12500, 2000, 0x00)
    OP_8E(0x00FE, -32600, 1500, 12500, 2000, 0x00)
    OP_8E(0x00FE, -32600, 1500, 8000, 2000, 0x00)
    OP_8E(0x00FE, -37200, 1500, 4000, 2000, 0x00)
    OP_8E(0x00FE, -37400, 1500, -1200, 2000, 0x00)
    OP_8E(0x00FE, -36800, 1500, -2400, 2000, 0x00)
    OP_8E(0x00FE, -36100, 1500, -2400, 2000, 0x00)
    OP_8E(0x00FE, -35700, 1500, -2100, 2000, 0x00)
    OP_8C(0x00FE, 45, 200)
    Sleep(5000)

    OP_8E(0x00FE, -35800, 1500, -2400, 2000, 0x00)
    OP_8E(0x00FE, -32299, 1500, -2400, 2000, 0x00)
    OP_8E(0x00FE, -32299, 1500, 400, 2000, 0x00)
    OP_8E(0x00FE, -35000, 1500, 400, 2000, 0x00)
    OP_8E(0x00FE, -36800, 1500, 2400, 2000, 0x00)
    OP_8E(0x00FE, -36800, 1500, 8600, 2000, 0x00)
    OP_8E(0x00FE, -50800, 1500, 8600, 2000, 0x00)
    OP_8E(0x00FE, -51700, 1500, 7400, 2000, 0x00)
    OP_8E(0x00FE, -51700, 1500, 2500, 2000, 0x00)
    OP_8E(0x00FE, -53300, 1500, 200, 2000, 0x00)
    OP_8C(0x00FE, 180, 200)
    Sleep(5000)

    Jump('func_03_EB3')

    def _loc_114B(): pass

    label('loc_114B')

    Return()

# id: 0x0004 offset: 0x114C
@scena.Code('func_04_114C')
def func_04_114C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12CA',
    )

    Sleep(2000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1175',
    )

    OP_8E(0x00FE, -1430, 0, 60, 2000, 0x00)

    def _loc_1175(): pass

    label('loc_1175')

    OP_8E(0x00FE, -2100, 0, -1200, 2000, 0x00)
    OP_8E(0x00FE, -4100, 1500, -1100, 1000, 0x00)
    OP_8E(0x00FE, -6000, 1500, -2700, 2000, 0x00)
    OP_8C(0x00FE, 180, 200)
    Sleep(5000)

    OP_8E(0x00FE, -7300, 1500, -100, 2000, 0x00)
    OP_8E(0x00FE, -7300, 3250, 2100, 1000, 0x00)
    OP_8E(0x00FE, -5000, 3250, 4100, 2000, 0x00)
    OP_8C(0x00FE, 0, 200)
    Sleep(5000)

    OP_8E(0x00FE, -6600, 3250, 2200, 2000, 0x00)
    OP_8E(0x00FE, -6600, 1500, 0, 1000, 0x00)
    OP_8E(0x00FE, -6000, 1500, -2700, 2000, 0x00)
    OP_8C(0x00FE, 180, 200)
    Sleep(5000)

    OP_8E(0x00FE, -4100, 1500, -1100, 2000, 0x00)
    OP_8E(0x00FE, -2100, 0, -1200, 1000, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_12A7',
    )

    OP_8E(0x00FE, -1430, 0, 60, 2000, 0x00)
    OP_8E(0x00FE, -1230, 0, 4400, 2000, 0x00)

    Jump('loc_12BB')

    def _loc_12A7(): pass

    label('loc_12A7')

    OP_8E(0x00FE, 1400, 0, 1500, 2000, 0x00)

    def _loc_12BB(): pass

    label('loc_12BB')

    OP_8C(0x00FE, 0, 200)
    Sleep(5000)

    Jump('func_04_114C')

    def _loc_12CA(): pass

    label('loc_12CA')

    Return()

# id: 0x0005 offset: 0x12CB
@scena.Code('func_05_12CB')
def func_05_12CB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12EE',
    )

    OP_8D(0x00FE, -47100, -2490, -44490, -1060, 2000)

    Jump('func_05_12CB')

    def _loc_12EE(): pass

    label('loc_12EE')

    Return()

# id: 0x0006 offset: 0x12EF
@scena.Code('func_06_12EF')
def func_06_12EF():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_13EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1382',
    )

    ChrTalk(
        0x00FE,
        (
            '本店当前最大的问题是\n',
            '定期船停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然筹集到了上等的葡萄酒，\n',
            '但却缺乏运输手段……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '衷心希望\n',
            '能够早日恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_13E8')

    def _loc_1382(): pass

    label('loc_1382')

    ChrTalk(
        0x00FE,
        (
            '本店当前最大的问题是\n',
            '定期船停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然筹集到了上等的葡萄酒，\n',
            '但空中运输通道是必不可缺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13E8(): pass

    label('loc_13E8')

    Jump('loc_19D2')

    def _loc_13EB(): pass

    label('loc_13EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_150E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14C1',
    )

    ChrTalk(
        0x00FE,
        (
            '为了应对这次状况，\n',
            '老板梅贝尔市长\n',
            '一直在忙碌着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来到店里也只是稍做视察\n',
            '就回市长官邸去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然曾几次提醒\n',
            '她注意身体，但……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '逼迫自己迎难而上的习惯\n',
            '是从父亲那里遗传下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_150B')

    def _loc_14C1(): pass

    label('loc_14C1')

    ChrTalk(
        0x00FE,
        (
            '老板好像也非常\n',
            '繁忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来到店里也只是稍做视察\n',
            '就回市长官邸了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_150B(): pass

    label('loc_150B')

    Jump('loc_19D2')

    def _loc_150E(): pass

    label('loc_150E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_162C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1571',
    )

    ChrTalk(
        0x00FE,
        (
            '享受葡萄酒的那种气氛\n',
            '终于又回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回过头来想想，\n',
            '果然还是和平最重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1629')

    def _loc_1571(): pass

    label('loc_1571')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '欢迎来到安特洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '享受葡萄酒的那种气氛\n',
            '终于又回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常有人说\n',
            '『空腹是最好的调味料』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仿效这句话，\n',
            '我们是不是可以说\n',
            '『和平才是最棒的佐料』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_1629(): pass

    label('loc_1629')

    Jump('loc_19D2')

    def _loc_162C(): pass

    label('loc_162C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_171A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_168D',
    )

    ChrTalk(
        0x00FE,
        (
            '超市的重建工程\n',
            '加上拉文努村的复兴支援……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老板梅贝尔市长也\n',
            '终日忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1717')

    def _loc_168D(): pass

    label('loc_168D')

    ChrTalk(
        0x00FE,
        (
            '超市的重建工程\n',
            '加上拉文努村的复兴支援……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老板梅贝尔市长\n',
            '一直在忙碌着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不劳烦到她，\n',
            '我们尽力把店铺的经营做到最好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_1717(): pass

    label('loc_1717')

    Jump('loc_19D2')

    def _loc_171A(): pass

    label('loc_171A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_183D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1768',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然混乱还在继续，\n',
            '但本店依然照常营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请多担待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_183A')

    def _loc_1768(): pass

    label('loc_1768')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '昨天真是紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，在非常时期\n',
            '能无视利益团结起来…\n',
            '这正是柏斯商人的传统。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '１０年前那场战争的时候，\n',
            '本店也为难民们提供过伙食。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后若是有什么事的话，\n',
            '也请让我们参与协助吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_183A(): pass

    label('loc_183A')

    Jump('loc_19D2')

    def _loc_183D(): pass

    label('loc_183D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1904',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1879',
    )

    ChrTalk(
        0x00FE,
        (
            '老板联系过我们了，\n',
            '看来情况非常严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1901')

    def _loc_1879(): pass

    label('loc_1879')

    ChrTalk(
        0x00FE,
        (
            '老板联系过我们了，\n',
            '看来情况非常严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在，正在为各位前来避难的\n',
            '朋友准备热汤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喝一点热腾腾的东西\n',
            '心情会比较平静吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_1901(): pass

    label('loc_1901')

    Jump('loc_19D2')

    def _loc_1904(): pass

    label('loc_1904')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_19D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1952',
    )

    ChrTalk(
        0x00FE,
        (
            '必定会拿出\n',
            '让各位满足的料理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请一定要好好品尝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19D2')

    def _loc_1952(): pass

    label('loc_1952')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '欢迎来到安特洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最棒的材料，最好的工作人员\n',
            '将接待各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请务必在我店\n',
            '领略一下利贝尔料理的精髓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_19D2(): pass

    label('loc_19D2')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x19D6
@scena.Code('func_07_19D6')
def func_07_19D6():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1ABF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A79',
    )

    ChrTalk(
        0x00FE,
        (
            '新出道的商人\n',
            '干得不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '托他的福，特殊食材\n',
            '的货源现在很充足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A73',
    )

    ChrTalk(
        0x00FE,
        (
            '……非常感激。\n',
            '介绍了一位出色的商人给我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A73(): pass

    label('loc_1A73')

    OP_A2(0x0001)

    Jump('loc_1ABC')

    def _loc_1A79(): pass

    label('loc_1A79')

    ChrTalk(
        0x00FE,
        (
            '新出道的商人\n',
            '干得不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽然他的收集的种类非常极端。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1ABC(): pass

    label('loc_1ABC')

    Jump('loc_1F65')

    def _loc_1ABF(): pass

    label('loc_1ABF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B23',
    )

    ChrTalk(
        0x00FE,
        (
            '就算没有了导力式的烹饪工具，\n',
            '问题也不会很大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真正的烹饪高手\n',
            '是不会挑剔道具的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F65')

    def _loc_1B23(): pass

    label('loc_1B23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1B8B',
    )

    ChrTalk(
        0x00FE,
        (
            '食材总算进到货了，\n',
            '恢复到平时的状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样就可以毫无顾虑地\n',
            '放手做我的拿手好菜啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F65')

    def _loc_1B8B(): pass

    label('loc_1B8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1CF5',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C59',
    )

    ChrTalk(
        0x00FE,
        (
            '由于定期船停航的缘故，\n',
            '进货变得非常困难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过好在多亏了那个新来的商人，\n',
            '或许能够撑一段时间也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然材料种类稍微有点极端，\n',
            '但货源数量还是可以保证的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF2')

    def _loc_1C59(): pass

    label('loc_1C59')

    ChrTalk(
        0x00FE,
        (
            '由于定期船停航的缘故，\n',
            '食材的进货情况很紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '花费时间过长，\n',
            '有必要对菜单进行浓缩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了兴致勃勃赶来的客人，\n',
            '这些事无论如何一定要避免……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF2(): pass

    label('loc_1CF2')

    Jump('loc_1F65')

    def _loc_1CF5(): pass

    label('loc_1CF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1DCA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D84',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船好像停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不使食材进货停滞，\n',
            '必须先行动才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '现在就看新来的商人的表现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DC7')

    def _loc_1D84(): pass

    label('loc_1D84')

    ChrTalk(
        0x00FE,
        (
            '定期船好像停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不使食材进货停滞，\n',
            '必须尽早行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DC7(): pass

    label('loc_1DC7')

    Jump('loc_1F65')

    def _loc_1DCA(): pass

    label('loc_1DCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1E0D',
    )

    ChrTalk(
        0x00FE,
        (
            '经理满脸怒气的\n',
            '来点东西吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……出什么事了吗',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F65')

    def _loc_1E0D(): pass

    label('loc_1E0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1F65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1E8E',
    )

    ChrTalk(
        0x00FE,
        (
            '格露娜发明的料理\n',
            '终于写进我们的菜单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她的料理完全发挥出她的特质，\n',
            '我想应该能够形成一种崭新的风味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F65')

    def _loc_1E8E(): pass

    label('loc_1E8E')

    ChrTalk(
        0x00FE,
        (
            '格露娜发明的料理\n',
            '终于写进我们的菜单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她的料理完全发挥出她的特质，\n',
            '我想应该能够形成一种崭新的风味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '菜单不能固定，\n',
            '要不断给客人带来惊喜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想成为一流的料理人\n',
            '就是要不断追寻自我革新的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1F65(): pass

    label('loc_1F65')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x1F69
@scena.Code('func_08_1F69')
def func_08_1F69():
    TalkBegin(0x000A)

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1F84',
    )

    Call(0, 0x0009)

    Jump('loc_1FAA')

    def _loc_1F84(): pass

    label('loc_1F84')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_1F95',
    )

    Call(2, 0x0001)

    Jump('loc_1FAA')

    def _loc_1F95(): pass

    label('loc_1F95')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_1FA6',
    )

    Call(2, 0x0000)

    Jump('loc_1FAA')

    def _loc_1FA6(): pass

    label('loc_1FA6')

    Call(0, 0x0009)

    def _loc_1FAA(): pass

    label('loc_1FAA')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1FAE
@scena.Code('func_09_1FAE')
def func_09_1FAE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_200A',
    )

    ChrTalk(
        0x000A,
        (
            '今天太谢谢了。\n',
            '真是帮了我们大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那，若是有空的话，\n',
            '请务必来店里吃饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B3')

    def _loc_200A(): pass

    label('loc_200A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2138',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20E1',
    )

    ChrTalk(
        0x000A,
        (
            '真不愧是罗宋厨师长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '竟能用火炉把平常那些高级料理\n',
            '简简单单的作出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '与之相比，\n',
            '我真是差远了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯～～热血沸腾了！\n',
            '得好好锻炼本领了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '然后，总有一天一定\n',
            '要赶上料理长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_2135')

    def _loc_20E1(): pass

    label('loc_20E1')

    ChrTalk(
        0x000A,
        (
            '和料理长比起来的话，\n',
            '我还不成熟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯～～热血沸腾了！\n',
            '得好好锻炼本领了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2135(): pass

    label('loc_2135')

    Jump('loc_28B3')

    def _loc_2138(): pass

    label('loc_2138')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_220B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21C6',
    )

    ChrTalk(
        0x000A,
        (
            '导，导力式炉子\n',
            '用不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看料理长优哉优哉的，\n',
            '我就没有这么从容了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不赶快掌握\n',
            '炉灶的火候控制方法的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_2208')

    def _loc_21C6(): pass

    label('loc_21C6')

    ChrTalk(
        0x000A,
        (
            '导力式火炉\n',
            '不能使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯～用火炉调理\n',
            '能顺利完成吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2208(): pass

    label('loc_2208')

    Jump('loc_28B3')

    def _loc_220B(): pass

    label('loc_220B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_23AA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_232C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2284',
    )

    ChrTalk(
        0x000A,
        (
            '定期船恢复了，\n',
            '进货也恢复到原来的状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '感觉新菜单的研究\n',
            '现在才算真正开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_2284(): pass

    label('loc_2284')

    ChrTalk(
        0x000A,
        (
            '定期船恢复了，\n',
            '进货也恢复到原来的状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '稀有食材方面\n',
            '有那个新出道的商人\n',
            '在做调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '感觉新菜单的研究\n',
            '现在才算真正开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好，鼓足干劲加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_2329(): pass

    label('loc_2329')

    Jump('loc_23A7')

    def _loc_232C(): pass

    label('loc_232C')

    ChrTalk(
        0x000A,
        (
            '虽然定期船恢复了，\n',
            '进货也恢复了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '部分珍贵食材\n',
            '还是很难弄到手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '为了研究新菜单，\n',
            '这个问题务必要解决啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_23A7(): pass

    label('loc_23A7')

    Jump('loc_28B3')

    def _loc_23AA(): pass

    label('loc_23AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_25C5',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2421',
    )

    ChrTalk(
        0x000A,
        (
            '料理长好像也在为\n',
            '进货的事烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '和奥维德联手，\n',
            '无论如何都要突破这次困境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_2421(): pass

    label('loc_2421')

    ChrTalk(
        0x000A,
        (
            '料理长好像也在为\n',
            '进货的事烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '和奥维德联手，\n',
            '无论如何都要突破这次困境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然不知道为什么，\n',
            '但那个人好像并不在乎\n',
            '定期船停航。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不知道是不是拥有和其它商人\n',
            '不同的进货管道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_24E3(): pass

    label('loc_24E3')

    Jump('loc_25C2')

    def _loc_24E6(): pass

    label('loc_24E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2540',
    )

    ChrTalk(
        0x000A,
        (
            '料理长好像也在为\n',
            '进货的事烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '商人们因为超市的事\n',
            '也没法顾及我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25C2')

    def _loc_2540(): pass

    label('loc_2540')

    ChrTalk(
        0x000A,
        (
            '料理长好像也在为\n',
            '进货的事烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '商人们因为超市的事\n',
            '也没法顾及我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊，一感到不安，\n',
            '舌头尝味的感觉会迟钝的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_25C2(): pass

    label('loc_25C2')

    Jump('loc_28B3')

    def _loc_25C5(): pass

    label('loc_25C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_26AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_262E',
    )

    ChrTalk(
        0x000A,
        (
            '听莉诺说\n',
            '好像有客人来相亲是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果能因为我们的料理\n',
            '营造出不错的气氛就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A8')

    def _loc_262E(): pass

    label('loc_262E')

    ChrTalk(
        0x000A,
        (
            '听莉诺说\n',
            '好像有客人来相亲是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样的事\n',
            '给人感觉压力很大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这种席位的气氛\n',
            '会随料理的不同发生变化呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_26A8(): pass

    label('loc_26A8')

    Jump('loc_28B3')

    def _loc_26AB(): pass

    label('loc_26AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_279D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_271F',
    )

    ChrTalk(
        0x000A,
        (
            '好像店里的人在吵闹什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是……\n',
            '我现在正忙着准备主菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '来，集中精神！集中精神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_279A')

    def _loc_271F(): pass

    label('loc_271F')

    ChrTalk(
        0x000A,
        (
            '好像店里的人在吵闹什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是……\n',
            '我现在正忙着准备主菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '在这节骨眼上松懈的话，\n',
            '成品可是会大大走样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_279A(): pass

    label('loc_279A')

    Jump('loc_28B3')

    def _loc_279D(): pass

    label('loc_279D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_28B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_27FA',
    )

    ChrTalk(
        0x000A,
        (
            '我制作的料理\n',
            '终于写进菜单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '当然我不会就此满足，\n',
            '还要继续努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B3')

    def _loc_27FA(): pass

    label('loc_27FA')

    ChrTalk(
        0x000A,
        (
            '我制作的料理\n',
            '终于写进菜单了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过这多亏了料理长用自己的时间\n',
            '陪我做新菜的尝试啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '所以不能说是自己的实力，\n',
            '现在绝对还不能满足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '所以计划马上开始\n',
            '新作品的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_28B3(): pass

    label('loc_28B3')

    Return()

# id: 0x000A offset: 0x28B4
@scena.Code('func_0A_28B4')
def func_0A_28B4():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_297F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_292C',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船好像\n',
            '还没有恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正打算订购葡萄酒，\n',
            '却发生这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，时机真的很糟糕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_297C')

    def _loc_292C(): pass

    label('loc_292C')

    ChrTalk(
        0x00FE,
        (
            '定期船好像\n',
            '还没有恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正打算订购葡萄酒，\n',
            '还在考虑的时候却出这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_297C(): pass

    label('loc_297C')

    Jump('loc_2FC8')

    def _loc_297F(): pass

    label('loc_297F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2A72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A13',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器停止的时候，\n',
            '我在葡萄酒窖里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果在一片漆黑中\n',
            '只能靠自己摸索走出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果身上满是灰尘。\n',
            '怎么会那么巧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_2A6F')

    def _loc_2A13(): pass

    label('loc_2A13')

    ChrTalk(
        0x00FE,
        (
            '导力器停止时，\n',
            '我在葡萄酒窖里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在一片漆黑中靠摸索着…\n',
            '想走出来真是太难了，可恶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A6F(): pass

    label('loc_2A6F')

    Jump('loc_2FC8')

    def _loc_2A72(): pass

    label('loc_2A72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2B7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2ACD',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，今早的快递\n',
            '终于把葡萄酒送来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '库存差一点\n',
            '就没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B7C')

    def _loc_2ACD(): pass

    label('loc_2ACD')

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，今早的快递\n',
            '总算把葡萄酒送来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每次定期船停班的时候\n',
            '我都会很担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全靠这飞船\n',
            '才能享受到世界上的各种美酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要想到这个\n',
            '就不会有太多怨言了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2B7C(): pass

    label('loc_2B7C')

    Jump('loc_2FC8')

    def _loc_2B7F(): pass

    label('loc_2B7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2CBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2BE4',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯地区的航空管制\n',
            '似乎还没有解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一部分品牌的葡萄酒\n',
            '都已经快断货了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CB7')

    def _loc_2BE4(): pass

    label('loc_2BE4')

    ChrTalk(
        0x00FE,
        (
            '真差劲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯地区的航空管制\n',
            '似乎还没有解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一部分品牌的葡萄酒\n',
            '已经快把库存用光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '库存最紧张的是\n',
            '中等价格的葡萄酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为来这里的客人大多是行家。\n',
            '很清楚哪些酒质量高又价格合理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2CB7(): pass

    label('loc_2CB7')

    Jump('loc_2FC8')

    def _loc_2CBA(): pass

    label('loc_2CBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2DB8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2D23',
    )

    ChrTalk(
        0x00FE,
        (
            '因为军队的作战\n',
            '飞船又停开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如战斗持续太久的话，\n',
            '销量大的葡萄酒会不够的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DB5')

    def _loc_2D23(): pass

    label('loc_2D23')

    ChrTalk(
        0x00FE,
        (
            '呼，真头疼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为军队的作战\n',
            '飞船又停开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诺桑普里亚产的葡萄酒\n',
            '预定好了要送来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望快点抓住龙，\n',
            '好早日解除戒严。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2DB5(): pass

    label('loc_2DB5')

    Jump('loc_2FC8')

    def _loc_2DB8(): pass

    label('loc_2DB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2E61',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2DF8',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然不是很清楚，\n',
            '不过外面好像出什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E5E')

    def _loc_2DF8(): pass

    label('loc_2DF8')

    ChrTalk(
        0x00FE,
        (
            '虽然不是很清楚，\n',
            '不过外面好像出什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '用箱子把矿泉水拿出去。\n',
            '其他的以后再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2E5E(): pass

    label('loc_2E5E')

    Jump('loc_2FC8')

    def _loc_2E61(): pass

    label('loc_2E61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2FC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2ED2',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在和老板商量，\n',
            '是不是也进一些东方的『清酒』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个也有着不逊于葡萄酒\n',
            '的丰富的味道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FC8')

    def _loc_2ED2(): pass

    label('loc_2ED2')

    ChrTalk(
        0x00FE,
        (
            '我是这家店的品酒员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提起品酒员，\n',
            '大多数人都是只热衷于葡萄酒，\n',
            '而我的话则对所有酒类都在行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在和老板商量，\n',
            '是不是也进一些东方的『清酒』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个也有着不逊于葡萄酒\n',
            '的丰富味道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许更适合配合清淡的食物\n',
            '来吃也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2FC8(): pass

    label('loc_2FC8')

    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x2FCC
@scena.Code('func_0B_2FCC')
def func_0B_2FCC():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_3078',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3040',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市里的情况已经\n',
            '完全安定下来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请各位客人\n',
            '好好品尝我们的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_3075')

    def _loc_3040(): pass

    label('loc_3040')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请各位客人\n',
            '好好品尝我们的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3075(): pass

    label('loc_3075')

    Jump('loc_3570')

    def _loc_3078(): pass

    label('loc_3078')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3185',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_312E',
    )

    ChrTalk(
        0x00FE,
        (
            '市里发生骚乱的时候，\n',
            '我们正在店里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '协会前聚集了很多人，\n',
            '一直争吵到深夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为从店里看去一片漆黑，\n',
            '所以不知道发生了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，真的非常害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_3182')

    def _loc_312E(): pass

    label('loc_312E')

    ChrTalk(
        0x00FE,
        (
            '镇上发生骚乱的时候，\n',
            '我们正在店里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '协会前聚集了很多人，\n',
            '一直争吵到深夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3182(): pass

    label('loc_3182')

    Jump('loc_3570')

    def _loc_3185(): pass

    label('loc_3185')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3280',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_31D8',
    )

    ChrTalk(
        0x00FE,
        (
            '来相亲的帝国青年\n',
            '已经回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那位女学生\n',
            '也回老家去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327D')

    def _loc_31D8(): pass

    label('loc_31D8')

    ChrTalk(
        0x00FE,
        (
            '来相亲的帝国青年\n',
            '已经回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那位女学生\n',
            '也回老家去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此，居然会来我们的餐厅相亲，\n',
            '可真是万万没有想到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯。\n',
            '一定都是出生自名门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_327D(): pass

    label('loc_327D')

    Jump('loc_3570')

    def _loc_3280(): pass

    label('loc_3280')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_32DC',
    )

    ChrTalk(
        0x00FE,
        (
            '大家都在很卖力地为超市的\n',
            '工程忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连这里也可以听到\n',
            '机械轰鸣的声音呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3570')

    def _loc_32DC(): pass

    label('loc_32DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3401',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3380',
    )

    ChrTalk(
        0x00FE,
        (
            '坐在相亲席上的女性……\n',
            '怎么看都好像是学生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种年纪就来相亲，\n',
            '是不是稍微着急了一点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还，还是说会这么想的我\n',
            '还比较幼稚呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33FE')

    def _loc_3380(): pass

    label('loc_3380')

    ChrTalk(
        0x00FE,
        (
            '看起来，\n',
            '那桌人好像在相亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边那位女性……\n',
            '怎么看都好像是学生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种年纪就来相亲，\n',
            '稍微着急了一点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_33FE(): pass

    label('loc_33FE')

    Jump('loc_3570')

    def _loc_3401(): pass

    label('loc_3401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_34A3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3462',
    )

    ChrTalk(
        0x00FE,
        (
            '超市被巨大的魔兽\n',
            '袭击了是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之得把前来避难\n',
            '的人们带到座位上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34A0')

    def _loc_3462(): pass

    label('loc_3462')

    ChrTalk(
        0x00FE,
        (
            '超市被巨大的魔兽\n',
            '袭击了是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不敢相信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_34A0(): pass

    label('loc_34A0')

    Jump('loc_3570')

    def _loc_34A3(): pass

    label('loc_34A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_3570',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_34FB',
    )

    ChrTalk(
        0x00FE,
        (
            '相亲的对象\n',
            '好像已经到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，太好了。\n',
            '接下来就上菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3570')

    def _loc_34FB(): pass

    label('loc_34FB')

    ChrTalk(
        0x00FE,
        (
            '今天预定要见\n',
            '来自帝国的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是怎么说呢、\n',
            '这好像是为了相亲而设的桌子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，对象是\n',
            '王国的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3570(): pass

    label('loc_3570')

    TalkEnd(0x000C)

    Return()

# id: 0x000C offset: 0x3574
@scena.Code('func_0C_3574')
def func_0C_3574():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_3688',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_361B',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯…\n',
            '这味道尝起来和平时一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的餐厅\n',
            '应该也不能使用导力炉才对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使如此，味道还是维持原来的水平，\n',
            '真不愧是安特洛丝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_3685')

    def _loc_361B(): pass

    label('loc_361B')

    ChrTalk(
        0x00FE,
        (
            '这里的餐厅\n',
            '应该也不能使用导力炉才对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使如此，味道还是维持原来的水平，\n',
            '真不愧是安特洛丝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3685(): pass

    label('loc_3685')

    Jump('loc_3BB5')

    def _loc_3688(): pass

    label('loc_3688')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_376B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3714',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔……\n',
            '完全以为是导力器的故障……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据我所见，\n',
            '市里的情况有点异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，这么说来，\n',
            '究竟出什么事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_3768')

    def _loc_3714(): pass

    label('loc_3714')

    ChrTalk(
        0x00FE,
        (
            '因为导力器发生故障，\n',
            '市里的情况有点异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔……\n',
            '这个世界还真是奇妙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3768(): pass

    label('loc_3768')

    Jump('loc_3BB5')

    def _loc_376B(): pass

    label('loc_376B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3884',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_37C3',
    )

    ChrTalk(
        0x00FE,
        (
            '和年轻人交谈果然有益啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个年轻人也为了取得\n',
            '成功而努力着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3881')

    def _loc_37C3(): pass

    label('loc_37C3')

    ChrTalk(
        0x00FE,
        (
            '哎呀，这几天，\n',
            '和碰巧相识的一个新手商人\n',
            '聊了聊关于买卖的话题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和年轻人交谈果然有益啊。\n',
            '原本打算传授他人知识的我\n',
            '反而受了鼓励啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，真希望今后\n',
            '还能在这里探讨问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_3881(): pass

    label('loc_3881')

    Jump('loc_3BB5')

    def _loc_3884(): pass

    label('loc_3884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_38F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_38E9',
    )

    ChrTalk(
        0x00FE,
        (
            '面对面做买卖，终究\n',
            '是人与人的应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '单纯的追求数字，\n',
            '总有一天会吃苦头的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38ED')

    def _loc_38E9(): pass

    label('loc_38E9')

    Call(0, 0x0019)

    def _loc_38ED(): pass

    label('loc_38ED')

    Jump('loc_3BB5')

    def _loc_38F0(): pass

    label('loc_38F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_39F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3953',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天遇到了一位\n',
            '即将在超市里开店的年轻人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '并和他约定\n',
            '今天也在这里见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39EF')

    def _loc_3953(): pass

    label('loc_3953')

    ChrTalk(
        0x00FE,
        (
            '昨天遇到了一位\n',
            '即将在超市里开店的年轻人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为想给他一些生意上的建议，\n',
            '所以今天也约他在这里见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，和晚辈交谈\n',
            '真的是年长者的乐趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_39EF(): pass

    label('loc_39EF')

    Jump('loc_3BB5')

    def _loc_39F2(): pass

    label('loc_39F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3B35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3A6D',
    )

    ChrTalk(
        0x00FE,
        (
            '这个年轻人在商店即将开业前\n',
            '被卷入了某起事件当中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也曾在超市开过店，\n',
            '假如能帮上他的忙就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B32')

    def _loc_3A6D(): pass

    label('loc_3A6D')

    ChrTalk(
        0x00FE,
        (
            '好像是\n',
            '有某种巨大的怪物袭击了超市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这位年轻人在即将开业的时候，\n',
            '被卷入了某起事件当中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一切都即将开始的时候，\n',
            '遇到了这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也曾在超市开过店，\n',
            '假如能帮上他的忙就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_3B32(): pass

    label('loc_3B32')

    Jump('loc_3BB5')

    def _loc_3B35(): pass

    label('loc_3B35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_3BB5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3B54',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BB5')

    def _loc_3B54(): pass

    label('loc_3B54')

    ChrTalk(
        0x00FE,
        (
            '嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这肉汁……\n',
            '菜式新而且味道也非常棒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的料理\n',
            '总是让人期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_3BB5(): pass

    label('loc_3BB5')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x3BB9
@scena.Code('func_0D_3BB9')
def func_0D_3BB9():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_3C9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C48',
    )

    ChrTalk(
        0x00FE,
        (
            '城里的人们\n',
            '虽然又有了精神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这没有导力器的日子\n',
            '究竟还要持续多久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想到这个\n',
            '实在没法尽情笑出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_3C9C')

    def _loc_3C48(): pass

    label('loc_3C48')

    ChrTalk(
        0x00FE,
        (
            '但这没有导力器的日子\n',
            '究竟还要持续多久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想到这个\n',
            '实在没法尽情笑出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C9C(): pass

    label('loc_3C9C')

    Jump('loc_4272')

    def _loc_3C9F(): pass

    label('loc_3C9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3DB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D5B',
    )

    ChrTalk(
        0x00FE,
        (
            '夜晚的骚乱可真严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '若没有梅贝尔市长出面说服的话，\n',
            '险些就爆发暴动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在明明是\n',
            '考验大家明辨是非能力的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种丢人的举动\n',
            '再也不想看到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_3DAE')

    def _loc_3D5B(): pass

    label('loc_3D5B')

    ChrTalk(
        0x00FE,
        (
            '夜晚的骚乱可真严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '若没有梅贝尔市长出面说服的话，\n',
            '险些就爆发暴动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DAE(): pass

    label('loc_3DAE')

    Jump('loc_4272')

    def _loc_3DB1(): pass

    label('loc_3DB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3E9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3DF9',
    )

    ChrTalk(
        0x00FE,
        (
            '这肉汁\n',
            '好像是道新菜式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，味道很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E98')

    def _loc_3DF9(): pass

    label('loc_3DF9')

    ChrTalk(
        0x00FE,
        (
            '哎呀，之前丝毫\n',
            '没有察觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这肉汁\n',
            '好像是道新菜式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可真是的……\n',
            '明明吃过很多次了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，发生事件的期间\n',
            '实在太多事情让人分心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_3E98(): pass

    label('loc_3E98')

    Jump('loc_4272')

    def _loc_3E9B(): pass

    label('loc_3E9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3FBE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3EFE',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得梅贝尔市长\n',
            '做的很出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲一定在女神爱德丝的身旁\n',
            '对着她微笑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FBB')

    def _loc_3EFE(): pass

    label('loc_3EFE')

    ChrTalk(
        0x00FE,
        (
            '前市长的政治手段\n',
            '真的很出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现任市长梅贝尔小姐\n',
            '是前市长的亲生女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然市民经常拿她和她父亲比较。\n',
            '但我认为她做得很出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲一定在女神爱德丝的身旁\n',
            '对着她微笑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_3FBB(): pass

    label('loc_3FBB')

    Jump('loc_4272')

    def _loc_3FBE(): pass

    label('loc_3FBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_4084',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4010',
    )

    ChrTalk(
        0x00FE,
        (
            '看着现在的城市\n',
            '让我想起了战争……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4081')

    def _loc_4010(): pass

    label('loc_4010')

    ChrTalk(
        0x00FE,
        (
            '超市的修复工程，\n',
            '在街上走的军人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一切都和１０年前的战争\n',
            '一摸一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_4081(): pass

    label('loc_4081')

    Jump('loc_4272')

    def _loc_4084(): pass

    label('loc_4084')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_418D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_40F9',
    )

    ChrTalk(
        0x00FE,
        (
            '在１０年前的那场战争里\n',
            '也听到过刚才的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '石造的建筑物坍塌时\n',
            '肯定会发出那样的声音的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_418A')

    def _loc_40F9(): pass

    label('loc_40F9')

    ChrTalk(
        0x00FE,
        (
            '刚才那声巨响……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让我想起了\n',
            '１０年前的那场战争……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时候也是，\n',
            '整个城市都被那种声音回绕着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '建筑物……倒塌的声音啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_418A(): pass

    label('loc_418A')

    Jump('loc_4272')

    def _loc_418D(): pass

    label('loc_418D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_4272',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_41E8',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然帝国的人\n',
            '在这里并不罕见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是……\n',
            '有种说不出的感觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4272')

    def _loc_41E8(): pass

    label('loc_41E8')

    ChrTalk(
        0x00FE,
        (
            '那边那张桌子的客人……\n',
            '好像是帝国的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约也签订了，\n',
            '隔阂虽然不像以前那么大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是\n',
            '有种说不出的感觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_4272(): pass

    label('loc_4272')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x4276
@scena.Code('func_0E_4276')
def func_0E_4276():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_42D1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_42B8',
    )

    ChrTalk(
        0x00FE,
        (
            '我也在赶时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快点开始商谈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_42CE')

    def _loc_42B8(): pass

    label('loc_42B8')

    ChrTalk(
        0x00FE,
        (
            '快点开始商谈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42CE(): pass

    label('loc_42CE')

    Jump('loc_4656')

    def _loc_42D1(): pass

    label('loc_42D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_4397',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_4305',
    )

    ChrTalk(
        0x00FE,
        (
            '哪里，这次\n',
            '十分感谢您的协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4394')

    def _loc_4305(): pass

    label('loc_4305')

    ChrTalk(
        0x00FE,
        (
            '哪里，这次\n',
            '十分感谢您的协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市被封锁的时候\n',
            '有点不知所措……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过托各位的福，\n',
            '本商会非但没有受到损失，\n',
            '反而还获得了利益。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_4394(): pass

    label('loc_4394')

    Jump('loc_4656')

    def _loc_4397(): pass

    label('loc_4397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_44C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_4414',
    )

    ChrTalk(
        0x00FE,
        (
            '如果在果物进货方面遇到了困难，\n',
            '本商会愿意提供储备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里，毕竟是非常时期，\n',
            '价格按照平常的就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44BE')

    def _loc_4414(): pass

    label('loc_4414')

    ChrTalk(
        0x00FE,
        (
            '如果是拉文努村产的水果的话，\n',
            '本商会的储备非常充足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看各位好像很为难，\n',
            '若是不嫌弃的话我们来提供这些水果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里，毕竟是非常时期，\n',
            '价格按照平常的就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_44BE(): pass

    label('loc_44BE')

    Jump('loc_4656')

    def _loc_44C1(): pass

    label('loc_44C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_451F',
    )

    ChrTalk(
        0x00FE,
        (
            '继超市被封锁后\n',
            '定期船也被停航了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真为难啊。\n',
            '这样的话进货就停止了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4656')

    def _loc_451F(): pass

    label('loc_451F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_45FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_4582',
    )

    ChrTalk(
        0x00FE,
        (
            '封锁超市的话，\n',
            '会使物价发生很大的变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这样的话商谈\n',
            '就从头开始啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45FA')

    def _loc_4582(): pass

    label('loc_4582')

    ChrTalk(
        0x00FE,
        (
            '在，在超市\n',
            '发生这种事……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这样的话商谈\n',
            '就从头开始啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通路被封锁的话\n',
            '会使物价发生很大的变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_45FA(): pass

    label('loc_45FA')

    Jump('loc_4656')

    def _loc_45FD(): pass

    label('loc_45FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_4656',
    )

    ChrTalk(
        0x00FE,
        (
            '关于下次的买卖，\n',
            '这样的价格如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即便和竞争公司相比\n',
            '也是相当优惠的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4656(): pass

    label('loc_4656')

    TalkEnd(0x000F)

    Return()

# id: 0x000F offset: 0x465A
@scena.Code('func_0F_465A')
def func_0F_465A():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_46F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46C0',
    )

    ChrTalk(
        0x00FE,
        (
            '这么急把你叫来，\n',
            '很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是有话要和你说，\n',
            '希望能尽快把买卖定下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_46F5')

    def _loc_46C0(): pass

    label('loc_46C0')

    ChrTalk(
        0x00FE,
        (
            '这么急把你叫来，\n',
            '很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次也请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46F5(): pass

    label('loc_46F5')

    Jump('loc_4A8C')

    def _loc_46F8(): pass

    label('loc_46F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_480D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4773',
    )

    ChrTalk(
        0x00FE,
        (
            '抛开这笔交易是否有利润不谈，\n',
            '但总算还做得成买卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '双方只要互相协助的话，\n',
            '果然还是有好的结果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_480A')

    def _loc_4773(): pass

    label('loc_4773')

    ChrTalk(
        0x00FE,
        (
            '哪里哪里，\n',
            '这都多亏了您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的交易虽然是\n',
            '不考虑利益的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算是……\n',
            '我们也得到很不错的商业伙伴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船提前恢复\n',
            '起作用了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_480A(): pass

    label('loc_480A')

    Jump('loc_4A8C')

    def _loc_480D(): pass

    label('loc_480D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_4906',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4872',
    )

    ChrTalk(
        0x00FE,
        (
            '海产品的进货\n',
            '请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟是非常时期，\n',
            '就让我们互相协助经营下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4903')

    def _loc_4872(): pass

    label('loc_4872')

    ChrTalk(
        0x00FE,
        (
            '那么的话，\n',
            '请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '货物还有一部分\n',
            '保管在柏斯的仓库。\n',
            '应该就能够救急了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟是非常时期，\n',
            '就让我们互相协助经营下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_4903(): pass

    label('loc_4903')

    Jump('loc_4A8C')

    def _loc_4906(): pass

    label('loc_4906')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_496F',
    )

    ChrTalk(
        0x00FE,
        (
            '拉文努村\n',
            '的果树园好像也被破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，真头痛。\n',
            '我们的水果几乎都是\n',
            '从那里进货的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A8C')

    def _loc_496F(): pass

    label('loc_496F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_4A2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_49CF',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到会发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本次的商业洽谈\n',
            '进展的还算比较顺利，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A2C')

    def _loc_49CF(): pass

    label('loc_49CF')

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '好像是非常严重的事态呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在进行中的交易\n',
            '必须要重新审查一遍才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_4A2C(): pass

    label('loc_4A2C')

    Jump('loc_4A8C')

    def _loc_4A2F(): pass

    label('loc_4A2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_4A8C',
    )

    ChrTalk(
        0x00FE,
        (
            '不，很抱歉，\n',
            '这样的价格我们无法答应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在物流也通畅了，\n',
            '库存应该很充裕吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A8C(): pass

    label('loc_4A8C')

    TalkEnd(0x0010)

    Return()

# id: 0x0010 offset: 0x4A90
@scena.Code('func_10_4A90')
def func_10_4A90():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BE5',
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
            TXT(0x00, '【◇123老爸帮忙通关＋关联任务完全称霸】\n'),
            TXT(0x01, '【◇123老爸帮忙通关】\n'),
            TXT(0x02, '【◇101通关】\n'),
            TXT(0x03, '【◇后编未接触】\n'),
            TXT(0x04, '【◇５章看初次】\n'),
            TXT(0x05, '【◇不变更】\n'),
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
        (0x00000000, 'loc_4B5A'),
        (0x00000001, 'loc_4B77'),
        (0x00000002, 'loc_4B94'),
        (0x00000003, 'loc_4BB1'),
        (0x00000004, 'loc_4BCE'),
        (0x00000005, 'loc_4BE2'),
        (-1, 'loc_4BE5'),
    )

    def _loc_4B5A(): pass

    label('loc_4B5A')

    OP_28(0x007B, 0x04, 0x10)
    OP_28(0x007B, 0x01, 0x0008)
    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0005, 0x04, 0x10)
    OP_28(0x001F, 0x04, 0x10)

    Jump('loc_4BE5')

    def _loc_4B77(): pass

    label('loc_4B77')

    OP_28(0x007B, 0x04, 0x10)
    OP_28(0x007B, 0x01, 0x0008)
    OP_28(0x0065, 0x03, 0x10)
    OP_28(0x0005, 0x03, 0x10)
    OP_28(0x001F, 0x03, 0x10)

    Jump('loc_4BE5')

    def _loc_4B94(): pass

    label('loc_4B94')

    OP_28(0x007B, 0x03, 0x10)
    OP_28(0x007B, 0x02, 0x0008)
    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0005, 0x03, 0x10)
    OP_28(0x001F, 0x03, 0x10)

    Jump('loc_4BE5')

    def _loc_4BB1(): pass

    label('loc_4BB1')

    OP_28(0x007B, 0x03, 0x10)
    OP_28(0x007B, 0x02, 0x0008)
    OP_28(0x0065, 0x03, 0x10)
    OP_28(0x0005, 0x03, 0x10)
    OP_28(0x001F, 0x03, 0x10)

    Jump('loc_4BE5')

    def _loc_4BCE(): pass

    label('loc_4BCE')

    OP_28(0x007B, 0x04, 0x10)
    OP_28(0x007B, 0x01, 0x0008)
    OP_28(0x007B, 0x01, 0x8000)

    Jump('loc_4BE5')

    def _loc_4BE2(): pass

    label('loc_4BE2')

    Jump('loc_4BE5')

    def _loc_4BE5(): pass

    label('loc_4BE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_58E6',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_57A9',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -35260, 0, 42950, 90)
    SetChrPos(0x00F7, -35690, 0, 41950, 90)
    SetChrPos(0x00F8, -36550, 0, 43150, 90)
    SetChrPos(0x00F9, -36640, 0, 41730, 90)
    OP_8C(0x0011, 270, 0)
    OP_4A(0x0011, 255)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C7A',
    )

    SetChrPos(0x0004, -35970, 0, 44280, 135)

    def _loc_4C7A(): pass

    label('loc_4C7A')

    OP_6D(-35000, 0, 42570, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0011,
        (
            '噢噢，各位游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '有好消息啊！\n',
            '商业洽谈成功了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我终于成为能够\n',
            '出入一流餐厅的商人了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1004F真、真的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1001F说的是和安特洛丝的交易吧。\n',
            '真厉害，叔叔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F祝贺你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '各位游击士。\n',
            '真的非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '能够和这家店做买卖\n',
            '是我多年来的梦想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这梦想终于实现了……\n',
            '这全都是各位的功劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，之所以会有今天\n',
            '全都是叔叔自己努力的结果啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们只是稍微\n',
            '帮了一点小忙而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5466',
    )

    ChrTalk(
        0x0011,
        (
            '嗯……\n',
            '和你们认识好像也已经很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '明明给你们添了很多麻烦，\n',
            '你们却能一直帮助我到现在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '作为对过去的答谢，\n',
            '请收下我这份谢礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1020F难，难道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '又想送很多奇怪的蘑菇\n',
            '给我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嗯？想要蘑菇吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这样的话，\n',
            '这里还有很多库存……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1007F不，不，不用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F……抱歉。\n',
            '打断你说话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嗯，刚才说到谢礼是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '所谓谢礼并不是别的。\n',
            '那就是我奥维德商会的会员资格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这可不是一般的会员，\n',
            '是最高级别的白金会员资格哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F白、白金会员资格？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊，如你所知，\n',
            '我是专门做食材生意的商人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但我只和其他职业商人做买卖。\n',
            '面向一般顾客的零售生意我是不做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但是曾经受到你们太多的照顾。\n',
            '所以我打算破格同意和你们交易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F这也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我可以从叔叔这里\n',
            '买东西啰？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '需要什么食材的话\n',
            '就和我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '只要支付适当的金额，\n',
            '不管什么食材都可以为你们准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5258',
    )

    ChrTalk(
        0x0104,
        (
            '#033F噢，这下厉害了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5330')

    def _loc_5258(): pass

    label('loc_5258')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_52A1',
    )

    ChrTalk(
        0x0108,
        (
            '#070F噢，这可厉害了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5330')

    def _loc_52A1(): pass

    label('loc_52A1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_52E6',
    )

    ChrTalk(
        0x0106,
        (
            '#052F这可真厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5330')

    def _loc_52E6(): pass

    label('loc_52E6')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5330',
    )

    ChrTalk(
        0x0103,
        (
            '#023F哎呀，这可真厉害啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5330(): pass

    label('loc_5330')

    ChrTalk(
        0x0011,
        (
            '是啊，只要是利贝尔王国内\n',
            '可见的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '各位游击士\n',
            '很多时候都需要自己做饭吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '请不必客气，\n',
            '尽管利用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，有需要的话一定来。\n',
            '那就先这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，差不多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '噢，对不起。\n',
            '耽误了各位这么长时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那么，我一直在这里经营。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是，告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x4000)
    OP_A2(0x000C)
    OP_28(0x007B, 0x01, 0x8000)
    EventEnd(0x00)
    OP_8C(0x0011, 0, 0)
    OP_4B(0x0011, 255)

    Return()

    def _loc_5466(): pass

    label('loc_5466')

    ChrTalk(
        0x0011,
        (
            '啊啊，\n',
            '或许的确是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但是，最后再加把劲这样的事\n',
            '我从来没有办到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '为表感谢，\n',
            '请收在下一份薄礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1020F难，难道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '又想送很多奇怪的蘑菇\n',
            '给我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嗯？想要蘑菇吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这样的话，\n',
            '这里还有很多库存……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1007F不，不，不用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F……抱歉。\n',
            '打断你说话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嗯，刚才说到谢礼是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '所谓谢礼并不是别的。\n',
            '那就是我奥维德商会的利用权。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F利用权？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嗯，我的店是做批发生意的……\n',
            '面向一般顾客的零售生意我是不做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但是你们曾经照顾过我。\n',
            '我打算破格给你们交易的权力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过交易的内容\n',
            '仅限于一般的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿，是这样啊。\n',
            '谢谢，真是帮了大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '毕竟现在情况很乱，普通的食材也\n',
            '不容易搞到嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F谢谢。\n',
            '帮了大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '需要什么食材的话\n',
            '就和我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '店面出售的食材\n',
            '都已经摆上货架了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)
    OP_28(0x007B, 0x01, 0x8000)
    EventEnd(0x00)
    OP_8C(0x0011, 0, 0)
    OP_4B(0x0011, 255)

    Return()

    def _loc_57A9(): pass

    label('loc_57A9')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_57E8',
    )

    ChrTalk(
        0x0011,
        (
            '喔，你们几个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '之前真的是劳烦你们了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5808')

    def _loc_57E8(): pass

    label('loc_57E8')

    ChrTalk(
        0x0011,
        (
            '哎呀？你们几个是游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5808(): pass

    label('loc_5808')

    ChrTalk(
        0x0011,
        (
            '现在物流机能停滞，\n',
            '想要保证食物充足是很困难的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '正是这种时期，\n',
            '才是我们奥维德商会出场的时候！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我商会会把从独有的渠道获得的山珍海味\n',
            '以适当的价格提供给大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '来，赶紧来\n',
            '看一看我们的商品吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x8000)
    OP_A2(0x000C)

    Jump('loc_6361')

    def _loc_58E6(): pass

    label('loc_58E6')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x8000)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6361',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -35260, 0, 42950, 90)
    SetChrPos(0x00F7, -35690, 0, 41950, 90)
    SetChrPos(0x00F8, -36550, 0, 43150, 90)
    SetChrPos(0x00F9, -36640, 0, 41730, 90)
    OP_8C(0x0011, 270, 0)
    OP_4A(0x0011, 255)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_596C',
    )

    SetChrPos(0x0004, -35970, 0, 44280, 135)

    def _loc_596C(): pass

    label('loc_596C')

    OP_6D(-35000, 0, 42570, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0011,
        (
            '真没想到能这么简单\n',
            '就可以谈下这个的商谈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '各位游击士。\n',
            '真的非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '和一流餐厅做买卖，\n',
            '是我多年来的梦想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '很快就会实现了……\n',
            '这全都是各位的功劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，之所以会有今天\n',
            '全都是叔叔自己努力的结果啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们只是稍微\n',
            '帮了点小忙而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B39',
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
            TXT(0x00, '【◇奥维德关联任务完全称霸】\n'),
            TXT(0x01, '【◇不变更】\n'),
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
        (0x00000000, 'loc_5B24'),
        (0x00000001, 'loc_5B36'),
        (-1, 'loc_5B39'),
    )

    def _loc_5B24(): pass

    label('loc_5B24')

    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0005, 0x04, 0x10)
    OP_28(0x001F, 0x04, 0x10)

    Jump('loc_5B39')

    def _loc_5B36(): pass

    label('loc_5B36')

    Jump('loc_5B39')

    def _loc_5B39(): pass

    label('loc_5B39')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_60A5',
    )

    ChrTalk(
        0x0011,
        (
            '嗯……\n',
            '和你们认识好像也已经很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '明明给你们添了很多麻烦，\n',
            '你们却能一直帮助我到现在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '作为对过去的答谢，\n',
            '请收下我这份谢礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1020F难，难道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '又想送很多奇怪的蘑菇\n',
            '给我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嗯？想要蘑菇吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这样的话，\n',
            '这里还有很多库存……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1007F不，不，不用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F……抱歉。\n',
            '打断你说话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嗯，刚才说到谢礼是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '所谓谢礼并不是别的。\n',
            '这是我奥维德商会的利用权。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊？利用权？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊，如你所知，\n',
            '我是专门做食材生意的商人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但我只和其他职业商人做买卖。\n',
            '面向一般顾客的零售生意我是不做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但是曾经受到你们太多的照顾。\n',
            '我打算破格给你们交易的权力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '能够在叔叔的店里\n',
            '买到东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '需要什么食材的话\n',
            '就和我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '只要支付适当的金额，\n',
            '不管什么食材都可以为你准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5ECA',
    )

    ChrTalk(
        0x0104,
        (
            '#033F嗯，这下厉害了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FA0')

    def _loc_5ECA(): pass

    label('loc_5ECA')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F13',
    )

    ChrTalk(
        0x0108,
        (
            '#070F噢，这可厉害了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FA0')

    def _loc_5F13(): pass

    label('loc_5F13')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F58',
    )

    ChrTalk(
        0x0106,
        (
            '#052F这可真厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FA0')

    def _loc_5F58(): pass

    label('loc_5F58')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5FA0',
    )

    ChrTalk(
        0x0103,
        (
            '#020F哎呀，这可真厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的什么种类的\n',
            '食材都有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FA0(): pass

    label('loc_5FA0')

    ChrTalk(
        0x0011,
        (
            '是啊，只要是利贝尔王国内\n',
            '可见的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '各位游击士\n',
            '很多时候都需要自己做饭吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '请不必客气，\n',
            '尽管利用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，有需要的话。\n',
            '那就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，差不多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '噢，对不起。\n',
            '耽误了各位这么长时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那么，我一直在这里经营。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)
    OP_28(0x007B, 0x01, 0x4000)

    Jump('loc_6351')

    def _loc_60A5(): pass

    label('loc_60A5')

    ChrTalk(
        0x0011,
        (
            '啊啊，\n',
            '或许的确是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就因为这一点\n',
            '我也要感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这就破例给你们\n',
            '我商会的利用权资格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊？利用权？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊，如你所知，\n',
            '我是个专门做食材生意的商人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但我只和其他职业商人做买卖。\n',
            '面向一般顾客的零售生意我是不做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但是你们曾经照顾过我。\n',
            '我打算破格给你们交易的权力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '能够在叔叔的店里\n',
            '买到东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '需要什么食材的话\n',
            '就和我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '本店的商品非常齐全，\n',
            '这可是其它商店所不能媲美的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F是吗，这可真方便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F嗯，有机会的话。\n',
            '我们一定光顾的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，差不多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '噢，对不起。\n',
            '耽误了各位这么长时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那么，各位游击士，\n',
            '你们也要继续努力做好自己的工作哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F再会，叔叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_6351(): pass

    label('loc_6351')

    OP_A2(0x000C)
    OP_28(0x007B, 0x01, 0x8000)
    EventEnd(0x00)
    OP_4B(0x0011, 255)

    Return()

    def _loc_6361(): pass

    label('loc_6361')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x4000)"),
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x8000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_642D',
    )

    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_641C',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63E7',
    )

    ChrTalk(
        0x0011,
        (
            '喔哟，要买点什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63E7(): pass

    label('loc_63E7')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_63F7',
    )

    OP_A9(0x38)

    Jump('loc_63F9')

    def _loc_63F7(): pass

    label('loc_63F7')

    OP_A9(0x37)

    def _loc_63F9(): pass

    label('loc_63F9')

    OP_A3(0x000C)

    ChrTalk(
        0x0011,
        (
            '那么，欢迎下次再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkEnd(0x0011)

    Return()

    def _loc_641C(): pass

    label('loc_641C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_642D',
    )

    TalkEnd(0x0011)

    Return()

    def _loc_642D(): pass

    label('loc_642D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_694A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_6542',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64E5',
    )

    ChrTalk(
        0x0011,
        (
            '我的食材在厨师长那里\n',
            '也有很高的评价。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '对于职业食品商来说，\n',
            '我们的产品优秀是理所当然的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过说真的，我还挺高兴的。\n',
            '毕竟吃了这么多苦嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_653F')

    def _loc_64E5(): pass

    label('loc_64E5')

    ChrTalk(
        0x0011,
        (
            '我的食材在厨师长那里\n',
            '也有很高的评价。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '对于职业食品商来说，\n',
            '自然是理所当然的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_653F(): pass

    label('loc_653F')

    Jump('loc_6947')

    def _loc_6542(): pass

    label('loc_6542')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6654',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65E7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6577',
    )

    ChrTalk(
        0x0011,
        (
            '噢，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6577(): pass

    label('loc_6577')

    ChrTalk(
        0x0011,
        (
            '外面虽然很乱，\n',
            '但我的生意却进行的非常顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '计划在大多数物流管道都停止之前，\n',
            '扩大我的销售渠道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_6651')

    def _loc_65E7(): pass

    label('loc_65E7')

    ChrTalk(
        0x0011,
        (
            '外面虽然很乱，\n',
            '但我的生意却进行的非常顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '计划在大多数物流管道都停止之前，\n',
            '扩大我的销售渠道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_6651(): pass

    label('loc_6651')

    Jump('loc_6947')

    def _loc_6654(): pass

    label('loc_6654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_6701',
    )

    ChrTalk(
        0x0011,
        (
            '定期船虽然好像恢复了，\n',
            '但对我的生意却一点影响也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为我们商会\n',
            '早准备好了各种极其珍贵的食材呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哼哼哼，\n',
            '这可是其它同行所模仿不来的食材阵容啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6947')

    def _loc_6701(): pass

    label('loc_6701')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_6812',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_677C',
    )

    ChrTalk(
        0x0011,
        (
            '我们奥维德商会有自己的经营特色，\n',
            '食材也都是自行收集的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不管定期船是否停航\n',
            '都丝毫不会受影响的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_680F')

    def _loc_677C(): pass

    label('loc_677C')

    ChrTalk(
        0x0011,
        (
            '我们奥维德商会有自己的经营特色，\n',
            '食材也都是自行收集的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不管定期船是否停航\n',
            '都丝毫不会受影响的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '嘿，这就是独立经营的最高境界啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_680F(): pass

    label('loc_680F')

    Jump('loc_6947')

    def _loc_6812(): pass

    label('loc_6812')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_686A',
    )

    ChrTalk(
        0x0011,
        (
            '因为定期船停航，\n',
            '进货变得非常困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哼哼，\n',
            '这么快就轮到我出场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6947')

    def _loc_686A(): pass

    label('loc_686A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_68DE',
    )

    ChrTalk(
        0x0011,
        (
            '嗯，由于那起事件，\n',
            '店里也变得非常混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '呼，商业洽谈也推迟了，\n',
            '毕竟是非常时期这也是无可奈何的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6947')

    def _loc_68DE(): pass

    label('loc_68DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_6947',
    )

    ChrTalk(
        0x0011,
        (
            '虽然计划只要料理长有空，\n',
            '就开始商业洽谈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '但料理长似乎非常忙。\n',
            '嗯嗯，不愧是一流的店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6947(): pass

    label('loc_6947')

    Jump('loc_699E')

    def _loc_694A(): pass

    label('loc_694A')

    ChrTalk(
        0x0011,
        (
            '不用客气。\n',
            '请尽情享受本店的服务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '虽然时间还早，\n',
            '请问要不要买点什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_699E(): pass

    label('loc_699E')

    TalkEnd(0x0011)

    Return()

# id: 0x0011 offset: 0x69A2
@scena.Code('func_11_69A2')
def func_11_69A2():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_69FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_69F3',
    )

    ChrTalk(
        0x00FE,
        (
            '这，这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请，请别这么说。\n',
            '我只不过是个平常女孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69F7')

    def _loc_69F3(): pass

    label('loc_69F3')

    Call(0, 0x0017)

    def _loc_69F7(): pass

    label('loc_69F7')

    Jump('loc_6ACA')

    def _loc_69FA(): pass

    label('loc_69FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_6A66',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_6A5F',
    )

    ChrTalk(
        0x00FE,
        (
            '你说的对，都市生活\n',
            '总觉得比较枯燥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在大自然中生活，\n',
            '也许很不错也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A63')

    def _loc_6A5F(): pass

    label('loc_6A5F')

    Call(0, 0x0017)

    def _loc_6A63(): pass

    label('loc_6A63')

    Jump('loc_6ACA')

    def _loc_6A66(): pass

    label('loc_6A66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_6ABF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_6AB8',
    )

    ChrTalk(
        0x0012,
        (
            '我好像……\n',
            '听到了什么可怕的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '到底出什么事了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6ABC')

    def _loc_6AB8(): pass

    label('loc_6AB8')

    Call(0, 0x0017)

    def _loc_6ABC(): pass

    label('loc_6ABC')

    Jump('loc_6ACA')

    def _loc_6ABF(): pass

    label('loc_6ABF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_6ACA',
    )

    Call(0, 0x0017)

    def _loc_6ACA(): pass

    label('loc_6ACA')

    TalkEnd(0x0012)

    Return()

# id: 0x0012 offset: 0x6ACE
@scena.Code('func_12_6ACE')
def func_12_6ACE():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_6BC1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 5, 0x1A55)),
            Expr.Return,
        ),
        'loc_6BBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_6B37',
    )

    ChrTalk(
        0x00FE,
        (
            '相亲之后\n',
            '回帝国的老家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '芙拉瑟小姐真是的，\n',
            '连休息的时间都没有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BB7')

    def _loc_6B37(): pass

    label('loc_6B37')

    ChrTalk(
        0x00FE,
        (
            '看来相亲\n',
            '总算完满结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，这结束之后\n',
            '很快就要回帝国的老家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '芙拉瑟小姐真是的，\n',
            '连休息的时间都没有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_6BB7(): pass

    label('loc_6BB7')

    Jump('loc_6BBE')

    def _loc_6BBA(): pass

    label('loc_6BBA')

    Call(0, 0x0013)
    def _loc_6BBE(): pass

    label('loc_6BBE')

    Jump('loc_709D')

    def _loc_6BC1(): pass

    label('loc_6BC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_6C9D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 5, 0x1A55)),
            Expr.Return,
        ),
        'loc_6C96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_6C28',
    )

    ChrTalk(
        0x00FE,
        (
            '由于时间开始空闲起来，\n',
            '小姐似乎也变得冷静些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，算是因祸得福吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C93')

    def _loc_6C28(): pass

    label('loc_6C28')

    ChrTalk(
        0x00FE,
        (
            '由于昨天的事，\n',
            '相亲被迫中断了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或者说……\n',
            '今天是个好的开端。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这可真值得期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_6C93(): pass

    label('loc_6C93')

    Jump('loc_6C9A')

    def _loc_6C96(): pass

    label('loc_6C96')

    Call(0, 0x0013)
    def _loc_6C9A(): pass

    label('loc_6C9A')

    Jump('loc_709D')

    def _loc_6C9D(): pass

    label('loc_6C9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_6CFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 5, 0x1A55)),
            Expr.Return,
        ),
        'loc_6CF8',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '好像出什么大事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，暂时\n',
            '先留在屋子里看看情况吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CFC')

    def _loc_6CF8(): pass

    label('loc_6CF8')

    Call(0, 0x0013)

    def _loc_6CFC(): pass

    label('loc_6CFC')

    Jump('loc_709D')

    def _loc_6CFF(): pass

    label('loc_6CFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_709D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_6D3E',
    )

    ChrTalk(
        0x00FE,
        (
            '相亲\n',
            '已经开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位请静一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_709D')

    def _loc_6D3E(): pass

    label('loc_6D3E')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_6E84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_6DB0',
    )

    ChrTalk(
        0x00FE,
        (
            '小姐的事，\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如遇到困难的话，\n',
            '请回忆一下传达给你的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E21')

    def _loc_6DB0(): pass

    label('loc_6DB0')

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐的事，\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如遇到困难的话，\n',
            '请回忆一下传达给你的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_6E21(): pass

    label('loc_6E21')

    Jump('loc_6E81')

    def _loc_6E24(): pass

    label('loc_6E24')

    ChrTurnDirection(0x00FE, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '告辞了各位。\n',
            '多谢关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如遇到困难的话，\n',
            '请回忆一下传达给你的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_8C(0x00FE, 90, 0)
    def _loc_6E81(): pass

    label('loc_6E81')

    Jump('loc_709D')

    def _loc_6E84(): pass

    label('loc_6E84')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_6EA7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_6EA0',
    )

    Call(1, 0x0008)

    Jump('loc_6EA4')

    def _loc_6EA0(): pass

    label('loc_6EA0')

    Call(1, 0x0007)

    def _loc_6EA4(): pass

    label('loc_6EA4')

    Jump('loc_709D')

    def _loc_6EA7(): pass

    label('loc_6EA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 4, 0x1A54)),
            Expr.Return,
        ),
        'loc_6F37',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_6EF3',
    )

    ChrTalk(
        0x00FE,
        (
            '能做的都已经做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '剩下的，\n',
            '就是和时间的战斗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F34')

    def _loc_6EF3(): pass

    label('loc_6EF3')

    ChrTalk(
        0x00FE,
        (
            '请你想办法\n',
            '再拖延点时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们已经\n',
            '安排人去办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_6F34(): pass

    label('loc_6F34')

    Jump('loc_709D')

    def _loc_6F37(): pass

    label('loc_6F37')

    ChrTalk(
        0x00FE,
        (
            '请您想办法\n',
            '再拖延点时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们已经\n',
            '安排人去办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F（啊，这个人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#050F（……难道你认识吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_704C',
    )

    ChrTalk(
        0x0101,
        (
            '#1002F（嗯，嗯……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F（王立学院的蕾娜。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（为什么……\n',
            '  她会出现在这种地方呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_709A')

    def _loc_704C(): pass

    label('loc_704C')

    ChrTalk(
        0x0101,
        (
            '#1015F（嗯……\n',
            '王立学院的学生。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（究竟她……\n',
            '  在这种地方做什么呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_709A(): pass

    label('loc_709A')

    OP_A2(0x1A54)

    def _loc_709D(): pass

    label('loc_709D')

    TalkEnd(0x0013)

    Return()

# id: 0x0013 offset: 0x70A1
@scena.Code('func_13_70A1')
def func_13_70A1():
    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，你是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_719C',
    )

    ChrTalk(
        0x0101,
        (
            '#1004F咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1011F你好像叫蕾娜……是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，调查学院时\n',
            '我们见过面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '蕾娜，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，连科洛丝都来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F那个，为什么\n',
            '会在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7245')

    def _loc_719C(): pass

    label('loc_719C')

    ChrTalk(
        0x0101,
        (
            '#1004F咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1011F你好像叫蕾娜……是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F姐姐的朋友？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，学院调查的时候，\n',
            '曾经向她打听过一些事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1002F……那个，为什么\n',
            '会在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7245(): pass

    label('loc_7245')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是。\n',
            '我是来照顾芙拉瑟小姐的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，\n',
            '今天是十分重要的相亲日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '芙拉瑟……\n',
            '要去相亲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是的。\n',
            '虽然经过一番的周折……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但得到了许多人的协助，\n',
            '总算取得了成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_7429',
    )

    ChrTalk(
        0x0101,
        (
            '#1016F可是，相亲什么的\n',
            '是不是太、太早了点？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '她现在还只是个学生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说身为学生，\n',
            '但小姐也已年满１６……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为帝国上层贵族千金，\n',
            '连一门亲事也没有是种耻辱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F原来是这么回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯，这对我来说\n',
            '非常难以理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74F2')

    def _loc_7429(): pass

    label('loc_7429')

    ChrTalk(
        0x00FE,
        (
            '……对了，外面好象发生了骚乱，\n',
            '究竟出什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我想虽然已经不危险了，\n',
            '但还是不要出去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来如此，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯……\n',
            '蕾娜你们也多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_74F2(): pass

    label('loc_74F2')

    OP_A2(0x1A55)

    Return()

# id: 0x0014 offset: 0x74F6
@scena.Code('func_14_74F6')
def func_14_74F6():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_75BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_7558',
    )

    ChrTalk(
        0x00FE,
        (
            '看起来……\n',
            '小姐也挺在意对方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这之后请务必用\n',
            '书信的形式加深交往。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75B7')

    def _loc_7558(): pass

    label('loc_7558')

    ChrTalk(
        0x00FE,
        (
            '嗯，看来这场相亲\n',
            '总算完满结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对拉近两家的关系而言，\n',
            '这次的相亲的确很有意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_75B7(): pass

    label('loc_75B7')

    Jump('loc_7888')

    def _loc_75BA(): pass

    label('loc_75BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_7643',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_7606',
    )

    ChrTalk(
        0x00FE,
        (
            '看来小姐对\n',
            '对方有意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐，看起来就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7640')

    def _loc_7606(): pass

    label('loc_7606')

    ChrTalk(
        0x00FE,
        (
            '看来小姐对\n',
            '对方有意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这真是令人高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_7640(): pass

    label('loc_7640')

    Jump('loc_7888')

    def _loc_7643(): pass

    label('loc_7643')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_768E',
    )

    ChrTalk(
        0x00FE,
        (
            '宛如打雷般\n',
            '响亮的声音啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，外面到底发生什么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7888')

    def _loc_768E(): pass

    label('loc_768E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_7888',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_77C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_7715',
    )

    ChrTalk(
        0x00FE,
        (
            '明明非常讨厌相亲，\n',
            '但现在又……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一旦开始行动，\n',
            '处事就变得如此伶俐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不，真不愧是小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77C1')

    def _loc_7715(): pass

    label('loc_7715')

    ChrTalk(
        0x00FE,
        (
            '竟然将相亲进行得如此顺利，\n',
            '但现在又……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一旦开始行动，\n',
            '处事就变得如此伶俐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的灵机应变，\n',
            '正是在社交界生存必要的能力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呀，真不愧是小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_77C1(): pass

    label('loc_77C1')

    Jump('loc_7888')

    def _loc_77C4(): pass

    label('loc_77C4')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_7815',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '小姐她现在正在补妆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很快就会出来，\n',
            '请各位稍等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7888')

    def _loc_7815(): pass

    label('loc_7815')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_7838',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_7831',
    )

    Call(1, 0x0008)

    Jump('loc_7835')

    def _loc_7831(): pass

    label('loc_7831')

    Call(1, 0x0007)

    def _loc_7835(): pass

    label('loc_7835')

    Jump('loc_7888')

    def _loc_7838(): pass

    label('loc_7838')

    ChrTalk(
        0x00FE,
        (
            '告诉对方小姐正忙着补妆，\n',
            '尽可能拖延时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，那件事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7888(): pass

    label('loc_7888')

    TalkEnd(0x0014)

    Return()

# id: 0x0015 offset: 0x788C
@scena.Code('func_15_788C')
def func_15_788C():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_78F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_78EC',
    )

    ChrTalk(
        0x00FE,
        (
            '哪里，这样的评价\n',
            '我觉得并不为过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和她相比，\n',
            '我才更是不成熟呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_78F0')

    def _loc_78EC(): pass

    label('loc_78EC')

    Call(0, 0x0017)

    def _loc_78F0(): pass

    label('loc_78F0')

    Jump('loc_7ADF')

    def _loc_78F3(): pass

    label('loc_78F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_796D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_7966',
    )

    ChrTalk(
        0x00FE,
        (
            '繁忙的帝都生活\n',
            '似乎不太适合我的性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与其在人群中生活，\n',
            '倒不如与自然为伴更为轻松自在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_796A')

    def _loc_7966(): pass

    label('loc_7966')

    Call(0, 0x0017)

    def _loc_796A(): pass

    label('loc_796A')

    Jump('loc_7ADF')

    def _loc_796D(): pass

    label('loc_796D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_79D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_79D2',
    )

    ChrTalk(
        0x00FE,
        (
            '危机虽然已经过去了，\n',
            '但此事绝非寻常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '今天这场相亲\n',
            '说不定必须早点结束呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_79D6')

    def _loc_79D2(): pass

    label('loc_79D2')

    Call(0, 0x0017)

    def _loc_79D6(): pass

    label('loc_79D6')

    Jump('loc_7ADF')

    def _loc_79D9(): pass

    label('loc_79D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_7ADF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_79F1',
    )

    Call(0, 0x0017)

    Jump('loc_7ADF')

    def _loc_79F1(): pass

    label('loc_79F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_7A55',
    )

    ChrTalk(
        0x00FE,
        (
            '该不会看到我穿着平时的衣服\n',
            '对方觉得不高兴吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯嗯。\n',
            '果然还是应该穿礼服出席。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7ADF')

    def _loc_7A55(): pass

    label('loc_7A55')

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '对象迟迟不出现啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该不会看到我穿着平时的衣服\n',
            '对方觉得不高兴吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是对方提出的，\n',
            '但是在这种场合的确不适宜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    def _loc_7ADF(): pass

    label('loc_7ADF')

    TalkEnd(0x0015)

    Return()

# id: 0x0016 offset: 0x7AE3
@scena.Code('func_16_7AE3')
def func_16_7AE3():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_7C0D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_7B53',
    )

    ChrTalk(
        0x00FE,
        (
            '这次的相亲，\n',
            '看来是成功了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了加深两家的关系，\n',
            '以后也希望你们能够持续保持友谊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C0A')

    def _loc_7B53(): pass

    label('loc_7B53')

    ChrTalk(
        0x00FE,
        (
            '起初，我还是非常担心\n',
            '事情会发展成什么样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的相亲，\n',
            '看来是成功了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了加深两家的关系，\n',
            '以后也希望你们能够持续保持友谊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是否成婚\n',
            '取决于他们个人的意愿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_7C0A(): pass

    label('loc_7C0A')

    Jump('loc_7EEE')

    def _loc_7C0D(): pass

    label('loc_7C0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_7C67',
    )

    ChrTalk(
        0x00FE,
        (
            '少主人实在\n',
            '太没有野心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明有着能在中央政治界大显身手\n',
            '的家庭背景。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7EEE')

    def _loc_7C67(): pass

    label('loc_7C67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_7D29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_7CBA',
    )

    ChrTalk(
        0x00FE,
        (
            '这边的店铺\n',
            '好像没有大碍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '少主人，\n',
            '请在座位上稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D26')

    def _loc_7CBA(): pass

    label('loc_7CBA')

    ChrTalk(
        0x00FE,
        (
            '少主人，这边的店铺\n',
            '好像没有大碍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请坐在座位上，\n',
            '稍等片刻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等查明事情原因\n',
            '再向您汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_7D26(): pass

    label('loc_7D26')

    Jump('loc_7EEE')

    def _loc_7D29(): pass

    label('loc_7D29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_7EEE',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_7E25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_7D92',
    )

    ChrTalk(
        0x00FE,
        (
            '看来才女的称呼，\n',
            '并非是浪得虚名啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种高雅的气质，\n',
            '不愧出身名门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E22')

    def _loc_7D92(): pass

    label('loc_7D92')

    ChrTalk(
        0x00FE,
        (
            '对面那位小姐正在王国留学，\n',
            '据说不是一般人可以高攀的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，果然这称呼\n',
            '并非是浪得虚名啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种高雅的气质，\n',
            '不愧是出身名门啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_7E22(): pass

    label('loc_7E22')

    Jump('loc_7EEE')

    def _loc_7E25(): pass

    label('loc_7E25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_7E93',
    )

    ChrTalk(
        0x00FE,
        (
            '少主人好像过于温和了。\n',
            '希望日后不要惧内就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的有点担心\n',
            '他日后会不会太过依从妻子啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7EEE')

    def _loc_7E93(): pass

    label('loc_7E93')

    ChrTalk(
        0x00FE,
        (
            '少主人，这次的事\n',
            '失败的并不是我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『请穿平时的服装』这要求\n',
            '是对方提出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_7EEE(): pass

    label('loc_7EEE')

    TalkEnd(0x0016)

    Return()

# id: 0x0017 offset: 0x7EF2
@scena.Code('func_17_7EF2')
def func_17_7EF2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_8059',
    )

    ChrTalk(
        0x0015,
        (
            '原来如此，那么这之后\n',
            '是不是要回帝国的老家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '是的，正是这样计划的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '学校的假期\n',
            '还剩下一点时间，\n',
            '所以准备去看看父亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '嗯，你果然\n',
            '是我所期待的女性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '一方面有着进步的思想，\n',
            '一方面又保留着古典的道义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '太感谢您了，女神大人。\n',
            '感谢你把这么优秀的女孩子介绍给我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '怎，怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '请，请别这么说。\n',
            '我只不过是个平常女孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8466')

    def _loc_8059(): pass

    label('loc_8059')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_81D7',
    )

    ChrTalk(
        0x0012,
        (
            '那个，抱歉\n',
            '请问你从事什么样的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '平时管理从祖父那里继承下来的\n',
            '农地和山林。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '农闲的时候\n',
            '看看书，打打猎，\n',
            '可以说是自由自在的农村生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '繁忙的帝都生活\n',
            '好像不太符合我的性格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '乡村生活吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '是的，听起来是很无聊，\n',
            '习惯了的话还是很不错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '与其在人群中生活，\n',
            '不如于自然为伴的话反而更轻松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '呵呵，原来如此。\n',
            '或许真的是这样也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8466')

    def _loc_81D7(): pass

    label('loc_81D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_82AD',
    )

    OP_4A(0x0012, 255)
    OP_4A(0x0015, 255)

    ChrTalk(
        0x0012,
        (
            '我好像……\n',
            '听到了什么可怕的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '到底出什么事了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '看来不会很快有危险。\n',
            '就在这里看看情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '但是，总觉得\n',
            '此事非同寻常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '今天的相亲\n',
            '可能必须提早结束也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0012, 255)
    OP_4B(0x0015, 255)

    Jump('loc_8466')

    def _loc_82AD(): pass

    label('loc_82AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_8466',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_8346',
    )

    ChrTalk(
        0x0015,
        (
            '总之先为我们两人的相遇',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '以及彼此两家族的光荣未来，\n',
            '以及两家的将来干杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '嗯，荣幸之至。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '不过，请允许我\n',
            '用饮料代替酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8466')

    def _loc_8346(): pass

    label('loc_8346')

    ChrTalk(
        0x0012,
        (
            '初次见面，\n',
            '我叫芙拉瑟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '让您久等了，\n',
            '真的非常抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '因为学院布置了课题，\n',
            '所以需要到社会上去实习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '啊……\n',
            '我从心底希望和你见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '但却一直等不到你来，\n',
            '心理很着急……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '不过，无论如何，\n',
            '你不是正在我面前了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我也是帝国出身的男子，\n',
            '不会太在意这些小细节。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0014)

    def _loc_8466(): pass

    label('loc_8466')

    OP_A2(0x0012)
    OP_A2(0x0010)

    Return()

# id: 0x0018 offset: 0x846D
@scena.Code('func_18_846D')
def func_18_846D():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_84DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_84D5',
    )

    ChrTalk(
        0x00FE,
        (
            '果然重要的是\n',
            '和客人间的信赖关系吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仔细想想的话，\n',
            '买卖也是人际关系啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84D9')

    def _loc_84D5(): pass

    label('loc_84D5')

    Call(0, 0x0019)

    def _loc_84D9(): pass

    label('loc_84D9')

    Jump('loc_86F0')

    def _loc_84DC(): pass

    label('loc_84DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_860B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_8551',
    )

    ChrTalk(
        0x00FE,
        (
            '今天也是来向以前当商人的叔叔\n',
            '请教一些事情的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这家店铺的门槛很高，\n',
            '总也不好意思进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8608')

    def _loc_8551(): pass

    label('loc_8551')

    ChrTalk(
        0x00FE,
        (
            '昨天在这里避难时，\n',
            '遇见过一位亲切的叔叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人原本也是商人，\n',
            '向我提了很多意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他让我今天再来，\n',
            '所以我就过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这家店铺的门槛很高，\n',
            '总也不好意思进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    def _loc_8608(): pass

    label('loc_8608')

    Jump('loc_86F0')

    def _loc_860B(): pass

    label('loc_860B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_86F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_8675',
    )

    ChrTalk(
        0x00FE,
        (
            '好不容易营业许可终于下来了，\n',
            '但正在准备开门营业的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是一大打击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86F0')

    def _loc_8675(): pass

    label('loc_8675')

    ChrTalk(
        0x00FE,
        (
            '好不容易营业许可终于下来了，\n',
            '但正在准备开门营业的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……超市居然\n',
            '会出这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是一大打击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    def _loc_86F0(): pass

    label('loc_86F0')

    TalkEnd(0x0017)

    Return()

# id: 0x0019 offset: 0x86F4
@scena.Code('func_19_86F4')
def func_19_86F4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_87F9',
    )

    ChrTalk(
        0x0017,
        (
            '那个，想要吸引顾客，\n',
            '最重要的是什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '进行广告宣传的话\n',
            '效果或许不错……\n',
            '但是所花费的米拉也不少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '客人们留意的是\n',
            '门前客人多的商店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '满足每一位顾客的需要，\n',
            '让他们不断回头消费……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这是做买卖的基本。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '原，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)
    OP_A2(0x0006)

    Jump('loc_891A')

    def _loc_87F9(): pass

    label('loc_87F9')

    ChrTalk(
        0x000D,
        (
            '那么，\n',
            '你是想在超市里开店是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '是的，就在离南面出口不远处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '虽然现在摊位还空着，\n',
            '但我觉得还是个不错的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这倒是不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '离入口近的商店\n',
            '要在让客人驻足上下功夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '刚进超市的客人，脚步是很快的。\n',
            '什么也不做的话客人们只会从店铺旁走过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '原，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0016)

    def _loc_891A(): pass

    label('loc_891A')

    Return()

# id: 0x001A offset: 0x891B
@scena.Code('func_1A_891B')
def func_1A_891B():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_8A6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_899D',
    )

    ChrTalk(
        0x00FE,
        (
            '购物讲究的是气氛。\n',
            '假的店铺是无法满足客人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买东西不是客人们的目的，\n',
            '购物中的乐趣才是顾客想要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A6C')

    def _loc_899D(): pass

    label('loc_899D')

    ChrTalk(
        0x00FE,
        (
            '超市的商人\n',
            '虽然好像在酒店里营业……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '购物讲究的是气氛。\n',
            '假的店铺是无法满足客人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '高高的天花板加上有感觉的展示，\n',
            '以及平易近人的店员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些结合在一起，\n',
            '顾客就会从中体验到购物的乐趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0017)

    def _loc_8A6C(): pass

    label('loc_8A6C')

    Jump('loc_8C99')

    def _loc_8A6F(): pass

    label('loc_8A6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_8B6B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_8AE2',
    )

    ChrTalk(
        0x00FE,
        (
            '直到超市恢复以前\n',
            '就在这里享受饭菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然那样好吃的东西啊。\n',
            '吃好吃的东西可真放松心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B68')

    def _loc_8AE2(): pass

    label('loc_8AE2')

    ChrTalk(
        0x00FE,
        (
            '超市的恢复\n',
            '看来还要些时日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之前别无选择\n',
            '就在这里享受饭菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然那样好吃的东西啊。\n',
            '吃好吃的东西可真放松心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0017)

    def _loc_8B68(): pass

    label('loc_8B68')

    Jump('loc_8C99')

    def _loc_8B6B(): pass

    label('loc_8B6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_8C99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_8C05',
    )

    ChrTalk(
        0x00FE,
        (
            '看到那个巨大的怪物，\n',
            '一直逃到了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是仔细一看，\n',
            '这里不是安特洛丝吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，不愧是我啊。\n',
            '身体会自然向着一流的方面前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C99')

    def _loc_8C05(): pass

    label('loc_8C05')

    ChrTalk(
        0x00FE,
        (
            '正在想怎么突然刮起了大风，\n',
            '突然周围就一下变得漆黑一片，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '紧接着超市上\n',
            '就有个巨大的怪物站在那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我来不及思考，\n',
            '就一直逃到了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0017)

    def _loc_8C99(): pass

    label('loc_8C99')

    TalkEnd(0x0018)

    Return()

# id: 0x001B offset: 0x8C9D
@scena.Code('func_1B_8C9D')
def func_1B_8C9D():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_8DC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Return,
        ),
        'loc_8D0F',
    )

    ChrTalk(
        0x00FE,
        (
            '的确……\n',
            '感觉和上次来时不太一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天觉得不可思议啊……\n',
            '居然能挺起胸膛地坐在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DBF')

    def _loc_8D0F(): pass

    label('loc_8D0F')

    ChrTalk(
        0x00FE,
        (
            '作为参加超市修复工程的答谢\n',
            '市长亲自招待了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许是由于这个原因，这次的感觉\n',
            '和上次来的时候有些不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我自己也感到有些不可思议，\n',
            '居然能挺起胸膛地坐在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)

    def _loc_8DBF(): pass

    label('loc_8DBF')

    Jump('loc_8DC9')

    def _loc_8DC2(): pass

    label('loc_8DC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_8DC9',
    )

    def _loc_8DC9(): pass

    label('loc_8DC9')

    TalkEnd(0x0019)

    Return()

# id: 0x001C offset: 0x8DCD
@scena.Code('func_1C_8DCD')
def func_1C_8DCD():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_8EA6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_8E2F',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，这里的料理\n',
            '果然是最棒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想到是市长款待的，\n',
            '就更觉得美味了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EA3')

    def _loc_8E2F(): pass

    label('loc_8E2F')

    ChrTalk(
        0x00FE,
        (
            '这里的料理\n',
            '果然最棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想到是市长款待的，\n',
            '就更觉得美味了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，呵呵……\n',
            '为工程尽力果然是对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0019)

    def _loc_8EA3(): pass

    label('loc_8EA3')

    Jump('loc_8EAD')

    def _loc_8EA6(): pass

    label('loc_8EA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_8EAD',
    )

    def _loc_8EAD(): pass

    label('loc_8EAD')

    TalkEnd(0x001A)

    Return()

# id: 0x001D offset: 0x8EB1
@scena.Code('func_1D_8EB1')
def func_1D_8EB1():
    Call(0, 0x001E)

    Return()

# id: 0x001E offset: 0x8EB6
@scena.Code('func_1E_8EB6')
def func_1E_8EB6():
    TalkBegin(0x001B)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '招牌菜『黄金调味饭』　1400米拉\n'),
            TXT(0x03, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F33',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x34)
    OP_56(0x00)
    TalkEnd(0x001B)

    Return()

    def _loc_8F33(): pass

    label('loc_8F33')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_906A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x578),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_9035',
    )

    SubMira(1400)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x000B, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '黄金调味饭',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFC, 0)
    SetChrStatus(ChrTable['约修亚'], 0xFC, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFC, 0)
    SetChrStatus(ChrTable['奥利维尔'], 0xFC, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFC, 0)
    SetChrStatus(ChrTable['阿加特'], 0xFC, 0)
    SetChrStatus(ChrTable['提妲'], 0xFC, 0)
    SetChrStatus(ChrTable['金'], 0xFC, 0)
    SetChrStatus(ChrTable['凯文神父'], 0xFC, 0)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFD, 3500)
    SetChrStatus(ChrTable['约修亚'], 0xFD, 3500)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFD, 3500)
    SetChrStatus(ChrTable['奥利维尔'], 0xFD, 3500)
    SetChrStatus(ChrTable['科洛丝'], 0xFD, 3500)
    SetChrStatus(ChrTable['阿加特'], 0xFD, 3500)
    SetChrStatus(ChrTable['提妲'], 0xFD, 3500)
    SetChrStatus(ChrTable['金'], 0xFD, 3500)
    SetChrStatus(ChrTable['凯文神父'], 0xFD, 3500)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9027',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0005)"),
            Expr.Return,
        ),
        'loc_8FFD',
    )

    Jump('loc_9027')

    def _loc_8FFD(): pass

    label('loc_8FFD')

    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '黄金调味饭',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9027(): pass

    label('loc_9027')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_905B')

    def _loc_9035(): pass

    label('loc_9035')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_905B(): pass

    label('loc_905B')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x001B)

    Return()

    def _loc_906A(): pass

    label('loc_906A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9084',
    )

    FadeIn(300, 0)
    TalkEnd(0x001B)

    Return()

    def _loc_9084(): pass

    label('loc_9084')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_9182',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9123',
    )

    ChrTalk(
        0x001B,
        (
            '虽然工房的人也说修了，\n',
            '可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '总之，\n',
            '只要炉子能用就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '假如没有导力器那强劲的火候\n',
            '我们店的味道是出不来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001A)

    Jump('loc_917F')

    def _loc_9123(): pass

    label('loc_9123')

    ChrTalk(
        0x001B,
        (
            '总之，\n',
            '只要炉子能用就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '假如没有导力器那强劲的火候\n',
            '我们店的味道是出不来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_917F(): pass

    label('loc_917F')

    Jump('loc_96C2')

    def _loc_9182(): pass

    label('loc_9182')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_9243',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_91F7',
    )

    ChrTalk(
        0x001B,
        (
            '虽然用不了导力器很为难，\n',
            '但因此引发骚乱就不好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '同身为柏斯市民的我们\n',
            '都感觉丢脸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001A)

    Jump('loc_9240')

    def _loc_91F7(): pass

    label('loc_91F7')

    ChrTalk(
        0x001B,
        (
            '动摇的心情我能理解，\n',
            '但爆发骚乱可就不好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '都感觉太丢脸了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9240(): pass

    label('loc_9240')

    Jump('loc_96C2')

    def _loc_9243(): pass

    label('loc_9243')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_9290',
    )

    ChrTalk(
        0x001B,
        (
            '呀——\n',
            '超市能够顺利修复可真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '是啊，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96C2')

    def _loc_9290(): pass

    label('loc_9290')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_93CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Return,
        ),
        'loc_932B',
    )

    ChrTalk(
        0x001B,
        (
            '自从那家蛋糕店开门以来\n',
            '我们的销量就一直下滑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '话虽如此，事到如今\n',
            '想让他们走又是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '……米拉和人情真是两难的取舍啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_93C8')

    def _loc_932B(): pass

    label('loc_932B')

    ChrTalk(
        0x001B,
        (
            '嗯，嗯，糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '自从那家蛋糕店开门以来\n',
            '销量越来越低。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '话虽如此，事到如今\n',
            '想让他们走又是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '生，生意真是到了最困窘的境地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001A)

    def _loc_93C8(): pass

    label('loc_93C8')

    Jump('loc_96C2')

    def _loc_93CB(): pass

    label('loc_93CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_94AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Return,
        ),
        'loc_942A',
    )

    ChrTalk(
        0x001B,
        (
            '那家蛋糕店\n',
            '人气实在是太旺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '因此我们这里的料理\n',
            '几乎没有人来点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94A8')

    def _loc_942A(): pass

    label('loc_942A')

    ChrTalk(
        0x001B,
        (
            '不～～～那家蛋糕店\n',
            '人气实在是太旺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '因此我们这里的料理\n',
            '完全没有人来点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '哈，哈哈……\n',
            '这也算是帮助人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001A)

    def _loc_94A8(): pass

    label('loc_94A8')

    Jump('loc_96C2')

    def _loc_94AB(): pass

    label('loc_94AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_960F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Return,
        ),
        'loc_9555',
    )

    ChrTalk(
        0x001B,
        (
            '我们这里也有冰淇淋和蛋糕铺子\n',
            '的人前来避难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '生意好像还要继续，\n',
            '不嫌弃的话买一点回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '买卖是很复杂的，\n',
            '遇到困难的时候大家都是差不多的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_960C')

    def _loc_9555(): pass

    label('loc_9555')

    ChrTalk(
        0x001B,
        (
            '毕竟发生的是\n',
            '超市倒塌这样的大事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '我们也想帮忙，\n',
            '于是就报名承当起了避难所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '因此，开冰淇淋和蛋糕铺子\n',
            '的人就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '生意好像还要继续，\n',
            '不嫌弃的话买一点回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001A)

    def _loc_960C(): pass

    label('loc_960C')

    Jump('loc_96C2')

    def _loc_960F(): pass

    label('loc_960F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_96C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Return,
        ),
        'loc_9653',
    )

    ChrTalk(
        0x001B,
        (
            '我店可是面向工薪阶层的平价店。\n',
            '请慢慢享用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96C2')

    def _loc_9653(): pass

    label('loc_9653')

    ChrTalk(
        0x001B,
        (
            '欢迎光临。\n',
            '我店可是面向工薪阶层的平价店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '和安特洛丝不同，\n',
            '为顾客提供像家一样的气氛是我们的卖点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001A)

    def _loc_96C2(): pass

    label('loc_96C2')

    TalkEnd(0x001B)

    Return()

# id: 0x001F offset: 0x96C6
@scena.Code('func_1F_96C6')
def func_1F_96C6():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_976F',
    )

    ChrTalk(
        0x00FE,
        (
            '我们老板\n',
            '只会使用导力炉做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，最近使用的是直接在火上烹调的方法，\n',
            '因此不管什么料理闻起来都有股焦味儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这已经不是料理好不好吃的问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D5B')

    def _loc_976F(): pass

    label('loc_976F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_9880',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9817',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然听老板的口气，\n',
            '好像对骚乱满不在乎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是老板自己\n',
            '还不是冲进市长官邸去抗议了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把自己的事当作没发生过，\n',
            '有什么好装模作样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001B)

    Jump('loc_987D')

    def _loc_9817(): pass

    label('loc_9817')

    ChrTalk(
        0x00FE,
        (
            '老板嘴上虽这么说，\n',
            '自己还不是冲进市长官邸去抗议了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样……\n',
            '所说的跟所做的不是截然相反吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_987D(): pass

    label('loc_987D')

    Jump('loc_9D5B')

    def _loc_9880(): pass

    label('loc_9880')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_99A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Return,
        ),
        'loc_9909',
    )

    ChrTalk(
        0x00FE,
        (
            '本店正处在危机当中啊。\n',
            '客人都被前来避难的那个蛋糕店老板抢走了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是超市再不开门话，\n',
            '我想肯定会被吞并的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A4')

    def _loc_9909(): pass

    label('loc_9909')

    ChrTalk(
        0x00FE,
        (
            '呵呵，超市能够顺利恢复\n',
            '真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是超市再不开门话，\n',
            '我们肯定被蛋糕店老板\n',
            '完全吞并了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，被并掉生意反而会更好些，\n',
            '好像也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001B)

    def _loc_99A4(): pass

    label('loc_99A4')

    Jump('loc_9D5B')

    def _loc_99A7(): pass

    label('loc_99A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_9AC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Return,
        ),
        'loc_9A12',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，我们这儿\n',
            '几乎快成『蛋糕酒馆』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都是来吃蛋糕的，\n',
            '再也没有人点菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AC2')

    def _loc_9A12(): pass

    label('loc_9A12')

    ChrTalk(
        0x00FE,
        (
            '最近，我们这儿\n',
            '几乎快成『蛋糕酒馆』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都是来吃蛋糕的，\n',
            '再也没有人点菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这样的结果是必然的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这儿的料理，\n',
            '只有价格便宜是唯一的长处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001B)

    def _loc_9AC2(): pass

    label('loc_9AC2')

    Jump('loc_9D5B')

    def _loc_9AC5(): pass

    label('loc_9AC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_9C31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Return,
        ),
        'loc_9B29',
    )

    ChrTalk(
        0x00FE,
        (
            '来我们这里避难的蛋糕店老板。\n',
            '跟我想的一样非常受欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客人都被抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C2E')

    def _loc_9B29(): pass

    label('loc_9B29')

    ChrTalk(
        0x00FE,
        (
            '来我们这里避难的蛋糕店老板。\n',
            '跟我想的一样非常受欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工地上班的工人，\n',
            '休息的时候也会来买的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店长最初的时候还洋洋得意，\n',
            '但最近可没那么自在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来就不是很有人气的店铺、又想装门面，\n',
            '就是这样的结果啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……总之这就是叫自做自受吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001B)

    def _loc_9C2E(): pass

    label('loc_9C2E')

    Jump('loc_9D5B')

    def _loc_9C31(): pass

    label('loc_9C31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_9D35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Return,
        ),
        'loc_9CA2',
    )

    ChrTalk(
        0x00FE,
        (
            '让人家在店铺里营业，\n',
            '是不是太大方了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老板的料理和人家一比，\n',
            '我想会马上就败下阵来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D32')

    def _loc_9CA2(): pass

    label('loc_9CA2')

    ChrTalk(
        0x00FE,
        (
            '虽然收留前来超市避难的人\n',
            '是理所当然的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但让人家在店铺里营业，\n',
            '是不是太大方了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道打算让原本就低迷的销售额\n',
            '下降到零吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001B)

    def _loc_9D32(): pass

    label('loc_9D32')

    Jump('loc_9D5B')

    def _loc_9D35(): pass

    label('loc_9D35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_9D5B',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！\n',
            '请空位上就坐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9D5B(): pass

    label('loc_9D5B')

    TalkEnd(0x001C)

    Return()

# id: 0x0020 offset: 0x9D5F
@scena.Code('func_20_9D5F')
def func_20_9D5F():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_9E1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 4, 0x1C)),
            Expr.Return,
        ),
        'loc_9DB7',
    )

    ChrTalk(
        0x00FE,
        (
            '我在找的东西\n',
            '肯定在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要将研究完成，\n',
            '得到荣誉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E1A')

    def _loc_9DB7(): pass

    label('loc_9DB7')

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '我是古代生物的研究者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在找的东西\n',
            '肯定在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼哼，好好期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001C)

    def _loc_9E1A(): pass

    label('loc_9E1A')

    TalkEnd(0x001D)

    Return()

# id: 0x0021 offset: 0x9E1E
@scena.Code('func_21_9E1E')
def func_21_9E1E():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_9F3C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 5, 0x1D)),
            Expr.Return,
        ),
        'loc_9E88',
    )

    ChrTalk(
        0x00FE,
        (
            '和喜欢的人一起工作，\n',
            '果然是件快乐的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在，\n',
            '真想稍微享受一下这种感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F39')

    def _loc_9E88(): pass

    label('loc_9E88')

    ChrTalk(
        0x00FE,
        (
            '在这之前，\n',
            '和他在不同的店铺里工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和喜欢的人一起工作，\n',
            '果然是件开心的事⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想稍微体验一下\n',
            '这种感觉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果超市恢复的话，\n',
            '我们就又是竞争对手了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001D)

    def _loc_9F39(): pass

    label('loc_9F39')

    Jump('loc_A06C')

    def _loc_9F3C(): pass

    label('loc_9F3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_A013',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 5, 0x1D)),
            Expr.Return,
        ),
        'loc_9FA3',
    )

    ChrTalk(
        0x00FE,
        (
            '经过了一个晚上，\n',
            '终于冷静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只有和他同心协力，\n',
            '一起努力往前走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A010')

    def _loc_9FA3(): pass

    label('loc_9FA3')

    ChrTalk(
        0x00FE,
        (
            '啊，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经过了一个晚上，\n',
            '终于冷静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只有和他同心协力，\n',
            '一起努力往前走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001D)

    def _loc_A010(): pass

    label('loc_A010')

    Jump('loc_A06C')

    def _loc_A013(): pass

    label('loc_A013')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_A06C',
    )

    ChrTalk(
        0x00FE,
        (
            '好象掉了一大堆瓦片什么的\n',
            '在我的货车后面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '在那边的人没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A06C(): pass

    label('loc_A06C')

    TalkEnd(0x001E)

    Return()

# id: 0x0022 offset: 0xA070
@scena.Code('func_22_A070')
def func_22_A070():
    TalkBegin(0x001F)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A0CE',
    )

    OP_0D()
    OP_A9(0x51)
    OP_56(0x00)
    TalkEnd(0x001F)

    Return()

    def _loc_A0CE(): pass

    label('loc_A0CE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A0DF',
    )

    TalkEnd(0x001F)

    Return()

    def _loc_A0DF(): pass

    label('loc_A0DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_A1F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 6, 0x1E)),
            Expr.Return,
        ),
        'loc_A14A',
    )

    ChrTalk(
        0x00FE,
        (
            '两人合作的话\n',
            '似乎能开发出不错的商品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市假如恢复的话\n',
            '要试试开发新的商品吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1F3')

    def _loc_A14A(): pass

    label('loc_A14A')

    ChrTalk(
        0x00FE,
        (
            '虽然真的好久没和卡特丽亚\n',
            '一起工作了，\n',
            '但因此会有很多新发现也挺有趣的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两人合作的话\n',
            '似乎能开发出不错的商品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市假如恢复的话\n',
            '要试试开发新的商品吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001E)

    def _loc_A1F3(): pass

    label('loc_A1F3')

    Jump('loc_A4A7')

    def _loc_A1F6(): pass

    label('loc_A1F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_A357',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 6, 0x1E)),
            Expr.Return,
        ),
        'loc_A273',
    )

    ChrTalk(
        0x00FE,
        (
            '修复工程虽然开始了，\n',
            '但恐怕要过很久才能恢复营业吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在要继续经营生意，\n',
            '不能把客人置之不理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A354')

    def _loc_A273(): pass

    label('loc_A273')

    ChrTalk(
        0x00FE,
        (
            '修复工程虽然开始了，\n',
            '但恐怕要过很久才能恢复营业吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在要继续经营生意，\n',
            '不能把客人置之不理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，也许是因为换了地方吧，\n',
            '客人果然不太多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才卡特丽亚还在担心呢，\n',
            '每天都来的男性客人没有再来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001E)

    def _loc_A354(): pass

    label('loc_A354')

    Jump('loc_A4A7')

    def _loc_A357(): pass

    label('loc_A357')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_A4A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 6, 0x1E)),
            Expr.Return,
        ),
        'loc_A3E5',
    )

    ChrTalk(
        0x00FE,
        (
            '这可不是小事情……\n',
            '就连卡特丽亚也深受打击啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话，正是轮到\n',
            '身为未婚夫的我要支持她才行啊。\n',
            '嗯，要支持她才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4A7')

    def _loc_A3E5(): pass

    label('loc_A3E5')

    ChrTalk(
        0x00FE,
        (
            '虽然事态变得很严重，\n',
            '但即使是为了未婚妻卡特丽亚，\n',
            '我也会坚持下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前，\n',
            '我有很长一段时间不在店里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时候她靠一个人的力量\n',
            '保住了店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以这次……\n',
            '轮到我支持她了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x001E)

    def _loc_A4A7(): pass

    label('loc_A4A7')

    TalkEnd(0x001F)

    Return()

# id: 0x0023 offset: 0xA4AB
@scena.Code('func_23_A4AB')
def func_23_A4AB():
    TalkBegin(0x0020)

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_A522',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_A509',
    )

    ChrTalk(
        0x0020,
        (
            '各位……\n',
            '那就麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '如果发现了什么，\n',
            '请再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A51F')

    def _loc_A509(): pass

    label('loc_A509')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_A51B',
    )

    Call(1, 0x0004)

    Jump('loc_A51F')

    def _loc_A51B(): pass

    label('loc_A51B')

    Call(1, 0x0003)

    def _loc_A51F(): pass

    label('loc_A51F')

    Jump('loc_A56F')

    def _loc_A522(): pass

    label('loc_A522')

    ChrTalk(
        0x0020,
        (
            '哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '外国之地果然叫人不放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '那个孩子\n',
            '一定吃了不少苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_A56F(): pass

    label('loc_A56F')

    TalkEnd(0x0020)

    Return()

# id: 0x0024 offset: 0xA573
@scena.Code('func_24_A573')
def func_24_A573():
    Return()

# id: 0x0025 offset: 0xA574
@scena.Code('func_25_A574')
def func_25_A574():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_A654',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0004, 0, 0x20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A626',
    )

    ChrTalk(
        0x00FE,
        (
            '哼哼哼，啦啦啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………咕咚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能是我的错觉……\n',
            '总觉得有股焦味儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……也罢，\n',
            '反正吃下去都一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0020)

    Jump('loc_A651')

    def _loc_A626(): pass

    label('loc_A626')

    ChrTalk(
        0x00FE,
        (
            '哼哼哼，啦啦啦……\n',
            '………………咕咚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A651(): pass

    label('loc_A651')

    Jump('loc_A76B')

    def _loc_A654(): pass

    label('loc_A654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A76B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0004, 0, 0x20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A705',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，诸位是……\n',
            '游击士吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我们的『赛希莉亚号』上\n',
            '见过很多次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个，\n',
            '很不巧船停开了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来一时半会儿还出不了港，\n',
            '所以就先来吃个饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0020)

    Jump('loc_A76B')

    def _loc_A705(): pass

    label('loc_A705')

    ChrTalk(
        0x00FE,
        (
            '那么，来吃点什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店里推荐的价格都很贵，\n',
            '我可不吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟……\n',
            '那不是一个人能吃完的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A76B(): pass

    label('loc_A76B')

    TalkEnd(0x0022)

    Return()

# id: 0x0026 offset: 0xA76F
@scena.Code('func_26_A76F')
def func_26_A76F():
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_A77C',
    )

    Jump('loc_A883')

    def _loc_A77C(): pass

    label('loc_A77C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_A786',
    )

    Jump('loc_A883')

    def _loc_A786(): pass

    label('loc_A786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_A883',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0004, 1, 0x21)),
            Expr.Return,
        ),
        'loc_A7EF',
    )

    ChrTalk(
        0x00FE,
        (
            '蛋糕店的姐姐\n',
            '是和未婚夫一起经营店铺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说早知会有今天，\n',
            '但还是挺受打击的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A883')

    def _loc_A7EF(): pass

    label('loc_A7EF')

    ChrTalk(
        0x00FE,
        (
            '我是听说\n',
            '蛋糕店姐姐在酒馆避难才来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进去里面一看，姐姐她原来\n',
            '是和未婚夫一起经营店铺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说早知会有今天，\n',
            '但还是挺受打击的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0021)

    def _loc_A883(): pass

    label('loc_A883')

    TalkEnd(0x0025)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
