import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0131   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '托露塔'),
    TXT(0x02, '托露塔'),
    TXT(0x03, '伊莉莎'),
    TXT(0x04, '德瑟鲁'),
    TXT(0x05, '福克纳'),
    TXT(0x06, '矿工提恩特'),
    TXT(0x07, '矿工彭兹'),
    TXT(0x08, '佩特洛夫船长'),
    TXT(0x09, '乘务员罗杰'),
    TXT(0x0A, '拉欧老人'),
    TXT(0x0B, '布露姆老奶奶'),
    TXT(0x0C, '洛连特风味炖煮'),
    TXT(0x0D, '阿鲁姆'),
    TXT(0x0E, '艾娅莉'),
    TXT(0x0F, '新郎的亲属'),
    TXT(0x10, '新郎的亲属'),
    TXT(0x11, '新郎的亲属'),
    TXT(0x12, '新娘的亲属'),
    TXT(0x13, '新娘的亲属'),
    TXT(0x14, '新娘的亲属'),
    TXT(0x15, '新娘的朋友'),
    TXT(0x16, '新娘的朋友'),
    TXT(0x17, '赛拉'),
    TXT(0x18, '料理'),
    TXT(0x19, '料理'),
    TXT(0x1A, '料理'),
    TXT(0x1B, '料理'),
    TXT(0x1C, '料理'),
    TXT(0x1D, '迪拜恩教区长'),
    TXT(0x1E, '安敦'),
    TXT(0x1F, '爱娜'),
    TXT(0x20, '奥利维尔'),
    TXT(0x21, '酒瓶'),
    TXT(0x22, '酒瓶'),
    TXT(0x23, '酒瓶'),
    TXT(0x24, '酒瓶'),
    TXT(0x25, '酒瓶'),
    TXT(0x26, '酒瓶'),
    TXT(0x27, '酒瓶'),
    TXT(0x28, '酒瓶'),
    TXT(0x29, '酒瓶'),
    TXT(0x2A, '酒瓶'),
    TXT(0x2B, '酒瓶'),
    TXT(0x2C, '酒杯'),
    TXT(0x2D, '酒杯'),
    TXT(0x2E, '酒杯'),
    TXT(0x2F, '酒杯'),
    TXT(0x30, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0131.x'
    header.mapIndex       = 7
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T0131._SN', 'ED6_DT21/T0131_1._SN', 'ED6_DT21/T0131_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x67B8
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
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01503._CH', 'ED6_DT07/CH01503P._CP'),
        ('ED6_DT26/CH20330._CH', 'ED6_DT26/CH20330P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01443._CH', 'ED6_DT07/CH01443P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH02560._CH', 'ED6_DT07/CH02560P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT26/CH20213._CH', 'ED6_DT26/CH20213P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT26/CH20452._CH', 'ED6_DT26/CH20452P._CP'),
        ('ED6_DT26/CH20453._CH', 'ED6_DT26/CH20453P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01133._CH', 'ED6_DT07/CH01133P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00031._CH', 'ED6_DT07/CH00031P._CP'),
    ]

# id: 0x10002 offset: 0x1D2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 87400,
            z                   = 0,
            y                   = 81630,
            direction           = 344,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 88620,
            z                   = 0,
            y                   = 78900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 131077,
            chipIndex           = 5,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34500,
            z                   = 0,
            y                   = 75200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 36450,
            z                   = 0,
            y                   = 126300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 40200,
            z                   = 1500,
            y                   = 78700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 39320,
            z                   = 220,
            y                   = 70940,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 36640,
            z                   = 0,
            y                   = 72850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 39470,
            z                   = 1620,
            y                   = 77070,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 41450,
            z                   = 0,
            y                   = 67700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 36700,
            z                   = 0,
            y                   = 75440,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 35520,
            z                   = 800,
            y                   = 74850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40660,
            z                   = 0,
            y                   = 75350,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 39580,
            z                   = 0,
            y                   = 75440,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 43710,
            z                   = 0,
            y                   = 73240,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 40620,
            z                   = 0,
            y                   = 66290,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 39720,
            z                   = 220,
            y                   = 66420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 43810,
            z                   = 0,
            y                   = 71980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 38130,
            z                   = 0,
            y                   = 75250,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 36600,
            z                   = 0,
            y                   = 72650,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 42470,
            z                   = 0,
            y                   = 65640,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 43540,
            z                   = 0,
            y                   = 66710,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 38730,
            z                   = 220,
            y                   = 73090,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 39370,
            z                   = 700,
            y                   = 72160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131091,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39700,
            z                   = 700,
            y                   = 67800,
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
            x                   = 39660,
            z                   = 700,
            y                   = 67220,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589843,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 44970,
            z                   = 700,
            y                   = 65470,
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
            x                   = 44150,
            z                   = 700,
            y                   = 65349,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131091,
            chipIndex           = 19,
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
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39680,
            z                   = 600,
            y                   = 67660,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40400,
            z                   = 2100,
            y                   = 76950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39480,
            z                   = 600,
            y                   = 67190,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39440,
            z                   = 600,
            y                   = 67960,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39510,
            z                   = 600,
            y                   = 67480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40620,
            z                   = 600,
            y                   = 67910,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40420,
            z                   = 600,
            y                   = 67930,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40780,
            z                   = 600,
            y                   = 67090,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40390,
            z                   = 600,
            y                   = 67140,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 38760,
            z                   = 600,
            y                   = 67050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39040,
            z                   = 600,
            y                   = 67220,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39910,
            z                   = 500,
            y                   = 67970,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 38760,
            z                   = 500,
            y                   = 67940,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40080,
            z                   = 500,
            y                   = 66980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 40770,
            z                   = 500,
            y                   = 67760,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x7B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x7B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x7B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 35580,
            triggerZ            = 0,
            triggerY            = 74990,
            triggerRange        = 1000,
            actorX              = 34500,
            actorZ              = 1500,
            actorY              = 75200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x7D6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_870',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E8',
    )

    Jump('loc_86A')

    def _loc_7E8(): pass

    label('loc_7E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F3',
    )

    Jump('loc_86A')

    def _loc_7F3(): pass

    label('loc_7F3')

    SetChrChipByIndex(0x001C, 35)
    SetChrChipByIndex(0x001D, 36)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
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
    SetChrPos(0x000C, 41270, 0, 71880, 270)
    CreateThread(0x000C, 0x00, 0x06, 0x0002)
    SetChrFlags(0x000C, 0x0010)

    def _loc_86A(): pass

    label('loc_86A')

    OP_A2(0x000F)

    Jump('loc_983')

    def _loc_870(): pass

    label('loc_870')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_89A',
    )

    SetChrPos(0x000B, 37110, 0, 127270, 360)
    CreateThread(0x000B, 0x00, 0x06, 0x0002)
    ClearChrFlags(0x0011, 0x0080)
    OP_A2(0x000F)

    Jump('loc_983')

    def _loc_89A(): pass

    label('loc_89A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_901',
    )

    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x000A, 86530, 0, 81370, 133)
    SetChrPos(0x000B, 87000, 0, 79140, 90)
    CreateThread(0x000B, 0x00, 0x06, 0x0002)
    SetChrPos(0x000C, 34500, 0, 75200, 90)
    CreateThread(0x000C, 0x00, 0x06, 0x0002)
    OP_A3(0x000F)

    Jump('loc_983')

    def _loc_901(): pass

    label('loc_901')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_946',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x000A, 87000, 0, 79140, 90)
    SetChrPos(0x000C, 34500, 0, 75200, 90)
    CreateThread(0x000C, 0x00, 0x06, 0x0002)
    OP_A3(0x000F)

    Jump('loc_983')

    def _loc_946(): pass

    label('loc_946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_97B',
    )

    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 36550, 0, 72670, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 5, 0x1895)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_975',
    )

    SetChrFlags(0x0008, 0x0010)

    def _loc_975(): pass

    label('loc_975')

    OP_A2(0x000F)

    Jump('loc_983')

    def _loc_97B(): pass

    label('loc_97B')

    ClearChrFlags(0x000D, 0x0080)
    OP_A2(0x000F)

    def _loc_983(): pass

    label('loc_983')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_994',
    )

    OP_A3(0x10F0)
    Event(0, 0x0019)

    Jump('loc_9A7')

    def _loc_994(): pass

    label('loc_994')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_9A7',
    )

    SetMapFlags(0x10000000)
    OP_A3(0x10F1)
    Event(2, 0x0000)

    def _loc_9A7(): pass

    label('loc_9A7')

    Return()

