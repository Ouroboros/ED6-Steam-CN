import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4262_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4262   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '克劳斯市长'),
    TXT(0x02, '莉拉'),
    TXT(0x03, '梅贝尔市长'),
    TXT(0x04, '科林兹校长'),
    TXT(0x05, '茜亚'),
    TXT(0x06, '金'),
    TXT(0x07, '里拉老人'),
    TXT(0x08, '布莉姆'),
    TXT(0x09, '阿加特'),
    TXT(0x0A, '奥利维尔'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4262.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x612D
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
        ('ED6_DT07/CH02353._CH', 'ED6_DT07/CH02353P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02363._CH', 'ED6_DT07/CH02363P._CP'),
        ('ED6_DT07/CH02603._CH', 'ED6_DT07/CH02603P._CP'),
        ('ED6_DT07/CH02623._CH', 'ED6_DT07/CH02623P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
    ]

# id: 0x10002 offset: 0x12A
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
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
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -139520,
            z                   = 4000,
            y                   = 9500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -78950,
            z                   = 0,
            y                   = 5960,
            direction           = 359,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -81130,
            z                   = 0,
            y                   = 61160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -77050,
            z                   = 0,
            y                   = 55320,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0x26A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x26A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x26A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x26A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_278',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000C)

    def _loc_278(): pass

    label('loc_278')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_289',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    SetScenaFlags(ScenaFlag(0x00C7, 7, 0x63F))
    Event(0, 0x000F)

    def _loc_289(): pass

    label('loc_289')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_297',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0011)

    def _loc_297(): pass

    label('loc_297')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FB',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000A, -28870, 200, 53540, 270)
    SetChrPos(0x0009, -28040, 0, 54950, 211)
    SetChrPos(0x000B, -83970, 200, -52980, 270)
    SetChrPos(0x0008, -86020, 200, -52980, 90)

    def _loc_2FB(): pass

    label('loc_2FB')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006A, 'loc_30B'),
        (0x00000065, 'loc_32A'),
        (-1, 'loc_340'),
    )

    def _loc_30B(): pass

    label('loc_30B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 2, 0x63A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 3, 0x63B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 4, 0x63C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 7, 0x63F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_327',
    )

    Event(0, 0x000E)

    def _loc_327(): pass

    label('loc_327')

    Jump('loc_340')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 7, 0x63F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33D',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 0, 0x640))
    Event(0, 0x0010)

    def _loc_33D(): pass

    label('loc_33D')

    Jump('loc_340')

    def _loc_340(): pass

    label('loc_340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_36A',
    )

    SetChrChipByIndex(0x0000, 7)
    SetChrChipByIndex(0x0001, 8)
    SetChrChipByIndex(0x0138, 9)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)

    def _loc_36A(): pass

    label('loc_36A')

    SetScenaFlags(ScenaFlag(0x00C7, 1, 0x639))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_42D',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrChipByIndex(0x000D, 14)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000D, 0x0010)
    SetChrFlags(0x000D, 0x0800)
    SetChrPos(0x000D, -85910, 200, 59730, 270)
    SetChrChipByIndex(0x0008, 15)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -25510, 0, -57090, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, -84730, 250, -53560, 270)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000A, 0x0010)
    SetChrPos(0x000A, -28700, 250, 53020, 270)
    SetChrPos(0x0009, -29640, 0, 51490, 0)

    Jump('loc_653')

    def _loc_42D(): pass

    label('loc_42D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_43C',
    )

    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_653')

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_44B',
    )

    SetChrFlags(0x000E, 0x0080)

    Jump('loc_653')

    def _loc_44B(): pass

    label('loc_44B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_4FC',
    )

    SetChrFlags(0x000E, 0x0080)
    SetChrChipByIndex(0x000D, 14)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000D, 0x0010)
    SetChrFlags(0x000D, 0x0800)
    SetChrPos(0x000D, -85910, 200, 59730, 270)
    SetChrChipByIndex(0x0008, 15)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -25510, 0, -57090, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, -84730, 250, -53560, 270)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000A, 0x0010)
    SetChrPos(0x000A, -28700, 250, 53020, 270)
    SetChrPos(0x0009, -29640, 0, 51490, 0)

    Jump('loc_653')

    def _loc_4FC(): pass

    label('loc_4FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 7, 0x63F)),
            Expr.Return,
        ),
        'loc_5AC',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -80180, 0, 61190, 0)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x0008, 15)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -25510, 0, -57090, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, -84730, 250, -53560, 270)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000A, 0x0010)
    SetChrPos(0x000A, -28700, 250, 53020, 270)
    SetChrPos(0x0009, -29640, 0, 51490, 0)
    SetChrPos(0x000E, -138810, 0, 7070, 0)

    Jump('loc_653')

    def _loc_5AC(): pass

    label('loc_5AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_653',
    )

    SetChrChipByIndex(0x000D, 14)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000D, 0x0010)
    SetChrFlags(0x000D, 0x0800)
    SetChrPos(0x000D, -85910, 200, 59730, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, -87350, 300, -53560, 90)
    SetChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, -84730, 250, -53560, 270)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000A, 0x0010)
    SetChrPos(0x000A, -28700, 250, 53020, 270)
    SetChrPos(0x0009, -29640, 0, 51490, 0)

    def _loc_653(): pass

    label('loc_653')

    Return()

# id: 0x0001 offset: 0x654
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_66D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_66D(): pass

    label('loc_66D')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x677
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_68C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_68C(): pass

    label('loc_68C')

    Return()

