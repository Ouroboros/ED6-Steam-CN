import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特蕾莎院长'),
    TXT(0x02, '克拉姆'),
    TXT(0x03, '波利'),
    TXT(0x04, '玛丽'),
    TXT(0x05, '达尼艾尔'),
    TXT(0x06, '克鲁茨'),
    TXT(0x07, '亚妮拉丝'),
    TXT(0x08, '库拉茨'),
    TXT(0x09, '卡露娜'),
    TXT(0x0A, '王国军士兵'),
    TXT(0x0B, '王国军士兵'),
    TXT(0x0C, '王国军士兵'),
    TXT(0x0D, '装甲猎豹'),
    TXT(0x0E, '装甲猎豹'),
    TXT(0x0F, '装甲猎豹'),
    TXT(0x10, '装甲猎豹'),
    TXT(0x11, '装甲猎豹'),
    TXT(0x12, '装甲猎豹'),
    TXT(0x13, '装甲猎豹'),
    TXT(0x14, '装甲猎豹'),
    TXT(0x15, '装甲猎豹'),
    TXT(0x16, '装甲猎豹'),
    TXT(0x17, '目标用照相机'),
    TXT(0x18, '目标'),
    TXT(0x19, '目标'),
    TXT(0x1A, '目标'),
    TXT(0x1B, '目标'),
    TXT(0x1C, '玛诺利亚村方向'),
    TXT(0x1D, '玛西亚孤儿院方向'),
    TXT(0x1E, '卢安方向'),
    TXT(0x1F, ''),
    TXT(0x20, ''),
    TXT(0x21, ''),
    TXT(0x22, ''),
    TXT(0x23, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2200.x'
    header.mapIndex       = 101
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4465
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
        ('ED6_DT29/CH12100._CH', 'ED6_DT29/CH12100P._CP'),
        ('ED6_DT29/CH12101._CH', 'ED6_DT29/CH12101P._CP'),
        ('ED6_DT29/CH12150._CH', 'ED6_DT29/CH12150P._CP'),
        ('ED6_DT29/CH12151._CH', 'ED6_DT29/CH12151P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH00412._CH', 'ED6_DT07/CH00412P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00390._CH', 'ED6_DT07/CH00390P._CP'),
        ('ED6_DT07/CH00400._CH', 'ED6_DT07/CH00400P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT29/CH12330._CH', 'ED6_DT29/CH12330P._CP'),
        ('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP'),
        ('ED6_DT07/CH00412._CH', 'ED6_DT07/CH00412P._CP'),
        ('ED6_DT07/CH00415._CH', 'ED6_DT07/CH00415P._CP'),
        ('ED6_DT07/CH00416._CH', 'ED6_DT07/CH00416P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT07/CH00422._CH', 'ED6_DT07/CH00422P._CP'),
        ('ED6_DT07/CH00391._CH', 'ED6_DT07/CH00391P._CP'),
        ('ED6_DT07/CH00392._CH', 'ED6_DT07/CH00392P._CP'),
        ('ED6_DT07/CH00401._CH', 'ED6_DT07/CH00401P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT07/CH00326._CH', 'ED6_DT07/CH00326P._CP'),
        ('ED6_DT29/CH12331._CH', 'ED6_DT29/CH12331P._CP'),
        ('ED6_DT29/CH12333._CH', 'ED6_DT29/CH12333P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
    ]

# id: 0x10002 offset: 0x1BA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
            x                   = -139370,
            z                   = -2020,
            y                   = 15120,
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
            x                   = -28630,
            z                   = -1990,
            y                   = 79340,
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
            x                   = 7410,
            z                   = -2000,
            y                   = 29980,
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

# id: 0x10003 offset: 0x57A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -96260,
            z           = -1950,
            y           = 27960,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0184,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -104740,
            z           = -5970,
            y           = 11000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -81100,
            z           = -5870,
            y           = 13330,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -88220,
            z           = -5960,
            y           = 9810,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x5EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x5EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -114230,
            triggerZ            = -6050,
            triggerY            = 11770,
            triggerRange        = 1000,
            actorX              = -114730,
            actorZ              = -6040,
            actorY              = 12270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -77980,
            triggerZ            = -6870,
            triggerY            = -11780,
            triggerRange        = 1000,
            actorX              = -77540,
            actorZ              = -6730,
            actorY              = -11140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -21830,
            triggerZ            = -2000,
            triggerY            = 37790,
            triggerRange        = 1500,
            actorX              = -21830,
            actorZ              = -800,
            actorY              = 37790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0030,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18840,
            triggerZ            = -2000,
            triggerY            = 33860,
            triggerRange        = 1500,
            actorX              = -18840,
            actorZ              = -500,
            actorY              = 33860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0031,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x67A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_690',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0006)

    Jump('loc_6D8')

    def _loc_690(): pass

    label('loc_690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_6AF',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x29),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0007)

    Jump('loc_6D8')

    def _loc_6AF(): pass

    label('loc_6AF')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_6BB'),
        (-1, 'loc_6D8'),
    )

    def _loc_6BB(): pass

    label('loc_6BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 7, 0x1217)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D5',
    )

    ClearMapFlags(0x00000010)
    SetMapFlags(0x10000000)
    Event(0, 0x0005)

    def _loc_6D5(): pass

    label('loc_6D5')

    Jump('loc_6D8')

    def _loc_6D8(): pass

    label('loc_6D8')

    Return()

# id: 0x0001 offset: 0x6D9
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFD21A0, 0xFFFE5638, 0x00230026)

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x186A),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x01C8, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 2, 0x1302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_70C',
    )

    OP_6F(0x0000, 0)

    Jump('loc_713')

    def _loc_70C(): pass

    label('loc_70C')

    OP_6F(0x0000, 60)

    def _loc_713(): pass

    label('loc_713')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 3, 0x1303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_725',
    )

    OP_6F(0x0001, 0)

    Jump('loc_72C')

    def _loc_725(): pass

    label('loc_725')

    OP_6F(0x0001, 60)

    def _loc_72C(): pass

    label('loc_72C')

    Return()

