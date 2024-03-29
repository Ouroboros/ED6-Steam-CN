import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0031_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0031   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0030.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
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
        ('ED6_DT07/CH00000._CH', 'ED6_DT07/CH00000P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02190._CH', 'ED6_DT07/CH02190P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH02210._CH', 'ED6_DT07/CH02210P._CP'),
        ('ED6_DT07/CH02220._CH', 'ED6_DT07/CH02220P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02250._CH', 'ED6_DT07/CH02250P._CP'),
        ('ED6_DT07/CH02260._CH', 'ED6_DT07/CH02260P._CP'),
        ('ED6_DT07/CH02270._CH', 'ED6_DT07/CH02270P._CP'),
        ('ED6_DT07/CH02280._CH', 'ED6_DT07/CH02280P._CP'),
        ('ED6_DT07/CH02290._CH', 'ED6_DT07/CH02290P._CP'),
        ('ED6_DT07/CH02300._CH', 'ED6_DT07/CH02300P._CP'),
        ('ED6_DT07/CH02310._CH', 'ED6_DT07/CH02310P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02330._CH', 'ED6_DT07/CH02330P._CP'),
        ('ED6_DT07/CH02340._CH', 'ED6_DT07/CH02340P._CP'),
    ]

# id: 0x10001 offset: 0x1E2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = 'CH00000艾丝蒂尔',
            x                   = 4000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = 'CH00010约修亚',
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = 'CH00020雪拉',
            x                   = 4000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = 'CH00030奥利维尔',
            x                   = 4000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = 'CH00040科洛丝',
            x                   = 4000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '表情',
            x                   = 4000,
            z                   = 0,
            y                   = 15000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0030,
        ),
        ScenaNpcData(
            name                = 'CH00050阿加特',
            x                   = 8000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = 'CH00060提妲',
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = 'CH00070金',
            x                   = 8000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = 'CH02000卡西乌斯老爸',
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = 'CH02010艾莉茜雅女王',
            x                   = 8000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = 'CH02020Ｄｒ．拉赛尔',
            x                   = 12000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = 'CH02030理查德上校',
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = 'CH02040莱维',
            x                   = 12000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = 'CH02050亚鲁瓦教授（怀斯曼）',
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = 'CH02060记者奈尔',
            x                   = 12000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = 'CH02070摄影师朵洛希',
            x                   = 16000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = 'CH02080摩尔根将军',
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = 'CH02090亲卫队尤莉亚',
            x                   = 16000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = 'CH02100原特务兵凯诺娜队长',
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = 'CH02110空贼团长男多伦',
            x                   = 16000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = 'CH02120空贼团次男吉尔',
            x                   = 20000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = 'CH02130空贼团妹乔丝特',
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = 'CH02140杜南公爵',
            x                   = 20000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = 'CH02190穆拉',
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            name                = 'CH02200洛伦斯',
            x                   = 20000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            name                = 'CH02210艾丝蒂尔１１岁',
            x                   = 24000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = 'CH02220约修亚１１岁',
            x                   = 24000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = 'CH02230女佣艾丝蒂尔',
            x                   = 24000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            name                = 'CH02240女佣约修亚',
            x                   = 24000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            name                = 'CH02260骑士艾丝蒂尔',
            x                   = 28000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            name                = 'CH02270骑士科洛丝',
            x                   = 28000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            name                = 'CH02280公主约修亚',
            x                   = 28000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            name                = 'CH02290温泉约修亚',
            x                   = 28000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            name                = 'CH02300温泉艾丝蒂尔',
            x                   = 28000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            name                = 'CH02310温泉提妲',
            x                   = 32000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            name                = 'CH02320基库',
            x                   = 32000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = 'CH02330学生乔丝特',
            x                   = 32000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002E,
        ),
        ScenaNpcData(
            name                = 'CH02340公主科洛丝',
            x                   = 32000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002F,
        ),
    )

# id: 0x10002 offset: 0x6C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x6C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x6C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x6C2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x6C3
@scena.Code('func_01_6C3')
def func_01_6C3():
    Return()

# id: 0x0002 offset: 0x6C4
@scena.Code('func_02_6C4')
def func_02_6C4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6D9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_6C4')

    def _loc_6D9(): pass

    label('loc_6D9')

    Return()

# id: 0x0003 offset: 0x6DA
@scena.Code('func_03_6DA')
def func_03_6DA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6EF',
    )

    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('func_03_6DA')

    def _loc_6EF(): pass

    label('loc_6EF')

    Return()

