import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4104   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4104.x'
    header.mapIndex       = 1
    header.bgm            = 18
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T4104._SN', 'ED6_DT01/T4104_1._SN', 'ED6_DT01/T4104_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT06/CH20123._CH', 'ED6_DT06/CH20123P._CP'),
        ('ED6_DT06/CH20124._CH', 'ED6_DT06/CH20124P._CP'),
        ('ED6_DT06/CH20125._CH', 'ED6_DT06/CH20125P._CP'),
        ('ED6_DT06/CH20126._CH', 'ED6_DT06/CH20126P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT06/CH20088._CH', 'ED6_DT06/CH20088P._CP'),
    ]

# id: 0x10001 offset: 0x1B2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '金',
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
            name                = '卡露娜',
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
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
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
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            name                = '库拉茨',
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
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            name                = '克鲁茨',
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
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002E,
        ),
        ScenaNpcData(
            name                = '空贼',
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
            name                = '多伦',
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
            name                = '吉尔',
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
            name                = '乔丝特',
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
            name                = '不良青年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '迪恩',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '雷斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '洛克',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '莱尔中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '贝伦中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '迪鲁队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '洛伦斯少尉',
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
            name                = '管家菲利普',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '杜南公爵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亚鲁瓦教授',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            name                = '裁判',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '不良青年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '不良青年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '不良青年',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
        ScenaNpcData(
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '芭蒂',
            x                   = -12680,
            z                   = 4700,
            y                   = -4790,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            name                = '拉尔夫',
            x                   = -12660,
            z                   = 4700,
            y                   = -3750,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            name                = '蒂库',
            x                   = -14750,
            z                   = 5200,
            y                   = 3290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131099,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            name                = '拉尔斯',
            x                   = -14750,
            z                   = 5200,
            y                   = 3960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65564,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            name                = '托伊',
            x                   = -14750,
            z                   = 5200,
            y                   = 4700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196634,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 393244,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14740,
            z                   = 5200,
            y                   = -13430,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15730,
            z                   = 5450,
            y                   = -5010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = 3270,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15820,
            z                   = 5450,
            y                   = -9240,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15850,
            z                   = 5450,
            y                   = 1890,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = -6590,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12680,
            z                   = 4700,
            y                   = -17670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14720,
            z                   = 5200,
            y                   = -3720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458778,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = 1670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13710,
            z                   = 4950,
            y                   = -13580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14750,
            z                   = 5200,
            y                   = -8060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14720,
            z                   = 5200,
            y                   = 510,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12660,
            z                   = 4700,
            y                   = -9280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13750,
            z                   = 4950,
            y                   = 4710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13770,
            z                   = 4950,
            y                   = -6540,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196636,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14850,
            z                   = 5200,
            y                   = -15970,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = -13490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327708,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15610,
            z                   = 5450,
            y                   = -17700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15900,
            z                   = 5450,
            y                   = -14800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16640,
            z                   = 5700,
            y                   = -13560,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13720,
            z                   = 4950,
            y                   = -9500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13810,
            z                   = 4950,
            y                   = -4800,
            direction           = 91,
            word_0E             = 0,
            dword_10            = 196635,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14870,
            z                   = 5200,
            y                   = -4980,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15810,
            z                   = 5450,
            y                   = -6530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327706,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15850,
            z                   = 5450,
            y                   = 3270,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = 520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13720,
            z                   = 4950,
            y                   = 3330,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14730,
            z                   = 5200,
            y                   = 1860,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13780,
            z                   = 4950,
            y                   = -8039,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458779,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15680,
            z                   = 5450,
            y                   = 550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12660,
            z                   = 4700,
            y                   = 4760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13930,
            z                   = 4950,
            y                   = -3700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16620,
            z                   = 5700,
            y                   = -3710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15860,
            z                   = 5450,
            y                   = 4750,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196636,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12730,
            z                   = 4700,
            y                   = -8010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131100,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16720,
            z                   = 5700,
            y                   = -13930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13800,
            z                   = 4950,
            y                   = -14740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327708,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14800,
            z                   = 5200,
            y                   = -14740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15640,
            z                   = 5450,
            y                   = -15910,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15790,
            z                   = 5450,
            y                   = -13450,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16820,
            z                   = 5700,
            y                   = -17670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16710,
            z                   = 5700,
            y                   = -16280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196635,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16710,
            z                   = 5700,
            y                   = -14840,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15840,
            z                   = 5450,
            y                   = -16740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327706,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14720,
            z                   = 5200,
            y                   = -16740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14860,
            z                   = 5200,
            y                   = -14050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12700,
            z                   = 4700,
            y                   = -14100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14670,
            z                   = 5200,
            y                   = -9220,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15900,
            z                   = 5450,
            y                   = -7990,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458779,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14820,
            z                   = 5200,
            y                   = -6520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15740,
            z                   = 5450,
            y                   = -3710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14700,
            z                   = 5200,
            y                   = -7290,
            direction           = 90,
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
            name                = '观众',
            x                   = -13790,
            z                   = 4950,
            y                   = -5620,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16740,
            z                   = 5700,
            y                   = -5620,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196636,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16690,
            z                   = 5700,
            y                   = -8690,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131100,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15800,
            z                   = 5450,
            y                   = -5790,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = -5670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = -7390,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458778,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14700,
            z                   = 5200,
            y                   = -4400,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -16690,
            z                   = 5700,
            y                   = -7210,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13760,
            z                   = 4950,
            y                   = -8770,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13760,
            z                   = 4950,
            y                   = 530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13760,
            z                   = 4950,
            y                   = 1760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15870,
            z                   = 5450,
            y                   = 1130,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -13900,
            z                   = 4950,
            y                   = 2470,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12680,
            z                   = 4700,
            y                   = 4050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -15780,
            z                   = 5450,
            y                   = 4019,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -14710,
            z                   = 5200,
            y                   = 2590,
            direction           = 90,
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
            name                = '观众',
            x                   = -12650,
            z                   = 4950,
            y                   = 1110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -12650,
            z                   = 4700,
            y                   = 2550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 14670,
            z                   = 4700,
            y                   = 1910,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 14660,
            z                   = 4700,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 327708,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 15770,
            z                   = 4950,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 16860,
            z                   = 5200,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 17850,
            z                   = 5450,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 18800,
            z                   = 5700,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 15910,
            z                   = 4950,
            y                   = 1830,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 196635,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 16760,
            z                   = 5200,
            y                   = 1830,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 17780,
            z                   = 5450,
            y                   = 1990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 327706,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1092
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1092
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1092
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1092
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 6, 0x3FE)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 7, 0x3FF)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 0, 0x3F0)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 1, 0x3F1)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 2, 0x3F2)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 3, 0x3F3)),
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1224',
    )

    ChrClearFlags(0x0053, 0x0080)
    ChrClearFlags(0x0054, 0x0080)
    ChrClearFlags(0x0055, 0x0080)
    ChrClearFlags(0x0056, 0x0080)
    ChrClearFlags(0x0057, 0x0080)
    ChrClearFlags(0x0058, 0x0080)
    ChrClearFlags(0x0059, 0x0080)
    ChrClearFlags(0x005A, 0x0080)
    ChrClearFlags(0x005B, 0x0080)
    ChrClearFlags(0x005C, 0x0080)
    ChrClearFlags(0x005D, 0x0080)
    ChrClearFlags(0x005E, 0x0080)
    ChrClearFlags(0x005F, 0x0080)
    ChrClearFlags(0x0060, 0x0080)
    ChrClearFlags(0x0061, 0x0080)
    ChrClearFlags(0x0062, 0x0080)
    ChrClearFlags(0x0063, 0x0080)
    ChrClearFlags(0x0064, 0x0080)
    ChrClearFlags(0x0065, 0x0080)
    ChrClearFlags(0x0066, 0x0080)
    ChrClearFlags(0x0067, 0x0080)
    ChrClearFlags(0x0068, 0x0080)
    ChrClearFlags(0x0069, 0x0080)
    ChrClearFlags(0x006A, 0x0080)
    ChrClearFlags(0x006B, 0x0080)
    ChrClearFlags(0x006C, 0x0080)
    ChrClearFlags(0x006D, 0x0080)
    ChrClearFlags(0x006E, 0x0080)
    ChrClearFlags(0x006F, 0x0080)
    ChrClearFlags(0x0070, 0x0080)
    ChrClearFlags(0x0071, 0x0080)
    ChrClearFlags(0x0072, 0x0080)
    ChrClearFlags(0x0073, 0x0080)
    ChrClearFlags(0x0074, 0x0080)
    ChrClearFlags(0x0075, 0x0080)
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
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrClearFlags(0x004E, 0x0080)
    ChrClearFlags(0x004F, 0x0080)
    ChrClearFlags(0x0050, 0x0080)
    ChrClearFlags(0x0051, 0x0080)
    ChrClearFlags(0x0052, 0x0080)

    def _loc_1224(): pass

    label('loc_1224')

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0015, 17290, 9500, -4880, 270)
    ChrSetPos(0x0016, 17290, 9500, -8150, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_125E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_03_3E30)

    def _loc_125E(): pass

    label('loc_125E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_126C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_04_4421)

    def _loc_126C(): pass

    label('loc_126C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_127A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_05_45F0)

    def _loc_127A(): pass

    label('loc_127A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_1288',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_07_56FB)

    def _loc_1288(): pass

    label('loc_1288')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 6, 0x3FE)),
            Expr.Return,
        ),
        'loc_1296',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    Event(0, func_08_5AF0)

    def _loc_1296(): pass

    label('loc_1296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 7, 0x3FF)),
            Expr.Return,
        ),
        'loc_12A4',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    Event(0, func_09_60DA)

    def _loc_12A4(): pass

    label('loc_12A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 0, 0x3F0)),
            Expr.Return,
        ),
        'loc_12B2',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    Event(0, func_0A_6697)

    def _loc_12B2(): pass

    label('loc_12B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 1, 0x3F1)),
            Expr.Return,
        ),
        'loc_12C0',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))
    Event(0, func_0C_7397)

    def _loc_12C0(): pass

    label('loc_12C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 2, 0x3F2)),
            Expr.Return,
        ),
        'loc_12CE',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 2, 0x3F2))
    Event(0, func_0D_7D80)

    def _loc_12CE(): pass

    label('loc_12CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 3, 0x3F3)),
            Expr.Return,
        ),
        'loc_12DC',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 3, 0x3F3))
    Event(0, func_0E_83D1)

    def _loc_12DC(): pass

    label('loc_12DC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_12F0'),
        (0x00000064, 'loc_12F0'),
        (0x00000067, 'loc_1306'),
        (-1, 'loc_1342'),
    )

    def _loc_12F0(): pass

    label('loc_12F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 6, 0x60E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1303',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 6, 0x60E))
    Event(0, func_02_155A)

    def _loc_1303(): pass

    label('loc_1303')

    Jump('loc_1342')

    def _loc_1306(): pass

    label('loc_1306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 6, 0x636)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1319',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 7, 0x637))
    Event(0, func_0F_8631)

    def _loc_1319(): pass

    label('loc_1319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_132C',
    )

    SetScenaFlags(ScenaFlag(0x00C3, 6, 0x61E))
    Event(0, func_06_4BB2)

    def _loc_132C(): pass

    label('loc_132C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 5, 0x625)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_133F',
    )

    SetScenaFlags(ScenaFlag(0x00C4, 6, 0x626))
    Event(0, func_0B_6788)

    def _loc_133F(): pass

    label('loc_133F')

    Jump('loc_1342')

    def _loc_1342(): pass

    label('loc_1342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 0, 0x638)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13D2',
    )

    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0022, -17490, 5950, -9620, 90)
    ChrSetPos(0x0023, -10510, 4200, -6570, 90)
    ChrSetPos(0x0009, -12660, 4700, -16340, 90)
    ChrSetPos(0x000A, -12670, 4700, -15020, 90)
    ChrSetPos(0x000B, -13760, 4950, -17160, 90)
    ChrSetPos(0x000C, -14580, 5200, -17680, 90)

    def _loc_13D2(): pass

    label('loc_13D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_13DC',
    )

    Jump('loc_154E')

    def _loc_13DC(): pass

    label('loc_13DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_13E6',
    )

    Jump('loc_154E')

    def _loc_13E6(): pass

    label('loc_13E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_13F0',
    )

    Jump('loc_154E')

    def _loc_13F0(): pass

    label('loc_13F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_13FA',
    )

    Jump('loc_154E')

    def _loc_13FA(): pass

    label('loc_13FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_149E',
    )

    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 5, 0x635)),
            Expr.Return,
        ),
        'loc_1437',
    )

    ChrClearFlags(0x002F, 0x0080)
    ChrSetPos(0x002F, -14380, 5200, 4380, 98)

    def _loc_1437(): pass

    label('loc_1437')

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
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrClearFlags(0x004E, 0x0080)
    ChrClearFlags(0x004F, 0x0080)
    ChrClearFlags(0x0050, 0x0080)
    ChrClearFlags(0x0051, 0x0080)
    ChrClearFlags(0x0052, 0x0080)

    Jump('loc_154E')

    def _loc_149E(): pass

    label('loc_149E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_14A8',
    )

    Jump('loc_154E')

    def _loc_14A8(): pass

    label('loc_14A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_14FA',
    )

    ChrClearFlags(0x002A, 0x0080)
    ChrSetPos(0x002A, -14850, 5200, 4019, 90)
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

    Jump('loc_154E')

    def _loc_14FA(): pass

    label('loc_14FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1504',
    )

    Jump('loc_154E')

    def _loc_1504(): pass

    label('loc_1504')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_153D',
    )

    ChrClearFlags(0x002A, 0x0080)
    ChrSetPos(0x002A, -12690, 4700, -4810, 90)
    ChrClearFlags(0x0030, 0x0080)
    ChrClearFlags(0x0031, 0x0080)
    ChrClearFlags(0x0032, 0x0080)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)

    Jump('loc_154E')

    def _loc_153D(): pass

    label('loc_153D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1547',
    )

    Jump('loc_154E')

    def _loc_1547(): pass

    label('loc_1547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_154E',
    )

    def _loc_154E(): pass

    label('loc_154E')

    Return()