# id: 0x0002 offset: 0x72D
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
        'loc_752',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_894')

    def _loc_752(): pass

    label('loc_752')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_76B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_894')

    def _loc_76B(): pass

    label('loc_76B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_784',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_894')

    def _loc_784(): pass

    label('loc_784')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_79D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_894')

    def _loc_79D(): pass

    label('loc_79D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B6',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_894')

    def _loc_7B6(): pass

    label('loc_7B6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CF',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_894')

    def _loc_7CF(): pass

    label('loc_7CF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E8',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_894')

    def _loc_7E8(): pass

    label('loc_7E8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_801',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_894')

    def _loc_801(): pass

    label('loc_801')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_81A',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_894')

    def _loc_81A(): pass

    label('loc_81A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_833',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_894')

    def _loc_833(): pass

    label('loc_833')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84C',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_894')

    def _loc_84C(): pass

    label('loc_84C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_865',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_894')

    def _loc_865(): pass

    label('loc_865')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87E',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_894')

    def _loc_87E(): pass

    label('loc_87E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_894',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_894(): pass

    label('loc_894')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8A9',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_894')

    def _loc_8A9(): pass

    label('loc_8A9')

    Return()

# id: 0x0003 offset: 0x8AA
@scena.Code('func_03_8AA')
def func_03_8AA():
    UnlockAchievement(0x02, 0xE0, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 2, 0x1302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_987',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['棕榈之药'], 1)"),
            Expr.Return,
        ),
        'loc_91E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1302)

    Jump('loc_984')

    def _loc_91E(): pass

    label('loc_91E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_984(): pass

    label('loc_984')

    Jump('loc_9B8')

    def _loc_987(): pass

    label('loc_987')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_9B8(): pass

    label('loc_9B8')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x9C6
@scena.Code('func_04_9C6')
def func_04_9C6():
    UnlockAchievement(0x02, 0xE1, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 3, 0x1303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA3',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_A3A',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1303)

    Jump('loc_AA0')

    def _loc_A3A(): pass

    label('loc_A3A')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_AA0(): pass

    label('loc_AA0')

    Jump('loc_AD4')

    def _loc_AA3(): pass

    label('loc_AA3')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_AD4(): pass

    label('loc_AD4')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xAE2
@scena.Code('func_05_AE2')
def func_05_AE2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AF3',
    )

    Call(0, 0x002F)

    def _loc_AF3(): pass

    label('loc_AF3')

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrPos(0x0101, -28930, -1990, 68170, 180)
    SetChrPos(0x00F7, -27890, -2009, 67540, 180)
    ClearMapFlags(0x00000001)
    OP_6D(-28090, -2060, 66510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0B6E')
    def lambda_0B6E():
        OP_6D(-28100, -2000, 63110, 2800)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0B6E)

    @scena.Lambda('lambda_0B86')
    def lambda_0B86():
        OP_67(0, 9500, -10000, 2800)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_0B86)

    @scena.Lambda('lambda_0B9E')
    def lambda_0B9E():
        OP_8E(0x00FE, -27890, 0, 63240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_0B9E)

    @scena.Lambda('lambda_0BB9')
    def lambda_0BB9():
        OP_8E(0x00FE, -28930, 0, 63440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0BB9)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x00F7, 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_E92',
    )

    OP_8C(0x0106, 270, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210113V#051F#2P不过，那位院长老师\n',
            '给人的感觉还是像母亲一样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210114V女王也是那样……\n',
            '在那种人面前自然没法不低头啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210115V#1016F#6P啊哈哈，阿加特\n',
            '原来也会这么想啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210116V#1017F嗯，和我妈妈\n',
            '感觉很像呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210117V#052F#2P是吗，大叔的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210118V#552F听说是在１０年前的战争中\n',
            '去世了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210119V……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210120V#1004F#6P怎么了，阿加特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210121V#552F#2P不……怎么说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210122V我觉得女人真是坚强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210123V#1015F#6P你想说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210124V#053F#2P……别再问下去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210125V#050F好啦，赶快去玛利诺亚\n',
            '把小鬼们都接回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10EF')

    def _loc_E92(): pass

    label('loc_E92')

    OP_8C(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210126V#021F#2P嗯……\n',
            '很了不起的女性呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210127V虽然类型完全不同，\n',
            '不过感觉上跟蕾娜阿姨很像。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210128V#1017F#6P啊，雪拉姐也这么想？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210129V我觉得妈妈也是那个样子，\n',
            '而且跟女王陛下也很相似呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210130V怎么说呢……\n',
            '会让人心中温暖起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210131V#020F#2P说到底，这可能\n',
            '就是女性的包容力呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210132V#026F呼……我还差的远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210133V#1006F#6P嗯～我认为雪拉姐\n',
            '还算有一定的包容力哦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210134V不过要更上一层楼的话，\n',
            '首先嗜酒就是个问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210135V#025F#2P唔……\n',
            '一针见血啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210136V#020F好了，赶快去村子\n',
            '接孩子们去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10EF(): pass

    label('loc_10EF')

    OP_A2(0x1217)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x10F5
@scena.Code('func_06_10F5')
def func_06_10F5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1106',
    )

    Call(0, 0x002F)

    def _loc_1106(): pass

    label('loc_1106')

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrPos(0x0101, -27520, -1970, 67560, 197)
    SetChrPos(0x00F7, -28770, -2040, 67850, 173)
    SetChrPos(0x0109, -28090, -2000, 66790, 186)
    OP_6D(-27790, -1950, 68340, 0)
    OP_67(0, 10060, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_118D')
    def lambda_118D():
        OP_6D(-28370, -1950, 60060, 5000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_118D)

    @scena.Lambda('lambda_11A5')
    def lambda_11A5():
        OP_67(0, 10060, -10000, 5000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_11A5)

    @scena.Lambda('lambda_11BD')
    def lambda_11BD():
        OP_8E(0x00FE, -28430, -1980, 58820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_11BD)

    Sleep(500)

    @scena.Lambda('lambda_11DD')
    def lambda_11DD():
        OP_8E(0x00FE, -27830, -1970, 60430, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11DD)

    Sleep(200)

    @scena.Lambda('lambda_11FD')
    def lambda_11FD():
        OP_8E(0x00FE, -29280, -1980, 60730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_11FD)

    FadeIn(2000, 0)
    WaitForThreadExit(0x0109, 0x0000)
    OP_8C(0x0109, 0, 400)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F7, 0x0002)

    ChrTalk(
        0x0109,
        (
            '#0180210371V#1061F呀～真是一群\n',
            '有精神的小鬼啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210372V#1062F不过，这就是院长老师的魅力吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210373V每个人都是那么率直，\n',
            '实在令人感到十分舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210374V#1006F因为是特蕾莎老师嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210375V不过本来还有\n',
            '另一个人在照顾孩子们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210376V由于正值学校的考试期间，\n',
            '今天好像没来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210377V#1062F嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210378V#1060F话说回来我\n',
            '现在就回卢安了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210379V你们怎么办？\n',
            '一起去城里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1446',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210380V#051F#5P是啊，这边的\n',
            '探听也结束了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210381V一路上结伴同行也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14A1')

    def _loc_1446(): pass

    label('loc_1446')

    ChrTalk(
        0x0103,
        (
            '#0030210382V#021F#5P是啊，这边的\n',
            '探听也结束了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210383V一路上结伴同行也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A1(): pass

    label('loc_14A1')

    ChrTalk(
        0x0101,
        (
            '#0010210384V#1006F那就决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210385V目标卢安——Ｌｅｔ＇ｓ　ｇｏ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x121A)
    OP_28(0x0082, 0x02, 0x0100)
    OP_28(0x0082, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1503
@scena.Code('func_07_1503')
def func_07_1503():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-45040, -2090, 25310, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(4610, 0)
    OP_6C(48000, 0)
    OP_6E(339, 0)
    SetChrPos(0x0008, -35650, -2000, 30000, 90)
    SetChrPos(0x0009, -36610, -2000, 30450, 90)
    SetChrPos(0x000B, -36680, -2000, 29000, 90)
    SetChrPos(0x000C, -37600, -2000, 30100, 90)
    SetChrPos(0x000A, -37620, -2000, 29000, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrPos(0x0011, -32070, -1990, 32290, 135)
    SetChrPos(0x0012, -31520, -2000, 31180, 135)
    SetChrPos(0x0013, -32080, -2000, 29670, 135)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    SetChrFlags(0x0013, 0x0040)
    LoadEffect(0x00, 'map\\\\mp008_00.eff')
    LoadEffect(0x01, 'Craft\\\\cr000_00.eff')
    LoadEffect(0x02, 'monster\\\\msc0290.eff')
    LoadEffect(0x03, 'monster\\\\msc0100.eff')
    LoadEffect(0x04, 'battle\\\\btgun00.eff')
    LoadEffect(0x05, 'map\\\\mp003_00.eff')
    LoadEffect(0x06, 'scraft\\\\sc000_11.eff')

    @scena.Lambda('lambda_16CD')
    def lambda_16CD():
        OP_6D(-24600, -2000, 30160, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_16CD)

    OP_C8(0x0200, 0x0046, 'C_PLAC18._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    OP_6D(-10080, -2000, 30010, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(1540, 0)
    OP_6C(72000, 0)
    OP_6E(562, 0)
    CreateThread(0x0014, 0x00, 0x00, 0x0018)
    Sleep(150)

    CreateThread(0x000B, 0x03, 0x00, 0x0028)
    OP_0D()

    @scena.Lambda('lambda_175F')
    def lambda_175F():
        OP_6D(-16810, -2000, 29970, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_175F)

    @scena.Lambda('lambda_1777')
    def lambda_1777():
        OP_67(0, 6040, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1777)

    @scena.Lambda('lambda_178F')
    def lambda_178F():
        OP_6B(1400, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_178F)

    @scena.Lambda('lambda_179F')
    def lambda_179F():
        OP_6C(59000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_179F)

    WaitForThreadExit(0x0014, 0x0000)
    TerminateThread(0x000B, 0x03)
    OP_23(0x013F)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    OP_6D(-34180, -2000, 31670, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(33000, 0)
    OP_6E(378, 0)
    OP_0D()
    CreateThread(0x0011, 0x00, 0x00, 0x0015)
    Sleep(100)

    CreateThread(0x0012, 0x00, 0x00, 0x0016)
    Sleep(100)

    CreateThread(0x0013, 0x00, 0x00, 0x0017)
    WaitForThreadExit(0x0012, 0x0000)

    @scena.Lambda('lambda_182C')
    def lambda_182C():
        OP_8F(0x00FE, -33070, -1990, 32290, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_182C)

    Sleep(100)

    @scena.Lambda('lambda_184C')
    def lambda_184C():
        OP_8F(0x00FE, -33080, -2000, 29670, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_184C)

    Sleep(100)

    @scena.Lambda('lambda_186C')
    def lambda_186C():
        OP_8F(0x00FE, -32520, -2000, 31180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_186C)

    ChrTalk(
        0x0012,
        (
            '#2460341229V#6P唔……\n',
            '还在追吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2450341230V#6P很快就能和玛诺利亚的\n',
            '守备队会合了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2470341231V#6P别退缩！\n',
            '必定能平安送到的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0011, 0x01, 0x00, 0x0021)
    Sleep(100)

    CreateThread(0x0012, 0x01, 0x00, 0x0022)
    Sleep(100)

    CreateThread(0x0013, 0x01, 0x00, 0x0023)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0410341232V#6P老、老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#0390341233V#754F#2P没问题……不要担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390341234V#750F我不会让它们\n',
            '伤害你们任何一个人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000A, 270, 400)

    ChrTalk(
        0x000A,
        (
            '#0430341235V#1733F#5P这下真的麻烦大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390341236V#752F#2P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0016, 0x03, 0x00, 0x0002)
    CreateThread(0x0017, 0x03, 0x00, 0x0002)
    SetChrPos(0x0014, -58610, -1700, 17850, 90)
    SetChrPos(0x0015, -61080, -1700, 19330, 90)
    SetChrPos(0x0016, -59760, -1700, 15360, 90)
    SetChrPos(0x0017, -62900, -1700, 16980, 90)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0014, 0x0040)
    SetChrFlags(0x0015, 0x0040)
    SetChrFlags(0x0016, 0x0040)
    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x0014, 0x0800)
    SetChrFlags(0x0015, 0x0800)
    SetChrFlags(0x0016, 0x0800)
    SetChrFlags(0x0017, 0x0800)

    @scena.Lambda('lambda_1AC8')
    def lambda_1AC8():
        OP_6D(-60930, -2000, 17930, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1AC8)

    @scena.Lambda('lambda_1AE0')
    def lambda_1AE0():
        OP_67(0, 4890, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AE0)

    @scena.Lambda('lambda_1AF8')
    def lambda_1AF8():
        OP_6B(2250, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1AF8)

    @scena.Lambda('lambda_1B08')
    def lambda_1B08():
        OP_6C(299000, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1B08)

    @scena.Lambda('lambda_1B18')
    def lambda_1B18():
        OP_6E(362, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1B18)

    @scena.Lambda('lambda_1B28')
    def lambda_1B28():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B28)

    Sleep(80)

    @scena.Lambda('lambda_1B3B')
    def lambda_1B3B():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B3B)

    Sleep(50)

    @scena.Lambda('lambda_1B4E')
    def lambda_1B4E():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1B4E)

    OP_8E(0x0008, -35820, -2000, 28400, 3000, 0x00)
    OP_8E(0x0008, -38110, -2000, 27710, 3000, 0x00)
    OP_8E(0x0008, -38700, -2000, 28720, 3000, 0x00)
    OP_8C(0x0008, 270, 400)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(1000)

    Fade(500)
    OP_6D(-36180, -2000, 31670, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(33000, 0)
    OP_6E(378, 0)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0013, 0x01)
    SetChrSubChip(0x0011, 0)
    SetChrSubChip(0x0013, 0)
    SetChrChipByIndex(0x0011, 13)
    SetChrChipByIndex(0x0013, 13)
    OP_8C(0x0011, 270, 0)
    OP_8C(0x0013, 270, 0)
    OP_8C(0x0014, 90, 0)
    OP_8C(0x0015, 90, 0)
    OP_8C(0x0016, 90, 0)
    OP_8C(0x0017, 90, 0)
    ClearChrFlags(0x0014, 0x0800)
    ClearChrFlags(0x0015, 0x0800)
    ClearChrFlags(0x0016, 0x0800)
    ClearChrFlags(0x0017, 0x0800)
    OP_0D()

    ChrTalk(
        0x0013,
        (
            '#2470341237V#2P什…什么…！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2450341238V#2P从另一边过来！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000C,
        (
            '#0420341239V#1723F#2P呜哎哎哎哎哎！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400341240V#776F#2P这、这样的话\n',
            '连我们也……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390341241V#755F#5P不行！\n',
            '退下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390341242V#757F（女神啊……\n',
            '　请拯救我们这些无助的人吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    TerminateThread(0x0012, 0x01)
    OP_6D(-58200, -2000, 18040, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(255000, 0)
    OP_6E(371, 0)

    @scena.Lambda('lambda_1DAB')
    def lambda_1DAB():
        OP_6D(-51550, -2000, 22170, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DAB)

    CreateThread(0x000B, 0x03, 0x00, 0x0028)
    CreateThread(0x0014, 0x00, 0x00, 0x0019)
    Sleep(200)

    CreateThread(0x0015, 0x00, 0x00, 0x001A)
    Sleep(250)

    CreateThread(0x0016, 0x00, 0x00, 0x001B)
    Sleep(200)

    CreateThread(0x0017, 0x00, 0x00, 0x001C)
    Sleep(1000)

    OP_20(0x000003E8)
    WaitForThreadExit(0x0017, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    OP_1D(0x2C)
    Sleep(500)

    Fade(500)
    OP_6D(-49530, -2000, 23670, 0)
    OP_67(0, 6880, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(20000, 0)
    OP_6E(355, 0)
    ClearMapFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x000E, -50890, 300, 35800, 225)
    SetChrPos(0x000D, -50890, 300, 35800, 225)
    SetChrPos(0x000F, -50890, 300, 35800, 225)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000F, 0x0040)
    CreateThread(0x000F, 0x01, 0x00, 0x0024)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, 0x0025)
    Sleep(100)

    CreateThread(0x000D, 0x01, 0x00, 0x0027)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000F, 0x0001)
    SetChrFlags(0x000E, 0x0020)
    SetChrFlags(0x000F, 0x0020)

    @scena.Lambda('lambda_1EEE')
    def lambda_1EEE():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1EEE)

    @scena.Lambda('lambda_1EFC')
    def lambda_1EFC():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1EFC)

    Sleep(1000)

    @scena.Lambda('lambda_1F0F')
    def lambda_1F0F():
        OP_6D(-57190, -2000, 18670, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F0F)

    OP_7D(0x00, 0x000E, 0x0032, 0x01F4)
    OP_7D(0x00, 0x000D, 0x0032, 0x01F4)
    OP_7D(0x00, 0x000F, 0x0032, 0x01F4)
    SetChrSubChip(0x000E, 0)
    SetChrChipByIndex(0x000E, 20)

    @scena.Lambda('lambda_1F49')
    def lambda_1F49():
        OP_99(0x00FE, 0x01, 0x04, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1F49)

    @scena.Lambda('lambda_1F59')
    def lambda_1F59():
        OP_99(0x00FE, 0x01, 0x04, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1F59)

    @scena.Lambda('lambda_1F69')
    def lambda_1F69():
        OP_99(0x00FE, 0x01, 0x04, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1F69)

    @scena.Lambda('lambda_1F79')
    def lambda_1F79():
        OP_8F(0x00FE, -57630, -2000, 18410, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_1F79)

    @scena.Lambda('lambda_1F94')
    def lambda_1F94():
        OP_8F(0x00FE, -56740, -2000, 17830, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1F94)

    @scena.Lambda('lambda_1FAF')
    def lambda_1FAF():
        OP_8F(0x00FE, -57610, -2000, 19660, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1FAF)

    OP_22(0x009B, 0x00, 0x64)
    Sleep(100)

    TerminateThread(0x0017, 0x03)
    SetChrChipByIndex(0x0017, 27)
    SetChrSubChip(0x0017, 0)
    WaitForThreadExit(0x000E, 0x0002)
    WaitForThreadExit(0x000D, 0x0002)
    WaitForThreadExit(0x000F, 0x0002)
    OP_7D(0x01, 0x000E, 0x0000, 0x0000)
    OP_7D(0x01, 0x000D, 0x0000, 0x0000)
    OP_7D(0x01, 0x000F, 0x0000, 0x0000)
    PlayEffect(0x03, 0x00, 0x0017, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_83(0x00, 0x02)
    SetChrFlags(0x0017, 0x0080)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(-37000, -2000, 30060, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(24000, 0)
    OP_6E(282, 0)
    SetChrPos(0x0011, -35550, -2000, 30860, 270)
    SetChrPos(0x0012, -34880, -2000, 29770, 270)
    SetChrPos(0x0013, -34710, -2000, 28220, 270)
    SetChrSubChip(0x0011, 0)
    SetChrSubChip(0x0012, 0)
    SetChrSubChip(0x0013, 0)
    SetChrChipByIndex(0x0011, 29)
    SetChrChipByIndex(0x0012, 29)
    SetChrChipByIndex(0x0013, 29)
    OP_8C(0x0012, 270, 0)
    ClearChrFlags(0x000D, 0x0020)
    ClearChrFlags(0x000E, 0x0020)
    ClearChrFlags(0x000F, 0x0020)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 30)
    SetChrSubChip(0x000E, 0)
    SetChrChipByIndex(0x000E, 31)
    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000F, 32)

    @scena.Lambda('lambda_211B')
    def lambda_211B():
        OP_8E(0x00FE, -41340, -2000, 27500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_211B)

    OP_0D()
    SetMapFlags(0x00000010)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_2158')
    def lambda_2158():
        OP_8E(0x00FE, -42290, -2000, 28170, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2158)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    @scena.Lambda('lambda_221E')
    def lambda_221E():
        OP_8E(0x00FE, -41470, -2000, 26020, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_221E)

    WaitForThreadExit(0x000D, 0x0001)
    SetChrSubChip(0x000D, 0)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)

    ChrTalk(
        0x0011,
        (
            '#2450341243V#2P你、你们是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400341244V#774F#2P难、难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0410341245V#1714F#2P游击士先生……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0310341246V#821F#6P嘿嘿，久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0120341247V#811F#6P没事吧？\n',
            '没受伤吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0420341248V#1720F#2P嗯，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430341249V#1732F#2P没事～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0010, -44820, 0, 51380, 135)

    NpcTalk(
        0x0010,
        '女性的声音',
        (
            '#0320341250V呵呵……\n',
            '幸好赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrPos(0x0010, -48280, 0, 36210, 135)
    ClearChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0010, 0x0040)
    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x0010, 33)

    @scena.Lambda('lambda_23CD')
    def lambda_23CD():
        OP_6D(-40770, -2000, 33410, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23CD)

    @scena.Lambda('lambda_23E5')
    def lambda_23E5():
        OP_67(0, 3940, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_23E5)

    @scena.Lambda('lambda_23FD')
    def lambda_23FD():
        OP_6B(2880, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_23FD)

    @scena.Lambda('lambda_240D')
    def lambda_240D():
        OP_6C(327000, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_240D)

    @scena.Lambda('lambda_241D')
    def lambda_241D():
        OP_6E(367, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_241D)

    @scena.Lambda('lambda_242D')
    def lambda_242D():
        OP_8E(0x00FE, -42520, 0, 32790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_242D)

    @scena.Lambda('lambda_2448')
    def lambda_2448():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_2448')

    DispatchAsync2(0x0008, 0x0001, lambda_2448)

    @scena.Lambda('lambda_2459')
    def lambda_2459():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_2459')

    DispatchAsync2(0x0009, 0x0001, lambda_2459)

    @scena.Lambda('lambda_246A')
    def lambda_246A():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_246A')

    DispatchAsync2(0x000C, 0x0001, lambda_246A)

    @scena.Lambda('lambda_247B')
    def lambda_247B():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_247B')

    DispatchAsync2(0x0011, 0x0001, lambda_247B)

    @scena.Lambda('lambda_248C')
    def lambda_248C():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_248C')

    DispatchAsync2(0x000F, 0x0001, lambda_248C)

    Sleep(100)

    @scena.Lambda('lambda_24A2')
    def lambda_24A2():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_24A2')

    DispatchAsync2(0x000B, 0x0001, lambda_24A2)

    @scena.Lambda('lambda_24B3')
    def lambda_24B3():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_24B3')

    DispatchAsync2(0x000A, 0x0001, lambda_24B3)

    @scena.Lambda('lambda_24C4')
    def lambda_24C4():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_24C4')

    DispatchAsync2(0x0012, 0x0001, lambda_24C4)

    @scena.Lambda('lambda_24D5')
    def lambda_24D5():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_24D5')

    DispatchAsync2(0x000E, 0x0001, lambda_24D5)

    Sleep(100)

    @scena.Lambda('lambda_24EB')
    def lambda_24EB():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_24EB')

    DispatchAsync2(0x0013, 0x0001, lambda_24EB)

    @scena.Lambda('lambda_24FC')
    def lambda_24FC():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_24FC')

    DispatchAsync2(0x000D, 0x0001, lambda_24FC)

    WaitForThreadExit(0x0010, 0x0001)
    SetChrSubChip(0x0010, 0)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x000D, 0x01)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0390341251V#753F#6P啊，卡露娜小姐……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0320341252V#831F#6P好久不见呢，院长老师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320341253V你们在前往玛诺利亚避难的途中吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390341254V#750F#6P嗯嗯，承蒙\n',
            '军队的各位相送……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_260B')
    def lambda_260B():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_260B)

    Sleep(100)

    @scena.Lambda('lambda_261E')
    def lambda_261E():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_261E)

    Sleep(100)

    @scena.Lambda('lambda_2631')
    def lambda_2631():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2631)

    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#0330341255V#842F#5P军队的各位！\n',
            '这里交给我们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0120341256V#816F#5P请赶快带孩子们\n',
            '去玛诺利亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2460341257V#2P不、不胜感激！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2470341258V#2P各位！\n',
            '跟我们来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_26F9')
    def lambda_26F9():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_26F9)

    Sleep(80)

    @scena.Lambda('lambda_270C')
    def lambda_270C():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_270C)

    @scena.Lambda('lambda_271A')
    def lambda_271A():
        OP_8C(0x00FE, 90, 400)
        Yield()

        Jump('lambda_271A')

    DispatchAsync2(0x000B, 0x0001, lambda_271A)

    Sleep(80)

    @scena.Lambda('lambda_2730')
    def lambda_2730():
        OP_8C(0x00FE, 90, 400)
        Yield()

        Jump('lambda_2730')

    DispatchAsync2(0x000A, 0x0001, lambda_2730)

    Sleep(50)

    @scena.Lambda('lambda_2746')
    def lambda_2746():
        OP_8C(0x00FE, 90, 400)
        Yield()

        Jump('lambda_2746')

    DispatchAsync2(0x000C, 0x0001, lambda_2746)

    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0400341259V#770F#5P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430341260V#1731F#5P知道了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0013, 0x01, 0x00, 0x002E)
    CreateThread(0x0012, 0x01, 0x00, 0x002D)
    Sleep(100)

    CreateThread(0x000D, 0x01, 0x00, 0x002B)

    @scena.Lambda('lambda_27B7')
    def lambda_27B7():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_27B7')

    DispatchAsync2(0x0010, 0x0003, lambda_27B7)

    Sleep(200)

    CreateThread(0x000F, 0x01, 0x00, 0x0029)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x00, 0x002A)

    @scena.Lambda('lambda_27E0')
    def lambda_27E0():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_27E0)

    @scena.Lambda('lambda_27EE')
    def lambda_27EE():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27EE)

    @scena.Lambda('lambda_27FC')
    def lambda_27FC():
        OP_8C(0x00FE, 270, 400)
        Yield()

        Jump('lambda_27FC')

    DispatchAsync2(0x0008, 0x0001, lambda_27FC)

    @scena.Lambda('lambda_280D')
    def lambda_280D():
        OP_8C(0x00FE, 270, 400)
        Yield()

        Jump('lambda_280D')

    DispatchAsync2(0x0009, 0x0001, lambda_280D)

    @scena.Lambda('lambda_281E')
    def lambda_281E():
        OP_8C(0x00FE, 270, 400)
        Yield()

        Jump('lambda_281E')

    DispatchAsync2(0x000C, 0x0001, lambda_281E)

    @scena.Lambda('lambda_282F')
    def lambda_282F():
        OP_8C(0x00FE, 270, 400)
        Yield()

        Jump('lambda_282F')

    DispatchAsync2(0x000B, 0x0001, lambda_282F)

    @scena.Lambda('lambda_2840')
    def lambda_2840():
        OP_8C(0x00FE, 270, 400)
        Yield()

        Jump('lambda_2840')

    DispatchAsync2(0x000A, 0x0001, lambda_2840)

    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0012, 0x0001)
    WaitForThreadExit(0x0013, 0x0001)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000A, 0x01)
    SetChrSubChip(0x0012, 0)
    SetChrChipByIndex(0x0012, 24)

    @scena.Lambda('lambda_287E')
    def lambda_287E():
        OP_8E(0x00FE, -52320, -2000, 21570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_287E)

    Sleep(50)

    SetChrSubChip(0x0013, 0)
    SetChrChipByIndex(0x0013, 24)

    @scena.Lambda('lambda_28A8')
    def lambda_28A8():
        OP_8E(0x00FE, -53930, -1970, 23260, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_28A8)

    Sleep(100)

    @scena.Lambda('lambda_28C8')
    def lambda_28C8():
        OP_8E(0x00FE, -51580, -2000, 22790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_28C8)

    @scena.Lambda('lambda_28E3')
    def lambda_28E3():
        OP_6D(-39740, -1500, 29550, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28E3)

    @scena.Lambda('lambda_28FB')
    def lambda_28FB():
        OP_67(0, 5590, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28FB)

    @scena.Lambda('lambda_2913')
    def lambda_2913():
        OP_6B(2600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2913)

    @scena.Lambda('lambda_2923')
    def lambda_2923():
        OP_6C(306000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2923)

    @scena.Lambda('lambda_2933')
    def lambda_2933():
        OP_6E(367, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2933)

    Sleep(100)

    @scena.Lambda('lambda_2948')
    def lambda_2948():
        OP_8E(0x00FE, -50070, -2000, 22250, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2948)

    Sleep(50)

    @scena.Lambda('lambda_2968')
    def lambda_2968():
        OP_8E(0x00FE, -51400, -2000, 24520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2968)

    Sleep(100)

    @scena.Lambda('lambda_2988')
    def lambda_2988():
        OP_8E(0x00FE, -50070, -2000, 22250, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2988)

    @scena.Lambda('lambda_29A3')
    def lambda_29A3():
        OP_8E(0x00FE, -51400, -2000, 24520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_29A3)

    Sleep(100)

    SetChrSubChip(0x0011, 0)
    SetChrChipByIndex(0x0011, 24)

    @scena.Lambda('lambda_29CD')
    def lambda_29CD():
        OP_8E(0x00FE, -50290, -2000, 23590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_29CD)

    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    TerminateThread(0x000F, 0x03)
    TerminateThread(0x0010, 0x03)
    TerminateThread(0x000E, 0x03)
    TerminateThread(0x000D, 0x03)
    OP_8C(0x000D, 45, 400)

    @scena.Lambda('lambda_2A31')
    def lambda_2A31():
        OP_8E(0x00FE, -38550, -2000, 28010, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_2A31)

    Sleep(100)

    OP_8C(0x0010, 135, 400)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_2A5D')
    def lambda_2A5D():
        OP_96(0x00FE, 0xFFFF6794, 0xFFFFF830, 0x000073BE, 0x000003E8, 0x00001770)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_2A5D)

    Sleep(100)

    WaitForThreadExit(0x000D, 0x0000)
    OP_8C(0x000D, 90, 400)
    WaitForThreadExit(0x0010, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_2A96')
    def lambda_2A96():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2A96)

    Sleep(100)

    @scena.Lambda('lambda_2AA9')
    def lambda_2AA9():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2AA9)

    Sleep(100)

    OP_8C(0x000E, 90, 400)
    Fade(1000)
    OP_6D(-16780, -2000, 30390, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(89000, 0)
    OP_6E(349, 0)

    @scena.Lambda('lambda_2B05')
    def lambda_2B05():
        OP_6C(53000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2B05)

    CreateThread(0x0014, 0x00, 0x00, 0x000F)
    Sleep(200)

    CreateThread(0x000B, 0x03, 0x00, 0x0028)
    Sleep(200)

    CreateThread(0x0015, 0x00, 0x00, 0x0010)
    Sleep(400)

    CreateThread(0x0016, 0x00, 0x00, 0x0011)
    Sleep(400)

    CreateThread(0x0017, 0x00, 0x00, 0x0012)
    Sleep(400)

    CreateThread(0x0018, 0x00, 0x00, 0x0013)
    Sleep(400)

    CreateThread(0x0019, 0x00, 0x00, 0x0014)
    WaitForThreadExit(0x0019, 0x0000)
    TerminateThread(0x000B, 0x03)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(1000)

    SetChrPos(0x000D, -37670, -2000, 29370, 90)
    SetChrPos(0x000F, -39320, -2000, 30070, 90)
    SetChrPos(0x000E, -39100, -2000, 27880, 90)
    SetChrPos(0x0010, -41230, -2000, 28610, 90)
    SetChrChipByIndex(0x000D, 9)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000F, 11)
    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000E, 10)
    SetChrSubChip(0x000E, 0)
    SetChrChipByIndex(0x0010, 12)
    SetChrSubChip(0x0010, 0)

    @scena.Lambda('lambda_2BE3')
    def lambda_2BE3():
        OP_6D(-37540, -2000, 29550, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2BE3)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#0310341261V#825F#6P好了～\n',
            '看来会相当吃力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0320341262V#835F#6P不过……\n',
            '也只能全力以赴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0120341263V#816F#6P没问题，总有办法的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120341264V和前往塔内的\n',
            '艾丝蒂尔他们相比\n',
            '这实在算不了什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0330341265V#840F#6P呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330341266V为了让他们放心战斗，\n',
            '就让我们尽最大努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0330341267V#843F#6P方术──满碛寒光生铁衣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 18)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    PlayEffect(0x01, 0x00, 0x000D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_83(0x00, 0x02)
    PlayEffect(0x02, 0x01, 0x000D, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x02, 0x02, 0x000E, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x02, 0x03, 0x000F, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x02, 0x04, 0x0010, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_83(0x04, 0x02)
    Sleep(500)

    Fade(500)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0330341268V#846F#6P要上啰，各位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#815F#1K好！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000F,
        (
            '#822F#1K#1P啊啊！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0010,
        (
            '#0320341271V#832F#1K明白！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    OP_56(0x01)
    OP_59()

    @scena.Lambda('lambda_2F72')
    def lambda_2F72():
        OP_6D(-26760, -2000, 31240, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F72)

    @scena.Lambda('lambda_2F8A')
    def lambda_2F8A():
        OP_6B(2390, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F8A)

    FadeOut(2000, 0, -1)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 15)

    @scena.Lambda('lambda_2FAE')
    def lambda_2FAE():
        OP_8F(0x00FE, -29190, -2000, 31240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2FAE)

    Sleep(100)

    SetChrSubChip(0x000E, 0)
    SetChrChipByIndex(0x000E, 19)

    @scena.Lambda('lambda_2FD8')
    def lambda_2FD8():
        OP_8F(0x00FE, -30340, -2000, 29780, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2FD8)

    Sleep(50)

    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000F, 21)

    @scena.Lambda('lambda_3002')
    def lambda_3002():
        OP_8F(0x00FE, -30760, -2000, 31910, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3002)

    Sleep(100)

    SetChrSubChip(0x0010, 0)
    SetChrChipByIndex(0x0010, 23)

    @scena.Lambda('lambda_302C')
    def lambda_302C():
        OP_8F(0x00FE, -31740, -2000, 30490, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_302C)

    CreateThread(0x0014, 0x01, 0x00, 0x0008)
    CreateThread(0x000B, 0x03, 0x00, 0x0028)
    OP_A2(0x0000)
    Sleep(100)

    OP_0D()
    OP_20(0x000007D0)
    Sleep(200)

    OP_24(0x01C8, 0x5A)
    Sleep(200)

    OP_24(0x01C8, 0x50)
    Sleep(200)

    OP_24(0x01C8, 0x46)
    Sleep(200)

    OP_24(0x01C8, 0x3C)
    Sleep(200)

    OP_24(0x01C8, 0x32)
    Sleep(200)

    OP_24(0x01C8, 0x28)
    Sleep(200)

    OP_24(0x01C8, 0x1E)
    Sleep(200)

    OP_23(0x01C8)
    OP_21()
    OP_A2(0x1E2F)
    OP_A2(0x10F6)
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x30B5
@scena.Code('func_08_30B5')
def func_08_30B5():
    Sleep(500)

    CreateThread(0x0014, 0x00, 0x00, 0x0009)
    Sleep(200)

    CreateThread(0x0015, 0x00, 0x00, 0x000A)
    Sleep(200)

    CreateThread(0x0016, 0x00, 0x00, 0x000B)
    Sleep(200)

    CreateThread(0x0017, 0x00, 0x00, 0x000C)
    Sleep(200)

    CreateThread(0x0018, 0x00, 0x00, 0x000D)
    Sleep(200)

    CreateThread(0x0019, 0x00, 0x00, 0x000E)

    Return()

# id: 0x0009 offset: 0x30FE
@scena.Code('func_09_30FE')
def func_09_30FE():
    SetChrChipByIndex(0x00FE, 26)
    OP_90(0x00FE, -5000, -200, 500, 5000, 0x00)

    Return()

# id: 0x000A offset: 0x3118
@scena.Code('func_0A_3118')
def func_0A_3118():
    SetChrChipByIndex(0x00FE, 26)
    OP_90(0x00FE, -5000, -200, 500, 5000, 0x00)

    Return()

# id: 0x000B offset: 0x3132
@scena.Code('func_0B_3132')
def func_0B_3132():
    SetChrChipByIndex(0x00FE, 26)
    OP_90(0x00FE, -5000, -200, 500, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x314C
@scena.Code('func_0C_314C')
def func_0C_314C():
    SetChrChipByIndex(0x00FE, 26)
    OP_90(0x00FE, -5000, -200, 500, 5000, 0x00)

    Return()

# id: 0x000D offset: 0x3166
@scena.Code('func_0D_3166')
def func_0D_3166():
    SetChrChipByIndex(0x00FE, 26)
    OP_90(0x00FE, -5000, -200, 500, 5000, 0x00)

    Return()

# id: 0x000E offset: 0x3180
@scena.Code('func_0E_3180')
def func_0E_3180():
    SetChrChipByIndex(0x00FE, 26)
    OP_90(0x00FE, -5000, -200, 500, 5000, 0x00)

    Return()

# id: 0x000F offset: 0x319A
@scena.Code('func_0F_319A')
def func_0F_319A():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    SetChrPos(0x00FE, -2790, -1750, 30120, 270)
    ClearChrFlags(0x00FE, 0x0080)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -10400, -1750, 29700, 6000, 0x00)
    OP_8E(0x00FE, -19710, -1750, 31220, 6000, 0x00)
    SetChrPos(0x00FE, -19710, -1600, 31220, 270)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0010 offset: 0x320D
@scena.Code('func_10_320D')
def func_10_320D():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    SetChrPos(0x00FE, -2790, -1750, 30120, 270)
    ClearChrFlags(0x00FE, 0x0080)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -10400, -1750, 29700, 6000, 0x00)
    OP_8E(0x00FE, -20630, -1750, 28820, 6000, 0x00)
    SetChrPos(0x00FE, -20630, -1600, 28820, 270)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0011 offset: 0x3280
