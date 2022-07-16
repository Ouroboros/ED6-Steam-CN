import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2513_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2513   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔儿'),
    TXT(0x02, '汉斯'),
    TXT(0x03, '拉迪奥老师'),
    TXT(0x04, '碧欧拉老师'),
    TXT(0x05, '米丽亚老师'),
    TXT(0x06, '艾福托老师'),
    TXT(0x07, '罗迪'),
    TXT(0x08, '米克'),
    TXT(0x09, '坎诺'),
    TXT(0x0A, '雅莉丝'),
    TXT(0x0B, '帕布尔'),
    TXT(0x0C, '黛拉'),
    TXT(0x0D, '罗基克'),
    TXT(0x0E, '亚吉鲁'),
    TXT(0x0F, '罗伊斯'),
    TXT(0x10, '莫妮卡'),
    TXT(0x11, '塞尔玛'),
    TXT(0x12, '莉秋尔'),
    TXT(0x13, '巴托姆'),
    TXT(0x14, '基诺奇奥'),
    TXT(0x15, '德尼斯'),
    TXT(0x16, '妮吉塔'),
    TXT(0x17, '芙拉瑟'),
    TXT(0x18, '蕾娜'),
    TXT(0x19, '勤务员巴克斯'),
    TXT(0x1A, '侍女蕾妮'),
    TXT(0x1B, '侍女玲珐'),
    TXT(0x1C, '拉多公爵'),
    TXT(0x1D, '科洛多议长'),
    TXT(0x1E, '王都的主教'),
    TXT(0x1F, '暗杀者'),
    TXT(0x20, '波利'),
    TXT(0x21, '特蕾莎院长'),
    TXT(0x22, '达尼艾尔'),
    TXT(0x23, '玛丽'),
    TXT(0x24, '克拉姆'),
    TXT(0x25, '科林兹校长'),
    TXT(0x26, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2513.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5AE3
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02260._CH', 'ED6_DT07/CH02260P._CP'),
        ('ED6_DT07/CH02270._CH', 'ED6_DT07/CH02270P._CP'),
        ('ED6_DT07/CH02280._CH', 'ED6_DT07/CH02280P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT06/CH20069._CH', 'ED6_DT06/CH20069P._CP'),
        ('ED6_DT06/CH20071._CH', 'ED6_DT06/CH20071P._CP'),
        ('ED6_DT07/CH01083._CH', 'ED6_DT07/CH01083P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
    ]

# id: 0x10002 offset: 0x1AA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 59640,
            z                   = 1000,
            y                   = 13450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 66040,
            z                   = 1000,
            y                   = 16210,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 0,
            y                   = 9300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 2160,
            z                   = 0,
            y                   = 8570,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 3320,
            z                   = 0,
            y                   = 8570,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -2100,
            z                   = 0,
            y                   = 9290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -2970,
            z                   = 0,
            y                   = 3210,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 5200,
            z                   = 250,
            y                   = -4530,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -4160,
            z                   = 0,
            y                   = 5180,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -5390,
            z                   = 0,
            y                   = 3910,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -3890,
            z                   = 0,
            y                   = 1240,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -5880,
            z                   = 0,
            y                   = 1770,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -470,
            z                   = 0,
            y                   = 720,
            direction           = 192,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -820,
            z                   = 0,
            y                   = -3270,
            direction           = 1,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -3170,
            z                   = 0,
            y                   = -1120,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 1130,
            z                   = 0,
            y                   = -2530,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 1380,
            z                   = 0,
            y                   = -300,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -2520,
            z                   = 0,
            y                   = -2890,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 3400,
            z                   = 0,
            y                   = 3800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 4400,
            z                   = 0,
            y                   = 200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 3100,
            z                   = 0,
            y                   = 1700,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 6030,
            z                   = 0,
            y                   = 2120,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 6230,
            z                   = 0,
            y                   = 5420,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 6240,
            z                   = 0,
            y                   = 3780,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -510,
            z                   = 0,
            y                   = 4270,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 61850,
            z                   = 1000,
            y                   = 17310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 63320,
            z                   = 1000,
            y                   = 15250,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 57740,
            z                   = 1000,
            y                   = 16980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 58590,
            z                   = 1000,
            y                   = 17010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 59600,
            z                   = 1000,
            y                   = 16379,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 56830,
            z                   = 1000,
            y                   = 16500,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 33500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 6000,
            z                   = 200,
            y                   = 22200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 4300,
            z                   = 200,
            y                   = 22900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x64A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_654',
    )

    Jump('loc_884')

    def _loc_654(): pass

    label('loc_654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_832',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
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
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 590, 0, 4100, 270)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -820, 0, 4100, 90)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x70),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x71),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6D),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6C),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_82F',
    )

    ExecExpressionWithValue(
        0x0008,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x01,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_82F(): pass

    label('loc_82F')

    Jump('loc_884')

    def _loc_832(): pass

    label('loc_832')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_83C',
    )

    Jump('loc_884')

    def _loc_83C(): pass

    label('loc_83C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_846',
    )

    Jump('loc_884')

    def _loc_846(): pass

    label('loc_846')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_850',
    )

    Jump('loc_884')

    def _loc_850(): pass

    label('loc_850')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_85F',
    )

    ClearChrFlags(0x0020, 0x0080)

    Jump('loc_884')

    def _loc_85F(): pass

    label('loc_85F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_869',
    )

    Jump('loc_884')

    def _loc_869(): pass

    label('loc_869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_873',
    )

    Jump('loc_884')

    def _loc_873(): pass

    label('loc_873')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_87D',
    )

    Jump('loc_884')

    def _loc_87D(): pass

    label('loc_87D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_884',
    )

    def _loc_884(): pass

    label('loc_884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_89B',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x001C)
    OP_B1('t2513_n')

    def _loc_89B(): pass

    label('loc_89B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_8B2',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x001D)
    OP_B1('t2513_n')

    def _loc_8B2(): pass

    label('loc_8B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_8C9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, 0x001E)

    def _loc_8C9(): pass

    label('loc_8C9')

    Return()

# id: 0x0001 offset: 0x8CA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8EB',
    )

    OP_B1('t2513_y')

    Jump('loc_8F4')

    def _loc_8EB(): pass

    label('loc_8EB')

    OP_B1('t2513_n')

    def _loc_8F4(): pass

    label('loc_8F4')

    Return()