# id: 0x0003 offset: 0x68D
@scena.Code('func_03_68D')
def func_03_68D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_6DF',
    )

    ChrTalk(
        0x0011,
        (
            '#0041050026V#035F以前我就这么觉得……\n',
            '他的演奏总是带有淡淡的忧伤呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BF')

    def _loc_6DF(): pass

    label('loc_6DF')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0011,
        (
            '#0041050021V#033F……嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050022V能听到口琴声呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050023V#030F这个好像是约修亚君\n',
            '在柏斯湖畔吹奏的曲子吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050024V#035F以前我就这么觉得……\n',
            '他的演奏总是带有淡淡的忧伤呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050025V虽然我没有听过，\n',
            '原曲也是这么悲伤吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BF(): pass

    label('loc_7BF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x7C3
@scena.Code('func_04_7C3')
def func_04_7C3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0010,
        (
            '#050F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结果还是没有和那个红头盔分出胜负……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#057F真是个半吊子的结局啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x82F
@scena.Code('func_05_82F')
def func_05_82F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_910',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_85B',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_88C')

    def _loc_85B(): pass

    label('loc_85B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_871',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_88C')

    def _loc_871(): pass

    label('loc_871')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_887',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_88C')

    def _loc_887(): pass

    label('loc_887')

    SetChrSubChip(0x00FE, 2)

    def _loc_88C(): pass

    label('loc_88C')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x000D,
        (
            '#0080120182V#070F哎呀哎呀，\n',
            '真没想到今天也能受到王城的招待呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120183V恢复和平之后，\n',
            '喝起酒来心情也舒畅了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x00FE, 0)

    Jump('loc_CAA')

    def _loc_910(): pass

    label('loc_910')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_91A',
    )

    Jump('loc_CAA')

    def _loc_91A(): pass

    label('loc_91A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_924',
    )

    Jump('loc_CAA')

    def _loc_924(): pass

    label('loc_924')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_AF1',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0102, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_94D',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_97E')

    def _loc_94D(): pass

    label('loc_94D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_963',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_97E')

    def _loc_963(): pass

    label('loc_963')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_979',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_97E')

    def _loc_979(): pass

    label('loc_979')

    SetChrSubChip(0x00FE, 2)

    def _loc_97E(): pass

    label('loc_97E')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_A16',
    )

    ChrTalk(
        0x000D,
        (
            '#0080120188V#070F不愧是王城啊。\n',
            '王国里美丽的景色都集中在这里了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120187V小姐们，如果打扫房间的话，\n',
            '拜托你们动作麻利一点好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE9')

    def _loc_A16(): pass

    label('loc_A16')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '#0080120184V#073F哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120185V#070F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120186V不愧是王城啊。\n',
            '王国里美丽的景色都集中在这里了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120187V小姐们，如果打扫房间的话，\n',
            '拜托你们动作麻利一点好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE9(): pass

    label('loc_AE9')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_CAA')

    def _loc_AF1(): pass

    label('loc_AF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 7, 0x63F)),
            Expr.Return,
        ),
        'loc_B71',
    )

    ChrTalk(
        0x000D,
        (
            '#0080120178V#070F料理非常美味，\n',
            '如果说还有什么美中不足的话，\n',
            '就是酒还没有喝爽啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120179V我现在就要再去痛饮一番。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAA')

    def _loc_B71(): pass

    label('loc_B71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_CAA',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B9A',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_B9F')

    def _loc_B9A(): pass

    label('loc_B9A')

    SetChrSubChip(0x00FE, 0)

    def _loc_B9F(): pass

    label('loc_B9F')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_C1E',
    )

    ChrTalk(
        0x000D,
        (
            '#0080120180V#070F说起来，\n',
            '奥利维尔那家伙那么努力，\n',
            '却没能来这里，真是可怜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120181V不过这又能怨谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA5')

    def _loc_C1E(): pass

    label('loc_C1E')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '#0080120176V#070F呼～不管什么时候，\n',
            '只要呆在酒吧里就会觉得肚子饿……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120177V晚宴怎么还没开始啊，\n',
            '我对宫廷料理的盛宴期待已久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CA5(): pass

    label('loc_CA5')

    SetChrSubChip(0x00FE, 0)

    def _loc_CAA(): pass

    label('loc_CAA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xCAE
@scena.Code('func_06_CAE')
def func_06_CAE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯，接下来是打扫客房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为今天有许多客人要在城里留宿，\n',
            '所以要做的准备不少啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xD0E
@scena.Code('func_07_D0E')
def func_07_D0E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_D1B',
    )

    Jump('loc_E61')

    def _loc_D1B(): pass

    label('loc_D1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D8E',
    )

    ChrTalk(
        0x00FE,
        (
            '《王城设计图》、《七至宝》、\n',
            '《百日战役全貌》……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '被情报部拿走的这些书\n',
            '终于又回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E61')

    def _loc_D8E(): pass

    label('loc_D8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_D98',
    )

    Jump('loc_E61')

    def _loc_D98(): pass

    label('loc_D98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_DA2',
    )

    Jump('loc_E61')

    def _loc_DA2(): pass

    label('loc_DA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_E04',
    )

    ChrTalk(
        0x00FE,
        (
            '完了，\n',
            '格兰赛尔城的设计图纸竟然也不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的家伙\n',
            '究竟打算拿去做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E61')

    def _loc_E04(): pass

    label('loc_E04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_E61',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的那群家伙，\n',
            '到底要做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然把严禁外借的\n',
            '重要资料强行取走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E61(): pass

    label('loc_E61')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xE65
@scena.Code('func_08_E65')
def func_08_E65():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 3, 0x63B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E74',
    )

    Call(0, 0x0009)

    Jump('loc_137C')

    def _loc_E74(): pass

    label('loc_E74')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_F7E',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EA0',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_ED1')

    def _loc_EA0(): pass

    label('loc_EA0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EB6',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_ED1')

    def _loc_EB6(): pass

    label('loc_EB6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_ECC',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_ED1')

    def _loc_ECC(): pass

    label('loc_ECC')

    SetChrSubChip(0x00FE, 2)

    def _loc_ED1(): pass

    label('loc_ED1')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0530120331V#780F真是个平静的夜晚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120332V#780F王国能够恢复这样的和平，\n',
            '多亏了艾丝蒂尔你们啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120333V卡西乌斯拥有这么好的孩子，\n',
            '真是让人羡慕。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x00FE, 0)

    Jump('loc_1379')

    def _loc_F7E(): pass

    label('loc_F7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_F88',
    )

    Jump('loc_1379')

    def _loc_F88(): pass

    label('loc_F88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_F92',
    )

    Jump('loc_1379')

    def _loc_F92(): pass

    label('loc_F92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1065',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FBB',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_FEC')

    def _loc_FBB(): pass

    label('loc_FBB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FD1',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_FEC')

    def _loc_FD1(): pass

    label('loc_FD1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FE7',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_FEC')

    def _loc_FE7(): pass

    label('loc_FE7')

    SetChrSubChip(0x00FE, 2)

    def _loc_FEC(): pass

    label('loc_FEC')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0530120327V#780F哦，\n',
            '想不到希尔丹夫人竟然亲自到访……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120328V唔，我明白了。\n',
            '是在培训实习的侍女吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x00FE, 0)

    Jump('loc_1379')

    def _loc_1065(): pass

    label('loc_1065')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_1152',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_108E',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_10BF')

    def _loc_108E(): pass

    label('loc_108E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_10A4',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_10BF')

    def _loc_10A4(): pass

    label('loc_10A4')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_10BA',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_10BF')

    def _loc_10BA(): pass

    label('loc_10BA')

    SetChrSubChip(0x00FE, 2)

    def _loc_10BF(): pass

    label('loc_10BF')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0530120329V#780F就上校所说的话来看，\n',
            '是非常合乎情理的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120330V但无论如何，也必须亲自向女王陛下\n',
            '还有公主殿下询问才恰当啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x00FE, 0)

    Jump('loc_1379')

    def _loc_1152(): pass

    label('loc_1152')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_1379',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_117B',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_11AC')

    def _loc_117B(): pass

    label('loc_117B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1191',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_11AC')

    def _loc_1191(): pass

    label('loc_1191')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11A7',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_11AC')

    def _loc_11A7(): pass

    label('loc_11A7')

    SetChrSubChip(0x00FE, 2)

    def _loc_11AC(): pass

    label('loc_11AC')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1222',
    )

    ChrTalk(
        0x000B,
        (
            '#0530120325V#782F呼～我有些担心啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120326V她会不会在回王都之前，\n',
            '先顺路去找特蕾莎院长了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1374')

    def _loc_1222(): pass

    label('loc_1222')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000B,
        (
            '#0530120318V#780F对了，我说你们俩啊……\n',
            '见到科洛丝了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120319V我从她那儿听说了\n',
            '你们约好在王都相见的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120320V#007F唔～这个啊，\n',
            '协会还没有通知我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120321V#014F请问校长，\n',
            '她已经来到王都了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530120322V#782F这是肯定的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120323V#783F呼～我有些担心啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120324V她会不会在回王都之前，\n',
            '先顺路去找特蕾莎院长了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1374(): pass

    label('loc_1374')

    SetChrSubChip(0x00FE, 0)

    def _loc_1379(): pass

    label('loc_1379')

    TalkEnd(0x00FE)

    def _loc_137C(): pass

    label('loc_137C')

    Return()

# id: 0x0009 offset: 0x137D
@scena.Code('func_09_137D')
def func_09_137D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 3, 0x63B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C04',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 3, 0x63B))
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -85750, 0, -55050, 0)
    SetChrPos(0x0102, -86740, 0, -55050, 0)
    CameraMove(-85810, 0, -53740, 0)
    SetChrSubChip(0x000B, 1)
    SetChrSubChip(0x0008, 2)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0340120269V#601F#1P哦哦，来了吗。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530120270V#780F呵呵，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120271V#004F哎……校长！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120272V#010F难道科林兹校长您\n',
            '也被邀请参加今天的晚宴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530120273V#780F是啊，就是乘今天的定期船\n',
            '从卢安赶过来的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120274V我已经听克劳斯市长说了，\n',
            '你们赢得了武术大会的冠军啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120275V乔儿他们听到了肯定也会十分高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120276V#506F嘿嘿……谢谢了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120277V#010F说起来，\n',
            '我没有想到校长也会被邀请来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340120278V#603F#1P科林兹校长作为利贝尔首屈一指的贤者，\n',
            '每年都会出席王国会议。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120279V被邀请出席晚宴也没有什么奇怪的啦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530120280V#780F哈哈，说我是贤者，\n',
            '克劳斯市长你真是太过誉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120281V#505F嗯……王国会议是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120282V#010F是为解决整个王国范围内的问题\n',
            '而召开的一年一度的例会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120283V女王陛下、各地区的市长，\n',
            '以及各界的代表人士齐聚一堂，\n',
            '讨论和协商各种各样的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120284V#501F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120285V那么，今天的晚宴\n',
            '邀请的都是这些人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530120286V#783F不……\n',
            '其实连一半都不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120287V女王陛下身体欠佳，\n',
            '摩尔根将军忙于军务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120288V卢安的戴尔蒙市长\n',
            '也因为那个案件被逮捕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120289V还有，拉赛尔博士也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0340120290V#603F和他相关的那个案件，\n',
            '现在还有很多地方没有弄清楚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120291V不仅牵扯到王室亲卫队，\n',
            '而且还说是大规模的恐怖组织所为，\n',
            '到底真相是怎样我们现在也很迷惑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120292V#602F真是的，在这种情况下，\n',
            '还有心思召开什么晚宴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120293V#003F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120294V#015F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 0)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0530120295V#780F不过，为了确认公爵大人真正的心意，\n',
            '我们也有出席这次晚宴的必要。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530120296V而且更重要的是……\n',
            '可以借此机会探望和问候女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340120297V#603F嗯，这才是最重要的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120298V#602F来到这格兰赛尔城，\n',
            '却不能拜见陛下这不是很奇怪吗。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120299V#601F而且……\n',
            '也很久没有见到科洛蒂娅公主了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120300V#501F科洛蒂娅公主……\n',
            '我记得是女王陛下的孙女吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120301V#014F公主殿下也住在格兰赛尔城吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 1)
    Sleep(100)

    SetChrSubChip(0x0008, 2)
    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0340120302V#604F#1P不，她平常是住在另外一个地方的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120303V不过，听说几天前回到王都来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120304V#501F哎～是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120305V#502F嗯～如果有机会，\n',
            '一定要和她见上一面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0530120306V#781F呵呵，如果是你们，\n',
            '肯定能见到她的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x0008, 0)
    EventEnd(0x00)

    Jump('loc_1F4B')

    def _loc_1C04(): pass

    label('loc_1C04')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1D2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C5A',
    )

    ChrTalk(
        0x0008,
        (
            '#0340120317V#600F以后我们也会一如既往地努力，\n',
            '为女王陛下工作。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D27')

    def _loc_1C5A(): pass

    label('loc_1C5A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0008,
        (
            '#0340120314V#600F公主殿下被抓做人质，\n',
            '女王陛下为此一定相当心痛吧……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120315V就算是为国家着想，\n',
            '但理查德上校也不应该走上这样一条路……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120316V……以后我们也会一如既往地努力，\n',
            '为女王陛下工作。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D27(): pass

    label('loc_1D27')

    Jump('loc_1F48')

    def _loc_1D2A(): pass

    label('loc_1D2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1D34',
    )

    Jump('loc_1F48')

    def _loc_1D34(): pass

    label('loc_1D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_1D3E',
    )

    Jump('loc_1F48')

    def _loc_1D3E(): pass

    label('loc_1D3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1D8B',
    )

    ChrTalk(
        0x0008,
        (
            '#0340120309V#600F哦，这不是希尔丹夫人吗……\n',
            '这么晚了还有什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F48')

    def _loc_1D8B(): pass

    label('loc_1D8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_1E87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1DD7',
    )

    ChrTalk(
        0x0008,
        (
            '#0340120310V#600F呼，一切都来得那么突然，\n',
            '怎能不让人震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E84')

    def _loc_1DD7(): pass

    label('loc_1DD7')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0008,
        (
            '#0340120311V#602F没想到陛下正为退位的决定\n',
            '而感到烦恼……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120312V而且那么快就把\n',
            '科洛蒂娅公主的婚姻大事提了出来。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120313V#603F一切都来得那么突然，\n',
            '怎能不让人震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E84(): pass

    label('loc_1E84')

    Jump('loc_1F48')

    def _loc_1E87(): pass

    label('loc_1E87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_1F48',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1EB0',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_1EE1')

    def _loc_1EB0(): pass

    label('loc_1EB0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1EC6',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_1EE1')

    def _loc_1EC6(): pass

    label('loc_1EC6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1EDC',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_1EE1')

    def _loc_1EDC(): pass

    label('loc_1EDC')

    SetChrSubChip(0x00FE, 1)

    def _loc_1EE1(): pass

    label('loc_1EE1')

    SetChrDirection(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0340120307V#603F真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120308V在这种状况下还要召开晚宴，\n',
            '不知道公爵是怎么想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x00FE, 0)

    def _loc_1F48(): pass

    label('loc_1F48')

    TalkEnd(0x00FE)

    def _loc_1F4B(): pass

    label('loc_1F4B')

    Return()

# id: 0x000A offset: 0x1F4C
@scena.Code('func_0A_1F4C')
def func_0A_1F4C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 2, 0x63A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F5B',
    )

    Call(0, 0x000B)

    Jump('loc_215C')

    def _loc_1F5B(): pass

    label('loc_1F5B')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1FCC',
    )

    ChrTalk(
        0x0009,
        (
            '#0370120264V#620F被卷入这样一个事件，\n',
            '真是不得了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370120265V这几天就让公主殿下\n',
            '好好休息一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2159')

    def _loc_1FCC(): pass

    label('loc_1FCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1FD6',
    )

    Jump('loc_2159')

    def _loc_1FD6(): pass

    label('loc_1FD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_1FE0',
    )

    Jump('loc_2159')

    def _loc_1FE0(): pass

    label('loc_1FE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_2078',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2017',
    )

    ChrTalk(
        0x0009,
        (
            '#0370120268V#620F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2075')

    def _loc_2017(): pass

    label('loc_2017')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0009,
        (
            '#0370120266V#620F……………………！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370120267V#621F…………………………\n',
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2075(): pass

    label('loc_2075')

    Jump('loc_2159')

    def _loc_2078(): pass

    label('loc_2078')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_20E7',
    )

    ChrTalk(
        0x0009,
        (
            '#0370120262V#620F看样子在晚宴上\n',
            '又出现了严重的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370120263V小姐的烦恼又增加了，\n',
            '真让我担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2159')

    def _loc_20E7(): pass

    label('loc_20E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_2159',
    )

    ChrTalk(
        0x0009,
        (
            '#0370120260V#621F小姐她因为能与你们二位相遇\n',
            '而感到非常的愉快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370120261V请二位以后一定要\n',
            '经常到柏斯来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2159(): pass

    label('loc_2159')

    TalkEnd(0x00FE)

    def _loc_215C(): pass

    label('loc_215C')

    Return()

# id: 0x000B offset: 0x215D
@scena.Code('func_0B_215D')
def func_0B_215D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 2, 0x63A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2957',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 2, 0x63A))
    EventBegin(0x00)
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -28930, 0, 54500, 180)
    SetChrPos(0x0102, -29780, 0, 54500, 180)
    CameraMove(-29260, 0, 53440, 0)
    SetChrSubChip(0x000A, 2)
    SetChrDirection(0x0009, 0, 0)
    OP_4A(0x0009, 255)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010120198V#501F啊……市长姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120199V#010F莉拉小姐也来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370120200V#621F艾丝蒂尔小姐、约修亚先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120201V#611F呵呵，我们又见面了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120202V我一直等着你们两个的到来呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120203V#001F市长姐姐果然也被邀请参加晚宴了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120204V#004F哎，为什么会知道我们要来……？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120205V#610F我是听克劳斯市长说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120206V你们在武术大会中获得优胜，\n',
            '所以肯定会被邀请出席晚宴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120207V#617F啊～如果早知道的话，\n',
            '我就放下所有工作来给你们加油了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370120208V#623F小姐，话虽这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370120209V可是，如果这样做的话，\n',
            '小姐自己不是到最后又要非常辛苦了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120210V#612F呜～我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120211V#506F啊哈哈……\n',
            '看来市长姐姐总是忙于公务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120212V#615F真是的，女王陛下暂且不论，\n',
            '那个杜南公爵举办的晚宴，\n',
            '本来就没有什么闲工夫来参加啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120213V都是因为那个军队的女军官\n',
            '固执地催促让我出席，\n',
            '我也是在没办法之下才来王都的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120214V#012F是情报部的凯诺娜上尉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120215V#612F嗯，就是她。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120216V表面很有礼貌，但其实不把别人放在眼里，\n',
            '我其实很不喜欢那种人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120217V而且最近……\n',
            '也没办法和摩尔根将军取得联系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120218V#002F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120219V#012F和哈肯大门那边联系不上吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120220V#615F那里守关的士兵老是说『将军不在』，\n',
            '每次都让我吃了闭门羹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120221V好像是为了应对恐怖事件，\n',
            '看来他的工作相当繁忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120222V#610F本来还想能不能\n',
            '在今天的晚宴上见到他呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120223V看起来好像也没有出席啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120224V#003F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120225V#012F请问市长您对这件事是怎么看的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120226V在这个时候把各市的市长召集起来\n',
            '召开这样的晚宴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120227V#613F这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120228V如果是女王陛下举办的话，\n',
            '应该是要宣布重要的事情吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120229V#611F不过这次大概只是为了\n',
            '陪杜南公爵打发时间而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120230V滥用陛下代理人的特权，\n',
            '让人认为他大权在握而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120231V#509F哇～真是精辟啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120232V#015F不过……\n',
            '也有可能不只是为这样的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0360120233V#611F算了，听说格兰赛尔城的西餐\n',
            '是整个利贝尔王国最棒的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120234V总之，享用完美味的晚餐，\n',
            '探望一下久未见面的女王陛下，\n',
            '然后明天一大早就赶快回柏斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 255)
    SetChrSubChip(0x000A, 0)
    EventEnd(0x00)

    Jump('loc_301D')

    def _loc_2957(): pass

    label('loc_2957')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_2AE5',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2983',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_29B4')

    def _loc_2983(): pass

    label('loc_2983')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2999',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_29B4')

    def _loc_2999(): pass

    label('loc_2999')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_29AF',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_29B4')

    def _loc_29AF(): pass

    label('loc_29AF')

    SetChrSubChip(0x00FE, 2)

    def _loc_29B4(): pass

    label('loc_29B4')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2A3C',
    )

    ChrTalk(
        0x000A,
        (
            '#0360120255V#610F艾丝蒂尔，\n',
            '我们打算乘坐明天的定期船回柏斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120256V#611F如果你们再到柏斯，\n',
            '一定要来找我们玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ADD')

    def _loc_2A3C(): pass

    label('loc_2A3C')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000A,
        (
            '#0360120255V#610F艾丝蒂尔，\n',
            '我们打算乘坐明天的定期船回柏斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120258V#611F如果你们再到柏斯，\n',
            '一定要来找我们玩哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120259V我们再去安特洛丝餐厅吃饭聊天吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2ADD(): pass

    label('loc_2ADD')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_301A')

    def _loc_2AE5(): pass

    label('loc_2AE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2AEF',
    )

    Jump('loc_301A')

    def _loc_2AEF(): pass

    label('loc_2AEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_2AF9',
    )

    Jump('loc_301A')

    def _loc_2AF9(): pass

    label('loc_2AF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_2D3E',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B22',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_2B53')

    def _loc_2B22(): pass

    label('loc_2B22')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B38',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_2B53')

    def _loc_2B38(): pass

    label('loc_2B38')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B4E',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_2B53')

    def _loc_2B4E(): pass

    label('loc_2B4E')

    SetChrSubChip(0x00FE, 2)

    def _loc_2B53(): pass

    label('loc_2B53')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2BB9',
    )

    ChrTalk(
        0x000A,
        (
            '#0360120246V#610F您背后的是实习女佣吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120247V让我想起莉拉刚来的时候了呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D36')

    def _loc_2BB9(): pass

    label('loc_2BB9')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000A,
        (
            '#0360120238V#610F希尔丹夫人，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0000,
        '希尔丹夫人',
        (
            '#0650120239V#712F梅贝尔市长，\n',
            '您好像非常劳累呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360120240V#617F呵呵，\n',
            '果然还是被您看出来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120241V#610F来这里之前有些棘手的事情要处理，\n',
            '所以就没有休息好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0000,
        '希尔丹夫人',
        (
            '#0650120242V#710F那样可不行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120243V稍后我拿一支催眠香为您点上吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120244V那个是最近从东方订购回来的呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360120245V#610F嗯，万分感激。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D36(): pass

    label('loc_2D36')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_301A')

    def _loc_2D3E(): pass

    label('loc_2D3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_2E98',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2D67',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_2D98')

    def _loc_2D67(): pass

    label('loc_2D67')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2D7D',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_2D98')

    def _loc_2D7D(): pass

    label('loc_2D7D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2D93',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_2D98')

    def _loc_2D93(): pass

    label('loc_2D93')

    SetChrSubChip(0x00FE, 2)

    def _loc_2D98(): pass

    label('loc_2D98')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2E07',
    )

    ChrTalk(
        0x000A,
        (
            '#0360120248V#612F那个杜南公爵将要继承王位……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120249V呼，\n',
            '从现在开始我就感到头疼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E90')

    def _loc_2E07(): pass

    label('loc_2E07')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000A,
        (
            '#0360120250V#612F晚宴上的一席话真是让人震惊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120251V那个杜南公爵将要继承王位……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120252V#617F呼，\n',
            '从现在开始我就感到头疼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E90(): pass

    label('loc_2E90')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_301A')

    def _loc_2E98(): pass

    label('loc_2E98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_301A',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2EC1',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_2EF2')

    def _loc_2EC1(): pass

    label('loc_2EC1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2ED7',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_2EF2')

    def _loc_2ED7(): pass

    label('loc_2ED7')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2EED',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_2EF2')

    def _loc_2EED(): pass

    label('loc_2EED')

    SetChrSubChip(0x00FE, 2)

    def _loc_2EF2(): pass

    label('loc_2EF2')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2F81',
    )

    ChrTalk(
        0x000A,
        (
            '#0360120253V#615F以前公爵到柏斯视察时，\n',
            '还在市内恣意妄为……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120237V#617F市民们纷纷跑来投诉，\n',
            '真是让我难办得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3015')

    def _loc_2F81(): pass

    label('loc_2F81')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000A,
        (
            '#0360120235V#615F公爵真是个麻烦的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120236V以前他到柏斯视察时，\n',
            '还在市内恣意妄为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120237V#617F市民们纷纷跑来投诉，\n',
            '真是让我难办得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3015(): pass

    label('loc_3015')

    SetChrSubChip(0x00FE, 0)

    def _loc_301A(): pass

    label('loc_301A')

    TalkEnd(0x00FE)

    def _loc_301D(): pass

    label('loc_301D')

    Return()

# id: 0x000C offset: 0x301E
@scena.Code('func_0C_301E')
def func_0C_301E():
    EventBegin(0x00)
    SetChrPos(0x0102, -52050, 0, 2040, 0)
    SetChrPos(0x0101, -52050, 0, 2040, 0)
    SetChrPos(0x0108, -52050, 0, 2040, 0)
    SetChrPos(0x000C, -52050, 0, 2040, 0)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0101, 0x0004)
    OP_69(0x000C, 0)
    OP_6A(0x000C)

    @scena.Lambda('lambda_308D')
    def lambda_308D():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_308D)

    Sleep(500)

    @scena.Lambda('lambda_30AD')
    def lambda_30AD():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_30AD)

    Sleep(500)

    @scena.Lambda('lambda_30CD')
    def lambda_30CD():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_30CD')

    DispatchAsync2(0x0102, 0x0002, lambda_30CD)

    @scena.Lambda('lambda_30DE')
    def lambda_30DE():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_30DE)

    Sleep(500)

    @scena.Lambda('lambda_30FE')
    def lambda_30FE():
        ChrWalkTo(0x00FE, -78180, 0, 2180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_30FE)

    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_311E')
    def lambda_311E():
        ChrWalkTo(0x00FE, -78970, 0, 7390, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_311E)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_313E')
    def lambda_313E():
        ChrWalkTo(0x00FE, -79880, 0, 5530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_313E)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_315E')
    def lambda_315E():
        ChrWalkTo(0x00FE, -78550, 0, 5460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_315E)

    WaitForThreadExit(0x0108, 0x0001)

    @scena.Lambda('lambda_317E')
    def lambda_317E():
        ChrWalkTo(0x00FE, -79280, 0, 4450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_317E)

    WaitForThreadExit(0x000C, 0x0001)
    Sleep(200)

    OP_6F(0x001D, 0)
    OP_70(0x001D, 60)
    Sleep(400)

    ChrWalkTo(0x000C, -80280, 0, 7250, 2000, 0x00)
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#2300120133V这个就是各位\n',
            '晚上可以使用的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120134V请进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120135V#501F啊，好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120136V#010F那么我们就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x000D)
    Sleep(500)

    TerminateThread(0x0102, 0x02)
    CreateThread(0x0102, 0x01, 0x00, 0x000D)
    Sleep(500)

    CreateThread(0x0108, 0x01, 0x00, 0x000D)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    ClearMapFlags(0x00000001)
    Fade(1000)
    CameraMove(-89640, 0, 57110, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 255, 0)
    SetChrPos(0x000C, -80040, 0, 50510, 0)
    SetChrPos(0x0101, -80880, 0, 53000, 270)
    SetChrPos(0x0102, -79650, 0, 53710, 270)
    SetChrPos(0x0108, -78830, 0, 52390, 270)
    SetChrFlags(0x000D, 0x0080)
    CameraMove(-79120, 0, 55910, 5000)
    ClearChrFlags(0x0101, 0x0040)
    ClearChrFlags(0x0101, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010120137V#004F#2P哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120138V#010F#2P能在这种地方过夜，\n',
            '真是做梦也无法想象呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120139V#071F#2P哎呀～真是不错啊，\n',
            '回共和国之后可以当成炫耀的资本了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120140V#2P在晚宴开始之前，\n',
            '请各位客人在此等候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3432')
    def lambda_3432():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3432)

    @scena.Lambda('lambda_3440')
    def lambda_3440():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3440)

    @scena.Lambda('lambda_344E')
    def lambda_344E():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_344E)

    CameraMove(-79790, 0, 52600, 1200)

    ChrTalk(
        0x000C,
        (
            '#2300120141V虽然城内允许自由参观，\n',
            '不过因为警卫上的理由，\n',
            '有一些场所是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120142V请不要到那些地方去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120143V#505F嗯……\n',
            '具体来说哪些地方不能去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120144V首先是，\n',
            '女王陛下居住的女王宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120145V就是在王城顶层空中庭园的一角\n',
            '建造的小型宫殿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120146V#008F空中庭园……\n',
            '听起来感觉十分的美丽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120147V嘻嘻……诞辰庆典的时候，\n',
            '陛下会在空中庭园的露台上\n',
            '向王都的市民致意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120148V如果只是到空中庭园去的话，\n',
            '我想应该没有什么问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120149V还有，其他禁止进入的场所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120150V一楼的亲卫队办公室\n',
            '以及地下的宝物库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0108, 255, 255, 255, 255, 0)

    ChrTalk(
        0x0102,
        (
            '#0020120151V#012F亲卫队办公室……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120152V#072F是不是被认定为恐怖分子\n',
            '而受到王国军通缉的那些人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120153V是、是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120154V现在，那个办公室\n',
            '正由情报部的人使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120155V所以不允许进入，\n',
            '请各位客人理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120156V#015F差不多明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120157V#010F对了，请问一下\n',
            '出席晚宴的其他客人现在在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120158V过一会儿，\n',
            '你们就能见到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120159V大概他们现在\n',
            '正在各自的房间里休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120160V#010F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120161V#501F这样的话，\n',
            '克劳斯市长已经来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120162V是的，\n',
            '刚刚才招待过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120163V那么，我先告退了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120164V如果各位客人有什么事情的话，\n',
            '请到一楼的侍女休息室来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 180, 400)

    @scena.Lambda('lambda_391E')
    def lambda_391E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_391E)

    ChrWalkTo(0x000C, -80140, 0, 48190, 2000, 0x00)
    SetChrFlags(0x000C, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010120165V#500F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrTurnDirection(0x0102, 0x0101, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '趁金没有注意的时候交换了一下眼色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    @scena.Lambda('lambda_39D3')
    def lambda_39D3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_39D3)

    Sleep(400)

    ChrTurnDirection(0x0102, 0x0108, 400)
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010120166V#006F……我说，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120167V我们想借此机会在城里参观一下……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120168V#010F晚宴开始之前就会回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120169V#075F哎呀哎呀，刚刚比赛完，\n',
            '你们年轻人真是精力旺盛啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120170V#070F好，你们去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120171V晚宴开始之前，\n',
            '我就在这豪华的房间里小憩一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-79060, 0, 5600, 0)
    FormationDelMember(0x07, 0xFF)
    SetChrPos(0x0101, -79060, 0, 9840, 0)
    SetChrPos(0x0102, -79060, 0, 9840, 0)
    OP_6F(0x001D, 60)

    @scena.Lambda('lambda_3B4A')
    def lambda_3B4A():
        ChrWalkTo(0x00FE, -79060, 0, 5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B4A)

    Sleep(600)

    @scena.Lambda('lambda_3B6A')
    def lambda_3B6A():
        ChrWalkTo(0x00FE, -79060, 0, 6400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3B6A)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_3B8A')
    def lambda_3B8A():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B8A)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_3B9D')
    def lambda_3B9D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3B9D)

    OP_72(0x001D, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x001D, 0)
    OP_73(0x001D)
    OP_71(0x001D, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010120172V#006F#4P在晚宴开始之前，\n',
            '一定要尽可能多做一些事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120173V首先要去找\n',
            '尤莉亚小姐所说的希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120174V#010F之后还有时间的话，\n',
            '我们最好去和其他的客人打个招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120175V大概，认识的人会很多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6A(0x0000)
    ClearMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x3C9F
@scena.Code('func_0D_3C9F')
def func_0D_3C9F():
    ChrWalkTo(0x00FE, -79010, 0, 7330, 3000, 0x00)

    @scena.Lambda('lambda_3CB9')
    def lambda_3CB9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3CB9)

    ChrWalkTo(0x00FE, -79000, 0, 9730, 3000, 0x00)

    Return()

# id: 0x000E offset: 0x3CDA
@scena.Code('func_0E_3CDA')
def func_0E_3CDA():
    EventBegin(0x00)
    CameraMove(-80000, 0, 52700, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x000D, 0x0080)
    FormationAddMember(0x07, 0xFF)
    SetChrPos(0x0101, -79490, 0, 51290, 0)
    SetChrPos(0x0102, -80530, 0, 51090, 0)
    SetChrPos(0x0108, -80180, 0, 61190, 0)

    @scena.Lambda('lambda_3D5A')
    def lambda_3D5A():
        CameraMove(-79580, 0, 57340, 2000)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3D5A)

    Sleep(1000)

    SetChrDirection(0x0108, 180, 400)
    WaitForThreadExit(0x0108, 0x0001)

    ChrTalk(
        0x0108,
        (
            '#0080120572V#070F哟，艾丝蒂尔、约修亚。\n',
            '回来得是不是有些晚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120573V就要到晚宴开始的时候了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3DE5')
    def lambda_3DE5():
        CameraMove(-80100, 0, 60780, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3DE5)

    @scena.Lambda('lambda_3DFD')
    def lambda_3DFD():
        ChrWalkTo(0x00FE, -79740, 0, 59790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3DFD)

    Sleep(300)

    @scena.Lambda('lambda_3E1D')
    def lambda_3E1D():
        ChrWalkTo(0x00FE, -80740, 0, 59720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3E1D)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010120574V#506F不好意思啊，金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120575V东看看西逛逛的就把时间给忘了～\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120576V#006F而且还和各地的市长谈了许多话哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120577V#073F咦，你们俩之前就\n',
            '认识那些有身份的人物吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120578V#010F洛连特的市长平日就对我们很亲切。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120579V其他的几位是我们在\n',
            '旅行途中经过各个城市时认识的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120580V#074F原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120581V游击士在完成任务的时候，\n',
            '的确有许多结识有身份人物的机会呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120582V#070F哈哈，这样看来，\n',
            '你们在王国好像相当活跃对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120583V#506F哈哈哈……还没有到那种程度啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120584V#501F对了，金先生到王都来\n',
            '是因为有什么任务要完成吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120585V我想，虽说是在别国，\n',
            '但还是照样可以完成相关任务吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120586V#070F是啊，一旦成为了正游击士，\n',
            '就可以去做一些超越国界的任务了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120587V不过预选赛啊，大使馆的手续啊什么的，\n',
            '忙得我连接受任务的时间都没有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120588V#075F不过，有其他四位游击士在，\n',
            '好像就没有我出场的必要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120589V#010F的确，如果游击士都聚集到一起，\n',
            '大部分事件都可以迎刃而解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120590V可是，假如都集中在王都的话，\n',
            '其他地方的支部可就人手不足了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120591V#071F哇哈哈，说的也是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120592V#007F呼，总觉得到现在\n',
            '才想到这些也用处不大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120593V#505F雪拉姐现在在洛连特做什么呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120594V#073F之前我也听你们提到过这个名字……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120595V那个雪拉姐莫非就是雪拉扎德？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010120596V#004F咦……你认识她！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120597V#014F是啊，她是我们的前辈，\n',
            '过去一直都在照顾着我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120598V#071F原来如此，竟然是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120599V以前她到卡尔瓦德来的时候，\n',
            '我和她曾经有过一面之缘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120600V真羡慕她有一个很好的老师啊，\n',
            '年纪轻轻却见多识广、身手不凡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120601V#008F（他说的那个老师不就是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120602V#019F（嗯，就是父亲呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0108, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    SetChrPos(0x000C, -80290, 0, 50310, 0)
    SetChrFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_4504')
    def lambda_4504():
        CameraMove(-80130, 0, 59550, 1500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_4504)

    @scena.Lambda('lambda_451C')
    def lambda_451C():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_451C)

    @scena.Lambda('lambda_452A')
    def lambda_452A():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_452A)

    @scena.Lambda('lambda_4538')
    def lambda_4538():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4538)

    PlaySE(6, 0x00, 0x64)
    ClearChrFlags(0x000C, 0x0080)
    ChrWalkTo(0x000C, -80410, 0, 53680, 2000, 0x00)
    WaitForThreadExit(0x0108, 0x0002)

    ChrTalk(
        0x000C,
        (
            '#2300120603V#2P打搅一下，\n',
            '晚宴已经准备完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2300120604V#2P现在我带大家过去可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120605V#070F#5P哦，我都已经等不及了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120606V#071F那～么，\n',
            '我们这就去好好享用这顿美餐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120607V#006F#5P嗯，说起来在比赛之后\n',
            '我的肚子已经饿得咕咕地叫了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120608V#001F走吧～大吃一顿去了～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    SetChrDirection(0x0102, 45, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120609V#019F#6P我说你们俩啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120610V还是不要忘记餐桌上的礼仪哦……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4251._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x470E
@scena.Code('func_0F_470E')
def func_0F_470E():
    EventBegin(0x00)
    FormationDelMember(0x07, 0xFF)
    ClearChrFlags(0x000D, 0x0080)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x000D, 6)
    OP_4A(0x000D, 255)
    SetChrPos(0x000D, -80180, 0, 61190, 180)
    SetChrPos(0x0101, -79740, 0, 59790, 0)
    SetChrPos(0x0102, -80740, 0, 59720, 0)
    CameraMove(-80100, 0, 60780, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0080120782V#070F哎呀，竟然意外地在晚宴上\n',
            '听到了这么出乎预料的消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120783V我一来就插入你们国家的谈话，\n',
            '把你们两个吓了一跳对吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120784V#005F那、那是当然的了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120785V要、要不是说得还比较周到的话……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080120786V#073F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120787V#506F啊，嗯，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120788V#505F可是……真是遗憾啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120789V虽然特地让舌头沉醉于美味的料理之中，\n',
            '可最后那道菜的精妙还是没能体会。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120790V#019F哈哈，不用强求嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120791V#010F对了，艾丝蒂尔。\n',
            '去散散步消化一下食物如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111312V#004F咦……？',
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
            '#0010120793V#006F啊啊！\n',
            '对啊，好建议！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120794V不错呢～我也想好好\n',
            '呼吸一下外面的新鲜空气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080120795V#073F啊～刚才去参观王城各处，\n',
            '这回吃完饭又要去散步了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120796V#075F想不承认都不行啊，\n',
            '这就是年纪的差异所体现的区别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010120797V#001F啊哈哈，金先生你太夸张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000D, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120798V#010F金先生也一起去走走如何？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120799V这个历史悠久的建筑里\n',
            '可供参观的地方还真是不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080120800V#070F嗯，等我想散步的时候，\n',
            '再到处溜达一下也不迟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120801V我现在要去厨房看看，\n',
            '应该还有一些剩余的食物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120802V#509F不会吧……还要打算吃吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080120803V#071F就算是吧，只是想弄点酒菜。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120804V王城好像有可以喝酒的小酒吧，\n',
            '待会儿我就去瞧瞧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004A, 0x04, 0x02)
    OP_28(0x004A, 0x04, 0x04)
    OP_28(0x004A, 0x01, 0x0001)
    OP_28(0x004A, 0x01, 0x0002)
    OP_28(0x004A, 0x01, 0x0004)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    OP_4B(0x000D, 255)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x4C71
@scena.Code('func_10_4C71')
def func_10_4C71():
    EventBegin(0x00)
    CameraMove(-79060, 0, 5600, 0)
    FormationDelMember(0x07, 0xFF)
    SetChrPos(0x0101, -79060, 0, 9840, 0)
    SetChrPos(0x0102, -79060, 0, 9840, 0)
    OP_6F(0x001D, 60)

    @scena.Lambda('lambda_4CB6')
    def lambda_4CB6():
        ChrWalkTo(0x00FE, -79060, 0, 5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4CB6)

    Sleep(600)

    @scena.Lambda('lambda_4CD6')
    def lambda_4CD6():
        ChrWalkTo(0x00FE, -79060, 0, 6400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4CD6)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_4CF6')
    def lambda_4CF6():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4CF6)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_4D09')
    def lambda_4D09():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4D09)

    OP_72(0x001D, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x001D, 0)
    OP_73(0x001D)
    OP_71(0x001D, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010120805V#007F#4P呼～……\n',
            '真是出乎预料的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120806V越来越想见女王陛下，\n',
            '问清楚这到底是怎么回事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120807V#012F首先按照约定去见希尔丹夫人吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120808V她应该有办法让我们见到陛下的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120809V#006F#4P嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x4E13
@scena.Code('func_11_4E13')
def func_11_4E13():
    EventBegin(0x00)
    CameraMove(-79390, 0, 54420, 0)
    OP_67(0, 4890, -10000, 0)
    CameraSetDistance(1680, 0)
    OP_6C(38000, 0)
    OP_6E(509, 0)
    SetChrPos(0x0101, -80040, 0, 48610, 0)
    SetChrPos(0x0102, -80040, 0, 48610, 0)
    SetChrPos(0x0108, -80040, 0, 48610, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 0, 0)
    FadeIn(1500, 0)

    @scena.Lambda('lambda_4EB5')
    def lambda_4EB5():
        CameraMove(-79660, 0, 55810, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4EB5)

    @scena.Lambda('lambda_4ECD')
    def lambda_4ECD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_4ECD)

    @scena.Lambda('lambda_4EDF')
    def lambda_4EDF():
        ChrWalkTo(0x00FE, -80030, 0, 55890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_4EDF)

    Sleep(800)

    @scena.Lambda('lambda_4EFF')
    def lambda_4EFF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4EFF)

    @scena.Lambda('lambda_4F11')
    def lambda_4F11():
        ChrWalkTo(0x00FE, -80320, 0, 54310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4F11)

    Sleep(500)

    @scena.Lambda('lambda_4F31')
    def lambda_4F31():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_4F31)

    @scena.Lambda('lambda_4F43')
    def lambda_4F43():
        ChrWalkTo(0x00FE, -79160, 0, 54220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4F43)

    WaitForThreadExit(0x0108, 0x0001)
    SetChrDirection(0x0108, 180, 400)

    ChrTalk(
        0x0108,
        (
            '#0080121561V#074F#5P哎呀呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121562V总算用比较擅长的手法蒙混过去了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010121563V#004F#6P哎……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121564V金先生，你不是喝醉了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121565V#070F#5P那个嘛，只是演演戏而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121566V我可是一滴酒都没喝过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121567V#009F#6P说谎！明明脸那么红……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121568V#015F驱动内力，让血气上游，\n',
            '让表面看起来一副喝醉的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121569V#010F在东方的武术里，\n',
            '这就是一种名为『气功』的功夫对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121570V#073F#5P哦，这种功夫你都知道，\n',
            '真是见多识广的年轻人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121571V#071F哎呀，刚才看见你们遇到了麻烦，\n',
            '所以我就忍不住叫了你们一声。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121572V怎么样，还算帮了点忙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121573V#007F#6P真是的，金先生你啊……\n',
            '有时候也会让人捉摸不透呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121574V#509F虽说是来帮我们解围的，\n',
            '但着实吓了人家一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121575V#071F#5P哈哈，抱歉抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121576V#070F那么，情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121577V#505F#6P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121578V什么怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121579V#070F#5P已经办完了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121580V和女王陛下见面的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010121581V#005F#3S#6P怎、怎么会～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121582V#580F#6P为、为、为什么金先生你知道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121583V#014F难道说这件事您是从\n',
            '艾南先生那里听说的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121584V#070F#5P协会那个小哥并没有告诉我什么。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121585V#071F我只是根据自己的推断，\n',
            '来套你们的话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121586V#509F#6P推、推断……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121587V#015F……没有任何的情报，\n',
            '是不可能做出这样的推断的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121588V#012F金先生……\n',
            '请问您究竟知道些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121589V#074F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121590V也该是把那个东西\n',
            '拿给你们看看的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0108, 0x0101, 800, 2000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金将一封信递给了艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0108, -80030, 0, 55890, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010121591V#004F#6P一、一封信……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121592V#014F这个笔迹是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121593V#070F#5P嗯，没错。\n',
            '你们先拿来读一读吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121594V然后就知道怎么回事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121595V#505F#6P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x000001F4)
    FadeOut(300, 0, 100)
    Sleep(500)

    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0160121596V',
            (TxtCtl.SetColor, 0x5),
            '金·瓦赛克阁下敬启。\n',
            '久疏问候，身体可好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121597V',
            (TxtCtl.SetColor, 0x5),
            '由于事出匆忙，\n',
            '我唯有采取开门见山的方式，万望见谅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121598V',
            (TxtCtl.SetColor, 0x5),
            '事实上，连同猎兵团在内的事件\n',
            '已经朝向帝国方向发展了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121599V',
            (TxtCtl.SetColor, 0x5),
            '可是，利贝尔国内似乎正有\n',
            '一股微妙的势力正在滋长蔓延着。\n',
            '若只是交给年轻人去处理，我有些放心不下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121600V',
            (TxtCtl.SetColor, 0x5),
            '我想请你帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121601V',
            (TxtCtl.SetColor, 0x5),
            '在我外出的时候，请你到利贝尔来，\n',
            '如果有什么情况发生的话，\n',
            '就帮帮那些年轻人，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121602V',
            (TxtCtl.SetColor, 0x5),
            '因为你是第一次前往利贝尔，\n',
            '所以顺便游山玩水也是不错的选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121603V',
            (TxtCtl.SetColor, 0x5),
            '女王诞辰庆典前夕，\n',
            '会举办一场允许外国人参加的武术大会，\n',
            '这是一个能了解形势的好机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121604V',
            (TxtCtl.SetColor, 0x5),
            '突然提出这样的请求，或许让你有些为难。\n',
            '不过如果你有空的话，还请帮帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121605V',
            (TxtCtl.SetColor, 0x5),
            '女王诞辰庆典之时我会回来，\n',
            '到那时我再一并向你感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121606V',
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯·布莱特',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121607V',
            (TxtCtl.SetColor, 0x5),
            '另：\n',
            '你也许会有机会\n',
            '见到我的女儿和儿子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121608V',
            (TxtCtl.SetColor, 0x5),
            '我让他们在游击士协会实习，\n',
            '当时没有想太多，只是锻炼一下他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160121609V',
            (TxtCtl.SetColor, 0x5),
            '如果他们有什么事，\n',
            '还请您助他们一臂之力，帮他们摆脱困境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_1F(0x64, 0x000001F4)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010121610V#580F#6P……这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121611V#015F金先生是受父亲委托来利贝尔的……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121612V#010F这么说父亲他现在……\n',
            '正在埃雷波尼亚帝国了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121613V#074F#5P嗯，就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121614V#509F#6P什么叫就是这样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121615V关、关键的是金先生嘛。\n',
            '哼哼，你竟然和老爸串通一气！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121616V#070F#5P串通一气什么的不太好听啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121617V以前卡西乌斯大人来到我们卡尔瓦德时，\n',
            '我也受到了他诸多方面的关照啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121618V我一直都想报答他，\n',
            '这封信正好了却了我的心愿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121619V#007F#6P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121620V#010F请问金先生是什么时候\n',
            '发觉我们是父亲的孩子的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121621V#070F#5P第一次见面时，\n',
            '看见艾丝蒂尔拿着棍子，\n',
            '我就开始有些注意了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121622V在询问了雾香之后我才确信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121623V#009F#6P金先生也真是的，\n',
            '之前连一个字也没和我们提起过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121624V我们不知道老爸的行踪，\n',
            '一直都是忧心忡忡的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121625V#075F#5P这一点我很抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121626V但是从字面上来看，\n',
            '感觉卡西乌斯大哥到帝国的行动\n',
            '是一定要保密才行的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121627V#070F话又说回来，看来你们俩\n',
            '已经完成了一件不小的事情对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121628V#004F#6P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121629V#006F我说约修亚，\n',
            '现在说出来已经没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121630V#010F嗯，既然如此，\n',
            '我们就向您一一道来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121631V我们刚刚办完的事情要说起来的话，\n',
            '可是一个很长的故事。',
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
            '艾丝蒂尔他们向金说明了\n',
            '拉赛尔博士的委托以及见到艾莉茜雅女王的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后说明了已经接受了女王的委托，\n',
            '要将被囚禁的科洛蒂娅公主解救出来的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0108,
        (
            '#0080121632V#074F#5P原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121633V听了晚宴上那些话后，\n',
            '我就感觉充满了火药味……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121634V#070F好的，为了完成这个委托，\n',
            '也让我助你们一臂之力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121635V#004F#6P咦，可以吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121636V#070F#5P啊，这是报答卡西乌斯大人\n',
            '恩情的绝好机会呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121637V请务必让我帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121638V#008F#6P金、金大哥……\n',
            '我、我们俩也请你多多关照了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121639V#010F再次请您多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    ClearMapFlags(0x00000800)
    NewScene('ED6_DT01/C4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