@scena.Code('func_11_3280')
def func_11_3280():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    SetChrPos(0x00FE, -2790, -1750, 30120, 270)
    ClearChrFlags(0x00FE, 0x0080)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -10400, -1750, 29700, 6000, 0x00)
    OP_8E(0x00FE, -17410, -1750, 28230, 6000, 0x00)
    SetChrPos(0x00FE, -17410, -1600, 28230, 270)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0012 offset: 0x32F3
@scena.Code('func_12_32F3')
def func_12_32F3():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    SetChrPos(0x00FE, -2790, -1750, 30120, 270)
    ClearChrFlags(0x00FE, 0x0080)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -10400, -1750, 29700, 6000, 0x00)
    OP_8E(0x00FE, -16260, -1750, 30520, 6000, 0x00)
    SetChrPos(0x00FE, -16260, -1600, 30520, 270)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0013 offset: 0x3366
@scena.Code('func_13_3366')
def func_13_3366():
    SetChrPos(0x00FE, -2790, -1750, 30120, 270)
    ClearChrFlags(0x00FE, 0x0080)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -10400, -1750, 29700, 6000, 0x00)
    OP_8E(0x00FE, -13850, -1750, 29430, 6000, 0x00)
    SetChrPos(0x00FE, -13850, -1600, 29430, 270)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0014 offset: 0x33CE
