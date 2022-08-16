import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2400.x'
    header.mapIndex       = 97
    header.bgm            = 125
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C2400._SN', 'ED6_DT21/C2400_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT29/CH12120._CH', 'ED6_DT29/CH12120P._CP'),
        ('ED6_DT29/CH12121._CH', 'ED6_DT29/CH12121P._CP'),
        ('ED6_DT29/CH12260._CH', 'ED6_DT29/CH12260P._CP'),
        ('ED6_DT29/CH12261._CH', 'ED6_DT29/CH12261P._CP'),
        ('ED6_DT09/CH10530._CH', 'ED6_DT09/CH10530P._CP'),
        ('ED6_DT09/CH10531._CH', 'ED6_DT09/CH10531P._CP'),
        ('ED6_DT09/CH10540._CH', 'ED6_DT09/CH10540P._CP'),
        ('ED6_DT09/CH10541._CH', 'ED6_DT09/CH10541P._CP'),
        ('ED6_DT29/CH12480._CH', 'ED6_DT29/CH12480P._CP'),
        ('ED6_DT29/CH12481._CH', 'ED6_DT29/CH12481P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT26/CH20289._CH', 'ED6_DT26/CH20289P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT26/CH20254._CH', 'ED6_DT26/CH20254P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT26/CH20273._CH', 'ED6_DT26/CH20273P._CP'),
        ('ED6_DT26/CH20276._CH', 'ED6_DT26/CH20276P._CP'),
        ('ED6_DT27/CH04538._CH', 'ED6_DT27/CH04538P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT27/CH04532._CH', 'ED6_DT27/CH04532P._CP'),
        ('ED6_DT27/CH04530._CH', 'ED6_DT27/CH04530P._CP'),
        ('ED6_DT27/CH04531._CH', 'ED6_DT27/CH04531P._CP'),
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
        ('ED6_DT29/CH12122._CH', 'ED6_DT29/CH12122P._CP'),
        ('ED6_DT26/CH20278._CH', 'ED6_DT26/CH20278P._CP'),
        ('ED6_DT26/CH20275._CH', 'ED6_DT26/CH20275P._CP'),
        ('ED6_DT27/CH03000._CH', 'ED6_DT27/CH03000P._CP'),
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
    ]

