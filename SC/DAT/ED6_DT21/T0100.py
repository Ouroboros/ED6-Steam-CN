import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵'),
    TXT(0x02, '士兵'),
    TXT(0x03, '爱娜'),
    TXT(0x04, '佛莱迪'),
    TXT(0x05, '梅尔达斯'),
    TXT(0x06, '里农'),
    TXT(0x07, '鲁克'),
    TXT(0x08, '帕特'),
    TXT(0x09, '克露莎'),
    TXT(0x0A, '胡里奥'),
    TXT(0x0B, '艾娅莉'),
    TXT(0x0C, '阿鲁姆'),
    TXT(0x0D, '提克'),
    TXT(0x0E, '莫莉'),
    TXT(0x0F, '利吉'),
    TXT(0x10, '商人'),
    TXT(0x11, '旅行者'),
    TXT(0x12, '旅行者'),
    TXT(0x13, '鸽子'),
    TXT(0x14, '鸽子'),
    TXT(0x15, '鸽子'),
    TXT(0x16, '鸽子'),
    TXT(0x17, '鸽子'),
    TXT(0x18, '士兵斯科特'),
    TXT(0x19, '士兵哈罗德'),
    TXT(0x1A, '士兵拉科斯'),
    TXT(0x1B, '士兵霍帕'),
    TXT(0x1C, '士兵安托斯'),
    TXT(0x1D, '士兵多明戈'),
    TXT(0x1E, '士兵迈尔斯'),
    TXT(0x1F, '士兵马克斯'),
    TXT(0x20, '戴恩副队长'),
    TXT(0x21, '阿斯顿队长'),
    TXT(0x22, '基蒂'),
    TXT(0x23, '安敦'),
    TXT(0x24, '利库斯'),
    TXT(0x25, '迪拜恩教区长'),
    TXT(0x26, '修女梅'),
    TXT(0x27, '伴娘'),
    TXT(0x28, '布露姆老奶奶'),
    TXT(0x29, '亚尔丽 '),
    TXT(0x2A, '赛拉'),
    TXT(0x2B, '托露塔'),
    TXT(0x2C, '伊娜'),
    TXT(0x2D, '安莉尔'),
    TXT(0x2E, '年轻的女性'),
    TXT(0x2F, '临时演员'),
    TXT(0x30, '年轻的女性'),
    TXT(0x31, '临时演员'),
    TXT(0x32, '临时演员'),
    TXT(0x33, '新郎的亲属'),
    TXT(0x34, '新郎的亲属'),
    TXT(0x35, '新郎的亲属'),
    TXT(0x36, '新娘的亲属'),
    TXT(0x37, '新娘的亲属'),
    TXT(0x38, '新娘的亲属'),
    TXT(0x39, '新娘的朋友'),
    TXT(0x3A, '新娘的朋友'),
    TXT(0x3B, '捧花'),
    TXT(0x3C, '小猫'),
    TXT(0x3D, '小猫'),
    TXT(0x3E, '小猫'),
    TXT(0x3F, '菲特 '),
    TXT(0x40, '林德号的乘客'),
    TXT(0x41, '林德号的乘客'),
    TXT(0x42, '洛连特·市长官邸'),
    TXT(0x43, '洛连特飞船坪'),
    TXT(0x44, '艾利兹街道方向'),
    TXT(0x45, '米尔西街道方向'),
    TXT(0x46, '玛鲁加山道方向'),
    TXT(0x47, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'rolent'
    header.mapModel       = 'T0100.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xBFA1
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH02560._CH', 'ED6_DT07/CH02560P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01731._CH', 'ED6_DT07/CH01731P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT26/CH20247._CH', 'ED6_DT26/CH20247P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT27/CH03880._CH', 'ED6_DT27/CH03880P._CP'),
        ('ED6_DT27/CH03881._CH', 'ED6_DT27/CH03881P._CP'),
        ('ED6_DT27/CH03882._CH', 'ED6_DT27/CH03882P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
    ]

# id: 0x10002 offset: 0x1EA
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
            x                   = 49120,
            z                   = 0,
            y                   = 48300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 49870,
            z                   = 0,
            y                   = 50090,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 30420,
            z                   = 0,
            y                   = 40090,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 51830,
            z                   = 0,
            y                   = 35210,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 32700,
            z                   = 3250,
            y                   = 33000,
            direction           = 180,
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
            x                   = 31830,
            z                   = 3250,
            y                   = 33000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 61150,
            z                   = 0,
            y                   = 39190,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 60650,
            z                   = 0,
            y                   = 38310,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = 59490,
            z                   = 0,
            y                   = 44360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 60290,
            z                   = 0,
            y                   = 42390,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 60630,
            z                   = 0,
            y                   = 41060,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = 59130,
            z                   = 0,
            y                   = 41140,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 19740,
            z                   = 0,
            y                   = 42720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = 19740,
            z                   = 0,
            y                   = 38120,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 46620,
            z                   = 0,
            y                   = 12050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            x                   = 51800,
            z                   = 0,
            y                   = 12050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            x                   = 26440,
            z                   = 0,
            y                   = 70940,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            x                   = 29720,
            z                   = 0,
            y                   = 70940,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            x                   = 57650,
            z                   = 0,
            y                   = 70870,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            x                   = 40910,
            z                   = 0,
            y                   = 14450,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            x                   = 51560,
            z                   = 0,
            y                   = 45820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 51560,
            z                   = 0,
            y                   = 47080,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = 46300,
            z                   = 0,
            y                   = -1110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            x                   = 57080,
            z                   = 0,
            y                   = 36580,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            x                   = 55920,
            z                   = 0,
            y                   = 37500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002E,
        ),
        ScenaNpcData(
            x                   = 72900,
            z                   = 500,
            y                   = 33000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 72900,
            z                   = 500,
            y                   = 33000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 76000,
            z                   = 0,
            y                   = 34520,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 75940,
            z                   = 0,
            y                   = 36060,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 74350,
            z                   = 0,
            y                   = 41130,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 75990,
            z                   = 0,
            y                   = 37150,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 70250,
            z                   = 0,
            y                   = 36610,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 72180,
            z                   = 0,
            y                   = 42370,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            x                   = 70420,
            z                   = 0,
            y                   = 41930,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            x                   = 71520,
            z                   = 0,
            y                   = 41600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 70380,
            z                   = 0,
            y                   = 39760,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 73420,
            z                   = 0,
            y                   = 41930,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 75970,
            z                   = 0,
            y                   = 40020,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 70410,
            z                   = 0,
            y                   = 40770,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 75100,
            z                   = 0,
            y                   = 36700,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 75180,
            z                   = 0,
            y                   = 37580,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 75230,
            z                   = 0,
            y                   = 38600,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 70630,
            z                   = 0,
            y                   = 35600,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 70920,
            z                   = 0,
            y                   = 37110,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 70880,
            z                   = 0,
            y                   = 38120,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 74610,
            z                   = 0,
            y                   = 42650,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 71320,
            z                   = 0,
            y                   = 42840,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 72450,
            z                   = 1000,
            y                   = 34820,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x01E4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39440,
            z                   = 0,
            y                   = 52410,
            direction           = 43,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 43700,
            z                   = 0,
            y                   = 48980,
            direction           = 44,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 44050,
            z                   = 0,
            y                   = 52220,
            direction           = 337,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 45320,
            z                   = 0,
            y                   = 19750,
            direction           = 268,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x004E,
        ),
        ScenaNpcData(
            x                   = 39240,
            z                   = 3250,
            y                   = 34030,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x004F,
        ),
        ScenaNpcData(
            x                   = 37550,
            z                   = 3250,
            y                   = 34980,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0050,
        ),
        ScenaNpcData(
            x                   = 90860,
            z                   = 0,
            y                   = 40240,
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
            x                   = 49150,
            z                   = 0,
            y                   = 95090,
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
            x                   = 48960,
            z                   = 0,
            y                   = 1120,
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
            x                   = 5400,
            z                   = 0,
            y                   = 39830,
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
            x                   = 28060,
            z                   = 0,
            y                   = 80870,
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

# id: 0x10003 offset: 0xAAA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xAAA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 44000,
            y           = 0,
            z           = 12250,
            range       = 54000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00002710,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000056,
        ),
        ScenaEventData(
            x           = 18000,
            y           = 0,
            z           = 44000,
            range       = 19000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00009088,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000055,
        ),
        ScenaEventData(
            x           = 26300,
            y           = 0,
            z           = 72000,
            range       = 29700,
            dword_10    = 0x000003E8,
            dword_14    = 0x0001142C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000054,
        ),
        ScenaEventData(
            x           = 52800,
            y           = 0,
            z           = 18950,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000005C,
        ),
        ScenaEventData(
            x           = 52800,
            y           = 0,
            z           = 29050,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000005D,
        ),
        ScenaEventData(
            x           = 44700,
            y           = 0,
            z           = 33020,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000005E,
        ),
        ScenaEventData(
            x           = 44700,
            y           = 0,
            z           = 21990,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000005F,
        ),
        ScenaEventData(
            x           = 30900,
            y           = 0,
            z           = 47270,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000060,
        ),
        ScenaEventData(
            x           = 34300,
            y           = 0,
            z           = 52980,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000060,
        ),
        ScenaEventData(
            x           = 66000,
            y           = 0,
            z           = 52470,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000061,
        ),
        ScenaEventData(
            x           = 73000,
            y           = 0,
            z           = 34550,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000062,
        ),
        ScenaEventData(
            x           = 54800,
            y           = 0,
            z           = 49170,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000063,
        ),
    )

# id: 0x10005 offset: 0xC2A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 55000,
            triggerZ            = 0,
            triggerY            = 45300,
            triggerRange        = 1700,
            actorX              = 55000,
            actorZ              = 2500,
            actorY              = 45300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0057,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 44710,
            triggerZ            = 0,
            triggerY            = 70740,
            triggerRange        = 1500,
            actorX              = 44710,
            actorZ              = 1800,
            actorY              = 70740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0058,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45280,
            triggerZ            = 0,
            triggerY            = 71310,
            triggerRange        = 1500,
            actorX              = 45280,
            actorZ              = 1800,
            actorY              = 71310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0059,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 61370,
            triggerZ            = 250,
            triggerY            = 19380,
            triggerRange        = 1000,
            actorX              = 61370,
            actorZ              = 1500,
            actorY              = 19380,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 76980,
            triggerZ            = 0,
            triggerY            = 19020,
            triggerRange        = 800,
            actorX              = 76980,
            actorZ              = 0,
            actorY              = 19020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xCDE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E2B',
    )

    ClearChrFlags(0x0047, 0x0080)
    ClearChrFlags(0x0048, 0x0080)
    SetChrPos(0x000E, 49900, 0, 72100, 0)
    SetChrPos(0x000F, 46900, 0, 74100, 0)
    CreateThread(0x000E, 0x02, 0x00, 0x000B)
    CreateThread(0x000F, 0x02, 0x00, 0x000C)
    CreateThread(0x000E, 0x01, 0x00, 0x0002)
    CreateThread(0x000F, 0x01, 0x00, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DA3',
    )

    SetChrPos(0x0033, 39880, 0, 53180, 125)
    SetChrFlags(0x0033, 0x0010)
    ClearChrFlags(0x0033, 0x0080)
    CreateThread(0x0033, 0x00, 0x00, 0x0002)
    SetChrPos(0x0034, 39880, 0, 53850, 125)
    ClearChrFlags(0x0034, 0x0080)
    CreateThread(0x0034, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    ClearChrFlags(0x0045, 0x0080)
    SetChrFlags(0x0044, 0x0040)
    SetChrFlags(0x0045, 0x0040)
    CreateThread(0x0044, 0x01, 0x00, 0x0009)
    CreateThread(0x0045, 0x01, 0x00, 0x0009)
    ClearChrFlags(0x0046, 0x0080)

    Jump('loc_E28')

    def _loc_DA3(): pass

    label('loc_DA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC2',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)

    Jump('loc_E28')

    def _loc_DC2(): pass

    label('loc_DC2')

    SetChrFlags(0x0011, 0x0080)
    SetChrPos(0x0033, 39880, 0, 53180, 125)
    ClearChrFlags(0x0033, 0x0080)
    CreateThread(0x0033, 0x00, 0x00, 0x0002)
    SetChrPos(0x0034, 39880, 0, 53850, 125)
    ClearChrFlags(0x0034, 0x0080)
    CreateThread(0x0034, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    ClearChrFlags(0x0045, 0x0080)
    SetChrFlags(0x0044, 0x0040)
    SetChrFlags(0x0045, 0x0040)
    CreateThread(0x0044, 0x01, 0x00, 0x0009)
    CreateThread(0x0045, 0x01, 0x00, 0x0009)

    def _loc_E28(): pass

    label('loc_E28')

    Jump('loc_1001')

    def _loc_E2B(): pass

    label('loc_E2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_EA0',
    )

    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0033, 39890, 0, 53530, 180)
    ClearChrFlags(0x0033, 0x0080)
    CreateThread(0x0033, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0034, 0x0080)
    SetChrPos(0x0034, 40130, 0, 52240, 0)
    CreateThread(0x0034, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    ClearChrFlags(0x0045, 0x0080)
    SetChrFlags(0x0044, 0x0040)
    SetChrFlags(0x0045, 0x0040)
    CreateThread(0x0044, 0x01, 0x00, 0x0009)
    CreateThread(0x0045, 0x01, 0x00, 0x0009)

    Jump('loc_1001')

    def _loc_EA0(): pass

    label('loc_EA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_F06',
    )

    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0028, 0x0080)
    SetChrPos(0x0028, 51560, 0, 47080, 270)

    Jump('loc_1001')

    def _loc_F06(): pass

    label('loc_F06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_F8F',
    )

    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    SetChrPos(0x0029, 45200, 0, 19640, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_F8C',
    )

    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)
    ClearChrFlags(0x0028, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0314, 0, 0x18A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F8C',
    )

    SetChrFlags(0x0028, 0x0010)
    SetChrFlags(0x0027, 0x0010)

    def _loc_F8C(): pass

    label('loc_F8C')

    Jump('loc_1001')

    def _loc_F8F(): pass

    label('loc_F8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_FF7',
    )

    ClearChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0033, 0x0010)
    SetChrFlags(0x0033, 0x0004)
    SetChrChipByIndex(0x0033, 31)
    SetChrPos(0x0033, 39420, 250, 51560, 315)
    ClearChrFlags(0x0034, 0x0080)
    SetChrPos(0x0034, 38700, 0, 50720, 315)
    CreateThread(0x0034, 0x00, 0x00, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FF4',
    )

    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    def _loc_FF4(): pass

    label('loc_FF4')

    Jump('loc_1001')

    def _loc_FF7(): pass

    label('loc_FF7')

    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0012, 0x0080)

    def _loc_1001(): pass

    label('loc_1001')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1012',
    )

    OP_A3(0x10F0)
    Event(0, 0x002F)

    Jump('loc_10C3')

    def _loc_1012(): pass

    label('loc_1012')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_102C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    Event(0, 0x0038)

    Jump('loc_10C3')

    def _loc_102C(): pass

    label('loc_102C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_1042',
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 0x003A)

    Jump('loc_10C3')

    def _loc_1042(): pass

    label('loc_1042')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_1061',
    )

    OP_A3(0x10F3)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0041)

    Jump('loc_10C3')

    def _loc_1061(): pass

    label('loc_1061')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10B4',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000077, 'loc_108D'),
        (0x00000078, 'loc_1099'),
        (0x00000079, 'loc_10A5'),
        (-1, 'loc_10B1'),
    )

    def _loc_108D(): pass

    label('loc_108D')

    SetMapFlags(0x10000000)
    Event(0, 0x0034)

    Jump('loc_10B1')

    def _loc_1099(): pass

    label('loc_1099')

    SetMapFlags(0x10000000)
    Event(0, 0x0035)

    Jump('loc_10B1')

    def _loc_10A5(): pass

    label('loc_10A5')

    SetMapFlags(0x10000000)
    Event(0, 0x0036)

    Jump('loc_10B1')

    def _loc_10B1(): pass

    label('loc_10B1')

    Jump('loc_10C3')

    def _loc_10B4(): pass

    label('loc_10B4')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_10C0'),
        (-1, 'loc_10C3'),
    )

    def _loc_10C0(): pass

    label('loc_10C0')

    Jump('loc_10C3')

    def _loc_10C3(): pass

    label('loc_10C3')

    Return()

# id: 0x0001 offset: 0x10C4
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEC780, 0xFFFEA840, 0x00230001)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10EE',
    )

    OP_B1('t0100_n')

    Jump('loc_112B')

    def _loc_10EE(): pass

    label('loc_10EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1122',
    )

    OP_B1('t0100_y')
    OP_11(0xDB, 0xB7, 0xFF, 0x00000000, 0x0000FF78, 0x00000000)

    Jump('loc_112B')

    def _loc_1122(): pass

    label('loc_1122')

    OP_B1('t0100_n')

    def _loc_112B(): pass

    label('loc_112B')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_116B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1156',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)

    Jump('loc_116B')

    def _loc_1156(): pass

    label('loc_1156')

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x00013880, 0x00000000)

    def _loc_116B(): pass

    label('loc_116B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1177',
    )

    OP_64(0x04, 0x0001)

    def _loc_1177(): pass

    label('loc_1177')

    OP_64(0x03, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_119B',
    )

    OP_65(0x03, 0x0001)

    def _loc_119B(): pass

    label('loc_119B')

    OP_71(0x002F, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11B1',
    )

    OP_72(0x002F, 0x0004)

    def _loc_11B1(): pass

    label('loc_11B1')

    Return()

# id: 0x0002 offset: 0x11B2
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
        'loc_11D7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_1319')

    def _loc_11D7(): pass

    label('loc_11D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11F0',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_1319')

    def _loc_11F0(): pass

    label('loc_11F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1209',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_1319')

    def _loc_1209(): pass

    label('loc_1209')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1222',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_1319')

    def _loc_1222(): pass

    label('loc_1222')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_123B',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_1319')

    def _loc_123B(): pass

    label('loc_123B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1254',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_1319')

    def _loc_1254(): pass

    label('loc_1254')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_126D',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_1319')

    def _loc_126D(): pass

    label('loc_126D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1286',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_1319')

    def _loc_1286(): pass

    label('loc_1286')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129F',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_1319')

    def _loc_129F(): pass

    label('loc_129F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12B8',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_1319')

    def _loc_12B8(): pass

    label('loc_12B8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12D1',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_1319')

    def _loc_12D1(): pass

    label('loc_12D1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12EA',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_1319')

    def _loc_12EA(): pass

    label('loc_12EA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1303',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_1319')

    def _loc_1303(): pass

    label('loc_1303')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1319',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_1319(): pass

    label('loc_1319')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_132E',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_1319')

    def _loc_132E(): pass

    label('loc_132E')

    Return()

# id: 0x0003 offset: 0x132F
@scena.Code('func_03_132F')
def func_03_132F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1353',
    )

    def _loc_1336(): pass

    label('loc_1336')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1350',
    )

    OP_93(0x00FE, 0x000E, 0x000004B0, 0x00001838, 0x00)

    Jump('loc_1336')

    def _loc_1350(): pass

    label('loc_1350')

    Jump('loc_13A5')

    def _loc_1353(): pass

    label('loc_1353')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_13A5',
    )

    OP_8D(0x00FE, 48000, 49500, 50500, 50500, 3000)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13A2',
    )

    ChrTurnDirection(0x00FE, 0x000E, 400)
    Sleep(400)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13A2(): pass

    label('loc_13A2')

    Jump('loc_1353')

    def _loc_13A5(): pass

    label('loc_13A5')

    Return()