# id: 0x0001 offset: 0x154F
@scena.Code('func_01_154F')
def func_01_154F():
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)

    Return()

# id: 0x0002 offset: 0x155A
@scena.Code('func_02_155A')
def func_02_155A():
    ChrClearFlags(0x0053, 0x0080)
    ChrClearFlags(0x0054, 0x0080)
    ChrClearFlags(0x0055, 0x0080)
    ChrClearFlags(0x0056, 0x0080)
    ChrClearFlags(0x0057, 0x0080)
    ChrClearFlags(0x0058, 0x0080)
    ChrClearFlags(0x0059, 0x0080)
    ChrClearFlags(0x005A, 0x0080)
    ChrClearFlags(0x005B, 0x0080)
    ChrClearFlags(0x005C, 0x0080)
    ChrClearFlags(0x005D, 0x0080)
    ChrClearFlags(0x005E, 0x0080)
    ChrClearFlags(0x005F, 0x0080)
    ChrClearFlags(0x0060, 0x0080)
    ChrClearFlags(0x0061, 0x0080)
    ChrClearFlags(0x0062, 0x0080)
    ChrClearFlags(0x0063, 0x0080)
    ChrClearFlags(0x0064, 0x0080)
    ChrClearFlags(0x0065, 0x0080)
    ChrClearFlags(0x0066, 0x0080)
    ChrClearFlags(0x0067, 0x0080)
    ChrClearFlags(0x0068, 0x0080)
    ChrClearFlags(0x0069, 0x0080)
    ChrClearFlags(0x006A, 0x0080)
    ChrClearFlags(0x006B, 0x0080)
    ChrClearFlags(0x006C, 0x0080)
    ChrClearFlags(0x006D, 0x0080)
    ChrClearFlags(0x006E, 0x0080)
    ChrClearFlags(0x006F, 0x0080)
    ChrClearFlags(0x0070, 0x0080)
    ChrClearFlags(0x0071, 0x0080)
    ChrClearFlags(0x0072, 0x0080)
    ChrClearFlags(0x0073, 0x0080)
    ChrClearFlags(0x0074, 0x0080)
    ChrClearFlags(0x0075, 0x0080)
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
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrClearFlags(0x004E, 0x0080)
    ChrClearFlags(0x004F, 0x0080)
    ChrClearFlags(0x0050, 0x0080)
    ChrClearFlags(0x0051, 0x0080)
    ChrClearFlags(0x0052, 0x0080)
    ChrSetPos(0x0053, -13710, 4950, -16760, 90)
    ChrSetPos(0x005D, -12690, 4700, -15820, 90)
    ChrSetPos(0x0035, -14950, 5200, 4040, 90)
    ChrSetPos(0x0068, -12650, 4700, -3710, 90)
    ChrSetPos(0x0069, -16730, 5700, 2520, 90)
    ChrClearFlags(0x0076, 0x0080)
    ChrClearFlags(0x0077, 0x0080)
    ChrClearFlags(0x0078, 0x0080)
    ChrClearFlags(0x0079, 0x0080)
    ChrClearFlags(0x007A, 0x0080)
    ChrClearFlags(0x007B, 0x0080)
    ChrClearFlags(0x007C, 0x0080)
    ChrClearFlags(0x007D, 0x0080)
    ChrClearFlags(0x007E, 0x0080)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetFlags(0x0021, 0x0004)
    ChrSetChipByIndex(0x0021, 32)
    ChrSetPos(0x0021, 13860, 9850, -6510, 270)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x0020, 14630, 9750, -5420, 270)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17A8',
    )

    ChrSetPos(0x0102, -10510, 4200, 5460, 270)
    ChrSetPos(0x0101, -10500, 4200, 4210, 270)

    Jump('loc_17CA')

    def _loc_17A8(): pass

    label('loc_17A8')

    ChrSetPos(0x0101, -10510, 4200, -16790, 270)
    ChrSetPos(0x0102, -10510, 4200, -17970, 270)

    def _loc_17CA(): pass

    label('loc_17CA')

    CameraMove(12190, 5450, -6580, 0)
    OP_67(0, 5170, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(180000, 0)
    OP_6E(441, 0)
    OP_66(0x0000)

    @scena.Lambda('lambda_1810')
    def lambda_1810():
        CameraMove(-4240, 7800, 50, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1810)

    Sleep(6000)

    Fade(1000)
    OP_66(0x0001)
    Yield()

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1859',
    )

    CameraMove(-10980, 4200, 5030, 0)
    OP_6C(315000, 0)

    Jump('loc_1873')

    def _loc_1859(): pass

    label('loc_1859')

    CameraMove(-10520, 4200, -17340, 0)
    OP_6C(224000, 0)

    def _loc_1873(): pass

    label('loc_1873')

    OP_67(0, 6050, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010100898V#004F哇……\n',
            '这么多人啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100899V#010F嗯……大家的热情很高啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100900V预选赛都有这么多人来看，\n',
            '这个大会的规模可想而知了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_193D')
    def lambda_193D():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_193D)

    Sleep(200)

    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100901V#006F预选赛，进行到什么阶段了呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100902V',
            (TxtCtl.SetColor, 0x5),
            '让大家久等了。\n',
            '接下来开始第七场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100903V#006F啊……好像开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100904V#010F那么，\n',
            '我们赶快找个空位坐下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetPos(0x0102, -12660, 4700, -6310, 90)
    ChrSetPos(0x0101, -12650, 4700, -7170, 90)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    CameraSetDistance(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0000)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100905V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100906V',
            (TxtCtl.SetColor, 0x5),
            '国境警卫队第２连队所属，\n',
            '帕乌尔少尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetPos(0x0019, 2260, 120, -24190, 0)
    ChrSetPos(0x0015, 1380, 120, -24190, 0)
    ChrSetPos(0x0016, 300, 120, -24190, 0)
    ChrSetPos(0x0017, -560, 120, -24190, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    CameraMove(1200, 0, -21730, 2000)
    OP_70(0x0000, 100)
    OP_73(0x0000)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_1BCD')
    def lambda_1BCD():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1BCD)

    Sleep(300)

    @scena.Lambda('lambda_1BED')
    def lambda_1BED():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1BED)

    Sleep(50)

    @scena.Lambda('lambda_1C0D')
    def lambda_1C0D():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_1C0D)

    Sleep(50)

    @scena.Lambda('lambda_1C2D')
    def lambda_1C2D():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_1C2D)

    CameraMove(1000, 0, -6610, 6000)

    ChrTalk(
        0x0101,
        (
            '#0010100907V#004F咦……\n',
            '比赛不是一对一吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100908V#012F嗯，看起来好像是团体赛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100909V根据我的记忆，\n',
            '应该是个人赛没错啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100910V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100911V',
            (TxtCtl.SetColor, 0x5),
            '游击士协会格兰赛尔支部，\n',
            '克鲁茨选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010100912V#501F啊，是卡露娜姐姐他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100913V#010F差一点就错过了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, 2260, 120, 11000, 180)
    ChrSetPos(0x000A, 1380, 120, 11000, 180)
    ChrSetPos(0x000B, 300, 120, 11000, 180)
    ChrSetPos(0x000C, -560, 120, 11000, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    CameraMove(880, 0, 8980, 2000)
    OP_70(0x0001, 100)
    OP_73(0x0001)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_1E3F')
    def lambda_1E3F():
        ChrWalkTo(0x00FE, 2260, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E3F)

    @scena.Lambda('lambda_1E5A')
    def lambda_1E5A():
        ChrWalkTo(0x00FE, 300, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1E5A)

    Sleep(60)

    @scena.Lambda('lambda_1E7A')
    def lambda_1E7A():
        ChrWalkTo(0x00FE, -560, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1E7A)

    Sleep(100)

    @scena.Lambda('lambda_1E9A')
    def lambda_1E9A():
        ChrWalkTo(0x00FE, 1380, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1E9A)

    CameraMove(1000, 0, -6610, 6000)
    Sleep(500)

    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210100914V马上开始武术大会\n',
            '预选赛第７场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F43')
    def lambda_1F43():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1F43')

    DispatchAsync2(0x0019, 0x0001, lambda_1F43)

    @scena.Lambda('lambda_1F54')
    def lambda_1F54():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1F54')

    DispatchAsync2(0x0017, 0x0001, lambda_1F54)

    @scena.Lambda('lambda_1F65')
    def lambda_1F65():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1F65')

    DispatchAsync2(0x0015, 0x0001, lambda_1F65)

    @scena.Lambda('lambda_1F76')
    def lambda_1F76():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1F76')

    DispatchAsync2(0x0016, 0x0001, lambda_1F76)

    @scena.Lambda('lambda_1F87')
    def lambda_1F87():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_1F87)

    Sleep(200)

    @scena.Lambda('lambda_1FA7')
    def lambda_1FA7():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_1FA7)

    @scena.Lambda('lambda_1FC2')
    def lambda_1FC2():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_1FC2)

    @scena.Lambda('lambda_1FDD')
    def lambda_1FDD():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_1FDD)

    @scena.Lambda('lambda_1FF8')
    def lambda_1FF8():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_1FF8')

    DispatchAsync2(0x000B, 0x0001, lambda_1FF8)

    @scena.Lambda('lambda_2009')
    def lambda_2009():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_2009')

    DispatchAsync2(0x000A, 0x0001, lambda_2009)

    @scena.Lambda('lambda_201A')
    def lambda_201A():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_201A')

    DispatchAsync2(0x0009, 0x0001, lambda_201A)

    @scena.Lambda('lambda_202B')
    def lambda_202B():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_202B')

    DispatchAsync2(0x000C, 0x0001, lambda_202B)

    @scena.Lambda('lambda_203C')
    def lambda_203C():
        ChrWalkTo(0x00FE, 390, 0, -1720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_203C)

    @scena.Lambda('lambda_2057')
    def lambda_2057():
        ChrWalkTo(0x00FE, 1430, 0, -1790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2057)

    @scena.Lambda('lambda_2072')
    def lambda_2072():
        ChrWalkTo(0x00FE, 2260, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2072)

    @scena.Lambda('lambda_208D')
    def lambda_208D():
        ChrWalkTo(0x00FE, -560, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_208D)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0019, 29)
    ChrSetChipByIndex(0x0015, 29)
    ChrSetChipByIndex(0x0016, 29)
    ChrSetChipByIndex(0x0017, 29)
    ChrSetFlags(0x0019, 0x0002)
    ChrSetFlags(0x0015, 0x0002)
    ChrSetFlags(0x0016, 0x0002)
    ChrSetFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x34),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 29)
    ChrSetChipByIndex(0x000A, 29)
    ChrSetChipByIndex(0x0009, 29)
    ChrSetChipByIndex(0x000C, 29)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x000C, 0x0002)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
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

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000C, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BB9, 0x00100002, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    ChrSetPos(0x0019, 670, 0, -8630, 0)
    ChrSetPos(0x0015, 2400, 0, -9100, 0)
    ChrSetPos(0x0016, -120, 0, -9870, 0)
    ChrSetPos(0x0017, -1110, 0, -8890, 0)
    ChrSetPos(0x000B, 1480, 0, -4830, 180)
    ChrSetPos(0x000A, -1050, 0, -4440, 180)
    ChrSetPos(0x0009, 80, 0, -3240, 180)
    ChrSetPos(0x000C, 2650, 0, -3550, 180)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x35),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0019, 0, 0)
    ChrSetDirection(0x0015, 45, 0)
    ChrSetDirection(0x0016, 315, 0)
    ChrSetDirection(0x0017, 45, 0)
    ChrSetPos(0x0102, -12660, 4700, -6310, 90)
    ChrSetPos(0x0101, -12650, 4700, -7170, 90)
    OP_66(0x0000)
    CameraMove(1000, 0, -6610, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(790, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210100918V胜负已分！\n',
            '红之组，克鲁茨小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010100919V#001F太好了～～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100920V卡露娜姐姐他们真厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100921V#010F嗯，真是精彩的比赛啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100922V军队一方虽然打得也不错，\n',
            '但是进攻配合和角色分工方面\n',
            '和游击士组相比还是差了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100923V#006F嗯嗯，\n',
            '可以作为我们战斗的参考呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100924V#506F哎呀，该怎么说呢，\n',
            '我身体里武术家的血液已经沸腾起来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100925V早知道就先不去王城，\n',
            '来这里从头开始看比赛了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100926V#019F哈哈，我很理解你的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100927V不过如果连这个也忍耐不了的话，\n',
            '就没办法成为独当一面的游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100928V#009F哼，\n',
            '反正我只是个半吊子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100929V',
            (TxtCtl.SetColor, 0x5),
            '……接下来\n',
            '要进行的是第八场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100930V',
            (TxtCtl.SetColor, 0x5),
            '这场比赛之后，\n',
            '预选赛就全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    Fade(1000)
    ChrSetPos(0x0102, -12660, 4700, -6310, 90)
    ChrSetPos(0x0101, -12650, 4700, -7170, 90)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    CameraSetDistance(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0000)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100905V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100932V',
            (TxtCtl.SetColor, 0x5),
            '『渡鸦帮』所属，\n',
            '贝尔夫选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetPos(0x0011, 2260, 120, -24190, 0)
    ChrSetPos(0x0025, 1380, 120, -24190, 0)
    ChrSetPos(0x0026, 300, 120, -24190, 0)
    ChrSetPos(0x0027, -560, 120, -24190, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    CameraMove(1200, 0, -21730, 2000)
    OP_70(0x0000, 100)
    OP_73(0x0000)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_2821')
    def lambda_2821():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_2821)

    Sleep(50)

    @scena.Lambda('lambda_2841')
    def lambda_2841():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_2841)

    Sleep(50)

    @scena.Lambda('lambda_2861')
    def lambda_2861():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_2861)

    @scena.Lambda('lambda_287C')
    def lambda_287C():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_287C)

    CameraMove(1000, 0, -6610, 6000)

    ChrTalk(
        0x0101,
        (
            '#0010100933V#005F那、那些家伙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100934V#014F是卢安仓库那些流氓的成员。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100935V原来如此，\n',
            '大会对普通人也是开放的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100936V#007F唉，他们是不是来错地方了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100937V这里聚集的都是战斗和武术的高手，\n',
            '那些家伙们怎么可能打得过嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100910V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100939V',
            (TxtCtl.SetColor, 0x5),
            '来自邻国卡尔瓦德共和国的武术家，\n',
            '金选手单人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010100940V#004F金、金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100941V#014F又是熟人啊……\n',
            '这世界还真是狭小呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100942V#012F不过，只有一个人出场的话，\n',
            '情况会不会有所不利呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100943V#002F就是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100944V就算对手都是小混混，\n',
            '被包围起来也会很难办的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0008, 2260, 120, 11000, 180)
    ChrClearFlags(0x0008, 0x0080)
    CameraMove(880, 0, 8980, 2000)
    OP_70(0x0001, 100)
    OP_73(0x0001)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_2B73')
    def lambda_2B73():
        ChrWalkTo(0x00FE, 850, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2B73)

    CameraMove(1000, 0, -6610, 6000)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100945V',
            (TxtCtl.SetColor, 0x5),
            '这次的预选赛\n',
            '金选手没有任何队友陪同，\n',
            '所以只有他一个人出场应战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100946V',
            (TxtCtl.SetColor, 0x5),
            '虽然条件对他很不利，\n',
            '但根据他本人的强烈要求，\n',
            '主办方同意在这种情况下进行比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100947V',
            (TxtCtl.SetColor, 0x5),
            '特此声明，请大家理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210100948V马上开始武术大会\n',
            '预选赛第八场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2D2F')
    def lambda_2D2F():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2D2F')

    DispatchAsync2(0x0011, 0x0001, lambda_2D2F)

    @scena.Lambda('lambda_2D40')
    def lambda_2D40():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2D40')

    DispatchAsync2(0x0025, 0x0001, lambda_2D40)

    @scena.Lambda('lambda_2D51')
    def lambda_2D51():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2D51')

    DispatchAsync2(0x0026, 0x0001, lambda_2D51)

    @scena.Lambda('lambda_2D62')
    def lambda_2D62():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2D62')

    DispatchAsync2(0x0027, 0x0001, lambda_2D62)

    @scena.Lambda('lambda_2D73')
    def lambda_2D73():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2D73)

    Sleep(200)

    @scena.Lambda('lambda_2D93')
    def lambda_2D93():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_2D93)

    @scena.Lambda('lambda_2DAE')
    def lambda_2DAE():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_2DAE)

    @scena.Lambda('lambda_2DC9')
    def lambda_2DC9():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0002, lambda_2DC9)

    @scena.Lambda('lambda_2DE4')
    def lambda_2DE4():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_2DE4')

    DispatchAsync2(0x0008, 0x0001, lambda_2DE4)

    @scena.Lambda('lambda_2DF5')
    def lambda_2DF5():
        ChrWalkTo(0x00FE, 760, 0, -700, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2DF5)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0011, 29)
    ChrSetChipByIndex(0x0025, 29)
    ChrSetChipByIndex(0x0026, 29)
    ChrSetChipByIndex(0x0027, 29)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetFlags(0x0025, 0x0002)
    ChrSetFlags(0x0026, 0x0002)
    ChrSetFlags(0x0027, 0x0002)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 25)
    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0025, 0xFF)
    TerminateThread(0x0026, 0xFF)
    TerminateThread(0x0027, 0xFF)
    TerminateThread(0x0008, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBA, 0x00100003, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0011, 1870, 0, -9140, 0)
    ChrSetPos(0x0025, -60, 0, -9780, 0)
    ChrSetPos(0x0026, 1090, 0, -10320, 0)
    ChrSetPos(0x0027, 2720, 0, -10150, 0)
    ChrSetPos(0x0008, 1120, 0, -4070, 180)
    ChrSetPos(0x0102, -12660, 4700, -6310, 90)
    ChrSetPos(0x0101, -12650, 4700, -7170, 90)
    OP_66(0x0000)
    CameraMove(1000, 0, -6610, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(790, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210100952V胜负已分！\n',
            '红之组，金选手胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(176, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0008, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010100953V#001F呀嗬～～～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100954V不愧是金先生，完全一边倒嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100955V#019F看起来我们的担心是多余的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100956V虽然那么巨大的身体，\n',
            '但速度却很快，招式也相当厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100957V#010F不过，我觉得到了正式赛的时候，\n',
            '一对四还是会很困难的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100958V#007F嗯，确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200100959V',
            (TxtCtl.SetColor, 0x5),
            '经过刚才的一番竞逐，\n',
            '预选赛已经全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100960V',
            (TxtCtl.SetColor, 0x5),
            '在正式赛里出场的队伍一共八支。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100961V',
            (TxtCtl.SetColor, 0x5),
            '从明天开始连续三天，\n',
            '以淘汰赛的方式决定冠军所属。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100962V',
            (TxtCtl.SetColor, 0x5),
            '那么最后，\n',
            '请大会的主办者杜南公爵发表致词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(7100, 10100, -6310, 0)
    OP_67(0, 4570, -10000, 0)
    CameraSetDistance(1160, 0)
    OP_6C(306000, 0)
    OP_6E(823, 0)
    ChrSetChipByIndex(0x0021, 18)
    ChrSetPos(0x0021, 11990, 9750, -6500, 270)
    ChrSetPos(0x0020, 14000, 9750, -7520, 270)
    OP_0D()

    ChrTalk(
        0x0021,
        (
            '#0640100963V#225F#2P咳咳！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100964V#220F啊～～各位亲爱的市民，\n',
            '今天特意来看比赛，真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100965V很遗憾，因为我忙于政务，\n',
            '错过了今天前半部分的比赛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100966V#221F不过后半部分的比赛都很精彩，\n',
            '我感到非常的满足，特别的兴奋！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(274, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0021,
        (
            '#0640100967V#225F#2P最近接连发生了恐怖事件，\n',
            '陛下龙体欠佳等不好的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100968V#220F不过，请各位放心！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100969V作为陛下托付政务的本人——\n',
            '杜南·冯·奥赛雷丝，\n',
            '粉身碎骨也要不负各位的期待！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100970V希望借助本次武术大会如此活跃的气氛，\n',
            '能够让大家的心情好起来！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100971V#221F敬请期待明天开始的正式赛！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010100972V#509F这、这段话对那个公爵来说，\n',
            '也太过诚恳了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100973V#015F很可能是情报部的人帮他起草的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(7100, 10100, -6310, 0)
    OP_67(0, 4570, -10000, 0)
    CameraSetDistance(1160, 0)
    OP_6C(306000, 0)
    OP_6E(823, 0)
    ChrSetChipByIndex(0x0021, 18)
    ChrSetPos(0x0021, 11990, 9750, -6500, 270)
    OP_0D()

    ChrTalk(
        0x0021,
        (
            '#0640100974V#221F#2P哈、哈、哈……哦，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100975V#220F这次大会的冠军，除了得到奖金以外，\n',
            '我本人还准备了其他丰厚的礼物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0020, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0020, 0x0021, 400)

    ChrTalk(
        0x0020,
        (
            '#0660100976V#721F（公、公爵大人……\n',
            '　这样做真的妥当吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0021, 0x0020, 400)

    ChrTalk(
        0x0021,
        (
            '#0640100977V#222F#5P（真烦人，给我闭嘴。\n',
            '　这是让大家了解我优点的大好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0021, 270, 400)
    ChrSetDirection(0x0020, 270, 400)

    ChrTalk(
        0x0021,
        (
            '#0640100978V#225F#2P这个礼物就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100979V#224F三天后在格兰赛尔城举行的\n',
            '宫廷晚宴的请柬！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(176, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0021,
        (
            '#0640100980V#221F#2P很遗憾虽然陛下无法出席，\n',
            '不过这可是齐集各界名流的高级晚餐会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100981V还可以品尝到只能由王公贵族享用的，\n',
            '称得上为王国最高级的料理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100982V今天胜出的各位选手，\n',
            '为了得到我的请柬也请加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    FadeOut(1500, 0, -1)
    OP_0D()
    ChrTurnDirection(0x0101, 0x0102, 0)
    ChrTurnDirection(0x0102, 0x0101, 0)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6880, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2350, 0)
    OP_6C(134000, 0)
    OP_6E(261, 0)
    OP_23(0x00AE)
    Sleep(3000)

    ChrSetFlags(0x0053, 0x0080)
    ChrSetFlags(0x0054, 0x0080)
    ChrSetFlags(0x0055, 0x0080)
    ChrSetFlags(0x0056, 0x0080)
    ChrSetFlags(0x0057, 0x0080)
    ChrSetFlags(0x0058, 0x0080)
    ChrSetFlags(0x0059, 0x0080)
    ChrSetFlags(0x005A, 0x0080)
    ChrSetFlags(0x005B, 0x0080)
    ChrSetFlags(0x005C, 0x0080)
    ChrSetFlags(0x005D, 0x0080)
    ChrSetFlags(0x005E, 0x0080)
    ChrSetFlags(0x005F, 0x0080)
    ChrSetFlags(0x0060, 0x0080)
    ChrSetFlags(0x0061, 0x0080)
    ChrSetFlags(0x0062, 0x0080)
    ChrSetFlags(0x0063, 0x0080)
    ChrSetFlags(0x0064, 0x0080)
    ChrSetFlags(0x0065, 0x0080)
    ChrSetFlags(0x0066, 0x0080)
    ChrSetFlags(0x0067, 0x0080)
    ChrSetFlags(0x0068, 0x0080)
    ChrSetFlags(0x0069, 0x0080)
    ChrSetFlags(0x006A, 0x0080)
    ChrSetFlags(0x006B, 0x0080)
    ChrSetFlags(0x006C, 0x0080)
    ChrSetFlags(0x006D, 0x0080)
    ChrSetFlags(0x006E, 0x0080)
    ChrSetFlags(0x006F, 0x0080)
    ChrSetFlags(0x0070, 0x0080)
    ChrSetFlags(0x0071, 0x0080)
    ChrSetFlags(0x0072, 0x0080)
    ChrSetFlags(0x0073, 0x0080)
    ChrSetFlags(0x0074, 0x0080)
    ChrSetFlags(0x0075, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0031, 0x0080)
    ChrSetFlags(0x0032, 0x0080)
    ChrSetFlags(0x0033, 0x0080)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0035, 0x0080)
    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    ChrSetFlags(0x0039, 0x0080)
    ChrSetFlags(0x003A, 0x0080)
    ChrSetFlags(0x003B, 0x0080)
    ChrSetFlags(0x003C, 0x0080)
    ChrSetFlags(0x003D, 0x0080)
    ChrSetFlags(0x003E, 0x0080)
    ChrSetFlags(0x003F, 0x0080)
    ChrSetFlags(0x0040, 0x0080)
    ChrSetFlags(0x0041, 0x0080)
    ChrSetFlags(0x0042, 0x0080)
    ChrSetFlags(0x0043, 0x0080)
    ChrSetFlags(0x0044, 0x0080)
    ChrSetFlags(0x0045, 0x0080)
    ChrSetFlags(0x0046, 0x0080)
    ChrSetFlags(0x0047, 0x0080)
    ChrSetFlags(0x0048, 0x0080)
    ChrSetFlags(0x0049, 0x0080)
    ChrSetFlags(0x004A, 0x0080)
    ChrSetFlags(0x004B, 0x0080)
    ChrSetFlags(0x004C, 0x0080)
    ChrSetFlags(0x004D, 0x0080)
    ChrSetFlags(0x004E, 0x0080)
    ChrSetFlags(0x004F, 0x0080)
    ChrSetFlags(0x0050, 0x0080)
    ChrSetFlags(0x0051, 0x0080)
    ChrSetFlags(0x0052, 0x0080)
    ChrSetFlags(0x0076, 0x0080)
    ChrSetFlags(0x0077, 0x0080)
    ChrSetFlags(0x0078, 0x0080)
    ChrSetFlags(0x0079, 0x0080)
    ChrSetFlags(0x007A, 0x0080)
    ChrSetFlags(0x007B, 0x0080)
    ChrSetFlags(0x007C, 0x0080)
    ChrSetFlags(0x007D, 0x0080)
    ChrSetFlags(0x007E, 0x0080)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010100983V#003F喂，约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100984V不如我们去找卡露娜姐姐他们吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100985V#015F嗯，我也是这么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100986V如果他们能够获胜，\n',
            '就可以堂堂正正地进入格兰赛尔城了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100987V借此良机，\n',
            '能把那件事传达给女王也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100988V#010F你是这个意思吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100989V#003F嗯……虽然我不太情愿\n',
            '把博士的委托交给别人去做……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100990V不过这可不是固执的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100991V#010F我没什么意见哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100992V他们可能还没回去，\n',
            '我们去选手休息室看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100993V#000F嗯，好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100994V嗯……刚才卡露娜姐姐他们\n',
            '好像是从北边的大门出去的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100995V#010F嗯，如果在的话，\n',
            '肯定是在北边的休息室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C1, 6, 0x60E))
    SetScenaFlags(ScenaFlag(0x00C1, 7, 0x60F))
    OP_28(0x0045, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x3E30
@scena.Code('func_03_3E30')
def func_03_3E30():
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    ChrSetPos(0x002A, -12650, 4700, -3680, 90)
    ChrSetPos(0x0053, -12650, 4700, -16700, 90)
    ChrSetPos(0x005E, -12650, 4700, -14700, 90)
    ChrSetPos(0x006A, -13730, 4950, -16780, 90)
    ChrSetPos(0x0074, -12660, 4700, -15720, 90)
    ChrSetPos(0x006F, -14780, 5200, 3980, 90)
    ChrSetPos(0x005D, -13830, 4950, -15790, 90)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetRGBAMask(0x0021, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0020, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0004)
    ChrSetFlags(0x0020, 0x0004)
    ChrSetPos(0x0021, 19870, 9500, -6460, 270)
    ChrSetPos(0x0020, 20800, 9500, -5950, 270)
    CameraMove(-9450, 0, -6730, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(500, 0)

    @scena.Lambda('lambda_3F51')
    def lambda_3F51():
        OP_6E(339, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3F51)

    @scena.Lambda('lambda_3F61')
    def lambda_3F61():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3F61)

    @scena.Lambda('lambda_3F71')
    def lambda_3F71():
        CameraMove(13540, 9750, -6540, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3F71)

    FadeIn(2000, 0)
    Sleep(3500)

    ChrSetPos(0x0030, 14650, 4700, 250, 270)
    ChrSetPos(0x0031, 15730, 4950, 250, 270)
    ChrSetPos(0x0032, 16860, 5200, 250, 270)
    ChrSetPos(0x0033, 17850, 5450, 250, 270)
    ChrSetPos(0x0034, 18880, 5700, 250, 270)
    ChrSetPos(0x0035, 19640, 5950, 250, 270)
    ChrSetPos(0x0036, 14650, 4700, 1200, 270)
    ChrSetPos(0x0037, 15730, 4950, 1200, 270)
    ChrSetPos(0x0038, 16860, 5200, 1200, 270)
    ChrSetPos(0x0039, 17850, 5450, 1200, 270)
    ChrSetPos(0x003A, 18880, 5700, 1200, 270)
    ChrSetPos(0x003B, 19640, 5950, 1200, 270)
    ChrSetPos(0x003C, 14650, 4700, 2390, 270)
    ChrSetPos(0x003D, 15730, 4950, 2390, 270)
    ChrSetPos(0x003E, 16860, 5200, 2390, 270)
    ChrSetPos(0x003F, 17850, 5450, 2390, 270)
    ChrSetPos(0x0040, 18880, 5700, 2390, 270)
    ChrSetPos(0x0041, 19640, 5950, 2390, 270)
    ChrSetPos(0x0042, 14650, 4700, 3550, 270)
    ChrSetPos(0x0043, 15730, 4950, 3550, 270)
    ChrSetPos(0x0044, 16860, 5200, 3550, 270)
    ChrSetPos(0x0045, 17850, 5450, 3550, 270)
    ChrSetPos(0x0046, 18880, 5700, 3550, 270)
    ChrSetPos(0x0047, 19640, 5950, 3550, 270)
    ChrSetPos(0x0048, 14650, 4700, 4830, 270)
    ChrSetPos(0x0049, 15730, 4950, 4830, 270)
    ChrSetPos(0x004A, 16860, 5200, 4830, 270)
    ChrSetPos(0x004B, 17850, 5450, 4830, 270)
    ChrSetPos(0x004C, 18880, 5700, 4830, 270)
    ChrSetPos(0x004D, 19640, 5950, 4830, 270)
    ChrSetPos(0x004E, 14650, 4700, -13300, 270)
    ChrSetPos(0x004F, 15730, 4950, -13300, 270)
    ChrSetPos(0x0050, 16860, 5200, -13300, 270)
    ChrSetPos(0x0051, 17850, 5450, -13300, 270)
    ChrSetPos(0x0052, 18880, 5700, -13300, 270)
    ChrSetPos(0x0053, 19640, 5950, -13300, 270)
    ChrSetPos(0x0054, 14650, 4700, -14500, 270)
    ChrSetPos(0x0055, 15730, 4950, -14500, 270)
    ChrSetPos(0x0056, 16860, 5200, -14500, 270)
    ChrSetPos(0x0057, 17850, 5450, -14500, 270)
    ChrSetPos(0x0058, 18880, 5700, -14500, 270)
    ChrSetPos(0x0059, 19640, 5950, -14500, 270)
    ChrSetPos(0x005A, 14650, 4700, -15600, 270)
    ChrSetPos(0x005B, 15730, 4950, -15600, 270)
    ChrSetPos(0x005C, 16860, 5200, -15600, 270)
    ChrSetPos(0x005D, 17850, 5450, -15600, 270)
    ChrSetPos(0x005E, 18880, 5700, -15600, 270)
    ChrSetPos(0x005F, 19640, 5950, -15600, 270)
    ChrSetPos(0x0060, 14650, 4700, -16920, 270)
    ChrSetPos(0x0061, 15730, 4950, -16920, 270)
    ChrSetPos(0x0062, 16860, 5200, -16920, 270)
    ChrSetPos(0x0063, 17850, 5450, -16920, 270)
    ChrSetPos(0x0064, 18880, 5700, -16920, 270)
    ChrSetPos(0x0065, 19640, 5950, -16920, 270)
    ChrSetPos(0x0066, 14650, 4700, -18030, 270)
    ChrSetPos(0x0067, 15730, 4950, -18030, 270)
    ChrSetPos(0x0068, 16860, 5200, -18030, 270)
    ChrSetPos(0x0069, 17850, 5450, -18030, 270)
    ChrSetPos(0x006A, 18880, 5700, -18030, 270)
    ChrSetPos(0x006B, 19640, 5950, -18030, 270)
    Sleep(6000)

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    Sleep(1000)

    @scena.Lambda('lambda_43B0')
    def lambda_43B0():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_43B0)

    @scena.Lambda('lambda_43CB')
    def lambda_43CB():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_43CB)

    @scena.Lambda('lambda_43E6')
    def lambda_43E6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0021, 0x0002, lambda_43E6)

    @scena.Lambda('lambda_43F8')
    def lambda_43F8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_43F8)

    Sleep(500)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x4421
@scena.Code('func_04_4421')
def func_04_4421():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    FormationAddMember(0x01, 0xFF)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    CameraMove(810, 0, -6480, 0)
    OP_67(0, 15230, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(269000, 0)
    OP_6E(96, 0)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, -4240, 0, -6480, 0)

    @scena.Lambda('lambda_448A')
    def lambda_448A():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_448A)

    @scena.Lambda('lambda_449A')
    def lambda_449A():
        OP_6E(524, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_449A)

    @scena.Lambda('lambda_44AA')
    def lambda_44AA():
        OP_67(0, 8010, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_44AA)

    @scena.Lambda('lambda_44C2')
    def lambda_44C2():
        ChrWalkTo(0x00FE, 5940, 0, -6480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_44C2)

    WaitForThreadExit(0x0024, 0x0001)
    ChrSetDirection(0x0024, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110182V',
            (TxtCtl.SetColor, 0x5),
            '那么接下来，\n',
            '我们马上来公布\n',
            '有幸参加揭幕战的小组吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110183V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——\n',
            '游击士协会格兰赛尔支部，\n',
            '克鲁茨选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110184V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——\n',
            '王国军突击骑兵队所属，\n',
            '杰多中尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x45F0
@scena.Code('func_05_45F0')
def func_05_45F0():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0019, 2260, 0, -5460, 180)
    ChrSetPos(0x0015, 300, 0, -5460, 180)
    ChrSetPos(0x0016, -560, 0, -5460, 180)
    ChrSetPos(0x0017, 1380, 0, -5460, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0009, 2260, 0, -7590, 0)
    ChrSetPos(0x000B, 1380, 0, -7590, 0)
    ChrSetPos(0x000C, 300, 0, -7590, 0)
    ChrSetPos(0x000A, -560, 0, -7590, 0)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210110191V马上开始武术大会\n',
            '正式赛第一场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0016, 0x0040)

    @scena.Lambda('lambda_4791')
    def lambda_4791():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_4791')

    DispatchAsync2(0x000B, 0x0001, lambda_4791)

    @scena.Lambda('lambda_47A2')
    def lambda_47A2():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_47A2')

    DispatchAsync2(0x000A, 0x0001, lambda_47A2)

    @scena.Lambda('lambda_47B3')
    def lambda_47B3():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_47B3')

    DispatchAsync2(0x0009, 0x0001, lambda_47B3)

    @scena.Lambda('lambda_47C4')
    def lambda_47C4():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_47C4')

    DispatchAsync2(0x000C, 0x0001, lambda_47C4)

    @scena.Lambda('lambda_47D5')
    def lambda_47D5():
        ChrWalkTo(0x00FE, 2350, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_47D5)

    Sleep(100)

    @scena.Lambda('lambda_47F5')
    def lambda_47F5():
        ChrWalkTo(0x00FE, -170, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_47F5)

    Sleep(200)

    @scena.Lambda('lambda_4815')
    def lambda_4815():
        ChrWalkTo(0x00FE, 1570, 0, -11430, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_4815)

    @scena.Lambda('lambda_4830')
    def lambda_4830():
        ChrWalkTo(0x00FE, 390, 0, -11390, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_4830)

    @scena.Lambda('lambda_484B')
    def lambda_484B():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_484B')

    DispatchAsync2(0x0019, 0x0001, lambda_484B)

    @scena.Lambda('lambda_485C')
    def lambda_485C():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_485C')

    DispatchAsync2(0x0017, 0x0001, lambda_485C)

    @scena.Lambda('lambda_486D')
    def lambda_486D():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_486D')

    DispatchAsync2(0x0015, 0x0001, lambda_486D)

    @scena.Lambda('lambda_487E')
    def lambda_487E():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_487E')

    DispatchAsync2(0x0016, 0x0001, lambda_487E)

    @scena.Lambda('lambda_488F')
    def lambda_488F():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_488F)

    Sleep(200)

    @scena.Lambda('lambda_48AF')
    def lambda_48AF():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_48AF)

    Sleep(100)

    @scena.Lambda('lambda_48CF')
    def lambda_48CF():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_48CF)

    Sleep(200)

    @scena.Lambda('lambda_48EF')
    def lambda_48EF():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_48EF)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0019, 29)
    ChrSetChipByIndex(0x0015, 29)
    ChrSetChipByIndex(0x0016, 29)
    ChrSetChipByIndex(0x0017, 29)
    ChrSetFlags(0x0019, 0x0002)
    ChrSetFlags(0x0015, 0x0002)
    ChrSetFlags(0x0016, 0x0002)
    ChrSetFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x36),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x32),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x32),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x32),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 29)
    ChrSetChipByIndex(0x000A, 29)
    ChrSetChipByIndex(0x0009, 29)
    ChrSetChipByIndex(0x000C, 29)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x000C, 0x0002)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000C, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBB, 0x00100004, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x37),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x33),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x33),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x33),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x000B, 1570, 0, -9320, 0)
    ChrSetPos(0x000A, -10, 0, -9870, 0)
    ChrSetPos(0x0009, 2360, 0, -10500, 0)
    ChrSetPos(0x000C, -1470, 0, -9110, 0)
    ChrSetPos(0x0019, 1690, 0, -4090, 180)
    ChrSetPos(0x0015, 20, 0, -3980, 180)
    ChrSetPos(0x0016, 2390, 0, -2970, 180)
    ChrSetPos(0x0017, -970, 0, -2780, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110195V胜负已分！\n',
            '苍之组，克鲁茨小组获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x4BB2
@scena.Code('func_06_4BB2')
def func_06_4BB2():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    MapSetFlags(0x00100000)
    OP_66(0x0000)
    CameraMove(1450, 0, -21650, 0)
    OP_67(-6800, 5030, -14300, 0)
    CameraSetDistance(1530, 0)
    OP_6C(229000, 0)
    OP_6E(733, 0)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    ChrSetPos(0x0011, 2260, 0, -5460, 180)
    ChrSetPos(0x0013, 300, 0, -5460, 180)
    ChrSetPos(0x0014, -560, 0, -5460, 180)
    ChrSetPos(0x0012, 1380, 0, -5460, 180)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    FadeIn(2000, 0)
    ChrSetPos(0x0108, 2260, 0, -24190, 0)
    ChrSetPos(0x0101, 1380, 0, -24190, 0)
    ChrSetPos(0x0102, 300, 0, -24190, 0)
    ChrSetPos(0x0104, -560, 0, -24190, 0)
    OP_70(0x0000, 100)
    OP_73(0x0000)
    OP_66(0x0000)

    @scena.Lambda('lambda_4CCC')
    def lambda_4CCC():
        CameraMove(1160, 0, -6810, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4CCC)

    Sleep(500)

    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)

    @scena.Lambda('lambda_4CF3')
    def lambda_4CF3():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_4CF3)

    Sleep(300)

    @scena.Lambda('lambda_4D13')
    def lambda_4D13():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_4D13)

    Sleep(50)

    @scena.Lambda('lambda_4D33')
    def lambda_4D33():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4D33)

    Sleep(50)

    @scena.Lambda('lambda_4D53')
    def lambda_4D53():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4D53)

    Sleep(6000)

    OP_66(0x0001)
    Fade(1000)
    CameraMove(1130, 0, -6520, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(3320, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0012,
        (
            '#0450110212V嘿嘿……\n',
            '这么快复仇的机会就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0470110213V偶尔女神也会\n',
            '照顾我们一次嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0460110214V#6P之前发生的事情，\n',
            '让我们认识到自己的力量太弱小了，\n',
            '因此我们进行了地狱般的特训……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0460110215V#6P就让你们看看我们的修炼成果吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110216V#006F哼哼，这种劲头很好嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110217V我们也会拼尽全力，\n',
            '决不会手下留情的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110218V#031F#2P（呵呵，艾丝蒂尔今天怎么这么来劲呢，\n',
            '　真是难得一见哦。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110219V（该说她是假小子呢还是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110220V#017F（这句话被艾丝蒂尔听见的话，\n',
            '　你肯定又会挨打的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110221V#070F#2P那么，也差不多该开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210110222V马上开始武术大会\n',
            '正式赛第二场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ChrSetFlags(0x0108, 0x0040)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0104, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_50E1')
    def lambda_50E1():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_50E1')

    DispatchAsync2(0x0108, 0x0001, lambda_50E1)

    @scena.Lambda('lambda_50F2')
    def lambda_50F2():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_50F2')

    DispatchAsync2(0x0101, 0x0001, lambda_50F2)

    @scena.Lambda('lambda_5103')
    def lambda_5103():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_5103')

    DispatchAsync2(0x0102, 0x0001, lambda_5103)

    @scena.Lambda('lambda_5114')
    def lambda_5114():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_5114')

    DispatchAsync2(0x0104, 0x0001, lambda_5114)

    @scena.Lambda('lambda_5125')
    def lambda_5125():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_5125)

    Sleep(200)

    @scena.Lambda('lambda_5145')
    def lambda_5145():
        ChrWalkTo(0x00FE, 2580, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_5145)

    @scena.Lambda('lambda_5160')
    def lambda_5160():
        ChrWalkTo(0x00FE, -350, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5160)

    Sleep(200)

    @scena.Lambda('lambda_5180')
    def lambda_5180():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5180)

    @scena.Lambda('lambda_519B')
    def lambda_519B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_519B')

    DispatchAsync2(0x0012, 0x0001, lambda_519B)

    @scena.Lambda('lambda_51AC')
    def lambda_51AC():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_51AC')

    DispatchAsync2(0x0013, 0x0001, lambda_51AC)

    @scena.Lambda('lambda_51BD')
    def lambda_51BD():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_51BD')

    DispatchAsync2(0x0014, 0x0001, lambda_51BD)

    @scena.Lambda('lambda_51CE')
    def lambda_51CE():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_51CE')

    DispatchAsync2(0x0011, 0x0001, lambda_51CE)

    @scena.Lambda('lambda_51DF')
    def lambda_51DF():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_51DF)

    Sleep(200)

    @scena.Lambda('lambda_51FF')
    def lambda_51FF():
        ChrWalkTo(0x00FE, -310, 0, -800, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_51FF)

    @scena.Lambda('lambda_521A')
    def lambda_521A():
        ChrWalkTo(0x00FE, 2670, 0, -800, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_521A)

    Sleep(200)

    @scena.Lambda('lambda_523A')
    def lambda_523A():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_523A)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0012, 29)
    ChrSetChipByIndex(0x0013, 29)
    ChrSetChipByIndex(0x0014, 29)
    ChrSetChipByIndex(0x0011, 29)
    ChrSetFlags(0x0012, 0x0002)
    ChrSetFlags(0x0013, 0x0002)
    ChrSetFlags(0x0014, 0x0002)
    ChrSetFlags(0x0011, 0x0002)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x16),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x08,
        (
            (Expr.PushLong, 0x1E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x12),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0108, 25)
    ChrSetChipByIndex(0x0101, 22)
    ChrSetChipByIndex(0x0102, 23)
    ChrSetChipByIndex(0x0104, 24)
    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x0000039D, 0x00000000, 0x00, 0x0000, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x17),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x1B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x08,
        (
            (Expr.PushLong, 0x1F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x13),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0101, 1100, 0, -8740, 0)
    ChrSetPos(0x0102, -160, 0, -9400, 0)
    ChrSetPos(0x0108, 2380, 0, -9800, 0)
    ChrSetPos(0x0104, 1070, 0, -10590, 0)
    ChrSetPos(0x0012, 1830, 0, -3910, 180)
    ChrSetPos(0x0013, 900, 0, -2670, 180)
    ChrSetPos(0x0014, 320, 0, -3480, 180)
    ChrSetPos(0x0011, 2610, 0, -2850, 180)
    OP_66(0x0000)
    CameraMove(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110226V胜负已分！\n',
            '苍之组，金小组获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0012,
        (
            '#0450110227V#5P哈啊……哈啊……\n',
            '最后还是输了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0470110228V#5P真、真是厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0460110229V#5P可恶，可恶可恶可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110230V#506F#2P好啦好啦……\n',
            '不要那么沮丧嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110231V#006F说实话，我真是吃了一惊呢。\n',
            '你们现在居然能变得这么强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110232V#010F#2P我也这么觉得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110233V比在灯塔交手的时候要强得多了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0450110234V#5P是、是吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0470110235V#5P那个时候的事情，\n',
            '我们已经不太记得了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110236V#071F#2P虽然我不太明白是怎么一回事，\n',
            '不过我们都已拼尽全力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110237V大家就挺起胸膛回休息室去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x56FB
@scena.Code('func_07_56FB')
def func_07_56FB():
    EventBegin(0x00)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0019, 2260, 0, -7590, 0)
    ChrSetPos(0x0015, 300, 0, -7590, 0)
    ChrSetPos(0x0016, -560, 0, -7590, 0)
    ChrSetPos(0x0017, 1380, 0, -7590, 0)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    CameraSetDistance(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0000)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetPos(0x000D, 2260, 120, 11000, 180)
    ChrSetPos(0x000E, 1380, 120, 11000, 180)
    ChrSetPos(0x000F, 300, 120, 11000, 180)
    ChrSetPos(0x0010, -560, 120, 11000, 180)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    CameraMove(880, 0, 8980, 2000)
    OP_70(0x0001, 100)
    OP_73(0x0001)
    Sleep(500)

    PlaySE(176, 0x00, 0x64)

    @scena.Lambda('lambda_5842')
    def lambda_5842():
        ChrWalkTo(0x00FE, 1380, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5842)

    Sleep(50)

    @scena.Lambda('lambda_5862')
    def lambda_5862():
        ChrWalkTo(0x00FE, -560, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5862)

    Sleep(50)

    @scena.Lambda('lambda_5882')
    def lambda_5882():
        ChrWalkTo(0x00FE, 300, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5882)

    Sleep(50)

    @scena.Lambda('lambda_58A2')
    def lambda_58A2():
        ChrWalkTo(0x00FE, 2260, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_58A2)

    @scena.Lambda('lambda_58BD')
    def lambda_58BD():
        CameraMove(1000, 0, -6610, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_58BD)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110259V',
            (TxtCtl.SetColor, 0x5),
            '嗯，那个……\n',
            '我来说明一下这件事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110260V',
            (TxtCtl.SetColor, 0x5),
            '我想很多人也知道，\n',
            '他们是曾在柏斯地区作乱的\n',
            '空贼团『卡普亚一家』的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110261V',
            (TxtCtl.SetColor, 0x5),
            '他们希望能堂堂正正地战斗，\n',
            '给武术大会增添热闹的气氛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110262V',
            (TxtCtl.SetColor, 0x5),
            '同时也是为了向\n',
            '曾经受过困扰的王国人民谢罪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110263V',
            (TxtCtl.SetColor, 0x5),
            '为了这个目的，\n',
            '他们强烈希望参加这次的武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110264V',
            (TxtCtl.SetColor, 0x5),
            '因为在服刑期间态度良好，\n',
            '又得到了主办者杜南公爵的同意，\n',
            '所以他们今天得以在这里出场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110265V',
            (TxtCtl.SetColor, 0x5),
            '请大家给予理解和支持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x5AF0
@scena.Code('func_08_5AF0')
def func_08_5AF0():
    EventBegin(0x00)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x0019, 2260, 0, -7590, 0)
    ChrSetPos(0x0015, 1380, 0, -7590, 0)
    ChrSetPos(0x0016, 300, 0, -7590, 0)
    ChrSetPos(0x0017, -560, 0, -7590, 0)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x000D, 2260, 0, -5460, 180)
    ChrSetPos(0x000F, 300, 0, -5460, 180)
    ChrSetPos(0x0010, -560, 0, -5460, 180)
    ChrSetPos(0x000E, 1380, 0, -5460, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110271V各位，请安静！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210110272V马上开始武术大会\n',
            '正式赛第三场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0016, 0x0040)

    @scena.Lambda('lambda_5CC5')
    def lambda_5CC5():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_5CC5')

    DispatchAsync2(0x000E, 0x0001, lambda_5CC5)

    @scena.Lambda('lambda_5CD6')
    def lambda_5CD6():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_5CD6')

    DispatchAsync2(0x000F, 0x0001, lambda_5CD6)

    @scena.Lambda('lambda_5CE7')
    def lambda_5CE7():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_5CE7')

    DispatchAsync2(0x0010, 0x0001, lambda_5CE7)

    @scena.Lambda('lambda_5CF8')
    def lambda_5CF8():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_5CF8')

    DispatchAsync2(0x000D, 0x0001, lambda_5CF8)

    @scena.Lambda('lambda_5D09')
    def lambda_5D09():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_5D09)

    Sleep(200)

    @scena.Lambda('lambda_5D29')
    def lambda_5D29():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_5D29)

    @scena.Lambda('lambda_5D44')
    def lambda_5D44():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_5D44)

    Sleep(200)

    @scena.Lambda('lambda_5D64')
    def lambda_5D64():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_5D64)

    @scena.Lambda('lambda_5D7F')
    def lambda_5D7F():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5D7F')

    DispatchAsync2(0x0019, 0x0001, lambda_5D7F)

    @scena.Lambda('lambda_5D90')
    def lambda_5D90():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5D90')

    DispatchAsync2(0x0017, 0x0001, lambda_5D90)

    @scena.Lambda('lambda_5DA1')
    def lambda_5DA1():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5DA1')

    DispatchAsync2(0x0015, 0x0001, lambda_5DA1)

    @scena.Lambda('lambda_5DB2')
    def lambda_5DB2():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5DB2')

    DispatchAsync2(0x0016, 0x0001, lambda_5DB2)

    @scena.Lambda('lambda_5DC3')
    def lambda_5DC3():
        ChrWalkTo(0x00FE, 2260, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_5DC3)

    @scena.Lambda('lambda_5DDE')
    def lambda_5DDE():
        ChrWalkTo(0x00FE, -560, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_5DDE)

    Sleep(200)

    @scena.Lambda('lambda_5DFE')
    def lambda_5DFE():
        ChrWalkTo(0x00FE, 390, 0, -1720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_5DFE)

    @scena.Lambda('lambda_5E19')
    def lambda_5E19():
        ChrWalkTo(0x00FE, 1430, 0, -1790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_5E19)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0019, 29)
    ChrSetChipByIndex(0x0015, 29)
    ChrSetChipByIndex(0x0016, 29)
    ChrSetChipByIndex(0x0017, 29)
    ChrSetFlags(0x0019, 0x0002)
    ChrSetFlags(0x0015, 0x0002)
    ChrSetFlags(0x0016, 0x0002)
    ChrSetFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x34),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000E, 29)
    ChrSetChipByIndex(0x000F, 29)
    ChrSetChipByIndex(0x0010, 29)
    ChrSetChipByIndex(0x000D, 29)
    ChrSetFlags(0x000E, 0x0002)
    ChrSetFlags(0x000F, 0x0002)
    ChrSetFlags(0x0010, 0x0002)
    ChrSetFlags(0x000D, 0x0002)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x2A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x26),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x000D, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBC, 0x00100005, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x35),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0019, 1260, 0, -8950, 0)
    ChrSetPos(0x0015, 320, 0, -9900, 0)
    ChrSetPos(0x0016, 2130, 0, -10270, 0)
    ChrSetPos(0x0017, 2940, 0, -9340, 0)
    ChrSetPos(0x000E, 40, 0, -2660, 180)
    ChrSetPos(0x000F, 1100, 0, -3990, 180)
    ChrSetPos(0x0010, 2230, 0, -2600, 180)
    ChrSetPos(0x000D, 2040, 0, -3690, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110276V胜负已分！\n',
            '红之组，多伦小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x60DA
@scena.Code('func_09_60DA')
def func_09_60DA():
    EventBegin(0x00)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001C, 2260, 0, -5460, 180)
    ChrSetPos(0x001D, 300, 0, -5460, 180)
    ChrSetPos(0x001E, -560, 0, -5460, 180)
    ChrSetPos(0x001F, 1380, 0, -5460, 180)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0019, 2260, 0, -7590, 0)
    ChrSetPos(0x0015, 1380, 0, -7590, 0)
    ChrSetPos(0x0016, 300, 0, -7590, 0)
    ChrSetPos(0x0017, -560, 0, -7590, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110303V马上开始武术大会\n',
            '正式赛第四场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x001D, 0x0040)
    ChrSetFlags(0x001E, 0x0040)
    ChrSetFlags(0x001F, 0x0040)

    @scena.Lambda('lambda_627B')
    def lambda_627B():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_627B')

    DispatchAsync2(0x0019, 0x0001, lambda_627B)

    @scena.Lambda('lambda_628C')
    def lambda_628C():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_628C')

    DispatchAsync2(0x0015, 0x0001, lambda_628C)

    @scena.Lambda('lambda_629D')
    def lambda_629D():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_629D')

    DispatchAsync2(0x0016, 0x0001, lambda_629D)

    @scena.Lambda('lambda_62AE')
    def lambda_62AE():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_62AE')

    DispatchAsync2(0x0017, 0x0001, lambda_62AE)

    @scena.Lambda('lambda_62BF')
    def lambda_62BF():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_62BF)

    Sleep(200)

    @scena.Lambda('lambda_62DF')
    def lambda_62DF():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_62DF)

    @scena.Lambda('lambda_62FA')
    def lambda_62FA():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_62FA)

    Sleep(200)

    @scena.Lambda('lambda_631A')
    def lambda_631A():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_631A)

    @scena.Lambda('lambda_6335')
    def lambda_6335():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6335')

    DispatchAsync2(0x001C, 0x0001, lambda_6335)

    @scena.Lambda('lambda_6346')
    def lambda_6346():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6346')

    DispatchAsync2(0x001D, 0x0001, lambda_6346)

    @scena.Lambda('lambda_6357')
    def lambda_6357():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6357')

    DispatchAsync2(0x001E, 0x0001, lambda_6357)

    @scena.Lambda('lambda_6368')
    def lambda_6368():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6368')

    DispatchAsync2(0x001F, 0x0001, lambda_6368)

    @scena.Lambda('lambda_6379')
    def lambda_6379():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_6379)

    Sleep(200)

    @scena.Lambda('lambda_6399')
    def lambda_6399():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_6399)

    @scena.Lambda('lambda_63B4')
    def lambda_63B4():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_63B4)

    Sleep(200)

    @scena.Lambda('lambda_63D4')
    def lambda_63D4():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_63D4)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0019, 29)
    ChrSetChipByIndex(0x0015, 29)
    ChrSetChipByIndex(0x0016, 29)
    ChrSetChipByIndex(0x0017, 29)
    ChrSetFlags(0x0019, 0x0002)
    ChrSetFlags(0x0015, 0x0002)
    ChrSetFlags(0x0016, 0x0002)
    ChrSetFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x34),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x001C, 29)
    ChrSetChipByIndex(0x001D, 29)
    ChrSetChipByIndex(0x001E, 29)
    ChrSetChipByIndex(0x001F, 29)
    ChrSetFlags(0x001C, 0x0002)
    ChrSetFlags(0x001D, 0x0002)
    ChrSetFlags(0x001E, 0x0002)
    ChrSetFlags(0x001F, 0x0002)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBD, 0x00100006, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x35),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0019, 320, 0, -9150, 0)
    ChrSetPos(0x0015, 3630, 0, -8680, 0)
    ChrSetPos(0x0016, 1900, 0, -10130, 0)
    ChrSetPos(0x0017, -1110, 0, -10190, 0)
    ChrSetPos(0x001C, 790, 0, -2710, 180)
    ChrSetPos(0x001D, -400, 0, -3530, 180)
    ChrSetPos(0x001E, 2470, 0, -3700, 180)
    ChrSetPos(0x001F, 940, 0, -4430, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110307V胜负已分！\n',
            '红之组，洛伦斯小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x6697
@scena.Code('func_0A_6697')
def func_0A_6697():
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    CameraMove(-13010, 4700, -19290, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(1830, 0)
    OP_6C(190000, 0)
    OP_6E(620, 0)
    ChrSetPos(0x0053, -12650, 4700, -16700, 90)
    ChrSetPos(0x005E, -12650, 4700, -14700, 90)
    ChrSetPos(0x006A, -13730, 4950, -16780, 90)
    ChrSetPos(0x0074, -12660, 4700, -15720, 90)
    ChrSetPos(0x006F, -14780, 5200, 3980, 90)
    ChrSetPos(0x005D, -13830, 4950, -15790, 90)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)

    @scena.Lambda('lambda_675B')
    def lambda_675B():
        CameraMove(-13480, 4950, 3760, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_675B)

    OP_6C(315000, 6000)
    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007E, 2, 0x3F2))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x6788