# id: 0x10001 offset: 0x1F2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = -77650,
            z                   = 1000,
            y                   = -45450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 9260,
            z                   = 1000,
            y                   = -115060,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 87390,
            z                   = 1000,
            y                   = -64150,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = -285710,
            z                   = 1000,
            y                   = -116450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = -225060,
            z                   = 1000,
            y                   = -68690,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '霉菌雾',
            x                   = -288070,
            z                   = 0,
            y                   = -70170,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '怪盗布卢布兰',
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
            name                = '布卢布兰幻影',
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
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '曼·欧·诺斯',
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
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '福音中型',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '缝影用的针①',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01E4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '缝影用的针②',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01E4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '缝影用的针③',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01E4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '缝影用的针④',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01E4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '缝影用的针⑤',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01E4,
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
            name                = '艾丝蒂尔幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '约修亚幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雪拉幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奥利维尔幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科洛丝幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '金幻影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x552
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 140,
            z           = 0,
            y           = -26200,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -36720,
            z           = 0,
            y           = -32210,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -26310,
            z           = 0,
            y           = -61030,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0399,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -2870,
            z           = 0,
            y           = -84290,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 7900,
            z           = 0,
            y           = -51170,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 31140,
            z           = 0,
            y           = -44530,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0399,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 28370,
            z           = 0,
            y           = -63790,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -288370,
            z           = 0,
            y           = -48220,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0399,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -267560,
            z           = 0,
            y           = -24930,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -224930,
            z           = 0,
            y           = -62890,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -265230,
            z           = 0,
            y           = -1120,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -215420,
            z           = 0,
            y           = -1240,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0399,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -240970,
            z           = 0,
            y           = 21880,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -299360,
            z           = 0,
            y           = -20300,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x039C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -322950,
            z           = 0,
            y           = -22990,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0399,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x6F6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -282400,
            y           = -1000,
            z           = -79250,
            range       = -292410,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFEC08C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x716
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -48450,
            triggerZ            = 0,
            triggerY            = -100,
            triggerRange        = 1000,
            actorX              = -47750,
            actorZ              = 0,
            actorY              = -110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -26010,
            triggerZ            = 0,
            triggerY            = 580,
            triggerRange        = 1000,
            actorX              = -26070,
            actorZ              = 0,
            actorY              = 1270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 30880,
            triggerZ            = 0,
            triggerY            = 6510,
            triggerRange        = 1000,
            actorX              = 30960,
            actorZ              = 0,
            actorY              = 7200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -76860,
            triggerZ            = 0,
            triggerY            = -41820,
            triggerRange        = 1000,
            actorX              = -77670,
            actorZ              = 0,
            actorY              = -42070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -76860,
            triggerZ            = 0,
            triggerY            = -38850,
            triggerRange        = 1000,
            actorX              = -77550,
            actorZ              = 0,
            actorY              = -39020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -44430,
            triggerZ            = 0,
            triggerY            = -116030,
            triggerRange        = 1000,
            actorX              = -43740,
            actorZ              = 0,
            actorY              = -115970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -24880,
            triggerZ            = 0,
            triggerY            = -115770,
            triggerRange        = 1000,
            actorX              = -25600,
            actorZ              = 0,
            actorY              = -115990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 88610,
            triggerZ            = 0,
            triggerY            = -89500,
            triggerRange        = 1000,
            actorX              = 89330,
            actorZ              = 0,
            actorY              = -89530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -353240,
            triggerZ            = 0,
            triggerY            = 25560,
            triggerRange        = 1000,
            actorX              = -353040,
            actorZ              = 0,
            actorY              = 26220,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -320150,
            triggerZ            = 0,
            triggerY            = 26540,
            triggerRange        = 1000,
            actorX              = -320010,
            actorZ              = 0,
            actorY              = 27300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -354150,
            triggerZ            = 0,
            triggerY            = -5430,
            triggerRange        = 1000,
            actorX              = -353980,
            actorZ              = 0,
            actorY              = -4770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -341110,
            triggerZ            = 0,
            triggerY            = -47480,
            triggerRange        = 1000,
            actorX              = -341080,
            actorZ              = 0,
            actorY              = -46820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -313440,
            triggerZ            = 0,
            triggerY            = -83070,
            triggerRange        = 1000,
            actorX              = -312810,
            actorZ              = 0,
            actorY              = -83080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -197390,
            triggerZ            = 0,
            triggerY            = -67050,
            triggerRange        = 1000,
            actorX              = -196720,
            actorZ              = 0,
            actorY              = -67090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -76870,
            triggerZ            = 0,
            triggerY            = -45220,
            triggerRange        = 1000,
            actorX              = -77650,
            actorZ              = 0,
            actorY              = -45450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 8640,
            triggerZ            = 0,
            triggerY            = -115060,
            triggerRange        = 1000,
            actorX              = 9260,
            actorZ              = 0,
            actorY              = -115060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 86710,
            triggerZ            = 0,
            triggerY            = -64150,
            triggerRange        = 1000,
            actorX              = 87390,
            actorZ              = 0,
            actorY              = -64150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -286330,
            triggerZ            = 0,
            triggerY            = -116450,
            triggerRange        = 1000,
            actorX              = -285710,
            actorZ              = 0,
            actorY              = -116450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -224900,
            triggerZ            = 0,
            triggerY            = -67920,
            triggerRange        = 1000,
            actorX              = -225060,
            actorZ              = 0,
            actorY              = -68690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -263020,
            triggerZ            = 150,
            triggerY            = 92180,
            triggerRange        = 800,
            actorX              = -263020,
            actorZ              = 650,
            actorY              = 92180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3200,
            triggerZ            = 0,
            triggerY            = 30680,
            triggerRange        = 1200,
            actorX              = -3200,
            actorZ              = 1000,
            actorY              = 30680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -261769,
            triggerZ            = 0,
            triggerY            = 35590,
            triggerRange        = 1200,
            actorX              = -261769,
            actorZ              = 1000,
            actorY              = 35590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xA2E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 6, 0x12FE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A4C',
    )

    ChrSetPos(0x000D, -288070, 0, -70170, 180)
    ChrClearFlags(0x000D, 0x0080)

    def _loc_A4C(): pass

    label('loc_A4C')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_A5C'),
        (0x0000008F, 'loc_A70'),
        (-1, 'loc_A7F'),
    )

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 2, 0x122A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A6D',
    )

    MapSetFlags(0x10000000)
    Event(1, 0x0000)

    def _loc_A6D(): pass

    label('loc_A6D')

    Jump('loc_A7F')

    def _loc_A70(): pass

    label('loc_A70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A7C',
    )

    Event(1, 0x0001)

    def _loc_A7C(): pass

    label('loc_A7C')

    Jump('loc_A7F')

    def _loc_A7F(): pass

    label('loc_A7F')

    ExecExpressionWithValue(
        0x0013,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0xA91
@scena.Code('func_01_A91')
def func_01_A91():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_AA1',
    )

    OP_10(0x30, 0x00)
    OP_10(0x00, 0x01)

    Jump('loc_AA7')

    def _loc_AA1(): pass

    label('loc_AA1')

    OP_10(0x30, 0x01)
    OP_10(0x00, 0x00)

    def _loc_AA7(): pass

    label('loc_AA7')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x44C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ABC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_ABC(): pass

    label('loc_ABC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 2, 0x122A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_ADE',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 4500, 0, 28050, 270)

    def _loc_ADE(): pass

    label('loc_ADE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 0, 0x1320)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AF0',
    )

    OP_6F(0x0000, 0)

    Jump('loc_AF7')

    def _loc_AF0(): pass

    label('loc_AF0')

    OP_6F(0x0000, 60)

    def _loc_AF7(): pass

    label('loc_AF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 1, 0x1321)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B09',
    )

    OP_6F(0x0001, 0)

    Jump('loc_B10')

    def _loc_B09(): pass

    label('loc_B09')

    OP_6F(0x0001, 60)

    def _loc_B10(): pass

    label('loc_B10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 2, 0x1322)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B22',
    )

    OP_6F(0x0002, 0)

    Jump('loc_B29')

    def _loc_B22(): pass

    label('loc_B22')

    OP_6F(0x0002, 60)

    def _loc_B29(): pass

    label('loc_B29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 3, 0x1323)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B3B',
    )

    OP_6F(0x0003, 0)

    Jump('loc_B42')

    def _loc_B3B(): pass

    label('loc_B3B')

    OP_6F(0x0003, 60)

    def _loc_B42(): pass

    label('loc_B42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 4, 0x1324)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B54',
    )

    OP_6F(0x0004, 0)

    Jump('loc_B5B')

    def _loc_B54(): pass

    label('loc_B54')

    OP_6F(0x0004, 60)

    def _loc_B5B(): pass

    label('loc_B5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 5, 0x1325)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B6D',
    )

    OP_6F(0x0005, 0)

    Jump('loc_B74')

    def _loc_B6D(): pass

    label('loc_B6D')

    OP_6F(0x0005, 60)

    def _loc_B74(): pass

    label('loc_B74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 7, 0x1327)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B86',
    )

    OP_6F(0x0006, 0)

    Jump('loc_B8D')

    def _loc_B86(): pass

    label('loc_B86')

    OP_6F(0x0006, 60)

    def _loc_B8D(): pass

    label('loc_B8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 0, 0x1328)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B9F',
    )

    OP_6F(0x0007, 0)

    Jump('loc_BA6')

    def _loc_B9F(): pass

    label('loc_B9F')

    OP_6F(0x0007, 60)

    def _loc_BA6(): pass

    label('loc_BA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 1, 0x1329)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BB8',
    )

    OP_6F(0x0008, 0)

    Jump('loc_BBF')

    def _loc_BB8(): pass

    label('loc_BB8')

    OP_6F(0x0008, 60)

    def _loc_BBF(): pass

    label('loc_BBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 2, 0x132A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BD1',
    )

    OP_6F(0x0009, 0)

    Jump('loc_BD8')

    def _loc_BD1(): pass

    label('loc_BD1')

    OP_6F(0x0009, 60)

    def _loc_BD8(): pass

    label('loc_BD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 3, 0x132B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BEA',
    )

    OP_6F(0x000A, 0)

    Jump('loc_BF1')

    def _loc_BEA(): pass

    label('loc_BEA')

    OP_6F(0x000A, 60)

    def _loc_BF1(): pass

    label('loc_BF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 4, 0x132C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C03',
    )

    OP_6F(0x000B, 0)

    Jump('loc_C0A')

    def _loc_C03(): pass

    label('loc_C03')

    OP_6F(0x000B, 60)

    def _loc_C0A(): pass

    label('loc_C0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 5, 0x132D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C1C',
    )

    OP_6F(0x000C, 0)

    Jump('loc_C23')

    def _loc_C1C(): pass

    label('loc_C1C')

    OP_6F(0x000C, 60)

    def _loc_C23(): pass

    label('loc_C23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0267, 6, 0x133E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C35',
    )

    OP_6F(0x000D, 0)

    Jump('loc_C3C')

    def _loc_C35(): pass

    label('loc_C35')

    OP_6F(0x000D, 60)

    def _loc_C3C(): pass

    label('loc_C3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 0, 0x1330)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C4E',
    )

    OP_6F(0x000E, 0)

    Jump('loc_C55')

    def _loc_C4E(): pass

    label('loc_C4E')

    OP_6F(0x000E, 60)

    def _loc_C55(): pass

    label('loc_C55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 1, 0x1331)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C67',
    )

    OP_6F(0x000F, 0)

    Jump('loc_C6E')

    def _loc_C67(): pass

    label('loc_C67')

    OP_6F(0x000F, 60)

    def _loc_C6E(): pass

    label('loc_C6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 2, 0x1332)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C80',
    )

    OP_6F(0x0010, 0)

    Jump('loc_C87')

    def _loc_C80(): pass

    label('loc_C80')

    OP_6F(0x0010, 60)

    def _loc_C87(): pass

    label('loc_C87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 3, 0x1333)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C99',
    )

    OP_6F(0x0011, 0)

    Jump('loc_CA0')

    def _loc_C99(): pass

    label('loc_C99')

    OP_6F(0x0011, 60)

    def _loc_CA0(): pass

    label('loc_CA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 4, 0x1334)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB2',
    )

    OP_6F(0x0012, 0)

    Jump('loc_CB9')

    def _loc_CB2(): pass

    label('loc_CB2')

    OP_6F(0x0012, 60)

    def _loc_CB9(): pass

    label('loc_CB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_CC5',
    )

    OP_71(0x0015, 0x0004)

    def _loc_CC5(): pass

    label('loc_CC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_CD5',
    )

    OP_64(0x13, 0x0001)

    def _loc_CD5(): pass

    label('loc_CD5')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D73',
    )

    LoadEffect(0x02, 'map\\\\mp027_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, -3200, 1000, 30680, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x04, 'map\\\\mp027_00.eff')
    PlayEffect(0x04, 0x04, 0x00FF, -261769, 1000, 35590, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_D73(): pass

    label('loc_D73')

    Return()

# id: 0x0002 offset: 0xD74
@scena.Code('func_02_D74')
def func_02_D74():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D89',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_D74')

    def _loc_D89(): pass

    label('loc_D89')

    Return()

# id: 0x0003 offset: 0xD8A
@scena.Code('func_03_D8A')
def func_03_D8A():
    TalkBegin(0x000E)

    ChrTalk(
        0x000E,
        (
            '#0280211570V#150F如果找到什么\n',
            '请告诉我哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211571V我无论如何\n',
            '也想拍到幽灵哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0004 offset: 0xDEA
@scena.Code('func_04_DEA')
def func_04_DEA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 6, 0x12FE)),
            Expr.Return,
        ),
        'loc_DF2',
    )

    Return()

    def _loc_DF2(): pass

    label('loc_DF2')

    EventBegin(0x00)
    LoadEffect(0x00, 'monster\\msc0500.eff')
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 33)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 34)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 35)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 36)
    LoadChip('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP', 37)
    Fade(500)
    CameraMove(-287220, 0, -79900, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2220, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -288040, 0, -80880, 0)
    ChrSetPos(0x00F7, -287640, 0, -81990, 0)
    ChrSetPos(0x00F8, -289100, 0, -81800, 0)
    ChrSetPos(0x00F9, -288700, 0, -82730, 0)
    ChrClearFlags(0x000D, 0x0020)
    ChrSetChipByIndex(0x000D, 0)
    ChrSetSubChip(0x000D, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000D, 0, 500, 1500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    @scena.Lambda('lambda_0F29')
    def lambda_0F29():
        CameraMove(-287740, 0, -75300, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0F29)

    @scena.Lambda('lambda_0F41')
    def lambda_0F41():
        CameraSetDistance(2500, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_0F41)

    ChrSetChipByIndex(0x000D, 1)
    ChrSetSubChip(0x000D, 0)
    CreateThread(0x000D, 0x00, 0x00, func_02_D74)

    @scena.Lambda('lambda_0F62')
    def lambda_0F62():
        ChrMoveTo(0x00FE, -288070, 0, -73170, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F62)

    Sleep(1000)

    CreateThread(0x0101, 0x00, 0x00, func_05_1051)
    CreateThread(0x00F7, 0x00, 0x00, func_06_1081)
    CreateThread(0x00F8, 0x00, 0x00, func_07_10D9)
    CreateThread(0x00F9, 0x00, 0x00, func_08_1157)
    WaitForThreadExit(0x000D, 0x0001)
    TerminateThread(0x000D, 0x00)
    ChrSetChipByIndex(0x000D, 0)
    ChrSetSubChip(0x000D, 0)
    CreateThread(0x000D, 0x00, 0x00, func_02_D74)
    WaitForThreadExit(0x000D, 0x0002)
    Sleep(500)

    TerminateThread(0x000D, 0x00)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetChipByIndex(0x000D, 30)
    ChrSetSubChip(0x000D, 0)

    @scena.Lambda('lambda_0FD5')
    def lambda_0FD5():
        OP_99(0x00FE, 0x00, 0x01, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0FD5)

    Sleep(500)

    @scena.Lambda('lambda_0FEA')
    def lambda_0FEA():
        OP_99(0x00FE, 0x01, 0x05, 5000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0FEA)

    @scena.Lambda('lambda_0FFA')
    def lambda_0FFA():
        ChrMoveTo(0x00FE, -288070, 0, -77370, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0FFA)

    Sleep(250)

    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000D, 0x02)
    Battle(0x0000039D, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_103D'),
        (0x00000000, 'loc_1042'),
        (0x00000002, 'loc_1049'),
        (-1, 'loc_1050'),
    )

    def _loc_103D(): pass

    label('loc_103D')

    OP_B4(0x00)

    Jump('loc_1050')

    def _loc_1042(): pass

    label('loc_1042')

    Call(0, 0x0009)

    Jump('loc_1050')

    def _loc_1049(): pass

    label('loc_1049')

    Call(0, 0x000A)

    Jump('loc_1050')

    def _loc_1050(): pass

    label('loc_1050')

    Return()