@scena.Code('func_14_33CE')
def func_14_33CE():
    SetChrPos(0x00FE, -2790, -1750, 30120, 270)
    ClearChrFlags(0x00FE, 0x0080)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -10400, -1750, 29700, 6000, 0x00)
    OP_8E(0x00FE, -11490, -1750, 28990, 6000, 0x00)
    SetChrPos(0x00FE, -11490, -1600, 28990, 270)
    SetChrChipByIndex(0x00FE, 14)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0015 offset: 0x3436
@scena.Code('func_15_3436')
def func_15_3436():
    SetChrChipByIndex(0x00FE, 28)
    OP_8F(0x00FE, -33070, -2000, 32290, 2000, 0x00)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x0016 offset: 0x3455
@scena.Code('func_16_3455')
def func_16_3455():
    SetChrChipByIndex(0x00FE, 28)
    OP_8F(0x00FE, -32520, -2000, 31180, 2000, 0x00)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x0017 offset: 0x3474
@scena.Code('func_17_3474')
def func_17_3474():
    SetChrChipByIndex(0x00FE, 28)
    OP_8F(0x00FE, -33080, -2000, 29670, 2000, 0x00)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x0018 offset: 0x3493
@scena.Code('func_18_3493')
def func_18_3493():
    CreateThread(0x0014, 0x01, 0x00, 0x001D)
    Sleep(600)

    CreateThread(0x0015, 0x01, 0x00, 0x001E)
    WaitForThreadExit(0x0015, 0x0001)

    Return()