# id: 0x0004 offset: 0x13A6
@scena.Code('func_04_13A6')
def func_04_13A6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1434',
    )

    def _loc_13AD(): pass

    label('loc_13AD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1431',
    )

    OP_8E(0x00FE, 48900, 0, 42400, 6000, 0x00)
    OP_8E(0x00FE, 58900, 0, 42400, 6000, 0x00)
    OP_8E(0x00FE, 58900, 0, 60000, 6000, 0x00)
    OP_8E(0x00FE, 57500, 0, 60000, 6000, 0x00)
    OP_8E(0x00FE, 57500, 0, 71100, 6000, 0x00)
    OP_8E(0x00FE, 48900, 0, 71100, 6000, 0x00)

    Jump('loc_13AD')

    def _loc_1431(): pass

    label('loc_1431')

    Jump('loc_1486')

    def _loc_1434(): pass

    label('loc_1434')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1486',
    )

    OP_8D(0x00FE, 48000, 49000, 50500, 48000, 3000)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1483',
    )

    ChrTurnDirection(0x00FE, 0x000F, 400)
    Sleep(400)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1483(): pass

    label('loc_1483')

    Jump('loc_1434')

    def _loc_1486(): pass

    label('loc_1486')

    Return()

# id: 0x0005 offset: 0x1487
@scena.Code('func_05_1487')
def func_05_1487():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_14AA',
    )

    OP_8D(0x00FE, 25948, 43568, 37838, 41060, 3000)

    Jump('func_05_1487')

    def _loc_14AA(): pass

    label('loc_14AA')

    Return()

# id: 0x0006 offset: 0x14AB
@scena.Code('func_06_14AB')
def func_06_14AB():
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
    OP_8D(0x00FE, 51380, 38050, 58760, 43900, 0)

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

    def _loc_14DF(): pass

    label('loc_14DF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_17F2',
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
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x25, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x25, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x25, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x25, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x1388),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x1388),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x1388),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x1388),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Or,
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_17BB',
    )

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1630',
    )

    Sleep(250)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1630',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1630',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1630',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1630',
    )

    Sleep(500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1630',
    )

    Sleep(500)

    def _loc_1630(): pass

    label('loc_1630')

    TerminateThread(0x00FE, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_166B',
    )

    @scena.Lambda('lambda_164F')
    def lambda_164F():
        OP_97(0x00FE, 0x0000D6D8, 0x0000B824, 0x00057E40, 0x00001B58, 0x0001)
        Yield()

        Jump('lambda_164F')

    DispatchAsync2(0x00FE, 0x0001, lambda_164F)

    Jump('loc_168A')

    def _loc_166B(): pass

    label('loc_166B')

    @scena.Lambda('lambda_1671')
    def lambda_1671():
        OP_97(0x00FE, 0x0000D6D8, 0x0000B824, 0xFFFA81C0, 0x00001B58, 0x0001)
        Yield()

        Jump('lambda_1671')

    DispatchAsync2(0x00FE, 0x0001, lambda_1671)

    def _loc_168A(): pass

    label('loc_168A')

    SetChrChipByIndex(0x00FE, 11)
    ClearChrFlags(0x00FE, 0x0400)
    SetChrFlags(0x00FE, 0x0004)
    def _loc_1699(): pass

    label('loc_1699')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_16D1',
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
        'loc_16C9',
    )

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

    Jump('loc_16D1')

    def _loc_16C9(): pass

    label('loc_16C9')

    Sleep(15)

    Jump('loc_1699')

    def _loc_16D1(): pass

    label('loc_16D1')

    SetChrFlags(0x00FE, 0x0080)
    TerminateThread(0x00FE, 0x01)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrPos(0x00FE, 55000, 0, 47140, 74)
    def _loc_16F0(): pass

    label('loc_16F0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_17B8',
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
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x25, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x25, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x25, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x25, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17B0',
    )

    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 12)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, 51380, 38050, 58760, 43900, 0)

    Jump('loc_17B8')

    def _loc_17B0(): pass

    label('loc_17B0')

    Sleep(500)

    Jump('loc_16F0')

    def _loc_17B8(): pass

    label('loc_17B8')

    Jump('loc_17EF')

    def _loc_17BB(): pass

    label('loc_17BB')

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
        'loc_17EF',
    )

    @scena.Lambda('lambda_17D7')
    def lambda_17D7():
        OP_8D(0x00FE, 51380, 38050, 58760, 43900, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_17D7)

    def _loc_17EF(): pass

    label('loc_17EF')

    Jump('loc_14DF')

    def _loc_17F2(): pass

    label('loc_17F2')

    Return()

# id: 0x0007 offset: 0x17F3
@scena.Code('func_07_17F3')
def func_07_17F3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1933',
    )

    OP_8E(0x00FE, 57650, 0, 70870, 2000, 0x00)
    OP_8E(0x00FE, 48510, 0, 70870, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(1500)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 48510, 0, 41230, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(1500)

    OP_8C(0x00FE, 90, 400)
    OP_8E(0x00FE, 64140, 0, 41230, 2000, 0x00)
    Sleep(1500)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 64140, 0, 18670, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(1500)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 64140, 0, 14570, 2000, 0x00)
    OP_8E(0x00FE, 50700, 0, 14570, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1500)

    OP_8C(0x00FE, 0, 400)
    OP_8E(0x00FE, 50700, 0, 41230, 2000, 0x00)
    OP_8E(0x00FE, 59060, 0, 41230, 2000, 0x00)
    OP_8E(0x00FE, 59060, 0, 51960, 2000, 0x00)
    OP_8E(0x00FE, 57650, 0, 51960, 2000, 0x00)

    Jump('func_07_17F3')

    def _loc_1933(): pass

    label('loc_1933')

    Return()