# id: 0x0002 offset: 0x8F5
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
        'loc_925',
    )

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_A67')

    def _loc_925(): pass

    label('loc_925')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1300)

    Jump('loc_A67')

    def _loc_93E(): pass

    label('loc_93E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_957',
    )

    OP_99(0x00FE, 0x02, 0x07, 1250)

    Jump('loc_A67')

    def _loc_957(): pass

    label('loc_957')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_970',
    )

    OP_99(0x00FE, 0x03, 0x07, 1200)

    Jump('loc_A67')

    def _loc_970(): pass

    label('loc_970')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_989',
    )

    OP_99(0x00FE, 0x04, 0x07, 1150)

    Jump('loc_A67')

    def _loc_989(): pass

    label('loc_989')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9A2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1100)

    Jump('loc_A67')

    def _loc_9A2(): pass

    label('loc_9A2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9BB',
    )

    OP_99(0x00FE, 0x06, 0x07, 1050)

    Jump('loc_A67')

    def _loc_9BB(): pass

    label('loc_9BB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9D4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1355)

    Jump('loc_A67')

    def _loc_9D4(): pass

    label('loc_9D4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9ED',
    )

    OP_99(0x00FE, 0x01, 0x07, 1305)

    Jump('loc_A67')

    def _loc_9ED(): pass

    label('loc_9ED')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A06',
    )

    OP_99(0x00FE, 0x02, 0x07, 1255)

    Jump('loc_A67')

    def _loc_A06(): pass

    label('loc_A06')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A1F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1205)

    Jump('loc_A67')

    def _loc_A1F(): pass

    label('loc_A1F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A38',
    )

    OP_99(0x00FE, 0x04, 0x07, 1155)

    Jump('loc_A67')

    def _loc_A38(): pass

    label('loc_A38')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A51',
    )

    OP_99(0x00FE, 0x05, 0x07, 1105)

    Jump('loc_A67')

    def _loc_A51(): pass

    label('loc_A51')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A67',
    )

    OP_99(0x00FE, 0x06, 0x07, 1055)

    def _loc_A67(): pass

    label('loc_A67')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A7C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1200)

    Jump('loc_A67')

    def _loc_A7C(): pass

    label('loc_A7C')

    Return()

# id: 0x0003 offset: 0xA7D
@scena.Code('func_03_A7D')
def func_03_A7D():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '各位老师和同学\n',
            '真的是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次学园祭\n',
            '没有辜负王立学院的盛名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0xAD0