# id: 0x0019 offset: 0x34AC
@scena.Code('func_19_34AC')
def func_19_34AC():
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -54280, -1700, 20030, 6000, 0x00)
    OP_8E(0x00FE, -49430, -1700, 23650, 6000, 0x00)
    SetChrPos(0x00FE, -49430, -1500, 23650, 45)
    TerminateThread(0x00FE, 0x03)
    TerminateThread(0x000B, 0x03)
    OP_23(0x013F)
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x05, 0xFF, 0x0014, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 27)
    SetChrSubChip(0x00FE, 0)
    OP_22(0x0209, 0x00, 0x64)
    OP_9E(0x00FE, 0x00000014, 0x00000000, 0x0000012C, 0x00000BB8)
    ClearChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 14)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)

    Return()

# id: 0x001A offset: 0x3579
@scena.Code('func_1A_3579')
def func_1A_3579():
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -56540, -1700, 20040, 6000, 0x00)
    OP_8E(0x00FE, -52370, -1700, 23870, 6000, 0x00)
    SetChrPos(0x00FE, -52370, -1500, 23870, 45)
    TerminateThread(0x00FE, 0x03)
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x05, 0xFF, 0x0015, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 27)
    SetChrSubChip(0x00FE, 0)
    OP_22(0x0209, 0x00, 0x64)
    OP_9E(0x00FE, 0x00000014, 0x00000000, 0x0000012C, 0x00000BB8)
    ClearChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 14)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)

    Return()