# id: 0x0005 offset: 0x1051
@scena.Code('func_05_1051')
def func_05_1051():
    ChrSetChipByIndex(0x0101, 33)
    ChrSetSubChip(0x0101, 0)
    ChrWalkTo(0x00FE, -288070, 0, -77370, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetSubChip(0x0101, 0)

    Return()

# id: 0x0006 offset: 0x1081
@scena.Code('func_06_1081')
def func_06_1081():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1095',
    )

    ChrSetChipByIndex(0x0106, 35)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_109F')

    def _loc_1095(): pass

    label('loc_1095')

    ChrSetChipByIndex(0x0103, 34)
    ChrSetSubChip(0x0103, 0)

    def _loc_109F(): pass

    label('loc_109F')

    ChrWalkTo(0x00FE, -287250, 0, -78210, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_10CE',
    )

    ChrSetChipByIndex(0x0106, 15)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_10D8')

    def _loc_10CE(): pass

    label('loc_10CE')

    ChrSetChipByIndex(0x0103, 14)
    ChrSetSubChip(0x0103, 0)

    def _loc_10D8(): pass

    label('loc_10D8')

    Return()

# id: 0x0007 offset: 0x10D9
@scena.Code('func_07_10D9')
def func_07_10D9():
    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10F3',
    )

    ChrSetChipByIndex(0x0104, 36)
    ChrSetSubChip(0x0104, 0)

    Jump('loc_110A')

    def _loc_10F3(): pass

    label('loc_10F3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_110A',
    )

    ChrSetChipByIndex(0x0105, 37)
    ChrSetSubChip(0x0105, 0)

    def _loc_110A(): pass

    label('loc_110A')

    ChrWalkTo(0x00FE, -288990, 0, -78410, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_113F',
    )

    ChrSetChipByIndex(0x0104, 16)
    ChrSetSubChip(0x0104, 0)

    Jump('loc_1156')

    def _loc_113F(): pass

    label('loc_113F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1156',
    )

    ChrSetChipByIndex(0x0105, 17)
    ChrSetSubChip(0x0105, 0)

    def _loc_1156(): pass

    label('loc_1156')

    Return()