# id: 0x0001 offset: 0x9A8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_9B2',
    )

    Jump('loc_9DE')

    def _loc_9B2(): pass

    label('loc_9B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_9C3',
    )

    OP_6F(0x0000, 10)

    Jump('loc_9DE')

    def _loc_9C3(): pass

    label('loc_9C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_9D4',
    )

    OP_6F(0x0000, 10)

    Jump('loc_9DE')

    def _loc_9D4(): pass

    label('loc_9D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_9DE',
    )

    Jump('loc_9DE')

    def _loc_9DE(): pass

    label('loc_9DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9F0',
    )

    Jump('loc_A0F')

    def _loc_9F0(): pass

    label('loc_9F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9FB',
    )

    Jump('loc_A0F')

    def _loc_9FB(): pass

    label('loc_9FB')

    OP_D2(0x000700A9, 0x000700AD, 0x23)
    OP_D2(0x000700CB, 0x000700CF, 0x24)

    def _loc_A0F(): pass

    label('loc_A0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_A2F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_A2F',
    )

    Call(0, 0x001A)

    def _loc_A2F(): pass

    label('loc_A2F')

    Return()

# id: 0x0002 offset: 0xA30
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BDF',
    )

    Sleep(3000)

    OP_8E(0x00FE, 43100, 1500, 78900, 2500, 0x00)
    OP_8B(0x00FE, 0x000186A0, 0x00013434, 0x01F4)
    Sleep(3000)

    OP_8E(0x00FE, 42935, 1500, 77000, 2000, 0x00)
    OP_8E(0x00FE, 42907, 1500, 76200, 2000, 0x00)
    OP_8E(0x00FE, 42901, 0, 74390, 1000, 0x00)
    OP_8E(0x00FE, 41200, 0, 72000, 2500, 0x00)
    OP_8B(0x00FE, 0x00000000, 0x00011940, 0x01F4)
    Sleep(3000)

    OP_8E(0x00FE, 42800, 0, 65500, 2000, 0x00)
    OP_8B(0x00FE, 0x000186A0, 0x0000FFDC, 0x01F4)
    Sleep(3000)

    OP_8E(0x00FE, 34900, 0, 63860, 2500, 0x00)
    OP_8B(0x00FE, 0x00000000, 0x0000F938, 0x01F4)
    Sleep(3000)

    OP_8B(0x00FE, 0x000186A0, 0x0000F938, 0x01F4)
    OP_8E(0x00FE, 37100, 0, 64500, 2000, 0x00)
    OP_8E(0x00FE, 37700, 0, 67200, 2500, 0x00)
    OP_8B(0x00FE, 0x000186A0, 0x00010680, 0x01F4)
    Sleep(3000)

    OP_8E(0x00FE, 33200, 0, 69000, 2000, 0x00)
    OP_8E(0x00FE, 33200, 0, 74200, 2500, 0x00)
    OP_8B(0x00FE, 0x00000000, 0x000121D8, 0x01F4)
    Sleep(3000)

    OP_8E(0x00FE, 35120, 0, 78350, 2000, 0x00)
    OP_8E(0x00FE, 36400, 0, 78810, 2000, 0x00)
    OP_8E(0x00FE, 40200, 1500, 78700, 2500, 0x00)
    OP_8B(0x00FE, 0x00009D08, 0x00000000, 0x01F4)

    Jump('ReInit')

    def _loc_BDF(): pass

    label('loc_BDF')

    Return()

# id: 0x0003 offset: 0xBE0
@scena.Code('func_03_BE0')
def func_03_BE0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C91',
    )

    Sleep(3000)

    OP_8E(0x00FE, 36450, 0, 123500, 2000, 0x00)
    OP_8B(0x00FE, 0x00000000, 0x0001E26C, 0x01F4)
    Sleep(3000)

    OP_8E(0x00FE, 36450, 0, 126300, 2000, 0x00)
    OP_8B(0x00FE, 0x00000000, 0x0001ED5C, 0x01F4)
    Sleep(3000)

    OP_8E(0x00FE, 39600, 0, 127700, 2500, 0x00)
    OP_8B(0x00FE, 0x00009AB0, 0x00030D40, 0x01F4)
    Sleep(3000)

    OP_8B(0x00FE, 0x00000000, 0x0001F2D4, 0x01F4)
    OP_8E(0x00FE, 36450, 0, 126300, 2000, 0x00)
    OP_8B(0x00FE, 0x00000000, 0x0001ED5C, 0x01F4)

    Jump('func_03_BE0')

    def _loc_C91(): pass

    label('loc_C91')

    Return()

# id: 0x0004 offset: 0xC92
@scena.Code('func_04_C92')
def func_04_C92():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_CA0',
    )

    Call(0, 0x0005)

    Jump('loc_CA4')

    def _loc_CA0(): pass

    label('loc_CA0')

    Call(0, 0x0008)

    def _loc_CA4(): pass

    label('loc_CA4')

    Return()

