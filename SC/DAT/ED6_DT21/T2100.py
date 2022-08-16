import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2100.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T2100._SN', 'ED6_DT21/T2100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT06/CH20092._CH', 'ED6_DT06/CH20092P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT06/CH20039._CH', 'ED6_DT06/CH20039P._CP'),
        ('ED6_DT07/CH01663._CH', 'ED6_DT07/CH01663P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
    ]

# id: 0x10001 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奈尔',
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
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '诺曼候选人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '德尔斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '海利欧',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '波尔多斯候选人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '昆茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '布诺安',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '中年男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '哈尔德',
            x                   = 70990,
            z                   = 1050,
            y                   = 79010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '罗伊德',
            x                   = 22310,
            z                   = 0,
            y                   = 76950,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '罗伊德',
            x                   = 29307,
            z                   = -1800,
            y                   = 68254,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '塞尔玛',
            x                   = 21840,
            z                   = 0,
            y                   = 70280,
            direction           = 60,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '玛奇尔达',
            x                   = 23580,
            z                   = 2160,
            y                   = 102820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '菲利奥',
            x                   = 46320,
            z                   = 0,
            y                   = 79740,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '拉科舒',
            x                   = 47990,
            z                   = 0,
            y                   = 80530,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '昆茨',
            x                   = 46730,
            z                   = 0,
            y                   = 78510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '利顿',
            x                   = 28500,
            z                   = 0,
            y                   = 82470,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '穆拉德老人',
            x                   = 990,
            z                   = -2250,
            y                   = 94250,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '鲁蓓',
            x                   = 26280,
            z                   = 0,
            y                   = 88370,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '阿杰',
            x                   = 24400,
            z                   = 0,
            y                   = 93520,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '海利欧',
            x                   = 54940,
            z                   = 0,
            y                   = 78510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '修女芙丽达',
            x                   = 67840,
            z                   = 500,
            y                   = 93830,
            direction           = 270,
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
            name                = '森特',
            x                   = 39560,
            z                   = -1770,
            y                   = 69520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00A4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '连茨',
            x                   = 52980,
            z                   = 0,
            y                   = 95770,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '阿伦特',
            x                   = 43460,
            z                   = 3500,
            y                   = 72520,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '爱蕾塔',
            x                   = 29170,
            z                   = 0,
            y                   = 89110,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '迪恩',
            x                   = 51800,
            z                   = 0,
            y                   = 71000,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '雷斯',
            x                   = 50200,
            z                   = 0,
            y                   = 71000,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '洛克',
            x                   = 51000,
            z                   = 0,
            y                   = 72300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '布鲁托',
            x                   = 24000,
            z                   = 0,
            y                   = 93780,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '梅威海道方向',
            x                   = 25260,
            z                   = 0,
            y                   = 128199,
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
            name                = '卢安市·南街区',
            x                   = 51060,
            z                   = 400,
            y                   = 27190,
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
            name                = '卢安飞船坪',
            x                   = 81750,
            z                   = 0,
            y                   = 80640,
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

# id: 0x10002 offset: 0x8A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x8A2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 20100,
            y           = -2000,
            z           = 118500,
            range       = 28900,
            dword_10    = 0x00000708,
            dword_14    = 0x0001D524,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000029,
        ),
        ScenaEventData(
            x           = 48500,
            y           = -2000,
            z           = 68000,
            range       = 53500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00011170,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000020,
        ),
        ScenaEventData(
            x           = 67740,
            y           = 0,
            z           = 84010,
            range       = 66350,
            dword_10    = 0x00000708,
            dword_14    = 0x000130B0,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000002A,
        ),
        ScenaEventData(
            x           = 46730,
            y           = -1000,
            z           = 78510,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = 28500,
            y           = -1000,
            z           = 82470,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 54940,
            y           = -1000,
            z           = 78510,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = 50950,
            y           = -1000,
            z           = 75000,
            range       = 3000,
            dword_10    = 0x00001388,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = 44990,
            y           = 0,
            z           = 89330,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000039,
        ),
        ScenaEventData(
            x           = 38080,
            y           = 0,
            z           = 78540,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003A,
        ),
        ScenaEventData(
            x           = 37930,
            y           = 0,
            z           = 89380,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003B,
        ),
        ScenaEventData(
            x           = 30610,
            y           = 0,
            z           = 96060,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003B,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 108200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003C,
        ),
        ScenaEventData(
            x           = 20930,
            y           = -1500,
            z           = 93960,
            range       = 3500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003D,
        ),
        ScenaEventData(
            x           = 61000,
            y           = 0,
            z           = 78900,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003E,
        ),
        ScenaEventData(
            x           = 66890,
            y           = -500,
            z           = 93800,
            range       = 2200,
            dword_10    = 0x00000898,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003F,
        ),
        ScenaEventData(
            x           = 73630,
            y           = 0,
            z           = 80790,
            range       = 3500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000040,
        ),
    )

# id: 0x10004 offset: 0xAA2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 23750,
            triggerZ            = 1000,
            triggerY            = 102860,
            triggerRange        = 1000,
            actorX              = 23580,
            actorZ              = 4000,
            actorY              = 102820,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 26630,
            triggerZ            = 0,
            triggerY            = 86030,
            triggerRange        = 800,
            actorX              = 26330,
            actorZ              = 1000,
            actorY              = 86030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0037,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16250,
            triggerZ            = -1800,
            triggerY            = 112100,
            triggerRange        = 1000,
            actorX              = 13840,
            actorZ              = -2500,
            actorY              = 112130,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0038,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xB0E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B96',
    )

    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrSetPos(0x002C, 28500, 0, 82470, 45)
    ChrSetPos(0x002E, 27820, 0, 98030, 225)
    ChrSetPos(0x002F, 29470, 0, 97990, 45)
    CreateThread(0x002F, 0x00, 0x00, func_02_E90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B7D',
    )

    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrSetFlags(0x002F, 0x0010)

    Jump('loc_B93')

    def _loc_B7D(): pass

    label('loc_B7D')

    ChrClearFlags(0x0036, 0x0080)
    ChrSetPos(0x0039, 50750, 0, 78770, 0)

    def _loc_B93(): pass

    label('loc_B93')

    Jump('loc_CEA')

    def _loc_B96(): pass

    label('loc_B96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_BF3',
    )

    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0025, 22804, 0, 71275, 220)
    ChrTurnDirection(0x0025, 0x0027, 0)
    ChrTurnDirection(0x0027, 0x0025, 0)
    ChrSetFlags(0x0025, 0x0010)
    ChrSetFlags(0x0027, 0x0010)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetPos(0x002C, 46730, 0, 78510, 0)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x0037, 0x0080)

    Jump('loc_CEA')

    def _loc_BF3(): pass

    label('loc_BF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_C11',
    )

    ChrClearFlags(0x0026, 0x0080)
    ChrSetFlags(0x002F, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0035, 0x0080)

    Jump('loc_CEA')

    def _loc_C11(): pass

    label('loc_C11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_C8D',
    )

    Call(0, 0x001F)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetPos(0x002E, 47440, 0, 78530, 180)
    ChrSetPos(0x002F, 46010, 0, 79440, 130)
    CreateThread(0x002F, 0x00, 0x00, func_02_E90)
    ChrClearFlags(0x0035, 0x0080)
    ChrSetPos(0x0035, 66540, 0, 72560, 211)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0025, 29920, -1800, 68470, 138)
    ChrSetFlags(0x002D, 0x0010)
    OP_71(0x0012, 0x0004)
    ChrSetFlags(0x002F, 0x0010)

    Jump('loc_CEA')

    def _loc_C8D(): pass

    label('loc_C8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_CB4',
    )

    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x002B, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_CB1',
    )

    ChrClearFlags(0x0032, 0x0080)

    def _loc_CB1(): pass

    label('loc_CB1')

    Jump('loc_CEA')

    def _loc_CB4(): pass

    label('loc_CB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_CEA',
    )

    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x0035, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_CDE',
    )

    ChrClearFlags(0x0032, 0x0080)

    def _loc_CDE(): pass

    label('loc_CDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0248, 2, 0x1242)),
            Expr.Return,
        ),
        'loc_CEA',
    )

    ChrClearFlags(0x0025, 0x0080)

    def _loc_CEA(): pass

    label('loc_CEA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CFB',
    )

    ChrSetFlags(0x002D, 0x0080)

    def _loc_CFB(): pass

    label('loc_CFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D0A',
    )

    SetScenaFlags(ScenaFlag(0x0246, 1, 0x1231))

    def _loc_D0A(): pass

    label('loc_D0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_D20',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_24_7B33)

    Jump('loc_E1C')

    def _loc_D20(): pass

    label('loc_D20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_D3F',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_2C_8F81)

    Jump('loc_E1C')

    def _loc_D3F(): pass

    label('loc_D3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_D55',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(1, 0x0003)

    Jump('loc_E1C')

    def _loc_D55(): pass

    label('loc_D55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_D6B',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(1, 0x0005)

    Jump('loc_E1C')

    def _loc_D6B(): pass

    label('loc_D6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_D81',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    MapSetFlags(0x10000000)
    Event(1, 0x0004)

    Jump('loc_E1C')

    def _loc_D81(): pass

    label('loc_D81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_D97',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    MapSetFlags(0x10000000)
    Event(0, func_34_AE5B)

    Jump('loc_E1C')

    def _loc_D97(): pass

    label('loc_D97')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DB1',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    Event(0, func_2B_88DF)

    Jump('loc_E1C')

    def _loc_DB1(): pass

    label('loc_DB1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_DC5'),
        (0x00000069, 'loc_DDD'),
        (0x00000076, 'loc_E09'),
        (-1, 'loc_E1C'),
    )

    def _loc_DC5(): pass

    label('loc_DC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 3, 0x121B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DDA',
    )

    MapSetFlags(0x10000000)
    Event(0, func_1E_4A0D)

    def _loc_DDA(): pass

    label('loc_DDA')

    Jump('loc_E1C')

    def _loc_DDD(): pass

    label('loc_DDD')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 5, 0x2035)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DFD',
    )

    MapSetFlags(0x10000000)
    Event(0, func_32_930A)

    Jump('loc_E06')

    def _loc_DFD(): pass

    label('loc_DFD')

    MapSetFlags(0x10000000)
    Event(0, func_33_A468)

    def _loc_E06(): pass

    label('loc_E06')

    Jump('loc_E1C')

    def _loc_E09(): pass

    label('loc_E09')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E19',
    )

    Call(0, 0x0031)

    def _loc_E19(): pass

    label('loc_E19')

    Jump('loc_E1C')

    def _loc_E1C(): pass

    label('loc_E1C')

    Return()

# id: 0x0001 offset: 0xE1D
@scena.Code('func_01_E1D')
def func_01_E1D():
    OP_16(0x02, 4000, -88000, -44000, 2293831)
    PlaySE(453, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0248, 2, 0x1242)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E40',
    )

    OP_64(0x02, 0x0001)

    def _loc_E40(): pass

    label('loc_E40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E55',
    )

    OP_71(0x0012, 0x0004)

    def _loc_E55(): pass

    label('loc_E55')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E8F',
    )

    OP_6F(0x0011, 1500)
    OP_72(0x001A, 0x0002)
    OP_71(0x0012, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_64(0x01, 0x0001)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)

    def _loc_E8F(): pass

    label('loc_E8F')

    Return()