# id: 0x001B offset: 0x363F
@scena.Code('func_1B_363F')
def func_1B_363F():
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -54080, -1700, 17740, 6000, 0x00)
    OP_8E(0x00FE, -50700, -1700, 20280, 6000, 0x00)
    SetChrPos(0x00FE, -50700, -1500, 20280, 45)
    TerminateThread(0x00FE, 0x03)
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x05, 0xFF, 0x0016, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 27)
    SetChrSubChip(0x00FE, 0)
    OP_22(0x0209, 0x00, 0x64)
    OP_9E(0x00FE, 0x00000014, 0x00000000, 0x0000012C, 0x00000BB8)
    ClearChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 14)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)

    Return()

# id: 0x001C offset: 0x3705
@scena.Code('func_1C_3705')
def func_1C_3705():
    SetChrChipByIndex(0x00FE, 26)
    OP_8E(0x00FE, -57770, -1700, 17970, 6000, 0x00)
    OP_8E(0x00FE, -54410, -1700, 20300, 6000, 0x00)
    SetChrPos(0x00FE, -54410, -1500, 20300, 45)
    TerminateThread(0x00FE, 0x03)
    OP_22(0x01F7, 0x00, 0x64)
    PlayEffect(0x05, 0xFF, 0x0017, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 27)
    SetChrSubChip(0x00FE, 0)
    OP_22(0x0209, 0x00, 0x64)
    OP_9E(0x00FE, 0x00000014, 0x00000000, 0x0000012C, 0x00000BB8)
    ClearChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 14)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)

    Return()