# id: 0x0005 offset: 0xCA5
@scena.Code('func_05_CA5')
def func_05_CA5():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E86',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 3, 0x20A3)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_E86',
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
            TXT(0x02, '招牌菜『三蛋黄杂烩粥』　1600米拉\n'),
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
        'loc_D55',
    )

    FadeIn(300, 0)
    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D4D',
    )

    OP_A9(0x09)

    Jump('loc_D4F')

    def _loc_D4D(): pass

    label('loc_D4D')

    OP_A9(0x04)

    def _loc_D4F(): pass

    label('loc_D4F')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_D55(): pass

    label('loc_D55')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E63',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x640),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_E2E',
    )

    SubMira(1600)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x000B, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '三蛋黄杂烩粥',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFD, 2000)
    SetChrStatus(ChrTable['约修亚'], 0xFD, 2000)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFD, 2000)
    SetChrStatus(ChrTable['奥利维尔'], 0xFD, 2000)
    SetChrStatus(ChrTable['科洛丝'], 0xFD, 2000)
    SetChrStatus(ChrTable['阿加特'], 0xFD, 2000)
    SetChrStatus(ChrTable['提妲'], 0xFD, 2000)
    SetChrStatus(ChrTable['金'], 0xFD, 2000)
    SetChrStatus(ChrTable['凯文神父'], 0xFD, 2000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E20',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0006)"),
            Expr.Return,
        ),
        'loc_DF4',
    )

    Jump('loc_E20')

    def _loc_DF4(): pass

    label('loc_DF4')

    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '三蛋黄杂烩粥',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E20(): pass

    label('loc_E20')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_E54')

    def _loc_E2E(): pass

    label('loc_E2E')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_E54(): pass

    label('loc_E54')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000A)

    Return()

    def _loc_E63(): pass

    label('loc_E63')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E7D',
    )

    FadeIn(300, 0)
    TalkEnd(0x000A)

    Return()

    def _loc_E7D(): pass

    label('loc_E7D')

    FadeIn(300, 0)

    def _loc_E86(): pass

    label('loc_E86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 3, 0x20A3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1274',
    )

    ChrTalk(
        0x000A,
        (
            '欢迎光临～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000A, 0x0102, 400)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊，这不是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F好久不见啦，伊莉莎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '太好了，总算放心了。\n',
            '看起来似乎很有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你终于回来了啊！\n',
            '我都快担心死了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的～艾丝蒂尔每次\n',
            '都带不同的男人回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '难道和约修亚\n',
            '闹别扭了吗？\n',
            '真让人不放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1054F哈、哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '抱歉，\n',
            '让你担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F不、不愧是伊莉莎……\n',
            '担心的东西都和别人不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '那么……\n',
            '你们二位，打算怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这次是否准备\n',
            '多休息一下再走？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯、我也想那样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过还是要看\n',
            '情况而定了。',
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
        'loc_1100',
    )

    ChrTalk(
        0x0103,
        (
            '#021F嗯、稍微放松一下也无所谓，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不管是谁也都需要\n',
            '偶尔休息一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11C0')

    def _loc_1100(): pass

    label('loc_1100')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_116A',
    )

    ChrTalk(
        0x0108,
        (
            '#070F啊，稍微放松一下\n',
            '也没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不管有什么重大任务，\n',
            '我们游击士毕竟也只是普通人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11C0')

    def _loc_116A(): pass

    label('loc_116A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11C0',
    )

    ChrTalk(
        0x0106,
        (
            '#051F哈～稍微休息一下也没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是可不能放松过头\n',
            '把正事忘了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11C0(): pass

    label('loc_11C0')

    ChrTalk(
        0x000A,
        (
            '那么，等工作完成之后\n',
            '要再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还想让约修亚见识一下\n',
            '我充满自信的新料理呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F伊莉莎的新料理吗……\n',
            '那可是一定要吃的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯！一定会再来吃！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)
    OP_A2(0x20A3)

    Jump('loc_16AF')

    def _loc_1274(): pass

    label('loc_1274')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1380',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12DE',
    )

    ChrTalk(
        0x000A,
        (
            '我的料理已经\n',
            '被写到菜单上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这可是我充满自信的作品，\n',
            '希望约修亚也能尝一尝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137D')

    def _loc_12DE(): pass

    label('loc_12DE')

    ChrTalk(
        0x000A,
        (
            '今天的客人\n',
            '似乎不同寻常啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好象在举办结婚仪式的庆祝会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不但忙得要死，\n',
            '而且导力器也不能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呼～今天早上的工作\n',
            '简直就是战场啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0006)
    OP_A2(0x0005)

    def _loc_137D(): pass

    label('loc_137D')

    Jump('loc_16AF')

    def _loc_1380(): pass

    label('loc_1380')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_14B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_144F',
    )

    ChrTalk(
        0x000A,
        (
            '啊～艾丝蒂尔和约修亚～\n',
            '欢迎光临～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '抱歉啊，这里乱的很，\n',
            '其实正在举办结婚仪式的庆祝会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '所以今天早上的厨房\n',
            '简直就是恐怖的战场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不但忙得要死，\n',
            '而且导力器也不能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_14AD')

    def _loc_144F(): pass

    label('loc_144F')

    ChrTalk(
        0x000A,
        (
            '所以今天早上的厨房\n',
            '简直就是恐怖的战场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '准备庆祝会忙得要死，\n',
            '而且导力器也不能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14AD(): pass

    label('loc_14AD')

    Jump('loc_16AF')

    def _loc_14B0(): pass

    label('loc_14B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_15A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_154D',
    )

    ChrTalk(
        0x000A,
        (
            '啊！欢迎光临～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '庆祝会的料理终于\n',
            '准备完成了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好期待结婚仪式结束之后\n',
            '客人们赶快过来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呼～总算可以休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_159F')

    def _loc_154D(): pass

    label('loc_154D')

    ChrTalk(
        0x000A,
        (
            '庆祝会的料理终于\n',
            '准备完成了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '导力器无法使用，\n',
            '干什么都比平时花时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_159F(): pass

    label('loc_159F')

    Jump('loc_16AF')

    def _loc_15A2(): pass

    label('loc_15A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1665',
    )

    ChrTalk(
        0x000A,
        (
            '啊～艾丝蒂尔和约修亚～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天有人预约在店里\n',
            '举办庆祝会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '所以我和爸爸从一大早\n',
            '开始就忙个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不仅如此，而且连导力器\n',
            '也都不能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的～简直要累死人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_16AF')

    def _loc_1665(): pass

    label('loc_1665')

    ChrTalk(
        0x000A,
        (
            '不但要准备庆祝会，\n',
            '而且导力器也不能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我和爸爸都快\n',
            '忙死了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16AF(): pass

    label('loc_16AF')

    Jump('loc_25B1')

    def _loc_16B2(): pass

    label('loc_16B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1A0E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 0, 0x1A60)),
            Expr.Return,
        ),
        'loc_1823',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1718',
    )

    ChrTalk(
        0x000A,
        (
            '那么浓的雾，\n',
            '竟然这么快就散去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是让人觉得\n',
            '不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B9')

    def _loc_1718(): pass

    label('loc_1718')

    ChrTalk(
        0x000A,
        (
            '妈妈醒来的时候，\n',
            '天已经完全放晴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那么浓的雾，\n',
            '却这么快就散去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '妈妈昏睡过去的原因\n',
            '到现在也让人想不通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这次的事件还\n',
            '真是让人奇怪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_17B9(): pass

    label('loc_17B9')

    Jump('loc_1820')

    def _loc_17BC(): pass

    label('loc_17BC')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '妈妈的事\n',
            '多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '雾散了，\n',
            '店里也恢复了正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今后也要更加\n',
            '努力制作料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1820(): pass

    label('loc_1820')

    Jump('loc_1A0B')

    def _loc_1823(): pass

    label('loc_1823')

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊～艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我妈妈醒来了呢。\n',
            '真是太谢谢你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呜、真的太感谢了… \n',
            '……实在太好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F伊莉莎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，我也松了一口气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0103, 400)

    ChrTalk(
        0x000A,
        (
            '……雪拉姐也是。\n',
            '真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#524F没什么……\n',
            '能帮上忙我也很高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '今后也要多帮助\n',
            '托露塔阿姨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是！我一定会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '下次再叫上爱娜\n',
            '一起来喝酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F呵呵，我很期待呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#525F也向福克纳\n',
            '问声好吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F哇……',
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
        'loc_1A05',
    )

    ChrTalk(
        0x0104,
        (
            '#034F这、这是死亡宣告啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A05(): pass

    label('loc_1A05')

    OP_A2(0x1A60)
    OP_A2(0x0006)
    def _loc_1A0B(): pass

    label('loc_1A0B')

    Jump('loc_25B1')

    def _loc_1A0E(): pass

    label('loc_1A0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1B9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1A71',
    )

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '拜托了，不要乱来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '连艾丝蒂尔也倒下的话…\n',
            '我该怎么办才好啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B9C')

    def _loc_1A71(): pass

    label('loc_1A71')

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '啊～艾丝蒂尔，还有大家，\n',
            '以后要再来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '……不过，发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔的表情\n',
            '好像很消沉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F啊、没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F不要紧，我没事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真的吗？\n',
            '你是太累了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然工作应该努力，\n',
            '但也不要太勉强自己啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_1B9C(): pass

    label('loc_1B9C')

    Jump('loc_25B1')

    def _loc_1B9F(): pass

    label('loc_1B9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1C97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1BF1',
    )

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔你们\n',
            '要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '雾好像比昨天\n',
            '更加浓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C94')

    def _loc_1BF1(): pass

    label('loc_1BF1')

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '啊～艾丝蒂尔和大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '妈妈的样子从昨天\n',
            '开始就一直没变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '下次再来看看有\n',
            '什么情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我、今天要守在\n',
            '妈妈身旁… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_1C94(): pass

    label('loc_1C94')

    Jump('loc_25B1')

    def _loc_1C97(): pass

    label('loc_1C97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_214D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 2, 0x1882)),
            Expr.Return,
        ),
        'loc_1D7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D2D',
    )

    ChrTalk(
        0x000A,
        (
            '外边的雾还\n',
            '真厉害啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '店里虽然还没关系，\n',
            '但阳台的椅子也要去收拾一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总这样下去的话，\n',
            '潮湿可真是让人受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D7C')

    def _loc_1D2D(): pass

    label('loc_1D2D')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '无论如何，今天就\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '有兴趣的话尝尝\n',
            '我的新料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D7C(): pass

    label('loc_1D7C')

    Jump('loc_214A')

    def _loc_1D7F(): pass

    label('loc_1D7F')

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊…这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0103, 400)

    ChrTalk(
        0x000A,
        (
            '连雪拉扎德小姐也来拉！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵～最近还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿、真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '太好了～～\n',
            '看来训练顺利结束了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我真是好担心呢～\n',
            '总算是回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F现在有些工作，\n',
            '才在各地来回跑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所以一直到现在\n',
            '才回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵～果然很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对了，听说训练\n',
            '是在国外进行的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还真是厉害呀，\n',
            '游击士果然是国际性的职业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F哈哈，哪里～\n',
            '过奖过奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说是国外，\n',
            '但也只是协会的设施而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F……～不过也多亏这次训练\n',
            '让我转换心情下定决心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呼～是下定决心啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那么…那条裙子\n',
            '也是你决心的表现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F啊……\n',
            '果然注意到了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1013F那个……是不是很奇怪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哪里的话啊～\n',
            '很适合你的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然式样可爱，\n',
            '但却活动方便，一点也不累赘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，和艾丝蒂尔真是绝配啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F谢、谢谢称赞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我明白约修亚的事情\n',
            '给你带来了很大压力…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过一定要保持现在的精神继续努力啊！\n',
            '那样才像艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嗯、嗯……我会加油的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1882)
    OP_A2(0x0005)
    def _loc_214A(): pass

    label('loc_214A')

    Jump('loc_25B1')

    def _loc_214D(): pass

    label('loc_214D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_25B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 3, 0x102B)),
            Expr.Return,
        ),
        'loc_21CF',
    )

    ChrTalk(
        0x000A,
        (
            '对啦对啦～艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F啊，还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '缇欧可是\n',
            '很想你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '农场的那些\n',
            '孩子也是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25B1')

    def _loc_21CF(): pass

    label('loc_21CF')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '欢迎光临……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F伊莉莎，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '什么好久不见嘛～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '自从你去了柏斯以后\n',
            '就一直没回来过！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F啊、因为发生了很多事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#008F总之让你担心了，对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '事情我也听说了，\n',
            '你终于升为正游击士了，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对了，我也终于可以\n',
            '下厨做料理了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F好棒啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嘿嘿嘿，那就经常来尝尝\n',
            '我亲手作的料理吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，那是一定的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……好了，寒暄结束，\n',
            '转入正题吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F……正题？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '别再装傻啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '（你和约修亚怎么了？\n',
            '　那个男人又是谁～？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F（啊…………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#008F（你、你误会啦！！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#503F（凯文先生是担心我孤身一人，\n',
            '　才会陪同一起的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '（喔……担心你孤身一人，\n',
            '　所以陪同一起…吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#504F啊啊啊啊啊……\n',
            '总之不是你想象中的那样啦！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#506F这就要回家\n',
            '去见约修亚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好了，今天就\n',
            '聊到这里吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我也要开始工作了，\n',
            '下次你一定要带上约修亚，三个人一起来啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看起来似乎有很多\n',
            '有趣的内情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F呵呵呵……\n',
            '都说了不是你想的那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x102B)

    def _loc_25B1(): pass

    label('loc_25B1')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x25B5
@scena.Code('func_06_25B5')
def func_06_25B5():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2BD7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 1, 0x20A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_295C',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '噢、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '怎么回事，今天连\n',
            '约修亚也一起来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '噢！平安无事就比什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天在洛连特有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯……有些麻烦\n',
            '的事情需要处理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '德瑟鲁大叔似乎\n',
            '很烦恼的样子啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊～导力炉没法用了，\n',
            '真让人头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_2795',
    )

    ChrTalk(
        0x00FE,
        (
            '这样一来，庆祝会的料理\n',
            '可要费力气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F哈，果然是专业的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F这就是厨师的自尊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '必须借助道具才能做菜的厨师\n',
            '便不能算是一流的厨师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_2795(): pass

    label('loc_2795')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_282C',
    )

    ChrTalk(
        0x00FE,
        (
            '今天这里要\n',
            '举办一个庆祝会呢。',
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
            '#1004F庆、庆祝会吗……\n',
            '那么料理准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，总算是都\n',
            '准备好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_282C(): pass

    label('loc_282C')

    ChrTalk(
        0x00FE,
        (
            '今天这里要\n',
            '举办一个庆祝会呢。',
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
            '#1004F庆、庆祝会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F准备料理\n',
            '的事没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '一流的厨师可不能没了道具\n',
            '就什么都干不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28DC(): pass

    label('loc_28DC')

    ChrTalk(
        0x00FE,
        (
            '当然了，还是很希望\n',
            '赶快恢复正常…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以一切就拜托\n',
            '你们游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F啊……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F我们会尽力的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20A1)

    Jump('loc_2BD4')

    def _loc_295C(): pass

    label('loc_295C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_2A60',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29F8',
    )

    ChrTalk(
        0x00FE,
        (
            '看来庆祝会\n',
            '办得很顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欢声笑语、祝福的言辞，\n',
            '还有丰富美味的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，真是完美啊！\n',
            '对厨师来说，这就是最幸福的一刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_2A5D')

    def _loc_29F8(): pass

    label('loc_29F8')

    ChrTalk(
        0x00FE,
        (
            '看来庆祝会\n',
            '办得很顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，接下来\n',
            '该准备甜品了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '预定品种是香槟酒口味\n',
            '的冰淇淋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A5D(): pass

    label('loc_2A5D')

    Jump('loc_2BD4')

    def _loc_2A60(): pass

    label('loc_2A60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2B43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AEC',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，庆祝会的料理\n',
            '终于全部做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今日的主打菜式是\n',
            '香草为配料的肉料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，料理的香气\n',
            '这里都能闻到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_2B40')

    def _loc_2AEC(): pass

    label('loc_2AEC')

    ChrTalk(
        0x00FE,
        (
            '庆祝会的主打菜式是\n',
            '香草为配料的肉料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～料理的香气让\n',
            '身体彻底放松了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B40(): pass

    label('loc_2B40')

    Jump('loc_2BD4')

    def _loc_2B43(): pass

    label('loc_2B43')

    ChrTalk(
        0x00FE,
        (
            '导力炉无法使用\n',
            '确实让人头疼…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但不借助工具就不会做菜的人，\n',
            '根本就不能算是真正的厨师！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼！就算只用手边的工具，\n',
            '我也一定能完成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2BD4(): pass

    label('loc_2BD4')

    Jump('loc_3582')

    def _loc_2BD7(): pass

    label('loc_2BD7')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2C90',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏布露姆老奶奶，\n',
            '总算学会了那道菜的做法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然烹饪方法很复杂，\n',
            '但我会努力掌握，\n',
            '然后加到菜单中的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天真的是\n',
            '多谢各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，接下来也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3582')

    def _loc_2C90(): pass

    label('loc_2C90')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_2CA2',
    )

    Call(1, 0x0006)

    Jump('loc_3582')

    def _loc_2CA2(): pass

    label('loc_2CA2')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_2CB4',
    )

    Call(1, 0x0005)

    Jump('loc_3582')

    def _loc_2CB4(): pass

    label('loc_2CB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_2D1B',
    )

    ChrTalk(
        0x00FE,
        (
            '调查的事就拜托各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '找到食谱以后\n',
            '别忘了马上来报告啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '另外食材也不要忘记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3582')

    def _loc_2D1B(): pass

    label('loc_2D1B')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_2DA7',
    )

    ChrTalk(
        0x00FE,
        (
            '哟、艾丝蒂尔。\n',
            '调查进行得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '找到食谱以后\n',
            '别忘了马上来报告啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，到那时\n',
            '食材也不要忘记啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3582')

    def _loc_2DA7(): pass

    label('loc_2DA7')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_2DCA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_2DC3',
    )

    Call(1, 0x0001)

    Jump('loc_2DC7')

    def _loc_2DC3(): pass

    label('loc_2DC3')

    Call(1, 0x0000)

    def _loc_2DC7(): pass

    label('loc_2DC7')

    Jump('loc_3582')

    def _loc_2DCA(): pass

    label('loc_2DCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2F0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2E60',
    )

    ChrTalk(
        0x00FE,
        (
            '雾散了，托露塔也醒来了。\n',
            '总算是让人松了口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，你们今天也\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想点什么请随意说！\n',
            '我会认真做的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F0C')

    def _loc_2E60(): pass

    label('loc_2E60')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔，还有大家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的\n',
            '托露塔也醒来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次真是快\n',
            '担心死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得来一次，\n',
            '今天就多待一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会给\n',
            '大家制作最拿手的料理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2F0C(): pass

    label('loc_2F0C')

    Jump('loc_3582')

    def _loc_2F0F(): pass

    label('loc_2F0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_3029',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2F5D',
    )

    ChrTalk(
        0x00FE,
        (
            '托露塔\n',
            '好像睡得很舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '完全都不知道别人有多担心…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3026')

    def _loc_2F5D(): pass

    label('loc_2F5D')

    ChrTalk(
        0x00FE,
        (
            '趁着早上有空，\n',
            '来看看她的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她似乎完全都没察觉到，\n',
            '睡得那么熟… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，不过看到她那熟睡的样子，\n',
            '也算是放心多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，要赶快\n',
            '回厨房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不然福克纳一定\n',
            '又会大喊大叫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_3026(): pass

    label('loc_3026')

    Jump('loc_3582')

    def _loc_3029(): pass

    label('loc_3029')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_3145',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_30A2',
    )

    ChrTalk(
        0x00FE,
        (
            '托露塔的样子没什么变化。\n',
            '睡得很熟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是没吃早饭的话，\n',
            '就在这里吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还能增加些人气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3142')

    def _loc_30A2(): pass

    label('loc_30A2')

    ChrTalk(
        0x00FE,
        (
            '啊，今天早上雾还是这么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天就很担心，\n',
            '托露塔的样子没什么变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但听了教区长的话之后\n',
            '就平静不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～现在也只有\n',
            '安安静静地观望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_3142(): pass

    label('loc_3142')

    Jump('loc_3582')

    def _loc_3145(): pass

    label('loc_3145')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_33D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 3, 0x1893)),
            Expr.Return,
        ),
        'loc_32D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3249',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_31B1',
    )

    ChrTalk(
        0x00FE,
        (
            '雾实在太大，\n',
            '在一楼什么都看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望别持续太久，\n',
            '早点天晴吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3246')

    def _loc_31B1(): pass

    label('loc_31B1')

    ChrTalk(
        0x00FE,
        (
            '今天外边的雾\n',
            '还是很大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真担心我的店啊，\n',
            '在一楼什么都看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这些雾\n',
            '而没法进货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的店全都是\n',
            '选用最新鲜的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_3246(): pass

    label('loc_3246')

    Jump('loc_32D0')

    def _loc_3249(): pass

    label('loc_3249')

    ChrTalk(
        0x00FE,
        (
            '话虽如此……\n',
            '今天怎么这么大雾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真担心我的店啊，\n',
            '在一楼什么都看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，反正不影响正常营业，\n',
            '还是努力工作去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_32D0(): pass

    label('loc_32D0')

    Jump('loc_33D3')

    def _loc_32D3(): pass

    label('loc_32D3')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔和雪拉扎德。\n',
            '好久不见了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，最近还好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，还是和以前一样，\n',
            '生意很不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '伊莉莎的新料理\n',
            '也很受好评呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作之余就来\n',
            '这里休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1893)
    OP_A2(0x0004)
    def _loc_33D3(): pass

    label('loc_33D3')

    Jump('loc_3582')

    def _loc_33D6(): pass

    label('loc_33D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_3582',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0209, 3, 0x104B)),
            Expr.Return,
        ),
        'loc_343D',
    )

    ChrTalk(
        0x00FE,
        (
            '对了对了，我们增加\n',
            '了新菜式哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是『三蛋黄杂烩粥』。\n',
            '有兴趣的话来尝尝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3582')

    def _loc_343D(): pass

    label('loc_343D')

    ChrTalk(
        0x00FE,
        (
            '哟！欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(700)

    ChrTurnDirection(0x000B, 0x0101, 300)

    ChrTalk(
        0x00FE,
        (
            '啊、这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F德瑟鲁大叔，您很有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，我一向都是如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在心情好的时候制作的料理，\n',
            '客人吃起来会更觉得美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F哈哈，确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，我们增加\n',
            '了新菜式哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是『三蛋黄杂烩粥』。\n',
            '有兴趣的话来尝尝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x104B)

    def _loc_3582(): pass

    label('loc_3582')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x3586
@scena.Code('func_07_3586')
def func_07_3586():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3B42',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 2, 0x20A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_394C',
    )

    ChrTurnDirection(0x0008, 0x0102, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊……！？\n',
            '艾丝蒂尔和约修亚',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊！你们两个\n',
            '终于一起回来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……\n',
            '让您久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了，托露塔阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，不用那么正经啦，\n',
            '又不是外人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们两个……\n',
            '正赶在这种非常时期回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1026F啊、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F店里没什么问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，还好，先生和\n',
            '伊莉莎一直都很努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是…进货现在\n',
            '成了大问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船和搬运车\n',
            '都动不了了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1043F果然，物流问题很严重呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个对店里的影响很大，\n',
            '实在让人头疼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～为什么讨厌的事件\n',
            '一直发生个没完呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F确实如此呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F不过我们游击士一定\n',
            '会努力解决这一切的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然也许要花些时间，\n',
            '但肯定会让一切都恢复正常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F当然了，不仅是我们在努力，\n',
            '王国军也一直在努力思考对策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在转机出现之前，\n',
            '请阿姨也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊…\n',
            '现在正是考验人的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，总之只有努力\n',
            '坚持下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然了，我也会期待\n',
            '你们的好消息。',
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
        'loc_3943',
    )

    ChrTalk(
        0x0103,
        (
            '#020F嗯！我们一定会尽力而为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3943(): pass

    label('loc_3943')

    OP_A2(0x000E)
    OP_A2(0x20A2)

    Jump('loc_3B3F')

    def _loc_394C(): pass

    label('loc_394C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_39B2',
    )

    ChrTalk(
        0x00FE,
        (
            '店里的情况虽然很头疼，\n',
            '但也只能努力坚持下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然了，我也会期待\n',
            '你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B3F')

    def _loc_39B2(): pass

    label('loc_39B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_3AB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A5D',
    )

    ChrTalk(
        0x00FE,
        (
            '似乎庆祝会\n',
            '顺利结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然进货问题还是让人头疼，\n',
            '但只要努力，\n',
            '总会有解决的办法…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，只要保持现在的斗志，\n',
            '一定可以坚持营业下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    Jump('loc_3AB3')

    def _loc_3A5D(): pass

    label('loc_3A5D')

    ChrTalk(
        0x00FE,
        (
            '似乎庆祝会\n',
            '顺利结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，只要保持现在的斗志，\n',
            '一定可以坚持营业下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AB3(): pass

    label('loc_3AB3')

    Jump('loc_3B3F')

    def _loc_3AB6(): pass

    label('loc_3AB6')

    ChrTalk(
        0x00FE,
        (
            '要是店附近能\n',
            '有个农场就好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王都和柏斯的店\n',
            '一定也都遇到大麻烦了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在我已经无暇顾及别人了，\n',
            '但实在无法不去关心…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B3F(): pass

    label('loc_3B3F')

    Jump('loc_4621')

    def _loc_3B42(): pass

    label('loc_3B42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_4152',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 7, 0x1A5F)),
            Expr.Return,
        ),
        'loc_3C49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_3BD7',
    )

    ChrTalk(
        0x0008,
        (
            '很遗憾，\n',
            '我不知道那道料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在我开始学烹饪的时候，\n',
            '就已经没人做那道菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还是找更年长的人问问\n',
            '可能比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C46')

    def _loc_3BD7(): pass

    label('loc_3BD7')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0080)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C02',
    )

    Call(1, 0x0004)

    Jump('loc_3C46')

    def _loc_3C02(): pass

    label('loc_3C02')

    ChrTalk(
        0x00FE,
        (
            '有空的话\n',
            '就再来店里玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和伊莉莎一起，\n',
            '期待你们回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C46(): pass

    label('loc_3C46')

    Jump('loc_414F')

    def _loc_3C49(): pass

    label('loc_3C49')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊……艾丝蒂尔、\n',
            '还有雪拉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F您好，托露塔阿姨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1025F太好了。\n',
            '您终于醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F身体现在怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '啊啊～还有点\n',
            '恍惚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是做了个\n',
            '奇怪的梦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1026F啊、果然，\n',
            '阿姨也做了梦吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯、很让人怀念的梦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在梦中，我回到了艾丝蒂尔这么大的年龄，\n',
            '和大家一起玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '主日学校时代的朋友……\n',
            '汉娜和莱娜也都在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F啊？莱娜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '妈妈也出现了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不只是你妈妈哦，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连你和约修亚\n',
            '也都在一起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且就是现在这种年龄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1020F咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F果然是有趣的梦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，很奇妙的情景吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然在梦境中的\n',
            '经历很快乐…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但因为太过幸福，反而有些不真实，\n',
            '让我一直隐隐感到不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎一切都像是人造的幻境，\n',
            '清醒之后越想越是毛骨悚然…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '不过、再次看到了莱娜，\n',
            '真的很高兴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许是你妈妈借着这次的机会，\n',
            '来到我的梦中和我相见吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平常一直都在女神的身旁默默注视着我们，\n',
            '这次终于忍耐不住了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F啊哈哈……那也说不定吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然还是不明白……\n',
            '不过我也那么想啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯、不过我究竟能否达到妈妈的期望呢，\n',
            '说实话，还是很没自信呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不用担心，你没问题的，\n',
            '这一点我就可以确定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，拿出自信来，\n',
            '继续努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你现在已经是个很厉害的游击士了，\n',
            '无论各方面都很优秀呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯……谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A5F)
    def _loc_414F(): pass

    label('loc_414F')

    Jump('loc_4621')

    def _loc_4152(): pass

    label('loc_4152')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4470',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 5, 0x1895)),
            Expr.Return,
        ),
        'loc_41C8',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '现在你们看起来很忙，\n',
            '但以后有空的话一定再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔的话，\n',
            '我可是随时欢迎的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_446D')

    def _loc_41C8(): pass

    label('loc_41C8')

    ClearChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '……那么，我去\n',
            '检查帐本了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0008)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔，\n',
            '还有雪拉也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F托露塔阿姨，您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，看起来很热闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以的话你们也来\n',
            '吃点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '伊莉莎的新料理\n',
            '最近大受好评了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F啊，那当然要尝尝！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1001F伊莉莎的料理\n',
            '肯定很期待啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '呵呵，敬请期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那孩子也一直\n',
            '都很想见艾丝蒂尔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在品尝料理的时候\n',
            '顺便见上一面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 2, 0x1882)),
            Expr.Return,
        ),
        'loc_441D',
    )

    ChrTalk(
        0x0101,
        (
            '#1017F呵呵，其实\n',
            '我们都已经见过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也要再\n',
            '来啊!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔的话，\n',
            '随时欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_446A')

    def _loc_441D(): pass

    label('loc_441D')

    ChrTalk(
        0x0101,
        (
            '#1017F嗯，一定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也要再\n',
            '来啊!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔的话，\n',
            '随时欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_446A(): pass

    label('loc_446A')

    OP_A2(0x1895)

    def _loc_446D(): pass

    label('loc_446D')

    Jump('loc_4621')

    def _loc_4470(): pass

    label('loc_4470')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_4621',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0209, 2, 0x104A)),
            Expr.Return,
        ),
        'loc_44C0',
    )

    ChrTalk(
        0x00FE,
        (
            '我们一家一直都很健康呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时间的话，\n',
            '随时过来玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4621')

    def _loc_44C0(): pass

    label('loc_44C0')

    ChrTalk(
        0x00FE,
        (
            '嗯，受政变的影响，\n',
            '食材价格飞涨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 300)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x00FE,
        (
            '……艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久不见了啊！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F嘿嘿嘿，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让我吃了一惊！\n',
            '你什么时候回洛连特的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，刚刚下\n',
            '飞船没多久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀……\n',
            '伊莉莎看见你也会高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后一定多来\n',
            '店里玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，您不说\n',
            '我也会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……呵呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x104A)

    def _loc_4621(): pass

    label('loc_4621')

    TalkEnd(0x0008)

    Return()

# id: 0x0008 offset: 0x4625
@scena.Code('func_08_4625')
def func_08_4625():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47EE',
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
            TXT(0x02, '招牌菜『三蛋黄杂烩粥』　1600米拉\n'),
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
        'loc_46BD',
    )

    FadeIn(300, 0)
    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_46B5',
    )

    OP_A9(0x09)

    Jump('loc_46B7')

    def _loc_46B5(): pass

    label('loc_46B5')

    OP_A9(0x04)

    def _loc_46B7(): pass

    label('loc_46B7')

    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_46BD(): pass

    label('loc_46BD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47CB',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x640),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_4796',
    )

    SubMira(1600)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x000B, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '三蛋黄杂烩粥',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFD, 2000)
    SetChrStatus(ChrTable['约修亚'], 0xFD, 2000)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFD, 2000)
    SetChrStatus(ChrTable['奥利维尔'], 0xFD, 2000)
    SetChrStatus(ChrTable['科洛丝'], 0xFD, 2000)
    SetChrStatus(ChrTable['阿加特'], 0xFD, 2000)
    SetChrStatus(ChrTable['提妲'], 0xFD, 2000)
    SetChrStatus(ChrTable['金'], 0xFD, 2000)
    SetChrStatus(ChrTable['凯文神父'], 0xFD, 2000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4788',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0006)"),
            Expr.Return,
        ),
        'loc_475C',
    )

    Jump('loc_4788')

    def _loc_475C(): pass

    label('loc_475C')

    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '三蛋黄杂烩粥',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4788(): pass

    label('loc_4788')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_47BC')

    def _loc_4796(): pass

    label('loc_4796')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_47BC(): pass

    label('loc_47BC')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000C)

    Return()

    def _loc_47CB(): pass

    label('loc_47CB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47E5',
    )

    FadeIn(300, 0)
    TalkEnd(0x000C)

    Return()

    def _loc_47E5(): pass

    label('loc_47E5')

    FadeIn(300, 0)

    def _loc_47EE(): pass

    label('loc_47EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_4865',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_484B',
    )

    ChrTalk(
        0x000C,
        (
            '呼，还有宴会要办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好了，一鼓作气干完吧。\n',
            '我也要去忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x00FE, 0x0010)
    OP_A2(0x0000)

    Jump('loc_4862')

    def _loc_484B(): pass

    label('loc_484B')

    ChrTalk(
        0x000C,
        (
            '失陪～\n',
            '请自便吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4862(): pass

    label('loc_4862')

    Jump('loc_56E1')

    def _loc_4865(): pass

    label('loc_4865')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_49ED',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4990',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_494F',
    )

    ChrTalk(
        0x000C,
        (
            '啊……\n',
            '雪、雪拉扎德！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '难、难道说……\n',
            '工作已经结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，虽然暂时解决了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……但遗憾的是接下来\n',
            '还有不少事情要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊……是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那、那个……\n',
            '我会继续等的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_498D')

    def _loc_494F(): pass

    label('loc_494F')

    ChrTalk(
        0x000C,
        (
            '那、那个……\n',
            '我会继续等的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '有时间的时候\n',
            '要再来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_498D(): pass

    label('loc_498D')

    Jump('loc_49EA')

    def _loc_4990(): pass

    label('loc_4990')

    ChrTalk(
        0x000C,
        (
            '终于准备完庆祝会了，\n',
            '暂时可以休息一下啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '呼～其实我这个服务生\n',
            '接下来才要忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_49EA(): pass

    label('loc_49EA')

    Jump('loc_56E1')

    def _loc_49ED(): pass

    label('loc_49ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4BA1',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AE9',
    )

    ChrTurnDirection(0x000C, 0x0103, 0)

    ChrTalk(
        0x000C,
        (
            '啊……\n',
            '雪、雪拉扎德！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '喔、\n',
            '在工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯……太、太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F什么啊，怎么那种反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '啊……没、没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那、那个……\n',
            '我会继续等的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_4B1E')

    def _loc_4AE9(): pass

    label('loc_4AE9')

    ChrTalk(
        0x000C,
        (
            '那、那个……\n',
            '我会继续等的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '工作要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B1E(): pass

    label('loc_4B1E')

    Jump('loc_4B9E')

    def _loc_4B21(): pass

    label('loc_4B21')

    ChrTalk(
        0x000C,
        (
            '今天下午\n',
            '有团体预约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好像是结婚仪式的庆祝会，\n',
            '所以有的忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '导力式的烹饪器具都没法用，\n',
            '所以比平时还要累的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4B9E(): pass

    label('loc_4B9E')

    Jump('loc_56E1')

    def _loc_4BA1(): pass

    label('loc_4BA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_4E97',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0076, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CC9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4C0D',
    )

    ChrTalk(
        0x000C,
        (
            '那个布露姆老奶奶\n',
            '就像天使一样和善呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯……\n',
            '有点难以想象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CC6')

    def _loc_4C0D(): pass

    label('loc_4C0D')

    ChrTalk(
        0x000C,
        (
            '刚才的传统料理…\n',
            '还真是美味啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过，拉欧爷爷\n',
            '的印象还真是强烈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '竟然会对料理的味道\n',
            '那么执着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那个布露姆老奶奶\n',
            '就像天使一样和善呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯……\n',
            '有点难以想象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CC6(): pass

    label('loc_4CC6')

    Jump('loc_4E94')

    def _loc_4CC9(): pass

    label('loc_4CC9')

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_4DDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4D23',
    )

    ChrTalk(
        0x000C,
        (
            '今、今天所幸\n',
            '没有出现大事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这样暂时就\n',
            '可以松口气了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DD7')

    def _loc_4D23(): pass

    label('loc_4D23')

    ChrTalk(
        0x000C,
        (
            '哈，太好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '今、今天所幸\n',
            '没有出现大事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过，特地邀请爱娜小姐\n',
            '来喝酒…',
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
        'loc_4DB4',
    )

    ChrTalk(
        0x000C,
        (
            '奥利维尔先生…难道不想活了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DD7')

    def _loc_4DB4(): pass

    label('loc_4DB4')

    ChrTalk(
        0x000C,
        (
            '看来奥利维尔先生\n',
            '是想自杀呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DD7(): pass

    label('loc_4DD7')

    Jump('loc_4E94')

    def _loc_4DDA(): pass

    label('loc_4DDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4E2A',
    )

    ChrTalk(
        0x000C,
        (
            '雾散去了，\n',
            '定期船也恢复航行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '滞留的客人们\n',
            '都去飞船坪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E94')

    def _loc_4E2A(): pass

    label('loc_4E2A')

    ChrTalk(
        0x000C,
        (
            '太太她也终于\n',
            '清醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '阴影已经散去，\n',
            '好像一切都恢复原状了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我也要调整心情\n',
            '好好工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_4E94(): pass

    label('loc_4E94')

    Jump('loc_56E1')

    def _loc_4E97(): pass

    label('loc_4E97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_4F9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4EEE',
    )

    ChrTalk(
        0x000C,
        (
            '矿工们回来以后\n',
            '又要开始忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊啊、老板！\n',
            '快点回厨房吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F99')

    def _loc_4EEE(): pass

    label('loc_4EEE')

    ChrTalk(
        0x000C,
        (
            '矿工们回来以后\n',
            '又要开始忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '全都是力气活，\n',
            '但为了让大家吃上东西也没办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '早上终于过去了，\n',
            '本以为可以休息一下了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊啊、老板！\n',
            '快点回厨房吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_4F99(): pass

    label('loc_4F99')

    Jump('loc_56E1')

    def _loc_4F9C(): pass

    label('loc_4F9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_50E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_501D',
    )

    ChrTalk(
        0x000C,
        (
            '今天早上的客人还是很少…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过定期船上的\n',
            '人好像要来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '大家都被禁止出行了，\n',
            '也没有别的地方可去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50E0')

    def _loc_501D(): pass

    label('loc_501D')

    ChrTalk(
        0x000C,
        (
            '今天早上的客人还是很少…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过定期船上的\n',
            '人好像要来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '大家都被禁止出行了，\n',
            '也没有别的地方可去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这样的话，正是轮到\n',
            '酒馆起作用的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '美味的酒菜也\n',
            '可以让人解忧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_50E0(): pass

    label('loc_50E0')

    Jump('loc_56E1')

    def _loc_50E3(): pass

    label('loc_50E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_5560',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 6, 0x1896)),
            Expr.Return,
        ),
        'loc_5404',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_51C8',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_515F',
    )

    ChrTalk(
        0x000C,
        (
            '雪、雪拉。\n',
            '工作要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那个、今天这么大雾，\n',
            '要喝酒的话还是改日吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51C5')

    def _loc_515F(): pass

    label('loc_515F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51C5',
    )

    ChrTalk(
        0x000C,
        (
            '雪拉小姐和爱娜小姐\n',
            '两个人一起喝酒…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那种情景实在太恐怖，\n',
            '没经历过的人很难体会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51C5(): pass

    label('loc_51C5')

    Jump('loc_53BD')

    def _loc_51C8(): pass

    label('loc_51C8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_526C',
    )

    ChrTalk(
        0x000C,
        (
            '雪、雪拉扎德！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '难、难道已经喝了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F我也想那样……\n',
            '但很遗憾，现在在工作中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈、哈哈……是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '（哈～……太好了～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_53BD')

    def _loc_526C(): pass

    label('loc_526C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5344',
    )

    ChrTalk(
        0x000C,
        (
            '啊、那个……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那件白色外套……\n',
            '你难道是那时的？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F呵、肯定要多关照关照啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '身为同甘共苦过的人，\n',
            '一定会更有默契吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那种恐怖的事情都经历过，\n',
            '接下来一定更要顽强活下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_53BD')

    def _loc_5344(): pass

    label('loc_5344')

    ChrTalk(
        0x000C,
        (
            '要是只有雪拉的话\n',
            '还能勉强撑一下…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '但要再加上爱娜的话\n',
            '就和送死没区别了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊啊…\n',
            '至少要２、３天起不来床了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53BD(): pass

    label('loc_53BD')

    Jump('loc_5401')

    def _loc_53C0(): pass

    label('loc_53C0')

    ChrTalk(
        0x000C,
        (
            '雪、雪拉要带\n',
            '爱娜来喝酒的话…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '……要关门２、３天了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5401(): pass

    label('loc_5401')

    Jump('loc_555D')

    def _loc_5404(): pass

    label('loc_5404')

    ChrTalk(
        0x0103,
        (
            '#526F啊，福克纳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000C, 0x0103, 400)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '雪、雪拉扎德！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '什、什么时候回来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F呵呵、你看起来\n',
            '很想见我啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#525F那到时我带爱娜一起来喝酒，\n',
            '就请多关照了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '哈、哈哈……我等你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F（还、还是\n',
            '   那么恐怖啊。）',
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
        'loc_5557',
    )

    ChrTalk(
        0x0104,
        (
            '#034F福克纳兄。\n',
            '……我了解你的心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5557(): pass

    label('loc_5557')

    OP_A2(0x1896)
    OP_A2(0x0001)
    def _loc_555D(): pass

    label('loc_555D')

    Jump('loc_56E1')

    def _loc_5560(): pass

    label('loc_5560')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_56E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_55E1',
    )

    ChrTalk(
        0x000C,
        (
            '那天毫不犹豫地就赶紧下班了，\n',
            '所以后面的事情就不知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊啊，究竟发生什么事呢，\n',
            '光是想想就很可怕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56E1')

    def _loc_55E1(): pass

    label('loc_55E1')

    ChrTalk(
        0x000C,
        (
            '之前雪拉扎德带\n',
            '来过一个金发的男子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '一个穿着白色外套的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '在喝酒前就一直说些醉话，\n',
            '真是个奇怪的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '然后游击士协会的爱娜\n',
            '也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '那个男子好像什么都不知道，\n',
            '很欢迎她的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '但在我看来，他简直就像是冲向野狼\n',
            '的可怜小羊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_56E1(): pass

    label('loc_56E1')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x56E5
@scena.Code('func_09_56E5')
def func_09_56E5():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5842',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5782',
    )

    ChrTalk(
        0x00FE,
        (
            '哈，我今天实在\n',
            '是没食欲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是、什么都不吃的话\n',
            '对身体不好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法……\n',
            '稍微吃一点吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咔咔咔咔\n',
            '呱呱呱呱呱…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0002)

    Jump('loc_583F')

    def _loc_5782(): pass

    label('loc_5782')

    ChrTalk(
        0x00FE,
        (
            '呼呼呼呼呼…\n',
            '咯咯咯咯咯…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喔喔喔喔喔…\n',
            '…………嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊、回城的途中，\n',
            '遭到雾妖的袭击了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士们虽然\n',
            '帮我打退了它们，\n',
            '不过还是好可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我今天实在\n',
            '是没食欲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_583F(): pass

    label('loc_583F')

    Jump('loc_59D7')

    def _loc_5842(): pass

    label('loc_5842')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_5932',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5880',
    )

    ChrTalk(
        0x00FE,
        (
            '咔咔咔咔\n',
            '呱呱呱呱呱…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_592F')

    def _loc_5880(): pass

    label('loc_5880')

    ChrTalk(
        0x00FE,
        (
            '呼呼呼呼呼…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咯咯咯咯咯…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喔喔喔喔喔…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，外边的雾还很浓啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要去矿山吗？\n',
            '总有些不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么样，\n',
            '还是快点吃完出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_592F(): pass

    label('loc_592F')

    Jump('loc_59D7')

    def _loc_5932(): pass

    label('loc_5932')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_59D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5967',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼呼呼呼…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咯咯咯咯咯…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59D7')

    def _loc_5967(): pass

    label('loc_5967')

    ChrTalk(
        0x00FE,
        (
            '呼呼呼呼呼…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咯咯咯咯咯…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喔喔喔喔喔…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，今天老大休息，\n',
            '总算安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_59D7(): pass

    label('loc_59D7')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x59DB
@scena.Code('func_0A_59DB')
def func_0A_59DB():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5B21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_5A45',
    )

    ChrTalk(
        0x00FE,
        (
            '雾中现身的魔兽…\n',
            '想想就让人直流冷汗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然肚子很饿，\n',
            '但是实在提不起食欲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B21')

    def _loc_5A45(): pass

    label('loc_5A45')

    ChrTalk(
        0x00FE,
        (
            '今天多亏有游击士护送，\n',
            '才能从矿山回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '途中遭到了从来没见过\n',
            '的魔兽袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它们的样子就像一团烟雾…\n',
            '想想就让人直流冷汗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然肚子很饿，\n',
            '但是实在提不起食欲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候，好羡慕\n',
            '提恩特那小子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_5B21(): pass

    label('loc_5B21')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x5B25
@scena.Code('func_0B_5B25')
def func_0B_5B25():
    TalkBegin(0x000F)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B4A',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_5B65')

    def _loc_5B4A(): pass

    label('loc_5B4A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_5B60',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_5B65')

    def _loc_5B60(): pass

    label('loc_5B60')

    SetChrSubChip(0x00FE, 1)

    def _loc_5B65(): pass

    label('loc_5B65')

    OP_8C(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_5C38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_5BC0',
    )

    ChrTalk(
        0x00FE,
        (
            '乘务员他们\n',
            '一天基本都待在船上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除了吃饭就是\n',
            '休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C38')

    def _loc_5BC0(): pass

    label('loc_5BC0')

    ChrTalk(
        0x00FE,
        (
            '哟，早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乘务员他们\n',
            '一天基本都待在船上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除了吃饭就是\n',
            '休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……可不是只有\n',
            '船长我才来酒馆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_5C38(): pass

    label('loc_5C38')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0x5C41
@scena.Code('func_0C_5C41')
def func_0C_5C41():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5CFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_5CAB',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，看来这雾\n',
            '短时间内不会散去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要是也和库因特那家伙\n',
            '一起去祈祷就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CFB')

    def _loc_5CAB(): pass

    label('loc_5CAB')

    ChrTalk(
        0x00FE,
        (
            '飞不起来的飞船，\n',
            '简直一点用处也没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真想早日重新飞到空中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_5CFB(): pass

    label('loc_5CFB')

    TalkEnd(0x0010)

    Return()

# id: 0x000D offset: 0x5CFF
@scena.Code('func_0D_5CFF')
def func_0D_5CFF():
    TalkBegin(0x0011)

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_5E33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_5D64',
    )

    ChrTalk(
        0x00FE,
        (
            '今天真是谢谢了，\n',
            '让你们费心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全靠你们，我才能再次\n',
            '尝到怀念的味道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E30')

    def _loc_5D64(): pass

    label('loc_5D64')

    ChrTalk(
        0x00FE,
        (
            '今天真是谢谢了，\n',
            '让你们费心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全靠你们，我才能再次\n',
            '尝到怀念的味道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，布露姆老奶奶\n',
            '的烹饪水平真是一流啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是从小就学习\n',
            '烹饪的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有经过岁月的累积\n',
            '才能达到这种水平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_5E30(): pass

    label('loc_5E30')

    Jump('loc_60B6')

    def _loc_5E33(): pass

    label('loc_5E33')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_5EDB',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_5ED4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_5E89',
    )

    ChrTalk(
        0x00FE,
        (
            '调查的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待你们发现\n',
            '新的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5ED1')

    def _loc_5E89(): pass

    label('loc_5E89')

    ChrTalk(
        0x00FE,
        (
            '喔喔，是你们吗？\n',
            '调查怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待你们发现\n',
            '那怀念的食谱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5ED1(): pass

    label('loc_5ED1')

    Jump('loc_5ED8')

    def _loc_5ED4(): pass

    label('loc_5ED4')

    Call(1, 0x0003)
    def _loc_5ED8(): pass

    label('loc_5ED8')

    Jump('loc_60B6')

    def _loc_5EDB(): pass

    label('loc_5EDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_6060',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_5F65',
    )

    ChrTalk(
        0x00FE,
        (
            '已经很久没有\n',
            '做过年轻时的梦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以才想起了\n',
            '怀念的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然给厨师添了不少麻烦，\n',
            '不过总算是如愿以偿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_605D')

    def _loc_5F65(): pass

    label('loc_5F65')

    ChrTalk(
        0x00FE,
        (
            '呀，昨天梦见了很久没梦到过的\n',
            '年轻时代。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '梦的内容很奇怪，\n',
            '是和当时的恋人一起\n',
            '拼命制作料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '醒来之后，就非常\n',
            '想要吃那料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以就跑到酒馆\n',
            '来找寻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那是很久以前的菜式，\n',
            '厨师实在是找不到了。\n',
            '嗯，不过总算是如愿以偿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_605D(): pass

    label('loc_605D')

    Jump('loc_60B6')

    def _loc_6060(): pass

    label('loc_6060')

    ChrTalk(
        0x00FE,
        (
            '终于天晴了，\n',
            '但为何会突然出现浓雾呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这简直是故事中出现过的\n',
            '妖精恶作剧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_60B6(): pass

    label('loc_60B6')

    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x60BA
@scena.Code('func_0E_60BA')
def func_0E_60BA():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6191',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_6157',
    )

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
            '来了啊。\n',
            '快来参加庆祝会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近虽然有很多事情让人不安，\n',
            '但也让人很兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟是很难得\n',
            '的经历啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_618B')

    def _loc_6157(): pass

    label('loc_6157')

    ChrTalk(
        0x00FE,
        (
            '今天真是\n',
            '谢谢了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '机会难得，\n',
            '一定要去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_618B(): pass

    label('loc_618B')

    OP_A2(0x000A)

    Jump('loc_61D7')

    def _loc_6191(): pass

    label('loc_6191')

    ChrTalk(
        0x00FE,
        (
            '难得的机会，\n',
            '今天一定要好好享受啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟是很难得\n',
            '的经历啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_61D7(): pass

    label('loc_61D7')

    TalkEnd(0x0014)

    Return()

# id: 0x000F offset: 0x61DB
@scena.Code('func_0F_61DB')
def func_0F_61DB():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6274',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_6235',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，游击士。\n',
            '今天谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '约定了哦。\n',
            '我们一定会幸福的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_626E')

    def _loc_6235(): pass

    label('loc_6235')

    ChrTalk(
        0x00FE,
        (
            '谢谢你们来捧场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '约定了哦。\n',
            '我们一定会幸福的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_626E(): pass

    label('loc_626E')

    OP_A2(0x000B)

    Jump('loc_6295')

    def _loc_6274(): pass

    label('loc_6274')

    ChrTalk(
        0x00FE,
        (
            '谢谢你们来捧场。\n',
            '请随意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_6295(): pass

    label('loc_6295')

    TalkEnd(0x0015)

    Return()

# id: 0x0010 offset: 0x6299
@scena.Code('func_10_6299')
def func_10_6299():
    TalkBegin(0x0016)

    ChrTalk(
        0x00FE,
        (
            '真是完美的\n',
            '结婚仪式啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了祝福年轻的夫妇，\n',
            '今天一定要多喝几杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0016)

    Return()

# id: 0x0011 offset: 0x62EC
@scena.Code('func_11_62EC')
def func_11_62EC():
    TalkBegin(0x0017)

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆哥哥在结婚仪式上\n',
            '真是好帅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '第一次感觉到哥哥\n',
            '是个优秀的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

# id: 0x0012 offset: 0x6343
@scena.Code('func_12_6343')
def func_12_6343():
    TalkBegin(0x0018)

    ChrTalk(
        0x00FE,
        (
            '嗯，果然是家不错的店呢。\n',
            '料理非常美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以很早就\n',
            '跑来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0018)

    Return()

# id: 0x0013 offset: 0x6390
@scena.Code('func_13_6390')
def func_13_6390():
    TalkBegin(0x0019)

    ChrTalk(
        0x00FE,
        (
            '新娘的结婚礼服\n',
            '很漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真想让那孩子的父亲\n',
            '也看看…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0019)

    Return()

# id: 0x0014 offset: 0x63DB
@scena.Code('func_14_63DB')
def func_14_63DB():
    TalkBegin(0x001A)

    ChrTalk(
        0x00FE,
        (
            '仪式顺利结束了，\n',
            '总算可以稍微休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望那孩子的父亲在\n',
            '天国也能看见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001A)

    Return()

# id: 0x0015 offset: 0x6436
@scena.Code('func_15_6436')
def func_15_6436():
    TalkBegin(0x001B)

    ChrTalk(
        0x00FE,
        (
            '姐姐的礼服\n',
            '真是太漂亮了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也想早点\n',
            '当新娘啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001B)

    Return()

# id: 0x0016 offset: 0x6477
@scena.Code('func_16_6477')
def func_16_6477():
    TalkBegin(0x001C)

    ChrTalk(
        0x00FE,
        (
            '今天的艾娅莉\n',
            '真的很漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '穿上礼服之后\n',
            '简直像变了个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001C)

    Return()

# id: 0x0017 offset: 0x64C2
@scena.Code('func_17_64C2')
def func_17_64C2():
    TalkBegin(0x001D)

    ChrTalk(
        0x00FE,
        (
            '艾娅莉和阿鲁姆\n',
            '好像很幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真羡慕他们…\n',
            '要开始认真寻找目标了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001D)

    Return()

# id: 0x0018 offset: 0x6517
@scena.Code('func_18_6517')
def func_18_6517():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 7, 0x10BF)),
            Expr.Return,
        ),
        'loc_6569',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～今天的酒真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帮了这么多忙，\n',
            '总有权利出席庆祝会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_661E')

    def _loc_6569(): pass

    label('loc_6569')

    ChrTalk(
        0x00FE,
        (
            '呼～今天的酒真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为心情很好，\n',
            '就把这书送你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 11卷']),
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
    AddItem(ItemTable['牌技师杰克 11卷'], 1)
    OP_A2(0x10BF)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '呼～真是好酒。\n',
            '光是想想就很舒服了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_661E(): pass

    label('loc_661E')

    TalkEnd(0x001E)

    Return()

# id: 0x0019 offset: 0x6622
@scena.Code('func_19_6622')
def func_19_6622():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x000A, 84020, 0, 81160, 0)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    OP_4A(0x0008, 255)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0008, 2)
    OP_6F(0x0000, 10)
    SetChrPos(0x0008, 88750, 0, 78900, 270)
    ClearChrFlags(0x0008, 0x0080)
    OP_6D(83860, 0, 81320, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_66D1')
    def lambda_66D1():
        OP_6D(87450, 0, 79790, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_66D1)

    FadeIn(1000, 0)
    Sleep(3000)

    SetChrSubChip(0x0008, 3)
    Sleep(300)

    ChrTurnDirection(0x000A, 0x0008, 400)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8E(0x000A, 87000, 0, 80100, 5000, 0x00)
    OP_8E(0x000A, 87000, 0, 79180, 5000, 0x00)
    ChrTurnDirection(0x000A, 0x0008, 400)
    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0111._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x676B
@scena.Code('func_1A_676B')
def func_1A_676B():
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_21()
    OP_1D(0x19)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