@scena.Code('func_0B_6788')
def func_0B_6788():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    MapSetFlags(0x00100000)
    CameraMove(-6270, 0, -6280, 0)
    OP_67(0, 11870, -10000, 0)
    CameraSetDistance(3320, 0)
    OP_6C(90000, 0)
    OP_6E(505, 0)
    ChrSetPos(0x0053, -12650, 4700, -16700, 90)
    ChrSetPos(0x005E, -12650, 4700, -14700, 90)
    ChrSetPos(0x006A, -13730, 4950, -16780, 90)
    ChrSetPos(0x0074, -12660, 4700, -15720, 90)
    ChrSetPos(0x006F, -14780, 5200, 3980, 90)
    ChrSetPos(0x005D, -13830, 4950, -15790, 90)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_6846')
    def lambda_6846():
        CameraMove(1840, 0, -7130, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6846)

    @scena.Lambda('lambda_685E')
    def lambda_685E():
        OP_67(0, 5770, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_685E)

    @scena.Lambda('lambda_6876')
    def lambda_6876():
        OP_6C(135000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6876)

    @scena.Lambda('lambda_6886')
    def lambda_6886():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6886)

    ChrSetPos(0x0108, 2260, 0, -7590, 0)
    ChrSetPos(0x0101, 1380, 0, -7590, 0)
    ChrSetPos(0x0102, 300, 0, -7590, 0)
    ChrSetPos(0x0104, -560, 0, -7590, 0)
    ChrSetPos(0x0009, 2260, 0, -5460, 180)
    ChrSetPos(0x000A, 1380, 0, -5460, 180)
    ChrSetPos(0x000B, 300, 0, -5460, 180)
    ChrSetPos(0x000C, -560, 0, -5460, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    Sleep(5000)

    ChrTalk(
        0x0009,
        (
            '#0320110800V#6P来了吗。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120110801V#6P两位新人，呀嗬～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110802V#506F#2P嘿嘿……\n',
            '各位前辈，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110803V#010F#2P还请各位前辈手下留情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310110804V#822F#6P『不动金』……\n',
            '一直想向您讨教呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310110805V#6P到底有多厉害，\n',
            '就由这把剑来检验一下吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110806V#070F#2P哼哼，可以啊。\n',
            '我也会全力以赴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330110807V#845F#6P哈哈，如果可以的话，\n',
            '真的希望是在决赛中碰面呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110808V#6P在这里遇见也是命运的安排吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110809V#030F#2P一方是经验丰富的游击士集团。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110810V一方是令人注目的新人组合——\n',
            '武术家游击士和天才演奏家的混合小组。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110811V#035F哪一方会获胜，\n',
            '只有女神才会知道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210110812V马上开始武术大会\n',
            '正式赛第五场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ChrSetFlags(0x0108, 0x0040)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0104, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_6CD4')
    def lambda_6CD4():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_6CD4')

    DispatchAsync2(0x0108, 0x0001, lambda_6CD4)

    @scena.Lambda('lambda_6CE5')
    def lambda_6CE5():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_6CE5')

    DispatchAsync2(0x0101, 0x0001, lambda_6CE5)

    @scena.Lambda('lambda_6CF6')
    def lambda_6CF6():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_6CF6')

    DispatchAsync2(0x0102, 0x0001, lambda_6CF6)

    @scena.Lambda('lambda_6D07')
    def lambda_6D07():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_6D07')

    DispatchAsync2(0x0104, 0x0001, lambda_6D07)

    @scena.Lambda('lambda_6D18')
    def lambda_6D18():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_6D18)

    Sleep(200)

    @scena.Lambda('lambda_6D38')
    def lambda_6D38():
        ChrWalkTo(0x00FE, 2580, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_6D38)

    @scena.Lambda('lambda_6D53')
    def lambda_6D53():
        ChrWalkTo(0x00FE, -350, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6D53)

    Sleep(200)

    @scena.Lambda('lambda_6D73')
    def lambda_6D73():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6D73)

    @scena.Lambda('lambda_6D8E')
    def lambda_6D8E():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6D8E')

    DispatchAsync2(0x000B, 0x0001, lambda_6D8E)

    @scena.Lambda('lambda_6D9F')
    def lambda_6D9F():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6D9F')

    DispatchAsync2(0x000A, 0x0001, lambda_6D9F)

    @scena.Lambda('lambda_6DB0')
    def lambda_6DB0():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6DB0')

    DispatchAsync2(0x0009, 0x0001, lambda_6DB0)

    @scena.Lambda('lambda_6DC1')
    def lambda_6DC1():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6DC1')

    DispatchAsync2(0x000C, 0x0001, lambda_6DC1)

    @scena.Lambda('lambda_6DD2')
    def lambda_6DD2():
        ChrWalkTo(0x00FE, 390, 0, -1720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_6DD2)

    @scena.Lambda('lambda_6DED')
    def lambda_6DED():
        ChrWalkTo(0x00FE, 1430, 0, -1790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_6DED)

    @scena.Lambda('lambda_6E08')
    def lambda_6E08():
        ChrWalkTo(0x00FE, 2260, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_6E08)

    @scena.Lambda('lambda_6E23')
    def lambda_6E23():
        ChrWalkTo(0x00FE, -560, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_6E23)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0108, 25)
    ChrSetChipByIndex(0x0101, 22)
    ChrSetChipByIndex(0x0102, 23)
    ChrSetChipByIndex(0x0104, 24)
    ChrSetChipByIndex(0x000B, 29)
    ChrSetChipByIndex(0x000A, 29)
    ChrSetChipByIndex(0x0009, 29)
    ChrSetChipByIndex(0x000C, 29)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x000C, 0x0002)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
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

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000C, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x0000039E, 0x00000000, 0x00, 0x0000, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0101, 1100, 0, -8740, 0)
    ChrSetPos(0x0102, -160, 0, -9400, 0)
    ChrSetPos(0x0108, 2380, 0, -9800, 0)
    ChrSetPos(0x0104, 1070, 0, -10590, 0)
    ChrSetPos(0x000B, 2540, 0, -4780, 180)
    ChrSetPos(0x000A, -970, 0, -4310, 180)
    ChrSetPos(0x0009, 20, 0, -3500, 180)
    ChrSetPos(0x000C, 1670, 0, -3790, 180)
    OP_66(0x0000)
    CameraMove(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110816V#5P胜负已分！\n',
            '苍之组，金小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0330110817V#5P唔……干得漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310110818V#5P『不动金』……\n',
            '没想到会是如此厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110819V#070F#2P过奖了，你们也相当的强哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110820V如果没有艾丝蒂尔他们帮忙的话，\n',
            '我一个人肯定没有胜算的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110821V#007F#2P哈啊哈啊……\n',
            '我们，赢了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110822V#019F#2P嗯，怎么说呢……\n',
            '没有拖后腿就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320110823V#835F#5P呵呵……\n',
            '不要太谦虚啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320110824V#5P金大人就不用说了，\n',
            '你们两个也很厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120110825V#856F#5P呼，不愧是雪拉前辈\n',
            '教导出来的孩子啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120110826V#854F#5P而且，没想到那一位小哥\n',
            '也能有如此漂亮的表现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110827V#035F#2P呵呵……\n',
            '小姐你也让我很着迷呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110828V不介意的话，\n',
            '比赛之后我们去干杯庆祝一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110829V#509F#2P给我适可而止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0048, 0x01, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007E, 3, 0x3F3))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x7397
@scena.Code('func_0C_7397')
def func_0C_7397():
    EventBegin(0x00)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1130, 0, -5670, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(3320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001C, 2260, 0, -5460, 180)
    ChrSetPos(0x001D, 300, 0, -5460, 180)
    ChrSetPos(0x001E, -560, 0, -5460, 180)
    ChrSetPos(0x001F, 1380, 0, -5460, 180)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000E, 2260, 0, -7590, 0)
    ChrSetPos(0x000F, 1380, 0, -7590, 0)
    ChrSetPos(0x0010, 300, 0, -7590, 0)
    ChrSetPos(0x000D, -560, 0, -7590, 0)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0300110856V#190F#4P哟，带面具的小哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110857V我已经等这个复仇机会很久了！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0290110858V#200F#4P嘿嘿，这得感谢那个胖公爵啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140110859V#280F#5P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0090110860V#214F#4P有、有什么好笑的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140110861V#280F#5P埃雷波尼亚的没落贵族，\n',
            '卡普亚男爵家的各位孤儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110862V被恶德商人霸占了领地，\n',
            '为了家业复兴而干起空贼的行当……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110863V真是可歌可泣的故事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0300110864V#196F#4P#3S你、你！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0290110865V#201F#4P你怎么会知道的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140110866V#280F#5P别忘了，\n',
            '我们所属的可是『情报部』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110867V你们还是放弃向我们复仇的念头，\n',
            '老老实实地服刑比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110868V因为你们并不是什么穷凶极恶的坏人。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0090110869V#216F#4P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0290110870V#204F#4P哼，看来你不单会耍手段，\n',
            '连嘴上功夫也有两下子的嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0300110871V#196F哼，马上就让你们\n',
            '成为我导力炮下的食物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210110872V马上开始武术大会\n',
            '正式赛第六场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x001D, 0x0040)
    ChrSetFlags(0x001E, 0x0040)
    ChrSetFlags(0x001F, 0x0040)

    @scena.Lambda('lambda_7969')
    def lambda_7969():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_7969')

    DispatchAsync2(0x000E, 0x0001, lambda_7969)

    @scena.Lambda('lambda_797A')
    def lambda_797A():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_797A')

    DispatchAsync2(0x000F, 0x0001, lambda_797A)

    @scena.Lambda('lambda_798B')
    def lambda_798B():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_798B')

    DispatchAsync2(0x0010, 0x0001, lambda_798B)

    @scena.Lambda('lambda_799C')
    def lambda_799C():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_799C')

    DispatchAsync2(0x000D, 0x0001, lambda_799C)

    @scena.Lambda('lambda_79AD')
    def lambda_79AD():
        ChrWalkTo(0x00FE, 2350, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_79AD)

    @scena.Lambda('lambda_79C8')
    def lambda_79C8():
        ChrWalkTo(0x00FE, -170, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_79C8)

    Sleep(200)

    @scena.Lambda('lambda_79E8')
    def lambda_79E8():
        ChrWalkTo(0x00FE, 1570, 0, -11430, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_79E8)

    @scena.Lambda('lambda_7A03')
    def lambda_7A03():
        ChrWalkTo(0x00FE, 390, 0, -11390, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_7A03)

    @scena.Lambda('lambda_7A1E')
    def lambda_7A1E():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7A1E')

    DispatchAsync2(0x001C, 0x0001, lambda_7A1E)

    @scena.Lambda('lambda_7A2F')
    def lambda_7A2F():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7A2F')

    DispatchAsync2(0x001D, 0x0001, lambda_7A2F)

    @scena.Lambda('lambda_7A40')
    def lambda_7A40():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7A40')

    DispatchAsync2(0x001E, 0x0001, lambda_7A40)

    @scena.Lambda('lambda_7A51')
    def lambda_7A51():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7A51')

    DispatchAsync2(0x001F, 0x0001, lambda_7A51)

    @scena.Lambda('lambda_7A62')
    def lambda_7A62():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_7A62)

    Sleep(200)

    @scena.Lambda('lambda_7A82')
    def lambda_7A82():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_7A82)

    @scena.Lambda('lambda_7A9D')
    def lambda_7A9D():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_7A9D)

    Sleep(200)

    @scena.Lambda('lambda_7ABD')
    def lambda_7ABD():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_7ABD)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x000E, 29)
    ChrSetChipByIndex(0x000F, 29)
    ChrSetChipByIndex(0x0010, 29)
    ChrSetChipByIndex(0x000D, 29)
    ChrSetFlags(0x000E, 0x0002)
    ChrSetFlags(0x000F, 0x0002)
    ChrSetFlags(0x0010, 0x0002)
    ChrSetFlags(0x000D, 0x0002)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x24),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x20),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x001C, 29)
    ChrSetChipByIndex(0x001D, 29)
    ChrSetChipByIndex(0x001E, 29)
    ChrSetChipByIndex(0x001F, 29)
    ChrSetFlags(0x001C, 0x0002)
    ChrSetFlags(0x001D, 0x0002)
    ChrSetFlags(0x001E, 0x0002)
    ChrSetFlags(0x001F, 0x0002)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBE, 0x00100007, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x29),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x25),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x000E, 1540, 0, -9380, 0)
    ChrSetPos(0x000F, -170, 0, -9030, 0)
    ChrSetPos(0x0010, 730, 0, -10360, 0)
    ChrSetPos(0x000D, 2770, 0, -8750, 0)
    ChrSetPos(0x001C, 790, 0, -2710, 180)
    ChrSetPos(0x001D, -400, 0, -3530, 180)
    ChrSetPos(0x001E, 2470, 0, -3700, 180)
    ChrSetPos(0x001F, 940, 0, -4430, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110307V胜负已分！\n',
            '红之组，洛伦斯小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 4, 0x3F4))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x7D80
@scena.Code('func_0D_7D80')
def func_0D_7D80():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    PlaySE(174, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetRGBAMask(0x0021, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0020, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0029, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0028, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrSetFlags(0x0021, 0x0004)
    ChrSetFlags(0x0020, 0x0004)
    ChrSetFlags(0x0029, 0x0004)
    ChrSetFlags(0x0028, 0x0004)
    ChrSetPos(0x0021, 19870, 9500, -6460, 270)
    ChrSetPos(0x0020, 20800, 9500, -5950, 270)
    ChrSetPos(0x0029, 20290, 9750, -7200, 270)
    ChrSetPos(0x0028, 21100, 9500, -6600, 270)
    CameraMove(1210, 11600, -6480, 0)
    OP_67(0, 3630, -10000, 0)
    CameraSetDistance(2870, 0)
    OP_6C(269000, 0)
    OP_6E(428, 0)

    @scena.Lambda('lambda_7E80')
    def lambda_7E80():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7E80)

    FadeIn(2000, 0)
    Sleep(4000)

    ChrSetPos(0x0030, 14650, 4700, 250, 270)
    ChrSetPos(0x0031, 15730, 4950, 250, 270)
    ChrSetPos(0x0032, 16860, 5200, 250, 270)
    ChrSetPos(0x0033, 17850, 5450, 250, 270)
    ChrSetPos(0x0034, 18880, 5700, 250, 270)
    ChrSetPos(0x0035, 19640, 5950, 250, 270)
    ChrSetPos(0x0036, 14650, 4700, 1200, 270)
    ChrSetPos(0x0037, 15730, 4950, 1200, 270)
    ChrSetPos(0x0038, 16860, 5200, 1200, 270)
    ChrSetPos(0x0039, 17850, 5450, 1200, 270)
    ChrSetPos(0x003A, 18880, 5700, 1200, 270)
    ChrSetPos(0x003B, 19640, 5950, 1200, 270)
    ChrSetPos(0x003C, 14650, 4700, 2390, 270)
    ChrSetPos(0x003D, 15730, 4950, 2390, 270)
    ChrSetPos(0x003E, 16860, 5200, 2390, 270)
    ChrSetPos(0x003F, 17850, 5450, 2390, 270)
    ChrSetPos(0x0040, 18880, 5700, 2390, 270)
    ChrSetPos(0x0041, 19640, 5950, 2390, 270)
    ChrSetPos(0x0042, 14650, 4700, 3550, 270)
    ChrSetPos(0x0043, 15730, 4950, 3550, 270)
    ChrSetPos(0x0044, 16860, 5200, 3550, 270)
    ChrSetPos(0x0045, 17850, 5450, 3550, 270)
    ChrSetPos(0x0046, 18880, 5700, 3550, 270)
    ChrSetPos(0x0047, 19640, 5950, 3550, 270)
    ChrSetPos(0x0048, 14650, 4700, 4830, 270)
    ChrSetPos(0x0049, 15730, 4950, 4830, 270)
    ChrSetPos(0x004A, 16860, 5200, 4830, 270)
    ChrSetPos(0x004B, 17850, 5450, 4830, 270)
    ChrSetPos(0x004C, 18880, 5700, 4830, 270)
    ChrSetPos(0x004D, 19640, 5950, 4830, 270)
    ChrSetPos(0x004E, 14650, 4700, -13300, 270)
    ChrSetPos(0x004F, 15730, 4950, -13300, 270)
    ChrSetPos(0x0050, 16860, 5200, -13300, 270)
    ChrSetPos(0x0051, 17850, 5450, -13300, 270)
    ChrSetPos(0x0052, 18880, 5700, -13300, 270)
    ChrSetPos(0x0053, 19640, 5950, -13300, 270)
    ChrSetPos(0x0054, 14650, 4700, -14500, 270)
    ChrSetPos(0x0055, 15730, 4950, -14500, 270)
    ChrSetPos(0x0056, 16860, 5200, -14500, 270)
    ChrSetPos(0x0057, 17850, 5450, -14500, 270)
    ChrSetPos(0x0058, 18880, 5700, -14500, 270)
    ChrSetPos(0x0059, 19640, 5950, -14500, 270)
    ChrSetPos(0x005A, 14650, 4700, -15600, 270)
    ChrSetPos(0x005B, 15730, 4950, -15600, 270)
    ChrSetPos(0x005C, 16860, 5200, -15600, 270)
    ChrSetPos(0x005D, 17850, 5450, -15600, 270)
    ChrSetPos(0x005E, 18880, 5700, -15600, 270)
    ChrSetPos(0x005F, 19640, 5950, -15600, 270)
    ChrSetPos(0x0060, 14650, 4700, -16920, 270)
    ChrSetPos(0x0061, 15730, 4950, -16920, 270)
    ChrSetPos(0x0062, 16860, 5200, -16920, 270)
    ChrSetPos(0x0063, 17850, 5450, -16920, 270)
    ChrSetPos(0x0064, 18880, 5700, -16920, 270)
    ChrSetPos(0x0065, 19640, 5950, -16920, 270)
    ChrSetPos(0x0066, 14650, 4700, -18030, 270)
    ChrSetPos(0x0067, 15730, 4950, -18030, 270)
    ChrSetPos(0x0068, 16860, 5200, -18030, 270)
    ChrSetPos(0x0069, 17850, 5450, -18030, 270)
    ChrSetPos(0x006A, 18880, 5700, -18030, 270)
    ChrSetPos(0x006B, 19640, 5950, -18030, 270)
    Sleep(5000)

    @scena.Lambda('lambda_829F')
    def lambda_829F():
        CameraMove(9560, 14150, -6480, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_829F)

    @scena.Lambda('lambda_82B7')
    def lambda_82B7():
        OP_67(0, 6940, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_82B7)

    @scena.Lambda('lambda_82CF')
    def lambda_82CF():
        OP_6E(314, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_82CF)

    Sleep(1500)

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    Sleep(2000)

    @scena.Lambda('lambda_82FC')
    def lambda_82FC():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_82FC)

    @scena.Lambda('lambda_8317')
    def lambda_8317():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_8317)

    @scena.Lambda('lambda_8332')
    def lambda_8332():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0021, 0x0002, lambda_8332)

    @scena.Lambda('lambda_8344')
    def lambda_8344():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_8344)

    Sleep(300)

    @scena.Lambda('lambda_835B')
    def lambda_835B():
        ChrWalkTo(0x00FE, 3830, 9750, -7250, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_835B)

    @scena.Lambda('lambda_8376')
    def lambda_8376():
        ChrWalkTo(0x00FE, 3830, 9750, -7250, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_8376)

    @scena.Lambda('lambda_8391')
    def lambda_8391():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0029, 0x0002, lambda_8391)

    @scena.Lambda('lambda_83A3')
    def lambda_83A3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0028, 0x0002, lambda_83A3)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007E, 6, 0x3F6))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x83D1