# id: 0x0008 offset: 0x1157
@scena.Code('func_08_1157')
def func_08_1157():
    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1171',
    )

    ChrSetChipByIndex(0x0104, 36)
    ChrSetSubChip(0x0104, 0)

    Jump('loc_1188')

    def _loc_1171(): pass

    label('loc_1171')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1188',
    )

    ChrSetChipByIndex(0x0105, 37)
    ChrSetSubChip(0x0105, 0)

    def _loc_1188(): pass

    label('loc_1188')

    ChrWalkTo(0x00FE, -288340, 0, -79340, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11BD',
    )

    ChrSetChipByIndex(0x0104, 16)
    ChrSetSubChip(0x0104, 0)

    Jump('loc_11D4')

    def _loc_11BD(): pass

    label('loc_11BD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D4',
    )

    ChrSetChipByIndex(0x0105, 17)
    ChrSetSubChip(0x0105, 0)

    def _loc_11D4(): pass

    label('loc_11D4')

    Return()

# id: 0x0009 offset: 0x11D5
@scena.Code('func_09_11D5')
def func_09_11D5():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x000D, 0x01)
    ChrSetFlags(0x000D, 0x0080)
    CameraMove(-288040, 0, -76800, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -288040, 0, -76800, 0)
    ChrSetPos(0x0001, -288040, 0, -76800, 0)
    ChrSetPos(0x0002, -288040, 0, -76800, 0)
    ChrSetPos(0x0003, -288040, 0, -76800, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetSubChip(0x00F7, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    SetScenaFlags(ScenaFlag(0x025F, 6, 0x12FE))
    OP_B2(0x00, 0x00, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x12AC
@scena.Code('func_0A_12AC')
def func_0A_12AC():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x000D, 0x01)
    ChrSetPos(0x000D, -288070, 0, -70170, 180)
    ChrClearFlags(0x000D, 0x0080)
    CameraMove(-288040, 0, -83520, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -288040, 0, -83520, 180)
    ChrSetPos(0x0001, -288040, 0, -83520, 180)
    ChrSetPos(0x0002, -288040, 0, -83520, 180)
    ChrSetPos(0x0003, -288040, 0, -83520, 180)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetSubChip(0x00F7, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x138C
@scena.Code('func_0B_138C')
def func_0B_138C():
    UnlockAchievement(0x02, 0x00A4, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 0, 0x1320)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1469',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1400',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0264, 0, 0x1320))

    Jump('loc_1466')

    def _loc_1400(): pass

    label('loc_1400')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_1466(): pass

    label('loc_1466')

    Jump('loc_149A')

    def _loc_1469(): pass

    label('loc_1469')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_149A(): pass

    label('loc_149A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x14A8
@scena.Code('func_0C_14A8')
def func_0C_14A8():
    UnlockAchievement(0x02, 0x00A5, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 1, 0x1321)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1585',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_151C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0264, 1, 0x1321))

    Jump('loc_1582')

    def _loc_151C(): pass

    label('loc_151C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_1582(): pass

    label('loc_1582')

    Jump('loc_15B6')

    def _loc_1585(): pass

    label('loc_1585')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_15B6(): pass

    label('loc_15B6')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000D offset: 0x15C4
@scena.Code('func_0D_15C4')
def func_0D_15C4():
    UnlockAchievement(0x02, 0x00A6, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 2, 0x1322)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16A1',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['刺弹枪Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_1638',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['刺弹枪Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0264, 2, 0x1322))

    Jump('loc_169E')

    def _loc_1638(): pass

    label('loc_1638')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['刺弹枪Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['刺弹枪Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_169E(): pass

    label('loc_169E')

    Jump('loc_16D2')

    def _loc_16A1(): pass

    label('loc_16A1')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_16D2(): pass

    label('loc_16D2')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x16E0
@scena.Code('func_0E_16E0')
def func_0E_16E0():
    UnlockAchievement(0x02, 0x00A7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 3, 0x1323)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17BD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_1754',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0264, 3, 0x1323))

    Jump('loc_17BA')

    def _loc_1754(): pass

    label('loc_1754')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_17BA(): pass

    label('loc_17BA')

    Jump('loc_17EE')

    def _loc_17BD(): pass

    label('loc_17BD')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_17EE(): pass

    label('loc_17EE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000F offset: 0x17FC
@scena.Code('func_0F_17FC')
def func_0F_17FC():
    UnlockAchievement(0x02, 0x00A8, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 4, 0x1324)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18D9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['魔防１'], 1)"),
            Expr.Return,
        ),
        'loc_1870',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['魔防１']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0264, 4, 0x1324))

    Jump('loc_18D6')

    def _loc_1870(): pass

    label('loc_1870')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['魔防１']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['魔防１']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_18D6(): pass

    label('loc_18D6')

    Jump('loc_190A')

    def _loc_18D9(): pass

    label('loc_18D9')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_190A(): pass

    label('loc_190A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0010 offset: 0x1918
@scena.Code('func_10_1918')
def func_10_1918():
    UnlockAchievement(0x02, 0x00A9, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 5, 0x1325)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AB0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 6, 0x1326)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19FC',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_196F')
    def lambda_196F():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_196F)

    @scena.Lambda('lambda_198A')
    def lambda_198A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_198A)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x0000039E, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_19D7'),
        (0x00000002, 'loc_19E9'),
        (0x00000001, 'loc_19F9'),
        (-1, 'loc_19FC'),
    )

    def _loc_19D7(): pass

    label('loc_19D7')

    SetScenaFlags(ScenaFlag(0x0264, 6, 0x1326))
    OP_6F(0x0005, 60)
    Sleep(500)

    Jump('loc_19FC')

    def _loc_19E9(): pass

    label('loc_19E9')

    OP_6F(0x0005, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_19F9(): pass

    label('loc_19F9')

    OP_B4(0x00)

    Return()

    def _loc_19FC(): pass

    label('loc_19FC')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['羽毛胸针'], 1)"),
            Expr.Return,
        ),
        'loc_1A4B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['羽毛胸针']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0264, 5, 0x1325))

    Jump('loc_1AAD')

    def _loc_1A4B(): pass

    label('loc_1A4B')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['羽毛胸针']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['羽毛胸针']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_1AAD(): pass

    label('loc_1AAD')

    Jump('loc_1ADF')

    def _loc_1AB0(): pass

    label('loc_1AB0')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1ADF(): pass

    label('loc_1ADF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0011 offset: 0x1AED
@scena.Code('func_11_1AED')
def func_11_1AED():
    UnlockAchievement(0x02, 0x00AA, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0264, 7, 0x1327)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BCA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_1B61',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0264, 7, 0x1327))

    Jump('loc_1BC7')

    def _loc_1B61(): pass

    label('loc_1B61')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_1BC7(): pass

    label('loc_1BC7')

    Jump('loc_1BFB')

    def _loc_1BCA(): pass

    label('loc_1BCA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1BFB(): pass

    label('loc_1BFB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0012 offset: 0x1C09
@scena.Code('func_12_1C09')
def func_12_1C09():
    UnlockAchievement(0x02, 0x00AB, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 0, 0x1328)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CE6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_1C7D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0265, 0, 0x1328))

    Jump('loc_1CE3')

    def _loc_1C7D(): pass

    label('loc_1C7D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_1CE3(): pass

    label('loc_1CE3')

    Jump('loc_1D17')

    def _loc_1CE6(): pass

    label('loc_1CE6')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1D17(): pass

    label('loc_1D17')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0013 offset: 0x1D25
@scena.Code('func_13_1D25')
def func_13_1D25():
    UnlockAchievement(0x02, 0x00AC, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 1, 0x1329)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E02',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['攻击２'], 1)"),
            Expr.Return,
        ),
        'loc_1D99',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['攻击２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0265, 1, 0x1329))

    Jump('loc_1DFF')

    def _loc_1D99(): pass

    label('loc_1D99')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['攻击２']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['攻击２']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_1DFF(): pass

    label('loc_1DFF')

    Jump('loc_1E33')

    def _loc_1E02(): pass

    label('loc_1E02')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1E33(): pass

    label('loc_1E33')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0014 offset: 0x1E41
@scena.Code('func_14_1E41')
def func_14_1E41():
    UnlockAchievement(0x02, 0x00AD, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 2, 0x132A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F1E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['杰尼丝西装'], 1)"),
            Expr.Return,
        ),
        'loc_1EB5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['杰尼丝西装']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0265, 2, 0x132A))

    Jump('loc_1F1B')

    def _loc_1EB5(): pass

    label('loc_1EB5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['杰尼丝西装']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['杰尼丝西装']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)

    def _loc_1F1B(): pass

    label('loc_1F1B')

    Jump('loc_1F4F')

    def _loc_1F1E(): pass

    label('loc_1F1E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1F4F(): pass

    label('loc_1F4F')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0015 offset: 0x1F5D
@scena.Code('func_15_1F5D')
def func_15_1F5D():
    UnlockAchievement(0x02, 0x00AE, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 3, 0x132B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_203A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000A, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1FD1',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0265, 3, 0x132B))

    Jump('loc_2037')

    def _loc_1FD1(): pass

    label('loc_1FD1')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0)

    def _loc_2037(): pass

    label('loc_2037')

    Jump('loc_206B')

    def _loc_203A(): pass

    label('loc_203A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_206B(): pass

    label('loc_206B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0016 offset: 0x2079
@scena.Code('func_16_2079')
def func_16_2079():
    UnlockAchievement(0x02, 0x00AF, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 4, 0x132C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2156',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_20ED',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0265, 4, 0x132C))

    Jump('loc_2153')

    def _loc_20ED(): pass

    label('loc_20ED')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0)

    def _loc_2153(): pass

    label('loc_2153')

    Jump('loc_2187')

    def _loc_2156(): pass

    label('loc_2156')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2187(): pass

    label('loc_2187')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0017 offset: 0x2195
@scena.Code('func_17_2195')
def func_17_2195():
    UnlockAchievement(0x02, 0x00B0, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0265, 5, 0x132D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2272',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_2209',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0265, 5, 0x132D))

    Jump('loc_226F')

    def _loc_2209(): pass

    label('loc_2209')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000C, 60)
    OP_70(0x000C, 0)

    def _loc_226F(): pass

    label('loc_226F')

    Jump('loc_22A3')

    def _loc_2272(): pass

    label('loc_2272')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_22A3(): pass

    label('loc_22A3')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0018 offset: 0x22B1
@scena.Code('func_18_22B1')
def func_18_22B1():
    UnlockAchievement(0x02, 0x00B1, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0267, 6, 0x133E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2449',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000D, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0267, 7, 0x133F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2395',
    )

    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x000B, 0x0000, 0)
    ChrMoveToRelativeAsync(0x000B, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_2308')
    def lambda_2308():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2308)

    @scena.Lambda('lambda_2323')
    def lambda_2323():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2323)

    ChrClearFlags(0x000B, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x0000039E, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x000B, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_2370'),
        (0x00000002, 'loc_2382'),
        (0x00000001, 'loc_2392'),
        (-1, 'loc_2395'),
    )

    def _loc_2370(): pass

    label('loc_2370')

    SetScenaFlags(ScenaFlag(0x0267, 7, 0x133F))
    OP_6F(0x000D, 60)
    Sleep(500)

    Jump('loc_2395')

    def _loc_2382(): pass

    label('loc_2382')

    OP_6F(0x000D, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_2392(): pass

    label('loc_2392')

    OP_B4(0x00)

    Return()

    def _loc_2395(): pass

    label('loc_2395')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['驱动２'], 1)"),
            Expr.Return,
        ),
        'loc_23E4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['驱动２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0267, 6, 0x133E))

    Jump('loc_2446')

    def _loc_23E4(): pass

    label('loc_23E4')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['驱动２']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['驱动２']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000D, 60)
    OP_70(0x000D, 0)

    def _loc_2446(): pass

    label('loc_2446')

    Jump('loc_2478')

    def _loc_2449(): pass

    label('loc_2449')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2478(): pass

    label('loc_2478')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0019 offset: 0x2486