# id: 0x0008 offset: 0x1934
@scena.Code('func_08_1934')
def func_08_1934():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1A38',
    )

    OP_8E(0x00FE, 40910, 0, 14450, 2000, 0x00)
    OP_8E(0x00FE, 30240, 0, 14450, 2000, 0x00)
    OP_8E(0x00FE, 30240, 0, 40030, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(1500)

    OP_8C(0x00FE, 90, 400)
    OP_8E(0x00FE, 47460, 0, 40030, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1500)

    OP_8C(0x00FE, 0, 400)
    OP_8E(0x00FE, 47460, 0, 67980, 2000, 0x00)
    OP_8E(0x00FE, 28270, 0, 67980, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(1500)

    OP_8C(0x00FE, 90, 400)
    OP_8E(0x00FE, 47460, 0, 67980, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(1500)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 47460, 0, 14450, 2000, 0x00)
    Sleep(1500)

    OP_8C(0x00FE, 270, 400)

    Jump('func_08_1934')

    def _loc_1A38(): pass

    label('loc_1A38')

    Return()

# id: 0x0009 offset: 0x1A39
@scena.Code('func_09_1A39')
def func_09_1A39():
    ExecExpressionWithValue(
        0x00FE,
        0x2D,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x2E,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x2F,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x07,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x29,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1A70(): pass

    label('loc_1A70')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1A93',
    )

    OP_8D(0x00FE, 43070, 48140, 44730, 52710, 3000)

    Jump('loc_1A70')

    def _loc_1A93(): pass

    label('loc_1A93')

    Return()

# id: 0x000A offset: 0x1A94
@scena.Code('func_0A_1A94')
def func_0A_1A94():
    ExecExpressionWithValue(
        0x00FE,
        0x2D,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x2E,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x2F,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x07,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x29,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        'loc_1AF0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_1C32')

    def _loc_1AF0(): pass

    label('loc_1AF0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B09',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_1C32')

    def _loc_1B09(): pass

    label('loc_1B09')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B22',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_1C32')

    def _loc_1B22(): pass

    label('loc_1B22')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B3B',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_1C32')

    def _loc_1B3B(): pass

    label('loc_1B3B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B54',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_1C32')

    def _loc_1B54(): pass

    label('loc_1B54')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B6D',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_1C32')

    def _loc_1B6D(): pass

    label('loc_1B6D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B86',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_1C32')

    def _loc_1B86(): pass

    label('loc_1B86')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B9F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_1C32')

    def _loc_1B9F(): pass

    label('loc_1B9F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BB8',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_1C32')

    def _loc_1BB8(): pass

    label('loc_1BB8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BD1',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_1C32')

    def _loc_1BD1(): pass

    label('loc_1BD1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BEA',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_1C32')

    def _loc_1BEA(): pass

    label('loc_1BEA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C03',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_1C32')

    def _loc_1C03(): pass

    label('loc_1C03')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C1C',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_1C32')

    def _loc_1C1C(): pass

    label('loc_1C1C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C32',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_1C32(): pass

    label('loc_1C32')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1C47',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_1C32')

    def _loc_1C47(): pass

    label('loc_1C47')

    Return()

# id: 0x000B offset: 0x1C48
@scena.Code('func_0B_1C48')
def func_0B_1C48():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1CB3',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xD48),
            Expr.Add,
            (Expr.GetChrWork, 0xF, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xD48),
            Expr.Sub,
            (Expr.GetChrWork, 0xF, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xD48),
            Expr.Add,
            (Expr.GetChrWork, 0xF, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xD48),
            Expr.Sub,
            (Expr.GetChrWork, 0xF, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CA0',
    )

    Sleep(100)

    OP_4B(0x00FE, 0)

    Jump('loc_1CAB')

    def _loc_1CA0(): pass

    label('loc_1CA0')

    OP_4A(0x00FE, 0)
    ChrTurnDirection(0x00FE, 0x000F, 400)

    def _loc_1CAB(): pass

    label('loc_1CAB')

    Sleep(100)

    Jump('func_0B_1C48')

    def _loc_1CB3(): pass

    label('loc_1CB3')

    Return()

# id: 0x000C offset: 0x1CB4
@scena.Code('func_0C_1CB4')
def func_0C_1CB4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1CCC',
    )

    ChrTurnDirection(0x00FE, 0x000E, 0)
    Sleep(100)

    Jump('func_0C_1CB4')

    def _loc_1CCC(): pass

    label('loc_1CCC')

    Return()

# id: 0x000D offset: 0x1CCD
@scena.Code('func_0D_1CCD')
def func_0D_1CCD():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp...*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000E offset: 0x1D0F
@scena.Code('func_0E_1D0F')
def func_0E_1D0F():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chiiiirp!*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x000F offset: 0x1D58
@scena.Code('func_0F_1D58')
def func_0F_1D58():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chirp chirp*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0010 offset: 0x1DA3
@scena.Code('func_10_1DA3')
def func_10_1DA3():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp chiiirp chirp!*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0011 offset: 0x1DF1
@scena.Code('func_11_1DF1')
def func_11_1DF1():
    OP_4A(0x00FE, 255)
    TalkBegin(0x00FE)
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '*chirp?*',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    OP_4B(0x00FE, 255)

    Return()

# id: 0x0012 offset: 0x1E31
@scena.Code('func_12_1E31')
def func_12_1E31():
    TalkBegin(0x000E)
    OP_4A(0x00FE, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2057',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 0, 0x20A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E51',
    )

    OP_A2(0x0014)
    Call(0, 0x004D)

    Jump('loc_2054')

    def _loc_1E51(): pass

    label('loc_1E51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_2006',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_1EF4',
    )

    ChrTalk(
        0x000E,
        (
            '话说回来帕特的\n',
            '妈妈还真是过分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '刚才还硬把人家\n',
            '带去教会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然是第一次出席婚礼，\n',
            '感觉真是特别无聊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就算我长大了\n',
            '也绝对不做那种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0016)
    OP_A2(0x0015)

    Jump('loc_2003')

    def _loc_1EF4(): pass

    label('loc_1EF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FB5',
    )

    ChrTalk(
        0x000E,
        (
            '真是的……\n',
            '帕特的妈妈好过分哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '人家在这里玩，\n',
            '却硬给她拉去教会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结果一直坐着，\n',
            '还让人家老实点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉，大人还真是的，\n',
            '老是做那么无聊的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我长大以后\n',
            '绝对不要什么婚礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    Jump('loc_2003')

    def _loc_1FB5(): pass

    label('loc_1FB5')

    ChrTalk(
        0x000E,
        (
            '为什么连毫无关联的我们\n',
            '也得去参加婚礼啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是的……\n',
            '帕特的妈妈好过分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2003(): pass

    label('loc_2003')

    Jump('loc_2054')

    def _loc_2006(): pass

    label('loc_2006')

    ChrTalk(
        0x000E,
        (
            '外面的街道很危险，\n',
            '我们也明白啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉，虽然很可惜，\n',
            '今天还是在城里玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2054(): pass

    label('loc_2054')

    Jump('loc_27BC')

    def _loc_2057(): pass

    label('loc_2057')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_24DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 0, 0x1A68)),
            Expr.Return,
        ),
        'loc_20FE',
    )

    ChrTurnDirection(0x000E, 0x0101, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 3, 0x1883)),
            Expr.Return,
        ),
        'loc_20AD',
    )

    ChrTalk(
        0x000E,
        (
            '艾丝蒂尔！\n',
            '这次是真正的决斗了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '绝对不能忘了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20FB')

    def _loc_20AD(): pass

    label('loc_20AD')

    ChrTalk(
        0x000E,
        (
            '我也要苦练剑术\n',
            '当上游击士给你看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '艾丝蒂尔这种程度\n',
            '我马上就可以超越了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20FB(): pass

    label('loc_20FB')

    Jump('loc_24DB')

    def _loc_20FE(): pass

    label('loc_20FE')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000E, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000E,
        (
            '啊，艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哟嗬～～鲁克！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1025F太好了……\n',
            '看上去很有精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嘿嘿，已经全好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，醒过来\n',
            '还觉得有点遗憾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为睡着的时候，\n',
            '我一直做着超级棒的好梦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯……好梦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嘿嘿，我成为游击士后\n',
            '神勇威猛大活跃的梦喔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哼哼，简直是艾丝蒂尔\n',
            '想都想不到的活跃啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈，你可真单纯啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，想要梦想成真\n',
            '就要从现在开始努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '哼，艾丝蒂尔这水平\n',
            '我马上就可以超越了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 3, 0x1883)),
            Expr.Return,
        ),
        'loc_2480',
    )

    ChrTalk(
        0x000E,
        (
            '对了对了，艾丝蒂尔。\n',
            '关于决斗的约定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F啊～你还记着啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '约是约好了没错，\n',
            '……真的要来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不……\n',
            '今天还是算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这次的事也给\n',
            '艾丝蒂尔添了不少麻烦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，就特别放你一马吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F真是，嘴不饶人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F……不过，我知道了。\n',
            '以后有机会再决胜负吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '哦、你做好心理准备吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '鲁克大人华丽的剑术\n',
            '会把你彻底打垮！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F哼哼，好好\n',
            '努力修行吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要不然，可是会被我揍得惨兮兮哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嘿嘿，你才是呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24D8')

    def _loc_2480(): pass

    label('loc_2480')

    ChrTalk(
        0x0101,
        (
            '#1006F哼哼，好好\n',
            '努力修行吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '游击士的道路\n',
            '可没那么简单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嘿嘿，等着瞧吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24D8(): pass

    label('loc_24D8')

    OP_A2(0x1A68)
    def _loc_24DB(): pass

    label('loc_24DB')

    Jump('loc_27BC')

    def _loc_24DE(): pass

    label('loc_24DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_253B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 3, 0x1883)),
            Expr.Return,
        ),
        'loc_2534',
    )

    ChrTurnDirection(0x000E, 0x0101, 0)

    ChrTalk(
        0x000E,
        (
            '趁天亮\n',
            '赶快回家吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '绝对别忘了决斗哦！\n',
            '那是我们的约定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2538')

    def _loc_2534(): pass

    label('loc_2534')

    Call(0, 0x0014)

    def _loc_2538(): pass

    label('loc_2538')

    Jump('loc_27BC')

    def _loc_253B(): pass

    label('loc_253B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_27BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 0, 0x1028)),
            Expr.Return,
        ),
        'loc_2596',
    )

    ChrTalk(
        0x000E,
        (
            '好不容易……做的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F咦，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '……没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27BC')

    def _loc_2596(): pass

    label('loc_2596')

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(600)

    OP_63(0x000E)

    ChrTalk(
        0x000E,
        (
            '啊───！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这不是艾、艾丝蒂尔吗！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F鲁克，好久不见呢。\n',
            '还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '……哼哼哼哼哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '１００年没见了吧………\n',
            '现在就让你见识见识我的修行成果吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '艾丝蒂尔·布莱特，\n',
            '与本大人一决胜负！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F胜负……什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '还用问吗，决斗啦决斗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '话说在前头，\n',
            '我可不是以前的我了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……\n',
            '决斗还是下次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '………………啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '什、什么嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '才当了正游击士，\n',
            '胆子就没了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '……你是不是怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F你胡说什么。\n',
            '我和平时一样啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1028)

    def _loc_27BC(): pass

    label('loc_27BC')

    OP_4B(0x00FE, 255)
    TalkEnd(0x000E)

    Return()

# id: 0x0013 offset: 0x27C4
@scena.Code('func_13_27C4')
def func_13_27C4():
    TalkBegin(0x000F)
    OP_4A(0x00FE, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2901',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 0, 0x20A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27E4',
    )

    OP_A3(0x0014)
    Call(0, 0x004D)

    Jump('loc_28FE')

    def _loc_27E4(): pass

    label('loc_27E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_289B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2856',
    )

    ChrTalk(
        0x000F,
        (
            '刚才和妈妈一起\n',
            '出席了婚礼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '妈妈也真是的，\n',
            '硬把鲁克也拉了去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '鲁克真是\n',
            '有点可怜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_2898')

    def _loc_2856(): pass

    label('loc_2856')

    ChrTalk(
        0x000F,
        (
            '妈妈真是的，\n',
            '把鲁克也带去参加婚礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '鲁克真是\n',
            '有点可怜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2898(): pass

    label('loc_2898')

    Jump('loc_28FE')

    def _loc_289B(): pass

    label('loc_289B')

    ChrTalk(
        0x000F,
        (
            '其实我都想\n',
            '和鲁克一起玩的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是今天有要事\n',
            '不得不早点回去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉～婚礼什么的\n',
            '我也不想去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28FE(): pass

    label('loc_28FE')

    Jump('loc_2B3D')

    def _loc_2901(): pass

    label('loc_2901')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_29C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2959',
    )

    ChrTalk(
        0x000F,
        (
            '鲁克也真是的，\n',
            '从刚才起就一直在说做梦的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看来相当开心的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29C5')

    def _loc_2959(): pass

    label('loc_2959')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000F,
        (
            '啊，姐姐！\n',
            '鲁克完全没事了哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，他从刚刚开始\n',
            '就一直在说做梦的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看来相当开心的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_29C5(): pass

    label('loc_29C5')

    Jump('loc_2B3D')

    def _loc_29C8(): pass

    label('loc_29C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2A35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 3, 0x1883)),
            Expr.Return,
        ),
        'loc_2A2E',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000F,
        (
            '我会听姐姐的话，\n',
            '今天趁天还亮先回家去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '会顺便将鲁克也\n',
            '带走的，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A32')

    def _loc_2A2E(): pass

    label('loc_2A2E')

    Call(0, 0x0014)

    def _loc_2A32(): pass

    label('loc_2A32')

    Jump('loc_2B3D')

    def _loc_2A35(): pass

    label('loc_2A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_2B3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 1, 0x1029)),
            Expr.Return,
        ),
        'loc_2A96',
    )

    ChrTalk(
        0x000F,
        (
            '鲁克听说了姐姐你们的事迹，\n',
            '也开始学剑术了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他说一定要变得\n',
            '和姐姐一样强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B3D')

    def _loc_2A96(): pass

    label('loc_2A96')

    ChrTalk(
        0x000F,
        (
            '……艾丝蒂尔姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '你回来了，\n',
            '回来了呢！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '鲁克听说了姐姐你们的事迹，\n',
            '也开始学剑术了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '他说一定要变得\n',
            '和姐姐一样强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1029)

    def _loc_2B3D(): pass

    label('loc_2B3D')

    OP_4B(0x00FE, 255)
    TalkEnd(0x000F)

    Return()

# id: 0x0014 offset: 0x2B45
@scena.Code('func_14_2B45')
def func_14_2B45():
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)

    If(
        (
            (Expr.Eval, "OP_CD(0x000E)"),
            Expr.Return,
        ),
        'loc_2BAA',
    )

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x000E)

    ChrTalk(
        0x000E,
        (
            '啊～！？艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '艾丝蒂尔姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BFC')

    def _loc_2BAA(): pass

    label('loc_2BAA')

    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x000F)

    ChrTalk(
        0x000F,
        (
            '啊，艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '啊～回来啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BFC(): pass

    label('loc_2BFC')

    ChrTalk(
        0x0101,
        (
            '#1001F啊哈哈，\n',
            '不用那么大声啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1028F嗯……看来是\n',
            '非常想我了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '才、才没在等你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你突、突然出现\n',
            '稍微有点吃惊而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000E, 400)

    ChrTalk(
        0x000F,
        (
            '咦……可是……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '鲁克不是\n',
            '一直在等姐姐回来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000F, 400)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(1000)

    OP_63(0x000E)

    ChrTalk(
        0x000E,
        (
            '笨，笨蛋！\n',
            '我可没那么说过！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1012F哼哼，鲁克啊…\n',
            '偶尔还挺可爱的嘛⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1018F来，别害臊…\n',
            '对姐姐撒娇吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2D53')
    def lambda_2D53():
        ChrTurnDirection(0x000E, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2D53)

    Sleep(150)

    ChrTurnDirection(0x000F, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 0, 0x1028)),
            Expr.Return,
        ),
        'loc_2DD0',
    )

    ChrTalk(
        0x000E,
        (
            '别、别说得\n',
            '那么恶心啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话、话说回来\n',
            '可别说你忘了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '决斗吧！艾丝蒂尔。\n',
            '先和我决斗再说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E3B')

    def _loc_2DD0(): pass

    label('loc_2DD0')

    ChrTalk(
        0x000E,
        (
            '别、别说得\n',
            '那么恶心啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话、话说回来决胜负吧！\n',
            '和我一对一单挑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '决斗吧！艾丝蒂尔。\n',
            '可别吓得逃跑哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E3B(): pass

    label('loc_2E3B')

    ChrTalk(
        0x0101,
        (
            '#1007F啊、决斗……\n',
            '真是的，说什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没看见这么大雾吗？\n',
            '赶快回家啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '笨蛋，有雾正好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在雾中决斗\n',
            '简直酷毙了不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1009F说这种话\n',
            '就证明你还是个小鬼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '让别人担心\n',
            '可是一点都不酷哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那个翡翠之塔的事……\n',
            '难不成你就忘了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000E,
        (
            '呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '姐、姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1010F要想成为独当一面的男子汉，\n',
            '首先要做到不用别人担心哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '自己一个人都照顾不好，\n',
            '就别想照顾别人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1002F这种事……\n',
            '你们现在也该明白了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '让我看看你们\n',
            '稍微成熟的样子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '……切…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '知、知道啦。\n',
            '决斗就下次吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '抱歉哦，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '趁着天还没黑\n',
            '我们得先回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，赶快去吧。\n',
            '答应姐姐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '随便怎样都好啦，\n',
            '决斗的事可别忘了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F唉～好好好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '等到这阵雾散了\n',
            '随时奉陪啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '好，就这么说定啰！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)
    OP_A2(0x1883)

    Return()

# id: 0x0015 offset: 0x313C
@scena.Code('func_15_313C')
def func_15_313C():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_322E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_31A4',
    )

    ChrTalk(
        0x00FE,
        (
            '和女朋友一起去王都\n',
            '参观女王诞辰庆典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过被卷进那个\n',
            '政变，运气真够差的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322E')

    def _loc_31A4(): pass

    label('loc_31A4')

    ChrTalk(
        0x00FE,
        (
            '和女朋友一起去王都\n',
            '参观女王诞辰庆典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过居然遇到那个\n',
            '政变事件，运气真够差的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得的求婚也被\n',
            '冲进城里的亲卫队打乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_322E(): pass

    label('loc_322E')

    TalkEnd(0x0013)

    Return()

# id: 0x0016 offset: 0x3232
@scena.Code('func_16_3232')
def func_16_3232():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_328A',
    )

    ChrTalk(
        0x00FE,
        (
            '跟他的王都之旅\n',
            '确实非常棒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过像现在这样的\n',
            '平凡日子也很不错哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_328A(): pass

    label('loc_328A')

    TalkEnd(0x0012)

    Return()

# id: 0x0017 offset: 0x328E
@scena.Code('func_17_328E')
def func_17_328E():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_336C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3321',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然定期船停了，\n',
            '还是要做好出货的准备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得尽快做完工作，\n',
            '准备去礼拜堂才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为今天\n',
            '我被邀请参加婚礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_3369')

    def _loc_3321(): pass

    label('loc_3321')

    ChrTalk(
        0x00FE,
        (
            '早点弄完工作\n',
            '准备去礼拜堂才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为今天\n',
            '我被邀请参加婚礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3369(): pass

    label('loc_3369')

    Jump('loc_3927')

    def _loc_336C(): pass

    label('loc_336C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_3743',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 2, 0x1A62)),
            Expr.Return,
        ),
        'loc_3463',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33F0',
    )

    ChrTalk(
        0x00FE,
        (
            '雾也散了，\n',
            '总算能放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，接下来\n',
            '就要忙木材的出货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也得鼓起干劲\n',
            '努力工作才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3460')

    def _loc_33F0(): pass

    label('loc_33F0')

    ChrTalk(
        0x00FE,
        (
            '我也要学习岳父\n',
            '从现在开始努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船的航行也恢复了，\n',
            '要开始忙木材的出货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，你们也当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3460(): pass

    label('loc_3460')

    Jump('loc_3740')

    def _loc_3463(): pass

    label('loc_3463')

    ChrTalk(
        0x00FE,
        (
            '呀，游击士们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '托你们的福，岳父\n',
            '总算清醒过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F岳父是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1011F啊，是说拉欧爷爷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F爱娜说的对，\n',
            '看来大家都醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，岳父\n',
            '虽然还有点迷糊，\n',
            '但身体应该是没有问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有精神得想赶快工作，\n',
            '还把我赶出门呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F啊哈哈，那看来没问题了。',
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
        'loc_35B0',
    )

    ChrTalk(
        0x0105,
        (
            '#048F呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3639')

    def _loc_35B0(): pass

    label('loc_35B0')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35DA',
    )

    ChrTalk(
        0x0107,
        (
            '#061F嘿嘿……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3639')

    def _loc_35DA(): pass

    label('loc_35DA')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_360C',
    )

    ChrTalk(
        0x0106,
        (
            '#051F啊啊，看来可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3639')

    def _loc_360C(): pass

    label('loc_360C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3639',
    )

    ChrTalk(
        0x0108,
        (
            '#070F啊啊，不用担心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3639(): pass

    label('loc_3639')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '我还那么担心，真傻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我也得向岳父学习，\n',
            '增强体力才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船的航行也恢复了，\n',
            '要开始忙木材的出货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，请加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#525F别输给你岳父哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊，我会尽最大努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '你们也当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A62)
    OP_A2(0x0001)
    def _loc_3740(): pass

    label('loc_3740')

    Jump('loc_3927')

    def _loc_3743(): pass

    label('loc_3743')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_383B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_37AC',
    )

    ChrTalk(
        0x00FE,
        (
            '突然就起这么大的雾，\n',
            '感觉很不寻常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去森林巡视的时候，\n',
            '也要小心不要迷路啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3838')

    def _loc_37AC(): pass

    label('loc_37AC')

    ChrTalk(
        0x00FE,
        (
            '突然就起这么大的雾，\n',
            '感觉很不寻常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，大自然这东西\n',
            '就是这么反复无常，没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要应付好它就是\n',
            '我们经营林业之人的宿命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_3838(): pass

    label('loc_3838')

    Jump('loc_3927')

    def _loc_383B(): pass

    label('loc_383B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_3927',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_3899',
    )

    ChrTalk(
        0x00FE,
        (
            '砍伐结束之后，\n',
            '在日落前都要进行植树的工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天看来也会很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3927')

    def _loc_3899(): pass

    label('loc_3899')

    ChrTalk(
        0x00FE,
        (
            '接下来就要去神秘森林\n',
            '砍伐树木了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '树可是这片大地唯一\n',
            '能够再生的天然资源哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '培育森林，与森林一起生活──\n',
            '这就是真正的林业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_3927(): pass

    label('loc_3927')

    TalkEnd(0x0011)

    Return()

# id: 0x0018 offset: 0x392B
@scena.Code('func_18_392B')
def func_18_392B():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_3C9E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 6, 0x20A6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BA6',
    )

    OP_62(0x0010, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 5, 0x20A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A8A',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39E3',
    )

    ChrTurnDirection(0x0010, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '呀，还有雪拉小姐☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A20')

    def _loc_39E3(): pass

    label('loc_39E3')

    ChrTalk(
        0x0101,
        (
            '#1001F哟嗬～克露莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了呢。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A20(): pass

    label('loc_3A20')

    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '克露莎一直都很好哦。\n',
            '因为身体就是记者的资本啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，艾丝蒂尔你们似乎\n',
            '也相当活跃嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AAB')

    def _loc_3A8A(): pass

    label('loc_3A8A')

    ChrTalk(
        0x00FE,
        (
            '我都听说了哦。\n',
            '相当活跃嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3AAB(): pass

    label('loc_3AAB')

    ChrTalk(
        0x00FE,
        (
            '你们在玛鲁加矿山\n',
            '救了矿工们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F啊，你的消息还是那么灵通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F感觉上……\n',
            '比以前更加厉害了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们才刚刚回来\n',
            '就马上活跃起来，真有一套。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这个情况看来，连那个浮游岛的谜\n',
            '也能很快解开吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '克露莎，好期待哦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)
    OP_A2(0x20A6)

    Jump('loc_3C9B')

    def _loc_3BA6(): pass

    label('loc_3BA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C3F',
    )

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆他们的婚礼\n',
            '也没发生什么特别的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，即使是无聊的新闻\n',
            '也得拿去撑版面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这个意义上来说\n',
            '阿鲁姆还算是不错的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_3C9B')

    def _loc_3C3F(): pass

    label('loc_3C3F')

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆他们的婚礼\n',
            '也没发生什么特别的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，即使是无聊的新闻\n',
            '也得拿去撑版面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C9B(): pass

    label('loc_3C9B')

    Jump('loc_48ED')

    def _loc_3C9E(): pass

    label('loc_3C9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4096',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 5, 0x20A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F65',
    )

    OP_62(0x0010, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D4B',
    )

    ChrTurnDirection(0x0010, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '呀，还有雪拉小姐☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D88')

    def _loc_3D4B(): pass

    label('loc_3D4B')

    ChrTalk(
        0x0101,
        (
            '#1001F哟嗬～克露莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了呢。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D88(): pass

    label('loc_3D88')

    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '克露莎一直都很好哦。\n',
            '因为身体就是记者的资本啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E37',
    )

    ChrTalk(
        0x00FE,
        (
            '但是，这么有前途的年轻游击士\n',
            '同时出现３个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一定是为了那个吧。\n',
            '导力停止现象的调查？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E99')

    def _loc_3E37(): pass

    label('loc_3E37')

    ChrTalk(
        0x00FE,
        (
            '但是，这么有前途的年轻游击士\n',
            '两人一起回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一定是为了那个吧。\n',
            '导力停止现象的调查？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E99(): pass

    label('loc_3E99')

    ChrTalk(
        0x0101,
        (
            '#1007F嗯……你还是那么敏锐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F这么难的词\n',
            '你竟然也知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我采访过佛莱迪先生啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然浮游岛的事也很受瞩目，\n',
            '不过最热门话题还是这次异变嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '克露莎也打算\n',
            '跟踪报导哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)
    OP_A2(0x20A5)

    Jump('loc_4093')

    def _loc_3F65(): pass

    label('loc_3F65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_402F',
    )

    ChrTalk(
        0x00FE,
        (
            '谁说最热门话题\n',
            '是导力停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天预定去报道\n',
            '阿鲁姆和艾娅莉的婚礼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从相关人员那里拿到了请帖，\n',
            '克露莎正打算去采访呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不加入点地方性的话题，\n',
            '读者就不会有兴趣嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_4093')

    def _loc_402F(): pass

    label('loc_402F')

    ChrTalk(
        0x00FE,
        (
            '今天预定去报道\n',
            '阿鲁姆和艾娅莉的婚礼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从相关人员那里拿到了请帖，\n',
            '克露莎正打算去采访呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4093(): pass

    label('loc_4093')

    Jump('loc_48ED')

    def _loc_4096(): pass

    label('loc_4096')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_42C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 1, 0x1A61)),
            Expr.Return,
        ),
        'loc_4106',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然在这时候发生事件啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国主战派和情报部……\n',
            '还有空贼团呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～想不出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42BF')

    def _loc_4106(): pass

    label('loc_4106')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和雪拉小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们真的要离开洛连特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯嗯，很快就要走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F抱歉哦、克露莎。\n',
            '别的地方还有工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两人一起去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，一定发生了大事吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国主战派以互不侵犯条约掩人耳目，\n',
            '准备偷偷侵略的阴谋？\n',
            '还是情报部的余党？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，也有可能\n',
            '是空贼团的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，想不出来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1019F（这、这个小鬼\n',
            '的直觉还真是敏锐。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F（真是，不能小看啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A61)

    def _loc_42BF(): pass

    label('loc_42BF')

    Jump('loc_48ED')

    def _loc_42C2(): pass

    label('loc_42C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4698',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 1, 0x1899)),
            Expr.Return,
        ),
        'loc_4480',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_4334',
    )

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生不在城里，\n',
            '最近的话题好少哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有利吉先生一个人，\n',
            '实在是好无趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_447D')

    def _loc_4334(): pass

    label('loc_4334')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4393',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，你们俩也是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乘坐定期船\n',
            '中途停在这里被赶下来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43DE')

    def _loc_4393(): pass

    label('loc_4393')

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和雪拉小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们俩也是从定期船上\n',
            '中途被赶下来的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43DE(): pass

    label('loc_43DE')

    ChrTalk(
        0x0101,
        (
            '#1015F唔、嗯，是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F观察真的很敏锐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生不在\n',
            '话题也好少哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，你们俩要加油\n',
            '想办法热闹一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '克露莎很期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_447D(): pass

    label('loc_447D')

    Jump('loc_4695')

    def _loc_4480(): pass

    label('loc_4480')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊～艾丝蒂尔！\n',
            '还有雪拉小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F嗨～克露莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，乖乖的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，克露莎\n',
            '一直都是乖孩子呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '对了对了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说现在约修亚\n',
            '在单独行动哟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过根据克露莎的直觉\n',
            '这是假情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实是接受了协会的秘密指令\n',
            '与邪恶组织作战去了吧？',
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
            '#1019F（呼……\n',
            '　好、好厉害！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这才是最佳剧情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为约修亚\n',
            '根本不适合平凡的剧情嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '独自潜入\n',
            '邪恶组织基地的约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，克露莎都着迷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)
    OP_A2(0x1899)
    def _loc_4695(): pass

    label('loc_4695')

    Jump('loc_48ED')

    def _loc_4698(): pass

    label('loc_4698')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_48ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 2, 0x102A)),
            Expr.Return,
        ),
        'loc_473D',
    )

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，约修亚在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是说旁边这人是你新男朋友，\n',
            '你就把约修亚给甩了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1064F（……小妹妹，嘘……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48ED')

    def _loc_473D(): pass

    label('loc_473D')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊～是艾丝蒂尔！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F克露莎，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0142, 400)
    Sleep(600)

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你是谁啦～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1064F咦，说我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……破坏约修亚和艾丝蒂尔\n',
            '关系的神秘男人登场了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在克露莎不知道的情况下\n',
            '关系发展得如火如荼。\n',
            '这是绝对不允许的～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F我说……克露莎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，他一定会和约修亚\n',
            '作战，产生了友情\n',
            '最后却命丧黄泉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1061F好、好厉害的孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x102A)

    def _loc_48ED(): pass

    label('loc_48ED')

    TalkEnd(0x0010)

    Return()

# id: 0x0019 offset: 0x48F1
@scena.Code('func_19_48F1')
def func_19_48F1():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_4A16',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4950',
    )

    ChrTalk(
        0x00FE,
        (
            '这就是洛连特的钟楼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里是背负了沉重历史的\n',
            '百日战役的遗迹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A16')

    def _loc_4950(): pass

    label('loc_4950')

    ChrTalk(
        0x00FE,
        (
            '这就是洛连特的钟楼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说容易被错过，这里也是\n',
            '那个百日战役的遗迹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特攻防战中，这里\n',
            '被帝国军的炮弹直接击中了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说因此牺牲了很多不幸的市民，\n',
            '背负着沉重的历史啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_4A16(): pass

    label('loc_4A16')

    TalkEnd(0x0014)

    Return()

# id: 0x001A offset: 0x4A1A
@scena.Code('func_1A_4A1A')
def func_1A_4A1A():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_4B35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_4A80',
    )

    ChrTalk(
        0x00FE,
        (
            '终于雾散天晴了，\n',
            '可以尽情拍摄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先从洛连特的标志…\n',
            '这个钟楼开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B35')

    def _loc_4A80(): pass

    label('loc_4A80')

    ChrTalk(
        0x00FE,
        (
            '终于雾散天晴了，\n',
            '可以尽情拍摄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先从洛连特的标志…\n',
            '本打算从钟楼开始拍……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但听了这里的历史，\n',
            '都不敢随便按下快门了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从镜头里看过去\n',
            '感觉气氛也好严肃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_4B35(): pass

    label('loc_4B35')

    TalkEnd(0x0015)

    Return()

# id: 0x001B offset: 0x4B39
@scena.Code('func_1B_4B39')
def func_1B_4B39():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4E59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 0, 0x1880)),
            Expr.Return,
        ),
        'loc_4BC8',
    )

    ChrTalk(
        0x00FE,
        (
            '客人们请集中，\n',
            '我们打算出发去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就像雪拉前辈说的一样，\n',
            '现在能见度太差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也会十分小心地\n',
            '前去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E59')

    def _loc_4BC8(): pass

    label('loc_4BC8')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0103, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和雪拉前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哎呀，这不是利吉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F利吉先生，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔。\n',
            '出发去了训练场以后就没见到你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听爱娜小姐说了哦。\n',
            '你在做很重要的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '利吉先生也\n',
            '在工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，这边的客人们\n',
            '好像有急事要去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去今天\n',
            '定期船恐怕也没法航行了，\n',
            '所以要我送他们去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊～要去王都啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F由于起雾，道路上的视野很不好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F要比平常\n',
            '更加注意周围哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '是，我会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，前辈你们也\n',
            '请努力完成任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F利吉先生也是。\n',
            '护卫的工作请加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客人们我\n',
            '必定平安送到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1880)

    def _loc_4E59(): pass

    label('loc_4E59')

    TalkEnd(0x0016)

    Return()

# id: 0x001C offset: 0x4E5D
@scena.Code('func_1C_4E5D')
def func_1C_4E5D():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4ECB',
    )

    ChrTalk(
        0x00FE,
        (
            '据说在王都有重要的贸易谈判呢。\n',
            '无论如何也必须要去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是做大生意的机会，\n',
            '绝对不能错过的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4ECB(): pass

    label('loc_4ECB')

    TalkEnd(0x0017)

    Return()

# id: 0x001D offset: 0x4ECF
@scena.Code('func_1D_4ECF')
def func_1D_4ECF():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4F35',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，这种时候有游击士在\n',
            '真是令人安心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一个人在大雾里奔走\n',
            '实在连想都不敢想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F35(): pass

    label('loc_4F35')

    TalkEnd(0x0018)

    Return()

# id: 0x001E offset: 0x4F39
@scena.Code('func_1E_4F39')
def func_1E_4F39():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4F85',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到定期船\n',
            '会停航啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，不过有游击士\n',
            '护送就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F85(): pass

    label('loc_4F85')

    TalkEnd(0x0019)

    Return()

# id: 0x001F offset: 0x4F89
@scena.Code('func_1F_4F89')
def func_1F_4F89():
    TalkBegin(0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_50A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_501C',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才稍微看了一下\n',
            '偷溜出去的鲁克哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '意识还没恢复，\n',
            '但睡得很安稳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在为了那孩子\n',
            '我也必须完成自己的责任和义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_509E')

    def _loc_501C(): pass

    label('loc_501C')

    ChrTalk(
        0x00FE,
        (
            '现在还没什么问题，\n',
            '总之警备还算顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，只要这个状态持续，\n',
            '说不定还会发生事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家看来都\n',
            '不能放松警惕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_509E(): pass

    label('loc_509E')

    Jump('loc_5100')

    def _loc_50A1(): pass

    label('loc_50A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_5100',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0314, 0, 0x18A0)),
            Expr.Return,
        ),
        'loc_50FC',
    )

    ChrTalk(
        0x00FE,
        (
            '我们\n',
            '已经开始警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这边就交给我们吧。\n',
            '协会的工作就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5100')

    def _loc_50FC(): pass

    label('loc_50FC')

    Call(0, 0x0021)

    def _loc_5100(): pass

    label('loc_5100')

    TalkEnd(0x0028)

    Return()

# id: 0x0020 offset: 0x5104
@scena.Code('func_20_5104')
def func_20_5104():
    TalkBegin(0x0027)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_5163',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0314, 0, 0x18A0)),
            Expr.Return,
        ),
        'loc_515F',
    )

    ChrTalk(
        0x00FE,
        (
            '总之先开始警备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，应该会有些问题\n',
            '不过一定能慢慢解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5163')

    def _loc_515F(): pass

    label('loc_515F')

    Call(0, 0x0021)

    def _loc_5163(): pass

    label('loc_5163')

    TalkEnd(0x0027)

    Return()

# id: 0x0021 offset: 0x5167
@scena.Code('func_21_5167')
def func_21_5167():
    OP_4A(0x0028, 255)
    OP_4A(0x0027, 255)
    ClearChrFlags(0x0028, 0x0010)
    ClearChrFlags(0x0027, 0x0010)

    ChrTalk(
        0x0028,
        (
            '……对了戴恩副队长。\n',
            '西门的配置完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '……啊，那个地方\n',
            '安排了两个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '不过视情况\n',
            '应该得考虑增员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '原来如此……\n',
            '好，那么接下来是定期报告……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0028, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0028)

    @scena.Lambda('lambda_523F')
    def lambda_523F():
        ChrTurnDirection(0x0028, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_523F)

    Sleep(150)

    ChrTurnDirection(0x0027, 0x0101, 400)

    ChrTalk(
        0x0028,
        (
            '噢，艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '我们\n',
            '已经开始警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '这边就交给我们吧。\n',
            '协会的工作就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯！警备就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0028, 0x0027, 0)
    ChrTurnDirection(0x0027, 0x0028, 0)
    OP_4B(0x0028, 255)
    OP_4B(0x0027, 255)
    OP_A2(0x18A0)

    Return()

# id: 0x0022 offset: 0x52EB
@scena.Code('func_22_52EB')
def func_22_52EB():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_53AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_535D',
    )

    ChrTalk(
        0x00FE,
        (
            '感觉市民们都在看着\n',
            '一刻也不敢松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽说想想也不会有人\n',
            '有兴趣在雾中盯着士兵看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53A9')

    def _loc_535D(): pass

    label('loc_535D')

    ChrTalk(
        0x00FE,
        (
            '但是感觉市民们都在看着，\n',
            '一刻也不敢松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '却连个哈欠也不敢打。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_53A9(): pass

    label('loc_53A9')

    Jump('loc_5405')

    def _loc_53AC(): pass

    label('loc_53AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_5405',
    )

    ChrTalk(
        0x00FE,
        (
            '离开威尔特桥，\n',
            '这可是第一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，呼……\n',
            '这种紧张感果然还是不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5405(): pass

    label('loc_5405')

    TalkEnd(0x001F)

    Return()

# id: 0x0023 offset: 0x5409
@scena.Code('func_23_5409')
def func_23_5409():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5505',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_547B',
    )

    ChrTalk(
        0x00FE,
        (
            '就算有魔兽和可疑人士，\n',
            '不走到近距离也很难辨认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警，警备的我们\n',
            '老实说都有点紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5502')

    def _loc_547B(): pass

    label('loc_547B')

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '怎、怎么……\n',
            '你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，呼……\n',
            '别吓唬我啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想到会出现魔兽和可疑人士\n',
            '就好紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_5502(): pass

    label('loc_5502')

    Jump('loc_55E6')

    def _loc_5505(): pass

    label('loc_5505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_55E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_556C',
    )

    ChrTalk(
        0x00FE,
        (
            '我才刚到这城市，\n',
            '突然就派任务下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的阿斯顿队长\n',
            '也比平时更加严厉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_55E6')

    def _loc_556C(): pass

    label('loc_556C')

    ChrTalk(
        0x00FE,
        (
            '我才刚到这城市，\n',
            '突然就开始派任务下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的阿斯顿队长\n',
            '也比平时更加严厉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长这次果然\n',
            '很严格啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_55E6(): pass

    label('loc_55E6')

    TalkEnd(0x0020)

    Return()

# id: 0x0024 offset: 0x55EA
@scena.Code('func_24_55EA')
def func_24_55EA():
    TalkBegin(0x0021)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5703',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_5668',
    )

    ChrTalk(
        0x00FE,
        (
            '执行这种任务的时候，\n',
            '身旁有个沉默寡言的伙伴可真叫人受不了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算鼓起勇气搭话，\n',
            '那边也没反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5700')

    def _loc_5668(): pass

    label('loc_5668')

    ChrTalk(
        0x00FE,
        (
            '如果是平常的话\n',
            '我不讨厌沉默的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '执、执行这种任务的时候\n',
            '身旁有个沉默寡言的伙伴可叫人受不了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '意外的让人分心\n',
            '反而自己更觉得累。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_5700(): pass

    label('loc_5700')

    Jump('loc_57DB')

    def _loc_5703(): pass

    label('loc_5703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_57DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_5766',
    )

    ChrTalk(
        0x00FE,
        (
            '现在的洛连特\n',
            '简直像另一个世界似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盯着看一下下\n',
            '就感觉到丝丝的寒意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_57DB')

    def _loc_5766(): pass

    label('loc_5766')

    ChrTalk(
        0x00FE,
        (
            '平常休息我偶尔也会\n',
            '来洛连特玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在像是另一个世界似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盯着看一下下\n',
            '就感觉到丝丝的寒意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_57DB(): pass

    label('loc_57DB')

    TalkEnd(0x0021)

    Return()

# id: 0x0025 offset: 0x57DF
@scena.Code('func_25_57DF')
def func_25_57DF():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5876',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_581C',
    )

    ChrTalk(
        0x00FE,
        (
            '…………………………\n',
            '……没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5873')

    def _loc_581C(): pass

    label('loc_581C')

    ChrTalk(
        0x00FE,
        (
            '…………………………\n',
            '……没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………\n',
            '……有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_5873(): pass

    label('loc_5873')

    Jump('loc_58D0')

    def _loc_5876(): pass

    label('loc_5876')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_58D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_589F',
    )

    ChrTalk(
        0x00FE,
        (
            '………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58D0')

    def _loc_589F(): pass

    label('loc_589F')

    ChrTalk(
        0x00FE,
        (
            '………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_58D0(): pass

    label('loc_58D0')

    TalkEnd(0x0022)

    Return()

# id: 0x0026 offset: 0x58D4
@scena.Code('func_26_58D4')
def func_26_58D4():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5994',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_5940',
    )

    ChrTalk(
        0x00FE,
        (
            '多明戈先生这种自信\n',
            '是从哪儿来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，万一有事\n',
            '希望他还能维持这种自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5991')

    def _loc_5940(): pass

    label('loc_5940')

    ChrTalk(
        0x00FE,
        (
            '多明戈先生这种自信\n',
            '是从哪儿来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从哈肯大门来的人\n',
            '果然不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_5991(): pass

    label('loc_5991')

    Jump('loc_5A8F')

    def _loc_5994(): pass

    label('loc_5994')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_5A8F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_5A07',
    )

    ChrTalk(
        0x00FE,
        (
            '威尔特桥那边\n',
            '是由补充部队负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然是国境师团所属的士兵，\n',
            '实力上应该也不会有什么问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A8F')

    def _loc_5A07(): pass

    label('loc_5A07')

    ChrTalk(
        0x00FE,
        (
            '现在威尔特桥那边\n',
            '是由补充部队负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是补充部队\n',
            '但实力上应该没有任何问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为他们平时可是\n',
            '国境师团所属的士兵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_5A8F(): pass

    label('loc_5A8F')

    TalkEnd(0x0023)

    Return()

# id: 0x0027 offset: 0x5A93
@scena.Code('func_27_5A93')
def func_27_5A93():
    TalkBegin(0x0024)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5B54',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_5AE8',
    )

    ChrTalk(
        0x00FE,
        (
            '城市方面也完全没有问题啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '别这么担心嘛老兄！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B51')

    def _loc_5AE8(): pass

    label('loc_5AE8')

    ChrTalk(
        0x00FE,
        (
            '城市方面也完全没有问题啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '别这么担心嘛老兄！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然我都这么说了\n',
            '就一定没错啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_5B51(): pass

    label('loc_5B51')

    Jump('loc_5C06')

    def _loc_5B54(): pass

    label('loc_5B54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_5C06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_5BA7',
    )

    ChrTalk(
        0x00FE,
        (
            '既然我来了\n',
            '城市的安全就有保障啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '总之放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C06')

    def _loc_5BA7(): pass

    label('loc_5BA7')

    ChrTalk(
        0x00FE,
        (
            '哦，你们是刚才在街道\n',
            '碰见的那些游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，放心吧。\n',
            '我可以保证城市的安全啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_5C06(): pass

    label('loc_5C06')

    TalkEnd(0x0024)

    Return()

# id: 0x0028 offset: 0x5C0A
@scena.Code('func_28_5C0A')
def func_28_5C0A():
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5CC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_5C6C',
    )

    ChrTalk(
        0x00FE,
        (
            '总之天黑以前\n',
            '就这样继续在外面巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这样做\n',
            '市民也会感到安心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CC1')

    def _loc_5C6C(): pass

    label('loc_5C6C')

    ChrTalk(
        0x00FE,
        (
            '现在这时，\n',
            '不会有可疑人物的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，在这大雾之中\n',
            '能见度的确十分的低啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_5CC1(): pass

    label('loc_5CC1')

    Jump('loc_5D39')

    def _loc_5CC4(): pass

    label('loc_5CC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_5D39',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说听过传闻，\n',
            '实际看来是相当诡异的雾啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我们是记下地图才来的\n',
            '但在这浓雾中还是会迷路的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5D39(): pass

    label('loc_5D39')

    TalkEnd(0x0025)

    Return()

# id: 0x0029 offset: 0x5D3D
@scena.Code('func_29_5D3D')
def func_29_5D3D():
    TalkBegin(0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5DC7',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，游击士。\n',
            '这边没什么异常啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '硬要说有什么异常的话，\n',
            '那就是这些鸽子旺盛的食欲了，\n',
            '都起这么大雾了还是那么能吃啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E1C')

    def _loc_5DC7(): pass

    label('loc_5DC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_5E1C',
    )

    ChrTalk(
        0x00FE,
        (
            '真是好久没离开哈肯大门\n',
            '执行任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种工作用来\n',
            '换换心情倒是不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E1C(): pass

    label('loc_5E1C')

    TalkEnd(0x0026)

    Return()

# id: 0x002A offset: 0x5E20
@scena.Code('func_2A_5E20')
def func_2A_5E20():
    TalkBegin(0x0029)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_5EB0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_5E4D',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎！\n',
            '请随便看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EB0')

    def _loc_5E4D(): pass

    label('loc_5E4D')

    ChrTalk(
        0x00FE,
        (
            '请进！\n',
            '欢迎光临里农杂货铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然今天也很大雾，\n',
            '不过还是照常营业哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请随便看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    def _loc_5EB0(): pass

    label('loc_5EB0')

    TalkEnd(0x0029)

    Return()

# id: 0x002B offset: 0x5EB4
@scena.Code('func_2B_5EB4')
def func_2B_5EB4():
    TalkBegin(0x0033)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_5FC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F71',
    )

    OP_4A(0x0034, 255)

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆和艾娅莉。\n',
            '非常棒呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～我家的安莉尔\n',
            '也能举行那样的婚礼就好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0034, 400)

    ChrTalk(
        0x00FE,
        (
            '是吧～～安莉尔～～\n',
            '和你老公商量看看～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x0034,
        (
            '喵～～呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0034, 255)
    OP_A2(0x0010)

    Jump('loc_5FC5')

    def _loc_5F71(): pass

    label('loc_5F71')

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆和艾娅莉。\n',
            '非常棒呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～我家的安莉尔\n',
            '也能举行那样的婚礼就好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FC5(): pass

    label('loc_5FC5')

    Jump('loc_64B9')

    def _loc_5FC8(): pass

    label('loc_5FC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6020',
    )

    ChrTalk(
        0x00FE,
        (
            '喂喂小猫咪们～\n',
            '别玩了，快准备好～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等下要去出席\n',
            '很重要的婚礼哦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64B9')

    def _loc_6020(): pass

    label('loc_6020')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_6412',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_61CA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_60B2',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～怎样的名字\n',
            '才适合小猫咪呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '科洛～蒂娅……\n',
            '简称小科洛\n',
            '应该很可爱～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过对公主殿下太失礼了吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61C7')

    def _loc_60B2(): pass

    label('loc_60B2')

    ChrTalk(
        0x00FE,
        (
            '哎呀～～\n',
            '游击士们～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们看～～\n',
            '小猫咪们很精神吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F啊哈哈，没错没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1011F对了对了，名字决定了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，这个\n',
            '还没呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然想了很久…\n',
            '还是很伤脑筋啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～长大之前\n',
            '能决定就好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F不、不……\n',
            '别等到长大还没名字吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x2000)

    def _loc_61C7(): pass

    label('loc_61C7')

    Jump('loc_640F')

    def _loc_61CA(): pass

    label('loc_61CA')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_6326',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_6255',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～怎样的名字\n',
            '才适合小猫咪呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '科洛～蒂娅……\n',
            '简称小科洛\n',
            '应该很可爱～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过对公主殿下太失礼了吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6323')

    def _loc_6255(): pass

    label('loc_6255')

    ChrTalk(
        0x00FE,
        (
            '哎呀～～\n',
            '游击士们～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们看～～安莉尔\n',
            '当了妈妈回来了哦～',
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
            '#1004F咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这、带着自己的宝宝们回来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯～是啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，现在\n',
            '正在想名字哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x2000)

    def _loc_6323(): pass

    label('loc_6323')

    Jump('loc_640F')

    def _loc_6326(): pass

    label('loc_6326')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_6378',
    )

    ChrTalk(
        0x00FE,
        (
            '安莉尔的宝宝们\n',
            '可得早点起名字才行～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～怎样的\n',
            '名字才好呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_640F')

    def _loc_6378(): pass

    label('loc_6378')

    ChrTalk(
        0x00FE,
        (
            '安莉尔的宝宝们\n',
            '可得早点起名字才行～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～怎样的\n',
            '名字才好呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '科洛～蒂娅……\n',
            '简称小科洛\n',
            '应该很可爱～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过对公主殿下太失礼了吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    def _loc_640F(): pass

    label('loc_640F')

    Jump('loc_64B9')

    def _loc_6412(): pass

    label('loc_6412')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_64B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_644D',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……呼呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    Jump('loc_64B9')

    def _loc_644D(): pass

    label('loc_644D')

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '嗯～…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呼呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F（这、这种情况下\n',
            '居然睡得着啊～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)
    OP_A2(0x0010)

    def _loc_64B9(): pass

    label('loc_64B9')

    TalkEnd(0x0033)

    Return()

# id: 0x002C offset: 0x64BD
@scena.Code('func_2C_64BD')
def func_2C_64BD():
    TalkBegin(0x0034)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_64DF',
    )

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～～呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_650F')

    def _loc_64DF(): pass

    label('loc_64DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_64FE',
    )

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～～呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_650F')

    def _loc_64FE(): pass

    label('loc_64FE')

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_650F(): pass

    label('loc_650F')

    TalkEnd(0x0034)

    Return()

# id: 0x002D offset: 0x6513
@scena.Code('func_2D_6513')
def func_2D_6513():
    UnlockAchievement(0x01, 0x02, 0x00, 0x00)
    TalkBegin(0x002A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_6562',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然酒量很差，\n',
            '但我是真心的哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_664A')

    def _loc_6562(): pass

    label('loc_6562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_664A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_65CF',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到那么漂亮的人\n',
            '居然那么能喝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔～……真糟糕。\n',
            '这下可就不能随便约她了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_664A')

    def _loc_65CF(): pass

    label('loc_65CF')

    ChrTalk(
        0x00FE,
        (
            '啊啊，真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到那么漂亮的人\n',
            '居然那么能喝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔～真糟糕啊。\n',
            '这不就没法草率地提出邀请了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_664A(): pass

    label('loc_664A')

    TalkEnd(0x002A)

    Return()

# id: 0x002E offset: 0x664E
@scena.Code('func_2E_664E')
def func_2E_664E():
    TalkBegin(0x002B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_673C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_66A4',
    )

    ChrTalk(
        0x00FE,
        (
            '请别介意\n',
            '我旁边的同伴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是平常的相思病\n',
            '又发作了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6739')

    def _loc_66A4(): pass

    label('loc_66A4')

    ChrTalk(
        0x00FE,
        (
            '士兵们\n',
            '似乎开始城市警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像很紧张似的，\n',
            '要发生事件了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '此外……\n',
            '请别介意我旁边的同伴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是平常的相思病\n',
            '又发作了罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    def _loc_6739(): pass

    label('loc_6739')

    Jump('loc_6827')

    def _loc_673C(): pass

    label('loc_673C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_6827',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_679F',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦喜欢的女性\n',
            '感觉和他不合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不可能的事就早点死心，\n',
            '看看鸽子就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6827')

    def _loc_679F(): pass

    label('loc_679F')

    ChrTalk(
        0x00FE,
        (
            '安敦中意的女性，\n',
            '感觉实在跟他不合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不可能的事就早点死心，\n',
            '还不如去看看鸽子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鸽子真有趣啊……\n',
            '怎么看也看不腻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    def _loc_6827(): pass

    label('loc_6827')

    TalkEnd(0x002B)

    Return()

# id: 0x002F offset: 0x682B
@scena.Code('func_2F_682B')
def func_2F_682B():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_684B',
    )

    Call(0, 0x0051)
    FadeIn(0, 0)
    Call(0, 0x0052)

    def _loc_684B(): pass

    label('loc_684B')

    SetChrPos(0x0101, 55680, 250, 28860, 270)
    SetChrPos(0x0103, 56680, 250, 28860, 270)
    SetChrPos(0x00F8, 57680, 250, 28860, 270)
    SetChrPos(0x00F9, 58680, 250, 28860, 270)
    OP_6D(52910, 250, 28860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x000A, 0)
    OP_70(0x000A, 0x0000003B)
    OP_73(0x000A)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, 0x0030)
    CreateThread(0x0103, 0x01, 0x00, 0x0031)
    CreateThread(0x00F8, 0x01, 0x00, 0x0032)
    CreateThread(0x00F9, 0x01, 0x00, 0x0033)
    Sleep(2000)

    @scena.Lambda('lambda_6913')
    def lambda_6913():
        OP_6D(50680, 250, 28860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6913)

    @scena.Lambda('lambda_692B')
    def lambda_692B():
        OP_6C(39000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_692B)

    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010280821V#1007F呼……\n',
            '话说回来还真厉害呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280822V明明是熟到不能再熟的城市，\n',
            '但却感觉会迷路似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280823V#020F为了不迷路\n',
            '才带了地图和罗盘嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280824V如果迷失了方向\n',
            '就一边找方向一边前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6B34',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280827V阿加特，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280829V#051F啊啊，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280830V#061F姐姐的家啊。\n',
            '嘿嘿，有点期待啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_6B34(): pass

    label('loc_6B34')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6C5F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280833V阿加特，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280829V#051F啊啊，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280836V#031F艾丝蒂尔的家啊……\n',
            '呵呵呵，真令人期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_6C5F(): pass

    label('loc_6C5F')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D84',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280839V阿加特，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280829V#051F啊啊，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280842V#048F艾丝蒂尔的家吗？\n',
            '呵呵，有点期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_6D84(): pass

    label('loc_6D84')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6EA5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280845V阿加特，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280829V#051F啊啊，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280848V#071F哈哈，看来马上\n',
            '就要承蒙款待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_6EA5(): pass

    label('loc_6EA5')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6FD0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280851V提妲，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280853V#061F嗯，当然可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280836V#031F艾丝蒂尔的家啊……\n',
            '呵呵呵，真令人期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_6FD0(): pass

    label('loc_6FD0')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_70F5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280857V提妲，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280859V#061F嗯，当然可以⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280842V#048F艾丝蒂尔的家吗～？\n',
            '呵呵，有点期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_70F5(): pass

    label('loc_70F5')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7214',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280862V总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280863V#1015F提妲，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280859V#061F嗯，当然可以⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280848V#071F哈哈，看来马上\n',
            '就要承蒙款待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_7214(): pass

    label('loc_7214')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_733F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280869V科洛丝，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280871V#048F好的，我们陪你去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280872V#031F艾丝蒂尔的家啊……\n',
            '呵呵，真是期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_733F(): pass

    label('loc_733F')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7464',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280875V奥利维尔，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280877V#031F呵，当然可以啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280848V#071F哈哈，看来马上\n',
            '就要承蒙款待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7586')

    def _loc_7464(): pass

    label('loc_7464')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7586',
    )

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280826V#1015F总之先去各条路\n',
            '调查一下雾的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280881V科洛丝，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280828V我先回家里看看，\n',
            '确认一下情况可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280871V#048F好的，我们陪你去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280848V#071F哈哈，看来马上\n',
            '就要承蒙款待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7586(): pass

    label('loc_7586')

    ChrTalk(
        0x0103,
        (
            '#0030280885V#027F接下来……\n',
            '那么就出发喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008F, 0x04, 0x02)
    OP_28(0x008F, 0x04, 0x08)
    OP_28(0x008F, 0x01, 0x0001)
    OP_28(0x008F, 0x01, 0x0002)
    OP_28(0x008F, 0x01, 0x0004)
    OP_28(0x008F, 0x01, 0x0010)
    OP_28(0x008F, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x0030 offset: 0x75E1
@scena.Code('func_30_75E1')
def func_30_75E1():
    SetChrFlags(0x00FE, 0x0004)
    OP_90(0x00FE, -1000, 0, 0, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    OP_90(0x00FE, -5000, 0, 0, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0031 offset: 0x761B
@scena.Code('func_31_761B')
def func_31_761B():
    OP_90(0x00FE, -5000, 0, 0, 2000, 0x00)
    OP_90(0x00FE, -1000, 0, 1000, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0032 offset: 0x764B
@scena.Code('func_32_764B')
def func_32_764B():
    OP_90(0x00FE, -5000, 0, 0, 2000, 0x00)
    OP_90(0x00FE, -2000, 0, -1000, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0033 offset: 0x767B
@scena.Code('func_33_767B')
def func_33_767B():
    OP_8E(0x00FE, 52910, 250, 28860, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(200)

    OP_72(0x000A, 0x0800)
    OP_6F(0x000A, 59)
    OP_70(0x000A, 0x00000000)
    OP_23(0x0006)
    OP_22(0x0007, 0x00, 0x64)
    OP_73(0x000A)
    OP_71(0x000A, 0x0800)
    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    OP_90(0x00FE, -1230, 0, 0, 2000, 0x00)

    Return()

# id: 0x0034 offset: 0x76DF
@scena.Code('func_34_76DF')
def func_34_76DF():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_76FF',
    )

    Call(0, 0x0051)
    FadeIn(0, 0)
    Call(0, 0x0052)

    def _loc_76FF(): pass

    label('loc_76FF')

    OP_6D(49260, 0, 15200, 0)
    OP_67(0, 8770, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(29000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 48750, 0, 5350, 0)
    SetChrPos(0x0103, 49910, 0, 5310, 0)
    SetChrPos(0x00F8, 48680, 0, 4040, 0)
    SetChrPos(0x00F9, 49870, 0, 3980, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_778F')
    def lambda_778F():
        OP_90(0x00FE, 0, 0, 9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_778F)

    Sleep(100)

    @scena.Lambda('lambda_77AF')
    def lambda_77AF():
        OP_90(0x00FE, 0, 0, 9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_77AF)

    Sleep(200)

    @scena.Lambda('lambda_77CF')
    def lambda_77CF():
        OP_90(0x00FE, 0, 0, 9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_77CF)

    Sleep(100)

    @scena.Lambda('lambda_77EF')
    def lambda_77EF():
        OP_90(0x00FE, 0, 0, 9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_77EF)

    WaitForThreadExit(0x00F9, 0x0001)
    OP_22(0x0118, 0x00, 0x32)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010281286V#1004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    OP_8C(0x0101, 90, 400)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    Sleep(1000)

    Call(0, 0x0037)

    Return()

# id: 0x0035 offset: 0x7863
@scena.Code('func_35_7863')
def func_35_7863():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7883',
    )

    Call(0, 0x0051)
    FadeIn(0, 0)
    Call(0, 0x0052)

    def _loc_7883(): pass

    label('loc_7883')

    OP_6D(17320, 0, 39700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(227000, 0)
    OP_6E(261, 0)
    SetChrPos(0x0101, 10520, 0, 40860, 90)
    SetChrPos(0x0103, 10520, 0, 39800, 90)
    SetChrPos(0x00F8, 9520, 0, 41000, 90)
    SetChrPos(0x00F9, 9520, 0, 39850, 90)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_7913')
    def lambda_7913():
        OP_90(0x00FE, 8000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7913)

    Sleep(100)

    @scena.Lambda('lambda_7933')
    def lambda_7933():
        OP_90(0x00FE, 8000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_7933)

    Sleep(200)

    @scena.Lambda('lambda_7953')
    def lambda_7953():
        OP_90(0x00FE, 8000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_7953)

    Sleep(100)

    @scena.Lambda('lambda_7973')
    def lambda_7973():
        OP_90(0x00FE, 8000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_7973)

    WaitForThreadExit(0x00F9, 0x0001)
    OP_22(0x0118, 0x00, 0x32)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    Sleep(500)

    OP_8C(0x0101, 180, 400)
    Sleep(500)

    OP_8C(0x0101, 90, 400)
    Sleep(1000)

    Call(0, 0x0037)

    Return()

# id: 0x0036 offset: 0x79C0
@scena.Code('func_36_79C0')
def func_36_79C0():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_79E0',
    )

    Call(0, 0x0051)
    FadeIn(0, 0)
    Call(0, 0x0052)

    def _loc_79E0(): pass

    label('loc_79E0')

    OP_6D(27470, 0, 70500, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(299000, 0)
    OP_6E(303, 0)
    SetChrPos(0x0101, 28700, 0, 77670, 180)
    SetChrPos(0x0103, 27450, 0, 77670, 180)
    SetChrPos(0x00F8, 28690, 0, 78670, 180)
    SetChrPos(0x00F9, 27410, 0, 78670, 180)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_7A70')
    def lambda_7A70():
        OP_90(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7A70)

    Sleep(100)

    @scena.Lambda('lambda_7A90')
    def lambda_7A90():
        OP_90(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_7A90)

    Sleep(200)

    @scena.Lambda('lambda_7AB0')
    def lambda_7AB0():
        OP_90(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_7AB0)

    Sleep(100)

    @scena.Lambda('lambda_7AD0')
    def lambda_7AD0():
        OP_90(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_7AD0)

    WaitForThreadExit(0x00F9, 0x0001)
    OP_22(0x0118, 0x00, 0x32)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010281286V#1004F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    Sleep(500)

    OP_8C(0x0101, 270, 400)
    Sleep(500)

    OP_8C(0x0101, 180, 400)
    Sleep(1000)

    Call(0, 0x0037)

    Return()

# id: 0x0037 offset: 0x7B3D
@scena.Code('func_37_7B3D')
def func_37_7B3D():
    ChrTalk(
        0x0101,
        (
            '#0010281287V#1011F刚才……\n',
            '听到铃声了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BA8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281288V#061F嗯。\n',
            '从远方传来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7CA3')

    def _loc_7BA8(): pass

    label('loc_7BA8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BE4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281289V#051F啊啊。\n',
            '从远方传来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7CA3')

    def _loc_7BE4(): pass

    label('loc_7BE4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C28',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281290V#035F呼……\n',
            '似乎是从远方传来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7CA3')

    def _loc_7C28(): pass

    label('loc_7C28')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C64',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281291V#048F嗯。\n',
            '从远方传来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7CA3')

    def _loc_7C64(): pass

    label('loc_7C64')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CA3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281292V#070F啊啊。\n',
            '似乎是从远方传来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7CA3(): pass

    label('loc_7CA3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CE5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281293V#061F呼呼……\n',
            '相当悦耳的音色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DE4')

    def _loc_7CE5(): pass

    label('loc_7CE5')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D25',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281294V#051F哦……\n',
            '相当不错的音色啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DE4')

    def _loc_7D25(): pass

    label('loc_7D25')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D65',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281295V#035F呼……\n',
            '多么优雅的铃声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DE4')

    def _loc_7D65(): pass

    label('loc_7D65')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7DA7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281296V#048F呼呼……\n',
            '非常悦耳的音色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DE4')

    def _loc_7DA7(): pass

    label('loc_7DA7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7DE4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281297V#070F嗯……\n',
            '相当优雅的铃声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DE4(): pass

    label('loc_7DE4')

    ChrTalk(
        0x0101,
        (
            '#0010281298V#1001F嗯嗯。\n',
            '都听得入迷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281299V#023F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281300V#1015F咦……\n',
            '怎么了，雪拉姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030281301V#524F啊，不，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281302V只是音色太悦耳\n',
            '听得入迷了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281303V#1006F怎么，雪拉姐也会这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281304V铃声虽然少见\n',
            '会不会是里农先生的杂货铺\n',
            '新进的货品呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281305V#026F有可能呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281306V#020F先不说这个……\n',
            '这下雾的产生范围\n',
            '大概就清楚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281307V差不多该回协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281308V#1006F啊，嗯。\n',
            '得向爱娜姐报告才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0038 offset: 0x802E
@scena.Code('func_38_802E')
def func_38_802E():
    EventBegin(0x00)
    OP_20(0x000003E8)
    OP_21()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)
    SetChrStatus(ChrTable['提妲'], 0xFE, 0)
    SetChrStatus(ChrTable['金'], 0xFE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8070',
    )

    Call(0, 0x0051)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    def _loc_8070(): pass

    label('loc_8070')

    FadeOut(0, 0, -1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    OP_6D(52910, 250, 28860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 55680, 250, 28860, 270)
    SetChrPos(0x0103, 56680, 250, 28860, 270)
    SetChrPos(0x00F8, 57680, 250, 28860, 270)
    SetChrPos(0x00F9, 58680, 250, 28860, 270)
    OP_1D(0x0A)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(2000, 0)
    OP_0D()
    OP_6F(0x000A, 0)
    OP_70(0x000A, 0x0000003B)
    OP_73(0x000A)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, 0x0039)
    CreateThread(0x0103, 0x01, 0x00, 0x0031)
    CreateThread(0x00F8, 0x01, 0x00, 0x0032)
    CreateThread(0x00F9, 0x01, 0x00, 0x0033)
    Sleep(2000)

    @scena.Lambda('lambda_81EB')
    def lambda_81EB():
        OP_6D(50680, 250, 28860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_81EB)

    @scena.Lambda('lambda_8203')
    def lambda_8203():
        OP_6C(39000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8203)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010300075V#1011F#6P接下来，按照最初的计划\n',
            '该去柏斯地区了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300076V那是唯一一个\n',
            '还没有做过实验的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030300077V#020F#5P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300078V以现状来看，柏斯地区\n',
            '似乎还没发生什么奇怪的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300079V某种程度上来说，协助\n',
            '完成洛连特的工作后再去也来得及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300080V#1006F#6P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300081V那把事情都完成以后\n',
            '就去飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0092, 0x01, 0x0100)
    OP_28(0x0092, 0x01, 0x0200)
    OP_28(0x0092, 0x01, 0x0400)
    OP_28(0x0092, 0x01, 0x0800)
    OP_28(0x0092, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x0039 offset: 0x83A9
@scena.Code('func_39_83A9')
def func_39_83A9():
    SetChrFlags(0x00FE, 0x0004)
    OP_90(0x00FE, -1000, 0, 0, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    OP_90(0x00FE, -4000, 0, 0, 2000, 0x00)
    OP_90(0x00FE, -1000, 0, 0, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x003A offset: 0x83F7
@scena.Code('func_3A_83F7')
def func_3A_83F7():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrPos(0x0008, 49400, 0, 53090, 180)
    SetChrPos(0x0009, 40640, 0, 41220, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    CreateThread(0x0008, 0x01, 0x00, 0x003B)
    CreateThread(0x0009, 0x01, 0x00, 0x003C)
    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)
    OP_6D(49420, 0, 47770, 0)
    OP_67(0, 12280, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(19000, 0)
    OP_6E(386, 0)
    FadeIn(1000, 0)
    OP_12(0x00000000, 0x00000000, 0x00001F40)
    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    @scena.Lambda('lambda_84D4')
    def lambda_84D4():
        OP_6D(49240, 0, 28690, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_84D4)

    @scena.Lambda('lambda_84EC')
    def lambda_84EC():
        OP_67(0, 6000, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_84EC)

    @scena.Lambda('lambda_8504')
    def lambda_8504():
        OP_6C(13000, 10000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_8504)

    @scena.Lambda('lambda_8514')
    def lambda_8514():
        OP_6E(401, 10000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_8514)

    CreateThread(0x000A, 0x01, 0x00, 0x003D)
    CreateThread(0x000B, 0x01, 0x00, 0x003E)
    CreateThread(0x000C, 0x01, 0x00, 0x003F)
    CreateThread(0x000D, 0x01, 0x00, 0x0040)
    WaitForThreadExit(0x0001, 0x0002)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0210._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x003B offset: 0x8558
@scena.Code('func_3B_8558')
def func_3B_8558():
    OP_8E(0x00FE, 49400, 0, 46020, 1000, 0x00)
    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    def _loc_858D(): pass

    label('loc_858D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_85C9',
    )

    OP_8C(0x00FE, 90, 400)
    Sleep(400)

    OP_8C(0x00FE, 0, 400)
    Sleep(400)

    OP_8C(0x00FE, 270, 400)
    Sleep(400)

    OP_8C(0x00FE, 180, 400)
    Sleep(400)

    Jump('loc_858D')

    def _loc_85C9(): pass

    label('loc_85C9')

    Return()

# id: 0x003C offset: 0x85CA
@scena.Code('func_3C_85CA')
def func_3C_85CA():
    Sleep(500)

    OP_8E(0x00FE, 47560, 0, 41220, 1000, 0x00)
    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    def _loc_8604(): pass

    label('loc_8604')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8640',
    )

    OP_8C(0x00FE, 180, 400)
    Sleep(400)

    OP_8C(0x00FE, 270, 400)
    Sleep(400)

    OP_8C(0x00FE, 0, 400)
    Sleep(400)

    OP_8C(0x00FE, 90, 400)
    Sleep(400)

    Jump('loc_8604')

    def _loc_8640(): pass

    label('loc_8640')

    Return()

# id: 0x003D offset: 0x8641
@scena.Code('func_3D_8641')
def func_3D_8641():
    SetChrPos(0x00FE, 54290, 250, 28900, 270)
    OP_72(0x000A, 0x0010)
    OP_70(0x000A, 0x0000003B)
    OP_73(0x000A)
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, -2000, 0, 0, 2000, 0x00)
    OP_8E(0x00FE, 50040, 0, 30720, 2000, 0x00)
    def _loc_8693(): pass

    label('loc_8693')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_86CF',
    )

    OP_8C(0x00FE, 315, 400)
    Sleep(400)

    OP_8C(0x00FE, 45, 400)
    Sleep(400)

    OP_8C(0x00FE, 315, 400)
    Sleep(400)

    OP_8C(0x00FE, 225, 400)
    Sleep(400)

    Jump('loc_8693')

    def _loc_86CF(): pass

    label('loc_86CF')

    Return()

# id: 0x003E offset: 0x86D0
@scena.Code('func_3E_86D0')
def func_3E_86D0():
    Sleep(500)

    SetChrPos(0x00FE, 43270, 250, 33060, 90)
    OP_72(0x0003, 0x0010)
    OP_70(0x0003, 0x0000003B)
    OP_73(0x0003)
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 2000, 0, 0, 2000, 0x00)
    OP_8E(0x00FE, 48380, 0, 33600, 2000, 0x00)
    def _loc_8727(): pass

    label('loc_8727')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8763',
    )

    OP_8C(0x00FE, 180, 300)
    Sleep(600)

    OP_8C(0x00FE, 270, 300)
    Sleep(600)

    OP_8C(0x00FE, 0, 300)
    Sleep(600)

    OP_8C(0x00FE, 90, 300)
    Sleep(600)

    Jump('loc_8727')

    def _loc_8763(): pass

    label('loc_8763')

    Return()

# id: 0x003F offset: 0x8764
@scena.Code('func_3F_8764')
def func_3F_8764():
    Sleep(4000)

    SetChrPos(0x00FE, 43270, 250, 33060, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 3000, 0, 0, 2000, 0x00)
    OP_8E(0x00FE, 47640, 0, 35310, 2000, 0x00)
    def _loc_87A7(): pass

    label('loc_87A7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_87E3',
    )

    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    OP_8C(0x00FE, 360, 400)
    Sleep(500)

    OP_8C(0x00FE, 270, 400)
    Sleep(500)

    OP_8C(0x00FE, 180, 400)
    Sleep(500)

    Jump('loc_87A7')

    def _loc_87E3(): pass

    label('loc_87E3')

    Return()

# id: 0x0040 offset: 0x87E4
@scena.Code('func_40_87E4')
def func_40_87E4():
    Sleep(1000)

    SetChrPos(0x00FE, 43290, 250, 22060, 90)
    OP_72(0x0001, 0x0010)
    OP_70(0x0001, 0x0000003B)
    OP_73(0x0001)
    Sleep(1000)

    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 3000, 0, 0, 2000, 0x00)
    OP_8E(0x00FE, 48140, 0, 25350, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    def _loc_8842(): pass

    label('loc_8842')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8866',
    )

    OP_8C(0x00FE, 225, 400)
    Sleep(1000)

    OP_8C(0x00FE, 135, 400)
    Sleep(1000)

    Jump('loc_8842')

    def _loc_8866(): pass

    label('loc_8866')

    Return()

# id: 0x0041 offset: 0x8867
@scena.Code('func_41_8867')
def func_41_8867():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_26(191)
    OP_26(180)
    OP_26(141)
    OP_D2(0x00260221, 0x00260226, 0x09)
    OP_D2(0x00260220, 0x00260225, 0x0A)
    SetChrChipByIndex(0x0033, 23)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_88AA',
    )

    Call(0, 0x0051)
    Call(0, 0x0053)

    def _loc_88AA(): pass

    label('loc_88AA')

    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0011, 0x00)
    TerminateThread(0x0010, 0x00)
    TerminateThread(0x0012, 0x00)
    TerminateThread(0x0013, 0x00)
    TerminateThread(0x001A, 0x00)
    TerminateThread(0x001B, 0x00)
    TerminateThread(0x001C, 0x00)
    TerminateThread(0x001D, 0x00)
    TerminateThread(0x001E, 0x00)
    TerminateThread(0x0029, 0x00)
    SetChrPos(0x0012, 72900, 500, 33000, 0)
    SetChrPos(0x0013, 72900, 500, 33000, 0)
    ClearChrFlags(0x002E, 0x0080)
    ClearChrFlags(0x002F, 0x0080)
    ClearChrFlags(0x0030, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000E, 68880, 0, 41940, 135)
    SetChrPos(0x000F, 68520, 0, 40910, 135)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 70270, 0, 37620, 135)
    ClearChrFlags(0x0033, 0x0080)
    ClearChrFlags(0x0034, 0x0080)
    SetChrPos(0x0010, 70320, 0, 38640, 135)
    ClearChrFlags(0x0035, 0x0080)
    ClearChrFlags(0x0036, 0x0080)
    ClearChrFlags(0x0037, 0x0080)
    ClearChrFlags(0x0038, 0x0080)
    ClearChrFlags(0x0039, 0x0080)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    ClearChrFlags(0x003E, 0x0080)
    ClearChrFlags(0x003F, 0x0080)
    ClearChrFlags(0x0040, 0x0080)
    ClearChrFlags(0x0041, 0x0080)
    SetChrPos(0x0102, 69140, 0, 39210, 135)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89E3',
    )

    SetChrPos(0x0106, 69130, 0, 40270, 135)

    def _loc_89E3(): pass

    label('loc_89E3')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A02',
    )

    SetChrPos(0x0108, 69000, 0, 38290, 135)

    def _loc_8A02(): pass

    label('loc_8A02')

    SetChrPos(0x0101, 73140, 0, 40470, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A32',
    )

    SetChrPos(0x0103, 74000, 0, 40300, 180)

    def _loc_8A32(): pass

    label('loc_8A32')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A51',
    )

    SetChrPos(0x0107, 72170, 0, 40280, 180)

    def _loc_8A51(): pass

    label('loc_8A51')

    LoadEffect(0x00, 'map\\\\mp016_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 74440, 0, 38950, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6D(65680, 0, 38210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(110000, 0)
    OP_6E(262, 0)
    TerminateThread(0x001A, 0x00)
    TerminateThread(0x001B, 0x00)
    TerminateThread(0x001C, 0x00)
    SetChrPos(0x001A, 55200, 12320, 47260, 135)
    SetChrPos(0x001B, 54200, 12320, 46260, 0)
    SetChrPos(0x001C, 53570, 12000, 47000, 225)

    ExecExpressionWithValue(
        0x001A,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x001A, 0x0004)
    SetChrFlags(0x001A, 0x0040)
    SetChrFlags(0x001B, 0x0004)
    SetChrFlags(0x001B, 0x0040)
    SetChrFlags(0x001C, 0x0004)
    SetChrFlags(0x001C, 0x0040)

    @scena.Lambda('lambda_8B5B')
    def lambda_8B5B():
        OP_6C(135000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8B5B)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    CreateThread(0x000E, 0x01, 0x00, 0x005A)

    @scena.Lambda('lambda_8B81')
    def lambda_8B81():
        OP_6D(73060, 500, 34550, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8B81)

    @scena.Lambda('lambda_8B99')
    def lambda_8B99():
        OP_6B(2800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8B99)

    CreateThread(0x001A, 0x01, 0x00, 0x0046)
    CreateThread(0x001A, 0x03, 0x00, 0x0049)
    Sleep(200)

    CreateThread(0x001B, 0x01, 0x00, 0x0047)
    CreateThread(0x001B, 0x03, 0x00, 0x0049)
    Sleep(200)

    CreateThread(0x001C, 0x01, 0x00, 0x0048)
    CreateThread(0x001C, 0x03, 0x00, 0x0049)
    OP_6E(262, 5000)
    OP_6F(0x000E, 0)
    OP_70(0x000E, 0x0000003B)
    OP_73(0x000E)
    Sleep(200)

    OP_62(0x0037, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0038, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0036, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0031, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0033, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0041, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0032, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0039, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0040, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_22(0x00BF, 0x00, 0x64)
    CreateThread(0x0012, 0x01, 0x00, 0x0042)
    Sleep(1000)

    CreateThread(0x0013, 0x01, 0x00, 0x0043)
    Sleep(1000)

    CreateThread(0x002D, 0x01, 0x00, 0x0044)
    Sleep(1000)

    CreateThread(0x002C, 0x01, 0x00, 0x0045)
    WaitForThreadExit(0x0013, 0x0001)
    WaitForThreadExit(0x002C, 0x0001)
    OP_82(0x00, 0x02)
    WaitForThreadExit(0x002D, 0x0001)
    OP_8E(0x002D, 74340, 0, 36430, 2000, 0x00)

    ChrTalk(
        0x002D,
        (
            '#4070351165V#1P──那么，接下来\n',
            '请新娘抛捧花。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#4070351166V#1P未婚的女性\n',
            '请上前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8E44')
    def lambda_8E44():
        OP_6D(72780, 0, 39500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8E44)

    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    @scena.Lambda('lambda_8E6E')
    def lambda_8E6E():
        OP_94(0x00, 0x00FE, 0x0000, 0x000000C8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_8E6E)

    Sleep(100)

    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    @scena.Lambda('lambda_8E9B')
    def lambda_8E9B():
        OP_94(0x00, 0x00FE, 0x0000, 0x000000C8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0035, 0x0001, lambda_8E9B)

    Sleep(100)

    OP_62(0x0033, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    @scena.Lambda('lambda_8EC8')
    def lambda_8EC8():
        OP_94(0x00, 0x00FE, 0x0000, 0x000000C8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_8EC8)

    Sleep(100)

    OP_62(0x0037, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    @scena.Lambda('lambda_8EF5')
    def lambda_8EF5():
        OP_94(0x00, 0x00FE, 0x0000, 0x000000C8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_8EF5)

    Sleep(100)

    OP_62(0x0040, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    @scena.Lambda('lambda_8F22')
    def lambda_8F22():
        OP_94(0x00, 0x00FE, 0x0000, 0x000000C8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0040, 0x0001, lambda_8F22)

    Sleep(100)

    OP_62(0x0041, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    @scena.Lambda('lambda_8F4F')
    def lambda_8F4F():
        OP_94(0x00, 0x00FE, 0x0000, 0x000000C8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0041, 0x0001, lambda_8F4F)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0035,
        (
            '#4080351167V#4P呀～要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0030,
        '年轻的女性',
        (
            '#4090351168V#1P艾娅莉～朝这边扔～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000E, 0x01, 0x00, 0x005B)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_908B',
    )

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080351169V#070F原来如此，还有这样的风俗啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080351170V#071F哈哈，女孩子们\n',
            '连眼睛都亮了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020351171V#1040F某种意义上来说这是\n',
            '婚礼上最热闹的场面了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_914D')

    def _loc_908B(): pass

    label('loc_908B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_914D',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050351172V#053F嗯，抛捧花啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050351173V#555F虽不知道有什么有趣的，\n',
            '但感觉杀气很重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020351171V#1040F某种意义上来说这是\n',
            '婚礼上最热闹的场面了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_914D(): pass

    label('loc_914D')

    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010351175V#1016F#2P嗯～大家\n',
            '都鼓足了劲儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92C1',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030351176V#020F快，艾丝蒂尔。\n',
            '别磨磨蹭蹭的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030351177V看看风向，\n',
            '占个好位置哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    SetChrFlags(0x0030, 0x0040)

    @scena.Lambda('lambda_9221')
    def lambda_9221():
        OP_94(0x00, 0x0030, 0x0000, 0x0000012C, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_9221)

    Sleep(200)

    OP_94(0x01, 0x0103, 0x010E, 0x000000C8, 0x000007D0, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x0103, 0x0030, 400)

    ChrTalk(
        0x0103,
        (
            '#0030351178V#024F呼、别挤啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351179V#1019F#2P……哟、很认真啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_92B9')
    def lambda_92B9():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_92B9)

    def _loc_92C1(): pass

    label('loc_92C1')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_93EF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351180V#062F#2P（心跳心跳……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010351181V#1007F#2P我说……\n',
            '提妲也满是干劲嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x00, 0x0107, 0x0000, 0x000001F4, 0x000003E8, 0x00)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070351182V#062F#2P嗯嗯、湿度５５％……\n',
            '东南偏东风３．５亚矩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070351183V嗯……\n',
            '就机率上来说这里最好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351184V#1016F#2P要、要做到这种程度吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_93EF(): pass

    label('loc_93EF')

    OP_8C(0x0101, 180, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_946A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010351185V#1015F#2P嗯，那么\n',
            '也算我一份吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351186V怎么说\n',
            '我也是个年轻女孩嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_946A(): pass

    label('loc_946A')

    @scena.Lambda('lambda_9470')
    def lambda_9470():
        OP_6D(73720, 500, 33120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9470)

    TerminateThread(0x000E, 0x01)
    Sleep(500)

    OP_8C(0x0012, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0012,
        (
            '#3430351187V#2P要抛向正后方\n',
            '可是相当难的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3430351188V#2P那么，各位!\n',
            '要是没接到可别生气哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3430351189V#2P一～二～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3430351190V#2P……嘿咻────！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0042, 0x01, 0x00, 0x004C)

    @scena.Lambda('lambda_9557')
    def lambda_9557():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9557')

    DispatchAsync2(0x0101, 0x0001, lambda_9557)

    @scena.Lambda('lambda_9568')
    def lambda_9568():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9568')

    DispatchAsync2(0x0102, 0x0001, lambda_9568)

    @scena.Lambda('lambda_9579')
    def lambda_9579():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9579')

    DispatchAsync2(0x00F8, 0x0001, lambda_9579)

    @scena.Lambda('lambda_958A')
    def lambda_958A():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_958A')

    DispatchAsync2(0x00F9, 0x0001, lambda_958A)

    @scena.Lambda('lambda_959B')
    def lambda_959B():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_959B')

    DispatchAsync2(0x0035, 0x0001, lambda_959B)

    @scena.Lambda('lambda_95AC')
    def lambda_95AC():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_95AC')

    DispatchAsync2(0x0036, 0x0001, lambda_95AC)

    @scena.Lambda('lambda_95BD')
    def lambda_95BD():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_95BD')

    DispatchAsync2(0x0037, 0x0001, lambda_95BD)

    @scena.Lambda('lambda_95CE')
    def lambda_95CE():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_95CE')

    DispatchAsync2(0x0038, 0x0001, lambda_95CE)

    @scena.Lambda('lambda_95DF')
    def lambda_95DF():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_95DF')

    DispatchAsync2(0x0039, 0x0001, lambda_95DF)

    @scena.Lambda('lambda_95F0')
    def lambda_95F0():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_95F0')

    DispatchAsync2(0x003A, 0x0001, lambda_95F0)

    @scena.Lambda('lambda_9601')
    def lambda_9601():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9601')

    DispatchAsync2(0x003B, 0x0001, lambda_9601)

    @scena.Lambda('lambda_9612')
    def lambda_9612():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9612')

    DispatchAsync2(0x003C, 0x0001, lambda_9612)

    @scena.Lambda('lambda_9623')
    def lambda_9623():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9623')

    DispatchAsync2(0x003D, 0x0001, lambda_9623)

    @scena.Lambda('lambda_9634')
    def lambda_9634():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9634')

    DispatchAsync2(0x003E, 0x0001, lambda_9634)

    @scena.Lambda('lambda_9645')
    def lambda_9645():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9645')

    DispatchAsync2(0x003F, 0x0001, lambda_9645)

    @scena.Lambda('lambda_9656')
    def lambda_9656():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9656')

    DispatchAsync2(0x0040, 0x0001, lambda_9656)

    @scena.Lambda('lambda_9667')
    def lambda_9667():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9667')

    DispatchAsync2(0x0041, 0x0001, lambda_9667)

    @scena.Lambda('lambda_9678')
    def lambda_9678():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9678')

    DispatchAsync2(0x0013, 0x0001, lambda_9678)

    @scena.Lambda('lambda_9689')
    def lambda_9689():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9689')

    DispatchAsync2(0x002E, 0x0001, lambda_9689)

    @scena.Lambda('lambda_969A')
    def lambda_969A():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_969A')

    DispatchAsync2(0x002F, 0x0001, lambda_969A)

    @scena.Lambda('lambda_96AB')
    def lambda_96AB():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_96AB')

    DispatchAsync2(0x0030, 0x0001, lambda_96AB)

    @scena.Lambda('lambda_96BC')
    def lambda_96BC():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_96BC')

    DispatchAsync2(0x0031, 0x0001, lambda_96BC)

    @scena.Lambda('lambda_96CD')
    def lambda_96CD():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_96CD')

    DispatchAsync2(0x0032, 0x0001, lambda_96CD)

    @scena.Lambda('lambda_96DE')
    def lambda_96DE():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_96DE')

    DispatchAsync2(0x0011, 0x0001, lambda_96DE)

    @scena.Lambda('lambda_96EF')
    def lambda_96EF():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_96EF')

    DispatchAsync2(0x0033, 0x0001, lambda_96EF)

    @scena.Lambda('lambda_9700')
    def lambda_9700():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9700')

    DispatchAsync2(0x0010, 0x0001, lambda_9700)

    @scena.Lambda('lambda_9711')
    def lambda_9711():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9711')

    DispatchAsync2(0x002D, 0x0001, lambda_9711)

    @scena.Lambda('lambda_9722')
    def lambda_9722():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9722')

    DispatchAsync2(0x002C, 0x0001, lambda_9722)

    @scena.Lambda('lambda_9733')
    def lambda_9733():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9733')

    DispatchAsync2(0x0034, 0x0001, lambda_9733)

    @scena.Lambda('lambda_9744')
    def lambda_9744():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9744')

    DispatchAsync2(0x000F, 0x0001, lambda_9744)

    @scena.Lambda('lambda_9755')
    def lambda_9755():
        ChrTurnDirection(0x00FE, 0x0042, 400)
        Yield()

        Jump('lambda_9755')

    DispatchAsync2(0x000E, 0x0001, lambda_9755)

    OP_6D(79220, 3000, 36290, 2000)

    ChrTalk(
        0x0035,
        (
            '#4080351191V#2P呀～那边不行～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0037,
        (
            '#4090351192V#2P往哪里抛啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0042, 0x0001)
    Sleep(200)

    Fade(1000)
    OP_6D(73800, 0, 38790, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_983B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351193V#562F呜呜～好可惜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_983B(): pass

    label('loc_983B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9871',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351194V#025F唉……\n',
            '又没接住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9871(): pass

    label('loc_9871')

    ChrTalk(
        0x0101,
        (
            '#0010351195V#1007F简、简直就是\n',
            '往相反的方向飞了去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351196V有人接得到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0035, 0x01)
    TerminateThread(0x0036, 0x01)
    TerminateThread(0x0037, 0x01)
    TerminateThread(0x0038, 0x01)
    TerminateThread(0x0039, 0x01)
    TerminateThread(0x003A, 0x01)
    TerminateThread(0x003B, 0x01)
    TerminateThread(0x003C, 0x01)
    TerminateThread(0x003D, 0x01)
    TerminateThread(0x003E, 0x01)
    TerminateThread(0x003F, 0x01)
    TerminateThread(0x0040, 0x01)
    TerminateThread(0x0041, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x002E, 0x01)
    TerminateThread(0x002F, 0x01)
    TerminateThread(0x0030, 0x01)
    TerminateThread(0x0031, 0x01)
    TerminateThread(0x0032, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0033, 0x01)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x002D, 0x01)
    TerminateThread(0x002C, 0x01)
    TerminateThread(0x0034, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0042, 0x01)
    SetChrPos(0x0029, 82720, 0, 39930, 270)
    SetChrPos(0x0042, 82650, 600, 39930, 90)
    SetChrFlags(0x0042, 0x0002)
    SetChrSubChip(0x0042, 1)

    NpcTalk(
        0x0029,
        '年轻的女性',
        (
            '#4100351197V#3P请，请问～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_99AA')
    def lambda_99AA():
        OP_6D(78070, 0, 40000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_99AA)

    @scena.Lambda('lambda_99C2')
    def lambda_99C2():
        OP_6C(90000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_99C2)

    @scena.Lambda('lambda_99D2')
    def lambda_99D2():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_99D2')

    DispatchAsync2(0x0101, 0x0001, lambda_99D2)

    @scena.Lambda('lambda_99E3')
    def lambda_99E3():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_99E3')

    DispatchAsync2(0x0102, 0x0001, lambda_99E3)

    @scena.Lambda('lambda_99F4')
    def lambda_99F4():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_99F4')

    DispatchAsync2(0x00F8, 0x0001, lambda_99F4)

    @scena.Lambda('lambda_9A05')
    def lambda_9A05():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A05')

    DispatchAsync2(0x00F9, 0x0001, lambda_9A05)

    @scena.Lambda('lambda_9A16')
    def lambda_9A16():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A16')

    DispatchAsync2(0x0035, 0x0001, lambda_9A16)

    @scena.Lambda('lambda_9A27')
    def lambda_9A27():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A27')

    DispatchAsync2(0x0036, 0x0001, lambda_9A27)

    @scena.Lambda('lambda_9A38')
    def lambda_9A38():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A38')

    DispatchAsync2(0x0037, 0x0001, lambda_9A38)

    @scena.Lambda('lambda_9A49')
    def lambda_9A49():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A49')

    DispatchAsync2(0x0038, 0x0001, lambda_9A49)

    @scena.Lambda('lambda_9A5A')
    def lambda_9A5A():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A5A')

    DispatchAsync2(0x0039, 0x0001, lambda_9A5A)

    @scena.Lambda('lambda_9A6B')
    def lambda_9A6B():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A6B')

    DispatchAsync2(0x003A, 0x0001, lambda_9A6B)

    @scena.Lambda('lambda_9A7C')
    def lambda_9A7C():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A7C')

    DispatchAsync2(0x003B, 0x0001, lambda_9A7C)

    @scena.Lambda('lambda_9A8D')
    def lambda_9A8D():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A8D')

    DispatchAsync2(0x003C, 0x0001, lambda_9A8D)

    @scena.Lambda('lambda_9A9E')
    def lambda_9A9E():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9A9E')

    DispatchAsync2(0x003D, 0x0001, lambda_9A9E)

    @scena.Lambda('lambda_9AAF')
    def lambda_9AAF():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9AAF')

    DispatchAsync2(0x003E, 0x0001, lambda_9AAF)

    @scena.Lambda('lambda_9AC0')
    def lambda_9AC0():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9AC0')

    DispatchAsync2(0x003F, 0x0001, lambda_9AC0)

    @scena.Lambda('lambda_9AD1')
    def lambda_9AD1():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9AD1')

    DispatchAsync2(0x0040, 0x0001, lambda_9AD1)

    @scena.Lambda('lambda_9AE2')
    def lambda_9AE2():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9AE2')

    DispatchAsync2(0x0041, 0x0001, lambda_9AE2)

    @scena.Lambda('lambda_9AF3')
    def lambda_9AF3():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9AF3')

    DispatchAsync2(0x0013, 0x0001, lambda_9AF3)

    @scena.Lambda('lambda_9B04')
    def lambda_9B04():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B04')

    DispatchAsync2(0x002E, 0x0001, lambda_9B04)

    @scena.Lambda('lambda_9B15')
    def lambda_9B15():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B15')

    DispatchAsync2(0x002F, 0x0001, lambda_9B15)

    @scena.Lambda('lambda_9B26')
    def lambda_9B26():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B26')

    DispatchAsync2(0x0030, 0x0001, lambda_9B26)

    @scena.Lambda('lambda_9B37')
    def lambda_9B37():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B37')

    DispatchAsync2(0x0031, 0x0001, lambda_9B37)

    @scena.Lambda('lambda_9B48')
    def lambda_9B48():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B48')

    DispatchAsync2(0x0032, 0x0001, lambda_9B48)

    @scena.Lambda('lambda_9B59')
    def lambda_9B59():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B59')

    DispatchAsync2(0x0011, 0x0001, lambda_9B59)

    @scena.Lambda('lambda_9B6A')
    def lambda_9B6A():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B6A')

    DispatchAsync2(0x0033, 0x0001, lambda_9B6A)

    @scena.Lambda('lambda_9B7B')
    def lambda_9B7B():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B7B')

    DispatchAsync2(0x0010, 0x0001, lambda_9B7B)

    @scena.Lambda('lambda_9B8C')
    def lambda_9B8C():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B8C')

    DispatchAsync2(0x002D, 0x0001, lambda_9B8C)

    @scena.Lambda('lambda_9B9D')
    def lambda_9B9D():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9B9D')

    DispatchAsync2(0x002C, 0x0001, lambda_9B9D)

    @scena.Lambda('lambda_9BAE')
    def lambda_9BAE():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9BAE')

    DispatchAsync2(0x0034, 0x0001, lambda_9BAE)

    @scena.Lambda('lambda_9BBF')
    def lambda_9BBF():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9BBF')

    DispatchAsync2(0x000F, 0x0001, lambda_9BBF)

    @scena.Lambda('lambda_9BD0')
    def lambda_9BD0():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9BD0')

    DispatchAsync2(0x000E, 0x0001, lambda_9BD0)

    @scena.Lambda('lambda_9BE1')
    def lambda_9BE1():
        ChrTurnDirection(0x00FE, 0x0029, 400)
        Yield()

        Jump('lambda_9BE1')

    DispatchAsync2(0x0012, 0x0001, lambda_9BE1)

    ClearChrFlags(0x0029, 0x0080)
    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_9BFC')
    def lambda_9BFC():
        OP_8E(0x00FE, 78000, 600, 40000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0042, 0x0001, lambda_9BFC)

    OP_8E(0x0029, 78070, 0, 40000, 2000, 0x00)

    ChrTalk(
        0x0029,
        (
            '#4100351198V这、这是什么？这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#4100351199V从天空\n',
            '掉下来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0035, 0x01)
    TerminateThread(0x0036, 0x01)
    TerminateThread(0x0037, 0x01)
    TerminateThread(0x0038, 0x01)
    TerminateThread(0x0039, 0x01)
    TerminateThread(0x003A, 0x01)
    TerminateThread(0x003B, 0x01)
    TerminateThread(0x003C, 0x01)
    TerminateThread(0x003D, 0x01)
    TerminateThread(0x003E, 0x01)
    TerminateThread(0x003F, 0x01)
    TerminateThread(0x0040, 0x01)
    TerminateThread(0x0041, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x002E, 0x01)
    TerminateThread(0x002F, 0x01)
    TerminateThread(0x0030, 0x01)
    TerminateThread(0x0031, 0x01)
    TerminateThread(0x0032, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0033, 0x01)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x002D, 0x01)
    TerminateThread(0x002C, 0x01)
    TerminateThread(0x0034, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000E, 0x01)
    OP_6D(75450, 0, 37780, 2000)

    ChrTalk(
        0x0012,
        (
            '#3430351200V哎呀，你捡到的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3430351201V那是我抛出的\n',
            '新娘捧花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0029, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0029,
        (
            '#4100351202V啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#3420351203V#2P恭喜你了，小姐。\n',
            '你一定会结下良缘的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0029, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0029,
        (
            '#4100351204V怎，怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#4100351205V怎么办……我……\n',
            '还，还没有心理准备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    OP_6D(73160, 0, 40680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010351206V#1016F#3P呼、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351207V感觉是\n',
            '物归其所了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9EF8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351208V#025F#1P呼，一点不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EF8(): pass

    label('loc_9EF8')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F3D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351209V#067F#4P嘿嘿、捧花\n',
            '说不定正适合她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F3D(): pass

    label('loc_9F3D')

    OP_6D(73230, 260, 34450, 2000)
    ChrTurnDirection(0x002C, 0x0013, 400)
    Sleep(500)

    ChrTalk(
        0x002C,
        (
            '#1080351210V#2P好了──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#1080351211V#2P婚礼进行到这里\n',
            '也总算结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9FAF')
    def lambda_9FAF():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_9FAF)

    @scena.Lambda('lambda_9FBD')
    def lambda_9FBD():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9FBD)

    @scena.Lambda('lambda_9FCB')
    def lambda_9FCB():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9FCB)

    @scena.Lambda('lambda_9FD9')
    def lambda_9FD9():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_9FD9)

    @scena.Lambda('lambda_9FE7')
    def lambda_9FE7():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_9FE7)

    @scena.Lambda('lambda_9FF5')
    def lambda_9FF5():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0035, 0x0001, lambda_9FF5)

    @scena.Lambda('lambda_A003')
    def lambda_A003():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0036, 0x0001, lambda_A003)

    @scena.Lambda('lambda_A011')
    def lambda_A011():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_A011)

    @scena.Lambda('lambda_A01F')
    def lambda_A01F():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_A01F)

    @scena.Lambda('lambda_A02D')
    def lambda_A02D():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_A02D)

    @scena.Lambda('lambda_A03B')
    def lambda_A03B():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_A03B)

    @scena.Lambda('lambda_A049')
    def lambda_A049():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_A049)

    @scena.Lambda('lambda_A057')
    def lambda_A057():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_A057)

    @scena.Lambda('lambda_A065')
    def lambda_A065():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_A065)

    @scena.Lambda('lambda_A073')
    def lambda_A073():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x003E, 0x0001, lambda_A073)

    @scena.Lambda('lambda_A081')
    def lambda_A081():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x003F, 0x0001, lambda_A081)

    @scena.Lambda('lambda_A08F')
    def lambda_A08F():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0040, 0x0001, lambda_A08F)

    @scena.Lambda('lambda_A09D')
    def lambda_A09D():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0041, 0x0001, lambda_A09D)

    @scena.Lambda('lambda_A0AB')
    def lambda_A0AB():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x002E, 0x0001, lambda_A0AB)

    @scena.Lambda('lambda_A0B9')
    def lambda_A0B9():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_A0B9)

    @scena.Lambda('lambda_A0C7')
    def lambda_A0C7():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_A0C7)

    @scena.Lambda('lambda_A0D5')
    def lambda_A0D5():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_A0D5)

    @scena.Lambda('lambda_A0E3')
    def lambda_A0E3():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_A0E3)

    @scena.Lambda('lambda_A0F1')
    def lambda_A0F1():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_A0F1)

    @scena.Lambda('lambda_A0FF')
    def lambda_A0FF():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_A0FF)

    @scena.Lambda('lambda_A10D')
    def lambda_A10D():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_A10D)

    @scena.Lambda('lambda_A11B')
    def lambda_A11B():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_A11B)

    @scena.Lambda('lambda_A129')
    def lambda_A129():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_A129)

    @scena.Lambda('lambda_A137')
    def lambda_A137():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_A137)

    @scena.Lambda('lambda_A145')
    def lambda_A145():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_A145)

    @scena.Lambda('lambda_A153')
    def lambda_A153():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_A153)

    @scena.Lambda('lambda_A161')
    def lambda_A161():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_A161)

    @scena.Lambda('lambda_A16F')
    def lambda_A16F():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_A16F)

    Sleep(400)

    ChrTalk(
        0x002D,
        (
            '#4070351212V#1P祝愿你们俩\n',
            '幸福到永远……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x002D, 400)

    ChrTalk(
        0x0012,
        (
            '#3430351213V#2P谢谢你，修女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A1DA')
    def lambda_A1DA():
        ChrTurnDirection(0x00FE, 0x002C, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_A1DA)

    ChrTurnDirection(0x0013, 0x002C, 400)

    ChrTalk(
        0x0013,
        (
            '#3420351214V#1P还有教区长……\n',
            '今天真是非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#1080351215V#2P现在王国的情况很严峻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#1080351216V#2P但请不要畏惧任何困难，\n',
            '努力构筑幸福的家庭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002C,
        (
            '#1080351217V#2P这就是对出席的人们\n',
            '最好的回报哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#3420351218V#1P……是，是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A2EB')
    def lambda_A2EB():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A2EB)

    @scena.Lambda('lambda_A2F9')
    def lambda_A2F9():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A2F9)

    @scena.Lambda('lambda_A307')
    def lambda_A307():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_A307)

    @scena.Lambda('lambda_A315')
    def lambda_A315():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_A315)

    @scena.Lambda('lambda_A323')
    def lambda_A323():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0035, 0x0001, lambda_A323)

    @scena.Lambda('lambda_A331')
    def lambda_A331():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0036, 0x0001, lambda_A331)

    @scena.Lambda('lambda_A33F')
    def lambda_A33F():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_A33F)

    @scena.Lambda('lambda_A34D')
    def lambda_A34D():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_A34D)

    @scena.Lambda('lambda_A35B')
    def lambda_A35B():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_A35B)

    @scena.Lambda('lambda_A369')
    def lambda_A369():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_A369)

    @scena.Lambda('lambda_A377')
    def lambda_A377():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_A377)

    @scena.Lambda('lambda_A385')
    def lambda_A385():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_A385)

    @scena.Lambda('lambda_A393')
    def lambda_A393():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_A393)

    @scena.Lambda('lambda_A3A1')
    def lambda_A3A1():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x003E, 0x0001, lambda_A3A1)

    @scena.Lambda('lambda_A3AF')
    def lambda_A3AF():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x003F, 0x0001, lambda_A3AF)

    @scena.Lambda('lambda_A3BD')
    def lambda_A3BD():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0040, 0x0001, lambda_A3BD)

    @scena.Lambda('lambda_A3CB')
    def lambda_A3CB():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0041, 0x0001, lambda_A3CB)

    @scena.Lambda('lambda_A3D9')
    def lambda_A3D9():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x002E, 0x0001, lambda_A3D9)

    @scena.Lambda('lambda_A3E7')
    def lambda_A3E7():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_A3E7)

    @scena.Lambda('lambda_A3F5')
    def lambda_A3F5():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_A3F5)

    @scena.Lambda('lambda_A403')
    def lambda_A403():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_A403)

    @scena.Lambda('lambda_A411')
    def lambda_A411():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_A411)

    @scena.Lambda('lambda_A41F')
    def lambda_A41F():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_A41F)

    @scena.Lambda('lambda_A42D')
    def lambda_A42D():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_A42D)

    @scena.Lambda('lambda_A43B')
    def lambda_A43B():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_A43B)

    @scena.Lambda('lambda_A449')
    def lambda_A449():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_A449)

    @scena.Lambda('lambda_A457')
    def lambda_A457():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_A457)

    @scena.Lambda('lambda_A465')
    def lambda_A465():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_A465)

    @scena.Lambda('lambda_A473')
    def lambda_A473():
        ChrTurnDirection(0x0013, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_A473)

    OP_62(0x0037, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0038, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0036, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0031, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0033, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0041, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0032, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0039, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0040, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_8C(0x0013, 0, 400)
    OP_8C(0x0012, 0, 400)
    OP_22(0x00BF, 0x00, 0x64)

    @scena.Lambda('lambda_A62A')
    def lambda_A62A():
        OP_94(0x01, 0x00FE, 0x010E, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_A62A)

    @scena.Lambda('lambda_A640')
    def lambda_A640():
        OP_94(0x01, 0x00FE, 0x005A, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_A640)

    Sleep(500)

    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    OP_8C(0x0013, 270, 400)
    OP_8C(0x0012, 90, 400)

    @scena.Lambda('lambda_A673')
    def lambda_A673():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000096, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_A673)

    OP_94(0x00, 0x0012, 0x0000, 0x00000096, 0x000001F4, 0x00)
    OP_62(0x0013, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    OP_62(0x0037, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0038, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0036, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0031, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0033, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0041, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0032, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0039, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0040, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1500)

    OP_62(0x0037, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0038, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0036, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0031, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0033, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0041, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0032, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0039, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x003F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x002F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0040, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_6F(0x000E, 0)
    ClearMapFlags(0x10000000)
    OP_20(0x00000BB8)
    Sleep(2000)

    OP_A2(0x2086)
    NewScene('ED6_DT21/T0130._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0042 offset: 0xAA1F
@scena.Code('func_42_AA1F')
def func_42_AA1F():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 72900, 500, 34570, 1000, 0x00)
    OP_8E(0x00FE, 72460, 500, 34570, 1000, 0x00)
    OP_8E(0x00FE, 72460, 500, 35180, 1000, 0x00)

    Return()

# id: 0x0043 offset: 0xAA61
@scena.Code('func_43_AA61')
def func_43_AA61():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 72900, 500, 34570, 1000, 0x00)
    OP_8E(0x00FE, 73540, 500, 34570, 1000, 0x00)
    OP_8E(0x00FE, 73540, 480, 35180, 1000, 0x00)

    Return()

# id: 0x0044 offset: 0xAAA3
@scena.Code('func_44_AAA3')
def func_44_AAA3():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 72900, 500, 34570, 1000, 0x00)
    OP_8E(0x00FE, 74250, 500, 34570, 1000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0045 offset: 0xAAD8
@scena.Code('func_45_AAD8')
def func_45_AAD8():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 72900, 500, 34570, 1000, 0x00)
    OP_8E(0x00FE, 71790, 500, 34570, 1000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0046 offset: 0xAB0D
@scena.Code('func_46_AB0D')
def func_46_AB0D():
    SetChrChipByIndex(0x001A, 11)
    ClearChrFlags(0x001A, 0x0400)
    SetChrFlags(0x001A, 0x0004)
    SetChrFlags(0x001A, 0x0040)
    OP_98(0x00, 0x001A)
    OP_98(0x01, 0x00011BA2, 0x00001B58, 0x00009132)
    OP_98(0x01, 0x00016C10, 0x00001F40, 0x000097F4)
    CreateThread(0x00FE, 0x02, 0x00, 0x004B)
    OP_98(0x02, 0x001A, 0x0000157C, 0x02)

    Return()

# id: 0x0047 offset: 0xAB52
@scena.Code('func_47_AB52')
def func_47_AB52():
    SetChrChipByIndex(0x001B, 11)
    ClearChrFlags(0x001B, 0x0400)
    SetChrFlags(0x001B, 0x0004)
    SetChrFlags(0x001B, 0x0040)
    OP_98(0x00, 0x001B)
    OP_98(0x01, 0x00010D88, 0x00001B58, 0x000091DC)
    OP_98(0x01, 0x00016C10, 0x00001388, 0x00009BDC)
    CreateThread(0x00FE, 0x02, 0x00, 0x004B)
    OP_98(0x02, 0x001B, 0x0000157C, 0x02)

    Return()

# id: 0x0048 offset: 0xAB97
@scena.Code('func_48_AB97')
def func_48_AB97():
    SetChrChipByIndex(0x001C, 11)
    ClearChrFlags(0x001C, 0x0400)
    SetChrFlags(0x001C, 0x0004)
    SetChrFlags(0x001C, 0x0040)
    OP_98(0x00, 0x001C)
    OP_98(0x01, 0x000109A0, 0x00002328, 0x00009D94)
    OP_98(0x01, 0x00016C10, 0x00001F40, 0x0000940C)
    CreateThread(0x00FE, 0x02, 0x00, 0x004B)
    OP_98(0x02, 0x001C, 0x0000157C, 0x02)

    Return()

# id: 0x0049 offset: 0xABDC
@scena.Code('func_49_ABDC')
def func_49_ABDC():
    Sleep(800)

    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(4000)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

    Return()

# id: 0x004A offset: 0xABFD
@scena.Code('func_4A_ABFD')
def func_4A_ABFD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AC35',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x5DC),
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
        'loc_AC2D',
    )

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

    Jump('loc_AC35')

    def _loc_AC2D(): pass

    label('loc_AC2D')

    Sleep(15)

    Jump('func_4A_ABFD')

    def _loc_AC35(): pass

    label('loc_AC35')

    Return()

# id: 0x004B offset: 0xAC36
@scena.Code('func_4B_AC36')
def func_4B_AC36():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AC4B',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00001770)

    Jump('func_4B_AC36')

    def _loc_AC4B(): pass

    label('loc_AC4B')

    Return()

# id: 0x004C offset: 0xAC4C
@scena.Code('func_4C_AC4C')
def func_4C_AC4C():
    ClearChrFlags(0x0042, 0x0080)
    OP_22(0x00CB, 0x00, 0x64)
    OP_98(0x00, 0x0042)
    OP_98(0x01, 0x00012AF2, 0x00002710, 0x00008D54)
    OP_98(0x01, 0x00013A42, 0x00001F40, 0x00008DCC)
    OP_98(0x01, 0x000150A4, 0x00000000, 0x00009CFE)
    OP_98(0x02, 0x0042, 0x0000157C, 0x02)

    Return()

# id: 0x004D offset: 0xAC8E
@scena.Code('func_4D_AC8E')
def func_4D_AC8E():
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_AD24',
    )

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000E, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '啊～！？\n',
            '艾丝蒂尔和约修亚！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '啊，姐姐和哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你们回来了。\n',
            '今天两人在一起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA8')

    def _loc_AD24(): pass

    label('loc_AD24')

    ChrTurnDirection(0x000F, 0x0101, 0)

    ChrTalk(
        0x000F,
        (
            '啊……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '艾丝蒂尔姐姐\n',
            '和约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000E, 0x0102, 400)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '啊～！？约修亚！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '终于回来啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    def _loc_ADA8(): pass

    label('loc_ADA8')

    ChrTalk(
        0x0101,
        (
            '#1001F嗯，不容易呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000E, 400)

    ChrTalk(
        0x0102,
        (
            '#1040F好久没见你们俩了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哈哈，还是\n',
            '那么活泼的样子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0102, 400)

    ChrTalk(
        0x000E,
        (
            '嘿嘿，当然喽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '艾丝蒂尔你们\n',
            '今天也要工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '是不是导力器\n',
            '停止事件的调查？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000F, 400)

    ChrTalk(
        0x0102,
        (
            '#1040F嗯，是在干这个呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说这问题\n',
            '一时半刻是解决不了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '唉～好无聊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那还不如去调查\n',
            '那个浮在空中的岛呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B000',
    )

    ChrTalk(
        0x0101,
        (
            '#1007F要能那么做\n',
            '早就去做了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000E, 400)

    ChrTalk(
        0x0102,
        (
            '#1042F现在街道的灯都熄灭了，\n',
            '城外边非常危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '鲁克你们\n',
            '也不能到街道上去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0102, 400)

    ChrTalk(
        0x000E,
        (
            '嘿嘿，这个\n',
            '我还是知道的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉，虽然有点可惜，\n',
            '今天就在城中一日游吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好！走吧帕特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哥哥姐姐。\n',
            '那么，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B11F')

    def _loc_B000(): pass

    label('loc_B000')

    ChrTalk(
        0x0101,
        (
            '#1007F要能那么做\n',
            '早就去做了啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '导力器不能用了，\n',
            '你们也知道吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1042F现在街道的灯都熄灭了，\n',
            '城外是很危险的状态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '鲁克你们\n',
            '也不能到街道上去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嘿嘿，这个\n',
            '我还是知道的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉，虽然有点可惜，\n',
            '今天就忍忍待在城里面吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好！走吧帕特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，哥哥姐姐。\n',
            '回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B11F(): pass

    label('loc_B11F')

    OP_8C(0x000E, 90, 400)
    OP_8C(0x000F, 270, 400)
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)
    OP_A2(0x0017)
    OP_A2(0x0016)
    OP_A2(0x20A0)

    Return()

# id: 0x004E offset: 0xB13F
@scena.Code('func_4E_B13F')
def func_4E_B13F():
    TalkBegin(0x0046)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B3F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 3, 0x209B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B35F',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0102, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔啊……\n',
            '这，这不是约修亚吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F好久不见了，菲特先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，才多久没见啊，\n',
            '就完全长成个男子汉了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，这我就放心了。\n',
            '和艾丝蒂尔在游击士的道路上都\n',
            '做得很漂亮嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F这都是托您的福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来王国中\n',
            '好象发生了严重的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回归军队的卡西乌斯\n',
            '也忙得不可开交吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '作为游击士的你们两个\n',
            '可要努力，不能输给他哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯！\n',
            '我们会尽全力完成工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F有什么困难\n',
            '就联系协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '我会的。\n',
            '那么，两人都要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)
    OP_A2(0x209B)

    Jump('loc_B3F6')

    def _loc_B35F(): pass

    label('loc_B35F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Return,
        ),
        'loc_B3A2',
    )

    ChrTalk(
        0x00FE,
        (
            '有什么事我\n',
            '会联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，两人都要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3F6')

    def _loc_B3A2(): pass

    label('loc_B3A2')

    ChrTalk(
        0x00FE,
        (
            '今天早上起来的时候\n',
            '发现导力灯打不开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之先想办法\n',
            '把照明问题解决了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B3F6(): pass

    label('loc_B3F6')

    TalkEnd(0x0046)

    Return()

# id: 0x004F offset: 0xB3FA
@scena.Code('func_4F_B3FA')
def func_4F_B3FA():
    TalkBegin(0x0047)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_B47F',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然导力器停止了，\n',
            '洛连特的人们还是挺悠然的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，单是慌张也于事无补。 \n',
            '或许这种态度倒是应该大家仿效的。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4DB')

    def _loc_B47F(): pass

    label('loc_B47F')

    ChrTalk(
        0x00FE,
        (
            '本打算看看传闻中的浮游岛\n',
            '就从旅馆走出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～从这里看过去\n',
            '视野很差看不太清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B4DB(): pass

    label('loc_B4DB')

    TalkEnd(0x0047)

    Return()

# id: 0x0050 offset: 0xB4DF
@scena.Code('func_50_B4DF')
def func_50_B4DF():
    TalkBegin(0x0048)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_B53E',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船要修复\n',
            '看来还有得等呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要有浮游岛在\n',
            '可能就恢复不了也说不定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B58E')

    def _loc_B53E(): pass

    label('loc_B53E')

    ChrTalk(
        0x00FE,
        (
            '从钟楼上\n',
            '好像能清楚看到浮游岛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连洛连特都看得到，\n',
            '到底有多大呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B58E(): pass

    label('loc_B58E')

    TalkEnd(0x0048)

    Return()

# id: 0x0051 offset: 0xB592
@scena.Code('func_51_B592')
def func_51_B592():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_B60F'),
        (0x00000001, 'loc_B615'),
        (-1, 'loc_B61B'),
    )

    def _loc_B60F(): pass

    label('loc_B60F')

    OP_A2(0x1200)

    Jump('loc_B61B')

    def _loc_B615(): pass

    label('loc_B615')

    OP_A2(0x1201)

    Jump('loc_B61B')

    def _loc_B61B(): pass

    label('loc_B61B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B629',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_B62D')

    def _loc_B629(): pass

    label('loc_B629')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_B62D(): pass

    label('loc_B62D')

    Return()

# id: 0x0052 offset: 0xB62E
@scena.Code('func_52_B62E')
def func_52_B62E():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x0053 offset: 0xB680
@scena.Code('func_53_B680')
def func_53_B680():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x0054 offset: 0xB6D9
@scena.Code('func_54_B6D9')
def func_54_B6D9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B773',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010190291V#505F……这边是反方向吧。\n',
            '得早点回家才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0142, 0x0000, 400)

    ChrTalk(
        0x0142,
        (
            '#0180190292V#1060F这么说\n',
            '是从南门出去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_B9A6')

    def _loc_B773(): pass

    label('loc_B773')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B8EC',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B797',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_B79E')

    def _loc_B797(): pass

    label('loc_B797')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_B79E(): pass

    label('loc_B79E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_B7E8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030290316V#020F虽然也担心外面的情况、\n',
            '但还是先去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8CE')

    def _loc_B7E8(): pass

    label('loc_B7E8')

    ChrTalk(
        0x0103,
        (
            '#0030290316V#020F虽然也担心外面的情况、\n',
            '但还是先去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B860',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250129V#1000F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_B860(): pass

    label('loc_B860')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B897',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0105,
        (
            '#0060290319V#040F嗯，是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_B897(): pass

    label('loc_B897')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B8CE',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0107,
        (
            '#0070290320V#060F啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_B8CE(): pass

    label('loc_B8CE')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_B9A6')

    def _loc_B8EC(): pass

    label('loc_B8EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B9A6',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B952',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281284V#020F现在不是到处跑的时候。\n',
            '先得去协会报告才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B98B')

    def _loc_B952(): pass

    label('loc_B952')

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281285V#020F去哪里？\n',
            '先得去协会报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B98B(): pass

    label('loc_B98B')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_B9A6(): pass

    label('loc_B9A6')

    Return()

# id: 0x0055 offset: 0xB9A7
@scena.Code('func_55_B9A7')
def func_55_B9A7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BA4B',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010190293V#000F约修亚一定\n',
            '已经回家了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190294V早点去家里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190295V#1063F（…………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_BBC1')

    def _loc_BA4B(): pass

    label('loc_BA4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BBC1',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BA6F',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_BA76')

    def _loc_BA6F(): pass

    label('loc_BA6F')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_BA76(): pass

    label('loc_BA76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_BAC0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030290316V#020F虽然也担心外面的情况、\n',
            '但还是先去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BBA6')

    def _loc_BAC0(): pass

    label('loc_BAC0')

    ChrTalk(
        0x0103,
        (
            '#0030290316V#020F虽然也担心外面的情况、\n',
            '但还是先去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB38',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250129V#1000F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_BB38(): pass

    label('loc_BB38')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB6F',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0105,
        (
            '#0060290319V#040F嗯，是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_BB6F(): pass

    label('loc_BB6F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BBA6',
    )

    ChrTurnDirection(0x0000, 0x0103, 400)

    ChrTalk(
        0x0107,
        (
            '#0070290320V#060F啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_BBA6(): pass

    label('loc_BBA6')

    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_BBC1(): pass

    label('loc_BBC1')

    Return()

# id: 0x0056 offset: 0xBBC2
@scena.Code('func_56_BBC2')
def func_56_BBC2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BC7C',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BC28',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281284V#020F现在不是到处跑的时候。\n',
            '先得去协会报告才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC61')

    def _loc_BC28(): pass

    label('loc_BC28')

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281285V#020F去哪儿？\n',
            '先得去协会报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC61(): pass

    label('loc_BC61')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_BC7C(): pass

    label('loc_BC7C')

    Return()

# id: 0x0057 offset: 0xBC7D
@scena.Code('func_57_BC7D')
def func_57_BC7D():
    SetMapFlags(0x00000080)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『七耀历１０７５年』\n',
            '　由利贝尔王室、七耀教会\n',
            '　以及洛连特市共同建造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『七耀历１１９２年』\n',
            '　百日战役中，被围攻洛连特的\n',
            '　埃雷波尼亚帝国军队炮击而倒塌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『七耀历１１９７年』\n',
            '　在市民的协力下得以重建。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0058 offset: 0xBD81
@scena.Code('func_58_BD81')
def func_58_BD81():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　玛鲁加山道一侧出口',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0059 offset: 0xBDCA
@scena.Code('func_59_BDCA')
def func_59_BDCA():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　洛连特飞船坪',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x005A offset: 0xBE0D
@scena.Code('func_5A_BE0D')
def func_5A_BE0D():
    OP_22(0x00B4, 0x00, 0x64)
    Sleep(2500)

    OP_22(0x00B4, 0x00, 0x64)
    Sleep(2500)

    OP_22(0x00B4, 0x00, 0x64)
    Sleep(2500)

    OP_22(0x00B4, 0x00, 0x64)

    Return()

# id: 0x005B offset: 0xBE31
@scena.Code('func_5B_BE31')
def func_5B_BE31():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BEB8',
    )

    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0033, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0037, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0040, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0041, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2500)

    Jump('func_5B_BE31')

    def _loc_BEB8(): pass

    label('loc_BEB8')

    Return()

# id: 0x005C offset: 0xBEB9
@scena.Code('func_5C_BEB9')
def func_5C_BEB9():
    SetPlaceName(0x0004)

    Return()

# id: 0x005D offset: 0xBEBD
@scena.Code('func_5D_BEBD')
def func_5D_BEBD():
    SetPlaceName(0x0002)

    Return()

# id: 0x005E offset: 0xBEC1
@scena.Code('func_5E_BEC1')
def func_5E_BEC1():
    SetPlaceName(0x0006)

    Return()

# id: 0x005F offset: 0xBEC5
@scena.Code('func_5F_BEC5')
def func_5F_BEC5():
    SetPlaceName(0x0005)

    Return()

# id: 0x0060 offset: 0xBEC9
@scena.Code('func_60_BEC9')
def func_60_BEC9():
    SetPlaceName(0x0007)

    Return()

# id: 0x0061 offset: 0xBECD
@scena.Code('func_61_BECD')
def func_61_BECD():
    SetPlaceName(0x0008)

    Return()

# id: 0x0062 offset: 0xBED1
@scena.Code('func_62_BED1')
def func_62_BED1():
    SetPlaceName(0x0003)

    Return()

# id: 0x0063 offset: 0xBED5
@scena.Code('func_63_BED5')
def func_63_BED5():
    SetPlaceName(0x000A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