# id: 0x0004 offset: 0x6F0
@scena.Code('func_04_6F0')
def func_04_6F0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_705',
    )

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('func_04_6F0')

    def _loc_705(): pass

    label('loc_705')

    Return()

# id: 0x0005 offset: 0x706
@scena.Code('func_05_706')
def func_05_706():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_729',
    )

    OP_8D(0x00FE, 4000, 20000, 24000, 30000, 1500)

    Jump('func_05_706')

    def _loc_729(): pass

    label('loc_729')

    Return()

# id: 0x0006 offset: 0x72A
@scena.Code('func_06_72A')
def func_06_72A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_74D',
    )

    OP_8D(0x00FE, 22000, 20000, 42000, 30000, 1500)

    Jump('func_06_72A')

    def _loc_74D(): pass

    label('loc_74D')

    Return()

# id: 0x0007 offset: 0x74E
@scena.Code('func_07_74E')
def func_07_74E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呜喵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x761
@scena.Code('func_08_761')
def func_08_761():
    TalkBegin(0x00FE)
    PlayBGM(4)

    ChrTalk(
        0x00FE,
        (
            'ＢＧＭ改变喵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x77E
@scena.Code('func_09_77E')
def func_09_77E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            'ＢＧＭ降低喵。',
            TxtCtl.Enter,
        ),
    )

    OP_1F(0x5A, 0x000007D0)
    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ＢＧＭ更降低喵。',
            TxtCtl.Enter,
        ),
    )

    OP_1F(0x46, 0x000007D0)
    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ＢＧＭ回复原状喵。',
            TxtCtl.Enter,
        ),
    )

    OP_1F(0x64, 0x000007D0)
    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x7D9