@scena.Code('func_0E_83D1')
def func_0E_83D1():
    EventBegin(0x00)
    CameraMove(-4350, 1700, -6590, 0)
    OP_67(0, 9590, -10000, 0)
    CameraSetDistance(3970, 0)
    OP_6C(90000, 0)
    OP_6E(389, 0)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 870, 0, -6590, 0)

    @scena.Lambda('lambda_842C')
    def lambda_842C():
        CameraSetDistance(2940, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_842C)

    @scena.Lambda('lambda_843C')
    def lambda_843C():
        CameraMove(1020, 0, -6570, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_843C)

    @scena.Lambda('lambda_8454')
    def lambda_8454():
        ChrWalkTo(0x00FE, 5940, 0, -6480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_8454)

    WaitForThreadExit(0x0024, 0x0001)
    ChrSetDirection(0x0024, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200111743V',
            (TxtCtl.SetColor, 0x5),
            '武术大会从预选赛开始\n',
            '已经经过了一个星期的时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111744V',
            (TxtCtl.SetColor, 0x5),
            '今天终于迎来了\n',
            '最后一场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111745V',
            (TxtCtl.SetColor, 0x5),
            '到底哪一支队伍会\n',
            '获得胜利和荣耀呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111746V',
            (TxtCtl.SetColor, 0x5),
            '那么下面公布参加决赛的\n',
            '对阵的双方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110206V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——\n',
            '来自卡尔瓦德共和国的武术家。\n',
            '金选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110847V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——\n',
            '王国军情报部，特务部队所属。\n',
            '洛伦斯少尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 7, 0x3F7))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x8631
@scena.Code('func_0F_8631')
def func_0F_8631():
    EventBegin(0x00)
    MapSetFlags(0x00100000)
    PlaySE(174, 0x00, 0x64)
    CameraMove(1010, 0, -20480, 0)
    OP_67(0, 2060, -10000, 0)
    CameraSetDistance(3640, 0)
    OP_6C(180000, 0)
    OP_6E(316, 0)
    OP_71(0x0001, 0x0004)
    FadeOut(0, 0, -1)

    @scena.Lambda('lambda_868F')
    def lambda_868F():
        CameraSetDistance(1380, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_868F)

    @scena.Lambda('lambda_869F')
    def lambda_869F():
        OP_6E(840, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_869F)

    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 5550, 0, -6570, 270)
    Sleep(500)

    FadeIn(2000, 0)
    ChrSetPos(0x0108, 2260, 0, -24190, 0)
    ChrSetPos(0x0101, 1380, 0, -24190, 0)
    ChrSetPos(0x0102, 300, 0, -24190, 0)
    ChrSetPos(0x0104, -560, 0, -24190, 0)
    ChrSetPos(0x001C, 2260, 0, 11000, 180)
    ChrSetPos(0x001D, 1380, 0, 11000, 180)
    ChrSetPos(0x001E, 300, 0, 11000, 180)
    ChrSetPos(0x001F, -560, 0, 11000, 180)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    Sleep(2000)

    OP_70(0x0000, 100)
    OP_70(0x0001, 100)
    Sleep(3000)

    @scena.Lambda('lambda_8787')
    def lambda_8787():
        CameraMove(1650, 0, -6810, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8787)

    @scena.Lambda('lambda_879F')
    def lambda_879F():
        OP_6C(134000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_879F)

    @scena.Lambda('lambda_87AF')
    def lambda_87AF():
        OP_67(0, 5420, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_87AF)

    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)

    @scena.Lambda('lambda_87D1')
    def lambda_87D1():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_87D1)

    Sleep(300)

    @scena.Lambda('lambda_87F1')
    def lambda_87F1():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_87F1)

    Sleep(50)

    @scena.Lambda('lambda_8811')
    def lambda_8811():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8811)

    Sleep(50)

    @scena.Lambda('lambda_8831')
    def lambda_8831():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8831)

    ChrSetPos(0x001C, 2260, 0, -5460, 180)
    ChrSetPos(0x001D, 1380, 0, -5460, 180)
    ChrSetPos(0x001E, 300, 0, -5460, 180)
    ChrSetPos(0x001F, -560, 0, -5460, 180)
    OP_72(0x0001, 0x0004)
    Sleep(6000)

    Fade(1000)
    CameraSetDistance(1020, 0)
    OP_6C(45000, 0)
    CameraMove(910, 0, -6640, 0)
    OP_0D()

    ChrTalk(
        0x001C,
        (
            '#2620111754V（果然比至今为止碰到的家伙\n',
            '　看起来都要厉害得多……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111755V（可是，队伍的一半\n',
            '　只是稚气未脱的少年少女啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111756V（总之根本不是我们的对手嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111757V#280F（哼哼，不要轻敌。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140111758V（那些小孩是游击士协会的人哦。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111759V（哎……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111760V（难道是报告中的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111761V#281F（有这种可能。\n',
            '　一定不要放松警惕啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111762V（……是！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111763V（明白了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111764V#509F#4P喂喂～怎么叽叽咕咕的～\n',
            '你们在偷偷摸摸说些什么呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111765V#035F#4P呵，艾丝蒂尔君。\n',
            '不要和那些人介意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111766V带着那样的面具，\n',
            '肯定是对自己的脸没有信心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111767V因为嫉妒我这艺术般的美貌，\n',
            '偷偷地说些坏话也是没有办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111768V你、你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111769V不要随便乱解释！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111770V#012F#4P那个……\n',
            '您是叫洛伦斯少尉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111771V#281F怎么了，这位黑发少年？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111772V#004F#4P约修亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111773V#013F#4P你的剑法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111774V#015F…………………………\n',
            '不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111775V#012F总之请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111776V#280F哼……\n',
            '彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111777V#505F#4P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111778V#070F#4P好了，谈话就到这里为止吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111779V差不多该开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210111780V马上开始武术大会的决赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210111781V请两队队员站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ChrSetFlags(0x0108, 0x0040)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0104, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x001D, 0x0040)
    ChrSetFlags(0x001E, 0x0040)
    ChrSetFlags(0x001F, 0x0040)

    @scena.Lambda('lambda_8E4E')
    def lambda_8E4E():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_8E4E')

    DispatchAsync2(0x0108, 0x0001, lambda_8E4E)

    @scena.Lambda('lambda_8E5F')
    def lambda_8E5F():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_8E5F')

    DispatchAsync2(0x0101, 0x0001, lambda_8E5F)

    @scena.Lambda('lambda_8E70')
    def lambda_8E70():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_8E70')

    DispatchAsync2(0x0102, 0x0001, lambda_8E70)

    @scena.Lambda('lambda_8E81')
    def lambda_8E81():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_8E81')

    DispatchAsync2(0x0104, 0x0001, lambda_8E81)

    @scena.Lambda('lambda_8E92')
    def lambda_8E92():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_8E92)

    Sleep(200)

    @scena.Lambda('lambda_8EB2')
    def lambda_8EB2():
        ChrWalkTo(0x00FE, 2580, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_8EB2)

    @scena.Lambda('lambda_8ECD')
    def lambda_8ECD():
        ChrWalkTo(0x00FE, -350, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_8ECD)

    Sleep(200)

    @scena.Lambda('lambda_8EED')
    def lambda_8EED():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8EED)

    @scena.Lambda('lambda_8F08')
    def lambda_8F08():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8F08')

    DispatchAsync2(0x001C, 0x0001, lambda_8F08)

    @scena.Lambda('lambda_8F19')
    def lambda_8F19():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8F19')

    DispatchAsync2(0x001D, 0x0001, lambda_8F19)

    @scena.Lambda('lambda_8F2A')
    def lambda_8F2A():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8F2A')

    DispatchAsync2(0x001E, 0x0001, lambda_8F2A)

    @scena.Lambda('lambda_8F3B')
    def lambda_8F3B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8F3B')

    DispatchAsync2(0x001F, 0x0001, lambda_8F3B)

    @scena.Lambda('lambda_8F4C')
    def lambda_8F4C():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_8F4C)

    Sleep(200)

    @scena.Lambda('lambda_8F6C')
    def lambda_8F6C():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_8F6C)

    @scena.Lambda('lambda_8F87')
    def lambda_8F87():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_8F87)

    Sleep(200)

    @scena.Lambda('lambda_8FA7')
    def lambda_8FA7():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_8FA7)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210111782V在空之女神的见证下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x001C, 29)
    ChrSetChipByIndex(0x001D, 29)
    ChrSetChipByIndex(0x001E, 29)
    ChrSetChipByIndex(0x001F, 29)
    ChrSetFlags(0x001C, 0x0002)
    ChrSetFlags(0x001D, 0x0002)
    ChrSetFlags(0x001E, 0x0002)
    ChrSetFlags(0x001F, 0x0002)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0108, 25)
    ChrSetChipByIndex(0x0101, 22)
    ChrSetChipByIndex(0x0102, 23)
    ChrSetChipByIndex(0x0104, 24)
    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x0000039F, 0x00000000, 0x00, 0x0000, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0101, 1100, 0, -8740, 0)
    ChrSetPos(0x0102, -160, 0, -9400, 0)
    ChrSetPos(0x0108, 2380, 0, -9800, 0)
    ChrSetPos(0x0104, 1070, 0, -10590, 0)
    ChrSetPos(0x001C, 790, 0, -2710, 180)
    ChrSetPos(0x001D, -400, 0, -3530, 180)
    ChrSetPos(0x001E, 2470, 0, -3700, 180)
    ChrSetPos(0x001F, 940, 0, -4430, 180)
    OP_66(0x0000)
    CameraMove(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110816V#5P胜负已分！\n',
            '苍之组金小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111786V#5P不、不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111787V#5P代表精英的特务部队的我们\n',
            '竟然输掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111788V#280F#5P哼……还是有两下子嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010111789V#001F#2P#5S太好啦～～～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111790V#014F#2P赢了……我们赢了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111791V#034F#2P哈啊哈啊……\n',
            '真、真是累啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111792V#072F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_66(0x0001)
    CameraMove(860, 0, -6420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetPos(0x0020, 5470, 0, -6520, 270)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x0019, 3500, 0, -5190, 270)
    ChrSetPos(0x001B, 3500, 0, -7920, 270)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetChipByIndex(0x0104, 65535)
    ChrSetPos(0x0020, 3290, 0, -7050, 270)
    ChrSetPos(0x0021, 2500, 0, -6550, 270)
    ChrSetPos(0x0101, -1310, 0, -5190, 90)
    ChrSetPos(0x0102, -1310, 0, -6120, 90)
    ChrSetPos(0x0108, -1310, 0, -6940, 90)
    ChrSetPos(0x0104, -1310, 0, -7920, 90)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200111793V',
            (TxtCtl.SetColor, 0x5),
            '那么，接下来请杜南公爵\n',
            '为优胜小组送上祝福的讲话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200111794V',
            (TxtCtl.SetColor, 0x5),
            '代表，金·瓦赛克选手！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111795V',
            (TxtCtl.SetColor, 0x5),
            '请上前来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0108,
        (
            '#0080111796V#070F好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_95C0')
    def lambda_95C0():
        CameraMove(1860, 0, -6420, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_95C0)

    ChrWalkTo(0x0108, 930, 0, -6580, 1000, 0x00)
    ChrTurnDirection(0x0108, 0x0021, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0021,
        (
            '#0640111797V#223F#5P哦哦……\n',
            '走近了看还真是大块头啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111798V你们东方人都是这么大的体型吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111799V#070F#4P不，只是我自己特殊而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111800V从小的时候养成良好的饮食和作息习惯，\n',
            '经常锻炼，自然就成这样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111801V本性不会对事情深入考虑，\n',
            '所以只是体格变大了而已吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0640111802V#221F#5P哈哈哈，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111803V#220F嗯！\n',
            '我很欣赏你，金选手！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111804V现在给你颁发奖金１０万米拉\n',
            '和晚宴的邀请函！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111805V#074F#4P十分荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0021, 1900, 0, -6550, 1000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '晚宴请帖',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到奖金',
            (TxtCtl.SetColor, 0x4),
            '１０００００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddMira(50000)
    AddMira(50000)
    ChrMoveTo(0x0021, 2500, 0, -6550, 2000, 0x00)
    RemoveItem(0x0375, 1)
    RemoveItem(0x0372, 1)

    ChrTalk(
        0x0021,
        (
            '#0640111806V#220F#5P愿这位选手和他的同伴\n',
            '得到空之女神的祝福和光荣！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111807V#221F那么，各位亲爱的市民！\n',
            '请给优胜者最热烈的鼓掌和喝彩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    OP_28(0x0049, 0x01, 0x0020)
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 0, 0x3F8))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
