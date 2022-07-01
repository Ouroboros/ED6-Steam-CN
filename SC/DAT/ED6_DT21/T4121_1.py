import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4121_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4121_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4121.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x9AC8
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Call(1, 0x000C)

    Return()

# id: 0x0001 offset: 0xAD
@scena.Code('Init')
def Init():
    Call(0, 0x0025)

    Return()

# id: 0x0002 offset: 0xB2
@scena.Code('ReInit')
def ReInit():
    Call(1, 0x0009)

    Return()

# id: 0x0003 offset: 0xB7
@scena.Code('func_03_B7')
def func_03_B7():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000A)
    ClearChrFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_147',
    )

    Jump('loc_189')

    def _loc_147(): pass

    label('loc_147')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_163',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_189')

    def _loc_163(): pass

    label('loc_163')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_17F',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_189')

    def _loc_17F(): pass

    label('loc_17F')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_189(): pass

    label('loc_189')

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000A, 0x0010)

    ChrTalk(
        0x000A,
        (
            '#0050271304V#051F哟，怎么了？',
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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_22A'),
        (-1, 'loc_276'),
    )

    def _loc_22A(): pass

    label('loc_22A')

    ChrTalk(
        0x000A,
        (
            '#0050271305V#051F哦，知道了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26F',
    )

    Call(0, 0x0005)

    Jump('loc_273')

    def _loc_26F(): pass

    label('loc_26F')

    Call(0, 0x0004)

    def _loc_273(): pass

    label('loc_273')

    Jump('loc_2D0')

    def _loc_276(): pass

    label('loc_276')

    ChrTalk(
        0x000A,
        (
            '#0050271306V#052F怎么，不调整了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271307V#050F需要我的重剑时\n',
            '尽管开口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D0')

    def _loc_2D0(): pass

    label('loc_2D0')

    SetChrSubChip(0x000A, 0)
    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0x2D9
@scena.Code('func_04_2D9')
def func_04_2D9():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_369',
    )

    Jump('loc_3AB')

    def _loc_369(): pass

    label('loc_369')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_385',
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

    Jump('loc_3AB')

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3A1',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3AB')

    def _loc_3A1(): pass

    label('loc_3A1')

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3AB(): pass

    label('loc_3AB')

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0009, 0x0010)

    ChrTalk(
        0x0009,
        (
            '#0030271323V#020F嗯，怎么了？',
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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_44C'),
        (-1, 'loc_491'),
    )

    def _loc_44C(): pass

    label('loc_44C')

    ChrTalk(
        0x0009,
        (
            '#0030271324V#020F哎呀，要调整队伍吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48A',
    )

    Call(0, 0x0005)

    Jump('loc_48E')

    def _loc_48A(): pass

    label('loc_48A')

    Call(0, 0x0004)

    def _loc_48E(): pass

    label('loc_48E')

    Jump('loc_4E6')

    def _loc_491(): pass

    label('loc_491')

    ChrTalk(
        0x0009,
        (
            '#0030271325V#020F呵呵，我就在这儿\n',
            '休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271326V那么，之后就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E6')

    def _loc_4E6(): pass

    label('loc_4E6')

    SetChrSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x4EF
@scena.Code('func_05_4EF')
def func_05_4EF():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ClearChrFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_57F',
    )

    Jump('loc_5C1')

    def _loc_57F(): pass

    label('loc_57F')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_59B',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5C1')

    def _loc_59B(): pass

    label('loc_59B')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_5B7',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5C1')

    def _loc_5B7(): pass

    label('loc_5B7')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5C1(): pass

    label('loc_5C1')

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000B, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0040271284V#030F哎呀，怎么了？',
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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_728',
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_66B'),
        (-1, 'loc_6C4'),
    )

    def _loc_66B(): pass

    label('loc_66B')

    ChrTalk(
        0x000B,
        (
            '#0040240128V#030F呵，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240129V看来是需要\n',
            '我这个天才的力量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0004)

    Jump('loc_725')

    def _loc_6C4(): pass

    label('loc_6C4')

    ChrTalk(
        0x000B,
        (
            '#0040271287V#030F哎呀，不要我了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040271288V呼，思恋我美妙的琴声时，\n',
            '尽管来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_725')

    def _loc_725(): pass

    label('loc_725')

    Jump('loc_7EF')

    def _loc_728(): pass

    label('loc_728')

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_735'),
        (-1, 'loc_78E'),
    )

    def _loc_735(): pass

    label('loc_735')

    ChrTalk(
        0x000B,
        (
            '#0040240128V#030F呵，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240129V看来是需要\n',
            '我这个天才的力量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0002)

    Jump('loc_7EF')

    def _loc_78E(): pass

    label('loc_78E')

    ChrTalk(
        0x000B,
        (
            '#0040271287V#030F哎呀，不要我了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040271288V呼，思恋我美妙的琴声时，\n',
            '尽管来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7EF')

    def _loc_7EF(): pass

    label('loc_7EF')

    SetChrSubChip(0x000B, 0)
    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x7F8
@scena.Code('func_06_7F8')
def func_06_7F8():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_844',
    )

    ChrTalk(
        0x000C,
        (
            '#0060231330V#040F各位，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231331V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D1')

    def _loc_844(): pass

    label('loc_844')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_892',
    )

    ChrTalk(
        0x000C,
        (
            '#0060231330V#040F各位，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231331V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D1')

    def _loc_892(): pass

    label('loc_892')

    ChrTalk(
        0x000C,
        (
            '#0060231330V#040F各位，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231331V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D1(): pass

    label('loc_8D1')

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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_92A'),
        (-1, 'loc_9DC'),
    )

    def _loc_92A(): pass

    label('loc_92A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_966',
    )

    ChrTalk(
        0x000C,
        (
            '#0060231332V#040F明白了。\n',
            '要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0004)

    Jump('loc_9D9')

    def _loc_966(): pass

    label('loc_966')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9A7',
    )

    ChrTalk(
        0x000C,
        (
            '#0060231332V#040F明白了。\n',
            '要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0003)

    Jump('loc_9D9')

    def _loc_9A7(): pass

    label('loc_9A7')

    ChrTalk(
        0x000C,
        (
            '#0060231332V#040F明白了。\n',
            '要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0002)

    def _loc_9D9(): pass

    label('loc_9D9')

    Jump('loc_A29')

    def _loc_9DC(): pass

    label('loc_9DC')

    ChrTalk(
        0x000C,
        (
            '#0060231333V#040F我在这里待命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231334V如果有事，\n',
            '请尽管开口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A29')

    def _loc_A29(): pass

    label('loc_A29')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0xA2D
@scena.Code('func_07_A2D')
def func_07_A2D():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A86',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271308V#560F啊，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B15')

    def _loc_A86(): pass

    label('loc_A86')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_ACE',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271310V#060F啊，姐姐是你们。\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B15')

    def _loc_ACE(): pass

    label('loc_ACE')

    ChrTalk(
        0x000D,
        (
            '#0070271311V#060F啊，姐姐是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B15(): pass

    label('loc_B15')

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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_B6E'),
        (-1, 'loc_D16'),
    )

    def _loc_B6E(): pass

    label('loc_B6E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C01',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_BC8',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BFA')

    def _loc_BC8(): pass

    label('loc_BC8')

    ChrTalk(
        0x000D,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BFA(): pass

    label('loc_BFA')

    Call(0, 0x0005)

    Jump('loc_D13')

    def _loc_C01(): pass

    label('loc_C01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_C8F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_C56',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C88')

    def _loc_C56(): pass

    label('loc_C56')

    ChrTalk(
        0x000D,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C88(): pass

    label('loc_C88')

    Call(0, 0x0004)

    Jump('loc_D13')

    def _loc_C8F(): pass

    label('loc_C8F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_CDD',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0F')

    def _loc_CDD(): pass

    label('loc_CDD')

    ChrTalk(
        0x000D,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D0F(): pass

    label('loc_D0F')

    Call(0, 0x0002)
    def _loc_D13(): pass

    label('loc_D13')

    Jump('loc_DF3')

    def _loc_D16(): pass

    label('loc_D16')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_D8F',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271320V#060F我就在这里等，\n',
            '有什么事就来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF0')

    def _loc_D8F(): pass

    label('loc_D8F')

    ChrTalk(
        0x000D,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271322V#060F我会在这里等的，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF0(): pass

    label('loc_DF0')

    Jump('loc_DF3')

    def _loc_DF3(): pass

    label('loc_DF3')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0xDF7
@scena.Code('func_08_DF7')
def func_08_DF7():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000E)
    ClearChrFlags(0x000E, 0x0010)
    ChrTurnDirection(0x000E, 0x0000, 0)

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_E87',
    )

    Jump('loc_EC9')

    def _loc_E87(): pass

    label('loc_E87')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EA3',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_EC9')

    def _loc_EA3(): pass

    label('loc_EA3')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EBF',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_EC9')

    def _loc_EBF(): pass

    label('loc_EBF')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_EC9(): pass

    label('loc_EC9')

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000E, 0x0010)

    ChrTalk(
        0x000E,
        (
            '#0080271327V#070F哦，情况怎么样？',
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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_F6E'),
        (-1, 'loc_103D'),
    )

    def _loc_F6E(): pass

    label('loc_F6E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FA6',
    )

    ChrTalk(
        0x000E,
        (
            '#0080271328V#070F要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0005)

    Jump('loc_103A')

    def _loc_FA6(): pass

    label('loc_FA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_FD9',
    )

    ChrTalk(
        0x000E,
        (
            '#0080271328V#070F要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0004)

    Jump('loc_103A')

    def _loc_FD9(): pass

    label('loc_FD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1011',
    )

    ChrTalk(
        0x000E,
        (
            '#0080271328V#070F要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0003)

    Jump('loc_103A')

    def _loc_1011(): pass

    label('loc_1011')

    ChrTalk(
        0x000E,
        (
            '#0080271328V#070F要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0002)

    def _loc_103A(): pass

    label('loc_103A')

    Jump('loc_107A')

    def _loc_103D(): pass

    label('loc_103D')

    ChrTalk(
        0x000E,
        (
            '#0080271332V#070F嗯，需要我的时候\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_107A')

    def _loc_107A(): pass

    label('loc_107A')

    SetChrSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x1083
@scena.Code('func_09_1083')
def func_09_1083():
    TalkBegin(0x0019)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.Eval, "OP_40(0x0415, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 7, 0x20E7)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_127E',
    )

    ChrTurnDirection(0x0019, 0x0101, 0)

    ChrTalk(
        0x0019,
        (
            '…………唔唔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0019,
        (
            '这、这不是如假包换的……\n',
            '『特级钓师认定证书』吗！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F咦……啊啊、\n',
            '罗伊德先生给的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '唔，只有钓上湖之主的人\n',
            '才能得到的特级钓师认定证书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '同时也是我等的\n',
            '同道之人的证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F是，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（不知道是该\n',
            '　高兴还是不高兴……）\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '而且，特级钓师\n',
            '在我们师团本部\n',
            '要多少钓饵就可以买多少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F啊，这有点\n',
            '令人高兴……\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '唔，是吧是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '如果需要鱼饵，\n',
            '就尽管跟我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20E7)
    TalkEnd(0x0019)

    Return()

    def _loc_127E(): pass

    label('loc_127E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 7, 0x20E7)),
            Expr.Return,
        ),
        'loc_12AD',
    )

    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129C',
    )

    OP_A9(0xDC)
    TalkEnd(0x0019)

    Return()

    def _loc_129C(): pass

    label('loc_129C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12AD',
    )

    TalkEnd(0x0019)

    Return()

    def _loc_12AD(): pass

    label('loc_12AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_12B7',
    )

    Jump('loc_1C3C')

    def _loc_12B7(): pass

    label('loc_12B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1365',
    )

    ChrTalk(
        0x0019,
        (
            '哪怕导力器停了,\n',
            '我们对钓鱼火热的\n',
            '热情也不会冷却。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '这种时候，正应该\n',
            '让市民们一起享受钓鱼的乐趣，\n',
            '让心情平静下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '还能确保食物，一石二鸟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_13C7')

    def _loc_1365(): pass

    label('loc_1365')

    ChrTalk(
        0x0019,
        (
            '这种时候，正应该\n',
            '让市民们一起享受钓鱼的乐趣，\n',
            '让心情平静下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '还能确保食物，一石二鸟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C7(): pass

    label('loc_13C7')

    Jump('loc_1C3C')

    def _loc_13CA(): pass

    label('loc_13CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_14FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_149E',
    )

    ChrTalk(
        0x0019,
        (
            '咱们的同伴佩苏尔\n',
            '去调查洛连特的钓鱼场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '如果找到不为人知的好地方，\n',
            '说不定就潜藏着湖之主呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '而且还有在洛连特召开\n',
            '讲习会的大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '对我们师团的发展来说,\n',
            '他的任务至关重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_14FA')

    def _loc_149E(): pass

    label('loc_149E')

    ChrTalk(
        0x0019,
        (
            '咱们的同伴佩苏尔\n',
            '去调查洛连特的钓鱼场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '对我们师团的发展来说\n',
            '他的任务至关重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14FA(): pass

    label('loc_14FA')

    Jump('loc_1C3C')

    def _loc_14FD(): pass

    label('loc_14FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_1558',
    )

    ChrTalk(
        0x0019,
        (
            '看你似乎有点慌张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '如果不冷静沉着观察\n',
            '整个钓鱼场，是钓不到东西的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3C')

    def _loc_1558(): pass

    label('loc_1558')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_16AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_164F',
    )

    ChrTalk(
        0x0019,
        (
            '这瓦雷利亚湖里的湖之主\n',
            '在过去１０年以上时间里,\n',
            '可都重复着和我们钓公师团的死斗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '要把那巨大的鱼\n',
            '给钓上来是我们毕生的誓愿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '相信我们同心协力，\n',
            '一定能够做到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '没有钓不上的鱼！\n',
            '这就是我们钓公师团的座右铭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_16A9')

    def _loc_164F(): pass

    label('loc_164F')

    ChrTalk(
        0x0019,
        (
            '相信我们同心协力，\n',
            '一定能够做到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '没有钓不上的鱼！\n',
            '这就是我们钓公师团的座右铭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16A9(): pass

    label('loc_16A9')

    Jump('loc_1C3C')

    def _loc_16AC(): pass

    label('loc_16AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1780',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 2, 0x1632)),
            Expr.Return,
        ),
        'loc_173E',
    )

    ChrTalk(
        0x0019,
        (
            '穿白裙子的少女\n',
            '问了在下一个奇怪的问题，\n',
            '已经走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '问的问题记得是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '是『你知道又辣又苦又美味\n',
            '的店在哪里吗？』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_177D')

    def _loc_173E(): pass

    label('loc_173E')

    ChrTalk(
        0x0019,
        (
            '唔，在找谁吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '现在这里除了我\n',
            '和团员应该没别人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_177D(): pass

    label('loc_177D')

    Jump('loc_1C3C')

    def _loc_1780(): pass

    label('loc_1780')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1800',
    )

    ChrTalk(
        0x0019,
        (
            '师团创立已经２０年……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '赞同我们理念的\n',
            '同志的数量稳步增加着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '唔嗯，为了纪念这个\n',
            '打算召开盛大的活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3C')

    def _loc_1800(): pass

    label('loc_1800')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1857',
    )

    ChrTalk(
        0x0019,
        (
            '不过今天打算早早\n',
            '结束这边去瓦雷利亚湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '我今晚的目标是银伞鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3C')

    def _loc_1857(): pass

    label('loc_1857')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_19A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_192B',
    )

    ChrTalk(
        0x0019,
        (
            '跨越三国的互不侵犯条约……\n',
            '是动力引起的响声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '……我们钓公师团也总有一天\n',
            '会在帝国和共和国拥有支部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '那时才能与游击士协会对抗\n',
            '挂上『钓公师协会』的名号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '这是我小小的野心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_199F')

    def _loc_192B(): pass

    label('loc_192B')

    ChrTalk(
        0x0019,
        (
            '……我们钓公师团也总有一天\n',
            '会在帝国和共和国拥有支部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '那时才能与游击士协会对抗\n',
            '挂上『钓公师协会』的名号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_199F(): pass

    label('loc_199F')

    Jump('loc_1C3C')

    def _loc_19A2(): pass

    label('loc_19A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1BB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 5, 0x164D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B65',
    )

    ChrTalk(
        0x0019,
        (
            '哦哦，来得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '我们『钓公师团』今天\n',
            '也在积极准备活动,\n',
            '为了钓上利贝尔全境的湖之主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#264F……湖之主，是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x012F, 400)

    ChrTalk(
        0x0101,
        (
            '#1015F嗯……\n',
            '唔，也就是大鱼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F这里似乎是利贝尔\n',
            '钓鱼迷们汇集的地方哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '玲和爸爸一起钓过鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0101, 400)

    ChrTalk(
        0x012F,
        (
            '#261F呵呵呵……\n',
            '姐姐真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '钓鱼不是小孩\n',
            '和男人做的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F呜……\n',
            '话，话是没错啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F但是，我也钓的哦。\n',
            '很有趣嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#264F是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#265F那，玲下次\n',
            '也试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x164D)

    Jump('loc_1BB1')

    def _loc_1B65(): pass

    label('loc_1B65')

    ChrTalk(
        0x0019,
        (
            '你要是也喜欢钓鱼\n',
            '随时都可以来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '我们衷心期盼着\n',
            '有爱的人入团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BB1(): pass

    label('loc_1BB1')

    Jump('loc_1C3C')

    def _loc_1BB4(): pass

    label('loc_1BB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1C3C',
    )

    ChrTalk(
        0x0019,
        (
            '哦哦！\n',
            '欢迎来到『钓公师团』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '我乃『钓鱼男爵』\n',
            '是钓鱼者的团长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '诸位是志愿入团者吗？\n',
            '如果喜欢钓鱼那可是热烈欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C3C(): pass

    label('loc_1C3C')

    TalkEnd(0x0019)

    Return()

# id: 0x000A offset: 0x1C40
@scena.Code('func_0A_1C40')
def func_0A_1C40():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_1C4D',
    )

    Jump('loc_24EA')

    def _loc_1C4D(): pass

    label('loc_1C4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CA5',
    )

    ChrTalk(
        0x00FE,
        (
            '即使没有导力\n',
            '也没什么好不安的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和寻找湖之主露营的时候\n',
            '完全一样嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_1CA5(): pass

    label('loc_1CA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1DD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D58',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天去了港湾区\n',
            '碰上了不得了的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战车跑出来，\n',
            '还出现巨大人偶样的东西.\n',
            '真是不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从我的角度来说，\n',
            '那附近的鱼会不会变敏感，\n',
            '才是最担心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_1DD3')

    def _loc_1D58(): pass

    label('loc_1D58')

    ChrTalk(
        0x00FE,
        (
            '港湾区出现了战车，\n',
            '还出现巨大人偶样的东西.\n',
            '真是不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从我的角度来说，\n',
            '那附近的鱼会不会变敏感，\n',
            '才是最担心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DD3(): pass

    label('loc_1DD3')

    Jump('loc_24EA')

    def _loc_1DD6(): pass

    label('loc_1DD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_1E34',
    )

    ChrTalk(
        0x00FE,
        (
            '好吧，明天难得要\n',
            '挑战夜晚的瓦雷利亚湖！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '此外港湾区的仓库街\n',
            '有很大的鱼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_1E34(): pass

    label('loc_1E34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_1F4E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EEB',
    )

    ChrTalk(
        0x00FE,
        (
            '根据报告瓦雷利亚湖的\n',
            '湖之主好像还在柏斯地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我打算近日飞去柏斯地区\n',
            '再次挑战那家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次就差一点点,\n',
            '没想到鱼线断了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次一定，这次一定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_1F4B')

    def _loc_1EEB(): pass

    label('loc_1EEB')

    ChrTalk(
        0x00FE,
        (
            '根据报告瓦雷利亚湖的\n',
            '湖之主好像还在柏斯地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我打算近日飞去柏斯地区\n',
            '再次挑战那家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F4B(): pass

    label('loc_1F4B')

    Jump('loc_24EA')

    def _loc_1F4E(): pass

    label('loc_1F4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_20B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 1, 0x1631)),
            Expr.Return,
        ),
        'loc_1FAA',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才１楼有位穿着飘逸的\n',
            '白裙子的女孩来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莫非是希望入团的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B2')

    def _loc_1FAA(): pass

    label('loc_1FAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2064',
    )

    ChrTalk(
        0x00FE,
        (
            '入团以后，有位女士的水平\n',
            '是节节提高的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她叫诺琪，\n',
            '是诞辰庆典前后入团的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前阵子终于钓上了湖之主\n',
            '成为和我同级的特级钓师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下，我也\n',
            '不能不当回事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_20B2')

    def _loc_2064(): pass

    label('loc_2064')

    ChrTalk(
        0x00FE,
        (
            '入团以后，有位女士的水平\n',
            '是节节提高的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下，我也\n',
            '不能不当回事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20B2(): pass

    label('loc_20B2')

    Jump('loc_24EA')

    def _loc_20B5(): pass

    label('loc_20B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_212D',
    )

    ChrTalk(
        0x00FE,
        (
            '作为普及钓鱼文化的\n',
            '一环我们打算\n',
            '开拓新的钓鱼场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅如此\n',
            '为了不使钓鱼场荒废\n',
            '还要进行环境保护活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_212D(): pass

    label('loc_212D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_218E',
    )

    ChrTalk(
        0x00FE,
        (
            '糟糕！！\n',
            '已经到黄昏时间了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个时间不去钓鱼场\n',
            '多么可惜啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_21D1')

    def _loc_218E(): pass

    label('loc_218E')

    ChrTalk(
        0x00FE,
        (
            '傍晚的这个时间，\n',
            '鱼很活跃非常容易钓起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没理由错过这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21D1(): pass

    label('loc_21D1')

    Jump('loc_24EA')

    def _loc_21D4(): pass

    label('loc_21D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2246',
    )

    ChrTalk(
        0x00FE,
        (
            '钓鱼就是和自然作战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常使出全力\n',
            '也无法顺自己的意行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵……\n',
            '这也是钓鱼的奥妙所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_2246(): pass

    label('loc_2246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2337',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22F3',
    )

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔地区水边比较少,\n',
            '应该钓鱼场也少吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是且慢！\n',
            '附近有意外的好地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾尔贝离宫附近\n',
            '的罗马尔池知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的鱼影相当多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_2334')

    def _loc_22F3(): pass

    label('loc_22F3')

    ChrTalk(
        0x00FE,
        (
            '艾尔贝离宫附近\n',
            '的罗马尔池知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的鱼影相当多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2334(): pass

    label('loc_2334')

    Jump('loc_24EA')

    def _loc_2337(): pass

    label('loc_2337')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_24EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 6, 0x164E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2490',
    )

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '咦…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F啊，罗伊德先生？\n',
            '从卢安回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钓果如何。\n',
            '给你的鱼竿好用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊，嗯，\n',
            '工作间歇不时有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像你这样有资质的人，\n',
            '钓公师团是热烈欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想入团的时候，\n',
            '随时都可以跟团长说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他啊，\n',
            '一定会高兴得举双手赞成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F啊哈哈……\n',
            '会考虑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x164E)

    Jump('loc_24EA')

    def _loc_2490(): pass

    label('loc_2490')

    ChrTalk(
        0x00FE,
        (
            '像你这样有资质的人，\n',
            '钓公师团是热烈欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想入团的时候，\n',
            '随时都可以跟团长说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24EA(): pass

    label('loc_24EA')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x24EE
@scena.Code('func_0B_24EE')
def func_0B_24EE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_24FB',
    )

    Jump('loc_2A3B')

    def _loc_24FB(): pass

    label('loc_24FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2574',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的团员平常\n',
            '就适应了户外生活嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不像其他人那样\n',
            '惊惶失措哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '罗伊德似乎摩擦树木\n',
            '生起了火。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3B')

    def _loc_2574(): pass

    label('loc_2574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_257E',
    )

    Jump('loc_2A3B')

    def _loc_257E(): pass

    label('loc_257E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_25C3',
    )

    ChrTalk(
        0x00FE,
        (
            '之后预定是\n',
            '和团长碰头来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说有新任务给我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3B')

    def _loc_25C3(): pass

    label('loc_25C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_25FA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，正想着肚子饿了\n',
            '原来已经到晚上了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3B')

    def _loc_25FA(): pass

    label('loc_25FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_26B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 1, 0x1631)),
            Expr.Return,
        ),
        'loc_2652',
    )

    ChrTalk(
        0x00FE,
        (
            '最近女性的钓鱼迷\n',
            '好像也在增加呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为我们来说是热烈欢迎啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26B6')

    def _loc_2652(): pass

    label('loc_2652')

    ChrTalk(
        0x00FE,
        (
            '导力照相机普及之后\n',
            '就不太取鱼的拓本了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，大家伙上钩的时候\n',
            '还是想用那样的形态留下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26B6(): pass

    label('loc_26B6')

    Jump('loc_2A3B')

    def _loc_26B9(): pass

    label('loc_26B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_26E2',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～今天\n',
            '去哪里钓鱼呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3B')

    def _loc_26E2(): pass

    label('loc_26E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2825',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27B3',
    )

    ChrTalk(
        0x00FE,
        (
            '讲习中带初学者出去,\n',
            '晕船的人也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为对策要保持充足睡眠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，乘船前\n',
            '肚子不要吃得太饱哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是刚刚开始钓鱼的人,\n',
            '经常为了前一天的准备，\n',
            '来的时候都睡眠不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_2822')

    def _loc_27B3(): pass

    label('loc_27B3')

    ChrTalk(
        0x00FE,
        (
            '讲习中带初学者出去,\n',
            '晕船的人也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为对策要保持充足睡眠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，乘船前\n',
            '肚子不要吃得太饱哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2822(): pass

    label('loc_2822')

    Jump('loc_2A3B')

    def _loc_2825(): pass

    label('loc_2825')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_28A5',
    )

    ChrTalk(
        0x00FE,
        (
            '想起来政变的时候\n',
            '可真惨啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明持续着钓鱼的绝好天气,\n',
            '却禁止夜间外出……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我们来说\n',
            '简直是残酷的折磨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3B')

    def _loc_28A5(): pass

    label('loc_28A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_29EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2991',
    )

    ChrTalk(
        0x00FE,
        (
            '钓公师团的团员是根据实绩\n',
            '来编排等级。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钓过所谓湖之主的\n',
            '罗伊德是『特级钓师』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还和初学者一样的我,\n',
            '就是『初级钓师』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '顺带一提,团长有着\n',
            '一个自己独特的等级称号……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '叫做『太公望』。\n',
            '真有型啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_29E8')

    def _loc_2991(): pass

    label('loc_2991')

    ChrTalk(
        0x00FE,
        (
            '钓公师团的团员是根据实绩\n',
            '来编排等级。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还和初学者一样的我,\n',
            '就是『初级钓师』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29E8(): pass

    label('loc_29E8')

    Jump('loc_2A3B')

    def _loc_29EB(): pass

    label('loc_29EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2A3B',
    )

    ChrTalk(
        0x00FE,
        (
            '潜藏在各地钓鱼场的湖之主……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也希望有一天\n',
            '能钓上湖之主来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A3B(): pass

    label('loc_2A3B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2A3F
@scena.Code('func_0C_2A3F')
def func_0C_2A3F():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3539',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BCE',
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
            TXT(0x00, '【◇哪里都没恢复通信】\n'),
            TXT(0x01, '【◇只有洛连特恢复了通信】\n'),
            TXT(0x02, '【◇只有卢安恢复了通信】\n'),
            TXT(0x03, '【◇只有蔡斯恢复了通信】\n'),
            TXT(0x04, '【◇洛连特·卢安恢复了通信】\n'),
            TXT(0x05, '【◇洛连特·蔡斯恢复了通信】\n'),
            TXT(0x06, '【◇卢安·蔡斯恢复了通信】\n'),
            TXT(0x07, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_2B7A'),
        (0x00000001, 'loc_2B86'),
        (0x00000002, 'loc_2B92'),
        (0x00000003, 'loc_2B9E'),
        (0x00000004, 'loc_2BAA'),
        (0x00000005, 'loc_2BB6'),
        (0x00000006, 'loc_2BC2'),
        (-1, 'loc_2BCE'),
    )

    def _loc_2B7A(): pass

    label('loc_2B7A')

    OP_A3(0x2003)
    OP_A3(0x2001)
    OP_A3(0x2005)

    Jump('loc_2BCE')

    def _loc_2B86(): pass

    label('loc_2B86')

    OP_A2(0x2003)
    OP_A3(0x2001)
    OP_A3(0x2005)

    Jump('loc_2BCE')

    def _loc_2B92(): pass

    label('loc_2B92')

    OP_A3(0x2003)
    OP_A2(0x2001)
    OP_A3(0x2005)

    Jump('loc_2BCE')

    def _loc_2B9E(): pass

    label('loc_2B9E')

    OP_A3(0x2003)
    OP_A3(0x2001)
    OP_A2(0x2005)

    Jump('loc_2BCE')

    def _loc_2BAA(): pass

    label('loc_2BAA')

    OP_A2(0x2003)
    OP_A2(0x2001)
    OP_A3(0x2005)

    Jump('loc_2BCE')

    def _loc_2BB6(): pass

    label('loc_2BB6')

    OP_A2(0x2003)
    OP_A3(0x2001)
    OP_A2(0x2005)

    Jump('loc_2BCE')

    def _loc_2BC2(): pass

    label('loc_2BC2')

    OP_A3(0x2003)
    OP_A2(0x2001)
    OP_A2(0x2005)

    Jump('loc_2BCE')

    def _loc_2BCE(): pass

    label('loc_2BCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 2, 0x20DA)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33E9',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370849V#763F哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370850V#760F各位、还有……约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370851V欢迎你们，\n',
            '终于回到这里了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370852V#1040F艾南先生……\n',
            '抱歉让您担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590370853V#761F哪里，没事就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370854V#760F今后还是作为游击士协会\n',
            '的同伴，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370855V#1002F艾南先生，事不宜迟，\n',
            '王都的状况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590370856V#764F这个啊，导力器\n',
            '突然不能使用时\n',
            '城中确实是一片混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370857V#762F对面的工房也是，\n',
            '寻求修理的市民一齐涌来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370858V#760F然而，那里立刻\n',
            '放出了艾莉茜雅女王发出的布告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370859V说导力停止的原因正在调查中。\n',
            '请大家镇定下来，\n',
            '像平常一样生活───',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370860V因此市里并没发生大的\n',
            '纠纷和恐慌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370861V#1018F原来如此，不愧是女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590370862V#762F嗯嗯……然而，\n',
            '湖上出现了贝壳样物体……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370863V许多市民担心是由其导致\n',
            '导力停止而开始不安的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370864V#1042F原来如此，也难怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590370865V#762F现在港口参观\n',
            '那个物体的人好像增加了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370866V其他奇怪的事情，\n',
            '就是王城的大门由于\n',
            '导力停止无法开关了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370867V#1015F是吗……不过，大家\n',
            '似乎比想象中镇定得多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590370868V#760F是的……但是，这个情况\n',
            '如果持续下去难说不会引起混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370869V我们也想分秒必争地\n',
            '收集到各地的正确情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370870V#1035F因此要去各个支部\n',
            '恢复通信，确保正确的情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370871V#1006F就是说我们的任务\n',
            '相当重要吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370872V#1002F好，得鼓起\n',
            '干劲来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_31AE',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370873V#1042F洛连特、卢安、\n',
            '还有蔡斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370874V哪里都好，\n',
            '赶快把『零力场发生器』送去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335B')

    def _loc_31AE(): pass

    label('loc_31AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_31FB',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370875V#1040F剩下的是卢安、\n',
            '还有蔡斯的协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335B')

    def _loc_31FB(): pass

    label('loc_31FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_324A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370876V#1040F剩下的是洛连特、\n',
            '还有蔡斯的协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335B')

    def _loc_324A(): pass

    label('loc_324A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3299',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370877V#1040F剩下的是洛连特、\n',
            '还有卢安的协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335B')

    def _loc_3299(): pass

    label('loc_3299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32DA',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370878V#1040F剩下的是蔡斯的协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335B')

    def _loc_32DA(): pass

    label('loc_32DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_331B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370879V#1040F剩下的是卢安的协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335B')

    def _loc_331B(): pass

    label('loc_331B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_335B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370880V#1040F剩下的是洛连特的协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_335B(): pass

    label('loc_335B')

    ChrTalk(
        0x0101,
        (
            '#0010370881V#1000F嗯，得赶快了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590370882V#760F说利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370883V就请多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20DA)
    TalkEnd(0x0008)

    Return()

    def _loc_33E9(): pass

    label('loc_33E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 3, 0x20DB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3539',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_34C4',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370884V#762F这附近的居民\n',
            '已经去协会避难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370885V在其他的街区，军队也\n',
            '应该已经在做避难引导了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370886V各位，快去追\n',
            '前往城堡的执行者们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370887V#765F他们的目的恐怕是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3536')

    def _loc_34C4(): pass

    label('loc_34C4')

    ChrTalk(
        0x0008,
        (
            '#0590370882V#760F说利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370889V请刻不容缓地\n',
            '恢复各支部的通信机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3536(): pass

    label('loc_3536')

    OP_A2(0x20DB)

    def _loc_3539(): pass

    label('loc_3539')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_35A2',
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
            TXT(0x02, '呼叫同伴\n'),
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
    FadeIn(300, 0)

    Jump('loc_35A6')

    def _loc_35A2(): pass

    label('loc_35A2')

    Call(6, 0x0005)

    def _loc_35A6(): pass

    label('loc_35A6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36A2',
    )

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_35D0',
    )

    OP_28(0x00C3, 0x04, 0x20)

    def _loc_35D0(): pass

    label('loc_35D0')

    If(
        (
            (Expr.Eval, "OP_A9(0xCD)"),
            Expr.Return,
        ),
        'loc_363B',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370890V#760F辛苦了。\n',
            '看来顺利达到目的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370891V完成了什么任务的话\n',
            '请再来报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_369C')

    def _loc_363B(): pass

    label('loc_363B')

    ChrTalk(
        0x0008,
        (
            '#0590370892V#760F现在\n',
            '好象没有能报告的工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370893V完成了什么任务的话\n',
            '请再来报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_369C(): pass

    label('loc_369C')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_36A2(): pass

    label('loc_36A2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3778',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3774',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370894V#760F把大家都叫来这里吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370895V明白了。\n',
            '那么我马上去联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '联络各支部，\n',
            '集合了待命人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_0D()

    def _loc_3774(): pass

    label('loc_3774')

    TalkEnd(0x0008)

    Return()

    def _loc_3778(): pass

    label('loc_3778')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3789',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_3789(): pass

    label('loc_3789')

    Call(1, 0x000D)

    Return()

# id: 0x000D offset: 0x378E
@scena.Code('func_0D_378E')
def func_0D_378E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_3861',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370884V#762F这附近的居民\n',
            '已经去协会避难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370885V在其他的街区，军队也\n',
            '应该已经在做避难引导了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370886V各位，快去追\n',
            '前往城堡的执行者们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370887V#765F他们的目的恐怕是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DD5')

    def _loc_3861(): pass

    label('loc_3861')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3D12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38F9',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370882V#760F说利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370901V洛连特，卢安，蔡斯……\n',
            '请恢复各支部的通信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D0F')

    def _loc_38F9(): pass

    label('loc_38F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_39A8',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370902V#760F通信还没回复的是\n',
            '卢安，还有蔡斯支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370903V利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370904V劳你跑一趟了，\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D0F')

    def _loc_39A8(): pass

    label('loc_39A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A5D',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370905V#760F通信还没回复的是\n',
            '是洛连特，还有蔡斯支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370903V利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370904V劳你跑一趟了，\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D0F')

    def _loc_3A5D(): pass

    label('loc_3A5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B12',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370908V#760F通信还没回复的是\n',
            '是洛连特，还有卢安支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370903V利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370904V劳你跑一趟了，\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D0F')

    def _loc_3B12(): pass

    label('loc_3B12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3BBC',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370911V#760F通信还没回复的是\n',
            '只有蔡斯支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370903V利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370904V劳你跑一趟了，\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D0F')

    def _loc_3BBC(): pass

    label('loc_3BBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C66',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370914V#760F通信还没回复的是\n',
            '只有卢安支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370903V利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370904V劳你跑一趟了，\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D0F')

    def _loc_3C66(): pass

    label('loc_3C66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D0F',
    )

    ChrTalk(
        0x0008,
        (
            '#0590370917V#760F通信还没回复的是\n',
            '只有洛连特支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370903V利贝尔的治安维持\n',
            '全看各位的努力\n',
            '也不为过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590370904V劳你跑一趟了，\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D0F(): pass

    label('loc_3D0F')

    Jump('loc_4DD5')

    def _loc_3D12(): pass

    label('loc_3D12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3DC4',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271360V#760F接下来请前往\n',
            '空贼团出现的柏斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271361V我已经联络飞船坪\n',
            '安排了船票的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271362V准备好之后，请立即\n',
            '前往飞船坪接待处办理搭乘手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DD5')

    def _loc_3DC4(): pass

    label('loc_3DC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_4A01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 4, 0x1634)),
            Expr.Return,
        ),
        'loc_3E64',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271363V#760F艾丝蒂尔，\n',
            '找到玲了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271364V#1000F不，还没有。\n',
            '不过，总算快要抓到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271365V（得赶快去空港才行……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49FE')

    def _loc_3E64(): pass

    label('loc_3E64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 3, 0x1633)),
            Expr.Return,
        ),
        'loc_42A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 6, 0x1686)),
            Expr.Return,
        ),
        'loc_3F20',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271366V#760F没人管就会消失的点心……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271367V说不定是说路上的\n',
            '货摊卖的点心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271368V糖果，爆米花，\n',
            '葡萄干，还有冰淇淋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271369V是这些吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42A4')

    def _loc_3F20(): pass

    label('loc_3F20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4182',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271363V#760F艾丝蒂尔，\n',
            '找到玲了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271371V#1000F不，还没有。',
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
        1,
        (
            TXT(0x00, '【商量关于玲的事】\n'),
            TXT(0x01, '【没什么好商量的】\n'),
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
        'loc_40FE',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔向艾南说明了经过。',
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
            '#0590271372V#764F没人管就会消失的点心，对吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271373V#760F说到点心，格兰赛尔的\n',
            '路边摊上很多哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271374V说不定是指货摊卖的\n',
            '货摊卖的点心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271368V糖果，爆米花，\n',
            '葡萄干，还有冰淇淋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271376V#761F是这些吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1686)

    Jump('loc_417C')

    def _loc_40FE(): pass

    label('loc_40FE')

    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590271377V#761F……话说回来\n',
            '真是会藏的孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271378V#760F艾丝蒂尔在离宫\n',
            '很难找到也值得肯定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_417C(): pass

    label('loc_417C')

    OP_A2(0x0003)

    Jump('loc_42A4')

    def _loc_4182(): pass

    label('loc_4182')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 6, 0x1686)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41F9',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271377V#761F……话说回来\n',
            '真是会藏的孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271378V#760F艾丝蒂尔在离宫\n',
            '很难找到也值得肯定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42A4')

    def _loc_41F9(): pass

    label('loc_41F9')

    ChrTalk(
        0x0008,
        (
            '#0590271366V#760F没人管就会消失的点心……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271367V说不定是说路上的\n',
            '货摊卖的点心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271368V糖果，爆米花，\n',
            '葡萄干，还有冰淇淋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271369V是这些吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42A4(): pass

    label('loc_42A4')

    Jump('loc_49FE')

    def _loc_42A7(): pass

    label('loc_42A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 2, 0x1632)),
            Expr.Return,
        ),
        'loc_463A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 5, 0x1685)),
            Expr.Return,
        ),
        'loc_4329',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271385V#760F又辣又苦又美味的店……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271386V这么说来，以前熟人\n',
            '请我吃过辣的东西\n',
            '这我说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4637')

    def _loc_4329(): pass

    label('loc_4329')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4579',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271387V#760F如何，\n',
            '玲在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271388V#1007F这个……',
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
        1,
        (
            TXT(0x00, '【商量关于玲的事】\n'),
            TXT(0x01, '【没什么好商量的】\n'),
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
        'loc_44FE',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔向艾南说明了经过。',
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
            '#0590271389V#764F又辣又苦又美味的店，对吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271390V#760F说起来，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271391V以前熟人\n',
            '请我吃过辣的东西\n',
            '这我说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271392V#1011F啊……奈尔的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271393V#1015F记得是哪里的\n',
            '咖啡店或者是酒馆吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1685)

    Jump('loc_4573')

    def _loc_44FE(): pass

    label('loc_44FE')

    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590271394V#761F能够逃离正游击士的追捕\n',
            '玲也相当有一套呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271395V#760F各位，请加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4573(): pass

    label('loc_4573')

    OP_A2(0x0003)

    Jump('loc_4637')

    def _loc_4579(): pass

    label('loc_4579')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 5, 0x1685)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45C6',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271396V#761F能够逃离正游击士的追捕，\n',
            '玲也相当有一套呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4637')

    def _loc_45C6(): pass

    label('loc_45C6')

    ChrTalk(
        0x0008,
        (
            '#0590271385V#760F又辣又苦又美味的店……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271386V这么说来，以前熟人\n',
            '请我吃过辣的东西\n',
            '这我说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4637(): pass

    label('loc_4637')

    Jump('loc_49FE')

    def _loc_463A(): pass

    label('loc_463A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 1, 0x1631)),
            Expr.Return,
        ),
        'loc_4988',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 4, 0x1684)),
            Expr.Return,
        ),
        'loc_46B0',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271399V#760F和鱼有关系的\n',
            '建筑物我有印象哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271400V就是这个游击士协会\n',
            '隔壁的建筑物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4985')

    def _loc_46B0(): pass

    label('loc_46B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48E9',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271401V#760F哎呀，各位……\n',
            '找到玲了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271388V#1007F这个……',
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
        1,
        (
            TXT(0x00, '【商量关于玲的事】\n'),
            TXT(0x01, '【没什么好商量的】\n'),
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
        'loc_487E',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔向艾南说明了经过。',
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
            '#0590271403V#764F无色的鱼……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271404V#760F无色，这\n',
            '部分不太明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271405V不过和鱼有关的\n',
            '建筑物我有印象哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271406V#1004F真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590271407V#761F嗯嗯，就在这个游击士协会\n',
            '的隔壁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1684)

    Jump('loc_48E3')

    def _loc_487E(): pass

    label('loc_487E')

    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590271408V#762F……看来\n',
            '好象搁浅了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271409V玲到底，\n',
            '去哪里了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48E3(): pass

    label('loc_48E3')

    OP_A2(0x0003)

    Jump('loc_4985')

    def _loc_48E9(): pass

    label('loc_48E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 4, 0x1684)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4920',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271410V#762F玲到底\n',
            '去哪里了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4985')

    def _loc_4920(): pass

    label('loc_4920')

    ChrTalk(
        0x0008,
        (
            '#0590271399V#760F和鱼有关系的\n',
            '建筑物我有印象哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271400V就是这个游击士协会\n',
            '隔壁的建筑物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4985(): pass

    label('loc_4985')

    Jump('loc_49FE')

    def _loc_4988(): pass

    label('loc_4988')

    ChrTalk(
        0x0008,
        (
            '#0590271413V#760F而我就去进行\n',
            '各地支部和情报部的余党\n',
            '的情报交换工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271414V艾丝蒂尔你们\n',
            '请把玲带回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49FE(): pass

    label('loc_49FE')

    Jump('loc_4DD5')

    def _loc_4A01(): pass

    label('loc_4A01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_4A0B',
    )

    Jump('loc_4DD5')

    def _loc_4A0B(): pass

    label('loc_4A0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B96',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271415V#760F哎呀，艾丝蒂尔。\n',
            '探听结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271416V#1015F嗯……\n',
            '在大使馆和城里听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271417V#1000F之后要见见\n',
            '利贝尔通讯的奈尔才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4B2D',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271418V#760F那么，你们那边完成后\n',
            '麻烦赶快来报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271419V雪拉扎德应该\n',
            '也快回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B90')

    def _loc_4B2D(): pass

    label('loc_4B2D')

    ChrTalk(
        0x0008,
        (
            '#0590271418V#760F那么，你们那边完成后\n',
            '麻烦赶快来报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271421V阿加特差不多\n',
            '也快回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B90(): pass

    label('loc_4B90')

    OP_A2(0x0003)

    Jump('loc_4C6A')

    def _loc_4B96(): pass

    label('loc_4B96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4C05',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271422V#760F在利贝尔通讯的探听\n',
            '结束之后请回这里来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271421V阿加特差不多\n',
            '也快回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C6A')

    def _loc_4C05(): pass

    label('loc_4C05')

    ChrTalk(
        0x0008,
        (
            '#0590271422V#760F在利贝尔通讯的探听\n',
            '结束之后请回这里来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271419V雪拉扎德应该\n',
            '也快回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C6A(): pass

    label('loc_4C6A')

    Jump('loc_4DD5')

    def _loc_4C6D(): pass

    label('loc_4C6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_4D46',
    )

    ChrTalk(
        0x0008,
        (
            '#0590250338V#760F按之前说好的，艾丝蒂尔小姐请\n',
            '去帝国、共和国大使馆和格兰赛尔城和\n',
            '利贝尔通讯社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271427V关于各大使馆，就拜托金先生和\n',
            '奥利维尔先生帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271428V关于格兰赛尔城\n',
            '就拜托殿下您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DD5')

    def _loc_4D46(): pass

    label('loc_4D46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_4D50',
    )

    Jump('loc_4DD5')

    def _loc_4D50(): pass

    label('loc_4D50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_4DD5',
    )

    ChrTalk(
        0x0008,
        (
            '#0590271429V#760F在艾尔贝离宫工作的\n',
            '管家雷蒙德先生，\n',
            '负责看管迷路的孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271430V如果到了艾尔贝离宫\n',
            '请先问问他看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DD5(): pass

    label('loc_4DD5')

    TalkEnd(0x0008)

    Return()

# id: 0x000E offset: 0x4DD9
@scena.Code('func_0E_4DD9')
def func_0E_4DD9():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '突、突然就有穿着\n',
            '红色铠甲的家伙袭击过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说早习惯了麻烦，\n',
            '这次真是吓坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x4E38
@scena.Code('func_0F_4E38')
def func_0F_4E38():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哆哆嗦嗦……\n',
            '颤抖不停……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些人，真打算把我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x4E7C
@scena.Code('func_10_4E7C')
def func_10_4E7C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '他、他们是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样子奇怪的４个人\n',
            '好像是他们的首领……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x4EC8
@scena.Code('func_11_4EC8')
def func_11_4EC8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '不止导力器不能使用\n',
            '还碰上这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太过分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x4F0C
@scena.Code('func_12_4F0C')
def func_12_4F0C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '那些家伙是帝国军吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '破坏好不容易定下的条约，\n',
            '会做这种事的除了帝国还有谁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x4F68
@scena.Code('func_13_4F68')
def func_13_4F68():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 7, 0x164F)),
            Expr.Return,
        ),
        'loc_4FDB',
    )

    ChrTalk(
        0x00FE,
        (
            '袭、袭击我们的人中\n',
            '有个白衣服的女人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '士兵一转眼\n',
            '就被她干掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是、是不是看错了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_501F')

    def _loc_4FDB(): pass

    label('loc_4FDB')

    ChrTalk(
        0x00FE,
        (
            '痛痛痛……\n',
            '逃跑的时候跌倒受伤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸和妈妈\n',
            '不要紧吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_501F(): pass

    label('loc_501F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x5023
@scena.Code('func_14_5023')
def func_14_5023():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '王国军的人\n',
            '带我来这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些人不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x505F
@scena.Code('func_15_505F')
def func_15_505F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '为，为什么那些人\n',
            '要袭击我们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们完全没做坏事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x50A5
@scena.Code('func_16_50A5')
def func_16_50A5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '混帐！\n',
            '我的店到底怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x50CF
@scena.Code('func_17_50CF')
def func_17_50CF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '把打算留在店里的塞森\n',
            '硬拖走去避难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '千钧一发，真是危险啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x511D
@scena.Code('func_18_511D')
def func_18_511D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '王国军的士兵们\n',
            '竟会被仅仅４人……难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x5157
@scena.Code('func_19_5157')
def func_19_5157():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊啊，怎么回事……\n',
            '王都……在燃烧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x5189
@scena.Code('func_1A_5189')
def func_1A_5189():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '士兵们叫我\n',
            '去避难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个士兵没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x51C1
@scena.Code('func_1B_51C1')
def func_1B_51C1():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '怎、怎么回事……\n',
            '那些家伙到底是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x51F7
@scena.Code('func_1C_51F7')
def func_1C_51F7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '在柏斯的罗伊德\n',
            '不要紧吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x521F
@scena.Code('func_1D_521F')
def func_1D_521F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '婆婆，没事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x523A
@scena.Code('func_1E_523A')
def func_1E_523A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没事的，女神大人\n',
            '或者女王陛下会想办法的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '努力忍耐吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x5286
@scena.Code('func_1F_5286')
def func_1F_5286():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '帮、帮帮忙！\n',
            '王都，王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x52AE
@scena.Code('func_20_52AE')
def func_20_52AE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '率领红色士兵\n',
            '的４人向王城那边去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下和科洛蒂娅公主\n',
            '不知道要不要紧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x530F
@scena.Code('func_21_530F')
def func_21_530F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊哇哇……\n',
            '怎么会变成这样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x5337
@scena.Code('func_22_5337')
def func_22_5337():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这……\n',
            '难道是战争？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚刚才缔结了互不侵犯条约……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x5379
@scena.Code('func_23_5379')
def func_23_5379():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哪怕建筑物被烧毁，\n',
            '钓公师团也不会灭亡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要我们的心中\n',
            '还燃烧着对钓鱼的热情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x53D8
@scena.Code('func_24_53D8')
def func_24_53D8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54E7',
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
        100,
        0,
        (
            TXT(0x00, '【◇集齐了全部『牌技师杰克』】\n'),
            TXT(0x01, '【◇没集齐全部『牌技师杰克』】\n'),
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
        (0x00000000, 'loc_5455'),
        (0x00000001, 'loc_549E'),
        (-1, 'loc_54E7'),
    )

    def _loc_5455(): pass

    label('loc_5455')

    AddItem(ItemTable['牌技师杰克 １卷'], 1)
    AddItem(ItemTable['牌技师杰克 ２卷'], 1)
    AddItem(ItemTable['牌技师杰克 ３卷'], 1)
    AddItem(ItemTable['牌技师杰克 ４卷'], 1)
    AddItem(ItemTable['牌技师杰克 ５卷'], 1)
    AddItem(ItemTable['牌技师杰克 ６卷'], 1)
    AddItem(ItemTable['牌技师杰克 ７卷'], 1)
    AddItem(ItemTable['牌技师杰克 ８卷'], 1)
    AddItem(ItemTable['牌技师杰克 ９卷'], 1)
    AddItem(ItemTable['牌技师杰克 10卷'], 1)
    AddItem(ItemTable['牌技师杰克 11卷'], 1)
    AddItem(ItemTable['牌技师杰克 12卷'], 1)
    AddItem(ItemTable['牌技师杰克 13卷'], 1)
    AddItem(ItemTable['牌技师杰克 14卷'], 1)

    Jump('loc_54E7')

    def _loc_549E(): pass

    label('loc_549E')

    RemoveItem(ItemTable['牌技师杰克 １卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ２卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ３卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ４卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ５卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ６卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ７卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ８卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ９卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 10卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 11卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 12卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 13卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 14卷'], 1)

    Jump('loc_54E7')

    def _loc_54E7(): pass

    label('loc_54E7')

    If(
        (
            (Expr.Eval, "OP_40(0x023A, 0x00)"),
            (Expr.Eval, "OP_40(0x023B, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023C, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023D, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023E, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x023F, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0240, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0241, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0242, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0243, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0244, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0245, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0246, 0x00)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0247, 0x00)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5561',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0218, 4, 0x10C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5561',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0218, 3, 0x10C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5559',
    )

    OP_A2(0x10C3)
    Call(1, 0x0026)
    TalkEnd(0x002A)

    Return()

    def _loc_5559(): pass

    label('loc_5559')

    Call(1, 0x0027)
    TalkEnd(0x002A)

    Return()

    def _loc_5561(): pass

    label('loc_5561')

    ChrTalk(
        0x00FE,
        (
            '出来采购的时候，\n',
            '突然说要我避难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候不要慌乱，\n',
            '读读书镇定下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x55B9
@scena.Code('func_25_55B9')
def func_25_55B9():
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
        'loc_55DE',
    )

    Call(0, 0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_55DA',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_55DE')

    def _loc_55DA(): pass

    label('loc_55DA')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_55DE(): pass

    label('loc_55DE')

    OP_6D(-5500, 0, 20, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -2600, 0, 560, 270)
    SetChrPos(0x000C, -1280, 0, 980, 270)
    SetChrPos(0x000A, -2600, 0, 1590, 270)
    SetChrPos(0x0009, -2600, 0, -590, 270)
    SetChrPos(0x000E, -1680, 0, 2260, 270)
    SetChrPos(0x000B, -360, 0, 1500, 270)
    SetChrPos(0x000D, -1240, 0, -60, 270)
    SetChrPos(0x0010, -1480, 0, -1090, 270)
    SetChrPos(0x0008, -5700, 0, -130, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x0109, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x0008, 255)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0590270851V#764F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590270852V#760F嗯嗯……知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590270853V那么拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x01, 0x00)
    Sleep(300)

    OP_8C(0x0008, 45, 400)

    @scena.Lambda('lambda_57CB')
    def lambda_57CB():
        OP_6D(-3320, 0, 1160, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_57CB)

    OP_8E(0x0008, -4480, 0, 960, 1500, 0x00)
    OP_8C(0x0008, 90, 400)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010270854V#1026F怎么了，艾南先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590270855V#760F嗯嗯，凯诺娜原上尉\n',
            '好像接受审问了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590270856V知道了详细情况\n',
            '也告诉协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270857V#1025F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_590F',
    )

    ChrTalk(
        0x0009,
        (
            '#0030270858V#027F#6P那个强硬的女人\n',
            '居然打算招了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270859V用了怎样的手段呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5969')

    def _loc_590F(): pass

    label('loc_590F')

    ChrTalk(
        0x000A,
        (
            '#0050270860V#051F咦，那个强硬的\n',
            '母狐狸居然会开口……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270861V使了怎样的手段啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5969(): pass

    label('loc_5969')

    ChrTalk(
        0x000E,
        (
            '#0080270862V#074F#2P嗯，那边的调查\n',
            '就交给王国军吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080270863V#072F我们就做好自己的事情，\n',
            '继续整理情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590270864V#764F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590270865V#760F那么，先交给你们\n',
            '这次工作的报酬吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590270866V其他的小委托也就都\n',
            '一并核定了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008D, 0x04, 0x20)
    OP_28(0x0089, 0x04, 0x10)
    OP_AF(0xCD, 0x0089)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 4, 0x1684)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A7E',
    )

    OP_2B(0x008C, 0x0001)

    def _loc_5A7E(): pass

    label('loc_5A7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 5, 0x1685)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A8B',
    )

    OP_2B(0x008C, 0x0001)

    def _loc_5A8B(): pass

    label('loc_5A8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 6, 0x1686)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A98',
    )

    OP_2B(0x008C, 0x0001)

    def _loc_5A98(): pass

    label('loc_5A98')

    OP_28(0x008C, 0x04, 0x10)
    OP_AF(0xCD, 0x008C)
    Sleep(100)

    OP_28(0x008E, 0x04, 0x10)
    OP_AF(0xCD, 0x008E)
    Sleep(100)

    OP_28(0x008A, 0x04, 0x10)
    OP_28(0x008A, 0x04, 0x20)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x000C,
        (
            '#0060270867V#043F那个，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060270868V玲真的是『结社』的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221183V#1003F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    @scena.Lambda('lambda_5B45')
    def lambda_5B45():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5B45)

    @scena.Lambda('lambda_5B53')
    def lambda_5B53():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5B53)

    @scena.Lambda('lambda_5B61')
    def lambda_5B61():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5B61)

    @scena.Lambda('lambda_5B6F')
    def lambda_5B6F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_5B6F)

    @scena.Lambda('lambda_5B7D')
    def lambda_5B7D():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5B7D)

    @scena.Lambda('lambda_5B8B')
    def lambda_5B8B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5B8B)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270870V#1025F#5P『执行者』之一\n',
            '名为『歼灭天使』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270871V本人这么说就没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060270872V#049F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070270873V#063F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270874V#1317F#6P但，但是那样的女孩\n',
            '竟然是『结社』的精锐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120270875V而且『执行者』\n',
            '不是很厉害的人吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120270876V会不会是弄错了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270877V#1003F#5P不，我想大概是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270878V约修亚也是在和她同龄的时候\n',
            '就已经成为『执行者』了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270879V#813F#6P………啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5E60',
    )

    ChrTalk(
        0x0009,
        (
            '#0030270880V#522F#6P不过真是\n',
            '彻底被耍了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270881V将『福音』交给凯诺娜,\n',
            '挑唆使用战车卷土重来的\n',
            '好像也是那个孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050270882V#555F向各方发出恐吓信的\n',
            '似乎也是那个小鬼啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270883V到底是为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F40')

    def _loc_5E60(): pass

    label('loc_5E60')

    ChrTalk(
        0x000A,
        (
            '#0050270884V#552F不过真是\n',
            '彻底被耍了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270885V把『福音』交给那母狐狸,\n',
            '挑唆使用战车卷土重来的\n',
            '好像也是那小鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030270886V#022F#6P向各方发出恐吓信的\n',
            '似乎也是那个孩子呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270887V到底是什么打算呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F40(): pass

    label('loc_5F40')

    ChrTalk(
        0x0101,
        (
            '#0010270888V#1015F#5P虽然是我的直觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270889V但会不会是这样做\n',
            '比较有趣呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_60C1',
    )

    ChrTalk(
        0x000A,
        (
            '#0050270890V#052F什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270891V#1003F#5P玲认为这次的实验\n',
            '是『茶会』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270892V于是，为了让包括我们在内\n',
            '众多的人都来参加\n',
            '而做了很多准备邀请……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270893V我感觉是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050270894V#055F……真的吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270895V因为恐吓信的事来到王都\n',
            '这的确没错，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61E0')

    def _loc_60C1(): pass

    label('loc_60C1')

    ChrTalk(
        0x0009,
        (
            '#0030270896V#023F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270891V#1003F#5P玲认为这次的实验\n',
            '是『茶会』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270892V于是，为了让包括我们在内\n',
            '众多的人都来参加\n',
            '而做了很多准备邀请……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270893V我感觉是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030270900V#522F#6P……受不了了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270901V我们的确是因为恐吓信的事\n',
            '来到王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_61E0(): pass

    label('loc_61E0')

    ChrTalk(
        0x000B,
        (
            '#0040270902V#035F唔，那只小猫咪\n',
            '确实可能这么做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040270903V#030F看来让我们睡着的\n',
            '安眠药的量也有控制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_62AF',
    )

    ChrTalk(
        0x000A,
        (
            '#0050270904V#057F让我们刚好\n',
            '能在那个时机\n',
            '到达码头啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270905V真是胡闹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6307')

    def _loc_62AF(): pass

    label('loc_62AF')

    ChrTalk(
        0x0009,
        (
            '#0030270906V#022F#6P让我们刚好\n',
            '能在那个时机\n',
            '可以到达吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270907V真行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6307(): pass

    label('loc_6307')

    ChrTalk(
        0x0101,
        (
            '#0010270908V#1015F#5P唔，就是说都是\n',
            '那孩子让大家睡着的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060270909V#043F嗯嗯……恐怕是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060270910V吃了玲在百货店买的\n',
            '曲奇之后马上就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080270911V#074F#2P但是……\n',
            '真是严重的失策啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080270912V要是她用的是毒，\n',
            '搞不好大家就都会死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200268V#1026F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590270914V#765F这是我的失策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590270915V作为大家的后援\n',
            '应该更加当心才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590270916V真是对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270917V#1025F#5P哪、哪里的话嘛，艾南先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270918V#1007F我想这次\n',
            '是我们全体人员的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270919V没想到『结社』竟是\n',
            '那样的亡命之徒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070270920V#561F#6P那个巨大人形兵器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070270921V那种东西，恐怕连\n',
            '爷爷也很难制造出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070270922V#062F即使能造出来……\n',
            '竟能那样移动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070270923V而且……那个玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070270924V#562F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270925V#1026F#5P提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270926V#1018F#5P真是的，打起精神来啦！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270927V下次碰到她，绝对\n',
            '要让她脱离『结社』！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070270928V#064F#6P呜哎…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6710',
    )

    ChrTalk(
        0x000A,
        (
            '#0050270929V#055F慢、慢着！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_673A')

    def _loc_6710(): pass

    label('loc_6710')

    ChrTalk(
        0x0009,
        (
            '#0030270930V#023F#6P艾丝蒂尔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_673A(): pass

    label('loc_673A')

    ChrTalk(
        0x0101,
        (
            '#0010270931V#1006F#5P５年前、老爸就让约修亚\n',
            '脱离『结社』了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270932V所以，身为他女儿的我\n',
            '不可能做不到同样的事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270933V哪怕揪着她的头发\n',
            '也要把她拖出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070270934V#560F#6P姐、姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070270935V#067F嗯，是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060270936V#048F呵呵……\n',
            '到底是艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270937V#811F#6P嗯嗯，就是这股劲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040270938V#031F呼，这股冲劲\n',
            '真令人高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050270939V#556F真是的……\n',
            '别说得那么轻松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030270940V#021F#6P呵呵，有什么不好。\n',
            '这才是艾丝蒂尔嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080270941V#070F#2P这股冲劲\n',
            '说不定更胜过老师呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0109, -20, -500, -7250, 0)
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    NpcTalk(
        0x0109,
        '青年的声音',
        (
            '#0180270942V#2P嗯～真棒啊。\n',
            '我好像越来越被她吸引了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_69DF')
    def lambda_69DF():
        OP_6D(-1820, 0, -1810, 2000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_69DF)

    @scena.Lambda('lambda_69F7')
    def lambda_69F7():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_69F7)

    @scena.Lambda('lambda_6A05')
    def lambda_6A05():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_6A05)

    @scena.Lambda('lambda_6A13')
    def lambda_6A13():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6A13)

    @scena.Lambda('lambda_6A21')
    def lambda_6A21():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6A21)

    @scena.Lambda('lambda_6A2F')
    def lambda_6A2F():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6A2F)

    @scena.Lambda('lambda_6A3D')
    def lambda_6A3D():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6A3D)

    @scena.Lambda('lambda_6A4B')
    def lambda_6A4B():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6A4B)

    @scena.Lambda('lambda_6A59')
    def lambda_6A59():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6A59)

    @scena.Lambda('lambda_6A67')
    def lambda_6A67():
        ChrTurnDirection(0x00FE, 0x0109, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6A67)

    @scena.Lambda('lambda_6A75')
    def lambda_6A75():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6A75')

    DispatchAsync2(0x0101, 0x0001, lambda_6A75)

    @scena.Lambda('lambda_6A86')
    def lambda_6A86():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6A86')

    DispatchAsync2(0x000A, 0x0001, lambda_6A86)

    @scena.Lambda('lambda_6A97')
    def lambda_6A97():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6A97')

    DispatchAsync2(0x0009, 0x0001, lambda_6A97)

    @scena.Lambda('lambda_6AA8')
    def lambda_6AA8():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6AA8')

    DispatchAsync2(0x000C, 0x0001, lambda_6AA8)

    @scena.Lambda('lambda_6AB9')
    def lambda_6AB9():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6AB9')

    DispatchAsync2(0x000D, 0x0001, lambda_6AB9)

    @scena.Lambda('lambda_6ACA')
    def lambda_6ACA():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6ACA')

    DispatchAsync2(0x000E, 0x0001, lambda_6ACA)

    @scena.Lambda('lambda_6ADB')
    def lambda_6ADB():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6ADB')

    DispatchAsync2(0x0008, 0x0001, lambda_6ADB)

    @scena.Lambda('lambda_6AEC')
    def lambda_6AEC():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_6AEC')

    DispatchAsync2(0x0010, 0x0001, lambda_6AEC)

    ClearChrFlags(0x0109, 0x0080)
    Sleep(1000)

    OP_9F(0x0109, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_6B12')
    def lambda_6B12():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_6B12)

    @scena.Lambda('lambda_6B24')
    def lambda_6B24():
        OP_8E(0x00FE, -20, -250, -5800, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_6B24)

    WaitForThreadExit(0x0109, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270943V#1004F#4P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590270944V#761F#6P凯文神父。\n',
            '正等着你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6B98')
    def lambda_6B98():
        OP_6D(-2800, 0, 240, 2000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_6B98)

    @scena.Lambda('lambda_6BB0')
    def lambda_6BB0():
        OP_8E(0x00FE, -1870, 0, -2230, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_6BB0)

    WaitForThreadExit(0x0109, 0x0001)
    ChrTurnDirection(0x0109, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180270945V#1068F#6P呀～抱歉迟到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270946V之前被卡兰大主教\n',
            '严厉说教了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270947V所以才迟到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_62(0x0109, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180270948V#1064F#6P怎么了？\n',
            '我脸上有什么东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010270949V#1019F我说～事到如今\n',
            '才问这个问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270950V凯文先生到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6D74',
    )

    ChrTalk(
        0x0009,
        (
            '#0030270951V#026F#5P嗯嗯，说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270952V#027F到头来我们，\n',
            '也总是被转移话题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6DC8')

    def _loc_6D74(): pass

    label('loc_6D74')

    ChrTalk(
        0x000A,
        (
            '#0050270953V#051F咦，说得对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270954V到头来我们，\n',
            '也总是被转移话题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6DC8(): pass

    label('loc_6DC8')

    ChrTalk(
        0x0010,
        (
            '#0120270955V#816F#5P当然不是普通的\n',
            '神父吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270956V#1065F#6P是吗……\n',
            '那我重新自我介绍一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270957V#1060F──我是七耀教会星杯骑士团\n',
            '所属的凯文·格拉汉姆神父。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270958V以后，请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270959V#1002F星杯骑士团……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040270960V#033F#2P哟，这可诚惶诚恐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040270961V#030F没想到你这么年轻\n',
            '居然是『星杯骑士』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270962V#1004F#5P奥利维尔，你知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040270963V#035F#2P古代遗物被\n',
            '教会管理的事，\n',
            '你应该听说过吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040270964V担任其调查·回收任务的\n',
            '就是被称为星杯骑士团的组织。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040270965V#030F成员似乎都是非公开\n',
            '挑选的相当精干之人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270966V#1064F#6P咦，很清楚嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270967V#1066F很遗憾，我在骑士团\n',
            '还是一介新人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270968V说精干实在是过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270969V#1015F古代遗物的回收……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270970V#1004F那么，那时用的\n',
            '戴尔蒙市长之杖……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270971V#1060F#6P啊啊，那个是王国军\n',
            '正式交给我的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270972V教会和利贝尔之间\n',
            '缔结了古代遗物\n',
            '回收的盟约的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270973V#1068F由于我私自破坏\n',
            '而被大主教说教……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270974V#1025F是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270975V但是那个情况下，除了那样做\n',
            '我想也没有别的办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7260',
    )

    ChrTalk(
        0x0009,
        (
            '#0030270976V#020F#5P嗯嗯，那可不是\n',
            '该选择手段的时机啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_7260(): pass

    label('loc_7260')

    ChrTalk(
        0x000A,
        (
            '#0050270977V#051F啊啊，也不是\n',
            '该选择手段的时机啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7298(): pass

    label('loc_7298')

    ChrTalk(
        0x0109,
        (
            '#0180270978V#1066F#6P嘿嘿。\n',
            '这样说我真是轻松多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270979V#1060F嗯，就是这样。\n',
            '今后也请多关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270980V关于『噬身之蛇』，\n',
            '要是知道了什么就交换情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231253V#1004F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270982V#1065F#6P我来利贝尔\n',
            '是为了调查『结社』嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270983V#1063F正确的说……\n',
            '是调查他们想得到的\n',
            '『辉之环』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270984V#1020F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030270985V#023F#5P『辉之环』……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060270986V#047F#2P女神授予古代人的\n',
            '『七至宝』之一……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060270987V#042F被认为封印在\n',
            '格兰赛尔城地下的\n',
            '传说之古代遗物对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270988V#1063F#6P嗯嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270989V#1065F最近，在大陆各地\n',
            '似乎出现了收集有关\n',
            '『七至宝』相关情报的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270990V即使是教会，对其动向\n',
            '也相当在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270991V#1060F利贝尔也在此时\n',
            '发来了『辉之环』的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270992V因此，为了确认真伪，\n',
            '就派遣了我这个新人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060270993V#542F#2P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270994V#1002F那么『辉之环』\n',
            '真的在利贝尔吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270995V因为不在封印区域里\n',
            '我以为仅仅是传说而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_769E',
    )

    ChrTalk(
        0x000A,
        (
            '#0050270996V#555F说到底，并不知道\n',
            '是怎样的东西对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_76DD')

    def _loc_769E(): pass

    label('loc_769E')

    ChrTalk(
        0x0009,
        (
            '#0030270997V#022F#5P说到底，并不知道\n',
            '是怎样的东西不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_76DD(): pass

    label('loc_76DD')

    ChrTalk(
        0x0109,
        (
            '#0180270998V#1065F#6P嗯，关于此事真伪的\n',
            '调查也是我的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270999V#1060F今天来，是想说明\n',
            '我的情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180271000V就是说，有什么事\n',
            '再互相帮助吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271001V#1015F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271002V#1006F嗯，我们也这么想呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080271003V#070F是啊。\n',
            '也帮了我们大忙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_783A',
    )

    ChrTalk(
        0x0009,
        (
            '#0030271004V#027F#5P这也是种缘分，\n',
            '有困难再联络了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_786C')

    def _loc_783A(): pass

    label('loc_783A')

    ChrTalk(
        0x000A,
        (
            '#0050271005V#051F没办法……\n',
            '有困难再联络啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_786C(): pass

    label('loc_786C')

    ChrTalk(
        0x0109,
        (
            '#0180271006V#1062F#6P非常感谢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180271007V#1061F那么，今天\n',
            '我就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180271008V回见～各位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_B7(0x08)
    OP_8C(0x0109, 135, 400)

    @scena.Lambda('lambda_78E5')
    def lambda_78E5():
        OP_6D(-1820, 0, -1810, 2000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_78E5)

    OP_8E(0x0109, -110, -250, -6230, 2000, 0x00)

    @scena.Lambda('lambda_7911')
    def lambda_7911():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_7911)

    @scena.Lambda('lambda_7923')
    def lambda_7923():
        OP_8E(0x00FE, -10, -500, -7250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_7923)

    WaitForThreadExit(0x0109, 0x0001)
    Sleep(500)

    OP_22(0x0007, 0x00, 0x64)
    Sleep(500)

    SetChrFlags(0x0109, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0008, 0x01)

    @scena.Lambda('lambda_7977')
    def lambda_7977():
        OP_6D(-3320, 0, 1160, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_7977)

    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010271009V#1007F#5P走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030271010V#027F#5P真是个和奥利维尔不同风格\n',
            '却同样让人脱力的神父啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040271011V#035F#2P呼，要我说来\n',
            '修行还差的远呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040271012V再稍微优雅一点就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271013V#1019F#5P你那些无聊话\n',
            '哪里优雅了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060271014V#049F#2P不过『辉之环』啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060271015V#043F和结社在各地\n',
            '用『福音』做实验\n',
            '有什么关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 90, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0590271016V#764F嗯……\n',
            '不能否定这个可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7B3E')
    def lambda_7B3E():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_7B3E)

    @scena.Lambda('lambda_7B4C')
    def lambda_7B4C():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_7B4C)

    Sleep(50)

    @scena.Lambda('lambda_7B5F')
    def lambda_7B5F():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_7B5F)

    @scena.Lambda('lambda_7B6D')
    def lambda_7B6D():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_7B6D)

    Sleep(50)

    @scena.Lambda('lambda_7B80')
    def lambda_7B80():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7B80)

    @scena.Lambda('lambda_7B8E')
    def lambda_7B8E():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_7B8E)

    Sleep(50)

    @scena.Lambda('lambda_7BA1')
    def lambda_7BA1():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7BA1)

    @scena.Lambda('lambda_7BAF')
    def lambda_7BAF():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7BAF)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0590271017V#762F顺带一提，这次事件中\n',
            '他们在３个地方\n',
            '进行了『福音』的实验。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271018V照这样看来，其他地方\n',
            '可能也进行了实验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271019V#1002F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271020V王都的骚动也解决了\n',
            '是不是该转移了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7CE5',
    )

    ChrTalk(
        0x000A,
        (
            '#0050271021V#053F这么说，就是洛连特地区\n',
            '或者柏斯地区了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D2A')

    def _loc_7CE5(): pass

    label('loc_7CE5')

    ChrTalk(
        0x0009,
        (
            '#0030271022V#020F#6P这么说，就是洛连特地区\n',
            '或者柏斯地区了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D2A(): pass

    label('loc_7D2A')

    Sleep(100)

    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00C3, 0x01, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0008, 270, 400)

    @scena.Lambda('lambda_7DAB')
    def lambda_7DAB():
        OP_6D(-5500, 0, 20, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_7DAB)

    OP_8F(0x0008, -5700, 0, -130, 2000, 0x00)
    Sleep(400)

    WaitForThreadExit(0x0008, 0x0002)
    OP_23(0x00C3)
    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x00, 0x00)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0590271023V#760F#6P是，这里是游击士协会，\n',
            '格兰赛尔支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271024V………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271025V#763F什么……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271026V#764F……明白了。\n',
            '我们也会注意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271027V嗯嗯，那么再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x01, 0x00)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0030271028V#020F#6P艾南先生，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050271029V#051F#2P那母狐狸的\n',
            '审讯结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 45, 400)

    @scena.Lambda('lambda_7F84')
    def lambda_7F84():
        OP_6D(-3320, 0, 1160, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_7F84)

    OP_8E(0x0008, -4480, 0, 960, 2000, 0x00)
    OP_8C(0x0008, 90, 400)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0590271030V#762F不，是其他的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271031V看来昨夜，柏斯地方\n',
            '出现了空贼团的余党。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(30)

    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(30)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010271032V#1005F#3S咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080271033V#072F情报部加上空贼团……\n',
            '真是忙得一塌糊涂的夜晚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271034V那，到底是在哪里出现的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590271035V#762F似乎是以前他们作为大本营的\n',
            '『迷雾峡谷』里的要塞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271036V现在，本是作为军队的\n',
            '飞行训练场来用的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271037V他们抢了保管在那里的\n',
            '空贼艇逃走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030271038V#023F#6P你说什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040271039V#033F哦哦，穆拉\n',
            '收领的那个吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271040V#1020F等、等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271041V不觉得这\n',
            '时机好得太过头了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271042V搞不好这个\n',
            '也和『结社』有关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590271043V#764F不否定这个可能性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271044V#762F由于这个，接下来\n',
            '请各位去柏斯地区\n',
            '可能比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271045V#1002F确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8980',
    )

    ChrTurnDirection(0x0009, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0030271046V#020F#6P不是挺好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271047V现在本来就不清楚\n',
            '洛连特和柏斯\n',
            '到底哪边会发生事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251416V#1015F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010271049V#1004F#5P那，雪拉姐\n',
            '也要一起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8470')
    def lambda_8470():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_8470)

    @scena.Lambda('lambda_847E')
    def lambda_847E():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_847E)

    Sleep(10)

    @scena.Lambda('lambda_8491')
    def lambda_8491():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_8491)

    @scena.Lambda('lambda_849F')
    def lambda_849F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_849F)

    Sleep(30)

    @scena.Lambda('lambda_84B2')
    def lambda_84B2():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_84B2)

    @scena.Lambda('lambda_84C0')
    def lambda_84C0():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_84C0)

    ChrTalk(
        0x0009,
        (
            '#0030271050V#027F#6P情报部的余党收拾后，\n',
            '我们的工作也告一段落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271051V敌人似乎相当不好对付，\n',
            '我也打算出一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271052V#1018F#5P太好啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050271053V#051F呵，『银闪』的手腕，\n',
            '可要好好见识一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040271054V#037F呵呵呵，雪拉\n',
            '也终于来到我身边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060271055V#048F雪拉扎德小姐。\n',
            '就请多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030271056V#021F#6P嗯嗯，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010271057V#1004F#5P啊，难道……\n',
            '亚妮拉丝也一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0120271058V#819F#6P嘿嘿……\n',
            '我就不好意思了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120271059V#816F克鲁茨他们也快\n',
            '结束强化训练回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120271060V我打算加入\n',
            '那边的队伍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271061V#1025F#5P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0010, 400)

    ChrTalk(
        0x000E,
        (
            '#0080271062V#070F#2P说是队伍的话\n',
            '果然还是对付『结社』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000E, 400)

    ChrTalk(
        0x0010,
        (
            '#0120271063V#816F#6P是的，打算去搜索\n',
            '『结社』的据点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271064V#1004F#5P据点的搜索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590271065V#764F根据目前的行动来看，\n',
            '『结社』在国内构筑了\n',
            '什么据点的可能性似乎很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271066V#762F不破坏那里，\n',
            '就无法从根本上解决问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271067V今后，有必要与王国军\n',
            '全面合作进行搜索活动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070271068V#062F的确，那个巨大人形兵器\n',
            '绝对需要维护……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271069V在什么地方一定有\n',
            '规范的设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050271070V#051F哦，对付结社的队伍\n',
            '再多一个当然也是必要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F70')

    def _loc_8980(): pass

    label('loc_8980')

    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050271071V#051F不是很好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271072V现在这时候\n',
            '洛连特和柏斯，\n',
            '也不清楚是否会有事件发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251416V#1015F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010271074V#1004F那，阿加特\n',
            '也要一起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8A67')
    def lambda_8A67():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_8A67)

    Sleep(10)

    @scena.Lambda('lambda_8A7A')
    def lambda_8A7A():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_8A7A)

    @scena.Lambda('lambda_8A88')
    def lambda_8A88():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_8A88)

    Sleep(30)

    @scena.Lambda('lambda_8A9B')
    def lambda_8A9B():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_8A9B)

    @scena.Lambda('lambda_8AA9')
    def lambda_8AA9():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_8AA9)

    ChrTalk(
        0x000A,
        (
            '#0050271075V#051F情报部的余党收拾之后，\n',
            '我们的工作也告一段落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271076V敌人似乎相当不好对付，\n',
            '我也打算出一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271077V#1018F真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070271078V#061F#6P哇、阿加特哥哥\n',
            '也一起来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030271079V#027F#6P『重剑』的威力，\n',
            '可要做个示范哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080271080V#070F嗯，就承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000D, 400)

    ChrTalk(
        0x000A,
        (
            '#0050271081V#051F#5P啊啊，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010271057V#1004F#5P啊，难道……\n',
            '亚妮拉丝也一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0120271058V#819F#6P嘿嘿……\n',
            '我就不好意思了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120271059V#816F克鲁茨他们也快\n',
            '结束强化训练回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120271060V我打算加入\n',
            '那边的队伍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271061V#1025F#5P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0010, 400)

    ChrTalk(
        0x000E,
        (
            '#0080271062V#070F#2P说是队伍的话\n',
            '果然还是对付『结社』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000E, 400)

    ChrTalk(
        0x0010,
        (
            '#0120271063V#816F#6P是的，打算去搜索\n',
            '『结社』的据点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271064V#1004F#5P据点的搜索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590271065V#764F根据目前的行动来看，\n',
            '『结社』在国内构筑了\n',
            '什么据点的可能性似乎很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271066V#762F不破坏那里，\n',
            '就无法从根本上解决问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590271067V今后，有必要与王国军\n',
            '全面合作进行搜索活动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060271093V#040F看来这次事件中，\n',
            '王国军对『结社』的应对\n',
            '似乎也大幅度强化了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060271094V或许需要\n',
            '更紧密的合作体制呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030271095V#027F#6P唔，对付结社的队伍\n',
            '再多一个当然也是必要的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F70(): pass

    label('loc_8F70')

    ChrTalk(
        0x0101,
        (
            '#0010271096V#1015F#5P嗯～这么说\n',
            '克鲁茨的队伍\n',
            '似乎也需要战力了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271097V#1016F亚妮拉丝\n',
            '被抢走也没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0120271098V#819F#6P嘿嘿，抱歉哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120271099V#816F『结社』的据点找到之后，\n',
            '应该也会需要借助\n',
            '艾丝蒂尔你们的力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120271100V到时候一起作战吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271101V#1017F#5P嗯……好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x08, 0xFF)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/C5601._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0026 offset: 0x90C8
@scena.Code('func_26_90C8')
def func_26_90C8():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 124010, 0, -3770, 90)
    SetChrPos(0x0102, 124010, 0, -2950, 90)
    SetChrPos(0x00F8, 122910, 0, -3770, 90)
    SetChrPos(0x00F9, 122910, 0, -2950, 90)
    OP_8C(0x00FE, 270, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010370920V#1004F啊，咖啡店的老板？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2380370921V呀，本来出来采购，\n',
            '突然叫我去避难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2380370922V这种时候正应该\n',
            '读本书镇定一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370923V#1015F（嗯～不过你现在\n',
            '　就已经足够镇定了嘛……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370924V哟……这本书是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370925V应该是流行于街头巷尾的\n',
            '传说中的《牌技师杰克》吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370926V#1004F啊，你是说这本小说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370927V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370928V以共和国为舞台、\n',
            '背负了不幸命运的\n',
            '牌技师们的故事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370929V哎呀呀，我老早\n',
            '就想读这本书了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370930V#1011F是，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370931V#1015F（唔～我也受了不少\n',
            '　老板的关照……)',
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
            TXT(0x00, '【给店主小说】\n'),
            TXT(0x01, '【不给】\n'),
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
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93D8',
    )

    Call(1, 0x0028)

    Jump('loc_9400')

    def _loc_93D8(): pass

    label('loc_93D8')

    ChrTalk(
        0x0101,
        (
            '#0010370932V#1016F（还是算了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9400(): pass

    label('loc_9400')

    EventEnd(0x00)

    Return()

# id: 0x0027 offset: 0x9403
@scena.Code('func_27_9403')
def func_27_9403():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 124010, 0, -3770, 90)
    SetChrPos(0x0102, 124010, 0, -2950, 90)
    SetChrPos(0x00F8, 122910, 0, -3770, 90)
    SetChrPos(0x00F9, 122910, 0, -2950, 90)
    OP_8C(0x00FE, 270, 0)
    OP_0D()

    ChrTalk(
        0x002A,
        (
            '#2380370987V咦，你这是？',
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
            TXT(0x00, '【给店主小说】\n'),
            TXT(0x01, '【不给】\n'),
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
            Expr.Equ,
            Expr.Return,
        ),
        'loc_94D6',
    )

    Call(1, 0x0028)

    Jump('loc_94FE')

    def _loc_94D6(): pass

    label('loc_94D6')

    ChrTalk(
        0x0101,
        (
            '#0010370990V#1015F（还是算了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_94FE(): pass

    label('loc_94FE')

    EventEnd(0x00)

    Return()

# id: 0x0028 offset: 0x9501
@scena.Code('func_28_9501')
def func_28_9501():
    ChrTalk(
        0x0101,
        (
            '#0010370941V#1001F喏，给你。\n',
            '就送给老板吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370942V啊，我不是为了要书\n',
            '才跟你们说这些的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370943V#1000F请别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370944V这就当美味咖喱和咖啡\n',
            '的回礼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370945V你能这么说\n',
            '我真高兴…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370946V这样的话，\n',
            '那我就不客气了。',
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
            (TxtCtl.SetColor, 0x2),
            '牌技师杰克',
            (TxtCtl.SetColor, 0x0),
            '交给了店主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    RemoveItem(ItemTable['牌技师杰克 １卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ２卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ３卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ４卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ５卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ６卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ７卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ８卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 ９卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 10卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 11卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 12卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 13卷'], 1)
    RemoveItem(ItemTable['牌技师杰克 14卷'], 1)
    OP_0D()

    ChrTalk(
        0x002A,
        (
            '#2380370947V谢谢，我马上读来\n',
            '镇定一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370948V对了……\n',
            '这点东西，\n',
            '不呈谢意。',
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
            (TxtCtl.Item, ItemTable['塞姆里亚石']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['塞姆里亚石'], 1)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020370949V#1044F这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370950V这是我还在当外交官的时候，\n',
            '在亚尔特利亚得到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370951V#1015F亚尔特利亚应该是\n',
            '七耀教会的总部吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370927V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370953V这好像是用很久以前的塞姆里亚时代\n',
            '出产的金属制成的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370954V#1044F塞姆里亚时代的？\n',
            '确实从没见过这样的金属……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370955V哈哈，我也不知道\n',
            '是真是假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370956V顺带一提，加工此物的技术,\n',
            '据说已经完全失传了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370957V#1004F咦，这样想\n',
            '感觉像是很不得了的人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 7, 0x6F7)),
            Expr.Return,
        ),
        'loc_9A03',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370958V#1040F记得以前老板也拿武器\n',
            '来跟我换过书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370959V哈哈，你还记得阿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002A,
        (
            '#2380370960V这次虽然不是什么好东西，\n',
            '还请各位收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370961V#1001F嗯，我会好好珍惜它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A72')

    def _loc_9A03(): pass

    label('loc_9A03')

    ChrTalk(
        0x002A,
        (
            '#2380370962V哈哈，这次虽然不是什么好东西，\n',
            '还请各位收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370961V#1001F嗯，我会好好珍惜它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A72(): pass

    label('loc_9A72')

    OP_A2(0x10C4)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