@scena.Code('func_04_AD0')
def func_04_AD0():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B1C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '大家真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每个人都尽全力努力了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B49')

    def _loc_B1C(): pass

    label('loc_B1C')

    ChrTalk(
        0x00FE,
        (
            '这次结束后，\n',
            '就和米丽亚一起去城里玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B49(): pass

    label('loc_B49')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0xB4D
@scena.Code('func_05_B4D')
def func_05_B4D():
    TalkBegin(0x000C)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '大家都干得很不错呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算他们合格了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x0006 offset: 0xB8B
@scena.Code('func_06_B8B')
def func_06_B8B():
    TalkBegin(0x000D)

    ChrTalk(
        0x00FE,
        (
            '能顺利地完成真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天开始大家\n',
            '还是要努力学习哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0xBD5
@scena.Code('func_07_BD5')
def func_07_BD5():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C1A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '好，庆祝吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家痛快地玩吧，痛快地玩吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C53')

    def _loc_C1A(): pass

    label('loc_C1A')

    ChrTalk(
        0x00FE,
        (
            '明天开始又要上课了，\n',
            '现实在等着我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C53(): pass

    label('loc_C53')

    TalkEnd(0x000E)

    Return()

# id: 0x0008 offset: 0xC57
@scena.Code('func_08_C57')
def func_08_C57():
    TalkBegin(0x000F)

    ChrTalk(
        0x00FE,
        (
            '学园祭已经结束了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那干嘛还要特地\n',
            '聚在一起那么吵闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我好想快点回去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000F)

    Return()

# id: 0x0009 offset: 0xCB7
@scena.Code('func_09_CB7')
def func_09_CB7():
    TalkBegin(0x0010)

    ChrTalk(
        0x00FE,
        (
            '好像失去了什么的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，为学园祭做准备的\n',
            '那段时间是最快乐的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0010)

    Return()

# id: 0x000A offset: 0xD0B
@scena.Code('func_0A_D0B')
def func_0A_D0B():
    TalkBegin(0x0011)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '庆祝胜利真是好开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0011)

    Return()

# id: 0x000B offset: 0xD35
@scena.Code('func_0B_D35')
def func_0B_D35():
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '准备花了那么多时间，\n',
            '今天却是一眨眼就过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '客人们看起来很高兴啊。\n',
            '我自己也很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x000C offset: 0xDA3
@scena.Code('func_0C_DA3')
def func_0C_DA3():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '这几天虽然很忙，\n',
            '但我很努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是很有成就感的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x000D offset: 0xDE5
@scena.Code('func_0D_DE5')
def func_0D_DE5():
    TalkBegin(0x0014)

    ChrTalk(
        0x00FE,
        (
            '我家在卢安，\n',
            '好想提前回去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过今天就趁着余兴一起庆祝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x000E offset: 0xE35
@scena.Code('func_0E_E35')
def func_0E_E35():
    TalkBegin(0x0015)

    ChrTalk(
        0x00FE,
        (
            '顺利地结束了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0015)

    Return()

# id: 0x000F offset: 0xE54
@scena.Code('func_0F_E54')
def func_0F_E54():
    TalkBegin(0x0016)

    ChrTalk(
        0x00FE,
        (
            '击剑部的冰淇淋店\n',
            '反响十分好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很高兴，\n',
            '因为来学园祭的孩子们那么开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0016)

    Return()

# id: 0x0010 offset: 0xEAF
@scena.Code('func_10_EAF')
def func_10_EAF():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F50',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿。\n',
            '啊，好开心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，学园祭……\n',
            '因为一年只有一次，\n',
            '大家齐心协力做这件事才会十分开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是每天都这样，\n',
            '大家一定会累死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F6B')

    def _loc_F50(): pass

    label('loc_F50')

    ChrTalk(
        0x00FE,
        (
            '嘿嘿。\n',
            '啊，好开心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F6B(): pass

    label('loc_F6B')

    TalkEnd(0x0017)

    Return()

# id: 0x0011 offset: 0xF6F
@scena.Code('func_11_F6F')
def func_11_F6F():
    TalkBegin(0x0018)

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '真是个不能不参加的活动呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都尽力了，\n',
            '这就是最好的结局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0018)

    Return()

# id: 0x0012 offset: 0xFC4
@scena.Code('func_12_FC4')
def func_12_FC4():
    TalkBegin(0x0019)

    ChrTalk(
        0x00FE,
        (
            '啊，是前辈们呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不论舞台剧还是冰淇淋店都很成功。\n',
            '莉秋尔，非常开心呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0019)

    Return()

# id: 0x0013 offset: 0x101C
@scena.Code('func_13_101C')
def func_13_101C():
    TalkBegin(0x001A)

    ChrTalk(
        0x00FE,
        (
            '哈哈，我也非常开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '舞台剧也非常好哦。\n',
            '真是辛苦大家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001A)

    Return()

# id: 0x0014 offset: 0x1066
@scena.Code('func_14_1066')
def func_14_1066():
    TalkBegin(0x001B)

    ChrTalk(
        0x00FE,
        (
            '呼，好累呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快点回家睡觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001B)

    Return()

# id: 0x0015 offset: 0x1095
@scena.Code('func_15_1095')
def func_15_1095():
    TalkBegin(0x001C)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '今天不看书也不要紧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我有\n',
            '平时的积累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001C)

    Return()

# id: 0x0016 offset: 0x10DA
@scena.Code('func_16_10DA')
def func_16_10DA():
    TalkBegin(0x001D)

    ChrTalk(
        0x00FE,
        (
            '真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥\n',
            '就只会打哈欠……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001D)

    Return()

# id: 0x0017 offset: 0x1110
@scena.Code('func_17_1110')
def func_17_1110():
    TalkBegin(0x001E)
    OP_4A(0x001F, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11B6',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    ChrTalk(
        0x001E,
        (
            '真是的，都怪你，\n',
            '让我忙得焦头烂额。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '老爷子也很\n',
            '感谢你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '呵呵，得到你的夸奖真是光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '我只是为了\n',
            '锻炼芙拉瑟你嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x001F, 0x0010)

    Jump('loc_122B')

    def _loc_11B6(): pass

    label('loc_11B6')

    ChrTalk(
        0x001E,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '哎呀，你为什么叹气啊？\n',
            '有烦恼的话可以和我谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001E, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x001E,
        (
            '求你了，放过我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_122B(): pass

    label('loc_122B')

    OP_4B(0x001F, 255)
    TalkEnd(0x001E)

    Return()

# id: 0x0018 offset: 0x1233
@scena.Code('func_18_1233')
def func_18_1233():
    TalkBegin(0x001F)
    OP_4A(0x001E, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12D9',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    ChrTalk(
        0x001E,
        (
            '真是的，都怪你，\n',
            '让我忙得焦头烂额。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '老爷子也很\n',
            '感谢你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '呵呵，得到你的夸奖真是光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '我只是为了\n',
            '锻炼芙拉瑟你嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x001F, 0x0010)

    Jump('loc_12E9')

    def _loc_12D9(): pass

    label('loc_12D9')

    ChrTalk(
        0x00FE,
        (
            '呵呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12E9(): pass

    label('loc_12E9')

    OP_4B(0x001E, 255)
    TalkEnd(0x001F)

    Return()

# id: 0x0019 offset: 0x12F1
@scena.Code('func_19_12F1')
def func_19_12F1():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1378',
    )

    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))

    ChrTalk(
        0x00FE,
        (
            '#0510060932V#640F哎？\n',
            '你们还在这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060933V不赶快回到卢安没有关系吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060934V如果想参加庆祝会的话十分欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13CE')

    def _loc_1378(): pass

    label('loc_1378')

    ChrTalk(
        0x00FE,
        (
            '#0510060935V#640F不赶快回到卢安\n',
            '没有关系吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060936V如果想参加庆祝会的话十分欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13CE(): pass

    label('loc_13CE')

    TalkEnd(0x0008)

    Return()

# id: 0x001A offset: 0x13D2
@scena.Code('func_1A_13D2')
def func_1A_13D2():
    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '#0520060937V#730F哦，\n',
            '你们是不是舍不得庆祝会啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0521220001V今天全部\n',
            '由老师们请客呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x001B offset: 0x142C
@scena.Code('func_1B_142C')
def func_1B_142C():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1488',
    )

    ChrTalk(
        0x00FE,
        (
            '我的工作就是\n',
            '管理学院的设施和用品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是在学园祭前\n',
            '要好好检查才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1488(): pass

    label('loc_1488')

    TalkEnd(0x0020)

    Return()

# id: 0x001C offset: 0x148C
@scena.Code('func_1C_148C')
def func_1C_148C():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    CameraMove(-410, 4000, -4600, 0)
    OP_67(0, 5000, -10000, 0)
    CameraSetDistance(3720, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0101, 850, 1000, 14010, 270)
    SetChrPos(0x0105, -960, 1000, 14000, 90)
    SetChrPos(0x0008, -80, 1000, 13250, 0)
    SetChrChipByIndex(0x0101, 14)
    SetChrChipByIndex(0x0105, 15)
    SetChrChipByIndex(0x0102, 16)
    FadeIn(1000, 0)
    OP_13(0x005F)
    CameraMove(910, 2000, 12490, 4000)
    Fade(500)
    CameraMove(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x0009, 0x0040)
    SetChrPos(0x0101, 61000, 1000, 14250, 225)
    SetChrPos(0x0105, 59080, 1000, 14210, 135)
    SetChrPos(0x0008, 60000, 1000, 13140, 45)
    SetChrPos(0x0102, 67180, 1000, 16860, 270)
    SetChrPos(0x0009, 67180, 1000, 16860, 270)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010051149V#340F#2P嗯～这就是戏服啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051150V刚才说要演骑士，\n',
            '我还以为要穿铠甲什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051151V#644F#3P因为穿甲胄的话，\n',
            '会妨碍到演员动作的流畅度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051152V所以我们就照现在\n',
            '王室亲卫队的制服式样设计了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051153V#340F#2P哦，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051154V#341F科洛丝是短发，\n',
            '感觉正适合这角色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051155V#351F#1P呵呵，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051156V艾丝蒂尔也很适合呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051157V#348F#2P嘿嘿，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051158V对了……\n',
            '为什么我们的衣服颜色不同？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051159V#350F#1P我演的是\n',
            '平民的『苍骑士奥斯卡』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051160V艾丝蒂尔演的是\n',
            '贵族的『红骑士尤利乌斯』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051161V这是双方势力的代表色。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051162V#340F#2P哦～原来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051163V那么，约修亚是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051164V#3P牵挂着两名骑士的\n',
            '王家『白色公主塞茜莉亚』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051165V好了公主，请到这边来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051166V#3P再、再等一下。\n',
            '……我还没做好心理准备………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_66(0x0000)

    @scena.Lambda('lambda_18F6')
    def lambda_18F6():
        CameraMove(61500, 2310, 14620, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_18F6)

    @scena.Lambda('lambda_190E')
    def lambda_190E():
        CameraSetDistance(850, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_190E)

    @scena.Lambda('lambda_191E')
    def lambda_191E():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_191E')

    DispatchAsync2(0x0101, 0x0001, lambda_191E)

    @scena.Lambda('lambda_192F')
    def lambda_192F():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_192F')

    DispatchAsync2(0x0105, 0x0001, lambda_192F)

    @scena.Lambda('lambda_1940')
    def lambda_1940():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1940')

    DispatchAsync2(0x0008, 0x0001, lambda_1940)

    @scena.Lambda('lambda_1951')
    def lambda_1951():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1951')

    DispatchAsync2(0x0009, 0x0001, lambda_1951)

    @scena.Lambda('lambda_1962')
    def lambda_1962():
        ChrMoveTo(0x00FE, 62850, 1000, 15120, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1962)

    Sleep(800)

    @scena.Lambda('lambda_1982')
    def lambda_1982():
        ChrMoveTo(0x00FE, 63260, 1000, 15870, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1982)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 225, 0)
    WaitForThreadExit(0x0009, 0x0002)
    Sleep(200)

    ChrMoveTo(0x0009, 63580, 1000, 14220, 2000, 0x00)
    TerminateThread(0x0009, 0xFF)
    SetChrDirection(0x0009, 315, 0)

    ChrTalk(
        0x0102,
        (
            '#0020051167V#363F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051168V#344F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051169V#354F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051170V#643F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051171V#367F#2P拜托了，说点什么吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051172V在这种沉默的气氛\n',
            '呆呆地站着实在是有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051173V#340F哎呀，怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051174V#341F完全没有不协调的感觉⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051175V#351F我也吃了一惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051176V#358F啊啊，真的好漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051177V#731F嗯嗯，自信一点啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051178V假如你真的是女孩子，\n',
            '我恐怕会忍不住上来挑逗你哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0102,
        (
            '#0020051179V#368F#2P多谢你们真诚的感想。\n',
            '不过我可一点都高兴不起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051180V#659F哦呵呵……\n',
            '这就是我要的效果……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051181V这样的人选安排\n',
            '一定会受到各方面的认同……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051182V#641F各位，大家要团结一致，\n',
            '打造最完美的舞台剧哦～！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#341F#1P#1K好～！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#351F#1K是！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#0520051185V#731F#1K喔！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0102,
        (
            '#0020051186V#367F#2P咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '由当晚开始，艾丝蒂尔和约修亚\n',
            '分别住进了学院的女生宿舍和男生宿舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_66(0x0001)
    OP_28(0x003D, 0x01, 0x0080)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2512._SN', 115, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x1D9D
@scena.Code('func_1D_1D9D')
def func_1D_1D9D():
    EventBegin(0x00)
    OP_77(0xFF, 0xC8, 0x96, 0x00, 0x00000000)
    CameraMove(60480, 1000, 9080, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(19000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    SetChrPos(0x0101, 60900, 1000, 12690, 270)
    SetChrPos(0x0105, 59100, 1000, 12780, 90)
    SetChrPos(0x0102, 63020, 1000, 16920, 225)
    SetChrPos(0x0008, 58340, 1000, 14950, 0)
    SetChrPos(0x0009, 61530, 1000, 15270, 45)
    CreateThread(0x0102, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x0102, 16)
    SetChrChipByIndex(0x0101, 23)
    SetChrChipByIndex(0x0105, 24)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0105, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1E91')
    def lambda_1E91():
        CameraMove(60970, 1000, 14570, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1E91)

    @scena.Lambda('lambda_1EA9')
    def lambda_1EA9():
        OP_6C(30000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1EA9)

    OP_0D()
    SetChrFlags(0x0101, 0x0020)
    SetChrFlags(0x0105, 0x0020)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0105, 0x1000)

    @scena.Lambda('lambda_1ECE')
    def lambda_1ECE():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1ECE)

    OP_99(0x0101, 0x01, 0x02, 1500)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1EF7')
    def lambda_1EF7():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1EF7)

    WaitForThreadExit(0x0105, 0x0001)
    Sleep(150)

    @scena.Lambda('lambda_1F1C')
    def lambda_1F1C():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F1C)

    OP_99(0x0101, 0x01, 0x02, 1500)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1F45')
    def lambda_1F45():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1F45)

    WaitForThreadExit(0x0105, 0x0001)
    Sleep(500)

    SetChrSubChip(0x0101, 0)

    @scena.Lambda('lambda_1F6F')
    def lambda_1F6F():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1F6F)

    OP_99(0x0105, 0x01, 0x02, 1500)
    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_1F98')
    def lambda_1F98():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F98)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(150)

    @scena.Lambda('lambda_1FBD')
    def lambda_1FBD():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1FBD)

    OP_99(0x0105, 0x01, 0x02, 1500)
    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_1FE6')
    def lambda_1FE6():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FE6)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    SetChrSubChip(0x0105, 0)

    @scena.Lambda('lambda_2010')
    def lambda_2010():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2010)

    OP_99(0x0101, 0x01, 0x02, 2000)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2039')
    def lambda_2039():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2039)

    WaitForThreadExit(0x0105, 0x0001)
    Sleep(120)

    @scena.Lambda('lambda_205E')
    def lambda_205E():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_205E)

    OP_99(0x0101, 0x01, 0x02, 2000)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2087')
    def lambda_2087():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2087)

    WaitForThreadExit(0x0105, 0x0001)
    Sleep(120)

    @scena.Lambda('lambda_20AC')
    def lambda_20AC():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20AC)

    OP_99(0x0101, 0x01, 0x02, 2000)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_20D5')
    def lambda_20D5():
        ChrMoveToRelativeAsync(0x00FE, -600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_20D5)

    WaitForThreadExit(0x0105, 0x0001)
    Sleep(500)

    SetChrSubChip(0x0101, 0)
    FadeOut(1500, 0, -1)

    @scena.Lambda('lambda_2109')
    def lambda_2109():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2109)

    OP_99(0x0105, 0x01, 0x02, 2000)
    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_2132')
    def lambda_2132():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2132)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(120)

    @scena.Lambda('lambda_2157')
    def lambda_2157():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2157)

    OP_99(0x0105, 0x01, 0x02, 2000)
    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_2180')
    def lambda_2180():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2180)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(120)

    @scena.Lambda('lambda_21A5')
    def lambda_21A5():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_21A5)

    OP_99(0x0105, 0x01, 0x02, 2000)
    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_21CE')
    def lambda_21CE():
        ChrMoveToRelativeAsync(0x00FE, 600, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21CE)

    WaitForThreadExit(0x0101, 0x0001)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '而放学后则要进行严格的排练，直到深夜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，两人忙碌而快乐的校园生活\n',
            '就在眨眼之间飞快过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000007D0)
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2533._SN', 100, 0, 0)
    IdleLoop()
    CameraMove(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x0008, 0x0080)
    SetChrPos(0x0009, 610, 0, -360, 0)
    SetChrPos(0x0102, -400, 0, 430, 0)
    SetChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrChipByIndex(0x0101, 14)
    SetChrChipByIndex(0x0105, 15)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0105, 0)
    SetChrPos(0x0101, 62000, 1000, 14000, 270)
    SetChrPos(0x0105, 58000, 1000, 14000, 90)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(2000, 0)
    PlayBGM(97)
    OP_0D()
    Sleep(1000)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051273V#424F#2P挚友啊。\n',
            '事已至此你我别无选择……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051274V命中注定\n',
            '我们终要决一雌雄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(22, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 23)
    SetChrSubChip(0x0101, 5)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051275V#421F#2P拔剑！\n',
            '为了彼此所背负的责任！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051276V更为了你我心爱的公主！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051277V#359F#1P所谓命运，\n',
            '是凭自己的双手开拓的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051278V本应承担的立场与公主的微笑，\n',
            '此时此刻是那么的遥远……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051279V#422F#2P你怕了吗，奥斯卡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051280V#357F#1P然而，此刻驱使着身体的，\n',
            '这近乎疯狂的热情究竟是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051281V我似乎再次不可避免地\n',
            '在此与你一决高下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(22, 0x00, 0x64)
    SetChrChipByIndex(0x0105, 24)
    SetChrSubChip(0x0105, 8)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051282V#352F#1P在以革命之名的暴风雨\n',
            '将一切吞没之前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051283V以手中的剑刃决定命运吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051284V#420F#2P啊啊……\n',
            '空之女神将见证你我二人的灵魂！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051285V来吧，一决胜负！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051286V#356F#1P来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0105)
    OP_21()

    ChrTalk(
        0x0101,
        (
            '#0010051287V#347F#2P哈～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051288V#357F#1P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(22, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 14)
    SetChrChipByIndex(0x0105, 15)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0105, 0)
    OP_0D()
    PlayBGM(14)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010051289V#341F#2P成功了～㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051290V终于准确无误地\n',
            '完成了这一幕呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051291V#351F#1P呵呵，你的演技真是逼真。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051292V#346F#2P嘿嘿，不过跟科洛丝相比，\n',
            '我的功夫还差的远呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051293V而且，\n',
            '你又从来不会念错过台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051294V#350F#1P那是因为我从很早之前\n',
            '就开始看剧本了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051295V现在我也总算能\n',
            '跟得上艾丝蒂尔的动作了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051296V#351F要你不厌其烦地指点我练剑，\n',
            '真是太谢谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051297V#340F#2P你太客气了，\n',
            '因为你基础本来就很好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051298V只要你愿意，我想你随时\n',
            '都能取得游击士的资格的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051299V#355F#1P呵呵，你就别抬举我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F终于，明天就要正式演出了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051301V不知道特蕾莎老师和孩子们\n',
            '会不会喜欢呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呵呵，你真的很关心\n',
            '特蕾莎院长他们呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '简直就像一家人似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，对不起。\n',
            '我说错什么话了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不是呢……\n',
            '就像艾丝蒂尔所说的那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051307V是老师他们让我知道\n',
            '家人才是世上最宝贵的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为我刚出生不久，\n',
            '父母就在一次意外中去世了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F虽然被富裕的亲戚收养，\n',
            '过着自由自在随心所欲的生活……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051311V但我却从来都不知道，\n',
            '所谓的家人究竟是什么样的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '直到１０年前……\n',
            '遇到老师他们的那一天开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F１０年前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难道是『百日战役』的时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是的，\n',
            '那时候我正好来到了卢安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051316V不仅要逃避帝国军追杀，\n',
            '而且还和自己的亲戚走散了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051317V是特蕾莎老师和\n',
            '她丈夫约瑟夫先生保护了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F战争结束后，我就被亲戚接回去了。\n',
            '虽然只是短短的几个月……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051320V但是，特蕾莎老师和约瑟夫叔叔\n',
            '对我的关心和照顾却是无微不至的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那时候，我才第一次知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051322V拥有父亲和母亲，\n',
            '是一种什么样的感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051323V全家人能够生活在一起，\n',
            '又是一种何等温暖的幸福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对、对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051326V情不自禁之下，\n',
            '说了那么一大堆无聊的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不，没这回事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '明天的舞台剧……\n',
            '我们一起加油，来场绝佳的演出吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F……好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F由我来说可能有点自卖自夸，\n',
            '不过，我想绝对会很精彩的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051331V不单是我们，\n',
            '乔儿和汉斯也都很努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051333V不过，功劳最大的\n',
            '应该还是非约修亚莫属吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051334V想不到他的演技居然那么好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '明明那么不情愿，\n',
            '却还能把公主演得活灵活现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不论是发音还是时机的把握，\n',
            '真的丝毫也不比职业演员逊色呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051338V约修亚过去曾经演过戏吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在我和他相遇之前，\n',
            '有关他的事我自己也不是很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051341V我不知道他以前经历过什么，\n',
            '而且，他一直总不想和我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051343V对不起……\n',
            '问了不该问的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈，没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯～约修亚确实就是\n',
            '那种什么事都能做得很完美的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的总是优哉游哉从容不迫的，\n',
            '一点儿都不可爱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051347V倒还是偶尔慌张的时候\n',
            '才显出他那比较可爱一面～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051349V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051350V#000F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F其实我们两个的角色\n',
            '换过来扮演或许会比较好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F尤利乌斯和奥斯卡啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051354V我觉得奥斯卡还是\n',
            '由艾丝蒂尔来演比较好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎？为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过我和贵族出身的尤利乌斯\n',
            '在身份上的确有点不大相称……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不，我不是这个意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……就是，舞台剧的最后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哦、哦哦……\n',
            '是公主对奥斯卡做那个……是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，那个不只是对着脸颊吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940006V#040F虽然是这样没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真是便宜了约修亚啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051362V难道说科洛丝\n',
            '不想和约修亚演那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F我、我不是这个意思！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，总觉得有点\n',
            '对不起你们两个呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F讨、讨厌啦～\n',
            '别像乔儿那样说这种话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我和他其实也只是家人关系而已，\n',
            '反正约修亚也只是把我当作\n',
            '妹妹那样照顾罢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940007V#040F是……这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F他呀，总是站在老爸那边，\n',
            '把我当作小孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051369V真是气死我了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '总之呢，我觉得你完全\n',
            '没必要为这种事和我介意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……啊，你们在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_34F5')
    def lambda_34F5():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34F5)

    @scena.Lambda('lambda_3503')
    def lambda_3503():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3503)

    @scena.Lambda('lambda_3511')
    def lambda_3511():
        CameraMove(-150, 1000, 11520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3511)

    @scena.Lambda('lambda_3529')
    def lambda_3529():
        ChrWalkTo(0x00FE, 220, 0, 8240, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3529)

    ChrWalkTo(0x0102, 1300, 0, 8610, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F约、约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F汉斯也在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051375V#730F彩排都结束了，\n',
            '居然还在练习啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051376V你们俩还真是卖力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051377V#010F决斗那场戏，没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F当然，就交给我们吧！\n',
            '一定让你看到完美无缺的表演！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这样啊……\n',
            '嗯，那我就拭目以待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940008V#040F说起来，\n',
            '你们难道是来找我们的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051382V#730F是啊，今天是艾丝蒂尔和约修亚\n',
            '在学院里住的最后一天了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051383V大家不如一起吃顿晚饭，\n',
            '也算是为了预祝明天的成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好，我也赞成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F也请让我一同参加哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051387V#010F对了……\n',
            '乔儿没和你们在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F你说乔儿啊，\n',
            '她刚才被校长叫走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051389V我去找她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，我也去！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051391V约修亚你们\n',
            '就先去食堂占位子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那我们就先去食堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#730F好！老大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F谁是你的老大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_3877')
    def lambda_3877():
        ChrWalkTo(0x00FE, 320, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3877)

    Sleep(500)

    ChrWalkTo(0x0102, 320, 0, 320, 3000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    CameraMove(-410, 1000, 15230, 1000)
    OP_67(0, 9500, -10000, 0)

    ChrTalk(
        0x0101,
        (
            '#000F呵呵，看来他们两个\n',
            '也相处得不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051397V约修亚他有时候\n',
            '会有拒人于千里之外的一面，\n',
            '我本来还有点担心呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#000F咦？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#040F不不……\n',
            '也没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯～好了。\n',
            '我们先去换衣服吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051402V穿成这样招摇过市的话，\n',
            '实在是有点难为情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160857V#040F嗯，是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    CameraMove(-35450, 1000, 8010, 0)
    OP_6C(45000, 0)
    FormationDelMember(0x01, 0xFF)
    SetChrPos(0x0105, -36670, 1000, 6980, 0)
    SetChrPos(0x0101, -36420, 1000, 8500, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#000F……好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那我们现在\n',
            '就去接乔儿回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x001E offset: 0x3AA8
@scena.Code('func_1E_3AA8')
def func_1E_3AA8():
    EventBegin(0x00)

    ExecExpressionWithVar(
        0x1B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0105, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    CameraMove(-63840, 1000, 10070, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -64190, 1000, 9630, 225)
    SetChrPos(0x0105, -63900, 1000, 8550, 270)
    SetChrPos(0x0102, -65269, 1000, 9930, 180)
    SetChrPos(0x0009, -66110, 1000, 8290, 45)
    SetChrPos(0x0008, -65560, 1000, 7740, 45)
    TerminateThread(0x0028, 0xFF)
    TerminateThread(0x002A, 0xFF)
    TerminateThread(0x002B, 0xFF)
    TerminateThread(0x0029, 0xFF)
    TerminateThread(0x0027, 0xFF)
    TerminateThread(0x002C, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetChrPos(0x0028, -66100, 0, 1150, 0)
    SetChrPos(0x002A, -66100, 0, 1150, 0)
    SetChrPos(0x002B, -66100, 0, 1150, 0)
    SetChrPos(0x0029, -66100, 0, 1150, 0)
    SetChrPos(0x0027, -66100, 0, 1150, 0)
    SetChrPos(0x002C, -66100, 0, 1150, 0)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0510060769V#641F呀～真是辛苦大家了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060770V由我做导演也许缺乏说服力，\n',
            '不过这真的是有史以来最棒的舞台剧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060771V#041F#2P虽然一开始，\n',
            '因为男女反串而被大家笑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060772V不过随着剧情的发展，\n',
            '大家也都认真地观赏起来，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060773V#010F#1P嗯，是啊。\n',
            '扮成那样总算是值得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060774V#017F不过我再也不想有第二次了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060775V#731F#6P哈哈，别那么说嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060776V摄影部的同学\n',
            '说拍了好几张剧照……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060777V我可是很看好\n',
            '公主您的照片销量哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060778V#018F#1P啊？饶了我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060779V#649F我想艾丝蒂尔她们的照片\n',
            '也一定会很畅销的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060780V男生当然是不用说了，\n',
            '低年级的女生也都会去买的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060781V#641F而且买到手的时候还会高喊\n',
            '『姐姐大人～』呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060782V#045F#2P真是的，乔儿你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060783V#503F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060784V#014F#1P咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060785V怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060786V#004F#5P#3S哎……？',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0101, 50, 0, 300, 6000)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060787V#008F#5P啊，什么？什么事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060788V#013F#1P不……\n',
            '我是说你啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060789V舞台剧结束之后\n',
            '就好像神情恍惚的样子，\n',
            '没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060790V#730F#6P哎呀，演了一场那么艰苦的决斗，\n',
            '觉得累也是正常的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060791V#642F如果不舒服的话，\n',
            '我带你去医务室吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 300)

    ChrTalk(
        0x0101,
        (
            '#0010060792V#008F#5P没、没事啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060793V怎么说我也是个游击士，\n',
            '这点程度的辛苦，家常便饭啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060794V#503F只是，好像有点失魂落魄的，\n',
            '或者说，头脑有点混乱什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060795V#043F#2P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060796V艾丝蒂尔，难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060797V#503F#5P你、你别误会啦。\n',
            '完全不是那么回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060798V#504F啊～不管了，总之我完全不在意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060799V#014F#1P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060800V#1P呵呵……\n',
            '可以打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_4297')
    def lambda_4297():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4297)

    @scena.Lambda('lambda_42A5')
    def lambda_42A5():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_42A5)

    @scena.Lambda('lambda_42B3')
    def lambda_42B3():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_42B3)

    @scena.Lambda('lambda_42C1')
    def lambda_42C1():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_42C1)

    @scena.Lambda('lambda_42CF')
    def lambda_42CF():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_42CF)

    Sleep(400)

    @scena.Lambda('lambda_42E2')
    def lambda_42E2():
        ChrTurnDirection(0x00FE, 0x002A, 0)
        Yield()

        Jump('lambda_42E2')

    DispatchAsync2(0x0101, 0x0001, lambda_42E2)

    @scena.Lambda('lambda_42F3')
    def lambda_42F3():
        ChrTurnDirection(0x00FE, 0x0029, 0)
        Yield()

        Jump('lambda_42F3')

    DispatchAsync2(0x0102, 0x0001, lambda_42F3)

    @scena.Lambda('lambda_4304')
    def lambda_4304():
        ChrTurnDirection(0x00FE, 0x002B, 0)
        Yield()

        Jump('lambda_4304')

    DispatchAsync2(0x0105, 0x0001, lambda_4304)

    @scena.Lambda('lambda_4315')
    def lambda_4315():
        ChrTurnDirection(0x00FE, 0x002B, 0)
        Yield()

        Jump('lambda_4315')

    DispatchAsync2(0x0008, 0x0001, lambda_4315)

    @scena.Lambda('lambda_4326')
    def lambda_4326():
        ChrTurnDirection(0x00FE, 0x002B, 0)
        Yield()

        Jump('lambda_4326')

    DispatchAsync2(0x0009, 0x0001, lambda_4326)

    @scena.Lambda('lambda_4337')
    def lambda_4337():
        CameraMove(-64769, 1000, 9050, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4337)

    CreateThread(0x002B, 0x01, 0x00, 0x0020)
    CreateThread(0x002A, 0x01, 0x00, 0x0021)
    CreateThread(0x0027, 0x01, 0x00, 0x0022)
    CreateThread(0x0029, 0x01, 0x00, 0x0023)
    CreateThread(0x0028, 0x01, 0x00, 0x001F)
    Sleep(2000)

    TerminateThread(0x0008, 0xFF)

    @scena.Lambda('lambda_437B')
    def lambda_437B():
        ChrWalkTo(0x00FE, -64920, 1000, 6590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_437B)

    TerminateThread(0x0009, 0xFF)

    @scena.Lambda('lambda_439A')
    def lambda_439A():
        ChrWalkTo(0x00FE, -66080, 1000, 6450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_439A)

    WaitForThreadExit(0x0008, 0x0002)
    SetChrDirection(0x0008, 270, 400)
    WaitForThreadExit(0x0009, 0x0002)
    SetChrDirection(0x0009, 270, 400)
    WaitForThreadExit(0x0027, 0x0001)

    ChrTalk(
        0x002B,
        (
            '#0400060801V#771F#4P科洛丝姐姐！\n',
            '你的奥斯卡演得很帅哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060802V那样才叫男人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x002B, 0)

    ChrTalk(
        0x0105,
        (
            '#0060060803V#041F呵呵，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x002A, 0x0001)

    ChrTalk(
        0x002A,
        (
            '#0410060804V#6P艾丝蒂尔姐姐\n',
            '也演得好棒呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#0410060805V#6P啊啊，尤利乌斯大人～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060806V#008F那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0430060807V#3P约修亚哥哥☆\n',
            '也很可爱哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0420060808V#3P嗯㈱\n',
            '我都看得入迷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060809V#019F啊、啊哈哈……谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    WaitForThreadExit(0x0028, 0x0001)

    ChrTalk(
        0x0028,
        (
            '#0390060810V#750F呵呵，\n',
            '大家都很高兴呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060811V既要在爱情和友情之间作抉择，\n',
            '又要稳稳屹立于时代洪流中，\n',
            '这就是剧里描绘出的主人公们啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060812V在扣人心弦的决斗后\n',
            '等待着他们的悲伤考验……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060813V还有最终温馨的大团圆结局……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060814V#751F真的是精彩绝伦的舞台剧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060815V#641F哎呀～能听到您这么说，\n',
            '我们的努力也没有白费了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060816V#644F啊，对了……汉斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0520060817V#730F#6P嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060818V#501F#5P哎呀，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0510060819V#648F忽然想起件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060820V我们等一下就回来，\n',
            '你们先慢慢聊一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060821V#505F#5P嗯、嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_477A')
    def lambda_477A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_477A')

    DispatchAsync2(0x0028, 0x0001, lambda_477A)

    @scena.Lambda('lambda_478B')
    def lambda_478B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_478B')

    DispatchAsync2(0x0101, 0x0001, lambda_478B)

    @scena.Lambda('lambda_479C')
    def lambda_479C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_479C')

    DispatchAsync2(0x0102, 0x0001, lambda_479C)

    @scena.Lambda('lambda_47AD')
    def lambda_47AD():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47AD')

    DispatchAsync2(0x0105, 0x0001, lambda_47AD)

    SetChrDirection(0x0008, 90, 400)

    @scena.Lambda('lambda_47C5')
    def lambda_47C5():
        ChrWalkTo(0x00FE, -61630, 1000, 6460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_47C5)

    Sleep(500)

    @scena.Lambda('lambda_47E5')
    def lambda_47E5():
        ChrWalkTo(0x00FE, -61630, 1000, 6460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_47E5)

    WaitForThreadExit(0x0008, 0x0002)
    SetChrFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0009, 0x0002)
    SetChrFlags(0x0009, 0x0080)
    Sleep(500)

    ChrWalkTo(0x0028, -66010, 1000, 7940, 2000, 0x00)

    ChrTalk(
        0x0028,
        (
            '#0390060822V#750F刚才那两个学生\n',
            '是叫乔儿和汉斯吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060823V我记得是科洛丝的朋友，\n',
            '好像还是学生会的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0028, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)

    @scena.Lambda('lambda_48A6')
    def lambda_48A6():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_48A6)

    @scena.Lambda('lambda_48B4')
    def lambda_48B4():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_48B4)

    ChrTurnDirection(0x0105, 0x0028, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060824V#040F是的，这次的舞台剧\n',
            '是由他们负责导演和组织的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060825V#750F是吗……那得谢谢他们呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060826V#754F这一定会成为\n',
            '我们在卢安的美好回忆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060827V#043F老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060828V#013F这些孩子还……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0028, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0028,
        (
            '#0390060829V#750F嗯……\n',
            '等回到玛诺利亚村后就告诉他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060830V然后，如果快的话，\n',
            '或许明天就会起程了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060831V#004F那、那么快！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x002B, 0x0028, 400)

    ChrTalk(
        0x002B,
        (
            '#0400060832V#770F#2P什么什么，你们在说什么～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4A6C')
    def lambda_4A6C():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0029, 0x0002, lambda_4A6C)

    @scena.Lambda('lambda_4A7A')
    def lambda_4A7A():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0027, 0x0002, lambda_4A7A)

    ChrTurnDirection(0x002A, 0x002B, 400)

    ChrTalk(
        0x002A,
        (
            '#0410060833V没礼貌哦，克拉姆！\n',
            '大人说话时别乱插嘴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060834V#751F没关系，玛丽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060835V好了，孩子们。\n',
            '我们早点回去旅馆吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060836V#750F吃完晚饭……\n',
            '然后再告诉你们好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002B,
        (
            '#0400060837V#774F#2P嗯、嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060838V#750F那么科洛丝……\n',
            '还有艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060839V我们差不多该告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060840V#751F今天真是感谢你们。\n',
            '让我们看了那么精彩的演出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060841V#003F啊，再等等吧。\n',
            '乔儿他们很快就会回来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#0530060842V#1P……打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4C45')
    def lambda_4C45():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_4C45)

    @scena.Lambda('lambda_4C53')
    def lambda_4C53():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C53)

    @scena.Lambda('lambda_4C61')
    def lambda_4C61():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4C61)

    @scena.Lambda('lambda_4C6F')
    def lambda_4C6F():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4C6F)

    ClearChrFlags(0x002C, 0x0080)
    SetChrFlags(0x002C, 0x0004)
    ChrWalkTo(0x002C, -66120, 0, 3810, 2000, 0x00)

    @scena.Lambda('lambda_4C9B')
    def lambda_4C9B():
        ChrTurnDirection(0x00FE, 0x002C, 0)
        Yield()

        Jump('lambda_4C9B')

    DispatchAsync2(0x0028, 0x0001, lambda_4C9B)

    @scena.Lambda('lambda_4CAC')
    def lambda_4CAC():
        ChrTurnDirection(0x00FE, 0x002C, 0)
        Yield()

        Jump('lambda_4CAC')

    DispatchAsync2(0x0101, 0x0001, lambda_4CAC)

    @scena.Lambda('lambda_4CBD')
    def lambda_4CBD():
        ChrTurnDirection(0x00FE, 0x002C, 0)
        Yield()

        Jump('lambda_4CBD')

    DispatchAsync2(0x0102, 0x0001, lambda_4CBD)

    @scena.Lambda('lambda_4CCE')
    def lambda_4CCE():
        ChrTurnDirection(0x00FE, 0x002C, 0)
        Yield()

        Jump('lambda_4CCE')

    DispatchAsync2(0x0105, 0x0001, lambda_4CCE)

    @scena.Lambda('lambda_4CDF')
    def lambda_4CDF():
        ChrTurnDirection(0x00FE, 0x002C, 0)
        Yield()

        Jump('lambda_4CDF')

    DispatchAsync2(0x002A, 0x0001, lambda_4CDF)

    @scena.Lambda('lambda_4CF0')
    def lambda_4CF0():
        ChrTurnDirection(0x00FE, 0x002C, 0)
        Yield()

        Jump('lambda_4CF0')

    DispatchAsync2(0x0029, 0x0001, lambda_4CF0)

    @scena.Lambda('lambda_4D01')
    def lambda_4D01():
        ChrTurnDirection(0x00FE, 0x002C, 0)
        Yield()

        Jump('lambda_4D01')

    DispatchAsync2(0x0027, 0x0001, lambda_4D01)

    ClearChrFlags(0x002C, 0x0004)
    ChrWalkTo(0x002C, -68130, 0, 4400, 2000, 0x00)
    CreateThread(0x0008, 0x01, 0x00, 0x0024)
    CreateThread(0x0009, 0x01, 0x00, 0x0025)
    ChrWalkTo(0x002C, -67960, 1000, 7780, 2000, 0x00)
    ChrWalkTo(0x002C, -67210, 1000, 7860, 2000, 0x00)

    ChrTalk(
        0x0028,
        (
            '#0390060843V#753F#2P啊，科林兹校长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#0530060844V#780F好久不见了，特蕾莎院长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060845V难得你来学院一趟，\n',
            '我却到现在才来跟你打招呼，真是抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060846V#750F#2P校长您太客气了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060847V#751F能让我们来参加学园祭，\n',
            '我们已经很高兴了，真的非常感谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#0530060848V#780F呵呵，能得到这样的评价，\n',
            '学生们的努力也算有了回报啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060849V……你们的情况我听科洛丝说了。\n',
            '真的是非常不幸的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060850V所以，通过这次学园祭，\n',
            '我们也想略尽绵薄之力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060851V#753F#2P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#0530060852V#781F乔儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060853V#644F是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -66010, 1000, 7160, 1000, 0x00)
    TerminateThread(0x0028, 0xFF)

    @scena.Lambda('lambda_4F80')
    def lambda_4F80():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_4F80)

    @scena.Lambda('lambda_4F8E')
    def lambda_4F8E():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4F8E)

    @scena.Lambda('lambda_4F9C')
    def lambda_4F9C():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4F9C)

    @scena.Lambda('lambda_4FAA')
    def lambda_4FAA():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4FAA)

    @scena.Lambda('lambda_4FB8')
    def lambda_4FB8():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_4FB8)

    @scena.Lambda('lambda_4FC6')
    def lambda_4FC6():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4FC6)

    @scena.Lambda('lambda_4FD4')
    def lambda_4FD4():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_4FD4)

    @scena.Lambda('lambda_4FE2')
    def lambda_4FE2():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_4FE2)

    @scena.Lambda('lambda_4FF0')
    def lambda_4FF0():
        ChrTurnDirection(0x00FE, 0x0028, 400)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_4FF0)

    ChrTurnDirection(0x0028, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0510060854V#640F请收下这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '乔儿将一个印有王立学院徽章的厚厚信封\n',
            '交给了特蕾莎院长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0008, -66060, 1000, 6740, 1000, 0x00)

    ChrTalk(
        0x0028,
        (
            '#0390060855V#753F#1P这是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060856V#640F这是从来访者筹集得来的捐款，\n',
            '正好一百万米拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060857V请用来重建孤儿院吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0028, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010060858V#004F一、一百万米拉！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060859V#014F好大的数目……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060860V#756F#1P怎、怎么会有这么多……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#0530060861V#781F因为这次有公爵和柏斯市长\n',
            '等等悉数名人到场参加学园祭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060862V所以比往年筹到的都要多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060863V#048F校长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0028, 0x002C, 400)

    ChrTalk(
        0x0028,
        (
            '#0390060864V#755F#2P这、这怎么行！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060865V这钱我绝不能收！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060866V#730F不必客气啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060867V每年学园祭筹集到的捐款\n',
            '都是用于福利活动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060868V#641F如果是用于孤儿院的重建，\n',
            '捐款的各位也一定会很乐意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060869V#757F#2P但是……这……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060870V大家实在为我们做了太多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060871V#049F老师……\n',
            '就请您收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0028, 0xFF)
    ChrTurnDirection(0x0028, 0x0105, 400)

    ChrTalk(
        0x0028,
        (
            '#0390060872V#756F#3P科洛丝……可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060873V#049F老师踌躇的心情我很明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060874V#047F但是……\n',
            '请您仔细想一想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060875V有了这么一大笔钱\n',
            '不但可以重建孤儿院，\n',
            '大家也不需要长途跋涉去王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060876V#043F而且也不用\n',
            '扔下那块香草田……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '#0390060877V#757F#3P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#0530060878V#780F科洛丝说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060879V为了已故的约瑟夫，\n',
            '更重要的是为了孩子们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060880V您也应该抛下顾虑，\n',
            '接受这笔钱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0028, 0x002C, 400)
    Sleep(500)

    ChrTalk(
        0x0028,
        (
            '#0390060881V#754F#2P……啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060882V我……\n',
            '我该怎么感谢大家呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060883V#758F谢谢……\n',
            '真是太感谢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060884V#003F呜呜……太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060885V#019F嗯，这样事情终于完满解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002B,
        (
            '#0400060886V#775F#2P喂、喂……\n',
            '去王都是什么意思啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060887V到底怎么回事嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0028, 0x002B, 400)

    ChrTalk(
        0x0028,
        (
            '#0390060888V#758F#3P没事了……\n',
            '已经用不着担心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060889V孩子们……\n',
            '真是让你们受苦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002B,
        (
            '#0400060890V#775F#2P我、我们并不觉得\n',
            '受了什么苦啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060891V还、还有老师……\n',
            '你为什么要哭嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x002A, 0x002B, 400)

    ChrTalk(
        0x002A,
        (
            '#0410060892V克拉姆真是笨蛋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#0410060893V当然是因为太过高兴，\n',
            '高兴而哭了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '特蕾莎院长和孩子们起程回玛诺利亚之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚还有其他学生\n',
            '就开始了学园祭的收拾工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当所有工作都已经整理完毕的时候，\n',
            '天色已经是黄昏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T2500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x584D
@scena.Code('func_1F_584D')
def func_1F_584D():
    Sleep(2000)

    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -66120, 0, 3810, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -68130, 0, 4400, 2000, 0x00)
    ChrWalkTo(0x00FE, -67960, 1000, 7780, 2000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0020 offset: 0x58A5
@scena.Code('func_20_58A5')
def func_20_58A5():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -66120, 0, 3810, 4000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -68130, 0, 4400, 4000, 0x00)
    ChrWalkTo(0x00FE, -67960, 1000, 7780, 4000, 0x00)
    ChrWalkTo(0x00FE, -64800, 1000, 8250, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0105, 0)

    Return()

# id: 0x0021 offset: 0x590C
@scena.Code('func_21_590C')
def func_21_590C():
    Sleep(500)

    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -66120, 0, 3810, 4000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -68130, 0, 4400, 4000, 0x00)
    ChrWalkTo(0x00FE, -67960, 1000, 7780, 4000, 0x00)
    ChrWalkTo(0x00FE, -64810, 1000, 9040, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0022 offset: 0x5978
@scena.Code('func_22_5978')
def func_22_5978():
    Sleep(1500)

    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -66120, 0, 3810, 4000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -68130, 0, 4400, 4000, 0x00)
    ChrWalkTo(0x00FE, -67960, 1000, 7780, 4000, 0x00)
    ChrWalkTo(0x00FE, -65990, 1000, 9560, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0102, 400)

    Return()

# id: 0x0023 offset: 0x59E4
@scena.Code('func_23_59E4')
def func_23_59E4():
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -66120, 0, 3810, 4000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -68130, 0, 4400, 4000, 0x00)
    ChrWalkTo(0x00FE, -67960, 1000, 7780, 4000, 0x00)
    ChrWalkTo(0x00FE, -65510, 1000, 9200, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0102, 400)

    Return()

# id: 0x0024 offset: 0x5A50
@scena.Code('func_24_5A50')
def func_24_5A50():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -66080, 1000, 6450, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)

    Return()

# id: 0x0025 offset: 0x5A71
@scena.Code('func_25_5A71')
def func_25_5A71():
    Sleep(700)

    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -64920, 1000, 6590, 2000, 0x00)
    SetChrDirection(0x00FE, 315, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
