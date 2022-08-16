import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3120_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3120_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3120.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3120_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
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
    ChrClearFlags(0x000E, 0x0010)
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
        'loc_138',
    )

    Jump('loc_17A')

    def _loc_138(): pass

    label('loc_138')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_154',
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

    Jump('loc_17A')

    def _loc_154(): pass

    label('loc_154')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_170',
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

    Jump('loc_17A')

    def _loc_170(): pass

    label('loc_170')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17A(): pass

    label('loc_17A')

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

    ChrSetFlags(0x000E, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_224',
    )

    ChrTalk(
        0x000E,
        (
            '#0040240121V#030F想不到寻宝过程中\n',
            '会发现古代遗物呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240122V无论何时都拥有坚定信念的心……\n',
            '这应该是很重要的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313')

    def _loc_224(): pass

    label('loc_224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2D1',
    )

    ChrTalk(
        0x000E,
        (
            '#0040240123V#030F呀，诸位。\n',
            '贵安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240124V没想到在寻宝过程中竟然\n',
            '会发现古代遗物呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240125V无论何时都拥有坚定信念的心……\n',
            '这应该是很重要的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_313')

    def _loc_2D1(): pass

    label('loc_2D1')

    ChrTalk(
        0x000E,
        (
            '#0040240123V#030F呀，诸位。\n',
            '贵安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240127V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_313(): pass

    label('loc_313')

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
        (0x00000000, 'loc_370'),
        (0x00000001, 'loc_3E2'),
        (-1, 'loc_3E2'),
    )

    def _loc_370(): pass

    label('loc_370')

    ChrTalk(
        0x000E,
        (
            '#0040240128V#030F呼，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240129V看来你们还是需要\n',
            '我这个天才的力量啊。',
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
        'loc_3DB',
    )

    Call(1, 0x0007)

    Jump('loc_3DF')

    def _loc_3DB(): pass

    label('loc_3DB')

    Call(1, 0x0006)

    def _loc_3DF(): pass

    label('loc_3DF')

    Jump('loc_5D1')

    def _loc_3E2(): pass

    label('loc_3E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_567',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_473',
    )

    ChrTalk(
        0x000E,
        (
            '#0040240130V#031F那我就在这里\n',
            '稍微休息一会儿吧',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240131V呼呼～～趁这个机会，要和\n',
            '亲爱的提妲好好加深一下感情～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_564')

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F9',
    )

    ChrTalk(
        0x000E,
        (
            '#0040240132V#031F那我就继续\n',
            '在这里待命了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240133V呵呵，让我陪伴在公主殿下的身旁，\n',
            '一起渡过优雅的片刻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_564')

    def _loc_4F9(): pass

    label('loc_4F9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_564',
    )

    ChrTalk(
        0x000E,
        (
            '#0040240134V#031F那么就让我们在此\n',
            '畅谈一会儿吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240135V如果有葡萄酒喝\n',
            '就更好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_564(): pass

    label('loc_564')

    Jump('loc_5CE')

    def _loc_567(): pass

    label('loc_567')

    ChrTalk(
        0x000E,
        (
            '#0040231335V#030F我就继续\n',
            '在这里待命了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231336V如果需要我这个天才的话\n',
            '随时可以过来找我哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5CE(): pass

    label('loc_5CE')

    Jump('loc_5D1')

    def _loc_5D1(): pass

    label('loc_5D1')

    ChrSetSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x0001 offset: 0x5DA
@scena.Code('func_01_5DA')
def func_01_5DA():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x05,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000F)
    ChrClearFlags(0x000F, 0x0010)
    ChrTurnDirection(0x000F, 0x0000, 0)

    ExecExpressionWithValue(
        0x000F,
        0x04,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x04,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xF, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x05,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_66A',
    )

    Jump('loc_6AC')

    def _loc_66A(): pass

    label('loc_66A')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_686',
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6AC')

    def _loc_686(): pass

    label('loc_686')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_6A2',
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6AC')

    def _loc_6A2(): pass

    label('loc_6A2')

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.GetChrWork, 0xF, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6AC(): pass

    label('loc_6AC')

    ExecExpressionWithValue(
        0x000F,
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
        0x000F,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000F, 0x0010)

    ChrTalk(
        0x000F,
        (
            '#0060231330V#040F各位，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231331V有什么事吗？',
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
        (0x00000000, 'loc_76D'),
        (0x00000001, 'loc_7B5'),
        (-1, 'loc_7B5'),
    )

    def _loc_76D(): pass

    label('loc_76D')

    ChrTalk(
        0x000F,
        (
            '#0060231332V#040F明白了。\n',
            '要调整队伍吧？',
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
        'loc_7AE',
    )

    Call(1, 0x0007)

    Jump('loc_7B2')

    def _loc_7AE(): pass

    label('loc_7AE')

    Call(1, 0x0006)

    def _loc_7B2(): pass

    label('loc_7B2')

    Jump('loc_810')

    def _loc_7B5(): pass

    label('loc_7B5')

    ChrTalk(
        0x000F,
        (
            '#0060231333V#040F我就在这里待命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231334V如果有需要的话，\n',
            '请尽管开口就好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_810')

    def _loc_810(): pass

    label('loc_810')

    ChrSetSubChip(0x000F, 0)
    TalkEnd(0x000F)

    Return()

# id: 0x0002 offset: 0x819
@scena.Code('func_02_819')
def func_02_819():
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
    ChrClearFlags(0x000A, 0x0010)
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
        'loc_8A9',
    )

    Jump('loc_8EB')

    def _loc_8A9(): pass

    label('loc_8A9')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8C5',
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

    Jump('loc_8EB')

    def _loc_8C5(): pass

    label('loc_8C5')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8E1',
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

    Jump('loc_8EB')

    def _loc_8E1(): pass

    label('loc_8E1')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8EB(): pass

    label('loc_8EB')

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

    ChrSetFlags(0x000A, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_966',
    )

    ChrTalk(
        0x000A,
        (
            '#0070271308V#560F啊，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E2')

    def _loc_966(): pass

    label('loc_966')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_99F',
    )

    ChrTalk(
        0x000A,
        (
            '#0070890030V#060F啊，姐姐。\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E2')

    def _loc_99F(): pass

    label('loc_99F')

    ChrTalk(
        0x000A,
        (
            '#0070271311V#060F啊，是姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E2(): pass

    label('loc_9E2')

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
        (0x00000000, 'loc_A3F'),
        (0x00000001, 'loc_ADB'),
        (-1, 'loc_ADB'),
    )

    def _loc_A3F(): pass

    label('loc_A3F')

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
        'loc_A8F',
    )

    ChrTalk(
        0x000A,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AC1')

    def _loc_A8F(): pass

    label('loc_A8F')

    ChrTalk(
        0x000A,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AC1(): pass

    label('loc_AC1')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD4',
    )

    Call(1, 0x0007)

    Jump('loc_AD8')

    def _loc_AD4(): pass

    label('loc_AD4')

    Call(1, 0x0006)

    def _loc_AD8(): pass

    label('loc_AD8')

    Jump('loc_BC2')

    def _loc_ADB(): pass

    label('loc_ADB')

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
        'loc_B5A',
    )

    ChrTalk(
        0x000A,
        (
            '#0070271319V#064F咦，不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271320V#060F那我就在这里等着大家，\n',
            '有什么事就来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BBF')

    def _loc_B5A(): pass

    label('loc_B5A')

    ChrTalk(
        0x000A,
        (
            '#0070271319V#064F咦，不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271322V#060F我会一直在这里等着的，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BBF(): pass

    label('loc_BBF')

    Jump('loc_BC2')

    def _loc_BC2(): pass

    label('loc_BC2')

    ChrSetSubChip(0x000A, 0)
    TalkEnd(0x000A)

    Return()

# id: 0x0003 offset: 0xBCB
@scena.Code('func_03_BCB')
def func_03_BCB():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x05,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0011)
    ChrClearFlags(0x0011, 0x0010)
    ChrTurnDirection(0x0011, 0x0000, 0)

    ExecExpressionWithValue(
        0x0011,
        0x04,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x04,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x11, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x05,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_C5B',
    )

    Jump('loc_C9D')

    def _loc_C5B(): pass

    label('loc_C5B')

    If(
        (
            (Expr.GetChrWork, 0x11, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C77',
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C9D')

    def _loc_C77(): pass

    label('loc_C77')

    If(
        (
            (Expr.GetChrWork, 0x11, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C93',
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C9D')

    def _loc_C93(): pass

    label('loc_C93')

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.GetChrWork, 0x11, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C9D(): pass

    label('loc_C9D')

    ExecExpressionWithValue(
        0x0011,
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
        0x0011,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0011, 0x0010)

    ChrTalk(
        0x0011,
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
        (0x00000000, 'loc_D46'),
        (0x00000001, 'loc_D85'),
        (-1, 'loc_D85'),
    )

    def _loc_D46(): pass

    label('loc_D46')

    ChrTalk(
        0x0011,
        (
            '#0080271328V#070F要调整队伍吧？',
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
        'loc_D7E',
    )

    Call(1, 0x0007)

    Jump('loc_D82')

    def _loc_D7E(): pass

    label('loc_D7E')

    Call(1, 0x0006)

    def _loc_D82(): pass

    label('loc_D82')

    Jump('loc_DE2')

    def _loc_D85(): pass

    label('loc_D85')

    ChrTalk(
        0x0011,
        (
            '#0080311439V#070F喔，不用了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040033V如果需要我的拳头的话，\n',
            '尽管开口就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE2')

    def _loc_DE2(): pass

    label('loc_DE2')

    ChrSetSubChip(0x0011, 0)
    TalkEnd(0x0011)

    Return()

# id: 0x0004 offset: 0xDEB
@scena.Code('func_04_DEB')
def func_04_DEB():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x17, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x05,
        (
            (Expr.GetChrWork, 0x17, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0017)
    ChrClearFlags(0x0017, 0x0010)
    ChrTurnDirection(0x0017, 0x0000, 0)

    ExecExpressionWithValue(
        0x0017,
        0x04,
        (
            (Expr.GetChrWork, 0x17, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x04,
        (
            (Expr.GetChrWork, 0x17, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x17, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x05,
        (
            (Expr.GetChrWork, 0x17, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x17, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x17, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x17, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x17, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_E7B',
    )

    Jump('loc_EBD')

    def _loc_E7B(): pass

    label('loc_E7B')

    If(
        (
            (Expr.GetChrWork, 0x17, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E97',
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_EBD')

    def _loc_E97(): pass

    label('loc_E97')

    If(
        (
            (Expr.GetChrWork, 0x17, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EB3',
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_EBD')

    def _loc_EB3(): pass

    label('loc_EB3')

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.GetChrWork, 0x17, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_EBD(): pass

    label('loc_EBD')

    ExecExpressionWithValue(
        0x0017,
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
        0x0017,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0017, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F14',
    )

    ChrTalk(
        0x0017,
        (
            '#0030271323V#020F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F26')

    def _loc_F14(): pass

    label('loc_F14')

    ChrTalk(
        0x0017,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F26(): pass

    label('loc_F26')

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
        (0x00000000, 'loc_F83'),
        (0x00000001, 'loc_FE9'),
        (-1, 'loc_FE9'),
    )

    def _loc_F83(): pass

    label('loc_F83')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FBD',
    )

    ChrTalk(
        0x0017,
        (
            '#0030271324V#020F哎呀，要调整队伍吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FCF')

    def _loc_FBD(): pass

    label('loc_FBD')

    ChrTalk(
        0x0017,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FCF(): pass

    label('loc_FCF')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FE2',
    )

    Call(1, 0x0007)

    Jump('loc_FE6')

    def _loc_FE2(): pass

    label('loc_FE2')

    Call(1, 0x0006)

    def _loc_FE6(): pass

    label('loc_FE6')

    Jump('loc_1063')

    def _loc_FE9(): pass

    label('loc_FE9')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_104E',
    )

    ChrTalk(
        0x0017,
        (
            '#0030271325V#020F呵呵，我就在这儿\n',
            '慢慢休养吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271326V那么，之后就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1060')

    def _loc_104E(): pass

    label('loc_104E')

    ChrTalk(
        0x0017,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1060(): pass

    label('loc_1060')

    Jump('loc_1063')

    def _loc_1063(): pass

    label('loc_1063')

    ChrSetSubChip(0x0017, 0)
    TalkEnd(0x0017)

    Return()

# id: 0x0005 offset: 0x106C
@scena.Code('func_05_106C')
def func_05_106C():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x18, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x05,
        (
            (Expr.GetChrWork, 0x18, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0018)
    ChrClearFlags(0x0018, 0x0010)
    ChrTurnDirection(0x0018, 0x0000, 0)

    ExecExpressionWithValue(
        0x0018,
        0x04,
        (
            (Expr.GetChrWork, 0x18, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x04,
        (
            (Expr.GetChrWork, 0x18, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x18, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x05,
        (
            (Expr.GetChrWork, 0x18, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x18, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x18, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x18, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x18, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_10FC',
    )

    Jump('loc_113E')

    def _loc_10FC(): pass

    label('loc_10FC')

    If(
        (
            (Expr.GetChrWork, 0x18, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1118',
    )

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_113E')

    def _loc_1118(): pass

    label('loc_1118')

    If(
        (
            (Expr.GetChrWork, 0x18, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1134',
    )

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_113E')

    def _loc_1134(): pass

    label('loc_1134')

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.GetChrWork, 0x18, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_113E(): pass

    label('loc_113E')

    ExecExpressionWithValue(
        0x0018,
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
        0x0018,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0018, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1195',
    )

    ChrTalk(
        0x0018,
        (
            '#0050360144V#050F哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A7')

    def _loc_1195(): pass

    label('loc_1195')

    ChrTalk(
        0x0018,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A7(): pass

    label('loc_11A7')

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
        (0x00000000, 'loc_1204'),
        (0x00000001, 'loc_1268'),
        (-1, 'loc_1268'),
    )

    def _loc_1204(): pass

    label('loc_1204')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_123C',
    )

    ChrTalk(
        0x0018,
        (
            '#0050370786V#050F要替换队伍成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_124E')

    def _loc_123C(): pass

    label('loc_123C')

    ChrTalk(
        0x0018,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_124E(): pass

    label('loc_124E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1261',
    )

    Call(1, 0x0007)

    Jump('loc_1265')

    def _loc_1261(): pass

    label('loc_1261')

    Call(1, 0x0006)

    def _loc_1265(): pass

    label('loc_1265')

    Jump('loc_12E4')

    def _loc_1268(): pass

    label('loc_1268')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12CF',
    )

    ChrTalk(
        0x0018,
        (
            '#0050370787V#051F我就在此处待命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370788V如果需要我出力的话，\n',
            '随时说话就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12E1')

    def _loc_12CF(): pass

    label('loc_12CF')

    ChrTalk(
        0x0018,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12E1(): pass

    label('loc_12E1')

    Jump('loc_12E4')

    def _loc_12E4(): pass

    label('loc_12E4')

    ChrSetSubChip(0x0018, 0)
    TalkEnd(0x0018)

    Return()

# id: 0x0006 offset: 0x12ED
@scena.Code('func_06_12ED')
def func_06_12ED():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_132B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1313',
    )

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_1328')

    def _loc_1313(): pass

    label('loc_1313')

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_1328(): pass

    label('loc_1328')

    Jump('loc_1357')

    def _loc_132B(): pass

    label('loc_132B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1346',
    )

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    Jump('loc_1357')

    def _loc_1346(): pass

    label('loc_1346')

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    def _loc_1357(): pass

    label('loc_1357')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_13B4',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13B4',
    )

    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0011, 23530, 200, -2100, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetChipByIndex(0x0011, 18)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_13B4(): pass

    label('loc_13B4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1407',
    )

    ChrSetFlags(0x000E, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13E6',
    )

    ChrSetPos(0x000E, 23530, 200, -2100, 0)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_13FA')

    def _loc_13E6(): pass

    label('loc_13E6')

    ChrSetPos(0x000E, 23530, 200, 400, 180)
    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_13FA(): pass

    label('loc_13FA')

    ChrClearFlags(0x000E, 0x0080)
    ChrSetChipByIndex(0x000E, 6)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_1407(): pass

    label('loc_1407')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_145A',
    )

    ChrSetFlags(0x000F, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1439',
    )

    ChrSetPos(0x000F, 23530, 200, -2100, 0)
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_144D')

    def _loc_1439(): pass

    label('loc_1439')

    ChrSetPos(0x000F, 23530, 200, 400, 180)
    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_144D(): pass

    label('loc_144D')

    ChrClearFlags(0x000F, 0x0080)
    ChrSetChipByIndex(0x000F, 7)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_145A(): pass

    label('loc_145A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_148B',
    )

    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x000A, 23530, 200, 400, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 17)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_148B(): pass

    label('loc_148B')

    OP_0D()

    Return()

# id: 0x0007 offset: 0x148D
@scena.Code('func_07_148D')
def func_07_148D():
    OP_C9(
        0x01,
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

    Fade(1000)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_152A',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetFlags(0x0017, 0x0004)
    ChrSetChipByIndex(0x0017, 15)
    ChrSetPos(0x0017, 23550, 200, 420, 180)

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_150F',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_150F(): pass

    label('loc_150F')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_152A',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_152A(): pass

    label('loc_152A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_158D',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetFlags(0x0018, 0x0004)
    ChrSetChipByIndex(0x0018, 16)
    ChrSetPos(0x0018, 26270, 200, -480, 90)

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1572',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_1572(): pass

    label('loc_1572')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_158D',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_158D(): pass

    label('loc_158D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_15F0',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 17)
    ChrSetPos(0x000A, 28530, 200, -570, 270)

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15D5',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_15D5(): pass

    label('loc_15D5')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15F0',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_15F0(): pass

    label('loc_15F0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1653',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetChipByIndex(0x0011, 18)
    ChrSetPos(0x0011, 23550, 200, -2170, 0)

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1638',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_1638(): pass

    label('loc_1638')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1653',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_1653(): pass

    label('loc_1653')

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_16D4',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※要待命的成员\n',
            '　装备着『零力场发生器』。\n',
            '　将其回收后放入队伍的携带品中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_16D4(): pass

    label('loc_16D4')

    Return()

# id: 0x0008 offset: 0x16D5
@scena.Code('func_08_16D5')
def func_08_16D5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16E6',
    )

    OP_2A(0x00BB, 0x00BC, 0xFFFF)

    Jump('loc_17AB')

    def _loc_16E6(): pass

    label('loc_16E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1707',
    )

    OP_2A(0x006C, 0x006D, 0x006E, 0x00A5, 0x00A6, 0x006F, 0x0070, 0x00A7, 0x00A8, 0x0071, 0xFFFF)

    Jump('loc_17AB')

    def _loc_1707(): pass

    label('loc_1707')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1726',
    )

    OP_2A(0x006C, 0x006D, 0x006E, 0x00A5, 0x00A6, 0x006F, 0x0070, 0x00A7, 0x00A8, 0xFFFF)

    Jump('loc_17AB')

    def _loc_1726(): pass

    label('loc_1726')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1745',
    )

    OP_2A(0x006C, 0x006D, 0x006E, 0x00A5, 0x00A6, 0x006F, 0x0070, 0x00A7, 0x00A8, 0xFFFF)

    Jump('loc_17AB')

    def _loc_1745(): pass

    label('loc_1745')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 3, 0x140B)),
            Expr.Return,
        ),
        'loc_175C',
    )

    OP_2A(0x006C, 0x006D, 0x006E, 0x00A5, 0x00A6, 0xFFFF)

    Jump('loc_17AB')

    def _loc_175C(): pass

    label('loc_175C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_1773',
    )

    OP_2A(0x006C, 0x006D, 0x006E, 0x00A5, 0x00A6, 0xFFFF)

    Jump('loc_17AB')

    def _loc_1773(): pass

    label('loc_1773')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没有什么特别的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_17AB(): pass

    label('loc_17AB')

    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x17AF
@scena.Code('func_09_17AF')
def func_09_17AF():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    Call(1, 0x000F)

    ChrTalk(
        0x0008,
        (
            '#0580450691V#790F你们看过告示板了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450692V你们也要\n',
            '协助我们调查吗？',
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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1927',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450693V#1015F#7P不，不是这样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450694V#1006F只不过有点感兴趣而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580450695V#792F是吗，那就专心于\n',
            '其他的调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450696V这里的事情\n',
            '并不是什么紧急性的案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006C, 0x01, 0x8000)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

    def _loc_1927(): pass

    label('loc_1927')

    Call(1, 0x000B)

    Return()

# id: 0x000A offset: 0x192C
@scena.Code('func_0A_192C')
def func_0A_192C():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    Call(1, 0x000F)

    ChrTalk(
        0x0008,
        (
            '#0580450785V#790F看来你对招牌板的\n',
            '案件很有兴趣啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450786V愿意协助我们调查吗？',
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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A7C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450787V#1015F#7P不，不是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580450695V#792F是吗，那就专心于\n',
            '其他的调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450696V这里的事情\n',
            '并不是什么紧急性的案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

    def _loc_1A7C(): pass

    label('loc_1A7C')

    Call(1, 0x000B)

    Return()

# id: 0x000B offset: 0x1A81
@scena.Code('func_0B_1A81')
def func_0B_1A81():
    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010450697V#1002F#7P嗯、嗯……\n',
            '是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450698V招牌指的是\n',
            '吊在支部檐头上的\n',
            '那个带有徽章的招牌？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580450699V#792F嗯，那个招牌被盗了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450700V虽然不构成什么实际问题，\n',
            '不过徽章是协会的使命和义务的象征……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450701V#790F那东西被盗的话\n',
            '我们也不能坐视不管了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450702V#1015F是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450703V确实不能忽视呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1C46',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450704V#053F#5P呼，看来我们被别人小看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450705V#050F……那么，案件的经过是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CA5')

    def _loc_1C46(): pass

    label('loc_1C46')

    ChrTalk(
        0x0103,
        (
            '#0030450706V#025F#5P真是的，看来我们被别人小看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450707V#022F那么，案件的经过是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CA5(): pass

    label('loc_1CA5')

    ChrTalk(
        0x0008,
        (
            '#0580450708V#790F是在昨天午后\n',
            '被支部所属的王发现的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450709V他回来报告的时候，\n',
            '注意到外面的招牌不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450710V#792F被盗时间应该是\n',
            '当天上午。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450711V我因为有事出去所以支部内无人看守，\n',
            '正好在那时有人目击到\n',
            '支部面前有个施工人员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450712V#790F看来那个人就是\n',
            '化装后的罪犯。',
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
            '#0010450713V#1004F#7P化、化装？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E9A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450714V#043F艾、艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450715V这难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450716V#1020F#7P虽、虽然觉得有点不可思议……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F12')

    def _loc_1E9A(): pass

    label('loc_1E9A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F12',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450717V#033F哟，这可有意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450718V莫非这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450719V#1020F#7P莫、莫非……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F12(): pass

    label('loc_1F12')

    ChrTalk(
        0x0008,
        (
            '#0580450720V#790F看来你们有方向了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450721V#792F那么……\n',
            '这个是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170450722V　　美丽的公主及其随从啊。　\n',
            '　　　　众勇士之魂\n',
            '　　　 已落入我手中　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170450723V　　　如若期望得以解放\n',
            ' 　　只需胜我所施诅咒即可 　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170450724V　　　 第一把钥匙在市内　　　\n',
            '　寻『年龄４０之老翁』之背吧',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0580450725V#790F这是案发后\n',
            '寄来的卡片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450726V从内容来看\n',
            '可以认为这是犯罪声明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_211C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450727V#551F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_214A')

    def _loc_211C(): pass

    label('loc_211C')

    ChrTalk(
        0x0103,
        (
            '#0030450728V#025F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_214A(): pass

    label('loc_214A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2180',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450729V#045F看来是没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B1')

    def _loc_2180(): pass

    label('loc_2180')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21B1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321273V#032F看来没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21B1(): pass

    label('loc_21B1')

    ChrTalk(
        0x0101,
        (
            '#0010450731V#1007F#7P呼，是那家伙干的好事啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580450732V#792F『那家伙』指的是\n',
            '那个怪盗布卢布兰？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450733V#790F在卢安发生的一切\n',
            '我都听嘉恩说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450734V此次的案件……\n',
            '可以说成是怪盗Ｂ的挑战吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22ED',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450735V#031F呵呵，有意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450736V这正是我那劲敌的挑战。\n',
            '接受挑战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22ED(): pass

    label('loc_22ED')

    ChrTalk(
        0x0101,
        (
            '#0010450737V#1003F#7P竟然自说自话的发起挑战……',
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
        'loc_23AB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450738V#050F#5P不过，这是对方找上门的挑衅。\n',
            '我们只能接受挑战了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450739V总之先以卡片为依据\n',
            '开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2421')

    def _loc_23AB(): pass

    label('loc_23AB')

    ChrTalk(
        0x0103,
        (
            '#0030450740V#022F#5P虽然对方是自说自话地发起挑战，\n',
            '我们也只有接受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450741V总之先以卡片为依据\n',
            '开始调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2421(): pass

    label('loc_2421')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24D0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450744V#1000F#7P嗯，卡片上所写的是……\n',
            '『市内』和『４０岁老翁的后背』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070450745V#063F嗯～是不是要去找\n',
            '城里的某位老爷爷呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255F')

    def _loc_24D0(): pass

    label('loc_24D0')

    ChrTalk(
        0x0101,
        (
            '#0010450742V#1015F#7P嗯，卡片上所写的是……\n',
            '『市内』和『４０岁老翁的后背』呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450743V嗯～如果从字面意思理解的话，\n',
            '就是去找老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_255F(): pass

    label('loc_255F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2601',
    )

    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040450746V#032F唔，直接理解的话\n',
            '就是那样了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450747V但是，从在学院发生的一系列事件来看，\n',
            '用普通的方法明显是不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    Jump('loc_2694')

    def _loc_2601(): pass

    label('loc_2601')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2694',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060450748V#042F嗯，直接理解的话\n',
            '就是那样了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450749V不过从学院的系列谜团来看的话\n',
            '就不会是这么简单的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    def _loc_2694(): pass

    label('loc_2694')

    ChrTalk(
        0x0101,
        (
            '#0010450750V#1002F#7P那时的讯息\n',
            '都是某种『比喻』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450751V这次会不会也是那样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_275A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450752V#053F#5P嗯，这可不好说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450753V#050F发愁也没用。\n',
            '赶快去城里调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27B8')

    def _loc_275A(): pass

    label('loc_275A')

    ChrTalk(
        0x0103,
        (
            '#0030450754V#026F#5P嗯，这可不好说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450755V#022F发愁也没用。\n',
            '赶快去城里调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27B8(): pass

    label('loc_27B8')

    ChrTalk(
        0x0008,
        (
            '#0580450756V#790F嗯，只能这样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450757V那我就在这里静候佳音吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_280B')
    def lambda_280B():
        ChrSetDirection(0x0001, 0, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_280B)

    Sleep(50)

    @scena.Lambda('lambda_281E')
    def lambda_281E():
        ChrSetDirection(0x0002, 0, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_281E)

    Sleep(100)

    @scena.Lambda('lambda_2831')
    def lambda_2831():
        ChrSetDirection(0x0003, 0, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2831)

    ChrSetDirection(0x0000, 0, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28A3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450758V#031F呵呵，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450759V#1006F#7P那我们先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28EA')

    def _loc_28A3(): pass

    label('loc_28A3')

    ChrTalk(
        0x0101,
        (
            '#0010450760V#1006F#7P嗯，交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450761V那我们先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28EA(): pass

    label('loc_28EA')

    OP_28(0x006C, 0x01, 0x0001)
    OP_28(0x006C, 0x01, 0x0002)
    OP_28(0x006C, 0x04, 0x04)
    OP_28(0x006C, 0x04, 0x08)
    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x290A
@scena.Code('func_0C_290A')
def func_0C_290A():
    ChrTalk(
        0x0008,
        (
            '#0580450790V#790F要再次确认\n',
            '卡片内容？',
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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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
        'loc_2B28',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170450722V　　给美丽的公主和她的臣仆们。　　\n',
            '　　　众勇士之魂　　　　　　　　　\n',
            '　　 已落入我手中。 　　　　　　　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170450723V　　如若期望得以解放　　　\n',
            '　 只需胜我所施诅咒即可。 　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170450724V　　　 第一把钥匙在市内。 　　　\n',
            '　寻找『年龄４０之老翁』吧。　　',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0008,
        (
            '#0580450794V#790F关键点在于\n',
            '『市内』和『年龄４０之老翁』呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450795V那么调查就\n',
            '麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B6F')

    def _loc_2B28(): pass

    label('loc_2B28')

    ChrTalk(
        0x0008,
        (
            '#0580450796V#790F那就拜托你们调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580450797V我可期待着哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B6F(): pass

    label('loc_2B6F')

    Return()

# id: 0x000D offset: 0x2B70
@scena.Code('func_0D_2B70')
def func_0D_2B70():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0008, 3500, 0, 1200, 180)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 3500, 0, -3440, 0)
    ChrSetPos(0x0101, 3500, 0, -2210, 180)
    ChrSetPos(0x00F7, 4300, 0, -1830, 180)
    ChrSetPos(0x00F8, 2800, 0, -800, 180)
    ChrSetPos(0x00F9, 4200, 0, -800, 180)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C05',
    )

    ChrSetPos(0x000E, 2120, 0, -1810, 135)
    ChrSetChipByIndex(0x000E, 4)

    def _loc_2C05(): pass

    label('loc_2C05')

    CameraSetDistance(2720, 0)
    CameraMove(2650, 0, -1360, 0)
    OP_67(0, 6000, -10000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0580460201V#792F#2P──真可谓千钧一发啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580460202V如果先开宝箱的话\n',
            '你现在一定已经\n',
            '成为企鹅的食物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0019, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0019,
        (
            '#1770460203V啊、啊啊～！？\n',
            '企鹅的食物……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460204V我、我在反省啊，\n',
            '别吓唬我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2DA7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460205V#050F我并没有吓唬你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460206V因为这次你会得救\n',
            '真的是太偶然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460207V以此为鉴，\n',
            '你就好好认真反省吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E2C')

    def _loc_2DA7(): pass

    label('loc_2DA7')

    ChrTalk(
        0x0103,
        (
            '#0030460208V#020F我并没有吓唬你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460209V因为这次你会得救\n',
            '真的只是偶然的幸运。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460210V以此为鉴，\n',
            '你就好好地反省吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E2C(): pass

    label('loc_2E2C')

    ChrTalk(
        0x0019,
        (
            '#1770460211V嗯、嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460212V总、总之我要找份固定工作，\n',
            '挣够能够请护卫的米拉。',
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
            '#0010460213V#1016F原、原来是这么回事儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460214V就算反省了也还是\n',
            '要去危险的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460215V那、那当然了。\n',
            '寻宝是男人的浪漫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460216V为了像这次这样的发现，\n',
            '少许的危险也是不得已的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3059',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460217V#030F呼，那么所谓的\n',
            '『这次的发现』怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460218V好像从状况来看，\n',
            '是货真价实的海盗宝藏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460219V#1011F啊，是哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460220V总之要先把宝物\n',
            '还给吉米先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3234')

    def _loc_3059(): pass

    label('loc_3059')

    ChrTalk(
        0x000E,
        (
            '#0040460217V#030F呼，那么所谓的\n',
            '『这次的发现』怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460222V从刚才的话中，\n',
            '是货真价实的海盗宝藏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460219V#1011F啊，是哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460224V#1019F……咦，你怎么会\n',
            '见缝插针地站在这儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460225V你不是在2楼\n',
            '度过优雅的片刻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0040460226V#031F那个，因为听到了\n',
            '欢快的声音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460227V好了，不用管我，\n',
            '继续你们的谈话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460228V#1007F我总是对你的好奇心\n',
            '深感钦佩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460229V#1015F好，先不管这家伙，\n',
            '首先要返还宝物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0019, 400)

    def _loc_3234(): pass

    label('loc_3234')

    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x000003E8, 0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#16I银露宝珠',
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x000003E8, 0x00)

    ChrTalk(
        0x0019,
        (
            '#1770460230V啊、谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460231V感觉像梦境一样。\n',
            '竟然真能找到财宝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460232V#1015F嗯，不过不知道\n',
            '这是什么东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460233V根据残留下来的信件内容记载，\n',
            '这好像是很了不起的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460234V确、确实如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460235V我也没见过\n',
            '这种东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3482',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460236V#070F嗯，这恐怕是\n',
            '古代遗物吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460237V从外观来看\n',
            '应该已经没有力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_3438')
    def lambda_3438():
        ChrTurnDirection(0x0101, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3438)

    @scena.Lambda('lambda_3446')
    def lambda_3446():
        ChrTurnDirection(0x00F7, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3446)

    @scena.Lambda('lambda_3454')
    def lambda_3454():
        ChrTurnDirection(0x00F8, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3454)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3478',
    )

    @scena.Lambda('lambda_3470')
    def lambda_3470():
        ChrTurnDirection(0x000E, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3470)

    def _loc_3478(): pass

    label('loc_3478')

    ChrTurnDirection(0x00F9, 0x0108, 400)

    Jump('loc_35F9')

    def _loc_3482(): pass

    label('loc_3482')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3538',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460238V#030F嗯，这恐怕是\n',
            '古代遗物吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460239V从外观来看\n',
            '应该已经没有力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_350A')
    def lambda_350A():
        ChrTurnDirection(0x0101, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_350A)

    @scena.Lambda('lambda_3518')
    def lambda_3518():
        ChrTurnDirection(0x00F7, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3518)

    @scena.Lambda('lambda_3526')
    def lambda_3526():
        ChrTurnDirection(0x00F8, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3526)

    ChrTurnDirection(0x00F9, 0x0104, 400)

    Jump('loc_35F9')

    def _loc_3538(): pass

    label('loc_3538')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35F9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460240V#042F这恐怕是……\n',
            '古代遗物吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460241V从外观来看\n',
            '应该已经没有力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_35C0')
    def lambda_35C0():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35C0)

    @scena.Lambda('lambda_35CE')
    def lambda_35CE():
        ChrTurnDirection(0x00F7, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_35CE)

    @scena.Lambda('lambda_35DC')
    def lambda_35DC():
        ChrTurnDirection(0x00F8, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_35DC)

    @scena.Lambda('lambda_35EA')
    def lambda_35EA():
        ChrTurnDirection(0x000E, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_35EA)

    ChrTurnDirection(0x00F9, 0x0105, 400)

    def _loc_35F9(): pass

    label('loc_35F9')

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(400)

    ChrTalk(
        0x0019,
        (
            '#1770460242V咦咦！？\n',
            '古、古代遗物！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460243V#1004F古代遗物是……\n',
            '就是古代文明的遗物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460244V即便已经没有了力量，\n',
            '可这也算是了不得的东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_372C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460245V#070F嗯，应该拿到相关部门\n',
            '去让他们调查一下比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460246V个人持有的话\n',
            '会碰上很多麻烦的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3834')

    def _loc_372C(): pass

    label('loc_372C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37A2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460247V#030F应该拿到相关部门\n',
            '去让他们调查一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460248V我不推荐个人\n',
            '持有这种东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3834')

    def _loc_37A2(): pass

    label('loc_37A2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3834',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460249V#047F嗯，我觉得应该拿到相关部门\n',
            '去让他们调查一下比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460250V#042F因为这种东西由个人\n',
            '持有不是什么好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3834(): pass

    label('loc_3834')

    ChrTalk(
        0x0008,
        (
            '#0580460251V#790F说起附近的研究机关，\n',
            '那就是王都的历史资料馆了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580460252V如果你愿意的话\n',
            '我们可以帮你联系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_38AF')
    def lambda_38AF():
        ChrTurnDirection(0x0101, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38AF)

    Sleep(100)

    @scena.Lambda('lambda_38C2')
    def lambda_38C2():
        ChrSetDirection(0x00F7, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_38C2)

    Sleep(50)

    @scena.Lambda('lambda_38D5')
    def lambda_38D5():
        ChrTurnDirection(0x00F8, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_38D5)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38FE',
    )

    @scena.Lambda('lambda_38F1')
    def lambda_38F1():
        ChrTurnDirection(0x000E, 0x0019, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_38F1)

    Sleep(50)

    def _loc_38FE(): pass

    label('loc_38FE')

    ChrTurnDirection(0x00F9, 0x0019, 400)

    ChrTalk(
        0x0019,
        (
            '#1770460253V请、请一定帮我联系！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460254V如果是这么了不得的东西的话，\n',
            '我希望能被保管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580460255V#790F……这样啊，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580460256V那么，到王都的票也\n',
            '一并帮你安排了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460257V啊，谢谢！\n',
            '服务真周到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580460258V#792F不，这是必要的经费安排。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580460259V因为你现在\n',
            '身无分文吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0019,
        (
            '#1770460260V啊！？\n',
            '你、你怎么会知道的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460261V#1016F哈哈，这么快\n',
            '就被看穿了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460262V#1000F不过，这样的话\n',
            '就尽管使用定期船吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460263V老实说，让吉米先生\n',
            '在大道上步行还真令人不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3B66',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460264V#551F嗯，我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B8B')

    def _loc_3B66(): pass

    label('loc_3B66')

    ChrTalk(
        0x0103,
        (
            '#0030460265V#025F嗯，我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B8B(): pass

    label('loc_3B8B')

    ChrTalk(
        0x0008,
        (
            '#0580460266V#790F#2P船票你就在飞船坪的\n',
            '接待处领取吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580460267V那么，请小心前往王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460268V今天真是太谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x8000)"),
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x10)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C27',
    )

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    def _loc_3C27(): pass

    label('loc_3C27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CA0',
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
            TXT(0x00, '【◇曾经完成上部吉米任务】\n'),
            TXT(0x01, '【◇不变更】\n'),
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
        (0x00000000, 'loc_3C9A'),
        (-1, 'loc_3CA0'),
    )

    def _loc_3C9A(): pass

    label('loc_3C9A')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    Jump('loc_3CA0')

    def _loc_3CA0(): pass

    label('loc_3CA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_3E25',
    )

    ChrTalk(
        0x0019,
        (
            '#1770460269V……不，想想的话也\n',
            '不光是今天一天的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460270V一直以来都受\n',
            '你的照顾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460271V……对了，请收下这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['阴阳']),
            (TxtCtl.SetColor, 0x0),
            '结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['阴阳'], 1)

    ChrTalk(
        0x0019,
        (
            '#1770460272V这是我爱用的东西。\n',
            '从现在起由你来使用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460273V#1004F可以吗？　我收这种东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460274V这表示我一直以来的谢意。\n',
            '请收下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E25(): pass

    label('loc_3E25')

    ChrTalk(
        0x0019,
        (
            '#1770460275V那么我们在王都再会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460276V#1006F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460277V那个『宝珠』……\n',
            '要好好地送交资料馆哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1770460278V嗯，交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F41',
    )

    ChrTalk(
        0x000E,
        (
            '#0040460279V#031F那我也要\n',
            '撤了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460280V那么再见了，吉米。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0019, 0x000E, 400)

    ChrTalk(
        0x0019,
        (
            '#1770460281V嗯，你也要保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F41(): pass

    label('loc_3F41')

    @scena.Lambda('lambda_3F47')
    def lambda_3F47():
        CameraMove(1820, 0, -4980, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3F47)

    ChrSetDirection(0x0019, 270, 400)
    CreateThread(0x000E, 0x00, 0x01, 0x000E)
    ChrWalkTo(0x0019, 1450, 0, -6180, 2000, 0x00)

    @scena.Lambda('lambda_3F81')
    def lambda_3F81():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_3F81)

    ChrWalkTo(0x0019, 1450, 0, -8020, 2000, 0x00)
    WaitForThreadExit(0x0019, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    OP_28(0x0071, 0x04, 0x10)
    OP_28(0x0071, 0x01, 0x0004)
    OP_28(0x0071, 0x01, 0x0008)
    OP_28(0x0071, 0x01, 0x0010)
    OP_69(0x0101, 2000)
    WaitForThreadExit(0x000E, 0x0000)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【投宿客人的搜索】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x000E offset: 0x402C
@scena.Code('func_0E_402C')
def func_0E_402C():
    Sleep(400)

    ChrSetDirection(0x000E, 315, 500)
    ChrSetFlags(0x000E, 0x0004)
    ChrWalkTo(0x000E, -1840, 0, 1310, 2500, 0x00)
    ChrWalkTo(0x000E, -1960, 0, 2450, 2500, 0x00)
    ChrSetDirection(0x000E, 90, 500)
    ChrClearFlags(0x000E, 0x0004)
    ChrWalkTo(0x000E, 2500, 2250, 2730, 2500, 0x00)
    ChrSetFlags(0x000E, 0x0080)

    Return()

# id: 0x000F offset: 0x408B
@scena.Code('func_0F_408B')
def func_0F_408B():
    Fade(1000)
    ChrSetDirection(0x0008, 180, 0)
    ChrSetPos(0x0101, 4230, 0, -710, 0)
    ChrSetPos(0x00F7, 3180, 0, -700, 0)
    ChrSetPos(0x00F8, 4300, 0, -1950, 0)
    ChrSetPos(0x00F9, 3380, 0, -2100, 0)
    CameraMove(3550, 0, 330, 0)
    OP_67(0, 6000, -10000, 0)
    OP_0D()

    Return()

# id: 0x0010 offset: 0x40FF
@scena.Code('func_10_40FF')
def func_10_40FF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4110',
    )

    Call(0, 0x001B)

    def _loc_4110(): pass

    label('loc_4110')

    EventBegin(0x00)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0008, 5230, 0, 2029, 0)
    ChrSetPos(0x0101, 2240, 0, -5100, 0)
    ChrSetPos(0x00F7, 1230, 0, -5230, 0)
    ChrSetPos(0x0105, 2170, 0, -6120, 0)
    ChrSetPos(0x0104, 1010, 0, -6200, 0)
    CameraMove(5230, 0, 2029, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    CameraMove(2240, 0, -5100, 0)
    OP_69(0x0008, 0)
    LoadEffect(0x00, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0580220412V#792F嗯，中央工房\n',
            '没有受到损害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220413V#791F市区也没出什么大事，\n',
            '可以放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220414V嗯，有关那件事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220415V那么先这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0104, 0x0001)
    Sleep(300)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0580220416V#792F呵呵……\n',
            '来得还真是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4314')
    def lambda_4314():
        CameraMove(2450, 0, -1640, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4314)

    @scena.Lambda('lambda_432C')
    def lambda_432C():
        OP_67(0, 6000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_432C)

    ChrSetDirection(0x0008, 270, 400)
    ChrSetDirection(0x0008, 180, 400)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_44DE',
    )

    ChrTalk(
        0x0008,
        (
            '#0580220417V#791F#2P你们终于到了啊。\n',
            '艾丝蒂尔，阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220418V在飞船坪那里吓了一跳吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220419V#1016F#6P啊，啊哈哈……\n',
            '好久不见啦，雾香姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4404')
    def lambda_4404():
        CameraMove(3350, 0, 330, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4404)

    @scena.Lambda('lambda_441C')
    def lambda_441C():
        OP_67(0, 6000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_441C)

    CreateThread(0x0101, 0x01, 0x01, 0x0011)
    Sleep(250)

    CreateThread(0x0008, 0x01, 0x01, 0x0015)
    Sleep(250)

    CreateThread(0x00F7, 0x01, 0x01, 0x0012)
    Sleep(250)

    CreateThread(0x0105, 0x01, 0x01, 0x0013)
    Sleep(250)

    CreateThread(0x0104, 0x01, 0x01, 0x0014)
    WaitForThreadExit(0x0104, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0106,
        (
            '#0050220420V#051F#6P哼，还是和从前一样，\n',
            '什么事情都能料到啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220421V算啦，总之请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4660')

    def _loc_44DE(): pass

    label('loc_44DE')

    ChrTalk(
        0x0008,
        (
            '#0580220422V#791F#2P你们终于到了啊。\n',
            '艾丝蒂尔，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220418V在飞船坪那里吓了一跳吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220419V#1016F#6P啊，啊哈哈……\n',
            '好久不见啦，雾香姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4587')
    def lambda_4587():
        CameraMove(3550, 0, 330, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4587)

    @scena.Lambda('lambda_459F')
    def lambda_459F():
        OP_67(0, 6000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_459F)

    CreateThread(0x0101, 0x01, 0x01, 0x0011)
    Sleep(250)

    CreateThread(0x0008, 0x01, 0x01, 0x0015)
    Sleep(250)

    CreateThread(0x00F7, 0x01, 0x01, 0x0012)
    Sleep(250)

    CreateThread(0x0105, 0x01, 0x01, 0x0013)
    Sleep(250)

    CreateThread(0x0104, 0x01, 0x01, 0x0014)
    WaitForThreadExit(0x0104, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0103,
        (
            '#0030220425V#021F#6P呵呵，还是和以前一样，\n',
            '什么都被你料到了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220426V#020F雾香。\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4660(): pass

    label('loc_4660')

    ChrTalk(
        0x0008,
        (
            '#0580220427V#791F你们能来也是帮我大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220428V嗯，站在那边的两位就是\n',
            '公主殿下和奥利维尔先生了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220429V我叫雾香。\n',
            '是蔡斯支部的负责人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220430V以后还请多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220431V#048F#6P是的，彼此彼此。\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040220432V#037F#6P呼，真是比想象中\n',
            '更美丽的佳人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220433V请允许我奥利维尔为你\n',
            '献上一首即兴之曲吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580220434V#791F听嘉恩说，你们已经是\n',
            '正式的协力者了对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220435V协力者同游击士一样，\n',
            '可以自由使用楼上的休息室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220436V也可以在那里进行约见会谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220437V#041F#6P是，我们知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040220438V#036F#6P啊～我的即兴之曲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580220439V#792F想弹奏鲁特琴的话\n',
            '可以去楼上的休息室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220440V但请在常识的范围内进行演奏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040220441V#034F#6P呜……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220442V#1016F#6P（比起雪拉姐…\n',
            '真是一点情面也不留啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4A4C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220443V#551F#6P哈，那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220444V#051F还是快点把工作的状况\n',
            '说给我们听听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AB7')

    def _loc_4A4C(): pass

    label('loc_4A4C')

    ChrTalk(
        0x0103,
        (
            '#0030220445V#021F#6P好啦，这个笨蛋\n',
            '就不用管他了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220446V#020F还是先把工作的情况\n',
            '告诉我们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AB7(): pass

    label('loc_4AB7')

    ChrTalk(
        0x0008,
        (
            '#0580220447V#792F告示板上确实是积攒了不少委托，\n',
            '不过都不是什么太紧急的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220448V凭你们的能力\n',
            '很容易就可以解决了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220449V#790F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220450V#1004F#6P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220451V你怎么了？雾香姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580220452V#791F这个不是普通的委托，\n',
            '而是协会的直接请求……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220453V希望你们可以对『结社』\n',
            '展开调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4CA9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220454V#057F#6P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CD1')

    def _loc_4CA9(): pass

    label('loc_4CA9')

    ChrTalk(
        0x0103,
        (
            '#0030220455V#022F#6P怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CD1(): pass

    label('loc_4CD1')

    ChrTalk(
        0x0101,
        (
            '#0010220456V#1002F#6P还、还真是单刀直入啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220457V#043F#6P那个……\n',
            '究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580220458V#790F想让你们调查的事，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220459V就是刚才发生的『地震』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220460V#1015F#6P调查地震？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220461V是去向大家询问\n',
            '受害程度吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580220462V#792F那当然也包括在内……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220463V其实在３天前，沃尔费堡垒\n',
            '也发生过同样的地震。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220464V时间好像在１０秒左右，\n',
            '听说没有出现什么受害状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4EC0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220465V#552F#6P原来如此……\n',
            '和刚才的地震和相似啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EFD')

    def _loc_4EC0(): pass

    label('loc_4EC0')

    ChrTalk(
        0x0103,
        (
            '#0030220466V#522F#6P原来如此……\n',
            '和刚才的地震很相似呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EFD(): pass

    label('loc_4EFD')

    ChrTalk(
        0x0008,
        (
            '#0580220467V#790F奇怪的现象还有一个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220468V在沃尔费堡垒发生地震的时候，\n',
            '蔡斯市却完全没有任何摇晃。',
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
            '#0010220469V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220470V#032F#6P嗯，那真是很奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220471V从地图上看，沃尔费堡垒\n',
            '离这里并不算远。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220472V那里如果发生了地震，这边\n',
            '多少也应该能感觉到摇晃才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580220473V#790F也有可能是因为震级较低，\n',
            '所以没有注意到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220474V#792F只是，嗯……\n',
            '可能是直觉的判断吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220475V我总有种不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220476V#1007F#6P我明白你的意思了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220477V#1002F幽灵事件也是如此，\n',
            '这种奇异的现象我也是很在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_51C9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220478V#051F#6P好！我们接受了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220479V那就先在蔡斯市和沃尔费堡垒\n',
            '两个地方进行调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_523E')

    def _loc_51C9(): pass

    label('loc_51C9')

    ChrTalk(
        0x0103,
        (
            '#0030220480V#020F#6P嗯，那我们就接受委托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220481V只要在蔡斯市和沃尔费堡垒\n',
            '两个地方进行调查就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_523E(): pass

    label('loc_523E')

    ChrTalk(
        0x0008,
        (
            '#0580220482V#791F那就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220483V市内的情报你们可以\n',
            '找玛多克工房长帮忙，\n',
            '也许他那里已经有足够的情报了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220484V如果是那样的话，你们\n',
            '就可以省下不少力气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220485V#1006F#6P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220486V也就是说，沃尔费堡垒\n',
            '是必须要去调查的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580220487V#792F嗯，不过这也只是我个人比较在意而已，\n',
            '也不用把它当成紧急性的委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220488V一边完成告示板上的委托，\n',
            '一边抽空去进行就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580220489V#791F另外……\n',
            '你们也有想去拜会的朋友吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220490V#1008F#6P啊……嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220491V有关新型『福音』的事情\n',
            '我们也要去通知给博士和提妲才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220492V#542F#6P是啊……\n',
            '先去看看他们也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220493V#030F#6P呼～既然如此，协会的工作\n',
            '就先暂放一边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220494V#031F为了和提妲再会，\n',
            '我们马上就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_55C0',
    )

    @scena.Lambda('lambda_553E')
    def lambda_553E():
        ChrTurnDirection(0x0101, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_553E)

    @scena.Lambda('lambda_554C')
    def lambda_554C():
        ChrTurnDirection(0x0105, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_554C)

    ChrTurnDirection(0x0106, 0x0104, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220495V#551F#5P你这家伙\n',
            '有什么好激动的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220496V#050F好啦，这就去拉赛尔工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5648')

    def _loc_55C0(): pass

    label('loc_55C0')

    @scena.Lambda('lambda_55C6')
    def lambda_55C6():
        ChrTurnDirection(0x0103, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_55C6)

    @scena.Lambda('lambda_55D4')
    def lambda_55D4():
        ChrTurnDirection(0x0105, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_55D4)

    ChrSetDirection(0x0101, 186, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220497V#1007F#5P提妲和你\n',
            '又没有什么关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220498V#1006F好啦。\n',
            '去一趟拉赛尔工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5648(): pass

    label('loc_5648')

    SetScenaFlags(ScenaFlag(0x0281, 0, 0x1408))
    OP_28(0x0085, 0x04, 0x02)
    OP_28(0x0085, 0x04, 0x08)
    OP_28(0x0085, 0x01, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_4B(0x0008, 255)
    CameraMove(2550, 0, -2610, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2550, 0, -2610, 180)
    ChrSetPos(0x00F7, 2550, 0, -2610, 180)
    ChrSetPos(0x0105, 2550, 0, -2610, 180)
    ChrSetPos(0x0104, 2550, 0, -2610, 180)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x56FC
@scena.Code('func_11_56FC')
def func_11_56FC():
    ChrWalkTo(0x00FE, 4230, 0, -710, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0012 offset: 0x5718
@scena.Code('func_12_5718')
def func_12_5718():
    ChrWalkTo(0x00FE, 3180, 0, -700, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x5734
@scena.Code('func_13_5734')
def func_13_5734():
    ChrWalkTo(0x00FE, 4300, 0, -1950, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x5750
@scena.Code('func_14_5750')
def func_14_5750():
    ChrWalkTo(0x00FE, 3380, 0, -2100, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0015 offset: 0x576C
@scena.Code('func_15_576C')
def func_15_576C():
    ChrWalkTo(0x0008, 5250, 0, 1330, 2000, 0x00)
    ChrWalkTo(0x0008, 3500, 0, 1200, 2000, 0x00)
    ChrSetDirection(0x0008, 180, 400)

    Return()

# id: 0x0016 offset: 0x579C
@scena.Code('func_16_579C')
def func_16_579C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_57AD',
    )

    Call(0, 0x001B)

    def _loc_57AD(): pass

    label('loc_57AD')

    ChrSetStatus(ChrTable['提妲'], 0x00, 40)
    ChrSetStatus(ChrTable['提妲'], 0xFE, 0)
    EquipCmd(ChrTable['提妲'], ItemTable['Ｐ－０７'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['纤维护铠'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['金属靴'], 0xFF)
    EquipCmd(ChrTable['提妲'], ItemTable['省ＥＰ２'], 0x00)
    EquipCmd(ChrTable['提妲'], ItemTable['攻击２'], 0x02)
    EquipCmd(ChrTable['提妲'], ItemTable['鹰目'], 0x03)
    AddCraft(ChrTable['提妲'], 0x0000)
    AddCraft(ChrTable['提妲'], CraftTable['连锁战技１(２人协力)'])
    OP_BB(0x06, 0x06, 0x00000104)
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetPos(0x000B, 2770, 1050, 100, 0)
    ChrSetPos(0x000C, 3770, 1050, 100, 0)
    ChrSetPos(0x000D, 4770, 1050, 100, 0)
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_A1(0x000B, 0x0001)
    OP_A1(0x000C, 0x0002)
    OP_A1(0x000D, 0x0003)
    ChrSetPos(0x0009, 3400, 0, -790, 0)
    ChrSetPos(0x000A, 4460, 0, -720, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    CameraMove(1770, 0, -2950, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2720, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    CreateThread(0x0101, 0x01, 0x01, 0x0017)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x01, 0x0018)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x01, 0x0019)
    Sleep(500)

    CreateThread(0x0104, 0x01, 0x01, 0x001A)
    Sleep(500)

    PlaySE(7, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0104, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010221196V#1004F#5P啊……\n',
            '怎么了，二位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)
    ChrSetDirection(0x000A, 180, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_59A5',
    )

    ChrTalk(
        0x000A,
        (
            '#0070221197V#061F#2P啊……\n',
            '姐姐，还有阿加特哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59D4')

    def _loc_59A5(): pass

    label('loc_59A5')

    ChrTalk(
        0x000A,
        (
            '#0070221198V#061F#2P啊……\n',
            '艾丝蒂尔姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_59D4(): pass

    label('loc_59D4')

    ChrTalk(
        0x0009,
        (
            '#0540221199V#101F#2P喔喔～回来得\n',
            '还真是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5A0F')
    def lambda_5A0F():
        CameraMove(3520, 0, -260, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_5A0F)

    @scena.Lambda('lambda_5A27')
    def lambda_5A27():
        CameraMove(3520, 0, -260, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_5A27)

    @scena.Lambda('lambda_5A3F')
    def lambda_5A3F():
        ChrWalkTo(0x00FE, 4370, 0, -1770, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5A3F)

    Sleep(200)

    @scena.Lambda('lambda_5A5F')
    def lambda_5A5F():
        ChrWalkTo(0x00FE, 3330, 0, -2100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5A5F)

    Sleep(300)

    @scena.Lambda('lambda_5A7F')
    def lambda_5A7F():
        ChrWalkTo(0x00FE, 4560, 0, -2870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5A7F)

    Sleep(200)

    @scena.Lambda('lambda_5A9F')
    def lambda_5A9F():
        ChrWalkTo(0x00FE, 3520, 0, -3200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_5A9F)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 0, 400)
    WaitForThreadExit(0x00F7, 0x0001)
    ChrSetDirection(0x00F7, 0, 400)
    WaitForThreadExit(0x0105, 0x0001)
    ChrSetDirection(0x0105, 0, 400)
    WaitForThreadExit(0x0104, 0x0001)
    ChrSetDirection(0x0104, 0, 400)
    WaitForThreadExit(0x000A, 0x0002)
    WaitForThreadExit(0x000A, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5BC1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221200V#051F#3P地震的调查已经完成了，\n',
            '我们就回来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221201V嗯？那堆破烂是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540221202V#104F#5P说破烂可太失礼了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221203V#100F这个就是之前我说的那个\n',
            '『好东西』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C90')

    def _loc_5BC1(): pass

    label('loc_5BC1')

    ChrTalk(
        0x0101,
        (
            '#0010221204V#1011F#6P地震的调查已经完成了，\n',
            '我们正要回来报告……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221205V嗯？那些机械是做什么的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540221206V#101F#5P呵呵呵，\n',
            '问的好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221203V#100F这个就是之前我说的那个\n',
            '『好东西』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C90(): pass

    label('loc_5C90')

    ChrTalk(
        0x0008,
        (
            '#0580221208V#792F嗯，时间紧迫，有关那个的说明\n',
            '还请稍后再说吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221209V#791F听说你们连圣海姆门\n',
            '也一起调查过了对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221210V那么就和沃尔费堡垒的调查\n',
            '一起做个报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221211V#1002F#6P嗯，是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E0B',
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
            TXT(0x00, '【◇在蔡斯看过瓦鲁特的情报】\n'),
            TXT(0x01, '【◇没有在蔡斯看过瓦鲁特的情报】\n'),
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
        (0x00000000, 'loc_5DFF'),
        (0x00000001, 'loc_5E05'),
        (-1, 'loc_5E0B'),
    )

    def _loc_5DFF(): pass

    label('loc_5DFF')

    SetScenaFlags(ScenaFlag(0x0290, 0, 0x1480))

    Jump('loc_5E0B')

    def _loc_5E05(): pass

    label('loc_5E05')

    ClearScenaFlags(ScenaFlag(0x0290, 0, 0x1480))

    Jump('loc_5E0B')

    def _loc_5E0B(): pass

    label('loc_5E0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 0, 0x1480)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_60AD',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将沃尔费堡垒和圣海姆门\n',
            '的调查结果报告给雾香。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0540221212V#104F#5P原来如此……\n',
            '地震的规模似乎开始扩大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221213V#102F看来事态比想象中的更加严重呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070221214V#063F#2P嗯、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070221215V如果蔡斯市内\n',
            '再发生更大地震的话，\n',
            '那可就不得了了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580221216V#792F还有在两个地震地点都\n',
            '被目击到的墨镜男子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221217V#790F和在蔡斯市内被目击到的那个人\n',
            '像是同一个人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221218V#1002F#6P是吗……\n',
            '果然也出现在市内了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580221219V#790F嗯，玛多克工房长\n',
            '帮忙收集了市内的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221220V那个男人为『结社』一员\n',
            '的可能性相当的高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221221V因此各位今后一定要\n',
            '全力协助博士的实验才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62A0')

    def _loc_60AD(): pass

    label('loc_60AD')

    OP_2B(0x0085, 0x0003)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将沃尔费堡垒、圣海姆门\n',
            '以及蔡斯市内的调查结果做了报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0540221212V#104F#5P原来如此……\n',
            '地震的规模似乎开始扩大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221213V#102F看来事态比想象中的更加严重呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070221224V#063F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070221225V如果蔡斯市内\n',
            '再发生更大地震的话，\n',
            '那可就不得了了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580221226V#792F还有，在全部事发场所中都\n',
            '被目击到的墨镜男子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221227V#790F那个男人为『结社』一员\n',
            '的可能性相当的高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221221V因此各位今后一定要\n',
            '全力协助博士的实验才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62A0(): pass

    label('loc_62A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_62E1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221229V#052F#3P实验……\n',
            '是要使用这个装置吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_633C')

    def _loc_62E1(): pass

    label('loc_62E1')

    ChrTalk(
        0x0103,
        (
            '#0030221230V#027F#3P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221231V所谓的实验，就是要使用\n',
            '这个装置进行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_633C(): pass

    label('loc_633C')

    ChrTalk(
        0x0009,
        (
            '#0540221232V#101F#5P嗯，正是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221233V#100F这个是我在数年前\n',
            '开发的『七耀脉测量仪』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221234V将它设置在地面\n',
            '就可以对『七耀脉』的流动\n',
            '进行实时的感知和测定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221235V#1016F#6P哎哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221236V#1008F虽然这个名词已经听过好几次了，\n',
            '不过……『七耀脉』究竟是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070221237V#560F#2P那个啊，是存在于地下深处的\n',
            '巨大的七耀石矿脉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070221238V它蕴藏的巨大能源可以对大地\n',
            '造成一定的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_655C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040221239V#035F#3P『地脉』、『灵脉』等说法\n',
            '都是它的别称呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221240V#030F在东方好像是把它称作『龙脉』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_65D1')

    def _loc_655C(): pass

    label('loc_655C')

    ChrTalk(
        0x0103,
        (
            '#0030221241V#020F#3P『地脉』、『灵脉』等说法\n',
            '好像也都是指它呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221242V在东方，好像是把它称作『龙脉』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_65D1(): pass

    label('loc_65D1')

    ChrTalk(
        0x0008,
        (
            '#0580221243V#791F啊，你知道的还真清楚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221244V在很久以前的东方，人们都将都市建造\n',
            '在传说有龙脉流经的地方呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221245V大概是想把大地的能源\n',
            '用于国家的建设吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221246V#1011F#6P嘿嘿～原来是这样啊。\n',
            '又上了一课呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060221247V#043F#6P那么，使用这装置的话\n',
            '就可以阻止地震的发生了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540221248V#104F#5P不，它只能探测七耀脉的流动，\n',
            '并不能真正阻止地震的发生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221249V#100F但是，在塞姆里亚大陆中\n',
            '流传着这种说法：地震是由于七耀脉\n',
            '的流动造成地壳歪曲而引发的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221250V所以，只要调查七耀脉的流动情况，\n',
            '也许就能发现什么有用的线索了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060221251V#047F#6P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221252V#040F那么，在下次地震发生之前\n',
            '要尽快将它们设置好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_68C7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221253V#051F#3P装置共有３个，\n',
            '也就是说要分别放置在３个地方了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_690A')

    def _loc_68C7(): pass

    label('loc_68C7')

    ChrTalk(
        0x0103,
        (
            '#0030221254V#020F#3P装置共有３个，\n',
            '是要分别设置在３处场所吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_690A(): pass

    label('loc_690A')

    ChrTalk(
        0x0009,
        (
            '#0540221255V#102F#5P嗯，把地图给我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    @scena.Lambda('lambda_6945')
    def lambda_6945():
        ChrTurnDirection(0x000A, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6945)

    ChrTurnDirection(0x0101, 0x0009, 400)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS134._CH')
    OP_C5(0x01, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS204._CH')
    OP_C5(0x02, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS205._CH')
    OP_C5(0x03, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS206._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1500)

    SetMessageWindowPos(150, 50, -1, -1)
    TalkSetChrName('拉赛尔博士')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0540221256V#104F要设置的场所共有３处，\n',
            '都在蔡斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221257V#100F首先是托兰特平原北部外围\n',
            '的一处巨石堆积的场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(150, 50, -1, -1)
    TalkSetChrName('拉赛尔博士')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0540221258V#104F然后是卡鲁迪亚隧道的中间地带，\n',
            '大概就是从蔡斯方向出发，遇到的第一座桥那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(150, 50, -1, -1)
    TalkSetChrName('拉赛尔博士')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0540221259V#100F最后是雷斯顿要塞前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(150, 50, -1, -1)
    TalkSetChrName('拉赛尔博士')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0540221260V#101F──希望你们能将装置\n',
            '设置在以上３个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 1000, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010221261V#1006F#6P嗯……\n',
            '我们记住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221262V不过，设置测量仪…\n',
            '只需要将它放在那里就可以了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540221263V#102F#5P不，没那么简单。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221264V必须要将测定用的勘测针以正确的角度\n',
            '刺入地面，\n',
            '另外天线也需要手动设置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040221265V#030F#6P天线是导力通讯\n',
            '的装置吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221266V作用是要将勘测出的情报\n',
            '发送出去，没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540221267V#101F#5P喔，判断力很敏锐嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221268V#100F嗯，外设的天线会把测定出来的数值\n',
            '传送到演算导力器『卡佩尔』中，\n',
            '用以解析七耀脉的流动情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221269V卡佩尔会对３个地方的情况\n',
            '进行实时分析，\n',
            '因此应该可以得出正确的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221270V#1007F#6P嗯～似乎是很厉害的实验呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221271V#1011F那么，拉赛尔博士也要\n',
            '和我们同行，去进行装置的设置吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540221272V#100F#5P不，我还要进行『卡佩尔』\n',
            '的调整工作，实在没有空闲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221273V那件工作就让提妲替我去做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0070221274V#067F#2P嘿嘿嘿……\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7265',
    )

    ChrTalk(
        0x0101,
        (
            '#0010221275V#1006F#6P是吗。\n',
            '有提妲帮忙的话比一百人还要管用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010221276V#1019F#6P……阿加特。\n',
            '你没什么要说的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050221277V#053F#1P没办法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221278V#051F只是你可不能总\n',
            '陶醉在机械的世界里啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221279V要是还像以前那样动不动就发呆，\n',
            '也许被魔兽吃掉了还不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070221280V#562F#2P呜呜……\n',
            '阿加特哥哥又欺负人了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070221281V#560F可是～就算真的出现那种情况\n',
            '你也会保护我的对不对？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050221282V#551F#1P……真是的，这小鬼头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221283V#1001F#6P哈哈哈～\n',
            '阿加特果然还是败了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_735B')

    def _loc_7265(): pass

    label('loc_7265')

    ChrTalk(
        0x0101,
        (
            '#0010221275V#1006F#6P是吗。\n',
            '有提妲帮忙的话比一百人还要管用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010221285V#1011F#6P雪拉姐，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030221286V#021F#1P呵呵，那当然啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221287V#526F请多关照了，小提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070221288V#061F#2P是的，雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_735B(): pass

    label('loc_735B')

    TerminateThread(0x0101, 0xFF)
    ChrSetDirection(0x0101, 315, 400)
    ChrSetDirection(0x00F7, 0, 400)
    ChrSetDirection(0x000A, 270, 400)

    ChrTalk(
        0x0009,
        (
            '#0540221289V#100F#5P那么，我这就开始\n',
            '进行『卡佩尔』的输入调整了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540221290V你们把全部的测量仪设置完毕后\n',
            '就来中央工房的演算室找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221291V#1018F#6P嗯，明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_742F')
    def lambda_742F():
        ChrTurnDirection(0x000A, 0x0009, 400)
        Yield()

        Jump('lambda_742F')

    DispatchAsync2(0x000A, 0x0003, lambda_742F)

    ChrTalk(
        0x000A,
        (
            '#0070221292V#560F#2P爷爷也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 225, 400)

    @scena.Lambda('lambda_7471')
    def lambda_7471():
        CameraMove(1600, 0, -4670, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_7471)

    @scena.Lambda('lambda_7489')
    def lambda_7489():
        ChrTurnDirection(0x0101, 0x0009, 400)
        Yield()

        Jump('lambda_7489')

    DispatchAsync2(0x0101, 0x0003, lambda_7489)

    @scena.Lambda('lambda_749A')
    def lambda_749A():
        ChrTurnDirection(0x00F7, 0x0009, 400)
        Yield()

        Jump('lambda_749A')

    DispatchAsync2(0x00F7, 0x0003, lambda_749A)

    @scena.Lambda('lambda_74AB')
    def lambda_74AB():
        ChrTurnDirection(0x0105, 0x0009, 400)
        Yield()

        Jump('lambda_74AB')

    DispatchAsync2(0x0105, 0x0003, lambda_74AB)

    @scena.Lambda('lambda_74BC')
    def lambda_74BC():
        ChrTurnDirection(0x0104, 0x0009, 400)
        Yield()

        Jump('lambda_74BC')

    DispatchAsync2(0x0104, 0x0003, lambda_74BC)

    ChrWalkTo(0x0009, 1440, 0, -1690, 2500, 0x00)
    ChrWalkTo(0x0009, 1520, 0, -6320, 2500, 0x00)
    ChrWalkTo(0x0009, 1500, -500, -7180, 2500, 0x00)
    ChrSetFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_750E')
    def lambda_750E():
        ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_750E)

    ChrWalkTo(0x0009, 1560, -500, -8250, 2500, 0x00)
    ChrSetFlags(0x0009, 0x0080)
    WaitForThreadExit(0x0009, 0x0003)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x00F7, 0x03)
    TerminateThread(0x0105, 0x03)
    TerminateThread(0x0104, 0x03)
    TerminateThread(0x000A, 0x03)
    Sleep(500)

    @scena.Lambda('lambda_7557')
    def lambda_7557():
        CameraMove(3500, 0, -505, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_7557)

    @scena.Lambda('lambda_756F')
    def lambda_756F():
        ChrSetDirection(0x00F7, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_756F)

    @scena.Lambda('lambda_757D')
    def lambda_757D():
        ChrSetDirection(0x0105, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_757D)

    @scena.Lambda('lambda_758B')
    def lambda_758B():
        ChrSetDirection(0x0104, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_758B)

    @scena.Lambda('lambda_7599')
    def lambda_7599():
        ChrSetDirection(0x000A, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_7599)

    ChrSetDirection(0x0101, 270, 400)
    WaitForThreadExit(0x0009, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010221293V#1006F#6P一定要在下次地震发生之前\n',
            '将全部测量仪设置好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221294V我们马上出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_76B0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221295V#052F#5P哦，等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221296V#051F要一起行动的话\n',
            '人数似乎太多了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221297V在这里决定一下行动队员\n',
            '再决定比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7745')

    def _loc_76B0(): pass

    label('loc_76B0')

    ChrTalk(
        0x0103,
        (
            '#0030221298V#023F#5P啊，请稍等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221299V#020F这么多人一起行动的话\n',
            '似乎有些不便哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221300V在这里决定一下行动队员\n',
            '和待机队员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7745(): pass

    label('loc_7745')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※可以参加战斗的同行队员\n',
            '　最多只能有４位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '※今后，队伍成员超过４人的时候，\n',
            '　就需要在全部成员中\n',
            '　选出同行的角色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x000001F4)
    Sleep(500)

    FadeIn(0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7816',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    Jump('loc_7827')

    def _loc_7816(): pass

    label('loc_7816')

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    def _loc_7827(): pass

    label('loc_7827')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000A, 0x0080)
    CameraMove(2310, 0, -620, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x00F7, 3200, 0, -1260, 270)
    ChrSetPos(0x0101, 4240, 0, -1160, 270)
    ChrSetPos(0x0107, 4290, 0, -2310, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78DC',
    )

    ChrSetPos(0x000E, 1680, 0, -1990, 90)
    ChrSetPos(0x0105, 3020, 0, -2400, 270)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_7903')

    def _loc_78DC(): pass

    label('loc_78DC')

    ChrSetPos(0x000F, 1680, 0, -1990, 90)
    ChrSetPos(0x0104, 3020, 0, -2400, 270)
    ChrClearFlags(0x000F, 0x0080)

    def _loc_7903(): pass

    label('loc_7903')

    Sleep(500)

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A89',
    )

    ChrTalk(
        0x000E,
        (
            '#0040221301V#035F#5P呼～那么我暂且就在\n',
            '２楼优雅地休息一会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221302V#030F需要我这个天才帮忙的时候\n',
            '随时可以过来找我哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    @scena.Lambda('lambda_79B1')
    def lambda_79B1():
        ChrTurnDirection(0x0101, 0x000E, 400)
        Yield()

        Jump('lambda_79B1')

    DispatchAsync2(0x0101, 0x0003, lambda_79B1)

    @scena.Lambda('lambda_79C2')
    def lambda_79C2():
        ChrTurnDirection(0x00F7, 0x000E, 400)
        Yield()

        Jump('lambda_79C2')

    DispatchAsync2(0x00F7, 0x0003, lambda_79C2)

    @scena.Lambda('lambda_79D3')
    def lambda_79D3():
        ChrTurnDirection(0x0105, 0x000E, 400)
        Yield()

        Jump('lambda_79D3')

    DispatchAsync2(0x0105, 0x0003, lambda_79D3)

    @scena.Lambda('lambda_79E4')
    def lambda_79E4():
        ChrTurnDirection(0x0107, 0x000E, 400)
        Yield()

        Jump('lambda_79E4')

    DispatchAsync2(0x0107, 0x0003, lambda_79E4)

    ChrSetDirection(0x000E, 315, 500)

    @scena.Lambda('lambda_79FC')
    def lambda_79FC():
        CameraMove(1550, 0, 430, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_79FC)

    ChrSetFlags(0x000E, 0x0004)
    ChrWalkTo(0x000E, -1840, 0, 1310, 2500, 0x00)
    ChrWalkTo(0x000E, -1960, 0, 2450, 2500, 0x00)
    ChrSetDirection(0x000E, 90, 500)
    ChrClearFlags(0x000E, 0x0004)
    ChrWalkTo(0x000E, 2500, 2250, 2730, 2500, 0x00)

    @scena.Lambda('lambda_7A61')
    def lambda_7A61():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_7A61)

    ChrWalkTo(0x000E, 4000, 3500, 2460, 2500, 0x00)
    ChrSetFlags(0x000E, 0x0080)

    Jump('loc_7BD2')

    def _loc_7A89(): pass

    label('loc_7A89')

    ChrTalk(
        0x000F,
        (
            '#0060221303V#040F#5P明白了。\n',
            '我先在２楼待命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221304V#041F需要我出力的时候\n',
            '随时可以过来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    @scena.Lambda('lambda_7AFD')
    def lambda_7AFD():
        ChrTurnDirection(0x0101, 0x000F, 400)
        Yield()

        Jump('lambda_7AFD')

    DispatchAsync2(0x0101, 0x0003, lambda_7AFD)

    @scena.Lambda('lambda_7B0E')
    def lambda_7B0E():
        ChrTurnDirection(0x00F7, 0x000F, 400)
        Yield()

        Jump('lambda_7B0E')

    DispatchAsync2(0x00F7, 0x0003, lambda_7B0E)

    @scena.Lambda('lambda_7B1F')
    def lambda_7B1F():
        ChrTurnDirection(0x0104, 0x000F, 400)
        Yield()

        Jump('lambda_7B1F')

    DispatchAsync2(0x0104, 0x0003, lambda_7B1F)

    @scena.Lambda('lambda_7B30')
    def lambda_7B30():
        ChrTurnDirection(0x0107, 0x000F, 400)
        Yield()

        Jump('lambda_7B30')

    DispatchAsync2(0x0107, 0x0003, lambda_7B30)

    ChrSetDirection(0x000F, 315, 500)

    @scena.Lambda('lambda_7B48')
    def lambda_7B48():
        CameraMove(1550, 0, 430, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7B48)

    ChrSetFlags(0x000F, 0x0004)
    ChrWalkTo(0x000F, -1840, 0, 1310, 2500, 0x00)
    ChrWalkTo(0x000F, -1960, 0, 2450, 2500, 0x00)
    ChrSetDirection(0x000F, 90, 500)
    ChrClearFlags(0x000F, 0x0004)
    ChrWalkTo(0x000F, 2500, 2250, 2730, 2500, 0x00)

    @scena.Lambda('lambda_7BAD')
    def lambda_7BAD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_7BAD)

    ChrWalkTo(0x000F, 4000, 3500, 2460, 2500, 0x00)
    ChrSetFlags(0x000F, 0x0080)

    def _loc_7BD2(): pass

    label('loc_7BD2')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※不在队伍中的成员\n',
            '　会在协会的２楼待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '※通过对话，即可\n',
            '　随时更改\n',
            '　队伍内的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    @scena.Lambda('lambda_7C62')
    def lambda_7C62():
        CameraMove(3500, 0, -505, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7C62)

    TerminateThread(0x0101, 0x03)
    TerminateThread(0x00F7, 0x03)
    TerminateThread(0x00F9, 0x03)
    TerminateThread(0x0107, 0x03)

    @scena.Lambda('lambda_7C8A')
    def lambda_7C8A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_7C8A)

    @scena.Lambda('lambda_7C98')
    def lambda_7C98():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_7C98)

    @scena.Lambda('lambda_7CA6')
    def lambda_7CA6():
        ChrSetDirection(0x0107, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_7CA6)

    ChrSetDirection(0x0101, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010221305V#1006F#6P嗯，这就ＯＫ了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221306V#1015F嗯…测量仪需要设置在\n',
            '隧道途中、平原北部、\n',
            '雷斯顿要塞３个地方哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221307V哎～以什么顺序\n',
            '来设置比较好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580221308V#791F那就随便你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221309V雷斯顿要塞那边\n',
            '我会和他们联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580221310V到时你们只要把情况和门卫说一下，\n',
            '他应该就会允许你们在那里设置了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221311V#1006F#6P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7E36')
    def lambda_7E36():
        ChrSetDirection(0x00F7, 135, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_7E36)

    ChrSetDirection(0x0101, 270, 400)
    ChrSetDirection(0x0107, 315, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7EC7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221312V#051F#5P好，那我们马上出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221313V提妲。\n',
            '要跟上我们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070221314V#061F#6P好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F5A')

    def _loc_7EC7(): pass

    label('loc_7EC7')

    ChrTalk(
        0x0103,
        (
            '#0030221315V#020F#5P那么……\n',
            '我们这就出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221316V#021F小提妲。\n',
            '接下来就要看你的表现了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070221317V#560F#6P我、我会加油的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F5A(): pass

    label('loc_7F5A')

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0282, 7, 0x1417))
    OP_28(0x0087, 0x04, 0x02)
    OP_28(0x0087, 0x04, 0x08)
    OP_28(0x0087, 0x01, 0x0001)
    OP_28(0x0087, 0x01, 0x0002)
    OP_28(0x0087, 0x01, 0x0004)
    OP_28(0x0087, 0x01, 0x0008)
    OP_4B(0x0008, 255)
    CameraMove(3170, 0, -2350, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 3170, 0, -2350, 180)
    ChrSetPos(0x0001, 3170, 0, -2350, 180)
    ChrSetPos(0x0002, 3170, 0, -2350, 180)
    ChrSetPos(0x0003, 3170, 0, -2350, 180)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x803E
@scena.Code('func_17_803E')
def func_17_803E():
    ChrSetFlags(0x0101, 0x0004)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetPos(0x0101, 1480, -500, -8360, 0)
    ChrClearFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_806A')
    def lambda_806A():
        ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_806A)

    ChrWalkTo(0x00FE, 1550, -500, -7460, 2000, 0x00)
    ChrClearFlags(0x0101, 0x0004)
    ChrWalkTo(0x0101, 2420, 0, -4840, 2000, 0x00)
    ChrSetDirection(0x0101, 0, 0)

    Return()

# id: 0x0018 offset: 0x80AB
@scena.Code('func_18_80AB')
def func_18_80AB():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetRGBAMask(0x00F7, 255, 255, 255, 0, 0)
    ChrSetPos(0x00F7, 1480, -500, -8360, 0)
    ChrClearFlags(0x00F7, 0x0080)

    @scena.Lambda('lambda_80D7')
    def lambda_80D7():
        ChrSetRGBAMask(0x00F7, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_80D7)

    ChrWalkTo(0x00FE, 1550, -500, -7460, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00F7, 1360, 0, -4990, 2000, 0x00)
    ChrSetDirection(0x00F7, 0, 0)

    Return()

# id: 0x0019 offset: 0x8118
@scena.Code('func_19_8118')
def func_19_8118():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 0, 0)
    ChrSetPos(0x0105, 1480, -500, -8360, 0)
    ChrClearFlags(0x0105, 0x0080)

    @scena.Lambda('lambda_8144')
    def lambda_8144():
        ChrSetRGBAMask(0x0105, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_8144)

    ChrWalkTo(0x00FE, 1550, -500, -7460, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)
    ChrWalkTo(0x0105, 2270, 0, -5990, 2000, 0x00)
    ChrSetDirection(0x0105, 0, 0)

    Return()

# id: 0x001A offset: 0x8185
@scena.Code('func_1A_8185')
def func_1A_8185():
    ChrSetRGBAMask(0x0104, 255, 255, 255, 0, 0)
    ChrSetPos(0x0104, 1480, -500, -8360, 0)
    ChrClearFlags(0x0104, 0x0080)

    @scena.Lambda('lambda_81AC')
    def lambda_81AC():
        ChrSetRGBAMask(0x0104, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_81AC)

    ChrWalkTo(0x00FE, 1550, -500, -7460, 2000, 0x00)
    ChrWalkTo(0x0104, 1080, 0, -6180, 2000, 0x00)
    ChrSetDirection(0x0104, 0, 0)

    Return()

# id: 0x001B offset: 0x81E8
@scena.Code('func_1B_81E8')
def func_1B_81E8():
    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0151, 0x01)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8209',
    )

    RemoveItem(ItemTable['零力场发生器'], 1)

    Jump('loc_8722')

    def _loc_8209(): pass

    label('loc_8209')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8722',
    )

    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择取下零力场发生器的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x0, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8272',
    )

    Call(1, 0x001C)

    Jump('loc_8276')

    def _loc_8272(): pass

    label('loc_8272')

    Call(1, 0x001D)

    def _loc_8276(): pass

    label('loc_8276')

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x1, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x1, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_829D',
    )

    Call(1, 0x001C)

    Jump('loc_82A1')

    def _loc_829D(): pass

    label('loc_829D')

    Call(1, 0x001D)

    def _loc_82A1(): pass

    label('loc_82A1')

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x2, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x2, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_82C8',
    )

    Call(1, 0x001C)

    Jump('loc_82CC')

    def _loc_82C8(): pass

    label('loc_82C8')

    Call(1, 0x001D)

    def _loc_82CC(): pass

    label('loc_82CC')

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x3, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.GetChrWork, 0x3, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_82F3',
    )

    Call(1, 0x001C)

    Jump('loc_82F7')

    def _loc_82F3(): pass

    label('loc_82F3')

    Call(1, 0x001D)

    def _loc_82F7(): pass

    label('loc_82F7')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CC(0x02, 0x00)
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

    SetMessageWindowPos(72, 320, 56, 3)

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_833E'),
        (0x00000001, 'loc_8384'),
        (0x00000002, 'loc_83CA'),
        (0x00000003, 'loc_8410'),
        (-1, 'loc_8456'),
    )

    def _loc_833E(): pass

    label('loc_833E')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8361',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8381')

    def _loc_8361(): pass

    label('loc_8361')

    If(
        (
            (Expr.GetChrWork, 0x0, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8381',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8381(): pass

    label('loc_8381')

    Jump('loc_8456')

    def _loc_8384(): pass

    label('loc_8384')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83A7',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_83C7')

    def _loc_83A7(): pass

    label('loc_83A7')

    If(
        (
            (Expr.GetChrWork, 0x1, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83C7',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_83C7(): pass

    label('loc_83C7')

    Jump('loc_8456')

    def _loc_83CA(): pass

    label('loc_83CA')

    If(
        (
            (Expr.GetChrWork, 0x2, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83ED',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_840D')

    def _loc_83ED(): pass

    label('loc_83ED')

    If(
        (
            (Expr.GetChrWork, 0x2, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_840D',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_840D(): pass

    label('loc_840D')

    Jump('loc_8456')

    def _loc_8410(): pass

    label('loc_8410')

    If(
        (
            (Expr.GetChrWork, 0x3, 0x1F),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8433',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x1F,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8453')

    def _loc_8433(): pass

    label('loc_8433')

    If(
        (
            (Expr.GetChrWork, 0x3, 0x20),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8453',
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushValueByIndex, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x20,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8453(): pass

    label('loc_8453')

    Jump('loc_8456')

    def _loc_8456(): pass

    label('loc_8456')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_847F',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '未装备零力场发生器。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_847F(): pass

    label('loc_847F')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84C7',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_84C7(): pass

    label('loc_84C7')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_850D',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_850D(): pass

    label('loc_850D')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8555',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_8555(): pass

    label('loc_8555')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_859D',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奥利维尔已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_859D(): pass

    label('loc_859D')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_85E3',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_85E3(): pass

    label('loc_85E3')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8629',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特已取下零力场发生器，\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_8629(): pass

    label('loc_8629')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8694',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲已取下零力场发生器，\n',
            '无法使用魔法，战技，普通攻击。\n',
            '但Ｓ战技『炮射冲击』仍可使用。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_8694(): pass

    label('loc_8694')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86D4',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金已取下零力场发生器\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_8713')

    def _loc_86D4(): pass

    label('loc_86D4')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8713',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '凯文已取下零力场发生器\n',
            '所以暂时无法使用魔法。',
            TxtCtl.Enter,
        ),
    )

    def _loc_8713(): pass

    label('loc_8713')

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_8209')

    def _loc_8722(): pass

    label('loc_8722')

    Return()

# id: 0x001C offset: 0x8723
@scena.Code('func_1C_8723')
def func_1C_8723():
    Switch(
        (
            (Expr.PushReg, 0x5),
            Expr.Return,
        ),
        (0x00000000, 'loc_8750'),
        (0x00000001, 'loc_876B'),
        (0x00000002, 'loc_8784'),
        (0x00000003, 'loc_879F'),
        (0x00000004, 'loc_87BA'),
        (0x00000005, 'loc_87D3'),
        (0x00000006, 'loc_87EC'),
        (0x00000007, 'loc_8803'),
        (0x00000008, 'loc_8818'),
        (-1, 'loc_882F'),
    )

    def _loc_8750(): pass

    label('loc_8750')

    OP_CC(0x01, 0x00, '【艾丝蒂尔　装备中】')

    Jump('loc_882F')

    def _loc_876B(): pass

    label('loc_876B')

    OP_CC(0x01, 0x00, '【约修亚　装备中】')

    Jump('loc_882F')

    def _loc_8784(): pass

    label('loc_8784')

    OP_CC(0x01, 0x00, '【雪拉扎德　装备中】')

    Jump('loc_882F')

    def _loc_879F(): pass

    label('loc_879F')

    OP_CC(0x01, 0x00, '【奥利维尔　装备中】')

    Jump('loc_882F')

    def _loc_87BA(): pass

    label('loc_87BA')

    OP_CC(0x01, 0x00, '【科洛丝　装备中】')

    Jump('loc_882F')

    def _loc_87D3(): pass

    label('loc_87D3')

    OP_CC(0x01, 0x00, '【阿加特　装备中】')

    Jump('loc_882F')

    def _loc_87EC(): pass

    label('loc_87EC')

    OP_CC(0x01, 0x00, '【提妲　装备中】')

    Jump('loc_882F')

    def _loc_8803(): pass

    label('loc_8803')

    OP_CC(0x01, 0x00, '【金　装备中】')

    Jump('loc_882F')

    def _loc_8818(): pass

    label('loc_8818')

    OP_CC(0x01, 0x00, '【凯文　装备中】')

    Jump('loc_882F')

    def _loc_882F(): pass

    label('loc_882F')

    Return()

# id: 0x001D offset: 0x8830
@scena.Code('func_1D_8830')
def func_1D_8830():
    Switch(
        (
            (Expr.PushReg, 0x5),
            Expr.Return,
        ),
        (0x00000000, 'loc_885D'),
        (0x00000001, 'loc_8878'),
        (0x00000002, 'loc_8891'),
        (0x00000003, 'loc_88AC'),
        (0x00000004, 'loc_88C7'),
        (0x00000005, 'loc_88E0'),
        (0x00000006, 'loc_88F9'),
        (0x00000007, 'loc_8910'),
        (0x00000008, 'loc_8925'),
        (-1, 'loc_893C'),
    )

    def _loc_885D(): pass

    label('loc_885D')

    OP_CC(0x01, 0x00, '【艾丝蒂尔　未装备】')

    Jump('loc_893C')

    def _loc_8878(): pass

    label('loc_8878')

    OP_CC(0x01, 0x00, '【约修亚　未装备】')

    Jump('loc_893C')

    def _loc_8891(): pass

    label('loc_8891')

    OP_CC(0x01, 0x00, '【雪拉扎德　未装备】')

    Jump('loc_893C')

    def _loc_88AC(): pass

    label('loc_88AC')

    OP_CC(0x01, 0x00, '【奥利维尔　未装备】')

    Jump('loc_893C')

    def _loc_88C7(): pass

    label('loc_88C7')

    OP_CC(0x01, 0x00, '【科洛丝　未装备】')

    Jump('loc_893C')

    def _loc_88E0(): pass

    label('loc_88E0')

    OP_CC(0x01, 0x00, '【阿加特　未装备】')

    Jump('loc_893C')

    def _loc_88F9(): pass

    label('loc_88F9')

    OP_CC(0x01, 0x00, '【提妲　未装备】')

    Jump('loc_893C')

    def _loc_8910(): pass

    label('loc_8910')

    OP_CC(0x01, 0x00, '【金　未装备】')

    Jump('loc_893C')

    def _loc_8925(): pass

    label('loc_8925')

    OP_CC(0x01, 0x00, '【凯文　未装备】')

    Jump('loc_893C')

    def _loc_893C(): pass

    label('loc_893C')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