@scena.Code('func_19_2486')
def func_19_2486():
    UnlockAchievement(0x02, 0x00B2, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 0, 0x1330)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2563',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000E, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂粉'], 1)"),
            Expr.Return,
        ),
        'loc_24FA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0266, 0, 0x1330))

    Jump('loc_2560')

    def _loc_24FA(): pass

    label('loc_24FA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000E, 60)
    OP_70(0x000E, 0)

    def _loc_2560(): pass

    label('loc_2560')

    Jump('loc_2594')

    def _loc_2563(): pass

    label('loc_2563')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2594(): pass

    label('loc_2594')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x001A offset: 0x25A2
@scena.Code('func_1A_25A2')
def func_1A_25A2():
    UnlockAchievement(0x02, 0x00B3, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 1, 0x1331)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_267F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000F, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_2616',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0266, 1, 0x1331))

    Jump('loc_267C')

    def _loc_2616(): pass

    label('loc_2616')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0)

    def _loc_267C(): pass

    label('loc_267C')

    Jump('loc_26B0')

    def _loc_267F(): pass

    label('loc_267F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_26B0(): pass

    label('loc_26B0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x001B offset: 0x26BE
@scena.Code('func_1B_26BE')
def func_1B_26BE():
    UnlockAchievement(0x02, 0x00B4, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 2, 0x1332)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_279B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0010, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_2732',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0266, 2, 0x1332))

    Jump('loc_2798')

    def _loc_2732(): pass

    label('loc_2732')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0010, 60)
    OP_70(0x0010, 0)

    def _loc_2798(): pass

    label('loc_2798')

    Jump('loc_27CC')

    def _loc_279B(): pass

    label('loc_279B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_27CC(): pass

    label('loc_27CC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x001C offset: 0x27DA
@scena.Code('func_1C_27DA')
def func_1C_27DA():
    UnlockAchievement(0x02, 0x00B5, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 3, 0x1333)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28B7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0011, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['薄底船鞋'], 1)"),
            Expr.Return,
        ),
        'loc_284E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['薄底船鞋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0266, 3, 0x1333))

    Jump('loc_28B4')

    def _loc_284E(): pass

    label('loc_284E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['薄底船鞋']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['薄底船鞋']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0011, 60)
    OP_70(0x0011, 0)

    def _loc_28B4(): pass

    label('loc_28B4')

    Jump('loc_28E8')

    def _loc_28B7(): pass

    label('loc_28B7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_28E8(): pass

    label('loc_28E8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x001D offset: 0x28F6
@scena.Code('func_1D_28F6')
def func_1D_28F6():
    UnlockAchievement(0x02, 0x00B6, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0266, 4, 0x1334)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29D3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0012, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_296A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0266, 4, 0x1334))

    Jump('loc_29D0')

    def _loc_296A(): pass

    label('loc_296A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0012, 60)
    OP_70(0x0012, 0)

    def _loc_29D0(): pass

    label('loc_29D0')

    Jump('loc_2A04')

    def _loc_29D3(): pass

    label('loc_29D3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_2A04(): pass

    label('loc_2A04')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x001E offset: 0x2A12
@scena.Code('func_1E_2A12')
def func_1E_2A12():
    TalkBegin(0x00FF)
    Sleep(500)

    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '有空间投影装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【按右边的按钮】\n'),
            TXT(0x01, '【按中央的按钮】\n'),
            TXT(0x02, '【按左边的按钮】\n'),
            TXT(0x03, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E75',
    )

    Sleep(500)

    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp088_00.eff')
    PlayEffect(0x01, 0x00, 0x00FF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B6C',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x001B, 0x0001)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 170, 0)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, -263000, 500, 89640, 180)
    CreateThread(0x001B, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x001B, 0x0040)
    OP_0D()

    Jump('loc_2E72')

    def _loc_2B6C(): pass

    label('loc_2B6C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BDB',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x001C, 0x0001)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 170, 0)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, -263000, 500, 89640, 180)
    CreateThread(0x001C, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x001C, 0x0040)
    OP_0D()

    Jump('loc_2E72')

    def _loc_2BDB(): pass

    label('loc_2BDB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C4A',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x001D, 0x0001)
    ChrSetRGBAMask(0x001D, 255, 255, 255, 170, 0)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, -263000, 500, 89640, 180)
    CreateThread(0x001D, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x001D, 0x0040)
    OP_0D()

    Jump('loc_2E72')

    def _loc_2C4A(): pass

    label('loc_2C4A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CB9',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x001E, 0x0001)
    ChrSetRGBAMask(0x001E, 255, 255, 255, 170, 0)
    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x001E, -263000, 500, 89640, 180)
    CreateThread(0x001E, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x001E, 0x0040)
    OP_0D()

    Jump('loc_2E72')

    def _loc_2CB9(): pass

    label('loc_2CB9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D28',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x001F, 0x0001)
    ChrSetRGBAMask(0x001F, 255, 255, 255, 170, 0)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, -263000, 500, 89640, 180)
    CreateThread(0x001F, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x001F, 0x0040)
    OP_0D()

    Jump('loc_2E72')

    def _loc_2D28(): pass

    label('loc_2D28')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D97',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x0020, 0x0001)
    ChrSetRGBAMask(0x0020, 255, 255, 255, 170, 0)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x0020, -263000, 500, 89640, 180)
    CreateThread(0x0020, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x0020, 0x0040)
    OP_0D()

    Jump('loc_2E72')

    def _loc_2D97(): pass

    label('loc_2D97')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E06',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x0021, 0x0001)
    ChrSetRGBAMask(0x0021, 255, 255, 255, 170, 0)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x0021, -263000, 500, 89640, 180)
    CreateThread(0x0021, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x0021, 0x0040)
    OP_0D()

    Jump('loc_2E72')

    def _loc_2E06(): pass

    label('loc_2E06')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E72',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetRGBAMask(0x0022, 255, 255, 255, 170, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrSetPos(0x0022, -263000, 500, 89640, 180)
    CreateThread(0x0022, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x0022, 0x0040)
    OP_0D()

    def _loc_2E72(): pass

    label('loc_2E72')

    Jump('loc_2FA3')

    def _loc_2E75(): pass

    label('loc_2E75')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F47',
    )

    Sleep(500)

    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp088_00.eff')
    PlayEffect(0x01, 0x00, 0x00FF, -263120, 80, 93290, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 170, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -263000, 500, 89640, 180)
    CreateThread(0x0010, 0x01, 0x01, func_0C_14A8)
    ChrSetFlags(0x0010, 0x0040)
    OP_0D()

    Jump('loc_2FA3')

    def _loc_2F47(): pass

    label('loc_2F47')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F96',
    )

    Sleep(500)

    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    StopEffect(0x00, 0x02)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)

    Jump('loc_2FA3')

    def _loc_2F96(): pass

    label('loc_2F96')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FA3',
    )

    def _loc_2FA3(): pass

    label('loc_2FA3')

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x001F offset: 0x2FB0
@scena.Code('func_1F_2FB0')
def func_1F_2FB0():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3001',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_31BC')

    def _loc_3001(): pass

    label('loc_3001')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
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
            TXT(0x00, '在这里休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31A1',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x02, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, -3200, 1000, 30680, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0016, 0)
    OP_70(0x0016, 50)
    OP_73(0x0016)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x03, 'map\\\\mp027_01.eff')
    PlayEffect(0x03, 0x03, 0x00FF, -3200, 1000, 30680, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x03, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, -3200, 1000, 30680, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0016, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_31A1(): pass

    label('loc_31A1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31BB',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_31BB(): pass

    label('loc_31BB')

    Return()

    def _loc_31BC(): pass

    label('loc_31BC')

    Return()

# id: 0x0020 offset: 0x31BD
@scena.Code('func_20_31BD')
def func_20_31BD():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_320E',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_33C9')

    def _loc_320E(): pass

    label('loc_320E')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
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
            TXT(0x00, '在这里休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33AE',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x04, 0x02)
    PlayEffect(0x04, 0x04, 0x00FF, -261769, 1000, 35590, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0017, 0)
    OP_70(0x0017, 50)
    OP_73(0x0017)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x04, 0x02)
    LoadEffect(0x05, 'map\\\\mp027_01.eff')
    PlayEffect(0x05, 0x05, 0x00FF, -261769, 1000, 35590, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x05, 0x02)
    PlayEffect(0x04, 0x04, 0x00FF, -261769, 1000, 35590, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0017, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_33AE(): pass

    label('loc_33AE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33C8',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_33C8(): pass

    label('loc_33C8')

    Return()

    def _loc_33C9(): pass

    label('loc_33C9')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
