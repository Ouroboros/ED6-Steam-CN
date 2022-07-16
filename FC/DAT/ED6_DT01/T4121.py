import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4121_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4121   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '艾南'),
    TXT(0x02, '卡露娜'),
    TXT(0x03, '亚妮拉丝'),
    TXT(0x04, '库拉茨'),
    TXT(0x05, '克鲁茨'),
    TXT(0x06, '尤莉亚中尉'),
    TXT(0x07, '阿加特'),
    TXT(0x08, '雪拉扎德'),
    TXT(0x09, '金'),
    TXT(0x0A, '卡西乌斯'),
    TXT(0x0B, '费瑟尔'),
    TXT(0x0C, '罗伊德'),
    TXT(0x0D, '拜舍尔'),
    TXT(0x0E, '赫穆特'),
    TXT(0x0F, '玛多克工房长'),
    TXT(0x10, '克劳斯市长'),
    TXT(0x11, '奥利维尔'),
    TXT(0x12, '穆拉'),
    TXT(0x13, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4121.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T4121._SN', 'ED6_DT01/T4121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xCCBC
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
        ('ED6_DT07/CH02580._CH', 'ED6_DT07/CH02580P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT06/CH20112._CH', 'ED6_DT06/CH20112P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01633._CH', 'ED6_DT07/CH01633P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH02190._CH', 'ED6_DT07/CH02190P._CP'),
        ('ED6_DT06/CH20038._CH', 'ED6_DT06/CH20038P._CP'),
    ]

# id: 0x10002 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -4460,
            z                   = 0,
            y                   = 960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
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
            x                   = 27820,
            z                   = 0,
            y                   = 62520,
            direction           = 191,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 84510,
            z                   = 0,
            y                   = 56870,
            direction           = 274,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 90050,
            z                   = 0,
            y                   = 63770,
            direction           = 15,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 25740,
            z                   = 0,
            y                   = 58130,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 25470,
            z                   = 0,
            y                   = 58140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 31740,
            z                   = 0,
            y                   = 63030,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x392
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x392
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x392
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2600,
            triggerZ            = 0,
            triggerY            = 820,
            triggerRange        = 800,
            actorX              = -4460,
            actorZ              = 1500,
            actorY              = 960,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 27820,
            triggerZ            = 0,
            triggerY            = 60600,
            triggerRange        = 800,
            actorX              = 27820,
            actorZ              = 1500,
            actorY              = 62520,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4970,
            triggerZ            = 0,
            triggerY            = -1040,
            triggerRange        = 1400,
            actorX              = 4970,
            actorZ              = 2000,
            actorY              = -1040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3FE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_40C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000F)

    def _loc_40C(): pass

    label('loc_40C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_41A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0010)

    def _loc_41A(): pass

    label('loc_41A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_428',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0011)

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_436',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, 0x0012)

    def _loc_436(): pass

    label('loc_436')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_442'),
        (-1, 'loc_458'),
    )

    def _loc_442(): pass

    label('loc_442')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 1, 0x609)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_455',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 1, 0x609))
    Event(0, 0x000D)

    def _loc_455(): pass

    label('loc_455')

    Jump('loc_458')

    def _loc_458(): pass

    label('loc_458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_46C',
    )

    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)

    Jump('loc_664')

    def _loc_46C(): pass

    label('loc_46C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_476',
    )

    Jump('loc_664')

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 3, 0x64B)),
            Expr.Return,
        ),
        'loc_49A',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 120230, 0, -2360, 90)

    def _loc_49A(): pass

    label('loc_49A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 5, 0x64D)),
            Expr.Return,
        ),
        'loc_4B7',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 122900, 0, -2350, 270)

    def _loc_4B7(): pass

    label('loc_4B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Return,
        ),
        'loc_4D4',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 121650, 0, -3900, 0)

    def _loc_4D4(): pass

    label('loc_4D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Return,
        ),
        'loc_4F1',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 121680, 0, -830, 180)

    def _loc_4F1(): pass

    label('loc_4F1')

    Jump('loc_664')

    def _loc_4F4(): pass

    label('loc_4F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_538',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 62290, 0, -3770, 108)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 58990, 0, 2730, 7)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    Jump('loc_664')

    def _loc_538(): pass

    label('loc_538')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_547',
    )

    SetChrFlags(0x0014, 0x0080)

    Jump('loc_664')

    def _loc_547(): pass

    label('loc_547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_584',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 54920, 0, -3370, 95)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 58990, 0, 2730, 7)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    Jump('loc_664')

    def _loc_584(): pass

    label('loc_584')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5DE',
    )

    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 58990, 0, 2730, 7)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 15)
    SetChrFlags(0x000A, 0x0010)
    SetChrFlags(0x000A, 0x0004)
    TerminateThread(0x000A, 0xFF)
    SetChrPos(0x000A, 58500, 200, -3440, 90)

    Jump('loc_664')

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_61B',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 54920, 0, -3370, 95)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 58990, 0, 2730, 7)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    Jump('loc_664')

    def _loc_61B(): pass

    label('loc_61B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_62A',
    )

    ClearChrFlags(0x0015, 0x0080)

    Jump('loc_664')

    def _loc_62A(): pass

    label('loc_62A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_65D',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 15)
    SetChrFlags(0x000A, 0x0010)
    SetChrFlags(0x000A, 0x0004)
    TerminateThread(0x000A, 0xFF)
    SetChrPos(0x000A, 58500, 200, -3440, 90)

    Jump('loc_664')

    def _loc_65D(): pass

    label('loc_65D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_664',
    )

    def _loc_664(): pass

    label('loc_664')

    Return()

# id: 0x0001 offset: 0x665
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Neq,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6C),
            Expr.Neq,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6B),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_695',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_695(): pass

    label('loc_695')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_6A8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6B8')

    def _loc_6A8(): pass

    label('loc_6A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_6B8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6B8(): pass

    label('loc_6B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 7, 0x647)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6EB',
    )

    OP_B1('t4121_y')

    Jump('loc_6F4')

    def _loc_6EB(): pass

    label('loc_6EB')

    OP_B1('t4121_n')

    def _loc_6F4(): pass

    label('loc_6F4')

    Return()

# id: 0x0002 offset: 0x6F5
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_70A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_70A(): pass

    label('loc_70A')

    Return()

# id: 0x0003 offset: 0x70B
@scena.Code('func_03_70B')
def func_03_70B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_72E',
    )

    OP_8D(0x00FE, 84890, 62930, 95170, 65019, 2000)

    Jump('func_03_70B')

    def _loc_72E(): pass

    label('loc_72E')

    Return()

# id: 0x0004 offset: 0x72F
@scena.Code('func_04_72F')
def func_04_72F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            'Oh ho ho...',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话，我的确没有想到\n',
            '这里会是一个正式的俱乐部呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x780