@scena.Code('func_0A_7D9')
def func_0A_7D9():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#000F通常１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#001F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#002F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#003F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#004F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#005F发怒１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#006F通常２（自信）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#007F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#008F害羞',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#009F发怒２（唔）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#500F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#501F悠闲',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#502F哼哼',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#503F害羞２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#504F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#505F嗯～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#506F苦笑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#507F挑拨',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#508F笑容２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#509F眯缝眼',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x928
@scena.Code('func_0B_928')
def func_0B_928():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#010F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#011F笑容１（有企图）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#012F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#013F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#014F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#015F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#016F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#017F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#018F害羞（发牢骚）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#019F笑容２（发怒）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#510F杀意',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#511F真的害羞',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#512F笑容３',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#513F苦痛',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#514F暗示解除',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#515F暗示解除后叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#516F暗示解除后发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#517FED笑容４',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#518FED通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#519FED低头',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#590FED低头惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#591F暗示解除后叫喊２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#592FED笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#593FED瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0xAF3
@scena.Code('func_0C_AF3')
def func_0C_AF3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#020F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#021F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#022F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#023F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#024F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#025F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#026F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#027F诱惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#028F喝醉（好心情）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#029F喝醉（不高兴）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0xBA4
@scena.Code('func_0D_BA4')
def func_0D_BA4():
    TalkBegin(0x00FE)
    OP_62(0x000B, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)

    ChrTalk(
        0x00FE,
        (
            '#030F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#031F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#032F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#033F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#034F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#035F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#036F慌张',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#037F喝醉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#038F烂醉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000B)
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0xC47
@scena.Code('func_0E_C47')
def func_0E_C47():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#040F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#041F笑容１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#042F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#043F悲哀１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#044F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#045F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#046F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#047F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#048F笑容２（小姐ver）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#049F悲哀２（深刻）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0xCFF
@scena.Code('func_0F_CFF')
def func_0F_CFF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#050F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#051F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#052F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#053F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#054F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#055F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#056F痛',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#057F杀意',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#058F毒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#059F苦痛',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#550F可恶～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#551F笑容２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#552F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0xDCB
@scena.Code('func_10_DCB')
def func_10_DCB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#060F通常１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#061F笑容１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#062F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#063F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#064F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#065F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#066F笑容２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#067F害羞',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#068F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#069F哭泣',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#560F通常２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#561F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0xE8E
@scena.Code('func_11_E8E')
def func_11_E8E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#070F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#071F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#072F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#073F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#074F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0xEE0
@scena.Code('func_12_EE0')
def func_12_EE0():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#080F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#081F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#082F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#083F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#084F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#085F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#086F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0xF50
@scena.Code('func_13_F50')
def func_13_F50():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#090F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#091F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#092F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#093F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#094F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0xFA2
@scena.Code('func_14_FA2')
def func_14_FA2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#100F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#101F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#102F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#103F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#104F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#105F笑容2',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x1004
@scena.Code('func_15_1004')
def func_15_1004():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#110F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#111F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#112F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#113F惊讶',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#114F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#115F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x1065
@scena.Code('func_16_1065')
def func_16_1065():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#120F通常１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#121F通常２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#122F回头',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#123F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#124F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#280F洛伦斯版本通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#281F洛伦斯版本合口',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#282F洛伦斯（没见过）通常１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#283F洛伦斯（没见过）通常２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#284F洛伦斯（没见过）笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#285F洛伦斯（没见过）闭目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x116D
@scena.Code('func_17_116D')
def func_17_116D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#130F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#131F慌张',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#132F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#133FED用通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#134FED用笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#135FED用认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#136FED用瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x11ED
@scena.Code('func_18_11ED')
def func_18_11ED():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#140F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#141F笑容１（诡笑）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#142F怀疑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#143F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#144F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#145F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#146F喝醉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#147F笑容２（满面）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x1280
@scena.Code('func_19_1280')
def func_19_1280():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#150F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#151F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#152F呜呜',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#153F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#154F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x12D2
@scena.Code('func_1A_12D2')
def func_1A_12D2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#160F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#161F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#162F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#163F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x1315
@scena.Code('func_1B_1315')
def func_1B_1315():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#170F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#171F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#172F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#173F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#174F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#175F忧郁',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#176F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x1385
@scena.Code('func_1C_1385')
def func_1C_1385():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#180F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#181F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#182F通常２（温柔）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x13C3
@scena.Code('func_1D_13C3')
def func_1D_13C3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#190F通常（正常）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#191F笑容（正常）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#192F惊愕（正常）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#193F通常（发狂）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#194F笑容（发狂）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#195F发怒（发狂）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x1454
@scena.Code('func_1E_1454')
def func_1E_1454():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#200F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#201F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x1479
@scena.Code('func_1F_1479')
def func_1F_1479():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#210F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#211F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#212F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#213F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#214F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#215F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#216F慌张',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#217F变装通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#218F变装笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#219F变装空贼表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#410F变装白痴笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x153D
@scena.Code('func_20_153D')
def func_20_153D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#290F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#291F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#292F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#293F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#294F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x158F
@scena.Code('func_21_158F')
def func_21_158F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#300F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#301F无表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#302F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#303F痛',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#304F波澜不惊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#305F寝颜',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#306F寝颜（醒来）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x160B
@scena.Code('func_22_160B')
def func_22_160B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#220F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#221F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#222F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#223F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#224F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#225F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#226F慌张',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#227F喝醉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#228F气绝',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x1699
@scena.Code('func_23_1699')
def func_23_1699():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#310F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#311F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x16BE
@scena.Code('func_24_16BE')
def func_24_16BE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#270F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#271F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#272F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x16F2
@scena.Code('func_25_16F2')
def func_25_16F2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#280F洛伦斯版本',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0x170E
@scena.Code('func_26_170E')
def func_26_170E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#320F通常1（优先）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#321F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#322F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#323F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#324F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#325F通常2（自信）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#326F发怒２（唔）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0x1798
@scena.Code('func_27_1798')
def func_27_1798():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#330F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#331F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#332F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#333F害羞',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#334F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0x17EA
@scena.Code('func_28_17EA')
def func_28_17EA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#340F通常（悠闲）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#341F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#342F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#343F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#344F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#345F发怒１（叫喊）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#346F通常（自信）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#347F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#348F害羞',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#349F发怒２（唔）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#840F戏剧用通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#841F戏剧用认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#842F戏剧用惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#843F戏剧用叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#844F戏剧用瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0x1912
@scena.Code('func_29_1912')
def func_29_1912():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#350F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#351F笑容１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#352F认真·戏剧用通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#353F悲哀１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#354F惊愕·戏剧用',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#355F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#356F发怒·戏剧用',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#357F瞑目·戏剧用',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#358F笑容２（小姐ver）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#359F悲哀２（深刻）·戏剧用',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#850F戏剧用苦痛',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0x1A0B
@scena.Code('func_2A_1A0B')
def func_2A_1A0B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#360F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#361F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#362F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#363F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#364F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#365F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#366F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#367F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#368F害羞（发牢骚）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002B offset: 0x1AA3
@scena.Code('func_2B_1AA3')
def func_2B_1AA3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#370F通常１（悠闲）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#371F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#372F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#373F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#374F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#375F发怒１（叫喊）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#376F通常２（自信）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#377F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#378F害羞',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#379F发怒２（唔）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#440F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#441F赤面',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002C offset: 0x1B84
@scena.Code('func_2C_1B84')
def func_2C_1B84():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#380F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#381F笑容１（有企图）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#382F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#383F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#384F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#385F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#386F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#387F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#388F害羞（发牢骚）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#389F笑容２（发怒）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002D offset: 0x1C41
@scena.Code('func_2D_1C41')
def func_2D_1C41():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#390F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#391F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#392F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#393F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#394F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#395F害羞',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#396F通常２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002E offset: 0x1CB3
@scena.Code('func_2E_1CB3')
def func_2E_1CB3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#217F变装通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#218F变装笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#219F变装空贼表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#410F变装白痴笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002F offset: 0x1D0E
@scena.Code('func_2F_1D0E')
def func_2F_1D0E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#400F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#401F笑容（小姐ver）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#402F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#403F悲哀１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#404F悲哀２（深刻）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#405F嘿嘿',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#406F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#407F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0030 offset: 0x1DA4
@scena.Code('func_30_1DA4')
def func_30_1DA4():
    TalkBegin(0x00FE)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DB1(): pass

    label('loc_1DB1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22E7',
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
        10,
        1,
        (
            TXT(0x00, '表情测试\n'),
            TXT(0x01, '假名显示测试\n'),
            TXT(0x02, '音量测试\n'),
            TXT(0x03, '取消\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E18'),
        (0x00000001, 'loc_2101'),
        (0x00000002, 'loc_2280'),
        (-1, 'loc_22D7'),
    )

    def _loc_1E18(): pass

    label('loc_1E18')

    OP_62(0x000D, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F生气',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F焦躁',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F冷汗',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F脸色发青',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)
    OP_62(0x000D, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020FＺｚｚ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)
    OP_62(0x000D, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F闪烁',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F哈哈',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F啪',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F汗汗',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F哐当！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 1900, 0x30, 0x32, 0x00000096, 0x00)
    PlaySE(48, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F气绝',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)
    OP_62(0x000D, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F闪闪',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)
    OP_62(0x000D, 0x00000000, 1900, 0x33, 0x35, 0x000000C8, 0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F咕噜咕噜',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)
    OP_62(0x000D, 0x00000000, 2000, 0x3B, 0x3C, 0x000000FA, 0x02)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F搭话',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x3D, 0x3E, 0x000000FA, 0x02)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#020F钓鱼点',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E4')

    def _loc_2101(): pass

    label('loc_2101')

    ChrTalk(
        0x00FE,
        (
            '#040F假名测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#040F导力器。游击士。\n',
            '开拓时代的物语。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#040F导力引擎、导力炮（←文中限定）。\n',
            '游击士协会、七耀石、噬身之蛇。\n',
            '七至宝、『七至宝』、七 至 宝（←保留中）。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#040F『银闪之雪拉扎德』、女神。\n',
            '养父、王都格兰赛尔（←文中限定）。\n',
            '导力魔法、結晶回路、翠耀石。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#040F将文中限定使用在文首就会发生类似以下悲剧。\n',
            '王都（←文中限定）。\n',
            '导力炮（←文中限定）。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E4')

    def _loc_2280(): pass

    label('loc_2280')

    ChrTalk(
        0x00FE,
        (
            'ＢＧＭ降低喵。',
            TxtCtl.Enter,
        ),
    )

    OP_1F(0x5A, 0x000007D0)
    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ＢＧＭ更降低喵。',
            TxtCtl.Enter,
        ),
    )

    OP_1F(0x46, 0x000007D0)
    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ＢＧＭ回复原状喵。',
            TxtCtl.Enter,
        ),
    )

    OP_1F(0x64, 0x000007D0)
    CloseMessageWindow()

    Jump('loc_22E4')

    def _loc_22D7(): pass

    label('loc_22D7')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22E4')

    def _loc_22E4(): pass

    label('loc_22E4')

    Jump('loc_1DB1')

    def _loc_22E7(): pass

    label('loc_22E7')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