# id: 0x001D offset: 0x37CB
@scena.Code('func_1D_37CB')
def func_1D_37CB():
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrPos(0x00FE, 6670, -1750, 29940, 270)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 26)
    OP_8F(0x00FE, -11370, -1750, 29940, 6000, 0x00)
    OP_8F(0x00FE, -17170, -1750, 30490, 6000, 0x00)
    SetChrPos(0x00FE, -17170, -1600, 30490, 270)
    SetChrChipByIndex(0x00FE, 14)

    Return()

# id: 0x001E offset: 0x382C
@scena.Code('func_1E_382C')
def func_1E_382C():
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrPos(0x00FE, 6670, -1750, 29940, 270)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 26)
    OP_8F(0x00FE, -11370, -1750, 29940, 6000, 0x00)
    OP_8E(0x00FE, -17530, -1750, 27500, 6000, 0x00)
    SetChrPos(0x00FE, -17530, -1600, 27500, 270)
    OP_8C(0x00FE, 270, 0)
    SetChrChipByIndex(0x00FE, 14)

    Return()

# id: 0x001F offset: 0x3894
@scena.Code('func_1F_3894')
def func_1F_3894():
    SetChrPos(0x00FE, 6670, -1750, 29940, 270)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 26)
    OP_8F(0x00FE, -11370, -1750, 29940, 6000, 0x00)
    OP_8E(0x00FE, -15090, -1750, 28360, 6000, 0x00)
    SetChrPos(0x00FE, -15090, -1600, 28360, 270)
    OP_8C(0x00FE, 270, 0)

    Return()

# id: 0x0020 offset: 0x38F0
@scena.Code('func_20_38F0')
def func_20_38F0():
    SetChrPos(0x00FE, 6670, -1750, 29940, 270)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 26)
    OP_8F(0x00FE, -13760, -1750, 30110, 5000, 0x00)
    SetChrPos(0x00FE, -13760, -1600, 30110, 270)

    Return()

# id: 0x0021 offset: 0x3931
@scena.Code('func_21_3931')
def func_21_3931():
    SetChrChipByIndex(0x00FE, 25)
    def _loc_3936(): pass

    label('loc_3936')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3998',
    )

    OP_99(0x00FE, 0x00, 0x04, 0x00000A28)
    OP_22(0x01F7, 0x00, 0x50)
    PlayEffect(0x04, 0xFF, 0x00FE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x001F, 0, 0, 0, 0)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 0x00000A28)
    Sleep(550)

    Jump('loc_3936')

    def _loc_3998(): pass

    label('loc_3998')

    Return()

# id: 0x0022 offset: 0x3999
@scena.Code('func_22_3999')
def func_22_3999():
    SetChrChipByIndex(0x00FE, 25)
    def _loc_399E(): pass

    label('loc_399E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A00',
    )

    OP_99(0x00FE, 0x00, 0x04, 0x00000A28)
    OP_22(0x01F7, 0x00, 0x50)
    PlayEffect(0x04, 0xFF, 0x00FE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x001F, 0, 0, 0, 0)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 0x00000A28)
    Sleep(600)

    Jump('loc_399E')

    def _loc_3A00(): pass

    label('loc_3A00')

    Return()

# id: 0x0023 offset: 0x3A01
@scena.Code('func_23_3A01')
def func_23_3A01():
    SetChrChipByIndex(0x00FE, 25)
    def _loc_3A06(): pass

    label('loc_3A06')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A68',
    )

    OP_99(0x00FE, 0x00, 0x04, 0x00000A28)
    OP_22(0x01F7, 0x00, 0x50)
    PlayEffect(0x04, 0xFF, 0x00FE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x001F, 0, 0, 0, 0)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 0x00000A28)
    Sleep(500)

    Jump('loc_3A06')

    def _loc_3A68(): pass

    label('loc_3A68')

    Return()

# id: 0x0024 offset: 0x3A69
@scena.Code('func_24_3A69')
def func_24_3A69():
    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0xFFFF4F20, 0xFFFFF830, 0x00005D8E, 0x000004B0, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x00FE, 225, 400)
    SetChrFlags(0x0016, 0x0020)
    SetChrFlags(0x0016, 0x0004)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 21)
    OP_8E(0x00FE, -49070, -2000, 20960, 6000, 0x00)
    SetChrSubChip(0x000F, 0)
    SetChrChipByIndex(0x000F, 22)

    @scena.Lambda('lambda_3AC9')
    def lambda_3AC9():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3AC9)

    Sleep(300)

    PlayEffect(0x06, 0xFF, 0x0016, 0, 800, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    TerminateThread(0x0016, 0x03)
    SetChrChipByIndex(0x0016, 27)
    SetChrSubChip(0x0016, 0)

    @scena.Lambda('lambda_3B32')
    def lambda_3B32():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_3B32)

    Sleep(300)

    @scena.Lambda('lambda_3B51')
    def lambda_3B51():
        OP_96(0x00FE, 0xFFFF4052, 0xFFFFF830, 0x000051E0, 0x00000BB8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3B51)

    @scena.Lambda('lambda_3B6F')
    def lambda_3B6F():
        OP_99(0x00FE, 0x07, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3B6F)

    TerminateThread(0x0016, 0x01)
    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0800)
    OP_99(0x00FE, 0x00, 0x04, 0x00000DAC)
    WaitForThreadExit(0x00FE, 0x0003)
    PlayEffect(0x06, 0xFF, 0x0016, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)

    @scena.Lambda('lambda_3BE1')
    def lambda_3BE1():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_3BE1)

    @scena.Lambda('lambda_3BFB')
    def lambda_3BFB():
        OP_9F(0x0016, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_3BFB)

    OP_94(0x01, 0x0016, 0x0000, 0xFFFFE0C0, 0x00005DC0, 0x00)
    TerminateThread(0x0016, 0x01)
    OP_22(0x020B, 0x00, 0x64)
    SetChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0016, 0x0020)
    ClearChrFlags(0x0016, 0x0004)
    ClearChrFlags(0x00FE, 0x0800)
    OP_99(0x00FE, 0x04, 0x07, 0x000009C4)
    SetChrSubChip(0x00FE, 1)

    Return()