@scena.Code('func_05_780')
def func_05_780():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_807',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会和诞辰庆典，\n',
            '都是全体市民\n',
            '参加的活动吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可就算是在这种活动当日，\n',
            '我们的社团里仍然有\n',
            '很多人继续去钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D23')

    def _loc_807(): pass

    label('loc_807')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_8F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_87F',
    )

    ChrTalk(
        0x00FE,
        (
            '对于喜好外出的我而言，\n',
            '像这样进退不能\n',
            '真是一种折磨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想快点乘坐飞艇\n',
            '到别的地方去钓鱼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F5')

    def _loc_87F(): pass

    label('loc_87F')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于喜好外出的我而言，\n',
            '像这样进退不能\n',
            '真是一种折磨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想快点乘坐飞艇\n',
            '到别的地方去钓鱼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F5(): pass

    label('loc_8F5')

    Jump('loc_D23')

    def _loc_8F8(): pass

    label('loc_8F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_98F',
    )

    ChrTalk(
        0x00FE,
        (
            '我本打算要去卢安，\n',
            '刚到达空港准备乘定期船，\n',
            '士兵们就突然来将空港封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '许久没有去海边垂钓了，\n',
            '本来还以为这次可以好好享受一番呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D23')

    def _loc_98F(): pass

    label('loc_98F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_A02',
    )

    ChrTalk(
        0x00FE,
        (
            '在今天举办的讲座上，\n',
            '有一位热心的女士\n',
            '迫切地希望加入我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '讲座结束后，\n',
            '她还留在湖边继续钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D23')

    def _loc_A02(): pass

    label('loc_A02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_A0C',
    )

    Jump('loc_D23')

    def _loc_A0C(): pass

    label('loc_A0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_AF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A7C',
    )

    ChrTalk(
        0x00FE,
        (
            '明天要举办一场\n',
            '面向新手的讲座。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于我们来说，\n',
            '如果能让参加者明白\n',
            '钓鱼的乐趣就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF6')

    def _loc_A7C(): pass

    label('loc_A7C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '明天要举办一场\n',
            '面向新手的讲座。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会有什么样的人来，\n',
            '我真是很期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能让他们明白\n',
            '钓鱼的乐趣就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF6(): pass

    label('loc_AF6')

    Jump('loc_D23')

    def _loc_AF9(): pass

    label('loc_AF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_B03',
    )

    Jump('loc_D23')

    def _loc_B03(): pass

    label('loc_B03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_B6A',
    )

    ChrTalk(
        0x00FE,
        (
            '为了钓鱼而事先做准备\n',
            '也很有乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根据自己想要\n',
            '钓上多大的鱼\n',
            '来决定带些什么渔具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D23')

    def _loc_B6A(): pass

    label('loc_B6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_BE3',
    )

    ChrTalk(
        0x00FE,
        (
            '本来觉得用自己做的鱼饵\n',
            '钓不到什么鱼，\n',
            '但实际钓起来却意外地管用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用自己做的鱼饵\n',
            '来钓鱼很令人开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D23')

    def _loc_BE3(): pass

    label('loc_BE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_C45',
    )

    ChrTalk(
        0x00FE,
        (
            '在卢安还是\n',
            '没能见到努西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在蔡斯也没有\n',
            '什么大的收获。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还要加把劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D23')

    def _loc_C45(): pass

    label('loc_C45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_D23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_CA0',
    )

    ChrTalk(
        0x00FE,
        (
            '团长费瑟尔先生\n',
            '原来是贵族出身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此我们都称他为\n',
            '『钓鱼男爵』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D23')

    def _loc_CA0(): pass

    label('loc_CA0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '团长费瑟尔先生\n',
            '原来是贵族出身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为非常喜欢钓鱼，\n',
            '所以倾尽财产\n',
            '成立了钓公师团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此我们都称他为\n',
            '『钓鱼男爵』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D23(): pass

    label('loc_D23')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xD27
@scena.Code('func_06_D27')
def func_06_D27():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D82',
    )

    ChrTalk(
        0x00FE,
        (
            '为了发动政变而进行封锁，\n',
            '剥夺了我们钓鱼的权利，\n',
            '理查德上校真是不可饶恕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_D82(): pass

    label('loc_D82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_DEB',
    )

    ChrTalk(
        0x00FE,
        (
            '雷那特川……\n',
            '瓦雷利亚湖……\n',
            '亚瑟利亚湾都在呼唤我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，拜托了，\n',
            '让我拿起钓鱼竿吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_DEB(): pass

    label('loc_DEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_EAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_E42',
    )

    ChrTalk(
        0x00FE,
        (
            '不能去钓鱼，\n',
            '对于我来说\n',
            '可是痛苦万分的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我都快发疯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAA')

    def _loc_E42(): pass

    label('loc_E42')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '什么时候\n',
            '才能到外地去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能去钓鱼，\n',
            '对于我来说\n',
            '可是痛苦万分的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我都快发疯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAA(): pass

    label('loc_EAA')

    Jump('loc_13C4')

    def _loc_EAD(): pass

    label('loc_EAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_F0C',
    )

    ChrTalk(
        0x00FE,
        (
            '不快点逮捕\n',
            '恐怖分子的话，\n',
            '就不能安心去钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '快点采取行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_F0C(): pass

    label('loc_F0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_F63',
    )

    ChrTalk(
        0x00FE,
        (
            '拜舍尔今天要出席一个讲座。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '努力推广钓鱼运动\n',
            '也是我们的职责之一啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_F63(): pass

    label('loc_F63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_FCB',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天入团考试时\n',
            '钓场的条件真不错啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我是考官，\n',
            '不过不由自主就想垂下鱼竿钓鱼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_FCB(): pass

    label('loc_FCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_FD5',
    )

    Jump('loc_13C4')

    def _loc_FD5(): pass

    label('loc_FD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1036',
    )

    ChrTalk(
        0x00FE,
        (
            '因为我是\n',
            '明天入团测试的考官，\n',
            '所以必须得到湖畔去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要趁现在\n',
            '赶快准备好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_1036(): pass

    label('loc_1036')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1155',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_10B5',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔虽说是个小国，\n',
            '但海、河、湖这些\n',
            '适合钓鱼的场所非常多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '开拓新的钓场\n',
            '也是我们的任务哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1152')

    def _loc_10B5(): pass

    label('loc_10B5')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '利贝尔虽说是个小国，\n',
            '但对钓鱼爱好者而言是个很不错的国家哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '海、河、湖这些\n',
            '适合钓鱼的场所所非常多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '开拓新的钓场\n',
            '也是我们的任务哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1152(): pass

    label('loc_1152')

    Jump('loc_13C4')

    def _loc_1155(): pass

    label('loc_1155')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_11CD',
    )

    ChrTalk(
        0x00FE,
        (
            '瓦雷利亚湖的努西\n',
            '因为气温下降\n',
            '而潜入较深的水域了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是这样，\n',
            '我也要知难而进，\n',
            '再一次把它找出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_11CD(): pass

    label('loc_11CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_13C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_123E',
    )

    ChrTalk(
        0x00FE,
        (
            '我追寻瓦雷利亚湖的努西\n',
            '已经接近五年了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次是第２３回的挑战，\n',
            '一定要把它给钓上来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C4')

    def _loc_123E(): pass

    label('loc_123E')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎来到钓公师团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们不就是到柏斯的湖畔\n',
            '调查事件的游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#004F啊，\n',
            '您是把空贼的情报告诉我们的那位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～哈～想起来了啊。\n',
            '再次欢迎来到钓公师团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F钓公师团……\n',
            '我是觉得有些耳熟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正如你所知，\n',
            '这里是我们活动的根据地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请在这里好好放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C4(): pass

    label('loc_13C4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x13C8
@scena.Code('func_07_13C8')
def func_07_13C8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0550140897V#800F钓鱼用具是一种功能性\n',
            '和艺术性兼备的道具。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550140898V#801F就算不钓鱼，\n',
            '也还是想要啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1433
@scena.Code('func_08_1433')
def func_08_1433():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0340140899V#600F短短的时间内就发生了那么多事，\n',
            '让人的心情难以平静啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340140900V到瓦雷利亚湖去垂钓，\n',
            '放松一下心情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x14AF
@scena.Code('func_09_14AF')
def func_09_14AF():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x14B4
@scena.Code('func_0A_14B4')
def func_0A_14B4():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 4, 0x67C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1852',
    )

    SetScenaFlags(ScenaFlag(0x00CF, 4, 0x67C))

    ChrTalk(
        0x0012,
        (
            '哈哈！\n',
            '欢迎来到钓公师团！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F钓公师团？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '利贝尔各地的钓鱼场\n',
            '潜藏着一种\n',
            '名为『努西』的巨大鱼类……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '找到它们，\n',
            '并顺利钓到手\n',
            '就是我们的最终目标！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F哈～\n',
            '原来是钓鱼爱好者的集团嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我也喜欢钓鱼，\n',
            '对这里也比较感兴趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F不过我看了看，\n',
            '似乎举办的活动都是非常正式的吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '嗯，我们这些志同道合的人\n',
            '为了达成宏伟的宿愿，\n',
            '在利贝尔各地日复一日地开展活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '为了尽量推广钓鱼这项运动，\n',
            '我们还开办了面向初学者的课程，\n',
            '并且出售自制的钓鱼用具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '从中获得的利益\n',
            '会作为保护钓场环境的委托金\n',
            '交纳给女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哇，\n',
            '的确是非常专业嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F不愧是真正的爱好者集团啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那么你们愿意加入我们的团队吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '如果想加入的话，\n',
            '是需要进行考试的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F这、这个，虽然很有趣，\n',
            '但我们现在还有事情要办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '这样啊，\n',
            '你们两个看起来很有潜力呢，\n',
            '不加入实在是有些可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '如果改变主意了，\n',
            '随时都可以来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我们真诚期待着\n',
            '希望入团的志愿者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202D')

    def _loc_1852(): pass

    label('loc_1852')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1946',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_18B7',
    )

    ChrTalk(
        0x0012,
        (
            '前些日子新加入了\n',
            '一位很有前途的女士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '成为本团的一员\n',
            '是十分值得庆贺的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1943')

    def _loc_18B7(): pass

    label('loc_18B7')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0012,
        (
            '前些日子新加入了\n',
            '一位很有前途的女士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '成为本团的一员\n',
            '是十分值得庆贺的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '嗯嗯，虽说她是个新手，\n',
            '但使用钓鱼竿的技术不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1943(): pass

    label('loc_1943')

    Jump('loc_202D')

    def _loc_1946(): pass

    label('loc_1946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_19AB',
    )

    ChrTalk(
        0x0012,
        (
            '直到刚才，\n',
            '外面还在吵吵嚷嚷的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '如果在钓场\n',
            '也那么吵闹的话，\n',
            '就没办法钓到鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202D')

    def _loc_19AB(): pass

    label('loc_19AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1AB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1A25',
    )

    ChrTalk(
        0x0012,
        (
            '现在既不能夜间外出，\n',
            '也不能到外地去，\n',
            '真是难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '这真是我团创立以来\n',
            '遇到的最糟糕的情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB4')

    def _loc_1A25(): pass

    label('loc_1A25')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0012,
        (
            '因为禁止夜间外出，\n',
            '所以现在不能去夜钓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '不但如此，\n',
            '现在就连去外地\n',
            '钓鱼也不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '这真是我团创立以来\n',
            '遇到的最糟糕的情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AB4(): pass

    label('loc_1AB4')

    Jump('loc_202D')

    def _loc_1AB7(): pass

    label('loc_1AB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1B1A',
    )

    ChrTalk(
        0x0012,
        (
            '今天的天气很好，\n',
            '非常适合\n',
            '去钓场钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '工作结束后，\n',
            '和团员们一起去湖边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202D')

    def _loc_1B1A(): pass

    label('loc_1B1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1BAB',
    )

    ChrTalk(
        0x0012,
        (
            '昨天，来了一位客人，\n',
            '虽然是一位初学者，\n',
            '不过却对钓鱼抱有非常浓厚的兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我们的组织能够打动人心，\n',
            '归功于拜舍尔不懈的宣传啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202D')

    def _loc_1BAB(): pass

    label('loc_1BAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1CEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1C48',
    )

    ChrTalk(
        0x0012,
        (
            '只要您打心眼里喜欢钓鱼，\n',
            '并且有一定的基本技术，\n',
            '就欢迎您加入我们的行列。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '今天的考生技术还可以，\n',
            '但是感受不到\n',
            '他们的干劲及热情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CEB')

    def _loc_1C48(): pass

    label('loc_1C48')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0012,
        (
            '只要您打心眼里喜欢钓鱼，\n',
            '并且有一定的基本技术，\n',
            '就欢迎您加入我们的行列。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '今天的考生技术还可以，\n',
            '但是感受不到\n',
            '他们的干劲及热情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '唉，真是可惜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CEB(): pass

    label('loc_1CEB')

    Jump('loc_202D')

    def _loc_1CEE(): pass

    label('loc_1CEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1D4A',
    )

    ChrTalk(
        0x0012,
        (
            '今天要在瓦雷利亚湖\n',
            '举行入团考试呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '团员们作为监考官，\n',
            '全都倾巢而出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202D')

    def _loc_1D4A(): pass

    label('loc_1D4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1E86',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1DDB',
    )

    ChrTalk(
        0x0012,
        (
            '如果真的喜欢钓鱼，\n',
            '那么遵守钓鱼场的规则\n',
            '是理所应当要做到的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '团员一旦在钓鱼场\n',
            '乱丢垃圾的话，\n',
            '我们就会立刻责令其退团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1DDB(): pass

    label('loc_1DDB')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0012,
        (
            '如果真的喜欢钓鱼，\n',
            '那么遵守钓鱼场的规则\n',
            '是理所应当要做到的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '团员一旦在钓鱼场\n',
            '乱丢垃圾的话，\n',
            '我们就会立刻责令其退团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '但我相信\n',
            '不会有那样无知的人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E83(): pass

    label('loc_1E83')

    Jump('loc_202D')

    def _loc_1E86(): pass

    label('loc_1E86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1F5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1EEB',
    )

    ChrTalk(
        0x0012,
        (
            '我们这里销售的\n',
            '钓鱼用具广受好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '甚至还有顾客\n',
            '从很远的地方乘坐飞艇来买。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F5A')

    def _loc_1EEB(): pass

    label('loc_1EEB')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0012,
        (
            '我们这里销售的\n',
            '钓鱼用具广受好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '甚至还有顾客\n',
            '从很远的地方乘坐飞艇来买。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '以上所说绝无虚言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F5A(): pass

    label('loc_1F5A')

    Jump('loc_202D')

    def _loc_1F5D(): pass

    label('loc_1F5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1FD2',
    )

    ChrTalk(
        0x0012,
        (
            '就像武术大会一样，\n',
            '我们也要招募参加者\n',
            '来举行一次钓鱼大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '当然，我也会参加。\n',
            '我可是不会认输的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202D')

    def _loc_1FD2(): pass

    label('loc_1FD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_202D',
    )

    ChrTalk(
        0x0012,
        (
            '如果你们改变主意了，\n',
            '随时都可以来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我们真诚期待着\n',
            '希望入团的志愿者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_202D(): pass

    label('loc_202D')

    TalkEnd(0x0012)

    Return()

# id: 0x000B offset: 0x2031
@scena.Code('func_0B_2031')
def func_0B_2031():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x2036
@scena.Code('func_0C_2036')
def func_0C_2036():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22C3',
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
            TXT(0x01, '报告\n'),
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
        'loc_22B2',
    )

    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x004B, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x004B, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21D0',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101170V#760F各位，你们辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101171V#760F艾尔贝离宫解放作战\n',
            '干得相当漂亮。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101172V好不容易有这个机会，\n',
            '就把报酬给你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101173V可以作为今后作战必要的资金。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_AF(0x63, 0x004B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x004C, 0x04, 0x10)
    OP_28(0x004C, 0x04, 0x20)

    ChrTalk(
        0x0008,
        (
            '#0590101174V#760F继续保持警惕前进吧，\n',
            '祝你们好运。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101175V我们也会尽全力给你们以支援的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22AC')

    def _loc_21D0(): pass

    label('loc_21D0')

    If(
        (
            (Expr.Eval, "OP_A9(0x63)"),
            Expr.Return,
        ),
        'loc_2244',
    )

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0590101111V#760F辛苦了。\n',
            '看来顺利地完成了任务呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101112V如果完成其他任务的话，\n',
            '请再来我这里报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22AC')

    def _loc_2244(): pass

    label('loc_2244')

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0590101113V#760F现在好像没有需要报告的任务。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101112V如果完成其他任务的话，\n',
            '请再来我这里报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22AC(): pass

    label('loc_22AC')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_22B2(): pass

    label('loc_22B2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22C3',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_22C3(): pass

    label('loc_22C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_249C',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0008,
        (
            '#0590130513V#760F哦，是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130506V一旦开始作战，\n',
            '就没有机会回到市区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130515V已经准备完毕了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【准备好了】\n'),
            TXT(0x01, '【还没有准备好】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_23A7'),
        (0x00000001, 'loc_2447'),
        (-1, 'loc_2499'),
    )

    def _loc_23A7(): pass

    label('loc_23A7')

    SetScenaFlags(ScenaFlag(0x00CA, 0, 0x650))
    OP_28(0x004C, 0x04, 0x02)
    OP_28(0x004C, 0x04, 0x04)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)

    ChrTalk(
        0x0008,
        (
            '#0590130516V#764F好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130517V#762F那么就请在此等候，\n',
            '时间一到就开始作战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4111._SN', 100, 0, 0)
    IdleLoop()

    Return()

    def _loc_2447(): pass

    label('loc_2447')

    ChrTalk(
        0x0008,
        (
            '#0590130518V#760F我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130519V你们准备好的话请和我说一声。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 0)
    OP_4B(0x0008, 255)
    EventEnd(0x01)

    Return()

    def _loc_2499(): pass

    label('loc_2499')

    Jump('loc_72DA')

    def _loc_249C(): pass

    label('loc_249C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 3, 0x64B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 5, 0x64D)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 6, 0x64E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 7, 0x64F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_433D',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00CA, 0, 0x650))
    OP_28(0x004B, 0x01, 0x0800)
    OP_28(0x004B, 0x01, 0x1000)
    Fade(1000)
    OP_4A(0x0008, 255)
    CameraMove(-3330, 0, 750, 0)
    SetChrPos(0x0101, -2590, 0, 280, 270)
    SetChrPos(0x0102, -2590, 0, 1220, 270)
    SetChrPos(0x0108, -1500, 0, 750, 270)
    SetChrDirection(0x0008, 90, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0590130397V#760F其他的几位游击士已经全部集中起来了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130398V和记者还有亲卫队的人员取得了联络吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130399V#007F很遗憾……\n',
            '和他们两方都没能取得联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130400V#010F但必要的情报基本上都收集好了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向众人说明了\n',
            '在杂志社和大圣堂打听到的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590130401V#764F原来如此……\n',
            '科洛蒂娅公主被囚禁在艾尔贝离宫\n',
            '这一点已经确信无疑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130402V#762F亲卫队没来虽然很遗憾，\n',
            '但已经知道他们没有被捕，\n',
            '这样已经足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130403V#070F那么我们这就开始好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130404V#760F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130405V全体人员。\n',
            '现在开始制定作战计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    CameraMove(122020, 0, -2070, 0)
    OP_67(0, 6320, -10000, 0)
    CameraSetDistance(1200, 0)
    OP_6C(315000, 0)
    OP_6E(678, 0)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000C, 123360, 0, -2490, 1)
    SetChrPos(0x0009, 123640, 0, -1210, 350)
    SetChrPos(0x000B, 125100, 0, -1960, 320)
    SetChrPos(0x000A, 124920, 0, -560, 315)
    SetChrPos(0x0101, 120480, 0, 820, 90)
    SetChrPos(0x0102, 120560, 0, -380, 45)
    SetChrPos(0x0108, 121320, 0, -1960, 0)
    SetChrPos(0x0008, 122790, 0, 1800, 180)
    OP_4A(0x000C, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000A, 255)
    PlayBGM(101)
    FadeIn(2000, 0)
    CameraMove(122020, 0, 1070, 2500)

    ChrTalk(
        0x0008,
        (
            '#0590130406V#764F……以上所说的就是\n',
            '情报部正在发动的政变的详细情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130407V#762F根据这些事实，\n',
            '王都支部决定接受女王陛下的委托。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330130408V#844F没想到竟然有如此大的阴谋\n',
            '正在进行着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130409V连这种事情都看不穿，\n',
            '真恨自己这样没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120130410V#813F虽然之前就觉得\n',
            '那一伙特务兵比较可疑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120130411V但我一直认为理查德上校\n',
            '看起来是个好人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320130412V#833F非但不是，\n',
            '而且他居然还是空贼事件和\n',
            '戴尔蒙市长事件的幕后操纵者……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320130413V#832F这不就是在小瞧\n',
            '我们这些游击士吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310130414V#822F如果不给个说法，\n',
            '我们是无论如何也不会接受的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130415V#760F那么各位，请你们协助我们好吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310130416V#820F那是当然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320130417V#830F我会听从吩咐的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330130418V#840F我要让他们……加倍偿还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120130419V#816F请让我也加入你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130420V#008F哇啊～……这可太好了！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130421V#010F嗯……\n',
            '的确大家都是很值得信赖的伙伴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130422V#764F接下来就开始制定救出作战计划。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C08')
    def lambda_2C08():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C08)

    @scena.Lambda('lambda_2C16')
    def lambda_2C16():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2C16)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0590130423V#762F人质的性命最为要紧，\n',
            '所以不能进行持久战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130424V我们只有采取强行攻入，\n',
            '然后各个击破这种作战方法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310130425V#824F没有时间去探明进攻线路了，\n',
            '看来也只有采取这个办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320130426V#832F可是要进攻离宫的话，\n',
            '不如分别行动怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330130427V#840F……佯攻组和突入组，\n',
            '兵分两路行事比较可靠。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130428V如果给敌人制造了骚乱的话，\n',
            '就可以吸引敌人的大部分战斗力，\n',
            '然后突入队员就可以乘机冲进去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130429V#070F#5P但大家不要忘记了，对手可是\n',
            '王国军中精英级别的情报部特别部队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130430V我想说的是，作战中最好还要有\n',
            '佯攻时的伏击组以及突入时的扰乱组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130431V#004F#5P咦……\n',
            '这是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130432V#010F首先佯攻组佯攻，\n',
            '然后伏击组以逸待劳地痛击追来的敌人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130433V扰乱组给敌人制造混乱，\n',
            '让突入组的行动变得轻而易举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130434V#501F#5P原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130435V#505F可是就我们这几个人，\n',
            '要想那样分配有些勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130436V#765F嗯……没办法啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130437V虽然联络了其他支部，\n',
            '但是由于关所和飞艇坪都被封锁了，\n',
            '那些游击士就来不了这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2FF6')
    def lambda_2FF6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2FF6)

    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130438V#007F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130439V#003F如果这个时候雪拉姐和\n',
            '阿加特他们在就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130440V#764F……金先生说得很对，\n',
            '只分为佯攻和突入两个组危险性较大。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130441V或许只有重新制定其他的方案了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000D, 123420, -2000, 4570, 270)

    NpcTalk(
        0x000D,
        '女性的声音',
        (
            '#0100130442V#1P不必了。\n',
            '不足的战斗力由我们来补充。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000D, 0x0080)
    SetChrChipByIndex(0x000D, 6)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_31EC')
    def lambda_31EC():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_31EC')

    DispatchAsync2(0x0101, 0x0001, lambda_31EC)

    @scena.Lambda('lambda_31FD')
    def lambda_31FD():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_31FD')

    DispatchAsync2(0x0102, 0x0001, lambda_31FD)

    @scena.Lambda('lambda_320E')
    def lambda_320E():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_320E')

    DispatchAsync2(0x0108, 0x0001, lambda_320E)

    @scena.Lambda('lambda_321F')
    def lambda_321F():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_321F')

    DispatchAsync2(0x000B, 0x0001, lambda_321F)

    @scena.Lambda('lambda_3230')
    def lambda_3230():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_3230')

    DispatchAsync2(0x0009, 0x0001, lambda_3230)

    @scena.Lambda('lambda_3241')
    def lambda_3241():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_3241')

    DispatchAsync2(0x000C, 0x0001, lambda_3241)

    @scena.Lambda('lambda_3252')
    def lambda_3252():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_3252')

    DispatchAsync2(0x000A, 0x0001, lambda_3252)

    @scena.Lambda('lambda_3263')
    def lambda_3263():
        SetChrDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3263)

    SetChrFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_3276')
    def lambda_3276():
        ChrMoveTo(0x00FE, 122080, 0, 1850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3276)

    @scena.Lambda('lambda_3291')
    def lambda_3291():
        ChrWalkTo(0x00FE, 120190, 0, 4910, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3291)

    CameraMove(120550, 0, 3300, 2000)
    WaitForThreadExit(0x000D, 0x0001)
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130443V#004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130444V#014F#5P尤莉亚中尉……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130445V#073F#5P哦，这位不就是\n',
            '我们在周游道遇见的修女吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3349')
    def lambda_3349():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_3349')

    DispatchAsync2(0x0008, 0x0001, lambda_3349)

    @scena.Lambda('lambda_335A')
    def lambda_335A():
        ChrWalkTo(0x00FE, 119930, 0, 3060, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_335A)

    CameraMove(121320, 0, 1770, 2000)
    WaitForThreadExit(0x000D, 0x0001)
    Fade(1000)
    SetChrChipByIndex(0x000D, 5)
    ChrTurnDirection(0x000D, 0x0008, 400)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0100130446V#465F初次见面，你们好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111326V#460F我是王室亲卫队的中队长，\n',
            '尤莉亚·舒华兹中尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130448V请让我们亲卫队来协助你们的作战。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(122540, 0, 820, 0)
    OP_67(0, 6320, -10000, 0)
    CameraSetDistance(1200, 0)
    OP_6C(315000, 0)
    OP_6E(678, 0)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000D, 0xFF)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000C, 124600, 0, -2300, 340)
    SetChrPos(0x0009, 124530, 0, -1010, 319)
    SetChrPos(0x000B, 125530, 0, -570, 294)
    SetChrPos(0x000A, 125290, 0, 750, 284)
    SetChrPos(0x0101, 120540, 0, 1210, 75)
    SetChrPos(0x0102, 120520, 0, 190, 45)
    SetChrPos(0x0108, 120880, 0, -1300, 64)
    SetChrPos(0x0008, 122790, 0, 1800, 180)
    SetChrPos(0x000D, 122810, 0, -1980, 7)
    ChrTurnDirection(0x000C, 0x000D, 0)
    ChrTurnDirection(0x0009, 0x000D, 0)
    ChrTurnDirection(0x000B, 0x000D, 0)
    ChrTurnDirection(0x000A, 0x000D, 0)
    ChrTurnDirection(0x0101, 0x000D, 0)
    ChrTurnDirection(0x0102, 0x000D, 0)
    ChrTurnDirection(0x0108, 0x000D, 0)
    ChrTurnDirection(0x0008, 0x000D, 0)
    ChrTurnDirection(0x000D, 0x0008, 0)
    Sleep(500)

    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0590130449V#760F原来如此……\n',
            '您的意思我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130450V包括您在内的八名队员将协助\n',
            '我们的营救作战计划对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130451V#460F我的队员虽然分散潜伏在王都里面。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130452V但是他们在一小时之内就能集合到一起。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130453V#505F#5P这、这样就好了，可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130454V尤莉亚小姐，\n',
            '您是怎么得知我们要去营救人质的呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130455V#010F我们为了转达这个消息到了大圣堂一趟，\n',
            '但是没能见到尤莉亚中尉您的身影。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130456V#465F这样啊……真是对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130457V#460F不过我知道你们接受了陛下的委托。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130458V而且就在昨天晚上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130459V#004F#5P昨天晚上！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130460V就是说在我们与女王陛下见面之后？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130461V#461F呵呵……是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130462V总之，我们拥有连情报部\n',
            '都不知道的特殊联络方法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130463V前来协助你们也是陛下的指示。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130464V#505F#5P特殊的联络方法？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130465V#464F嗯，该怎么说好呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130466V#070F#5P嗯，这样就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130467V总算确保可以分为伏击组和扰乱组了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130468V#761F是啊，这样一来，\n',
            '作战的成功率就大幅上升了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130469V我们立刻决定人员的分配吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130470V#465F明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130471V#462F首先是佯攻组……\n',
            '就由我们亲卫队中的四名成员来担任吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310130472V#820F的确，\n',
            '正在被通缉的你们如果现身的话，\n',
            '可以很有效地吸引敌人注意力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130473V#460F啊，确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130474V具体来说，就是以在周游道外停放的\n',
            '情报部的特务飞艇为目标。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130475V#580F#5P特务飞艇……\n',
            '就是特务兵乘坐的那个！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130476V#012F周游道外围停放有飞艇……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130477V#072F#5P对了，就是那个封锁住不让人进去的\n',
            '所谓军事禁区……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130478V#460F据我调查，\n',
            '有数名特务兵是经常在那里看守的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130479V对那里展开进攻后，与离宫保持联络的\n',
            '支援部队就会朝着那里赶去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120130480V#814F啊，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120130481V#850F那个支援部队就是伏击组\n',
            '要攻击的目标对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330130482V#840F#6P这样的话，\n',
            '伏击组就由我们四人来担当吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310130483V#821F没错，在执行剿灭魔兽的任务时\n',
            '就已经习惯了森林里的战斗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320130484V#830F我们之中也有用枪作为兵器的……\n',
            '真是再合适不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130485V#764F确实是人尽其材啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130486V#760F接下来是扰乱组和突入组……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130487V#460F和佯攻组一样，\n',
            '扰乱组就由亲卫队成员担当吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130488V由他们将特务兵的注意力吸引过来。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130489V#006F#5P……这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130490V#010F我们就是突入组了，\n',
            '负责解救人质对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080130491V#070F#5P大家各自的行动都是为\n',
            '我们这最重要的角色所做的准备工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130492V一定要鼓足干劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130493V#007F#5P话、话是这么说，\n',
            '可多少还是感觉有压力呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    @scena.Lambda('lambda_3E96')
    def lambda_3E96():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3E96)

    ChrTurnDirection(0x0009, 0x0101, 400)

    @scena.Lambda('lambda_3EAB')
    def lambda_3EAB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3EAB)

    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0100130494V#461F呵呵……\n',
            '不用担心那么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320130495V#831F不管怎么说，\n',
            '你们都是武术大会的优胜组对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330130496V#841F#6P大部分敌人\n',
            '都是奈何不了我们的。',
            TxtCtl.Enter,
            '#0330130497V#6P你们只需要考虑\n',
            '救出人质这一点就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130498V#501F#5P尤莉亚中尉……各位前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130499V#019F并不是只有我们参与营救人质哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130500V集合大家的力量一定没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130501V#006F#5P嗯……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130502V好的！\n',
            '大干一场吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130503V#071F#5P哦哦，很有干劲嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130504V#764F作战会议到此结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_40A0')
    def lambda_40A0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_40A0)

    @scena.Lambda('lambda_40AE')
    def lambda_40AE():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_40AE)

    @scena.Lambda('lambda_40BC')
    def lambda_40BC():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_40BC)

    @scena.Lambda('lambda_40CA')
    def lambda_40CA():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_40CA)

    @scena.Lambda('lambda_40D8')
    def lambda_40D8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_40D8)

    @scena.Lambda('lambda_40E6')
    def lambda_40E6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_40E6)

    @scena.Lambda('lambda_40F4')
    def lambda_40F4():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_40F4)

    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0590130505V#760F作战计划今夜执行……\n',
            '希望各位能巧妙借助这个黑夜取得成功。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130506V一旦开始作战，\n',
            '就没有机会回到市区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130507V趁这段时间，\n',
            '把缺少的东西补充齐备如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130508V#006F啊，说的也是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0100130509V#465F我这就去和潜伏在王都的部下联络。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130510V#010F那么我们就暂时先分头行事吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0101, 119650, 0, 1610, 0)
    SetChrPos(0x0102, 119650, 0, 1610, 0)
    SetChrPos(0x0108, 119650, 0, 1610, 0)
    SetChrPos(0x0008, -4460, 0, 960, 90)
    SetChrPos(0x0009, 120230, 0, -2360, 90)
    SetChrPos(0x000C, 122900, 0, -2350, 270)
    SetChrPos(0x000B, 121650, 0, -3900, 0)
    SetChrPos(0x000A, 121680, 0, -830, 180)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000D, 0x0080)
    CameraMove(119650, 0, 1610, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_72DA')

    def _loc_433D(): pass

    label('loc_433D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5043',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00C5, 0, 0x628))
    OP_28(0x0048, 0x01, 0x0080)
    Fade(1000)
    CameraMove(-4030, 0, 1100, 0)
    SetChrPos(0x0101, -2590, 0, 280, 270)
    SetChrPos(0x0102, -2590, 0, 1220, 270)
    SetChrSubChip(0x0008, 0)
    SetChrDirection(0x0008, 90, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DF, 2, 0x6FA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_458C',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101135V#761F艾丝蒂尔、约修亚。\n',
            '听说你们顺利地进入决赛了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101136V虽然对克鲁茨他们来说有点遗憾，\n',
            '不过听说比赛打得很精彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101137V#006F嗯，真是白热化的战斗啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101138V#007F不过，和各位前辈比起来，\n',
            '我们的实力还需要有待提高呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101139V#010F说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101140V金先生就不用说了，\n',
            '奥利维尔的枪法和魔法也帮了很大的忙。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101141V我们以后还要加倍努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101142V#761F呵呵，有这种上进的意识，\n',
            '我想你们一定会不断地进步的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101143V#760F对了，\n',
            '今天有没有打听到什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45F0')

    def _loc_458C(): pass

    label('loc_458C')

    ChrTalk(
        0x0008,
        (
            '#0590111083V#760F艾丝蒂尔、约修亚。\n',
            '《利贝尔通讯》那边怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111084V有没有从那里得到什么情报？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45F0(): pass

    label('loc_45F0')

    ChrTalk(
        0x0102,
        (
            '#0020111085V#012F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚把奈尔调查到的情报报告给了艾南。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590111086V#763F原来如此……\n',
            '洛伦斯少尉是『猎兵团』出身啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111087V#764F『杰斯塔猎兵团』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111088V没有听说过的名字呢。\n',
            '看来我要好好去调查一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111089V#014F游击士协会和猎兵团也有交往吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111090V#762F不，双方可以说是商业上的竞争对手。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111091V我们的规约是不能参与国家之间的战争，\n',
            '而对他们来说这却是买卖的所在。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111092V在纷争不断的边境等地，\n',
            '我们协会为了普通居民的安全，\n',
            '曾经多次与他们处于对立的境地呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111093V#007F……真是让人没有好感的组织啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111094V#505F但是……\n',
            '这样不就没办法取得他们的情报了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111095V#760F这点不用担心。\n',
            '俗语有说『蛇行蛇道』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111096V不过收集情报可能要花两三天时间。\n',
            '会赶不上决赛的……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111097V这样也没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111098V#006F啊，没什么。\n',
            '这不只是和大会有关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111099V#015F拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111100V#764F还有一条情报就是……\n',
            '关于理查德上校在寻找\n',
            '科洛蒂娅公主结婚对象的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111101V其实……\n',
            '和这个有关的情报也不是没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111102V#004F……怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111103V#760F好像在女王诞辰庆典那天\n',
            '有一位埃雷波尼亚的皇族成员要来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111104V虽然现在还不知道他的名字……\n',
            '不过帝国的皇族自从十年前的\n',
            '侵略战争以来还没有访问过利贝尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111105V#010F原来如此，\n',
            '感觉与之前的谈话很有关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111106V#505F埃雷波尼亚的皇族吗。\n',
            '是什么样的人，我们完全不知道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111107V说起来，我们认识的帝国人\n',
            '就只有奥利维尔一个呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111108V#765F而且，科洛蒂娅公主才刚刚１６岁。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111109V这么着急结婚确实有点不自然啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111110V#004F哎，是吗！？\n',
            '不就是和我们一样大嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111111V#015F对于上流阶级，\n',
            '这正好是在社交界出道的年龄。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111112V#013F不过，以前从来没有听说过，\n',
            '这个年龄结婚也太早了点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111113V#762F但是……\n',
            '说不定这其中会有什么特别的理由。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111114V我觉得有调查的价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111115V#006F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111116V如果顺利地被招待入城的话，\n',
            '也打听一下这方面的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111117V#010F为了这个，\n',
            '明天的比赛说什么也要取胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111118V#764F嗯……\n',
            '虽然可能会有点危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111119V把这个给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '地下水路的钥匙Ｂ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x036E, 1)

    ChrTalk(
        0x0101,
        (
            '#0010111120V#004F哎，这个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111121V#760F是王都支部管理的\n',
            '地下水路钥匙的其中一把。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111122V用这把钥匙可以打开\n',
            '王立竞技场旁边的地下水路入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111123V不过，进入那边的区域之后，\n',
            '可能会遇到相当强大的魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111124V#001F这正是我想要的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111125V和那些家伙战斗之前，\n',
            '能再锻炼一下实在是很必要呢！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111126V#010F艾南先生，\n',
            '实在是太感谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590111127V#760F没什么，这也是身为负责人的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590111128V不过，如果只有你们两人，\n',
            '记住一定不要贸然进去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111129V#006F知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111130V明天早上和金先生他们会合之后\n',
            '再进去里面看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene('ED6_DT01/T4150._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_72DA')

    def _loc_5043(): pass

    label('loc_5043')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 7, 0x61F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5926',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00C3, 7, 0x61F))
    OP_28(0x0047, 0x01, 0x0200)
    Fade(1000)
    CameraMove(-4030, 0, 1100, 0)
    SetChrPos(0x0101, -2590, 0, 280, 270)
    SetChrPos(0x0102, -2590, 0, 1220, 270)
    SetChrSubChip(0x0008, 0)
    SetChrDirection(0x0008, 90, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0590110388V#761F啊，你们回来了。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110389V恭喜你们通过第一场比赛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110390V#506F嘿嘿，过奖过奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110391V#501F对了，艾南哥哥。\n',
            '你都知道比赛结果了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590110392V#760F刚才克鲁茨他们回来的时候，\n',
            '已经告诉我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110393V那么……\n',
            '怎么样，感觉不错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110394V#010F这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110395V不只是前辈他们，\n',
            '晋级的队伍也都是强敌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们说明了关于空贼和特务兵小组的事情。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590110396V#762F原来如此……\n',
            '我倒是听说过那些空贼被允许参赛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110397V可是没想到特务部队的队长那么厉害啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110398V#007F普通的队员就很厉害了，\n',
            '不过和那个队长完全不能相提并论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110399V#002F拥有单手举起巨剑的臂力，\n',
            '还有像豹子一样敏捷的身手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110400V虽然早就知道他不是一般人，\n',
            '不过真没想到会强到那种程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110401V#013F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110402V#012F那个，艾南先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110403V关于那个洛伦斯少尉的经历，\n',
            '你知不知道些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590110404V#765F嗯，真是遗憾，\n',
            '他的事情我也不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110405V情报部是新设立的部队，\n',
            '成员都是在理查德上校升职时候\n',
            '从各个部队选拔出来的精英。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110406V他也应该是其中一人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110407V#013F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110408V#505F#6P喂喂，约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110409V你好像很关心那个红头怪嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110410V有什么……你很在意的事情吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110411V#010F#2P不，很显然他不是个简单的人物。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110412V因为很可能和他交手，\n',
            '所以要知道对方详细的战斗力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110413V#006F#6P哦……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590110414V#760F说起来，还有件事要告诉你们，\n',
            '虽然和那个洛伦斯少尉无关……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110415V就在今天中午，\n',
            '一艘军用警备飞艇到达了王都的空港。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110416V从警备飞艇上面走下来的是\n',
            '上校的副官凯诺娜上尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)
    SetChrDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110417V#014F这个是值得注意的情报哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110418V#009F凯诺娜上尉……\n',
            '就是那个阴险的母狐狸嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110419V利用提妲、威胁博士的讨厌婆娘。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590110420V#760F那个警备飞艇，\n',
            '好像在五大都市都去过一遍呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110421V强行在空港着陆，\n',
            '让定期船的出发时间都不得不推迟。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110422V#509F真是没有好事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110423V#015F五大都市都到过吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110424V就算要搜捕博士他们，\n',
            '这样的范围也似乎太大了点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590110425V#760F现在，各地的支部正在调查这件事。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590110426V如果知道什么消息的话会立刻联系我们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101126V你们就不用担心太多了，\n',
            '安心地继续参加武术大会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110428V#006F嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110429V#010F那么，我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_72DA')

    def _loc_5926(): pass

    label('loc_5926')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 2, 0x60A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C11',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 2, 0x60A))

    ChrTalk(
        0x0101,
        (
            '#0010100737V#004F啊，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010100738V#501F我说约修亚，\n',
            '科洛丝不是也会来王都这里吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100739V#010F她确实说过在诞辰庆典之前\n',
            '要回王都这里的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100740V也许已经来了也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5A05')
    def lambda_5A05():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5A05)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100741V#006F艾南哥哥，我想问一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100742V有一个叫做科洛丝的女孩子来过这里吗？\n',
            '她和我们年纪差不多。\n',
            '  ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100743V我们约好在王都见面的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100744V#763F是叫科洛丝吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100745V没有，\n',
            '并没有你所说的女孩子来过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100746V#007F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100747V#505F对了，\n',
            '当时没有详细地问她会在哪里落脚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100748V#010F她好像说过\n',
            '会在富裕的亲戚家住下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100749V不过单凭这一点来寻找，\n',
            '似乎有点太过勉强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100750V#760F既然约好了，\n',
            '就肯定会取得联络的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100751V一旦有了消息，\n',
            '我会立刻告知你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72DA')

    def _loc_5C11(): pass

    label('loc_5C11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_6418',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DF, 4, 0x6FC)),
            (Expr.TestScenaFlags, ScenaFlag(0x00DF, 3, 0x6FB)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_624C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DF, 5, 0x6FD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_61B3',
    )

    SetScenaFlags(ScenaFlag(0x00DF, 5, 0x6FD))

    ChrTalk(
        0x0008,
        (
            '#0590101181V#762F对了，虽然在诞辰庆典\n',
            '说这些不合时宜的话有些煞风景……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101182V不过与『杰斯塔猎兵团』\n',
            '相关的情报终于收集到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101183V#004F『杰斯塔猎兵团』？\n',
            '那个好像是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101184V#012F是洛伦斯少尉在加入情报部之前\n',
            '所属的佣兵部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101185V#762F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101186V那是一个以埃雷波尼亚周边的自治州\n',
            '为主要活动范围的部队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101187V『猎兵团』这个名字与他们非常相称，\n',
            '既拥有实力又有显赫的战绩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101188V大约半年前，在毫无先兆的情况下，\n',
            '整个部队突然间行踪不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101189V#580F整个部队行踪不明！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101190V这么说……\n',
            '是因为在战场上打了败仗吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101191V#765F不，那个时候，\n',
            '他们完全没有到任何地方\n',
            '展开任何战斗的迹象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101192V像这种情况，\n',
            '超过百人的集团忽然之间消失得无影无踪，\n',
            '就连他们的同行也百思不得其解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101193V#505F总、总感觉好可怕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001451V#013F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101195V#015F就在那时，\n',
            '洛伦斯少尉正好加入了情报部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101196V#012F这两者之间有什么关联吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101197V#764F与之相关的情况正在调查当中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101198V说不定王国军方面会获得什么情报。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101199V#760F对了，还有一个不合时宜的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101200V埃雷波尼亚皇族答应过\n',
            '要来参加诞辰庆典的约定，\n',
            '最终还是没有兑现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101201V和往年一样，\n',
            '只有帝国的大使出席了庆典仪式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101202V#501F唔～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101203V对了，那个皇族\n',
            '就是科洛丝的婚约对象吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101204V#010F嗯，那是杜南公爵\n',
            '打算在继承王位之后安排的婚约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101205V#760F结果那个婚约在询问了\n',
            '女王陛下的意见之后决定取消了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101206V皇族取消访问大概也是因为这个缘故吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6249')

    def _loc_61B3(): pass

    label('loc_61B3')

    ChrTalk(
        0x0008,
        (
            '#0590101207V#760F诞辰庆典的警备工作\n',
            '都交给王国军来负责了，\n',
            '大家应该都在街上自由自在地游玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101208V我想在酒廊、小店还有酒店这些地方\n',
            '就能找到他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6249(): pass

    label('loc_6249')

    Jump('loc_6415')

    def _loc_624C(): pass

    label('loc_624C')

    SetScenaFlags(ScenaFlag(0x00DF, 4, 0x6FC))

    ChrTalk(
        0x0008,
        (
            '#0590101209V#760F哎呀呀，\n',
            '艾丝蒂尔和约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101210V今天基本上没有什么任务呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101211V#761F不用顾虑，\n',
            '好好地享受约会的快乐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101212V#503F约、约、约会，\n',
            '不是那样的啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101213V不过再过一段时间大概就能这么说了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101214V#014F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101215V#506F啊哈，哈哈哈……\n',
            '没、没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101207V#760F诞辰庆典的警备工作\n',
            '都交给王国军来负责了，\n',
            '大家应该都在街上自由自在地游玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101208V我想在酒廊、小店还有酒店这些地方\n',
            '就能找到他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_6415(): pass

    label('loc_6415')

    Jump('loc_72DA')

    def _loc_6418(): pass

    label('loc_6418')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_6589',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_64BA',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101176V#762F科洛蒂娅公主的委托情况\n',
            '我已经从亲卫队那里了解到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101177V#760F这边不会有问题的。\n',
            '就算王国军跑来询问，\n',
            '我们也会装作不知情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6586')

    def _loc_64BA(): pass

    label('loc_64BA')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0590101178V#762F约修亚，还有金先生，\n',
            '你们平安无事可真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101179V科洛蒂娅公主的委托情况\n',
            '我已经从亲卫队那里了解到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101177V#760F这边不会有问题的。\n',
            '就算王国军跑来询问，\n',
            '我们也会装作不知情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6586(): pass

    label('loc_6586')

    Jump('loc_72DA')

    def _loc_6589(): pass

    label('loc_6589')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6701',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 3, 0x64B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 5, 0x64D)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_660B',
    )

    ChrTalk(
        0x0008,
        (
            '#0590130511V#760F游击士已经全部到齐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130512V接下来要是还能联系到\n',
            '亲卫队以及熟识的记者就好了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_66FE')

    def _loc_660B(): pass

    label('loc_660B')

    ChrTalk(
        0x0008,
        (
            '#0590130095V#760F在王都的其余游击士有克鲁茨、\n',
            '库拉茨、卡露娜和亚妮拉丝这四位。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130394V在酒廊、一般的商店，\n',
            '或者酒店里都可以见到他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130395V找到的话，就叫他们到这里来集合吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130396V如果要是还能联系到\n',
            '亲卫队以及熟识的记者就好了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_66FE(): pass

    label('loc_66FE')

    Jump('loc_72DA')

    def _loc_6701(): pass

    label('loc_6701')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_696E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_674B',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101167V#760F今天很累了吧。\n',
            '晚宴的事，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_696B')

    def _loc_674B(): pass

    label('loc_674B')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0590101158V#761F我听大家说了，\n',
            '恭喜你们取得优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101159V#001F谢谢你，艾南哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101160V#760F我听克鲁茨他们说，\n',
            '决赛好像非常激烈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101161V#505F是呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101162V下次再和他们战斗的话，\n',
            '就不知能不能赢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101163V#015F嗯，\n',
            '肯定不再是那么简单的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101164V#761F哈哈，胜负有时要靠运气，\n',
            '但引导你们取得胜利的是\n',
            '你们自身的实力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101165V而且，\n',
            '你们以后还会继续成长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101166V#006F嗯，谢谢你的鼓励，\n',
            '我们会更加努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101167V#760F今天很累了吧。\n',
            '晚宴的事，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101168V#006F嗯！交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_696B(): pass

    label('loc_696B')

    Jump('loc_72DA')

    def _loc_696E(): pass

    label('loc_696E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6AB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6A01',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101153V#760F昨天你们有没有\n',
            '到我所说的地下水路看一下呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101152V我觉得对现在的你们来说，\n',
            '那里会是一个非常理想的锻炼场所。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6AB4')

    def _loc_6A01(): pass

    label('loc_6A01')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0590101150V#760F早上好啊，各位。\n',
            '今天终于到总决赛了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101151V昨天你们有没有\n',
            '到我所说的地下水路看一下呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101152V我觉得对现在的你们来说，\n',
            '那里会是一个非常理想的锻炼场所。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6AB4(): pass

    label('loc_6AB4')

    Jump('loc_72DA')

    def _loc_6AB7(): pass

    label('loc_6AB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Return,
        ),
        'loc_6B75',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101155V#760F给你们的那把钥匙可以打开\n',
            '竞技场旁边的地下水路入口。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101156V不过，进入那边的区域\n',
            '可能会遇到相当强大的魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101157V如果只有你们两人，\n',
            '记住一定不要贸然进去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72DA')

    def _loc_6B75(): pass

    label('loc_6B75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6E9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DF, 2, 0x6FA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E38',
    )

    SetScenaFlags(ScenaFlag(0x00DF, 2, 0x6FA))

    ChrTalk(
        0x0008,
        (
            '#0590101135V#761F艾丝蒂尔、约修亚。\n',
            '听说你们顺利地进入决赛了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101136V虽然对克鲁茨他们来说有点遗憾，\n',
            '不过听说比赛打得很精彩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101137V#006F嗯，真是白热化的战斗呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101138V#007F不过，和各位前辈比起来，\n',
            '我们的实力还需要有待提高呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101139V#010F说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101140V金先生就不用说了，\n',
            '奥利维尔的枪法和魔法也帮了很大的忙。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101141V我们以后还要加倍努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101142V#761F呵呵，有这种上进的意识，\n',
            '我想你们一定会不断地进步的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101143V#760F对了，\n',
            '今天有没有打听到什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101144V#006F其实，我们拜托了\n',
            '《利贝尔通讯》的记者帮忙收集情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101145V现在准备去看看情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101146V#763F《利贝尔通讯》吗……\n',
            '那真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101147V#761F我知道了。\n',
            '期待你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E98')

    def _loc_6E38(): pass

    label('loc_6E38')

    ChrTalk(
        0x0008,
        (
            '#0590101146V#763F《利贝尔通讯》吗……\n',
            '那真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101147V#761F我知道了。\n',
            '期待你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E98(): pass

    label('loc_6E98')

    Jump('loc_72DA')

    def _loc_6E9B(): pass

    label('loc_6E9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6FA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6F06',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101133V#760F从今天开始，不管对手是谁，\n',
            '应该都不是那么好对付的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101132V要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6FA0')

    def _loc_6F06(): pass

    label('loc_6F06')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0590101129V#760F早上好啊，各位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101130V怎么样，\n',
            '行装都整理好了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101131V从今天开始，不管对手是谁，\n',
            '应该都不是那么好对付的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101132V要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6FA0(): pass

    label('loc_6FA0')

    Jump('loc_72DA')

    def _loc_6FA3(): pass

    label('loc_6FA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_701E',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101125V#760F凯诺娜上尉的活动情况\n',
            '现在正由各支部在进行追踪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101126V你们就不用管了，\n',
            '专心地参加武术大会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72DA')

    def _loc_701E(): pass

    label('loc_701E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_71B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_709C',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101127V#760F比赛应该是在下午开始，\n',
            '所以不用这么着急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101124V在大街上稍微放松一下\n',
            '也许是个不错的选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71B3')

    def _loc_709C(): pass

    label('loc_709C')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0590101120V#760F早上好啊，各位。\n',
            '今天是第一回合的比赛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101121V现在王都的周边是由\n',
            '军队负责警备的工作，\n',
            '所以给协会的委托就少了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101122V各位只要专心为大会\n',
            '做好准备就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101123V比赛要下午才开始，\n',
            '所以各位现在不用着急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101124V在大街上稍微放松一下\n',
            '也许是个不错的选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_71B3(): pass

    label('loc_71B3')

    Jump('loc_72DA')

    def _loc_71B6(): pass

    label('loc_71B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_726A',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101117V#760F金先生在王都的住所\n',
            '是东街区的卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101118V他平常会呆在酒廊里面，\n',
            '你们最好也去那里看看。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101119V从北边的小路过去就能找到酒廊了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72DA')

    def _loc_726A(): pass

    label('loc_726A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_72DA',
    )

    ChrTalk(
        0x0008,
        (
            '#0590101115V#760F想要去王城的话，\n',
            '沿着大街一直往北走就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101116V总之，\n',
            '收集情报的时候请一定要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_72DA(): pass

    label('loc_72DA')

    TalkEnd(0x0008)

    Return()

# id: 0x000D offset: 0x72DE
@scena.Code('func_0D_72DE')
def func_0D_72DE():
    EventBegin(0x00)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000C, -2590, 0, 1600, 270)
    SetChrPos(0x0009, -1500, 0, 770, 270)
    SetChrPos(0x000B, -1770, 0, -310, 270)
    SetChrPos(0x000A, -2590, 0, -610, 270)
    OP_4A(0x000C, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0008, 255)
    CameraMove(-4030, 0, 1100, 0)
    CameraSetDistance(2800, 0)
    SetChrPos(0x0101, 30, -250, -4920, 315)
    SetChrPos(0x0102, 1120, -250, -4920, 315)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0590100618V#760F那么，祝你们胜利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100619V实际上，如果是你们的话，\n',
            '比赛肯定可以轻松通过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310100620V#821F嘿嘿，你很清楚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320100621V#830F一旦出场，\n',
            '就要全力以赴哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120100622V#850F没错！\n',
            '绝对不能输给军队那些人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330100623V#840F那么……\n',
            '差不多该出发了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0330100624V#840F……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    @scena.Lambda('lambda_74DD')
    def lambda_74DD():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_74DD)

    @scena.Lambda('lambda_74EB')
    def lambda_74EB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_74EB)

    @scena.Lambda('lambda_74F9')
    def lambda_74F9():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_74F9)

    @scena.Lambda('lambda_7507')
    def lambda_7507():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7507)

    @scena.Lambda('lambda_7515')
    def lambda_7515():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_7515')

    DispatchAsync2(0x0101, 0x0001, lambda_7515)

    @scena.Lambda('lambda_7526')
    def lambda_7526():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_7526')

    DispatchAsync2(0x0102, 0x0001, lambda_7526)

    @scena.Lambda('lambda_7537')
    def lambda_7537():
        ChrWalkTo(0x00FE, -1670, 0, -2050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7537)

    @scena.Lambda('lambda_7552')
    def lambda_7552():
        ChrWalkTo(0x00FE, -570, 0, -1820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7552)

    CameraMove(-2770, 0, 100, 2000)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010100625V#008F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020100626V#010F抱歉，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrWalkTo(0x0009, -280, 0, -450, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#0320100627V#831F#2P你们……\n',
            '不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_7635')
    def lambda_7635():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7635)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100628V#501F啊……\n',
            '你是卢安支部的卡露娜姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Return,
        ),
        'loc_770B',
    )

    ChrTalk(
        0x000B,
        (
            '#0310100631V#820F#2P说起来，在空贼作乱的时候，\n',
            '我们在柏斯曾经见过一面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120100632V#850F#1P我记得……\n',
            '你们是和雪拉前辈在一起的新人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7789')

    def _loc_770B(): pass

    label('loc_770B')

    ChrTalk(
        0x000B,
        (
            '#0310100629V#820F#2P说起来，在空贼作乱的时候，\n',
            '我们在柏斯曾经见过一面呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310100630V我记得……\n',
            '你们是和雪拉扎德在一起的新人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7789(): pass

    label('loc_7789')

    ChrTalk(
        0x0102,
        (
            '#0020100633V#010F嗯，很久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100634V不过请问一下，\n',
            '为什么大家都集中在王都呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100635V#760F关于这个问题，\n',
            '就让我来说明一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100636V各位如果不快点去的话，\n',
            '可能会赶不上准备哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320100637V#830F#2P哦，说的也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320100638V#2P不好意思，你们两个，\n',
            '要说的话过后再谈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x01, 0x00, 0x000E)

    ChrTalk(
        0x000B,
        (
            '#0310100639V#820F#2P那么，\n',
            '我们也告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x00, 0x000E)

    ChrTalk(
        0x000A,
        (
            '#0120100640V#811F#1P待会儿见，两位新人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000A, 0x01, 0x00, 0x000E)

    ChrTalk(
        0x000C,
        (
            '#0330100641V#840F……告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x01, 0x00, 0x000E)

    @scena.Lambda('lambda_7933')
    def lambda_7933():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_7933')

    DispatchAsync2(0x0101, 0x0001, lambda_7933)

    @scena.Lambda('lambda_7944')
    def lambda_7944():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_7944')

    DispatchAsync2(0x0102, 0x0001, lambda_7944)

    @scena.Lambda('lambda_7955')
    def lambda_7955():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_7955')

    DispatchAsync2(0x0008, 0x0001, lambda_7955)

    WaitForThreadExit(0x000C, 0x0001)
    Sleep(300)

    PlaySE(7, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x0101,
        (
            '#0010100642V#004F啊～单单有这几位游击士聚在一起，\n',
            '就感觉很壮观很气派呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100643V#010F是啊……\n',
            '每个人都很身手不凡呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100644V刚才你们说到出场，\n',
            '难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100645V#761F嗯，你想得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100646V他们现在正要出席武术大会的预选赛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100647V#001F哎～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0008, 400)

    @scena.Lambda('lambda_7AA5')
    def lambda_7AA5():
        CameraMove(-4030, 0, 1100, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7AA5)

    @scena.Lambda('lambda_7ABD')
    def lambda_7ABD():
        ChrWalkTo(0x00FE, -2590, 0, 280, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7ABD)

    @scena.Lambda('lambda_7AD8')
    def lambda_7AD8():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_7AD8')

    DispatchAsync2(0x0101, 0x0001, lambda_7AD8)

    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrWalkTo(0x0102, -1700, 0, 1140, 3000, 0x00)

    @scena.Lambda('lambda_7B04')
    def lambda_7B04():
        ChrWalkTo(0x00FE, -2590, 0, 1220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7B04)

    @scena.Lambda('lambda_7B1F')
    def lambda_7B1F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_7B1F')

    DispatchAsync2(0x0102, 0x0001, lambda_7B1F)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010100648V#008F对、对不起！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100649V我是从蔡斯支部来的准游击士\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100650V#010F和她一样，我是约修亚·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100651V#760F我是艾南，\n',
            '是格兰赛尔支部的负责人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100652V之前我收到了雾香的联络，\n',
            '所以知道你们今天会来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100653V趁现在赶快把转属手续办了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100654V#010F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '在转属手续的文书上签了字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590100655V#761F好，可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100656V欢迎来到游击士协会格兰赛尔支部。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100657V#760F就我个人来说，\n',
            '可是很期待你们的到来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100658V我记得，\n',
            '你们是卡西乌斯先生的孩子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100659V#004F啊～嗯，是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100660V艾南哥哥，你也和老爸认识吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100661V#760F是啊，我以前研修的时候\n',
            '也经常受到卡西乌斯先生的照顾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100662V我听说，\n',
            '他出去旅行一直没有回来是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100663V#007F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100664V虽然曾经写信说他暂时不会回来……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100665V#013F但是……\n',
            '完全没有提到具体去了哪里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100666V我们从洛连特到蔡斯各个城市走了一遍，\n',
            '也没有打听到父亲的消息。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100667V#762F嗯，听你们这样说的话，\n',
            '他不在国内的可能性就很高了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100668V#764F不过还真是麻烦啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100669V现在由于军队对恐怖事件实行的对策，\n',
            '王都的游击士的活动受到了很大的限制。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100670V如果作为原军人的卡西乌斯先生在的话，\n',
            '说不定他会知道现在的王国军里\n',
            '到底发生了什么事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100671V#509F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100672V#013F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100673V#763F哎……你们怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100674V#007F嗯，实际上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100675V其中的内幕我们两个就知道呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100676V#763F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100677V#012F连同蔡斯地区发生的事情，\n',
            '这就一并向您报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚向艾南说明了\n',
            '在雷斯顿要塞得知的事情\n',
            '以及拉赛尔博士的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0590100678V#763F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100679V#004F哎……\n',
            '艾南哥哥，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100680V#762F没、没什么……\n',
            '突然听到这么重大的事情，脑子一片空白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100681V理查德上校控制了王国军队……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100682V情报部特殊部队导演的恐怖事件……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100683V真是一时让人无法相信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100684V#580F可、可是这是真的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100685V#012F问问蔡斯支部的雾香小姐，\n',
            '我想您就可以知道得更清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100686V#764F没关系，\n',
            '我并不是在怀疑你们说的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100687V正相反，听了这些话，\n',
            '我心中的谜团终于找到答案了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100688V#762F不过话说回来，\n',
            '理查德上校在王都拥有极高的人望……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100689V不怕被你们笑话，在听你们说这件事之前，\n',
            '我也对他很有好感呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100690V而且，普通的市民对上校的阴谋，\n',
            '是做梦也都想不到的吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100691V#007F果然是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100692V#012F不愧是情报部，\n',
            '操纵情报的手法真是滴水不漏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100693V#762F游击士协会从原则上来说，\n',
            '是不能干涉军队内政的……\n',
            '但是，这也不代表我们就此袖手旁观。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100694V总而言之，\n',
            '请你们先按照预定的计划，\n',
            '完成拉赛尔博士的委托吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100695V#006F当然，我们正打算这么做呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100696V不过问题是，\n',
            '怎么样才能见到女王呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100697V#764F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100698V普通情况下，有游击士协会的介绍信，\n',
            '就可以直接晋见女王了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100699V#004F哎，是吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100700V#001F什么呀～⊙\n',
            '刚才真是白让我担心了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100701V#017F#2P艾丝蒂尔……\n',
            '我觉得事情没这么简单。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100702V不管怎么说，\n',
            '守城的亲卫队都被当成恐怖分子了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100703V#012F你知道这意味着什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100704V#505F#6P哎，你是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '「王城的警卫会变少？」\n'),
            TXT(0x01, '「女王本人会有危险？」\n'),
            TXT(0x02, '「会把介绍信拦下来？」\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_87B2'),
        (0x00000001, 'loc_894C'),
        (0x00000002, 'loc_8ACE'),
        (-1, 'loc_8C0D'),
    )

    def _loc_87B2(): pass

    label('loc_87B2')

    ChrTalk(
        0x0102,
        (
            '#0020100705V#015F#2P不，正好相反。\n',
            '警备会变得更加森严呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100706V#012F也就是说，和雷斯顿要塞一样，\n',
            '王城在理查德上校控制下的可能性很高。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100707V就算有游击士协会的介绍信，\n',
            '我想也会被他们拦下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100708V#005F#6P什、什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100709V那样的话，\n',
            '到底该怎么才能和女王会面呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100710V#013F#2P像在雷斯顿要塞那样，\n',
            '潜入王城的做法虽然可行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100711V但再次用同样的手法，\n',
            '应该不会那么简单就成功吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C0D')

    def _loc_894C(): pass

    label('loc_894C')

    ChrTalk(
        0x0102,
        (
            '#0020100712V#012F#2P这种可能性也有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100713V比起这个，和雷斯顿要塞一样，\n',
            '王城在理查德上校控制下的可能性很高。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100714V就算有游击士协会的介绍信，\n',
            '我想也会被他们拦下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100708V#005F#6P什、什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100709V那样的话，\n',
            '到底该怎么才能和女王会面呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100710V#013F#2P像在雷斯顿要塞那样，\n',
            '潜入王城的做法虽然可行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100711V但再次用同样的手法，\n',
            '应该不会那么简单就成功吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C0D')

    def _loc_8ACE(): pass

    label('loc_8ACE')

    ChrTalk(
        0x0102,
        (
            '#0020100719V#012F#2P嗯，很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100720V和雷斯顿要塞一样，\n',
            '王城在理查德上校控制下的可能性很高。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100721V#007F#6P呜呜，果然是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100722V还是不能这么简单就见到女王啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100710V#013F#2P像在雷斯顿要塞那样，\n',
            '潜入王城的做法虽然可行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100711V但再次用同样的手法，\n',
            '应该不会那么简单就成功吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0045, 0x0001)

    Jump('loc_8C0D')

    def _loc_8C0D(): pass

    label('loc_8C0D')

    ChrTalk(
        0x0101,
        (
            '#0010100725V#007F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100726V#006F在这里想也没用，\n',
            '总之先去城那边看看吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100727V运气好的话，\n',
            '说不定能从门卫那里得到什么情报呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100728V#012F#2P这样倒是没什么问题……\n',
            '不过行动的时候还是要注意一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100729V我们想要和女王陛下会面的事情，\n',
            '最好还是不要说出来。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100730V万一被理查德上校知道了，\n',
            '我们的计划很有可能会暴露出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100731V#004F#6P啊，原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590100732V#760F确实如此，\n',
            '最好连其他的游击士也瞒着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100733V顺便告诉你们，\n',
            '沿着大街一直往北走就到王城了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590100734V总之，\n',
            '收集情报的时候请一定要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8E28')
    def lambda_8E28():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8E28)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100735V#006F我知道了，艾南哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100736V#010F打听到什么会立刻回来报告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0045, 0x01, 0x0080)
    OP_28(0x0045, 0x01, 0x0100)
    TerminateThread(0x0008, 0x01)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x8EA2
@scena.Code('func_0E_8EA2')
def func_0E_8EA2():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 1070, 0, -1310, 3000, 0x00)
    ChrWalkTo(0x00FE, -180, -250, -5950, 3000, 0x00)

    @scena.Lambda('lambda_8ED5')
    def lambda_8ED5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_8ED5)

    ChrWalkTo(0x00FE, -110, -250, -7110, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x000F offset: 0x8EFB
@scena.Code('func_0F_8EFB')
def func_0F_8EFB():
    EventBegin(0x00)
    CameraMove(-4030, 0, 1100, 0)
    SetChrPos(0x0101, -2590, 0, 280, 270)
    SetChrPos(0x0102, -2590, 0, 1220, 270)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0590101080V#760F没错，金先生曾经拜托过我\n',
            '寻找能够协助他战斗的游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101081V不过你们有博士的委托在身，\n',
            '所以没有特地介绍给他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101082V#761F没想到因为杜南公爵的一时兴起，\n',
            '委托和大会重合在一起了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101083V#506F嘿嘿，从结果上来看，\n',
            '公爵的任性反而帮了我们大忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101084V#010F参加武术大会……\n',
            '艾南先生您觉得怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101085V#760F是啊……\n',
            '要把所有可能的方法都试一遍，\n',
            '我觉得这也很有尝试的价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101086V如果克鲁茨他们赢了，\n',
            '到时候再拜托他们也可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101087V不管怎样，\n',
            '你们就尽全力试着挑战一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101088V#001F太好了，就这样吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101089V#006F艾南哥哥，\n',
            '赶快告诉我们金先生现在在哪里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101090V#760F平常的话，\n',
            '应该都呆在这座建筑旁边的酒廊里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101091V顺带说一下，\n',
            '他在王都的住所是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101092V#000F原来是这样啊，\n',
            '是金先生祖国的大使馆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101093V#010F#2P共和国大使馆和竞技场一样在东街区。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101094V另外，\n',
            '我们最好也去酒廊看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101095V#006F#3P嗯，ＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101096V#763F啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101097V你们两个在王都的这段时间里\n',
            '打算住在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9334')
    def lambda_9334():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9334)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101098V#505F嗯～\n',
            '我想应该会在酒店吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101099V#010F我记得王国最大的酒店是在北街区吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101100V#760F对。\n',
            '叫做罗恩鲍姆酒店。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101101V如果没有问题的话，\n',
            '我就帮你们向酒店预约房间吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101102V费用由王都支部承担。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101103V#004F哎，这样好吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101104V#014F为了我们准备得这么周到……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101105V#760F就当作和博士的委托有关的必要经费吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101106V这也是我力所能及的事情……\n',
            '没帮上忙，真是对不住你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101107V#001F没有的事，已经帮了很大忙了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101108V#010F这样的话……\n',
            '我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590101109V#761F就这样定了，\n',
            '那么我这就去预约房间哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590101110V傍晚之后去酒店的前台说出自己的名字，\n',
            '他们就会给你们安排房间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C2, 1, 0x611))
    OP_28(0x0046, 0x04, 0x02)
    OP_28(0x0046, 0x04, 0x04)
    OP_28(0x0046, 0x01, 0x0001)
    OP_28(0x0046, 0x01, 0x0002)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x95EB
@scena.Code('func_10_95EB')
def func_10_95EB():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    CameraMove(-1330, 0, 750, 0)
    SetChrPos(0x0101, -2590, 0, 280, 270)
    SetChrPos(0x0102, -2590, 0, 1220, 270)
    SetChrPos(0x0108, -1500, 0, 750, 270)
    SetChrSubChip(0x0008, 0)
    SetChrDirection(0x0008, 90, 0)
    SetScenaFlags(ScenaFlag(0x00C9, 1, 0x649))
    OP_28(0x004B, 0x04, 0x02)
    OP_28(0x004B, 0x04, 0x04)
    OP_28(0x004B, 0x01, 0x0001)
    OP_28(0x004B, 0x01, 0x0002)
    OP_28(0x004B, 0x01, 0x0004)
    OP_28(0x004B, 0x01, 0x0008)
    FadeIn(2000, 0)
    CameraMove(-3330, 0, 750, 2000)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0590130001V#764F我明白当前的状况了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130002V#760F艾丝蒂尔、约修亚。\n',
            '你们两个做得非常出色。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130003V竟然可以接受女王陛下的直接委托……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130004V#008F啊哈哈，只是运气好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130005V#007F但是，从现在开始\n',
            '可能就没有那么好的运气了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130006V#015F嗯……\n',
            '但绝对不能放弃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130007V#761F既然你们都下了决心，\n',
            '我也就没有什么要说的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130008V总之，拉赛尔博士的委托已经达成了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130009V这些钱你们今后可能用得上，\n',
            '我这就把报酬交给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0045, 0x04, 0x10)
    Sleep(100)

    OP_AF(0x63, 0x0045)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x0046, 0x04, 0x10)
    OP_28(0x0047, 0x04, 0x10)
    OP_28(0x0048, 0x04, 0x10)
    OP_28(0x0049, 0x04, 0x10)
    OP_28(0x004A, 0x04, 0x10)
    OP_28(0x0046, 0x04, 0x20)
    OP_28(0x0047, 0x04, 0x20)
    OP_28(0x0048, 0x04, 0x20)
    OP_28(0x0049, 0x04, 0x20)
    OP_28(0x004A, 0x04, 0x20)

    ChrTalk(
        0x0008,
        (
            '#0590130010V#760F那么，接下来……金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130011V卡西乌斯先生能够把你找来，\n',
            '对于我们而言真是幸运啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130012V用你那身为Ａ级游击士的实力\n',
            '来全力帮助我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130013V#070F啊，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130014V这可是报答大人恩德的良机，\n',
            '这样的大事我怎能放任不管呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130015V我会一直帮忙到底的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_99AC')
    def lambda_99AC():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_99AC)

    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130016V#001F#5P不愧是金大哥，够爽快！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130017V#501F对了……什么叫做Ａ级呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130018V#010F#2P衡量正游击士实力的级别标准。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130019V从最低的Ｇ级开始到Ａ级为止，\n',
            '共分为七个级别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130020V#004F#5P那、那么说Ａ级不就是最高的级别了吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130021V金大哥……\n',
            '竟然是这么厉害的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130022V#070F哈哈，我啊，\n',
            '只是处于Ａ级中下游的水平罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130023V#074F而且从整个大陆来说，\n',
            'Ａ级游击士一共２０人左右……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130024V在其之上，\n',
            '其实还有不公开的Ｓ级那样的级别。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130025V是解决了国家的重大事件的游击士\n',
            '才能获得的特级游击士称号。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130026V#070F整个大陆一共只有四人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130027V#509F#5P那、那样的人究竟厉害到什么程度，\n',
            '简直完全无法想象啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130028V#075F呼，不管怎么说，\n',
            '你们也不该不知道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130029V#070F因为其中之一就是卡西乌斯大人啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010130030V#005F#5P#3S什么～～～～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130031V#009F难、难道说……\n',
            '约修亚你又是已经知道了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130032V#015F#2P对不起，其实我是知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130033V#010F因为父亲成功解决了\n',
            '五年前发生在共和国的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130034V#007F哈啊，又来一个……\n',
            '我算是彻底地服这个老爸了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130035V王国军的上校啦、幕后英雄啦、\n',
            '剑圣啦、Ｓ级游击士啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130036V#509F既然老爸这么厉害无比，\n',
            '怎么还不快点回利贝尔，\n',
            '把这次的事件通通给解决掉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130037V#070F哈哈，你说得也许没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130038V如果大人一开始就在这里的话，\n',
            '肯定会在这个事件发展成为\n',
            '政变之前将其阻止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130039V#013F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130040V#004F约修亚，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130041V#015F#2P……事情有一些奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130042V这一连串的事件\n',
            '都是在父亲外出旅行时发生的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130043V#012F难道他们早就瞄准了父亲外出的机会\n',
            '来制造这起政变吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130044V我有这样的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130045V#580F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130046V#072F唔，大人前往帝国也是\n',
            '这次政变的其中一个环节……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130047V就是这个意思对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130048V#010F#2P……不。\n',
            '是我有些多虑了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130049V那么强的父亲，被人不知不觉\n',
            '就下套的可能性几乎是没有的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130050V#013F除非存在那种可以掌握父亲的行动、\n',
            '并且可以将计就计的人物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130051V#506F唔～的确有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130052V好比说我吧，如果有人潜伏在我的附近，\n',
            '我是不会那么容易察觉的哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130053V#070F不过，要想钻大人的空子，\n',
            '那个理查德上校是不可能做到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130054V多半这两个重大的事件偶然产生了重叠吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130055V#764F不管怎么说，要想借助作为顶梁柱的\n',
            '卡西乌斯先生的力量看来是不行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130056V#762F因此，我决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130057V游击士协会·王都支部\n',
            '现在开始采取紧急应对制度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A2E8')
    def lambda_A2E8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A2E8)

    @scena.Lambda('lambda_A2F6')
    def lambda_A2F6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A2F6)

    ChrTurnDirection(0x0108, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130058V#004F紧、紧急应对制度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130059V#760F怎么说这也是女王陛下的直接委托。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130060V协会规约第三项——\n',
            '『不对国家主权进行干涉』的桎梏\n',
            '在这个紧要关头就解除掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130061V尽管如此，协会和王国军的战斗力\n',
            '在根本上还是有很大的差距的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130062V不止是金先生，\n',
            '在王都的其余所有游击士\n',
            '也都要来助一臂之力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130063V#006F原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130064V的确，要和情报部对峙的话，\n',
            '还需要集结更多的战斗力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130065V#765F可以的话，\n',
            '最好能取得国内其他支部的协助……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130066V可是现在所有地区的关所和飞艇坪\n',
            '都已经被王国军完全封锁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130067V以针对恐怖分子的名义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130068V#580F哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130069V#012F实质上是一道戒严令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130070V#074F敌人的行动也终于开始正式化了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130071V#762F我想，恐怕是打算封锁\n',
            '潜伏中的亲卫队和我们的行动吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130072V要想救出人质，\n',
            '手中没有充足的战斗力是不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130073V#006F说白了就是只要有实力，\n',
            '然后就是勇往直前不怕挑战对吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130074V对了，人质被囚禁的地方，\n',
            '有没有什么大致的线索呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130075V#764F是啊，我刚才已经想了许多……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130076V#762F最有可能的还是『艾尔贝离宫』了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130077V#505F『艾尔贝离宫』……\n',
            '不就是那座森林中的王家建筑吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130078V#010F可能性比较高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130079V以针对恐怖组织的名义接管那里，\n',
            '其实就是调用了特务兵来监守人质……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130080V而且，我认为王族的女性\n',
            '不可能会被监禁在雷斯顿要塞那种地方。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130081V#072F可对手是军队，\n',
            '我们要有确凿的情报才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130082V稍有差池的话是不能击败对手的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130083V#764F嗯……说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130084V#760F不管推测是否属实，\n',
            '先把在王都的其他游击士聚集起来再说吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130085V等把他们聚集到一起之后，\n',
            '我们再去收集情报如何？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130086V据我所知，艾丝蒂尔你们\n',
            '和杂志社的记者比较熟悉对吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130087V#501F啊，你是说奈尔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130088V#010F的确，在没有什么线索的情况下，\n',
            '还是先问问他们会比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130089V#762F还有，如果可能的话，\n',
            '也请尽量得到潜伏中的亲卫队的协助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130090V我们营救人质的计划，\n',
            '他们肯定会予以全力支持的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130091V#505F这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130092V要和乔装成修女的尤莉亚中尉\n',
            '取得联络才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130093V#010F上次多亏得到她的帮助才能见到女王，\n',
            '所以这次最好向她报告一下这件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130094V那我们这就前往大圣堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590130095V#760F在王都的其余游击士有克鲁茨、\n',
            '库拉茨、卡露娜和亚妮拉丝这四位。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130096V在酒廊、一般的商店，\n',
            '或者酒店里都可以见到他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590130097V找到的话，就叫他们到这里来集合吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130098V#006F嗯，ＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130099V#010F那么我们就立刻出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0xAC1F
@scena.Code('func_11_AC1F')
def func_11_AC1F():
    OP_28(0x004F, 0x01, 0x0020)
    OP_28(0x004F, 0x01, 0x0040)
    OP_28(0x004F, 0x01, 0x0080)
    OP_28(0x004F, 0x01, 0x0100)
    OP_28(0x004F, 0x01, 0x0200)
    OP_28(0x004F, 0x01, 0x0400)
    OP_28(0x004F, 0x01, 0x0800)
    OP_28(0x004F, 0x04, 0x10)
    EventBegin(0x00)
    CameraMove(115240, 250, 4410, 0)
    OP_67(0, 5950, -10000, 0)
    CameraSetDistance(1550, 0)
    OP_6C(315000, 0)
    OP_6E(519, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0008, 122730, 0, -1280, 180)
    SetChrPos(0x000A, 120000, 0, -2600, 90)
    SetChrPos(0x0009, 118530, 0, -3290, 90)
    SetChrPos(0x000B, 119790, 0, -3880, 90)
    SetChrPos(0x000C, 118310, 0, -1930, 90)
    SetChrPos(0x000E, 120540, 0, 450, 135)
    SetChrPos(0x000F, 120230, 0, -800, 135)
    SetChrPos(0x0010, 118670, 0, -680, 135)
    SetChrPos(0x0011, 123780, 0, -740, 180)
    SetChrPos(0x0101, 122440, 0, -3200, 0)
    SetChrPos(0x0102, 123620, 0, -3200, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    FadeIn(2000, 0)
    CameraMove(121410, 0, -1310, 4000)

    ChrTalk(
        0x0008,
        (
            '#0590140498V#760F#2P——艾丝蒂尔·布莱特，\n',
            '还有约修亚·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590140499V根据这次行动的表现，格兰赛尔支部\n',
            '决定授予你们正游击士资格的推荐信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590140500V请接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140501V#006F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 122840, 0, -2390, 2000, 0x00)
    Sleep(100)

    OP_AF(0x63, 0x004F)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '正游击士资格的推荐信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x033B, 1)
    ChrMoveTo(0x0008, 122730, 0, -1280, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0590140502V#761F#2P这样，你们二人也已经\n',
            '获得了五个地区支部的推荐信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0590140503V#760F#5P那么，卡西乌斯先生，\n',
            '接下来的工作就交给您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140504V#085F#2P嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 180, 400)
    ChrMoveTo(0x0008, 122510, 0, -410, 2000, 0x00)
    ChrMoveTo(0x0011, 122910, 0, -1770, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0160140505V#082F#2P艾丝蒂尔·布莱特，\n',
            '还有约修亚·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140506V现基于游击士协会的规定，\n',
            '正式授予你们二人正游击士的资格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140507V请交出各地方支部的推荐信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140508V#004F好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140509V#015F请您确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了所有的',
            (TxtCtl.SetColor, 0x2),
            '正游击士资格的推荐信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x0330, 1)
    RemoveItem(0x0333, 1)
    RemoveItem(0x0339, 1)
    RemoveItem(0x033A, 1)
    RemoveItem(0x033B, 1)
    RemoveItem(0x036D, 1)
    RemoveItem(0x036E, 1)

    ChrTalk(
        0x0011,
        (
            '#0160140510V#085F#2P洛连特支部、柏斯支部、\n',
            '卢安支部、蔡斯支部，\n',
            '还有格兰赛尔支部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140511V五个支部的签名都确认完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B24A',
    )

    ChrTalk(
        0x0011,
        (
            '#0160140512V#080F#2P最终等级是准游击士１级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140513V#081F没想到能达到如此程度，\n',
            '你们俩的成绩真是让我吃惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B484')

    def _loc_B24A(): pass

    label('loc_B24A')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B2B2',
    )

    ChrTalk(
        0x0011,
        (
            '#0160140514V#080F#2P最终等级是准游击士２级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140515V作为见习的新人已经做得很不错了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B484')

    def _loc_B2B2(): pass

    label('loc_B2B2')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B31A',
    )

    ChrTalk(
        0x0011,
        (
            '#0160140516V#080F#2P最终等级是准游击士３级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140515V作为见习的新人已经做得很不错了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B484')

    def _loc_B31A(): pass

    label('loc_B31A')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B395',
    )

    ChrTalk(
        0x0011,
        (
            '#0160140518V#080F#2P最终等级是准游击士４级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140519V#083F说真的，成绩差强人意，\n',
            '你们俩以后还要继续努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B484')

    def _loc_B395(): pass

    label('loc_B395')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B410',
    )

    ChrTalk(
        0x0011,
        (
            '#0160140520V#080F#2P最终等级是准游击士５级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140519V#083F说真的，成绩差强人意，\n',
            '你们俩以后还要继续努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B484')

    def _loc_B410(): pass

    label('loc_B410')

    ChrTalk(
        0x0011,
        (
            '#0160140522V#080F#2P最终等级是准游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140523V#083F……该怎么评价好呢，\n',
            '以这种成绩也能成为正游击士也算是奇迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B484(): pass

    label('loc_B484')

    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0160140524V#080F#2P现以女神与游击士徽章之名义，\n',
            '在此任命你们二人为正游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140525V你们二人，请接受徽章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140526V#508F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0011, 122840, 0, -2390, 2000, 0x00)
    OP_AD('ED6_DT04/C_VIS016._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '正游击士的徽章',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x035D, 1)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrMoveTo(0x0011, 122910, 0, -1770, 2000, 0x00)
    PlaySE(233, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_B5B3')
    def lambda_B5B3():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B5B3)

    @scena.Lambda('lambda_B5C1')
    def lambda_B5C1():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B5C1)

    CameraMove(119780, 0, -1210, 1500)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0030140527V#021F恭喜！艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080140528V#071F哈哈，新的徽章，\n',
            '看起来非常适合你们嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050140529V#051F哼……\n',
            '这次我就破例称赞你们『干得好』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140530V#008F#6P嘿嘿……\n',
            '真是太谢谢大家了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140531V#019F我们能取得今天的成绩……\n',
            '也是多亏了大家的帮助和支持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140532V#080F#2P游击士的生涯从这里才正式开始。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140533V你们俩，不要忘记这一点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B753')
    def lambda_B753():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B753)

    Sleep(100)

    SetChrDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140534V#006F#6P嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140535V#010F我们会努力更上一层楼的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(119780, 0, -210, 1000)
    SetChrDirection(0x0008, 225, 400)

    ChrTalk(
        0x0008,
        (
            '#0590140536V#760F#2P各位，虽然很抱歉打断你们的谈话，\n',
            '不过庆贺的话还请留待之后再说吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590140537V趁今天大家齐聚一起的机会，\n',
            '必须向大家宣布一件很遗憾的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B870')
    def lambda_B870():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_B870)

    @scena.Lambda('lambda_B87E')
    def lambda_B87E():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_B87E)

    @scena.Lambda('lambda_B88C')
    def lambda_B88C():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_B88C)

    @scena.Lambda('lambda_B89A')
    def lambda_B89A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_B89A)

    @scena.Lambda('lambda_B8A8')
    def lambda_B8A8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_B8A8)

    @scena.Lambda('lambda_B8B6')
    def lambda_B8B6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_B8B6)

    @scena.Lambda('lambda_B8C4')
    def lambda_B8C4():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_B8C4)

    @scena.Lambda('lambda_B8D2')
    def lambda_B8D2():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_B8D2)

    @scena.Lambda('lambda_B8E0')
    def lambda_B8E0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B8E0)

    @scena.Lambda('lambda_B8EE')
    def lambda_B8EE():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B8EE)

    ChrTalk(
        0x000C,
        (
            '#0330140538V#842F遗憾的事情……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590140539V#762F#2P从今天开始，\n',
            '卡西乌斯·布莱特先生正式决定\n',
            '退出我们游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590140540V在往后的日子里，\n',
            '卡西乌斯先生将重返王国军。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_BA01')
    def lambda_BA01():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_BA01)

    @scena.Lambda('lambda_BA0F')
    def lambda_BA0F():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_BA0F)

    @scena.Lambda('lambda_BA1D')
    def lambda_BA1D():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_BA1D)

    @scena.Lambda('lambda_BA2B')
    def lambda_BA2B():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BA2B)

    @scena.Lambda('lambda_BA39')
    def lambda_BA39():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BA39)

    Sleep(1000)

    @scena.Lambda('lambda_BA4C')
    def lambda_BA4C():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_BA4C)

    @scena.Lambda('lambda_BA5A')
    def lambda_BA5A():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_BA5A)

    @scena.Lambda('lambda_BA68')
    def lambda_BA68():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_BA68)

    @scena.Lambda('lambda_BA76')
    def lambda_BA76():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_BA76)

    ChrTalk(
        0x0009,
        (
            '#0320140541V#832F#5P什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310140542V#822F#5P是、是真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160140543V#085F#2P长时间外出之后，\n',
            '还向协会提出这样突然的请求，\n',
            '各位，我真是深感抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140544V#080F但是，王国的当务之急，\n',
            '是必须解决政变所带来的混乱状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140545V被情报部弄得乌烟瘴气的\n',
            '军队的指挥系统也有必要重建。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140546V所以，我打算协助做这些工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120140547V#818F#5P啊，是啊……\n',
            '军人不能同时担任游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000F, 400)

    ChrTalk(
        0x000A,
        (
            '#0120140548V#814F#5P对了，\n',
            '前辈你们好像知道这件事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000A, 400)

    ChrTalk(
        0x000F,
        (
            '#0030140549V#020F#2P嗯，老师和我们谈过这件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140550V老实说，虽然感到非常惋惜……\n',
            '但如果总是依赖老师的话，\n',
            '我们是无法成为独当一面的游击士的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000A, 400)

    ChrTalk(
        0x000E,
        (
            '#0050140551V#051F哼，以后我们要证明给他看看，\n',
            '不管什么事情年轻人也都能办到。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330140552V#841F#5P是吗……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320140553V#835F#5P不管什么时候\n',
            '都无法从忙碌中解脱出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BD91')
    def lambda_BD91():
        CameraMove(119780, 0, -1210, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BD91)

    SetChrDirection(0x0011, 180, 400)

    @scena.Lambda('lambda_BDB0')
    def lambda_BDB0():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_BDB0)

    @scena.Lambda('lambda_BDBE')
    def lambda_BDBE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_BDBE)

    @scena.Lambda('lambda_BDCC')
    def lambda_BDCC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_BDCC)

    @scena.Lambda('lambda_BDDA')
    def lambda_BDDA():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_BDDA)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0011,
        (
            '#0160140554V#080F#2P不过今天有两位新的正游击士诞生了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140555V他们俩作为我今后的代理人，\n',
            '可以任由你们这些前辈随意差遣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140556V#509F#6P喂～我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140557V#019F#4P哈哈，看来以后会变得更忙呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x00CD, 3, 0x66B))
    ClearMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0xBEDA
@scena.Code('func_12_BEDA')
def func_12_BEDA():
    EventBegin(0x00)
    CameraMove(-3270, 0, 730, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0018, 0x0080)
    SetChrPos(0x0018, -2600, 0, 100, 90)
    SetChrPos(0x0101, -860, 0, -670, 270)
    SetChrPos(0x0102, -950, 0, 482, 270)
    OP_4A(0x0008, 255)
    SetChrPos(0x0008, -5700, 0, -130, 270)
    LoadEffect(0x00, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0018,
        (
            '#0040181636V#033F#5P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181637V为什么要到游击士协会来呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181638V#507F哎呀呀，不要着急嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181639V#010F我们马上让艾南先生\n',
            '把那个人叫过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C05B')
    def lambda_C05B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_C05B)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0590181640V#760F#4P嗯，好的，\n',
            '那么，就请到游击士协会来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    Sleep(300)

    SetChrDirection(0x0008, 90, 400)
    ChrWalkTo(0x0008, -4480, 0, 960, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0590181641V#761F各位，联络完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590181642V那个人很快就会到这里了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0040181643V#035F呵，这么急不可耐\n',
            '想和我这个天才演奏家见面啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181644V#030F对了，\n',
            '那个小猫咪是我以前认识的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181645V#001F当然啦，\n',
            '而且是你再熟悉不过的朋友哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0018, 90, 400)

    ChrTalk(
        0x0018,
        (
            '#0040181646V#037F#5P唔呵呵……\n',
            '现在在王都这里的小猫咪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181647V这么说是雪拉君……\n',
            '还是卡露娜女士或亚妮拉丝小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181648V#035F不对不对，\n',
            '梅贝尔市长和莉拉小姐也是有可能的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181649V#033F啊，难道说是科洛蒂娅公主\n',
            '或是提妲小姑娘吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020181650V#019F该怎么说呢……\n',
            '这还真是惊人的想象力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x64)
    Sleep(700)

    SetChrPos(0x0019, -200, -250, -7270, 152)

    @scena.Lambda('lambda_C34B')
    def lambda_C34B():
        ChrTurnDirection(0x00FE, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C34B)

    @scena.Lambda('lambda_C359')
    def lambda_C359():
        ChrTurnDirection(0x00FE, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_C359)

    @scena.Lambda('lambda_C367')
    def lambda_C367():
        ChrTurnDirection(0x00FE, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_C367)

    @scena.Lambda('lambda_C375')
    def lambda_C375():
        ChrTurnDirection(0x00FE, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_C375)

    ChrSetRGBAMask(0x0019, 255, 255, 255, 0, 0)
    CameraMove(-1570, 0, -2670, 2000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0590181651V#760F#6P啊，\n',
            '请直接进来就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0040181652V#031F哦哦，终于来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181653V我心爱的人儿啊！\n',
            '快，进来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0019,
        '男人的声音',
        (
            '#0110181654V#2P……那么，我就不客气了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    ClearChrFlags(0x0019, 0x0080)

    @scena.Lambda('lambda_C45A')
    def lambda_C45A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_C45A)

    @scena.Lambda('lambda_C46C')
    def lambda_C46C():
        ChrWalkTo(0x0019, -1800, 0, -2060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_C46C)

    @scena.Lambda('lambda_C487')
    def lambda_C487():
        ChrTurnDirection(0x0019, 0x0018, 0)
        Yield()

        Jump('lambda_C487')

    DispatchAsync2(0x0019, 0x0000, lambda_C487)

    @scena.Lambda('lambda_C498')
    def lambda_C498():
        CameraMove(-2220, 0, -370, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_C498)

    @scena.Lambda('lambda_C4B0')
    def lambda_C4B0():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_C4B0')

    DispatchAsync2(0x0101, 0x0001, lambda_C4B0)

    @scena.Lambda('lambda_C4C1')
    def lambda_C4C1():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_C4C1')

    DispatchAsync2(0x0102, 0x0001, lambda_C4C1)

    @scena.Lambda('lambda_C4D2')
    def lambda_C4D2():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_C4D2')

    DispatchAsync2(0x0018, 0x0001, lambda_C4D2)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0018,
        (
            '#0040181655V#033F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0019, 0xFF)
    ChrTurnDirection(0x0019, 0x0101, 400)

    ChrTalk(
        0x0019,
        (
            '#0110181656V#270F看来只有靠你们俩\n',
            '才能这么顺利地完成这个委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110181657V#272F非常感谢，\n',
            '我代表帝国大使馆向你们致意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181658V#001F哪里哪里，不用客气啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181659V#019F奥利维尔他本人也非常愿意呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0040181660V#033F……和你们说的不一样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181661V想见我的小猫咪到底在哪儿啊……？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0019, 0x0018, 400)

    ChrTalk(
        0x0019,
        (
            '#0110181662V#270F你在说什么胡话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110181663V由于接受了女王陛下的直接邀请，\n',
            '现在正要对出席今夜晚宴的相关事项进行确认。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110181664V正因为如此，\n',
            '不能再对你放任不管了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110181665V这已经不是第一次了，\n',
            '我反复对你强调过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0018, 0xFF)
    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrDirection(0x0018, 90, 400)

    ChrTalk(
        0x0018,
        (
            '#0040181666V#036F艾、艾丝蒂尔君！约修亚君！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181667V你们太残忍了吧！\n',
            '怎么能够这样欺骗我的感情呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    SetChrDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181668V#509F这种话让别人听到会想歪的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    SetChrDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181669V#019F我们完全没有说过\n',
            '是一位女性在等着你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0019, 0x0040)
    ChrWalkTo(0x0019, -2600, 0, -800, 3000, 0x00)
    ChrTurnDirection(0x0019, 0x0018, 400)
    ChrTurnDirection(0x0018, 0x0019, 0)

    ChrTalk(
        0x0019,
        (
            '#0110181670V#272F#3P好了……时间不多了，\n',
            '很快就要到傍晚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110181671V还有许多事情要商定，\n',
            '赶快回大使馆去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C89D')
    def lambda_C89D():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_C89D')

    DispatchAsync2(0x0101, 0x0001, lambda_C89D)

    @scena.Lambda('lambda_C8AE')
    def lambda_C8AE():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_C8AE')

    DispatchAsync2(0x0102, 0x0001, lambda_C8AE)

    ChrWalkTo(0x0019, -2600, 0, -700, 3000, 0x00)
    SetChrDirection(0x0019, 90, 400)
    SetChrFlags(0x0018, 0x0004)
    SetChrPos(0x0018, -2600, 400, 100, 0)
    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_C902')
    def lambda_C902():
        OP_97(0x0018, -2600, -700, 92000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_C902)

    SetChrChipByIndex(0x0018, 20)
    SetChrSubChip(0x0018, 0)
    SetChrFlags(0x0018, 0x0020)
    SetChrDirection(0x0019, 180, 400)

    ChrTalk(
        0x0018,
        (
            '#0040181672V#20A#036F哎～呀～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CreateThread(0x0018, 0x01, 0x00, 0x0013)
    CreateThread(0x0019, 0x01, 0x00, 0x0014)
    WaitForThreadExit(0x0018, 0x0001)
    PlaySE(7, 0x00, 0x64)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0008, 0x01)
    CameraMove(-2240, 0, 670, 1000)
    ChrTurnDirection(0x0008, 0x0102, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0590181673V#760F呼，总算是告一段落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590181674V审核也一起完成了，请收下报酬。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590181675V因为正游击士的手册还没有准备好，\n',
            '所以暂且先用准游击士手册来记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0055, 0x04, 0x10)
    OP_28(0x0055, 0x01, 0x0001)
    OP_28(0x0055, 0x01, 0x0002)
    Sleep(100)

    OP_AF(0x63, 0x0055)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181676V#506F#6P嗯，感觉有点内疚呢，\n',
            '还好事先得到了他本人的同意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181677V#006F那么，\n',
            '诞辰庆典游览再次开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181678V#010F#2P嗯，好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181679V我们逛一圈之后，\n',
            '就到东街区的休息处去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMapFlags(0x00000800)
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x00DF, 3, 0x6FB))
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0xCB3F
@scena.Code('func_13_CB3F')
def func_13_CB3F():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    ChrMoveTo(0x00FE, 540, 250, -5630, 2000, 0x00)

    @scena.Lambda('lambda_CB63')
    def lambda_CB63():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_CB63)

    ChrMoveTo(0x00FE, 540, 250, -7790, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0014 offset: 0xCB89
@scena.Code('func_14_CB89')
def func_14_CB89():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    ChrMoveTo(0x00FE, -340, -250, -5630, 2100, 0x00)

    @scena.Lambda('lambda_CBAD')
    def lambda_CBAD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_CBAD)

    ChrMoveTo(0x00FE, -340, -250, -7790, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0xCBD3
@scena.Code('func_15_CBD3')
def func_15_CBD3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 5, 0x6ED)),
            Expr.Return,
        ),
        'loc_CBE6',
    )

    OP_2A(0x0050, 0x0051, 0x0055, 0xFFFF)

    Jump('loc_CC8C')

    def _loc_CBE6(): pass

    label('loc_CBE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_CC2E',
    )

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在没有什么特别的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_CC8C')

    def _loc_CC2E(): pass

    label('loc_CC2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_CC3F',
    )

    OP_2A(0x0050, 0x0051, 0xFFFF)

    Jump('loc_CC8C')

    def _loc_CC3F(): pass

    label('loc_CC3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_CC4E',
    )

    OP_2A(0x0050, 0xFFFF)

    Jump('loc_CC8C')

    def _loc_CC4E(): pass

    label('loc_CC4E')

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在没有什么特别的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_CC8C(): pass

    label('loc_CC8C')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