# id: 0x0002 offset: 0xE90
@scena.Code('func_02_E90')
def func_02_E90():
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
        'loc_EB5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_FF7')

    def _loc_EB5(): pass

    label('loc_EB5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ECE',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_FF7')

    def _loc_ECE(): pass

    label('loc_ECE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EE7',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_FF7')

    def _loc_EE7(): pass

    label('loc_EE7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F00',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_FF7')

    def _loc_F00(): pass

    label('loc_F00')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F19',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_FF7')

    def _loc_F19(): pass

    label('loc_F19')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F32',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_FF7')

    def _loc_F32(): pass

    label('loc_F32')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F4B',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_FF7')

    def _loc_F4B(): pass

    label('loc_F4B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F64',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_FF7')

    def _loc_F64(): pass

    label('loc_F64')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F7D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_FF7')

    def _loc_F7D(): pass

    label('loc_F7D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F96',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_FF7')

    def _loc_F96(): pass

    label('loc_F96')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FAF',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_FF7')

    def _loc_FAF(): pass

    label('loc_FAF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FC8',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_FF7')

    def _loc_FC8(): pass

    label('loc_FC8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FE1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_FF7')

    def _loc_FE1(): pass

    label('loc_FE1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FF7',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_FF7(): pass

    label('loc_FF7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_100C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_FF7')

    def _loc_100C(): pass

    label('loc_100C')

    Return()

# id: 0x0003 offset: 0x100D
@scena.Code('func_03_100D')
def func_03_100D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1030',
    )

    OP_8D(0x00FE, 24600, 90150, 28170, 94510, 4000)

    Jump('func_03_100D')

    def _loc_1030(): pass

    label('loc_1030')

    Return()

# id: 0x0004 offset: 0x1031
@scena.Code('func_04_1031')
def func_04_1031():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1054',
    )

    OP_8D(0x00FE, 28420, 86550, 31010, 89470, 4000)

    Jump('func_04_1031')

    def _loc_1054(): pass

    label('loc_1054')

    Return()

# id: 0x0005 offset: 0x1055
@scena.Code('func_05_1055')
def func_05_1055():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天要和阿杰\n',
            '外出游玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎嘿，好高兴哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1091
@scena.Code('func_06_1091')
def func_06_1091():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1172',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_10F7',
    )

    ChrTalk(
        0x00FE,
        (
            '要去王立学院就读\n',
            '果然需要很多钱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要在下次出海中\n',
            '大赚一笔才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_116F')

    def _loc_10F7(): pass

    label('loc_10F7')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '我儿子好像有意\n',
            '报考王立学院……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要去那里上学，\n',
            '需要很多钱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～首先要在下次出海中\n',
            '大赚一笔才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_116F(): pass

    label('loc_116F')

    Jump('loc_130D')

    def _loc_1172(): pass

    label('loc_1172')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_121E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_11C0',
    )

    ChrTalk(
        0x00FE,
        (
            '如果逃避争执\n',
            '就不可能相互理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就是这么想的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_121B')

    def _loc_11C0(): pass

    label('loc_11C0')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '打架什么的，也没什么啊。\n',
            '争执多半伴随着争吵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果逃避争执\n',
            '就不可能相互理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_121B(): pass

    label('loc_121B')

    Jump('loc_130D')

    def _loc_121E(): pass

    label('loc_121E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_1250',
    )

    ChrTalk(
        0x00FE,
        (
            '喂喂怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在桥上干什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_130D')

    def _loc_1250(): pass

    label('loc_1250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_128B',
    )

    ChrTalk(
        0x00FE,
        (
            '诺曼先生是很出色的人，\n',
            '但就是对公约不重视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_130D')

    def _loc_128B(): pass

    label('loc_128B')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '诺曼先生是很出色的人，\n',
            '但就是对公约不重视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安就不是旅游城市，\n',
            '原本就是船员和渔夫的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这点最好\n',
            '别搞错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_130D(): pass

    label('loc_130D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1311
@scena.Code('func_07_1311')
def func_07_1311():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1329',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_132E')

    def _loc_1329(): pass

    label('loc_1329')

    ChrSetSubChip(0x00FE, 1)

    def _loc_132E(): pass

    label('loc_132E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_140A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_138D',
    )

    ChrTalk(
        0x00FE,
        (
            '真想这样一直\n',
            '待在卢安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～啊，前往王都的船\n',
            '不能暂时停下吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1407')

    def _loc_138D(): pass

    label('loc_138D')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '工作结束之后\n',
            '喝一杯真是格外美味呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真想这样一直\n',
            '待在卢安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～啊，前往王都的船\n',
            '不能暂时停下吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1407(): pass

    label('loc_1407')

    Jump('loc_1497')

    def _loc_140A(): pass

    label('loc_140A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1497',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_144E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～海风真舒服啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀～果然\n',
            '卢安最棒了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_144E(): pass

    label('loc_144E')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '呀，各位。\n',
            '还在工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在等回去的船\n',
            '现在是片刻的休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1497(): pass

    label('loc_1497')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x14A0
@scena.Code('func_08_14A0')
def func_08_14A0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_15B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1508',
    )

    ChrTalk(
        0x00FE,
        (
            '说来那些家伙，\n',
            '连幽灵都要怪到我们头上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～回想起来\n',
            '又开始焦躁不安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15B6')

    def _loc_1508(): pass

    label('loc_1508')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '波尔多斯主任叫我来\n',
            '向诺曼先生道歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明是对方找的麻烦，\n',
            '为什么要我去谢罪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，虽说我说过那些贬低他儿子的话，\n',
            '确实做的不对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是～无法接受啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15B6(): pass

    label('loc_15B6')

    Jump('loc_16F9')

    def _loc_15B9(): pass

    label('loc_15B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_16F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1653',
    )

    ChrTalk(
        0x00FE,
        (
            '市长候选人波尔多斯！\n',
            '请多关照波尔多斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '海的男人波尔多斯！\n',
            '懂道理的波尔多斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '波尔多斯将以火热的心\n',
            '回应各位的期待！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F9')

    def _loc_1653(): pass

    label('loc_1653')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '诺曼阵营果然\n',
            '出动不少宣传员啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然只有自己一个人，\n',
            '但海的男人要以气势来决一胜负！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～～吸～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长候选人波尔多斯！\n',
            '请多关照波尔多斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16F9(): pass

    label('loc_16F9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x16FD
@scena.Code('func_09_16FD')
def func_09_16FD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_17C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_177E',
    )

    ChrTalk(
        0x00FE,
        (
            '那个漂浮在远方天空\n',
            '的大家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个到底是什么\n',
            '谁都不告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～下次主日学校\n',
            '问问看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_17C6')

    def _loc_177E(): pass

    label('loc_177E')

    ChrTalk(
        0x00FE,
        (
            '浮在天上的那是什么\n',
            '谁都不告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～下次主日学校\n',
            '问问看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17C6(): pass

    label('loc_17C6')

    Jump('loc_19AA')

    def _loc_17C9(): pass

    label('loc_17C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1869',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_182D',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，妈妈～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个浮在天上的\n',
            '大家伙是什么～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是新型飞船？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_1866')

    def _loc_182D(): pass

    label('loc_182D')

    ChrTalk(
        0x00FE,
        (
            '哎呀，妈妈～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个浮在天上的\n',
            '大家伙是什么～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1866(): pass

    label('loc_1866')

    Jump('loc_19AA')

    def _loc_1869(): pass

    label('loc_1869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_18C1',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才开始妈妈\n',
            '就一直盯着海报看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，海报里的那个人\n',
            '并不怎么帅嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19AA')

    def _loc_18C1(): pass

    label('loc_18C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_18E4',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈～？\n',
            '怎么了～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19AA')

    def _loc_18E4(): pass

    label('loc_18E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_192D',
    )

    ChrTalk(
        0x00FE,
        (
            '今天有主日学校吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能见到朋友们，\n',
            '真是好期待啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19AA')

    def _loc_192D(): pass

    label('loc_192D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_19AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1963',
    )

    ChrTalk(
        0x00FE,
        (
            '声音最大的人\n',
            '就会当上新市长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19AA')

    def _loc_1963(): pass

    label('loc_1963')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '总觉得叔叔们\n',
            '叫得好大声哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '问过妈妈了，\n',
            '她说这个是选举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19AA(): pass

    label('loc_19AA')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x19AE
@scena.Code('func_0A_19AE')
def func_0A_19AE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1A8E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A35',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才游击士协会\n',
            '有一些人冲了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定哪里\n',
            '又发生事件了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候果然\n',
            '还是游击士们可靠啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_1A8B')

    def _loc_1A35(): pass

    label('loc_1A35')

    ChrTalk(
        0x00FE,
        (
            '这种时候还是\n',
            '游击士们可靠啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与王国军不同，\n',
            '游击士在各地支部真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A8B(): pass

    label('loc_1A8B')

    Jump('loc_1DEC')

    def _loc_1A8E(): pass

    label('loc_1A8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B20',
    )

    ChrTalk(
        0x00FE,
        (
            '由于大桥不能动了，\n',
            '去南区现在很麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，市长诺曼先生\n',
            '在干什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不会是以为准备了渡船\n',
            '就足够了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_1B76')

    def _loc_1B20(): pass

    label('loc_1B20')

    ChrTalk(
        0x00FE,
        (
            '由于大桥不能动了，\n',
            '去南区现在很麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，市长诺曼先生\n',
            '在干什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B76(): pass

    label('loc_1B76')

    Jump('loc_1DEC')

    def _loc_1B79(): pass

    label('loc_1B79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1C06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1BCB',
    )

    ChrTalk(
        0x00FE,
        (
            '重要的还是人品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，只看海报\n',
            '可不知道是好人坏人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C03')

    def _loc_1BCB(): pass

    label('loc_1BCB')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '重要的还是人品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就看这个\n',
            '决定投谁票了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C03(): pass

    label('loc_1C03')

    Jump('loc_1DEC')

    def _loc_1C06(): pass

    label('loc_1C06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1CA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1C48',
    )

    ChrTalk(
        0x00FE,
        (
            '真是难以置信，\n',
            '居然做出打架这么危险的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C9D')

    def _loc_1C48(): pass

    label('loc_1C48')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '真是难以置信，\n',
            '居然做出打架这么危险的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望两边都\n',
            '冷静一下头脑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C9D(): pass

    label('loc_1C9D')

    Jump('loc_1DEC')

    def _loc_1CA0(): pass

    label('loc_1CA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_1CF4',
    )

    ChrTalk(
        0x00FE,
        (
            '桥、桥上好像有人\n',
            '在吵架啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话，\n',
            '那气势都快打起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DEC')

    def _loc_1CF4(): pass

    label('loc_1CF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1D57',
    )

    ChrTalk(
        0x00FE,
        (
            '波尔多斯候选人\n',
            '是个年轻的好男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但也不能因为这个理由\n',
            '就投票啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9C')

    def _loc_1D57(): pass

    label('loc_1D57')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '嗯～投给\n',
            '谁好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像两个人都还缺点\n',
            '决定性的东西似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D9C(): pass

    label('loc_1D9C')

    Jump('loc_1DEC')

    def _loc_1D9F(): pass

    label('loc_1D9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1DEC',
    )

    ChrTalk(
        0x00FE,
        (
            '选举的时候\n',
            '这种宣传劲儿真讨厌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，只有\n',
            '稍微忍耐一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DEC(): pass

    label('loc_1DEC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1DF0
@scena.Code('func_0B_1DF0')
def func_0B_1DF0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1F09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EA1',
    )

    ChrTalk(
        0x00FE,
        (
            '那个浮在天上的东西\n',
            '到底是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道…\n',
            '会是帝国军的新兵器……或者？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不……那是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是帝国\n',
            '也不可能做出那种东西来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_1F06')

    def _loc_1EA1(): pass

    label('loc_1EA1')

    ChrTalk(
        0x00FE,
        (
            '那个浮在天上的东西\n',
            '到底是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然觉得是帝国的新兵器，\n',
            '但是这想法应该\n',
            '也是有可能的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F06(): pass

    label('loc_1F06')

    Jump('loc_239D')

    def _loc_1F09(): pass

    label('loc_1F09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1FFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FA7',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯、嗯…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个浮在天上的东西\n',
            '到底是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少发表一下市长声明\n',
            '让大家安心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这时候\n',
            '音信全无是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_1FF9')

    def _loc_1FA7(): pass

    label('loc_1FA7')

    ChrTalk(
        0x00FE,
        (
            '那个浮在天上的东西\n',
            '到底是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少发表一下市长声明\n',
            '让大家安心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FF9(): pass

    label('loc_1FF9')

    Jump('loc_239D')

    def _loc_1FFC(): pass

    label('loc_1FFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2152',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_20E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2062',
    )

    ChrTalk(
        0x00FE,
        (
            '市长候选人诺曼\n',
            '请多多关照～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诺曼将以旅游业为中心，\n',
            '活化卢安市～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20E2')

    def _loc_2062(): pass

    label('loc_2062')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '诺曼先生对港口问题\n',
            '也不会轻视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望各位市民\n',
            '能更了解此事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，已经到了最后阶段，\n',
            '今天也要充满气势地高呼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20E2(): pass

    label('loc_20E2')

    Jump('loc_214F')

    def _loc_20E5(): pass

    label('loc_20E5')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '诺曼先生对港口问题\n',
            '也不会轻视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是这样我也\n',
            '不会支持他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我\n',
            '本来也是渔师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_214F(): pass

    label('loc_214F')

    Jump('loc_239D')

    def _loc_2152(): pass

    label('loc_2152')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2234',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_21B9',
    )

    ChrTalk(
        0x00FE,
        (
            '这种对立要是向全市\n',
            '发展那可头痛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两个阵营都需要\n',
            '相互理解从而更加努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2231')

    def _loc_21B9(): pass

    label('loc_21B9')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呀～刚才的\n',
            '骚动真是危险啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都杀气腾腾的，\n',
            '真是差点打起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种对立要是向全市\n',
            '发展那可头痛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2231(): pass

    label('loc_2231')

    Jump('loc_239D')

    def _loc_2234(): pass

    label('loc_2234')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2320',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2299',
    )

    ChrTalk(
        0x00FE,
        (
            '休息片刻\n',
            '一会再播音和发放传单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何都要让诺曼先生\n',
            '当上市长啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231D')

    def _loc_2299(): pass

    label('loc_2299')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我的本职是旅游向导，\n',
            '不过暂时休假支持诺曼先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正选举期间\n',
            '游客也显著减少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，休息片刻\n',
            '再大声努力支援吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_231D(): pass

    label('loc_231D')

    Jump('loc_239D')

    def _loc_2320(): pass

    label('loc_2320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_239D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2360',
    )

    ChrTalk(
        0x00FE,
        (
            '旅游城市卢安的啦啦队长！\n',
            '请多支持诺曼～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_239D')

    def _loc_2360(): pass

    label('loc_2360')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '市长候选人诺曼\n',
            '将支援旅游业！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请多\n',
            '支持诺曼～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_239D(): pass

    label('loc_239D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x23A1
@scena.Code('func_0C_23A1')
def func_0C_23A1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_23A9',
    )

    Return()

    def _loc_23A9(): pass

    label('loc_23A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_23B1',
    )

    Return()

    def _loc_23B1(): pass

    label('loc_23B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_23B9',
    )

    Return()

    def _loc_23B9(): pass

    label('loc_23B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_23C1',
    )

    Return()

    def _loc_23C1(): pass

    label('loc_23C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_23CF',
    )

    Jump('loc_23D6')

    def _loc_23CF(): pass

    label('loc_23CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_23D6',
    )

    def _loc_23D6(): pass

    label('loc_23D6')

    OP_4A(0x0030, 0)

    ChrTalk(
        0x0030,
        (
            '#4A请多支持诺曼～！\n',
            '请投诺曼宝贵１票！',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_4B(0x0030, 0)

    Return()

# id: 0x000D offset: 0x240F
@scena.Code('func_0D_240F')
def func_0D_240F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2417',
    )

    Return()

    def _loc_2417(): pass

    label('loc_2417')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_241F',
    )

    Return()

    def _loc_241F(): pass

    label('loc_241F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2427',
    )

    Return()

    def _loc_2427(): pass

    label('loc_2427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_242F',
    )

    Return()

    def _loc_242F(): pass

    label('loc_242F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_243D',
    )

    Jump('loc_2444')

    def _loc_243D(): pass

    label('loc_243D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2444',
    )

    def _loc_2444(): pass

    label('loc_2444')

    OP_4A(0x002C, 0)

    ChrTalk(
        0x002C,
        (
            '#4A旅游城市卢安的啦啦队长！\n',
            '请多支持诺曼～！',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_4B(0x002C, 0)

    Return()

# id: 0x000E offset: 0x2483
@scena.Code('func_0E_2483')
def func_0E_2483():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_248B',
    )

    Return()

    def _loc_248B(): pass

    label('loc_248B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2495',
    )

    Jump('loc_24BB')

    def _loc_2495(): pass

    label('loc_2495')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_249D',
    )

    Return()

    def _loc_249D(): pass

    label('loc_249D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_24A5',
    )

    Return()

    def _loc_24A5(): pass

    label('loc_24A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_24B3',
    )

    Jump('loc_24BB')

    def _loc_24B3(): pass

    label('loc_24B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_24BB',
    )

    Return()

    def _loc_24BB(): pass

    label('loc_24BB')

    OP_4A(0x002B, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_24FA',
    )

    ChrTalk(
        0x002C,
        (
            '#4A旅游城市卢安的啦啦队长！\n',
            '请多支持诺曼～！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2529')

    def _loc_24FA(): pass

    label('loc_24FA')

    ChrTalk(
        0x002B,
        (
            '#4A市长候选人波尔多斯！\n',
            '请多关照波尔多斯！',
            TxtCtl.Enter,
        ),
    )

    def _loc_2529(): pass

    label('loc_2529')

    Sleep(2000)

    OP_4B(0x002B, 0)

    Return()

# id: 0x000F offset: 0x2533
@scena.Code('func_0F_2533')
def func_0F_2533():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2652',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_25A1',
    )

    ChrTalk(
        0x00FE,
        (
            '说幽灵是波尔多斯阵营\n',
            '搞的鬼是太轻率……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算如此贬低诺曼先生\n',
            '的儿子也不应该吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_264F')

    def _loc_25A1(): pass

    label('loc_25A1')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '酒店里出现了像幽灵一样的影子,\n',
            '真是确有其事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但说是波尔多斯阵营\n',
            '搞的鬼是太轻率……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算如此贬低诺曼先生\n',
            '的儿子也不应该吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～想起来\n',
            '还是火冒三丈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_264F(): pass

    label('loc_264F')

    Jump('loc_2851')

    def _loc_2652(): pass

    label('loc_2652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_277A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_26DC',
    )

    ChrTalk(
        0x00FE,
        (
            '市长候选人诺曼\n',
            '请多多关照～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让卢安市重生为\n',
            '充满活力的旅游城市！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的选举\n',
            '请务必投诺曼宝贵１票！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2777')

    def _loc_26DC(): pass

    label('loc_26DC')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '波尔多斯阵营的\n',
            '宣传员好像也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～这下\n',
            '更要重新鼓足气势了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长候选人诺曼\n',
            '请多多关照～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下任市长是诺曼！\n',
            '请投诺曼宝贵１票！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2777(): pass

    label('loc_2777')

    Jump('loc_2851')

    def _loc_277A(): pass

    label('loc_277A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2851',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2800',
    )

    ChrTalk(
        0x00FE,
        (
            '市长候选人诺曼\n',
            '请多多关照～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让卢安市重生为\n',
            '充满活力的旅游城市！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的选举\n',
            '请务必投诺曼宝贵１票！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2851')

    def _loc_2800(): pass

    label('loc_2800')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '市长候选人诺曼\n',
            '请多多关照～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下任市长是诺曼！\n',
            '请投诺曼宝贵１票！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2851(): pass

    label('loc_2851')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2855
@scena.Code('func_10_2855')
def func_10_2855():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_28AA',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才开始\n',
            '选举的声音就吵个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怪不得旅行费用\n',
            '变得这么便宜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2901')

    def _loc_28AA(): pass

    label('loc_28AA')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '景色是很不错，\n',
            '就是选举的声音有点吵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '休养的心情都破坏了，\n',
            '唉，也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2901(): pass

    label('loc_2901')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2905
@scena.Code('func_11_2905')
def func_11_2905():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2957',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然是以娱乐场为目的\n',
            '来旅行的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但也不能不去市内看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2997')

    def _loc_2957(): pass

    label('loc_2957')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '喔喔，好厉害的桥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想看一次\n',
            '它运转时的样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2997(): pass

    label('loc_2997')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x299B
@scena.Code('func_12_299B')
def func_12_299B():
    Call(0, 0x0013)

    Return()

# id: 0x0013 offset: 0x29A0
@scena.Code('func_13_29A0')
def func_13_29A0():
    TalkBegin(0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2A40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A1A',
    )

    ChrTalk(
        0x0028,
        (
            '浮在天上的岛\n',
            '今天金光四射……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '……那个光辉是通往未来的门吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '还是\n',
            '是结束的征兆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_2A3D')

    def _loc_2A1A(): pass

    label('loc_2A1A')

    ChrTalk(
        0x0028,
        (
            '浮在天上的岛\n',
            '今天金光四射……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A3D(): pass

    label('loc_2A3D')

    Jump('loc_2EB9')

    def _loc_2A40(): pass

    label('loc_2A40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2B31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AE8',
    )

    ChrTalk(
        0x0028,
        (
            '就算用沙筑起的宫殿，\n',
            '沙子到底是沙子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '下一场雨\n',
            '就烟消云散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '难以得到的就难以失去，\n',
            '容易得到的也容易失去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '……同样的道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_2B2E')

    def _loc_2AE8(): pass

    label('loc_2AE8')

    ChrTalk(
        0x0028,
        (
            '就算用沙筑起的宫殿，\n',
            '沙子到底是沙子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '下一场雨\n',
            '就消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B2E(): pass

    label('loc_2B2E')

    Jump('loc_2EB9')

    def _loc_2B31(): pass

    label('loc_2B31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2C9E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 3, 0x4CB)),
            Expr.Return,
        ),
        'loc_2C38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2B9F',
    )

    ChrTalk(
        0x0028,
        (
            '发生过一次的事\n',
            '就期待再次发生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '人心始终是复杂的啊。\n',
            '但这也不是什么坏事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C35')

    def _loc_2B9F(): pass

    label('loc_2B9F')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0028,
        (
            '………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '发生过一次的事，\n',
            '就期待再次发生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '往这方向去想\n',
            '是人心特有的结构哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '绝不是你的心\n',
            '有什么不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C35(): pass

    label('loc_2C35')

    Jump('loc_2C9B')

    def _loc_2C38(): pass

    label('loc_2C38')

    ChrTalk(
        0x0028,
        (
            '集聚，相恋，誓约，\n',
            '吹走消散……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '空中的云也……\n',
            '为了换取自身的自由，\n',
            '承受着几多的离别啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2C9B(): pass

    label('loc_2C9B')

    Jump('loc_2EB9')

    def _loc_2C9E(): pass

    label('loc_2C9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2D77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2CFC',
    )

    ChrTalk(
        0x0028,
        (
            '人的心就像彼此\n',
            '相照映的镜子一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '爱和憎，\n',
            '都在被反射时\n',
            '相互增辉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D74')

    def _loc_2CFC(): pass

    label('loc_2CFC')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0028,
        (
            '人的心就像彼此\n',
            '相照映的镜子一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '如果我憎恨你\n',
            '不知不觉你也会憎恨我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '而后我就会更加\n',
            '强烈地憎恨你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D74(): pass

    label('loc_2D74')

    Jump('loc_2EB9')

    def _loc_2D77(): pass

    label('loc_2D77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2DE1',
    )

    ChrTalk(
        0x0028,
        (
            '哎呀，今天蓝天\n',
            '也是这么广阔晴朗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '看啊，看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '从那么高的地方\n',
            '俯视着我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EB9')

    def _loc_2DE1(): pass

    label('loc_2DE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2EB9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2E52',
    )

    ChrTalk(
        0x0028,
        (
            '啊啊，如果没有名字\n',
            '会有多么自由呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '像破茧而出的蝴蝶一样，\n',
            '我也是因为自我而存在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EB9')

    def _loc_2E52(): pass

    label('loc_2E52')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0028,
        (
            '人的名字\n',
            '到底有什么意义呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '我就是我本身……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0028,
        (
            '为什么要使用语言\n',
            '制造出另一个我呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EB9(): pass

    label('loc_2EB9')

    TalkEnd(0x0028)

    Return()

# id: 0x0014 offset: 0x2EBD
@scena.Code('func_14_2EBD')
def func_14_2EBD():
    ChrTalk(
        0x0027,
        (
            '叔父大人怎么会这么晚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '我已经\n',
            '等了１个小时了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '呀，抱歉抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '意想不到的大鱼\n',
            '上钩了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '啊，真受不了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '在这样的城市中\n',
            '也能钓鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '哈哈，别那么生气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0015 offset: 0x2F7D
@scena.Code('func_15_2F7D')
def func_15_2F7D():
    TalkBegin(0x00FE)
    OP_4A(0x0025, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2FE4',
    )

    ChrTalk(
        0x00FE,
        (
            '要吃饭的话，\n',
            '推荐去南区的渔师酒馆哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起娱乐场\n',
            '我想叔父大人更喜欢那家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FEB')

    def _loc_2FE4(): pass

    label('loc_2FE4')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    Call(0, 0x0014)

    def _loc_2FEB(): pass

    label('loc_2FEB')

    OP_4B(0x0025, 255)
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x2FF3
@scena.Code('func_16_2FF3')
def func_16_2FF3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_304C',
    )

    OP_4A(0x0027, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_303E',
    )

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '去填饱肚子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '知道哪里比较好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3045')

    def _loc_303E(): pass

    label('loc_303E')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    Call(0, 0x0014)

    def _loc_3045(): pass

    label('loc_3045')

    OP_4B(0x0027, 255)

    Jump('loc_332F')

    def _loc_304C(): pass

    label('loc_304C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_30E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_309A',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～比试耐力吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，这也挺有趣的。\n',
            '就决一胜负吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30E0')

    def _loc_309A(): pass

    label('loc_309A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

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
            '………来，怎么了。\n',
            '来，快咬钩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30E0(): pass

    label('loc_30E0')

    Jump('loc_332F')

    def _loc_30E3(): pass

    label('loc_30E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_3112',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么怎么？\n',
            '哎呀，怎么这么吵闹？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_332F')

    def _loc_3112(): pass

    label('loc_3112')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3237',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.PushLong, 0x3C),
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xC8),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_314A',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_314F')

    def _loc_314A(): pass

    label('loc_314A')

    ChrSetSubChip(0x00FE, 2)

    def _loc_314F(): pass

    label('loc_314F')

    ChrSetDirection(0x00FE, 225, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_31B9',
    )

    ChrTalk(
        0x00FE,
        (
            '朋友说得对，\n',
            '的确是相当不错的钓鱼点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '这下似乎能期待一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322F')

    def _loc_31B9(): pass

    label('loc_31B9')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '嗯，在这市区里有许多\n',
            '相当不错的钓鱼点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然品种不怎么样，\n',
            '但经常能上钩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和拜舍尔\n',
            '说的一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_322F(): pass

    label('loc_322F')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_332F')

    def _loc_3237(): pass

    label('loc_3237')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_332F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_32B7',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安如传言一样，\n',
            '真是满城选举的气氛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么吵闹\n',
            '真担心鱼会逃跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '暂且喝杯茶，\n',
            '然后再开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_332F')

    def _loc_32B7(): pass

    label('loc_32B7')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们。\n',
            '在工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来，如传言一样卢安\n',
            '真是满城选举的气氛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么吵闹\n',
            '真担心鱼会逃跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_332F(): pass

    label('loc_332F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x3333
@scena.Code('func_17_3333')
def func_17_3333():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_341E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_338F',
    )

    ChrTalk(
        0x0024,
        (
            '再过一会儿\n',
            '就去南区看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '好像是个危险的地方，\n',
            '有点害怕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_341E')

    def _loc_338F(): pass

    label('loc_338F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0024,
        (
            '嗯～好美的景色啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '我是柏斯来的商人，\n',
            '正在寻找新的旅游资源。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '因为这个城市魅力的本质是港口呢。\n',
            '我想南区的开发会是今后的关键。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_341E(): pass

    label('loc_341E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x3422
@scena.Code('func_18_3422')
def func_18_3422():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_351D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34C4',
    )

    ChrTalk(
        0x00FE,
        (
            '本、本来预定用打工\n',
            '挣的钱作旅费……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这么快就用光了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈……怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈、哈哈……哈哈……\n',
            '啊哈哈哈哈…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_351A')

    def _loc_34C4(): pass

    label('loc_34C4')

    ChrTalk(
        0x00FE,
        (
            '打、打工挣的钱\n',
            '已经用光了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下又一分钱都没了吗。\n',
            '哈、哈哈哈哈哈…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_351A(): pass

    label('loc_351A')

    Jump('loc_3560')

    def _loc_351D(): pass

    label('loc_351D')

    ChrTalk(
        0x00FE,
        (
            '吃喝玩乐…把买回去的\n',
            '船票钱都用掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊……怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3560(): pass

    label('loc_3560')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x3564
@scena.Code('func_19_3564')
def func_19_3564():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35DF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0450360347V#1740F巡逻啦向导啦，\n',
            '从早工作到晚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360348V#1749F呼，多少能理解\n',
            '游击士的辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    Jump('loc_3649')

    def _loc_35DF(): pass

    label('loc_35DF')

    ChrTalk(
        0x00FE,
        (
            '#0450360347V#1740F巡逻啦向导啦，\n',
            '从早工作到晚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360348V#1749F呼，多少能理解\n',
            '游击士的辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3649(): pass

    label('loc_3649')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x364D
@scena.Code('func_1A_364D')
def func_1A_364D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_37C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3752',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0470360351V#1751F哟，艾丝蒂尔㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360352V#1750F你应该知道\n',
            '去南区可以乘船了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360353V#1754F唉，不过想想\n',
            '也真辛苦啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360354V#1756F因为，你看。\n',
            '我是个好人吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360355V被大家一拜托，\n',
            '就怎么也拒绝不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    Jump('loc_37C6')

    def _loc_3752(): pass

    label('loc_3752')

    ChrTalk(
        0x00FE,
        (
            '#0470360356V#1756F看起来很轻松，\n',
            '没想到这么辛苦啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360357V#1751F因为我是个好人，\n',
            '有人拜托就拒绝不了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37C6(): pass

    label('loc_37C6')

    Jump('loc_38A8')

    def _loc_37C9(): pass

    label('loc_37C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_38A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_383E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0470360358V#1756F桥不能动了，\n',
            '去南区可以乘船了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360359V从酒店地下\n',
            '可以到达渡口哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    Jump('loc_38A8')

    def _loc_383E(): pass

    label('loc_383E')

    ChrTalk(
        0x00FE,
        (
            '#0470360360V#1756F从酒店地下\n',
            '可以到达渡口哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360361V#1750F那边有我们的成员\n',
            '带路，可以问问看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38A8(): pass

    label('loc_38A8')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x38AC
@scena.Code('func_1B_38AC')
def func_1B_38AC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3930',
    )

    ChrTalk(
        0x00FE,
        (
            '#0460360362V#1763F城市暂时相当安定，\n',
            '但不知道还会发生什么事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460360363V#1760F我们也不能疏忽大意，\n',
            '要持续警戒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3930(): pass

    label('loc_3930')

    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x3934
@scena.Code('func_1C_3934')
def func_1C_3934():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_39C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_398E',
    )

    ChrTalk(
        0x00FE,
        (
            '要去南街区\n',
            '请走这边的酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '酒店地下１层\n',
            '可以通向渡口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    Jump('loc_39C3')

    def _loc_398E(): pass

    label('loc_398E')

    ChrTalk(
        0x00FE,
        (
            '有事可做\n',
            '真好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少\n',
            '不会觉得无聊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    def _loc_39C3(): pass

    label('loc_39C3')

    Jump('loc_3A7C')

    def _loc_39C6(): pass

    label('loc_39C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3A7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A3A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～现在大桥\n',
            '不能通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要去南街区\n',
            '请走这边的酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '酒店地下１层\n',
            '可以通向渡口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    Jump('loc_3A7C')

    def _loc_3A3A(): pass

    label('loc_3A3A')

    ChrTalk(
        0x00FE,
        (
            '要去南街区\n',
            '请走这边的酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '酒店地下１层\n',
            '可以通向渡口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A7C(): pass

    label('loc_3A7C')

    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x3A80
@scena.Code('func_1D_3A80')
def func_1D_3A80():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 2, 0x20BA)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3A91',
    )

    Return()

    def _loc_3A91(): pass

    label('loc_3A91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AA6',
    )

    Call(0, 0x0035)
    Call(0, 0x0036)

    def _loc_3AA6(): pass

    label('loc_3AA6')

    EventBegin(0x00)
    OP_4A(0x003A, 255)
    OP_4A(0x0038, 255)
    OP_4A(0x0039, 255)
    ChrTurnDirection(0x0000, 0x003A, 0)
    ChrTurnDirection(0x0001, 0x003A, 0)
    ChrTurnDirection(0x0002, 0x003A, 0)
    ChrTurnDirection(0x0003, 0x003A, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360285V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_3B42')
    def lambda_3B42():
        CameraMove(51000, 0, 70500, 3000)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_3B42)

    OP_0D()
    WaitForThreadExit(0x0038, 0x0001)
    Sleep(1000)

    ChrSetPos(0x0101, 51550, 0, 79700, 180)
    ChrSetPos(0x0102, 50300, 0, 80000, 180)
    ChrSetPos(0x00F8, 51550, 0, 80960, 180)
    ChrSetPos(0x00F9, 50300, 0, 81370, 180)

    ChrTalk(
        0x003A,
        (
            '#0460360286V#1761F哟，状况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0038,
        (
            '#0450360287V#1741F啊啊，照指示\n',
            '都在好好引导市民坐船呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360288V告诉他们桥不能通行，要去南区\n',
            '就要使用酒店的小船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0039,
        (
            '#0470360289V#1750F#4P其他成员\n',
            '也都各尽其职呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360290V#1751F#4P意外的是，我们的成员\n',
            '中有不少认真的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x003A,
        (
            '#0460360291V#1763F啊啊，现在\n',
            '他们好像都很努力呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460360292V#1760F如果有人偷懒\n',
            '马上来通知我哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460360293V我去搞定他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0038,
        (
            '#0450360294V#1740F噢、噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D63')
    def lambda_3D63():
        CameraMove(50910, 0, 72470, 2500)

        ExitThread()

    DispatchAsync(0x0038, 0x0002, lambda_3D63)

    @scena.Lambda('lambda_3D7B')
    def lambda_3D7B():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001770, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D7B)

    Sleep(100)

    @scena.Lambda('lambda_3D96')
    def lambda_3D96():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001770, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3D96)

    Sleep(100)

    @scena.Lambda('lambda_3DB1')
    def lambda_3DB1():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001770, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_3DB1)

    Sleep(100)

    @scena.Lambda('lambda_3DCC')
    def lambda_3DCC():
        OP_94(0x01, 0x00FE, 0x0000, 0x00001770, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_3DCC)

    WaitForThreadExit(0x00F9, 0x0002)
    WaitForThreadExit(0x0038, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E80',
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
        0,
        (
            TXT(0x00, '【◇听说了渡鸦帮的改正】\n'),
            TXT(0x01, '【◇没听说渡鸦帮的改正】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3E74'),
        (0x00000001, 'loc_3E7A'),
        (-1, 'loc_3E80'),
    )

    def _loc_3E74(): pass

    label('loc_3E74')

    SetScenaFlags(ScenaFlag(0x0410, 0, 0x2080))

    Jump('loc_3E80')

    def _loc_3E7A(): pass

    label('loc_3E7A')

    ClearScenaFlags(ScenaFlag(0x0410, 0, 0x2080))

    Jump('loc_3E80')

    def _loc_3E80(): pass

    label('loc_3E80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 0, 0x2080)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Return,
        ),
        'loc_3ED5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360295V#1011F#1P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360296V在这种地方商量什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F7D')

    def _loc_3ED5(): pass

    label('loc_3ED5')

    ChrTalk(
        0x0101,
        (
            '#0010360297V#1009F#1P什～么搞定他啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360298V在这种地方偷偷摸摸，\n',
            '又在搞什么阴谋诡计？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F7D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360299V#551F#3P……真是些毫无上进心的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F7D(): pass

    label('loc_3F7D')

    Jump('loc_3FCD')

    def _loc_3F80(): pass

    label('loc_3F80')

    ChrTalk(
        0x0101,
        (
            '#0010360300V#1011F#1P哎啊～真令人吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360301V好像真的在努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3FCD(): pass

    label('loc_3FCD')

    OP_62(0x003A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0038, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0039, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_4027')
    def lambda_4027():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_4027)

    @scena.Lambda('lambda_4035')
    def lambda_4035():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_4035)

    @scena.Lambda('lambda_4043')
    def lambda_4043():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_4043)

    Sleep(500)

    ChrTalk(
        0x003A,
        (
            '#0460360302V#1762F你，你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40AB',
    )

    ChrTalk(
        0x0038,
        (
            '#0450360303V#1743F阿、阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D3')

    def _loc_40AB(): pass

    label('loc_40AB')

    ChrTalk(
        0x0038,
        (
            '#0450360304V#1741F哦，好久不见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40D3(): pass

    label('loc_40D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 0, 0x2080)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_463D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Return,
        ),
        'loc_413E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360305V#1015F#1P在南街区\n',
            '也看到他们的身影……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360306V你们\n',
            '在搞什么活动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4235')

    def _loc_413E(): pass

    label('loc_413E')

    ChrTalk(
        0x0101,
        (
            '#0010360307V#1019F#1P那，这次\n',
            '在商量什么坏事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360308V顺手牵羊？\n',
            '还是恐吓？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0039, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0039,
        (
            '#0470360309V#1755F艾、艾丝蒂尔～\n',
            '你又误解啦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360310V#1756F我们渡鸦帮\n',
            '脱胎换骨了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360311V#1004F#1P咦？怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4235(): pass

    label('loc_4235')

    ChrTalk(
        0x0038,
        (
            '#0450360312V#1740F#4P喔……\n',
            '是洛克那家伙提议的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360313V#1741F前阵子开始做城里的\n',
            '警备和向导了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42FC',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_433A')

    def _loc_42FC(): pass

    label('loc_42FC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4323',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_433A')

    def _loc_4323(): pass

    label('loc_4323')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_433A(): pass

    label('loc_433A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4361',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_439F')

    def _loc_4361(): pass

    label('loc_4361')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4388',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_439F')

    def _loc_4388(): pass

    label('loc_4388')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_439F(): pass

    label('loc_439F')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010360314V#1004F#1P骗、骗人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43FF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360315V#052F#3P真的假的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43FF(): pass

    label('loc_43FF')

    ChrTalk(
        0x0102,
        (
            '#0020360316V#1044F#4P就是说……\n',
            '像自卫队一样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x003A,
        (
            '#0460360317V#1761F#4P才没那么死板呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460360318V刚才还正在商量其他\n',
            '相关活动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360319V#1015F#1P嗯、嗯………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360320V感觉太突然了，\n',
            '难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360321V#1040F#4P不过看起来是真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x003A,
        (
            '#0460360322V#1763F#4P嗯，反正也没\n',
            '指望你们相信啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460360323V#1764F这不是为了任何人……\n',
            '而是完全为了\n',
            '我们自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x003A, 180, 400)
    Sleep(500)

    ChrTalk(
        0x003A,
        (
            '#0460360324V#1760F……继续商量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0038,
        (
            '#0450360325V#1743F#4P噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0038, 315, 400)

    ChrTalk(
        0x0039,
        (
            '#0470360326V#1750F想去南区的话\n',
            '请使用渡船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360327V从酒店地下\n',
            '可以到达渡口哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49EA')

    def _loc_463D(): pass

    label('loc_463D')

    ChrTalk(
        0x0039,
        (
            '#0470360328V#1751F嘿嘿，怎样？\n',
            '艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360329V我们的出色表现，\n',
            '听说了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360330V#1000F#1P听嘉恩先生说了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360331V似乎开始用自己的力量\n',
            '保护起卢安了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0038,
        (
            '#0450360332V#1740F喔，这个活动\n',
            '是洛克那家伙提议的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0450360333V现在正在城市中\n',
            '负责警备和向导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360316V#1044F#4P就是说……\n',
            '像自卫队一样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x003A,
        (
            '#0460360335V#1761F才没那么死板呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460360318V刚才还正在商量其他\n',
            '相关活动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_486D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360337V#053F#3P嗯，算是给自己\n',
            '做了个了断吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360338V#051F不知道你们能做到何种程度，\n',
            '就都努力做做看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_486D(): pass

    label('loc_486D')

    ChrTalk(
        0x003A,
        (
            '#0460360339V#1763F我们是自愿的，\n',
            '不会给你们添麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0460360340V#1761F当然实际的活动\n',
            '还是要请协会配合吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360341V#1006F#1P啊，嗯。\n',
            '请多帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360342V#1040F#4P多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x003A,
        (
            '#0460360343V#1760F那么，我们\n',
            '还要继续商量呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x003A, 180, 400)

    ChrTalk(
        0x0039,
        (
            '#0470360326V#1750F想去南区的话\n',
            '请使用渡船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0470360327V从酒店地下\n',
            '可以到达渡口哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0038,
        (
            '#0450360346V#1741F那么，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_49EA(): pass

    label('loc_49EA')

    ChrSetDirection(0x0038, 315, 400)
    ChrSetDirection(0x0039, 45, 400)
    OP_4B(0x003A, 255)
    OP_4B(0x0038, 255)
    OP_4B(0x0039, 255)
    SetScenaFlags(ScenaFlag(0x0417, 2, 0x20BA))
    SetScenaFlags(ScenaFlag(0x0410, 0, 0x2080))
    EventEnd(0x00)

    Return()

# id: 0x001E offset: 0x4A0D
@scena.Code('func_1E_4A0D')
def func_1E_4A0D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A1E',
    )

    Call(0, 0x0035)

    def _loc_4A1E(): pass

    label('loc_4A1E')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(25350, 0, 114410, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 25710, 0, 114720, 179)
    ChrSetPos(0x00F7, 24700, 0, 115030, 168)
    ChrSetPos(0x0109, 25250, 0, 113150, 181)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0109,
        (
            '#0180210386V#1068F#5P哎呀哎呀，终于回来了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0109, 0, 400)

    ChrTalk(
        0x0109,
        (
            '#0180210387V#1062F太感谢了。\n',
            '送到这里真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210388V#1016F#5P啊哈哈，不用谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4BBC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210389V#051F就算没有我们\n',
            '你自己也没问题吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210390V虽说弩箭比较老式……\n',
            '但本事可是相当了不得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C25')

    def _loc_4BBC(): pass

    label('loc_4BBC')

    ChrTalk(
        0x0103,
        (
            '#0030210391V#027F就算没有我们\n',
            '你也没问题吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210392V弩箭虽然很少见……\n',
            '但本领却是相当了得吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C25(): pass

    label('loc_4C25')

    ChrTalk(
        0x0109,
        (
            '#0180210393V#1066F呀～因为巡回神父\n',
            '都是自己在外单独行事的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210394V最低限度的武装还是要准备的，\n',
            '但哪里比得上专业人士嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210395V#1015F#5P嗯～是吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210396V我倒觉得你的本事\n',
            '当游击士都足够了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180210397V#1061F哎呀，艾丝蒂尔真是的～\n',
            '都把人捧上天啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210398V大哥哥会当真哦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210399V#1019F#5P说、说什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210400V#1061F哈哈，小事情不要介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210401V#1060F说到刚才的幽灵，\n',
            '卢安教会\n',
            '也有好几个人来询问的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210402V只是，据迪奥德罗教区长说\n',
            '好像不是普通的灵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210403V#1004F#5P不是普通的灵……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4F10',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210404V#050F根据教会的教条，人死之后，\n',
            '多行善事的灵魂会上天堂对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F5E')

    def _loc_4F10(): pass

    label('loc_4F10')

    ChrTalk(
        0x0103,
        (
            '#0030210405V#020F根据教会的教条，人死之后，\n',
            '多行善事的灵魂会上天堂对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F5E(): pass

    label('loc_4F5E')

    ChrTalk(
        0x0109,
        (
            '#0180210406V#1065F嗯嗯，相反背负罪责的灵魂\n',
            '会堕入昏暗的炼狱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210407V但，偶尔也会有跳出这限制\n',
            '两边都去不了的灵魂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210408V#1060F那就是所谓的『幽灵』，\n',
            '教会一般都是这么说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210409V#1007F#5P唔唔……\n',
            '就是迷途的灵魂吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210410V#1015F但是，说它不普通\n',
            '又是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210411V#1063F普通的灵，大多数\n',
            '都是被什么所束缚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210412V或者是地方，或者是人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210413V但是，这次的幽灵骚动\n',
            '好象两者都不是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210414V因此教区长\n',
            '也束手无策啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210415V#1002F#5P原来如此……这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210416V#1062F嗯，就作为\n',
            '调查的参考吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210417V#1061F那么，我回教会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210418V再见～艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0109, 180, 400)

    @scena.Lambda('lambda_5214')
    def lambda_5214():
        ChrWalkTo(0x0109, 25430, 1050, 103010, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_5214)

    @scena.Lambda('lambda_522F')
    def lambda_522F():
        CameraMove(25620, 0, 112450, 1500)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_522F)

    WaitForThreadExit(0x0109, 0x0001)
    WaitForThreadExit(0x0109, 0x0002)

    @scena.Lambda('lambda_5251')
    def lambda_5251():
        CameraMove(25470, 0, 115430, 1000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_5251)

    WaitForThreadExit(0x0109, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010210419V#1025F#5P嗯～刚才那番话倒\n',
            '挺像个神职者的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210420V但还是怎样看\n',
            '也不像是个神父啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_535A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210421V#051F#3P嗯，巡回神父\n',
            '多数都是些怪家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210422V从前来拉文努村的巡回神父\n',
            '也是个很奇怪的大叔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53E2')

    def _loc_535A(): pass

    label('loc_535A')

    ChrTalk(
        0x0103,
        (
            '#0030210423V#021F#3P呵呵，巡回神父\n',
            '好像不少人都挺奇怪的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210424V#020F我在剧团的时候就\n',
            '有个不知为何随同旅行的\n',
            '奇怪巡回修女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53E2(): pass

    label('loc_53E2')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 3, 0x1213)),
            Expr.Return,
        ),
        'loc_5482',
    )

    OP_28(0x0082, 0x01, 0x0400)

    ChrTalk(
        0x0101,
        (
            '#0010210425V#1016F#2P嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210426V#1006F好了……\n',
            '嘉恩哥哥那需要我们收集\n',
            '的目击情报都齐了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210427V先回协会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5506')

    def _loc_5482(): pass

    label('loc_5482')

    ChrTalk(
        0x0101,
        (
            '#0010210425V#1016F#2P嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210429V#1006F好了……\n',
            '还有没收集到的目击情报吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210430V照这个势头去找下一个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5506(): pass

    label('loc_5506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5536',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210431V#051F#3P啊啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_555C')

    def _loc_5536(): pass

    label('loc_5536')

    ChrTalk(
        0x0103,
        (
            '#0030210432V#020F#3P嗯嗯，是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_555C(): pass

    label('loc_555C')

    OP_59()
    OP_B7(0x08)
    FormationDelMember(0x08, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 3, 0x121B))
    EventEnd(0x00)

    Return()

# id: 0x001F offset: 0x5568
@scena.Code('func_1F_5568')
def func_1F_5568():
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
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
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
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
    ChrSetFlags(0x0010, 0x0200)
    ChrSetFlags(0x0011, 0x0200)
    ChrSetFlags(0x0012, 0x0200)
    ChrSetFlags(0x0013, 0x0200)
    ChrSetFlags(0x0014, 0x0200)
    ChrSetFlags(0x0015, 0x0200)
    ChrSetFlags(0x0016, 0x0200)
    ChrSetFlags(0x0017, 0x0200)
    ChrSetFlags(0x0018, 0x0200)
    ChrSetFlags(0x0019, 0x0200)
    ChrSetFlags(0x001A, 0x0200)
    ChrSetFlags(0x001B, 0x0200)
    ChrSetFlags(0x001C, 0x0200)
    ChrSetFlags(0x001D, 0x0200)
    ChrSetFlags(0x001E, 0x0200)
    ChrSetFlags(0x001F, 0x0200)
    ChrSetFlags(0x0020, 0x0200)
    ChrSetFlags(0x0021, 0x0200)
    ChrSetFlags(0x0022, 0x0200)
    ChrSetPos(0x0008, 50530, 500, 56000, 180)
    ChrSetPos(0x0009, 49520, 500, 56510, 180)
    ChrSetChipByIndex(0x0009, 25)
    ChrSetPos(0x000A, 51000, 500, 53200, 180)
    ChrSetPos(0x000B, 52000, 500, 53900, 180)
    ChrSetPos(0x000C, 50000, 500, 53900, 180)
    ChrSetPos(0x000D, 51000, 500, 50900, 0)
    ChrSetPos(0x000E, 52000, 500, 50200, 0)
    ChrSetPos(0x000F, 50000, 500, 50200, 0)
    ChrSetPos(0x0010, 52430, 500, 57380, 180)
    ChrSetPos(0x0012, 51660, 500, 58000, 180)
    ChrSetPos(0x0013, 50430, 500, 58170, 180)
    ChrSetPos(0x0011, 51470, 500, 56000, 180)
    ChrSetPos(0x0015, 49980, 500, 58910, 180)
    ChrSetPos(0x0018, 51100, 500, 58910, 180)
    ChrSetPos(0x0016, 52320, 500, 58610, 180)
    ChrSetPos(0x0014, 49520, 500, 59500, 180)
    ChrSetPos(0x0019, 49520, 500, 57540, 180)
    ChrSetPos(0x0017, 52480, 500, 56280, 180)
    ChrSetPos(0x001A, 52460, 500, 48150, 0)
    ChrSetPos(0x001C, 51560, 500, 48150, 0)
    ChrSetPos(0x001D, 50340, 500, 48330, 0)
    ChrSetPos(0x0021, 49530, 500, 48350, 0)
    ChrSetPos(0x001B, 51920, 500, 47190, 0)
    ChrSetPos(0x0020, 50310, 500, 47010, 0)
    ChrSetPos(0x001F, 49520, 500, 47190, 0)
    ChrSetPos(0x0022, 50900, 500, 46310, 0)
    ChrSetPos(0x001E, 52460, 500, 46310, 0)
    CreateThread(0x0008, 0x01, 0x00, func_02_E90)
    CreateThread(0x0009, 0x01, 0x00, func_02_E90)

    Return()

# id: 0x0020 offset: 0x58B4
@scena.Code('func_20_58B4')
def func_20_58B4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_58C1',
    )

    Return()

    def _loc_58C1(): pass

    label('loc_58C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_58D2',
    )

    Call(0, 0x0035)

    def _loc_58D2(): pass

    label('loc_58D2')

    EventBegin(0x00)
    Fade(500)
    CameraMove(51260, 0, 69660, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 51710, 0, 69900, 180)
    ChrSetPos(0x00F7, 50470, 0, 70110, 180)
    OP_0D()
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    ChrSetPos(0x000F, 49710, 500, 50290, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    MapClearFlags(0x00000001)
    MapClearFlags(0x00000010)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x00F7, 0x0040)
    ChrSetPos(0x0101, 51880, 0, 66000, 180)
    ChrSetPos(0x00F7, 50550, 0, 66000, 180)
    CameraMove(51370, 500, 44910, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(4620, 0)
    OP_6C(51000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_59F0')
    def lambda_59F0():
        CameraMove(51130, 500, 57140, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_59F0)

    Sleep(300)

    @scena.Lambda('lambda_5A0D')
    def lambda_5A0D():
        OP_67(0, 8000, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5A0D)

    @scena.Lambda('lambda_5A25')
    def lambda_5A25():
        ChrWalkTo(0x00FE, 51650, 500, 61250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5A25)

    Sleep(300)

    @scena.Lambda('lambda_5A45')
    def lambda_5A45():
        ChrWalkTo(0x00FE, 50260, 500, 61370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_5A45)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    Fade(1000)
    CameraMove(51380, 500, 52340, 0)
    OP_67(0, 4980, -10000, 0)
    CameraSetDistance(3650, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#2840210487V#5P别装傻了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2840210488V#5P酒店出现的幽灵\n',
            '肯定是你们搞的鬼，\n',
            '我们已经知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2850210489V#5P诺曼先生的儿子\n',
            '也因受惊而昏过去了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2850210490V#5P不觉得太过分了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2860210491V#6P哼，那小子不是\n',
            '渡鸦帮的不良少年吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2860210492V#6P那种不正经的人说的话\n',
            '能信吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2870210493V#5P……等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2870210494V#5P要是批判我个人那还好说，\n',
            '攻击家人太卑鄙了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2870210495V#5P那不正经这类的说法\n',
            '能不能收回呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1810210496V#5P嗯～确实那句\n',
            '可能说得过分了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#1790210497V#2P我说主任！\n',
            '别就这么认了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1790210498V#2P就因为你这么软弱\n',
            '才会让旅游推进派得势的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000B, 400)

    ChrTalk(
        0x000C,
        (
            '#2840210499V#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2850210500V#5P得势的不是\n',
            '你们港湾维持派吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2850210501V#5P还用幽灵骚动这种诡计，\n',
            '让人感到恶心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0101, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010210502V#1007F#5P糟糕……\n',
            '吵架升温了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210503V#1002F是不是去阻止比较好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5EAC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210504V#050F#1P好象还没打起来，\n',
            '可能还早了点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210505V不过，一旦打起来的话\n',
            '就马上移动到\n',
            '能够阻止的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F2B')

    def _loc_5EAC(): pass

    label('loc_5EAC')

    ChrTalk(
        0x0103,
        (
            '#0030210506V#022F#1P还没开始打架，\n',
            '现在出面可能早了点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210507V但是，一旦打起来的话\n',
            '就马上移动到\n',
            '能够阻止的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F2B(): pass

    label('loc_5F2B')

    ChrTalk(
        0x0101,
        (
            '#0010210508V#1007F#5P话虽如此，围观的人太多\n',
            '完全无法前进了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210509V#1019F真是的，奈尔他们\n',
            '竟然抢了前面的位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5FB0')
    def lambda_5FB0():
        CameraMove(51380, 500, 52340, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5FB0)

    OP_62(0x000E, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(500)

    Sleep(100)

    OP_62(0x000F, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000C, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000B, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000F, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#2860210510V#6P不能忍了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1790210511V#2P像你这么弱不禁风的家伙\n',
            '比腕力别想赢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#2840210512V#5P求、求之不得！\n',
            '怕你不成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2850210513V#5P诺曼先生的名誉\n',
            '由我们诺曼商会员来守护！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 300, 500)
    Sleep(300)

    ChrSetDirection(0x000A, 49, 500)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#2870210514V#6P你们快住手！\n',
            '暴力是不行的，不行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 124, 500)
    Sleep(300)

    ChrSetDirection(0x000D, 213, 500)
    Sleep(300)

    ChrTalk(
        0x000D,
        (
            '#1810210515V#5P大家稳住！\n',
            '现在应该冷静协商……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0101, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010210516V#1005F#5P（糟了……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6234',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210517V#552F#1P（……阻止不了吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6266')

    def _loc_6234(): pass

    label('loc_6234')

    ChrTalk(
        0x0103,
        (
            '#0030210518V#025F#1P（这下阻止不了了啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6266(): pass

    label('loc_6266')

    OP_1F(0x00, 0x00000190)
    Sleep(400)

    OP_20(0x00000000)
    PlaySE(190, 0x00, 0x64)
    Sleep(1000)

    Sleep(500)

    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
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
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0019, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x001A, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x001B, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0017, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x001C, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0020, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0016, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x001F, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0022, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0011, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0021, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    OP_72(0x0019, 0x0002)
    OP_71(0x0019, 0x0020)
    OP_71(0x0019, 0x0040)
    OP_6F(0x0019, 301)
    OP_70(0x0019, 360)
    OP_A1(0x0033, 0x0019)
    ChrSetFlags(0x0033, 0x0040)
    ChrSetPos(0x0033, 30000, -2800, 52100, 90)
    ChrSetDirection(0x0033, 270, 0)
    OP_89(0x0104, 30500, -2500, 52100, 90)
    ChrSetChipByIndex(0x0104, 27)
    ChrSetSubChip(0x0104, 0)

    NpcTalk(
        0x0104,
        '青年的声音',
        (
            '#0040210519V呼……\n',
            '真是可悲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    CameraMove(40290, 500, 51970, 0)
    OP_67(0, 7050, -10000, 0)
    CameraSetDistance(3320, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    CreateThread(0x0033, 0x00, 0x00, func_21_79DB)

    @scena.Lambda('lambda_6608')
    def lambda_6608():
        CameraMove(47120, 500, 52000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6608)

    @scena.Lambda('lambda_6620')
    def lambda_6620():
        OP_6C(270000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6620)

    OP_0D()

    @scena.Lambda('lambda_6631')
    def lambda_6631():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6631')

    DispatchAsync2(0x0101, 0x0001, lambda_6631)

    @scena.Lambda('lambda_6642')
    def lambda_6642():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6642')

    DispatchAsync2(0x00F7, 0x0001, lambda_6642)

    @scena.Lambda('lambda_6653')
    def lambda_6653():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6653')

    DispatchAsync2(0x0008, 0x0001, lambda_6653)

    Sleep(50)

    @scena.Lambda('lambda_6669')
    def lambda_6669():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6669')

    DispatchAsync2(0x0009, 0x0001, lambda_6669)

    @scena.Lambda('lambda_667A')
    def lambda_667A():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_667A')

    DispatchAsync2(0x000A, 0x0001, lambda_667A)

    @scena.Lambda('lambda_668B')
    def lambda_668B():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_668B')

    DispatchAsync2(0x000B, 0x0001, lambda_668B)

    Sleep(50)

    @scena.Lambda('lambda_66A1')
    def lambda_66A1():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_66A1')

    DispatchAsync2(0x000C, 0x0001, lambda_66A1)

    @scena.Lambda('lambda_66B2')
    def lambda_66B2():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_66B2')

    DispatchAsync2(0x000D, 0x0001, lambda_66B2)

    @scena.Lambda('lambda_66C3')
    def lambda_66C3():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_66C3')

    DispatchAsync2(0x000E, 0x0001, lambda_66C3)

    @scena.Lambda('lambda_66D4')
    def lambda_66D4():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_66D4')

    DispatchAsync2(0x000F, 0x0001, lambda_66D4)

    Sleep(50)

    @scena.Lambda('lambda_66EA')
    def lambda_66EA():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_66EA')

    DispatchAsync2(0x0010, 0x0001, lambda_66EA)

    @scena.Lambda('lambda_66FB')
    def lambda_66FB():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_66FB')

    DispatchAsync2(0x0011, 0x0001, lambda_66FB)

    @scena.Lambda('lambda_670C')
    def lambda_670C():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_670C')

    DispatchAsync2(0x0012, 0x0001, lambda_670C)

    Sleep(50)

    @scena.Lambda('lambda_6722')
    def lambda_6722():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6722')

    DispatchAsync2(0x0013, 0x0001, lambda_6722)

    @scena.Lambda('lambda_6733')
    def lambda_6733():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6733')

    DispatchAsync2(0x0014, 0x0001, lambda_6733)

    @scena.Lambda('lambda_6744')
    def lambda_6744():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6744')

    DispatchAsync2(0x0015, 0x0001, lambda_6744)

    Sleep(50)

    @scena.Lambda('lambda_675A')
    def lambda_675A():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_675A')

    DispatchAsync2(0x0016, 0x0001, lambda_675A)

    @scena.Lambda('lambda_676B')
    def lambda_676B():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_676B')

    DispatchAsync2(0x0017, 0x0001, lambda_676B)

    @scena.Lambda('lambda_677C')
    def lambda_677C():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_677C')

    DispatchAsync2(0x0018, 0x0001, lambda_677C)

    @scena.Lambda('lambda_678D')
    def lambda_678D():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_678D')

    DispatchAsync2(0x0019, 0x0001, lambda_678D)

    Sleep(50)

    @scena.Lambda('lambda_67A3')
    def lambda_67A3():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_67A3')

    DispatchAsync2(0x001A, 0x0001, lambda_67A3)

    @scena.Lambda('lambda_67B4')
    def lambda_67B4():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_67B4')

    DispatchAsync2(0x001B, 0x0001, lambda_67B4)

    @scena.Lambda('lambda_67C5')
    def lambda_67C5():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_67C5')

    DispatchAsync2(0x001C, 0x0001, lambda_67C5)

    Sleep(50)

    @scena.Lambda('lambda_67DB')
    def lambda_67DB():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_67DB')

    DispatchAsync2(0x001D, 0x0001, lambda_67DB)

    @scena.Lambda('lambda_67EC')
    def lambda_67EC():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_67EC')

    DispatchAsync2(0x001E, 0x0001, lambda_67EC)

    @scena.Lambda('lambda_67FD')
    def lambda_67FD():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_67FD')

    DispatchAsync2(0x001F, 0x0001, lambda_67FD)

    Sleep(50)

    @scena.Lambda('lambda_6813')
    def lambda_6813():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6813')

    DispatchAsync2(0x0020, 0x0001, lambda_6813)

    @scena.Lambda('lambda_6824')
    def lambda_6824():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6824')

    DispatchAsync2(0x0021, 0x0001, lambda_6824)

    @scena.Lambda('lambda_6835')
    def lambda_6835():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6835')

    DispatchAsync2(0x0022, 0x0001, lambda_6835)

    WaitForThreadExit(0x0033, 0x0000)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x00F7, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0020, 0xFF)
    TerminateThread(0x0021, 0xFF)
    TerminateThread(0x0022, 0xFF)
    Sleep(500)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210520V#035F纷争无法蕴育任何东西……\n',
            '只是产生空虚的裂缝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210521V#030F让我为这样的你们，献上一曲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210522V越过心中的鸿沟\n',
            '让彼此携起手来\n',
            '温柔而伤感的歌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Sleep(1000)

    PlayBGM(71)
    CreateThread(0x0104, 0x00, 0x00, func_02_E90)
    Sleep(1000)

    Sleep(500)

    OP_DB()

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210523V#70A#035F阳光映照　虹彩之桥',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(6500)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210524V#70A#035F跨越通往　你的去向……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(6500)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210525V#70A#035F有心追求 却消溶于空',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(7000)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210526V#70A#035F寂寞来袭 听浅风低吟……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(7500)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210527V#70A#032F若无法传达 这份心愿',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(7500)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210528V#70A#032F至少请留下 一道浅伤……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(8000)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210529V#70A#032F最初之约 未能守护',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(6500)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210530V#70A#035F你的气息 化作琥珀',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(8000)

    NpcTalk(
        0x0104,
        '金发的青年',
        (
            '#0040210531V#70A#035F这份梦境 永远封存……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_21()
    Sleep(300)

    OP_4A(0x0104, 255)
    Sleep(1000)

    Fade(250)
    ChrSetFlags(0x0104, 0x0002)
    ChrSetChipByIndex(0x0104, 28)
    ChrSetSubChip(0x0104, 0)
    OP_0D()
    OP_99(0x0104, 0x00, 0x03, 1500)
    Sleep(300)

    OP_99(0x0104, 0x03, 0x0A, 1000)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0104,
        (
            '#0040210532V#035F呼……\n',
            '大家都感觉得到吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210533V唯一的真实……\n',
            '那就是爱的永恒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210534V#030F用现代的话来说，\n',
            '就是Ｌｏｖｅ·ｉｓ·ｅｔｅｒｎａｌ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(137, 0x00, 0x64)
    OP_62(0x0104, 0x0000012C, 1900, 0x36, 0x39, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0104)
    PlayBGM(12)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0015, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0019, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x001A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x001B, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0017, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0018, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x001C, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0020, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0016, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x001D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x001F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0022, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0011, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x001E, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0021, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ExecExpressionWithValue(
        0x0034,
        0x01,
        (
            (Expr.GetChrWork, 0xA, 0x1),
            (Expr.GetChrWork, 0xD, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0034,
        0x02,
        (
            (Expr.GetChrWork, 0xA, 0x2),
            (Expr.GetChrWork, 0xD, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0034,
        0x03,
        (
            (Expr.GetChrWork, 0xA, 0x3),
            (Expr.GetChrWork, 0xD, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0034, 1500)

    ChrTalk(
        0x000A,
        (
            '#2870210535V#5P唔、唔咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000D, 400)

    ChrTalk(
        0x000A,
        (
            '#2870210536V#2P总而言之，波尔多斯先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2870210537V#2P现在还是双方都\n',
            '冷静一下头脑比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#1810210538V#1P嗯嗯，是啊。\n',
            '也妨碍大桥的通行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 180, 400)

    ChrTalk(
        0x000D,
        (
            '#1810210539V#2P各位，暂时回港口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000D, 400)

    ChrTalk(
        0x000F,
        (
            '#2860210540V#1P是、是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2840210541V#2P是啊……\n',
            '还得发传单呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(150)

    CreateThread(0x0013, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x0014, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x0012, 0x01, 0x00, func_22_7AF1)
    Sleep(150)

    CreateThread(0x001D, 0x01, 0x00, func_23_7B12)
    CreateThread(0x001E, 0x01, 0x00, func_23_7B12)
    CreateThread(0x001F, 0x01, 0x00, func_23_7B12)
    Sleep(130)

    CreateThread(0x0010, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x0011, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x0015, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x0016, 0x01, 0x00, func_22_7AF1)
    Sleep(150)

    CreateThread(0x001A, 0x01, 0x00, func_23_7B12)
    CreateThread(0x001B, 0x01, 0x00, func_23_7B12)
    CreateThread(0x001C, 0x01, 0x00, func_23_7B12)
    Sleep(130)

    CreateThread(0x0017, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x0018, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x0019, 0x01, 0x00, func_22_7AF1)
    Sleep(150)

    CreateThread(0x000D, 0x01, 0x00, func_23_7B12)
    CreateThread(0x000E, 0x01, 0x00, func_23_7B12)
    CreateThread(0x000F, 0x01, 0x00, func_23_7B12)
    Sleep(150)

    CreateThread(0x0020, 0x01, 0x00, func_23_7B12)
    CreateThread(0x0021, 0x01, 0x00, func_23_7B12)
    CreateThread(0x0022, 0x01, 0x00, func_23_7B12)
    Sleep(250)

    CreateThread(0x000A, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x000B, 0x01, 0x00, func_22_7AF1)
    CreateThread(0x000C, 0x01, 0x00, func_22_7AF1)
    Sleep(2500)

    @scena.Lambda('lambda_71F7')
    def lambda_71F7():
        ChrWalkTo(0x00FE, 51860, 500, 57940, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_71F7)

    @scena.Lambda('lambda_7212')
    def lambda_7212():
        ChrWalkTo(0x00FE, 50280, 500, 57590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_7212)

    @scena.Lambda('lambda_722D')
    def lambda_722D():
        ChrWalkTo(0x00FE, 49500, 500, 54170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_722D)

    @scena.Lambda('lambda_7248')
    def lambda_7248():
        CameraMove(49500, 500, 55540, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7248)

    @scena.Lambda('lambda_7260')
    def lambda_7260():
        OP_67(0, 7640, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7260)

    @scena.Lambda('lambda_7278')
    def lambda_7278():
        CameraSetDistance(3330, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_7278)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0104, 400)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x00F7, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010210542V#1019F（大、大家都走了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7305',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210543V#551F#5P（……我算是明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_733B')

    def _loc_7305(): pass

    label('loc_7305')

    ChrTalk(
        0x0103,
        (
            '#0030210544V#025F#5P（唉……\n',
            '  又是这样收场啊。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_733B(): pass

    label('loc_733B')

    ChrTalk(
        0x0104,
        (
            '#0040210545V#035F呼，对于任何国家来说，\n',
            '都有一个相同之处，\n',
            '就是民众们那容易发热又能快速冷静下来的头脑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)
    ChrTurnDirection(0x00F7, 0x0104, 400)
    Sleep(200)

    ChrTalk(
        0x0104,
        (
            '#0040210546V#033F不，真正恐怖的\n',
            '是这让人们恢复平常心…\n',
            '仿如奇迹般的旋律吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210547V#031F来吧诸位记者。\n',
            '请尽情拍照\n',
            '采访吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280210548V#150F#6P哇～可以吗。\n',
            '那么就不客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210549V#151F来，茄～～子㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 26)
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040210550V#035F嗯～太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetSubChip(0x0104, 3)
    OP_0D()
    Sleep(250)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Fade(250)
    ChrSetSubChip(0x0104, 4)
    OP_0D()
    ChrMoveTo(0x0009, 49500, 500, 51690, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0104, 400)
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Fade(250)
    ChrSetSubChip(0x0104, 7)
    OP_0D()
    ChrMoveTo(0x0009, 49500, 500, 53120, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0104, 400)
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Fade(250)
    ChrSetSubChip(0x0104, 10)
    OP_0D()
    ChrMoveTo(0x0009, 49500, 500, 52010, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0104, 400)
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrTurnDirection(0x0008, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x00F7, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0270210551V#145F#5P唔～那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210552V#141F刚才的事\n',
            '能说给我听吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210553V#1016F嗯、嗯，好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210554V先回协会说吧，不赶快报告的话\n',
            '感觉要忘了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_779A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210555V#051F#5P赶快回协会\n',
            '去向嘉恩报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77D3')

    def _loc_779A(): pass

    label('loc_779A')

    ChrTalk(
        0x0103,
        (
            '#0030210556V#021F#5P赶快回协会\n',
            '去向嘉恩先生报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_77D3(): pass

    label('loc_77D3')

    CreateThread(0x0101, 0x01, 0x00, func_22_7AF1)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_22_7AF1)
    Sleep(500)

    CreateThread(0x0008, 0x01, 0x00, func_22_7AF1)
    Sleep(500)

    OP_69(0x0104, 2000)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    ChrClearFlags(0x0104, 0x0002)
    ChrSetChipByIndex(0x0104, 65535)
    ChrSetSubChip(0x0104, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040210557V#033F哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210558V我说，艾丝蒂尔。\n',
            '打算去哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0104, 41700, -2890, 52060, 2000, 0x00)
    ChrTurnDirection(0x0104, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040210559V#036F#5P等、等一下！\n',
            '不，请等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280210560V#151F#6P哇哇，表情真好～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210561V好可爱哟～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    FadeOut(1500, 0, -1)
    OP_0D()
    ChrSetStatus(ChrTable['奥利维尔'], 0x00, 41)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['幻影'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['纤维护铠'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['金属靴'], 0xFF)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['ＥＰ２'], 0x00)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['范围'], 0x01)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['命中１'], 0x02)
    EquipCmd(ChrTable['奥利维尔'], ItemTable['防御１'], 0x03)
    AddCraft(ChrTable['奥利维尔'], 0x0000)
    AddCraft(ChrTable['奥利维尔'], CraftTable['连锁战技１(２人协力)'])
    OP_BB(0x03, 0x06, 0x000000F5)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2120._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0021 offset: 0x79DB
@scena.Code('func_21_79DB')
def func_21_79DB():
    LoadEffect(0x01, 'map\\\\mp013_00.eff')
    LoadEffect(0x02, 'map\\\\mp013_02.eff')
    PlayEffect(0x01, 0x01, 0x0033, 0, -100, 2000, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_7A3E')
    def lambda_7A3E():
        ChrMoveTo(0x00FE, 40500, -2800, 51990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7A3E)

    Sleep(2000)

    @scena.Lambda('lambda_7A5E')
    def lambda_7A5E():
        ChrMoveTo(0x00FE, 40500, -2800, 51990, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7A5E)

    Sleep(1200)

    @scena.Lambda('lambda_7A7E')
    def lambda_7A7E():
        ChrMoveTo(0x00FE, 40500, -2800, 51990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7A7E)

    Sleep(500)

    @scena.Lambda('lambda_7A9E')
    def lambda_7A9E():
        ChrMoveTo(0x00FE, 40500, -2800, 51990, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7A9E)

    WaitForThreadExit(0x0033, 0x0001)
    StopEffect(0x01, 0x02)
    PlayEffect(0x02, 0xFF, 0x0033, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0022 offset: 0x7AF1
@scena.Code('func_22_7AF1')
def func_22_7AF1():
    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, 51000, 0, 66220, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0023 offset: 0x7B12
@scena.Code('func_23_7B12')
def func_23_7B12():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 51000, 0, 39000, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0024 offset: 0x7B33
@scena.Code('func_24_7B33')
def func_24_7B33():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7B44',
    )

    Call(0, 0x0035)

    def _loc_7B44(): pass

    label('loc_7B44')

    EventBegin(0x00)
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    ChrClearFlags(0x0127, 0x0080)
    ChrSetFlags(0x0127, 0x0040)
    ChrSetFlags(0x0104, 0x0008)
    ChrSetPos(0x0101, 45070, 500, 91500, 180)
    ChrSetPos(0x00F7, 45070, 500, 91500, 180)
    ChrSetPos(0x0127, 45070, 500, 91500, 180)
    ChrSetPos(0x0104, 45070, 500, 91500, 180)
    CameraMove(45200, 0, 86800, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()
    OP_6F(0x0005, 0)
    OP_70(0x0005, 29)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, func_25_839B)
    CreateThread(0x00F7, 0x01, 0x00, func_26_83B7)
    CreateThread(0x0127, 0x01, 0x00, func_27_83EC)
    CreateThread(0x0104, 0x01, 0x00, func_28_8421)
    Sleep(3800)

    OP_72(0x0005, 0x0800)
    OP_6F(0x0005, 29)
    OP_70(0x0005, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    WaitForThreadExit(0x0104, 0x0001)
    OP_71(0x0005, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010210726V#1007F#6P……怎么说呢～\n',
            '事到如今再叹气也没什么意义了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210727V#1011F奥利维尔你果然跟来了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210728V#031F#2P哈哈哈。\n',
            '真讨厌，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210729V这不是和鸟在天空飞，鱼在水中游\n',
            '一样理所当然的事吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210730V#030F你以为我是为了什么才肯舍弃那美妙的温泉，\n',
            '从亚尔摩来到这里的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8049',
    )

    ChrTalk(
        0x0101,
        (
            '#0010210731V#1015F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210732V对了，阿加特。\n',
            '可以让他加入吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210733V#551F#1P随他便了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210734V#552F不过，我可还没有\n',
            '完全信任你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210735V如果做出奇怪的举动，\n',
            '别怪我不客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210736V#034F#2P呼，那真遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210737V本来觉得像你这样\n',
            '粗旷豪放的类型也不错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210738V#055F#1P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210739V#037F#2P呼，放心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210740V在争取到你的信赖之前\n',
            '我会控制追求的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210741V#055F#1P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050210742V#054F#1P#3S白痴！\n',
            '说什么乱七八糟的！！？？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0127, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0127,
        (
            '#0280210743V#153F#6P啊哇哇～成熟的魅力\n',
            '让人心跳不已呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210744V#1007F#6P（暂时把教训他的任务\n',
            '交给阿加特好了……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_837C')

    def _loc_8049(): pass

    label('loc_8049')

    ChrTalk(
        0x0101,
        (
            '#0010210731V#1015F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210746V对了，雪拉姐。\n',
            '可以让他加入吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210747V#026F#1P唔，你来帮忙\n',
            '说实话很感谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210748V#027F能不能问一件事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210749V你现在还在利贝尔这事\n',
            '卡西乌斯老师知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210750V#1004F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210751V#033F#2P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210752V#035F哎呀哎呀，不愧是雪拉。\n',
            '问的问题一刀见血啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210753V#030F回答是Ｙｅｓ。\n',
            '卡西乌斯先生知道哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210754V这样能接受了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210755V#1015F#6P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210756V#021F#1P呵呵，好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210757V#027F既然想帮忙\n',
            '我们也不客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210758V如果敢乱来\n',
            '就要你陪我一晚上哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210759V#034F#2P我一定诚心诚意、努力奋斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0127, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0127,
        (
            '#0280210760V#151F#6P啊哇哇～成熟的魅力\n',
            '让人心跳不已呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210761V#1016F#6P（不愧是雪拉姐……\n',
            '很会使唤奥利维尔。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_837C(): pass

    label('loc_837C')

    OP_28(0x0082, 0x01, 0x1000)
    OP_28(0x0082, 0x01, 0x2000)
    OP_28(0x0083, 0x04, 0x02)
    OP_28(0x0083, 0x04, 0x08)
    OP_28(0x0083, 0x01, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0025 offset: 0x839B
@scena.Code('func_25_839B')
def func_25_839B():
    ChrWalkTo(0x00FE, 45440, 0, 84720, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0026 offset: 0x83B7
@scena.Code('func_26_83B7')
def func_26_83B7():
    Sleep(1000)

    ChrWalkTo(0x00FE, 45110, 0, 87580, 2000, 0x00)
    ChrWalkTo(0x00FE, 44480, 0, 85840, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0027 offset: 0x83EC
@scena.Code('func_27_83EC')
def func_27_83EC():
    Sleep(1800)

    ChrWalkTo(0x00FE, 45110, 0, 87580, 2000, 0x00)
    ChrWalkTo(0x00FE, 46070, 0, 85580, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0028 offset: 0x8421
@scena.Code('func_28_8421')
def func_28_8421():
    Sleep(3000)

    ChrClearFlags(0x0104, 0x0008)
    ChrWalkTo(0x00FE, 45140, 0, 87630, 2000, 0x00)

    Return()

# id: 0x0029 offset: 0x8440
@scena.Code('func_29_8440')
def func_29_8440():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_84FF',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_849D',
    )

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210564V#050F……没空出去了。\n',
            '赶紧去伦格兰德大桥吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E4')

    def _loc_849D(): pass

    label('loc_849D')

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210565V#020F……没空出去了呢。\n',
            '赶紧去伦格兰德大桥吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84E4(): pass

    label('loc_84E4')

    ChrMoveToRelative(0x0000, 0, 0, -2000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_84FF(): pass

    label('loc_84FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 0, 0x1210)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8834',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 6, 0x120E)),
            Expr.Return,
        ),
        'loc_8697',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_85D6',
    )

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200962V#050F还没找贝尔夫那家伙\n',
            '问亡灵的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200963V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200965V#1006F是市长官邸右边的房子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8694')

    def _loc_85D6(): pass

    label('loc_85D6')

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200966V#020F还没找叫贝尔夫的孩子\n',
            '问白影的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200967V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200965V#1006F是市长官邸右边的房子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8694(): pass

    label('loc_8694')

    Jump('loc_8819')

    def _loc_8697(): pass

    label('loc_8697')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_875D',
    )

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200970V#050F还没找渡鸦帮那些小子\n',
            '问亡灵的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200963V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200973V#1006F要先去港口的仓库才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8819')

    def _loc_875D(): pass

    label('loc_875D')

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200974V#020F还没找渡鸦帮的小子们\n',
            '问白影的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200967V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200973V#1006F要先去港口的仓库才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8819(): pass

    label('loc_8819')

    ChrMoveToRelative(0x0000, 0, 0, -2000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_8834(): pass

    label('loc_8834')

    Return()

# id: 0x002A offset: 0x8835
@scena.Code('func_2A_8835')
def func_2A_8835():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_88DE',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8888',
    )

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210562V#050F没空绕道了。\n',
            '赶紧去桥那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88C3')

    def _loc_8888(): pass

    label('loc_8888')

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210563V#020F没空绕道了。\n',
            '赶紧去桥那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_88C3(): pass

    label('loc_88C3')

    ChrMoveToRelative(0x0000, -2000, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_88DE(): pass

    label('loc_88DE')

    Return()

# id: 0x002B offset: 0x88DF
@scena.Code('func_2B_88DF')
def func_2B_88DF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_88F0',
    )

    Call(0, 0x0035)

    def _loc_88F0(): pass

    label('loc_88F0')

    EventBegin(0x00)
    CameraMove(44890, 0, 88850, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 44960, 0, 92120, 180)
    ChrSetPos(0x00F7, 44960, 0, 93120, 180)
    ChrSetPos(0x0105, 44960, 0, 94120, 180)
    ChrSetPos(0x0104, 44960, 0, 95120, 180)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(1500, 0)
    OP_0D()
    OP_6F(0x0005, 0)
    OP_70(0x0005, 29)
    OP_73(0x0005)
    Sleep(500)

    @scena.Lambda('lambda_89D4')
    def lambda_89D4():
        ChrMoveToRelative(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_89D4)

    Sleep(100)

    @scena.Lambda('lambda_89F4')
    def lambda_89F4():
        ChrMoveToRelative(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_89F4)

    Sleep(100)

    @scena.Lambda('lambda_8A14')
    def lambda_8A14():
        ChrMoveToRelative(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_8A14)

    @scena.Lambda('lambda_8A2F')
    def lambda_8A2F():
        CameraMove(44470, 0, 84530, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8A2F)

    Sleep(200)

    @scena.Lambda('lambda_8A4C')
    def lambda_8A4C():
        ChrMoveToRelative(0x00FE, 0, 0, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_8A4C)

    Sleep(2700)

    OP_72(0x0005, 0x0800)
    OP_6F(0x0005, 29)
    OP_70(0x0005, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0001)
    OP_71(0x0005, 0x0800)

    @scena.Lambda('lambda_8A91')
    def lambda_8A91():
        ChrMoveToRelative(0x00FE, 0, 0, -1200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8A91)

    @scena.Lambda('lambda_8AAC')
    def lambda_8AAC():
        ChrMoveToRelative(0x00FE, -1000, 0, -1500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_8AAC)

    @scena.Lambda('lambda_8AC7')
    def lambda_8AC7():
        ChrMoveToRelative(0x00FE, 1000, 0, -2500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_8AC7)

    @scena.Lambda('lambda_8AE2')
    def lambda_8AE2():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_8AE2)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_8B02')
    def lambda_8B02():
        ChrSetDirection(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8B02)

    WaitForThreadExit(0x00F7, 0x0001)
    ChrSetDirection(0x00F7, 90, 400)
    WaitForThreadExit(0x0105, 0x0001)
    ChrSetDirection(0x0105, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220056V#1006F#6P好了……\n',
            '要出发去蔡斯地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220057V准备结束后\n',
            '就去飞船坪吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8BDA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220058V#051F#5P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220059V如果没有其他事\n',
            '最好马上出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C29')

    def _loc_8BDA(): pass

    label('loc_8BDA')

    ChrTalk(
        0x0103,
        (
            '#0030220060V#020F#5P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220061V如果没有其他事\n',
            '最好马上出发呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C29(): pass

    label('loc_8C29')

    ChrTalk(
        0x0104,
        (
            '#0040220062V#033F这么说来朵洛希小姐\n',
            '在那之后，去了哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220063V好像不知不觉\n',
            '就不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220064V#1011F#6P啊，好像去酒店\n',
            '找奈尔了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220065V如果要离开卢安\n',
            '最好还是去打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220066V#041F呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220067V#542F可以的话还想和院长他们\n',
            '打个招呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220068V可惜之前联络过，似乎有要事\n',
            '和孩子们一起出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220069V#1015F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220070V#1007F嗯～其实我也想\n',
            '临走前看看他们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8E51',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220071V#051F#5P嗯，到蔡斯\n',
            '再写信吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220072V实在不行也没事的，\n',
            '反正很快就会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EBD')

    def _loc_8E51(): pass

    label('loc_8E51')

    ChrTalk(
        0x0103,
        (
            '#0030220073V#021F#5P嗯，到了蔡斯\n',
            '再写信不就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220074V实在不行也没事的，\n',
            '反正很快就会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8EBD(): pass

    label('loc_8EBD')

    ChrTalk(
        0x0105,
        (
            '#0060220075V#041F好，就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220076V#1001F#6P我也一起写吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220077V#035F呼……\n',
            '那么出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220078V#030F去导力技术的殿堂，\n',
            '全王国智慧集聚于一地的工房都市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0280, 0, 0x1400))
    EventEnd(0x00)

    Return()

# id: 0x002C offset: 0x8F81
@scena.Code('func_2C_8F81')
def func_2C_8F81():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    MapClearFlags(0x00000010)
    OP_6F(0x0011, 1500)
    ChrSetPos(0x0010, 51560, 0, 69340, 180)
    ChrSetPos(0x0014, 50310, 0, 70350, 180)
    ChrSetPos(0x0015, 51050, 0, 71430, 180)
    ChrSetPos(0x002C, 51850, 0, 73410, 180)
    ChrSetPos(0x0012, 51850, 1050, 80560, 180)
    ChrSetPos(0x0016, 59910, 0, 81770, 270)
    ChrSetPos(0x0013, 39190, 0, 82810, 90)
    ChrSetPos(0x0018, 37700, 0, 82310, 90)
    OP_4A(0x002C, 255)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    CameraMove(52150, 0, 68780, 0)
    OP_67(0, 8740, -10000, 0)
    CameraSetDistance(4730, 0)
    OP_6C(139000, 0)
    OP_6E(343, 0)
    CreateThread(0x0012, 0x01, 0x00, func_2D_9150)
    CreateThread(0x0016, 0x01, 0x00, func_2E_9165)
    CreateThread(0x0013, 0x01, 0x00, func_2F_918E)
    CreateThread(0x0018, 0x01, 0x00, func_30_91B7)
    OP_C8(0x0200, 0x0046, 'C_PLAC04._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_90DF')
    def lambda_90DF():
        CameraMove(51840, 0, 52250, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_90DF)

    @scena.Lambda('lambda_90F7')
    def lambda_90F7():
        OP_67(0, 7140, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_90F7)

    @scena.Lambda('lambda_910F')
    def lambda_910F():
        CameraSetDistance(4970, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_910F)

    @scena.Lambda('lambda_911F')
    def lambda_911F():
        OP_6C(113000, 7000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_911F)

    OP_6E(431, 7000)
    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T3101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002D offset: 0x9150
@scena.Code('func_2D_9150')
def func_2D_9150():
    ChrWalkTo(0x00FE, 51860, 0, 75750, 4000, 0x00)

    Return()

# id: 0x002E offset: 0x9165
@scena.Code('func_2E_9165')
def func_2E_9165():
    ChrWalkTo(0x00FE, 52600, 0, 81760, 4000, 0x00)
    ChrWalkTo(0x00FE, 52600, 0, 72240, 4000, 0x00)

    Return()

# id: 0x002F offset: 0x918E
@scena.Code('func_2F_918E')
def func_2F_918E():
    ChrWalkTo(0x00FE, 49600, 0, 80420, 4000, 0x00)
    ChrWalkTo(0x00FE, 49600, 0, 72870, 4000, 0x00)

    Return()

# id: 0x0030 offset: 0x91B7
@scena.Code('func_30_91B7')
def func_30_91B7():
    ChrWalkTo(0x00FE, 49600, 0, 80420, 4000, 0x00)
    ChrWalkTo(0x00FE, 50050, 0, 74430, 4000, 0x00)

    Return()

# id: 0x0031 offset: 0x91E0
@scena.Code('func_31_91E0')
def func_31_91E0():
    ChrSetPos(0x0010, 1310, -2250, 94760, 270)
    ChrSetPos(0x0011, 1960, -2250, 94550, 270)
    ChrSetPos(0x0012, 2700, -2250, 94650, 270)
    ChrSetPos(0x0013, 3410, -2250, 94720, 270)
    ChrSetPos(0x0014, 4130, -2250, 94610, 270)
    ChrSetPos(0x0016, 4450, -2250, 95100, 180)
    ChrSetPos(0x0017, 4460, -2250, 95780, 180)
    ChrSetPos(0x0018, 4470, -2250, 96560, 180)
    ChrSetPos(0x0019, 5090, -2250, 96860, 225)
    ChrSetPos(0x0023, 5880, -2250, 96840, 225)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    CreateThread(0x0010, 0x00, 0x00, func_02_E90)
    CreateThread(0x0011, 0x00, 0x00, func_02_E90)
    CreateThread(0x0012, 0x00, 0x00, func_02_E90)
    CreateThread(0x0013, 0x00, 0x00, func_02_E90)
    CreateThread(0x0014, 0x00, 0x00, func_02_E90)
    CreateThread(0x0015, 0x00, 0x00, func_02_E90)
    CreateThread(0x0016, 0x00, 0x00, func_02_E90)
    CreateThread(0x0017, 0x00, 0x00, func_02_E90)
    CreateThread(0x0018, 0x00, 0x00, func_02_E90)
    CreateThread(0x0019, 0x00, 0x00, func_02_E90)
    CreateThread(0x0023, 0x00, 0x00, func_02_E90)

    Return()

# id: 0x0032 offset: 0x930A
@scena.Code('func_32_930A')
def func_32_930A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_932B',
    )

    Call(0, 0x0035)
    Call(0, 0x0036)

    def _loc_932B(): pass

    label('loc_932B')

    SetScenaFlags(ScenaFlag(0x0406, 5, 0x2035))
    ChrSetPos(0x0101, 6140, -2250, 93480, 270)
    ChrSetPos(0x0102, 6120, -2250, 92390, 270)
    ChrSetPos(0x00F8, 7260, -2250, 93700, 270)
    ChrSetPos(0x00F9, 7310, -2250, 92540, 270)
    ChrSetPos(0x0010, 1310, -2250, 94760, 270)
    ChrSetPos(0x0011, 1960, -2250, 94550, 270)
    ChrSetPos(0x0012, 2700, -2250, 94650, 270)
    ChrSetPos(0x0013, 3410, -2250, 94720, 270)
    ChrSetPos(0x0014, 4130, -2250, 94610, 270)
    ChrSetPos(0x0016, 4450, -2250, 95100, 180)
    ChrSetPos(0x0017, 4460, -2250, 95780, 180)
    ChrSetPos(0x0018, 4470, -2250, 96560, 180)
    ChrSetPos(0x0019, 5090, -2250, 96860, 225)
    ChrSetPos(0x0023, 5880, -2250, 96840, 225)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    CameraMove(2810, -2250, 93730, 0)
    OP_67(0, 6250, -10000, 0)
    CameraSetDistance(2460, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    FadeIn(1000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_95A1',
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
        0,
        (
            TXT(0x00, '【◇绕道去嘉恩那里(修好了卢安支部的通讯器)】\n'),
            TXT(0x01, '【◇不绕道(没修好卢安支部的通讯器)】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9542'),
        (0x00000001, 'loc_9548'),
        (-1, 'loc_954E'),
    )

    def _loc_9542(): pass

    label('loc_9542')

    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))

    Jump('loc_954E')

    def _loc_9548(): pass

    label('loc_9548')

    ClearScenaFlags(ScenaFlag(0x0400, 1, 0x2001))

    Jump('loc_954E')

    def _loc_954E(): pass

    label('loc_954E')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Return,
        ),
        'loc_9569',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_9569(): pass

    label('loc_9569')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Return,
        ),
        'loc_957A',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_957A(): pass

    label('loc_957A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Return,
        ),
        'loc_958B',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_958B(): pass

    label('loc_958B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_959E',
    )

    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))

    Jump('loc_95A1')

    def _loc_959E(): pass

    label('loc_959E')

    ClearScenaFlags(ScenaFlag(0x0412, 1, 0x2091))

    def _loc_95A1(): pass

    label('loc_95A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9881',
    )

    CameraMove(7470, -2250, 94090, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010360183V#1004F#5P这、这怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360184V#1042F#2P好混乱啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0023, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_9629')
    def lambda_9629():
        CameraMove(7160, -2250, 96060, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9629)

    ChrTurnDirection(0x0023, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0023,
        (
            '#3860360185V#5P怎么，你们也要\n',
            '前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_967D')
    def lambda_967D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_967D)

    Sleep(100)

    @scena.Lambda('lambda_9690')
    def lambda_9690():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_9690)

    Sleep(100)

    @scena.Lambda('lambda_96A3')
    def lambda_96A3():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_96A3)

    Sleep(100)

    ChrSetDirection(0x00F9, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360186V#1004F#6P啊……怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#3860360187V#5P怎么回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360188V伦格兰德大桥吊起来\n',
            '不动了知道吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360189V因为这个，要去对面\n',
            '只能乘小船了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360190V而这里就是渡口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360191V#1007F#6P这、这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360192V#1043F#4P那……\n',
            '还是很不方便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#3860360193V#5P不方便当然不方便。\n',
            '说实话，真是受不了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360194V虽然由于新市长的安排\n',
            '坐船是免费的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360195V尽管如此，光是排队\n',
            '就要等上３０分钟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A7D')

    def _loc_9881(): pass

    label('loc_9881')

    CameraMove(7470, -2250, 94090, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010360196V#1004F#5P这个，难道就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360197V#1042F#2P嘉恩先生说的\n',
            '小船渡口呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0023, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_9910')
    def lambda_9910():
        CameraMove(7160, -2250, 96060, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9910)

    ChrTurnDirection(0x0023, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0023,
        (
            '#3860360185V#5P怎么，你们也要\n',
            '前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9964')
    def lambda_9964():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9964)

    Sleep(100)

    @scena.Lambda('lambda_9977')
    def lambda_9977():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_9977)

    Sleep(100)

    @scena.Lambda('lambda_998A')
    def lambda_998A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_998A)

    Sleep(100)

    ChrSetDirection(0x00F9, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360199V#1025F#6P啊，嗯。\n',
            '虽然有这打算……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360200V需要花钱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#3860360201V#5P不，由于新市长的安排\n',
            '坐船是免费的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360202V尽管如此，光是排队\n',
            '就要等上３０分钟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360203V说实话，真是受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A7D(): pass

    label('loc_9A7D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9ABF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070360204V#065F#4P呜哎～……\n',
            '要那么久吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9B32')

    def _loc_9ABF(): pass

    label('loc_9ABF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9AFA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360205V#025F#4P那可够久的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9B32')

    def _loc_9AFA(): pass

    label('loc_9AFA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B32',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360206V#052F#4P那可够久的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9B32(): pass

    label('loc_9B32')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B8E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360207V#074F#4P不过，因为是往返航程，\n',
            '需要这么长时间也没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C43')

    def _loc_9B8E(): pass

    label('loc_9B8E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9BEA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360208V#053F#4P不过，因为是往返航程，\n',
            '需要这么长时间也没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C43')

    def _loc_9BEA(): pass

    label('loc_9BEA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C43',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360209V#025F#4P不过，因为是往返航程，\n',
            '需要这么长时间也没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C43(): pass

    label('loc_9C43')

    CameraMove(7470, -2250, 94090, 1500)

    ChrTalk(
        0x0102,
        (
            '#0020360210V#1042F#4P怎么办、艾丝蒂尔。\n',
            '我们也前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9C9A')
    def lambda_9C9A():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_9C9A)

    Sleep(100)

    @scena.Lambda('lambda_9CAD')
    def lambda_9CAD():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_9CAD)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360211V#1015F#5P唔、嗯～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【前往南街区】\n'),
            TXT(0x01, '【先不过去】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9DE4',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360212V#1025F#5P不，先不去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360213V做完手上的事之后\n',
            '再去对面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360214V#1040F#4P知道了。\n',
            '那么回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x10000000)
    NewScene('ED6_DT21/T2132._SN', 108, 0, 0)
    IdleLoop()

    def _loc_9DE4(): pass

    label('loc_9DE4')

    SetScenaFlags(ScenaFlag(0x0406, 6, 0x2036))

    ChrTalk(
        0x0101,
        (
            '#0010360215V#1007F#5P……没法子。\n',
            '似乎也没其他的办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360216V#1040F#4P知道了。\n',
            '那么排队吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(5640, -2250, 96310, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(116000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0014, 1310, -2250, 94760, 270)
    ChrSetPos(0x0016, 1960, -2250, 94550, 270)
    ChrSetPos(0x0017, 2700, -2250, 94650, 270)
    ChrSetPos(0x0018, 3410, -2250, 94720, 270)
    ChrSetPos(0x0019, 4130, -2250, 94610, 270)
    ChrSetPos(0x0023, 4450, -2250, 95100, 180)
    ChrSetPos(0x0101, 4460, -2250, 95780, 180)
    ChrSetPos(0x0102, 4470, -2250, 96560, 180)
    ChrSetPos(0x00F8, 5090, -2250, 96860, 225)
    ChrSetPos(0x00F9, 5880, -2250, 96840, 225)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(4070, -2250, 95380, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0017, 1310, -2250, 94760, 270)
    ChrSetPos(0x0018, 1960, -2250, 94550, 270)
    ChrSetPos(0x0019, 2700, -2250, 94650, 270)
    ChrSetPos(0x0023, 3410, -2250, 94720, 270)
    ChrSetPos(0x0101, 4130, -2250, 94610, 270)
    ChrSetPos(0x0102, 4450, -2250, 95100, 180)
    ChrSetPos(0x00F8, 4460, -2250, 95780, 180)
    ChrSetPos(0x00F9, 4470, -2250, 96560, 180)
    ChrSetPos(0x0013, 5090, -2250, 96860, 225)
    ChrSetPos(0x0012, 5880, -2250, 96840, 225)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(2540, -2250, 94610, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 1310, -2250, 94760, 270)
    ChrSetPos(0x0102, 1960, -2250, 94550, 270)
    ChrSetPos(0x00F8, 2700, -2250, 94650, 270)
    ChrSetPos(0x00F9, 3410, -2250, 94720, 270)
    ChrSetPos(0x0013, 4130, -2250, 94610, 270)
    ChrSetPos(0x0012, 4450, -2250, 95100, 180)
    ChrSetPos(0x0016, 4460, -2250, 95780, 180)
    ChrSetPos(0x0010, 4470, -2250, 96560, 180)
    ChrSetPos(0x0015, 5090, -2250, 96860, 225)
    ChrSetPos(0x0019, 5880, -2250, 96840, 225)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(-600, -2250, 94270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    LoadEffect(0x01, 'map\\\\mp013_02.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -1050, -3100, 92700, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0020, 0x0004)
    OP_72(0x0020, 0x0004)
    OP_72(0x0020, 0x0002)
    OP_71(0x0020, 0x0400)
    OP_71(0x0020, 0x0040)
    OP_71(0x0020, 0x0020)
    OP_B0(0x0020, 0x1E)
    OP_6F(0x0020, 1)
    OP_70(0x0020, 240)
    OP_72(0x0020, 0x0004)
    OP_A1(0x0033, 0x0020)
    ChrSetPos(0x0033, -810, -2850, 92590, 0)
    ChrSetDirection(0x0033, 90, 0)
    OP_4A(0x002D, 255)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetFlags(0x002D, 0x0040)
    ChrSetBattleFlags(0x002D, 0x0020)
    OP_89(0x002D, 400, -3000, 93100, 0)
    Yield()
    ChrSetPos(0x0101, -650, -2250, 94360, 180)
    ChrSetPos(0x0102, 280, -2250, 94270, 180)
    ChrSetPos(0x00F8, -50, -2250, 95350, 180)
    ChrSetPos(0x00F9, 1040, -2250, 95340, 180)
    ChrSetPos(0x0013, 2700, -2250, 94650, 270)
    ChrSetPos(0x0012, 3410, -2250, 94720, 270)
    ChrSetPos(0x0016, 4130, -2250, 94610, 270)
    ChrSetPos(0x0010, 4450, -2250, 95100, 180)
    ChrSetPos(0x0015, 4460, -2250, 95780, 180)
    ChrSetPos(0x0019, 4470, -2250, 96560, 180)
    CameraMove(40, -2250, 94620, 0)
    OP_67(0, 5220, -10000, 0)
    CameraSetDistance(2270, 0)
    OP_6C(9000, 0)
    OP_6E(390, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_DC()

    ChrTalk(
        0x002D,
        (
            '#1520360217V#6P久等了。\n',
            '轮到你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1520360218V赶快上小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360219V#1006F#5P啊，嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360220V#1040F#5P麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    StopEffect(0x01, 0x02)
    FadeOut(1000, 0, -1)
    OP_0D()
    PlaySE(460, 0x00, 0x64)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2101._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0033 offset: 0xA468
@scena.Code('func_33_A468')
def func_33_A468():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A489',
    )

    Call(0, 0x0035)
    Call(0, 0x0036)

    def _loc_A489(): pass

    label('loc_A489')

    ChrSetPos(0x0101, 6140, -2250, 93480, 270)
    ChrSetPos(0x0102, 6120, -2250, 92390, 270)
    ChrSetPos(0x00F8, 7260, -2250, 93700, 270)
    ChrSetPos(0x00F9, 7310, -2250, 92540, 270)
    ChrSetPos(0x0010, 1310, -2250, 94760, 270)
    ChrSetPos(0x0011, 1960, -2250, 94550, 270)
    ChrSetPos(0x0012, 2700, -2250, 94650, 270)
    ChrSetPos(0x0013, 3410, -2250, 94720, 270)
    ChrSetPos(0x0014, 4130, -2250, 94610, 270)
    ChrSetPos(0x0016, 4450, -2250, 95100, 180)
    ChrSetPos(0x0017, 4460, -2250, 95780, 180)
    ChrSetPos(0x0018, 4470, -2250, 96560, 180)
    ChrSetPos(0x0019, 5090, -2250, 96860, 225)
    ChrSetPos(0x0023, 5880, -2250, 96840, 225)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    CameraMove(7470, -2250, 94090, 0)
    OP_67(0, 6250, -10000, 0)
    CameraSetDistance(2460, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A666',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020360210V#1042F#4P怎么办、艾丝蒂尔。\n',
            '我们也前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360260V#1015F#5P唔、嗯～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A666(): pass

    label('loc_A666')

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
        0,
        (
            TXT(0x00, '【前往南街区】\n'),
            TXT(0x01, '【先不过去】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A771',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A758',
    )

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360212V#1025F#5P不，先不去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360213V做完手上的事之后\n',
            '再去对面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360214V#1040F#4P知道了。\n',
            '那么回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A758(): pass

    label('loc_A758')

    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x10000000)
    NewScene('ED6_DT21/T2132._SN', 108, 0, 0)
    IdleLoop()

    def _loc_A771(): pass

    label('loc_A771')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A7EC',
    )

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360215V#1007F#5P……没法子。\n',
            '似乎也没其他的办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360216V#1040F#4P知道了。\n',
            '那么排队吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A7EC(): pass

    label('loc_A7EC')

    OP_DB()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(5640, -2250, 96310, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(116000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0014, 1310, -2250, 94760, 270)
    ChrSetPos(0x0016, 1960, -2250, 94550, 270)
    ChrSetPos(0x0017, 2700, -2250, 94650, 270)
    ChrSetPos(0x0018, 3410, -2250, 94720, 270)
    ChrSetPos(0x0019, 4130, -2250, 94610, 270)
    ChrSetPos(0x0023, 4450, -2250, 95100, 180)
    ChrSetPos(0x0101, 4460, -2250, 95780, 180)
    ChrSetPos(0x0102, 4470, -2250, 96560, 180)
    ChrSetPos(0x00F8, 5090, -2250, 96860, 225)
    ChrSetPos(0x00F9, 5880, -2250, 96840, 225)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(4070, -2250, 95380, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0017, 1310, -2250, 94760, 270)
    ChrSetPos(0x0018, 1960, -2250, 94550, 270)
    ChrSetPos(0x0019, 2700, -2250, 94650, 270)
    ChrSetPos(0x0023, 3410, -2250, 94720, 270)
    ChrSetPos(0x0101, 4130, -2250, 94610, 270)
    ChrSetPos(0x0102, 4450, -2250, 95100, 180)
    ChrSetPos(0x00F8, 4460, -2250, 95780, 180)
    ChrSetPos(0x00F9, 4470, -2250, 96560, 180)
    ChrSetPos(0x0013, 5090, -2250, 96860, 225)
    ChrSetPos(0x0012, 5880, -2250, 96840, 225)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(2540, -2250, 94610, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 1310, -2250, 94760, 270)
    ChrSetPos(0x0102, 1960, -2250, 94550, 270)
    ChrSetPos(0x00F8, 2700, -2250, 94650, 270)
    ChrSetPos(0x00F9, 3410, -2250, 94720, 270)
    ChrSetPos(0x0013, 4130, -2250, 94610, 270)
    ChrSetPos(0x0012, 4450, -2250, 95100, 180)
    ChrSetPos(0x0016, 4460, -2250, 95780, 180)
    ChrSetPos(0x0010, 4470, -2250, 96560, 180)
    ChrSetPos(0x0015, 5090, -2250, 96860, 225)
    ChrSetPos(0x0019, 5880, -2250, 96840, 225)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(-600, -2250, 94270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    LoadEffect(0x01, 'map\\\\mp013_02.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -1050, -3100, 92700, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0020, 0x0004)
    OP_72(0x0020, 0x0004)
    OP_72(0x0020, 0x0002)
    OP_71(0x0020, 0x0400)
    OP_71(0x0020, 0x0040)
    OP_71(0x0020, 0x0020)
    OP_B0(0x0020, 0x1E)
    OP_6F(0x0020, 1)
    OP_70(0x0020, 240)
    OP_72(0x0020, 0x0004)
    OP_A1(0x0033, 0x0020)
    ChrSetPos(0x0033, -810, -2850, 92590, 0)
    ChrSetDirection(0x0033, 90, 0)
    OP_4A(0x002D, 255)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetFlags(0x002D, 0x0040)
    ChrSetBattleFlags(0x002D, 0x0020)
    OP_89(0x002D, 400, -3000, 93100, 0)
    Yield()
    ChrSetPos(0x0101, -650, -2250, 94360, 180)
    ChrSetPos(0x0102, 280, -2250, 94270, 180)
    ChrSetPos(0x00F8, -50, -2250, 95350, 180)
    ChrSetPos(0x00F9, 1040, -2250, 95340, 180)
    ChrSetPos(0x0013, 2700, -2250, 94650, 270)
    ChrSetPos(0x0012, 3410, -2250, 94720, 270)
    ChrSetPos(0x0016, 4130, -2250, 94610, 270)
    ChrSetPos(0x0010, 4450, -2250, 95100, 180)
    ChrSetPos(0x0015, 4460, -2250, 95780, 180)
    ChrSetPos(0x0019, 4470, -2250, 96560, 180)
    CameraMove(40, -2250, 94620, 0)
    OP_67(0, 5220, -10000, 0)
    CameraSetDistance(2270, 0)
    OP_6C(9000, 0)
    OP_6E(390, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_DC()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ADEA',
    )

    SetScenaFlags(ScenaFlag(0x0406, 6, 0x2036))

    ChrTalk(
        0x002D,
        (
            '#1520360217V#6P久等了。\n',
            '轮到你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1520360218V赶快上小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360219V#1006F#5P啊，嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360220V#1040F#5P麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE36')

    def _loc_ADEA(): pass

    label('loc_ADEA')

    ChrTalk(
        0x002D,
        (
            '#1520360270V#6P好，轮到你们了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1520360271V后面很挤\n',
            '赶快上小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE36(): pass

    label('loc_AE36')

    StopEffect(0x01, 0x02)
    FadeOut(1000, 0, -1)
    OP_0D()
    PlaySE(460, 0x00, 0x64)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2101._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0034 offset: 0xAE5B
@scena.Code('func_34_AE5B')
def func_34_AE5B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AE7D',
    )

    Call(0, 0x0035)
    Call(0, 0x0036)

    def _loc_AE7D(): pass

    label('loc_AE7D')

    LoadChip('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP', 35)
    LoadChip('ED6_DT27/CH03013._CH', 'ED6_DT27/CH03013P._CP', 36)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_AEAA'),
        (0x00000005, 'loc_AEB7'),
        (0x00000006, 'loc_AEC4'),
        (0x00000007, 'loc_AED1'),
        (-1, 'loc_AEDE'),
    )

    def _loc_AEAA(): pass

    label('loc_AEAA')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 37)

    Jump('loc_AEDE')

    def _loc_AEB7(): pass

    label('loc_AEB7')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 37)

    Jump('loc_AEDE')

    def _loc_AEC4(): pass

    label('loc_AEC4')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 37)

    Jump('loc_AEDE')

    def _loc_AED1(): pass

    label('loc_AED1')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 37)

    Jump('loc_AEDE')

    def _loc_AEDE(): pass

    label('loc_AEDE')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_AEF7'),
        (0x00000005, 'loc_AF04'),
        (0x00000006, 'loc_AF11'),
        (0x00000007, 'loc_AF1E'),
        (-1, 'loc_AF2B'),
    )

    def _loc_AEF7(): pass

    label('loc_AEF7')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 38)

    Jump('loc_AF2B')

    def _loc_AF04(): pass

    label('loc_AF04')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 38)

    Jump('loc_AF2B')

    def _loc_AF11(): pass

    label('loc_AF11')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 38)

    Jump('loc_AF2B')

    def _loc_AF1E(): pass

    label('loc_AF1E')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 38)

    Jump('loc_AF2B')

    def _loc_AF2B(): pass

    label('loc_AF2B')

    ChrSetChipByIndex(0x0101, 35)
    ChrSetChipByIndex(0x0102, 36)
    ChrSetChipByIndex(0x00F8, 37)
    ChrSetChipByIndex(0x00F9, 38)
    ChrSetPos(0x0010, 1310, -2250, 94760, 270)
    ChrSetPos(0x0011, 1960, -2250, 94550, 270)
    ChrSetPos(0x0012, 2700, -2250, 94650, 270)
    ChrSetPos(0x0013, 3410, -2250, 94720, 270)
    ChrSetPos(0x0014, 4130, -2250, 94610, 270)
    ChrSetPos(0x0016, 4450, -2250, 95100, 180)
    ChrSetPos(0x0017, 4460, -2250, 95780, 180)
    ChrSetPos(0x0018, 4470, -2250, 96560, 180)
    ChrSetPos(0x0019, 5090, -2250, 96860, 225)
    ChrSetPos(0x0023, 5880, -2250, 96840, 225)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    OP_4A(0x002D, 255)
    LoadEffect(0x00, 'map\\\\mp013_00.eff')
    PlayEffect(0x00, 0x00, 0x0033, 0, -150, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0020, 0x0004)
    OP_71(0x0020, 0x0002)
    OP_71(0x0020, 0x0040)
    OP_71(0x0020, 0x0020)
    OP_B0(0x0020, 0x1E)
    OP_6F(0x0020, 1)
    OP_70(0x0020, 240)
    OP_72(0x0020, 0x0004)
    OP_A1(0x0033, 0x0020)
    ChrSetPos(0x0033, -15000, -2850, 92590, 90)
    ChrSetBattleFlags(0x002D, 0x0020)
    ChrSetBattleFlags(0x0101, 0x0020)
    ChrSetBattleFlags(0x0102, 0x0020)
    ChrSetBattleFlags(0x00F8, 0x0020)
    ChrSetBattleFlags(0x00F9, 0x0020)
    Yield()
    ChrSetDirection(0x0033, 90, 0)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002D, 0x0001)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    ChrClearFlags(0x002D, 0x0001)
    ChrSetFlags(0x002D, 0x0020)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetFlags(0x00F8, 0x0020)
    ChrSetFlags(0x00F9, 0x0020)
    ChrSetFlags(0x002D, 0x0040)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x00F8, 0x0040)
    ChrSetFlags(0x00F9, 0x0040)
    Yield()
    ChrSetDirection(0x0033, 270, 0)
    OP_89(0x0101, -14050, -2800, 92360, 90)
    OP_89(0x0102, -14050, -2800, 93000, 90)
    OP_89(0x00F8, -15400, -2800, 93000, 90)
    OP_89(0x00F9, -15400, -2800, 92360, 90)
    OP_89(0x002D, -16100, -3000, 92200, 180)
    CameraMove(-2540, -2820, 92800, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_B1C9')
    def lambda_B1C9():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B1C9')

    DispatchAsync2(0x0023, 0x0001, lambda_B1C9)

    @scena.Lambda('lambda_B1DA')
    def lambda_B1DA():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B1DA')

    DispatchAsync2(0x0010, 0x0001, lambda_B1DA)

    @scena.Lambda('lambda_B1EB')
    def lambda_B1EB():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B1EB')

    DispatchAsync2(0x0011, 0x0001, lambda_B1EB)

    @scena.Lambda('lambda_B1FC')
    def lambda_B1FC():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B1FC')

    DispatchAsync2(0x0012, 0x0001, lambda_B1FC)

    @scena.Lambda('lambda_B20D')
    def lambda_B20D():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B20D')

    DispatchAsync2(0x0013, 0x0001, lambda_B20D)

    @scena.Lambda('lambda_B21E')
    def lambda_B21E():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B21E')

    DispatchAsync2(0x0014, 0x0001, lambda_B21E)

    @scena.Lambda('lambda_B22F')
    def lambda_B22F():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B22F')

    DispatchAsync2(0x0016, 0x0001, lambda_B22F)

    @scena.Lambda('lambda_B240')
    def lambda_B240():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B240')

    DispatchAsync2(0x0017, 0x0001, lambda_B240)

    @scena.Lambda('lambda_B251')
    def lambda_B251():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B251')

    DispatchAsync2(0x0018, 0x0001, lambda_B251)

    @scena.Lambda('lambda_B262')
    def lambda_B262():
        ChrTurnDirection(0x00FE, 0x0033, 400)
        Yield()

        Jump('lambda_B262')

    DispatchAsync2(0x0019, 0x0001, lambda_B262)

    @scena.Lambda('lambda_B273')
    def lambda_B273():
        ChrMoveTo(0x00FE, -800, -2850, 92590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_B273)

    @scena.Lambda('lambda_B28E')
    def lambda_B28E():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_B28E)

    @scena.Lambda('lambda_B2A9')
    def lambda_B2A9():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B2A9)

    @scena.Lambda('lambda_B2C4')
    def lambda_B2C4():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B2C4)

    @scena.Lambda('lambda_B2DF')
    def lambda_B2DF():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_B2DF)

    @scena.Lambda('lambda_B2FA')
    def lambda_B2FA():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_B2FA)

    Sleep(2000)

    @scena.Lambda('lambda_B31A')
    def lambda_B31A():
        CameraMove(200, -2250, 92990, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_B31A)

    Sleep(4000)

    @scena.Lambda('lambda_B337')
    def lambda_B337():
        ChrMoveTo(0x00FE, -810, -2850, 92590, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_B337)

    @scena.Lambda('lambda_B352')
    def lambda_B352():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_B352)

    @scena.Lambda('lambda_B36D')
    def lambda_B36D():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B36D)

    @scena.Lambda('lambda_B388')
    def lambda_B388():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B388)

    @scena.Lambda('lambda_B3A3')
    def lambda_B3A3():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_B3A3)

    @scena.Lambda('lambda_B3BE')
    def lambda_B3BE():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_B3BE)

    Sleep(2000)

    @scena.Lambda('lambda_B3DE')
    def lambda_B3DE():
        ChrMoveTo(0x00FE, -810, -2850, 92590, 750, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_B3DE)

    @scena.Lambda('lambda_B3F9')
    def lambda_B3F9():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_B3F9)

    @scena.Lambda('lambda_B414')
    def lambda_B414():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B414)

    @scena.Lambda('lambda_B42F')
    def lambda_B42F():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B42F)

    @scena.Lambda('lambda_B44A')
    def lambda_B44A():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_B44A)

    @scena.Lambda('lambda_B465')
    def lambda_B465():
        ChrMoveToRelativeAsync(0x00FE, 15800, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_B465)

    WaitForThreadExit(0x0033, 0x0001)
    TerminateThread(0x002D, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    StopEffect(0x00, 0x02)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x0101, 0x0001)
    ChrSetFlags(0x0102, 0x0001)
    ChrSetFlags(0x00F8, 0x0001)
    ChrSetFlags(0x00F9, 0x0001)
    OP_DC()
    MapClearFlags(0x10000000)
    NewScene('ED6_DT21/T2132._SN', 108, 0, 0)
    IdleLoop()

    Return()

# id: 0x0035 offset: 0xB4C5
@scena.Code('func_35_B4C5')
def func_35_B4C5():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_B53F'),
        (0x00000001, 'loc_B545'),
        (-1, 'loc_B54B'),
    )

    def _loc_B53F(): pass

    label('loc_B53F')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_B54B')

    def _loc_B545(): pass

    label('loc_B545')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_B54B')

    def _loc_B54B(): pass

    label('loc_B54B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B559',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_B55D')

    def _loc_B559(): pass

    label('loc_B559')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_B55D(): pass

    label('loc_B55D')

    Return()

# id: 0x0036 offset: 0xB55E
@scena.Code('func_36_B55E')
def func_36_B55E():
    MapClearFlags(0x00000001)
    CameraMove(-11050, -2250, 166960, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0037 offset: 0xB5B7
@scena.Code('func_37_B5B7')
def func_37_B5B7():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　    卢安市长选举\n',
            '※投票日请务必\n',
            '　要去投票所\n',
            '　　　　　选举管理委员会',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0038 offset: 0xB631
@scena.Code('func_38_B631')
def func_38_B631():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B669')
    def lambda_B669():
        CameraMove(15010, -1800, 111900, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_B669)

    @scena.Lambda('lambda_B681')
    def lambda_B681():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_B681)

    @scena.Lambda('lambda_B691')
    def lambda_B691():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_B691)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B718',
    )

    OP_C0(0x0E, 0x00000019, 0x00003F7A, 0xFFFFF8F8, 0x0001B5E4, 0x0000010E, 0x00003610, 0xFFFFF510, 0x0001B602)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_B727')

    def _loc_B718(): pass

    label('loc_B718')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B727',
    )

    EventEnd(0x01)

    def _loc_B727(): pass

    label('loc_B727')

    Return()

# id: 0x0039 offset: 0xB728
@scena.Code('func_39_B728')
def func_39_B728():
    OP_13(0x0048)

    Return()

# id: 0x003A offset: 0xB72C
@scena.Code('func_3A_B72C')
def func_3A_B72C():
    OP_13(0x004D)

    Return()

# id: 0x003B offset: 0xB730
@scena.Code('func_3B_B730')
def func_3B_B730():
    OP_13(0x004C)

    Return()

# id: 0x003C offset: 0xB734
@scena.Code('func_3C_B734')
def func_3C_B734():
    OP_13(0x004A)

    Return()

# id: 0x003D offset: 0xB738
@scena.Code('func_3D_B738')
def func_3D_B738():
    OP_13(0x004E)

    Return()

# id: 0x003E offset: 0xB73C
@scena.Code('func_3E_B73C')
def func_3E_B73C():
    OP_13(0x004B)

    Return()

# id: 0x003F offset: 0xB740
@scena.Code('func_3F_B740')
def func_3F_B740():
    OP_13(0x0049)

    Return()

# id: 0x0040 offset: 0xB744
@scena.Code('func_40_B744')
def func_40_B744():
    OP_13(0x004F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