# id: 0x0025 offset: 0x3C42
@scena.Code('func_25_3C42')
def func_25_3C42():
    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0xFFFF506A, 0xFFFFF830, 0x000064FA, 0x0000044C, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x00FE, 225, 400)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 19)
    OP_8E(0x00FE, -48220, -2000, 23900, 6000, 0x00)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 20)

    @scena.Lambda('lambda_3C98')
    def lambda_3C98():
        OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3C98)

    Sleep(200)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    PlayEffect(0x06, 0xFF, 0x0014, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x0014, 0x03)
    SetChrChipByIndex(0x0014, 27)
    SetChrSubChip(0x0014, 0)

    @scena.Lambda('lambda_3D01')
    def lambda_3D01():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3D01)

    WaitForThreadExit(0x00FE, 0x0002)

    @scena.Lambda('lambda_3D20')
    def lambda_3D20():
        OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3D20)

    Sleep(200)

    PlayEffect(0x06, 0xFF, 0x0014, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    TerminateThread(0x0014, 0x01)
    WaitForThreadExit(0x00FE, 0x0002)
    SetChrChipByIndex(0x0014, 14)
    SetChrSubChip(0x0014, 0)
    SetChrSubChip(0x00FE, 1)

    @scena.Lambda('lambda_3D93')
    def lambda_3D93():
        OP_96(0x00FE, 0xFFFF43A4, 0xFFFFF830, 0x00005D5C, 0x00000FA0, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3D93)

    WaitForThreadExit(0x00FE, 0x0003)

    @scena.Lambda('lambda_3DB6')
    def lambda_3DB6():
        OP_99(0x000E, 0x01, 0x04, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3DB6)

    CreateThread(0x0014, 0x03, 0x00, 0x0026)
    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0002)

    @scena.Lambda('lambda_3DD7')
    def lambda_3DD7():
        OP_96(0x00FE, 0xFFFF4548, 0xFFFFF830, 0x00005E88, 0x000007D0, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3DD7)

    SetChrSubChip(0x00FE, 1)
    OP_99(0x00FE, 0x00, 0x07, 0x00000FA0)
    OP_99(0x00FE, 0x00, 0x07, 0x00000FA0)
    ClearChrFlags(0x00FE, 0x0002)
    WaitForThreadExit(0x00FE, 0x0003)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_3E1B')
    def lambda_3E1B():
        ChrTurnDirection(0x00FE, 0x0017, 0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_3E1B)

    Return()

# id: 0x0026 offset: 0x3E24
@scena.Code('func_26_3E24')
def func_26_3E24():
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    PlayEffect(0x06, 0xFF, 0x0014, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrFlags(0x0014, 0x0020)
    SetChrChipByIndex(0x0014, 27)
    SetChrSubChip(0x0014, 0)

    @scena.Lambda('lambda_3E7F')
    def lambda_3E7F():
        OP_94(0x01, 0x0014, 0x0000, 0xFFFFEC78, 0x00005DC0, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0000, lambda_3E7F)

    @scena.Lambda('lambda_3E95')
    def lambda_3E95():
        OP_9F(0x0014, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_3E95)

    WaitForThreadExit(0x0014, 0x0000)
    OP_22(0x020B, 0x00, 0x64)
    SetChrFlags(0x0014, 0x0080)

    Return()

# id: 0x0027 offset: 0x3EB1
@scena.Code('func_27_3EB1')
def func_27_3EB1():
    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0xFFFF455C, 0xFFFFF830, 0x00006824, 0x000003E8, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x00FE, 225, 400)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 15)
    OP_8E(0x00FE, -51070, -2000, 24490, 6000, 0x00)
    SetChrFlags(0x0015, 0x0020)
    SetChrFlags(0x00FE, 0x0020)
    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 16)

    @scena.Lambda('lambda_3F11')
    def lambda_3F11():
        OP_99(0x00FE, 0x00, 0x05, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3F11)

    Sleep(200)

    PlayEffect(0x06, 0xFF, 0x0015, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    TerminateThread(0x0015, 0x03)
    SetChrChipByIndex(0x0015, 27)
    SetChrSubChip(0x0015, 0)

    @scena.Lambda('lambda_3F7A')
    def lambda_3F7A():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_3F7A)

    @scena.Lambda('lambda_3F94')
    def lambda_3F94():
        OP_99(0x00FE, 0x00, 0x05, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3F94)

    Sleep(200)

    PlayEffect(0x06, 0xFF, 0x0015, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    WaitForThreadExit(0x00FE, 0x0002)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_3FF9')
    def lambda_3FF9():
        OP_96(0x00FE, 0xFFFF4098, 0xFFFFF830, 0x000066BC, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3FF9)

    SetChrChipByIndex(0x000D, 18)
    SetChrSubChip(0x00FE, 1)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_4030')
    def lambda_4030():
        OP_8F(0x00FE, -51150, -2000, 24490, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4030)

    SetChrChipByIndex(0x000D, 16)
    SetChrSubChip(0x00FE, 0)
    OP_99(0x00FE, 0x00, 0x03, 0x00000BB8)
    WaitForThreadExit(0x00FE, 0x0003)
    PlayEffect(0x06, 0xFF, 0x0015, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)

    @scena.Lambda('lambda_40A9')
    def lambda_40A9():
        OP_9F(0x0015, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_40A9)

    OP_94(0x01, 0x0015, 0x0000, 0xFFFFE890, 0x00005DC0, 0x00)
    SetChrFlags(0x0015, 0x0080)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 9)
    OP_22(0x020B, 0x00, 0x64)
    ClearChrFlags(0x0015, 0x0020)
    OP_99(0x00FE, 0x04, 0x07, 0x000009C4)

    Return()

# id: 0x0028 offset: 0x40E7
@scena.Code('func_28_40E7')
def func_28_40E7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4106',
    )

    OP_22(0x013F, 0x00, 0x4B)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x4B)
    Sleep(300)

    Jump('func_28_40E7')

    def _loc_4106(): pass

    label('loc_4106')

    OP_22(0x013F, 0x00, 0x41)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x41)
    Sleep(300)

    OP_22(0x013F, 0x00, 0x37)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x37)
    Sleep(300)

    OP_22(0x013F, 0x00, 0x2D)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x2D)
    Sleep(300)

    OP_22(0x013F, 0x00, 0x23)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x23)
    Sleep(300)

    OP_22(0x013F, 0x00, 0x19)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x19)
    Sleep(300)

    Return()

# id: 0x0029 offset: 0x416B
@scena.Code('func_29_416B')
def func_29_416B():
    OP_8E(0x00FE, -41050, -2000, 31020, 3000, 0x00)

    @scena.Lambda('lambda_4185')
    def lambda_4185():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4185')

    DispatchAsync2(0x00FE, 0x0003, lambda_4185)

    Return()

# id: 0x002A offset: 0x4191
@scena.Code('func_2A_4191')
def func_2A_4191():
    OP_8E(0x00FE, -41720, -2000, 30190, 3000, 0x00)

    @scena.Lambda('lambda_41AB')
    def lambda_41AB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_41AB')

    DispatchAsync2(0x00FE, 0x0003, lambda_41AB)

    Return()

# id: 0x002B offset: 0x41B7
@scena.Code('func_2B_41B7')
def func_2B_41B7():
    OP_8E(0x00FE, -38900, -2009, 24770, 3000, 0x00)

    @scena.Lambda('lambda_41D1')
    def lambda_41D1():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_41D1')

    DispatchAsync2(0x00FE, 0x0003, lambda_41D1)

    Return()

# id: 0x002C offset: 0x41DD
@scena.Code('func_2C_41DD')
def func_2C_41DD():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, -37860, -1920, 31390, 5000, 0x00)
    OP_8E(0x00FE, -39030, -2000, 30210, 5000, 0x00)
    OP_8E(0x00FE, -39860, -2000, 28680, 5000, 0x00)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 13)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x002D offset: 0x4235
@scena.Code('func_2D_4235')
def func_2D_4235():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, -35480, -2000, 27380, 5000, 0x00)
    OP_8E(0x00FE, -38990, -2000, 26820, 5000, 0x00)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 13)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x002E offset: 0x4279
@scena.Code('func_2E_4279')
def func_2E_4279():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, -38990, -2000, 26820, 5000, 0x00)
    OP_8E(0x00FE, -40490, -2000, 28650, 5000, 0x00)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 13)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x002F offset: 0x42BD
@scena.Code('func_2F_42BD')
def func_2F_42BD():
    FadeOut(0, 0, -1)
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
        (0x00000000, 'loc_4337'),
        (0x00000001, 'loc_433D'),
        (-1, 'loc_4343'),
    )

    def _loc_4337(): pass

    label('loc_4337')

    OP_A2(0x1200)

    Jump('loc_4343')

    def _loc_433D(): pass

    label('loc_433D')

    OP_A2(0x1201)

    Jump('loc_4343')

    def _loc_4343(): pass

    label('loc_4343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4351',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4355')

    def _loc_4351(): pass

    label('loc_4351')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4355(): pass

    label('loc_4355')

    Return()

# id: 0x0030 offset: 0x4356
@scena.Code('func_30_4356')
def func_30_4356():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　玛西亚孤儿院',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0031 offset: 0x4399
@scena.Code('func_31_4399')
def func_31_4399():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　卢安市　　２３８塞尔矩\n',
            '西　玛诺利亚村　７４塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
