import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0012_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0012_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0012.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x127B
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 29200, 0, -7430, 270)
    SetChrPos(0x0102, 30010, 0, -8090, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F2',
    )

    SetChrPos(0x0107, 29960, 0, -6410, 225)

    def _loc_F2(): pass

    label('loc_F2')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_111',
    )

    SetChrPos(0x0106, 31010, 0, -7540, 270)

    def _loc_111(): pass

    label('loc_111')

    CameraMove(28990, 0, -7070, 2000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010180494V#000F菲小姐，\n',
            '打扰一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000A, 0x0010)
    TalkBegin(0x000A)
    OP_4A(0x000A, 255)
    ClearChrFlags(0x000A, 0x0010)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180495V嗯？什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180496V#000F在你正忙的时候来打扰真是抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180497V#000F这是某人托我们带给您的东西。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180444V这个，请您收下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '给菲的情书',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    RemoveItem(0x035E, 1)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1980180499V这封信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180500V…………难道说，\n',
            '是沃尔费堡垒的布拉姆写的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160314V#000F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180502V#002F（好！\n',
            '　这就把礼物拿给她。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_39E',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180482V#008F（……哎呀，虽然心里一直惦记着，\n',
            '　最后还是忘记买礼物了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_7BA')

    def _loc_39E(): pass

    label('loc_39E')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_428',
    )

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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_419'),
        (0x00000001, 'loc_41F'),
        (-1, 'loc_425'),
    )

    def _loc_419(): pass

    label('loc_419')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_425')

    def _loc_41F(): pass

    label('loc_41F')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_425')

    def _loc_425(): pass

    label('loc_425')

    Jump('loc_7BA')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B0',
    )

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
            TXT(0x00, '【果馅饼】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_4A1'),
        (0x00000001, 'loc_4A7'),
        (-1, 'loc_4AD'),
    )

    def _loc_4A1(): pass

    label('loc_4A1')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_4AD')

    def _loc_4A7(): pass

    label('loc_4A7')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_4AD')

    def _loc_4AD(): pass

    label('loc_4AD')

    Jump('loc_7BA')

    def _loc_4B0(): pass

    label('loc_4B0')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_53C',
    )

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
            TXT(0x00, '【绒毛编织帽】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_52D'),
        (0x00000001, 'loc_533'),
        (-1, 'loc_539'),
    )

    def _loc_52D(): pass

    label('loc_52D')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_539')

    def _loc_533(): pass

    label('loc_533')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_539')

    def _loc_539(): pass

    label('loc_539')

    Jump('loc_7BA')

    def _loc_53C(): pass

    label('loc_53C')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DA',
    )

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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【果馅饼】\n'),
            TXT(0x02, '【放弃】\n'),
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
        (0x00000000, 'loc_5C5'),
        (0x00000001, 'loc_5CB'),
        (0x00000002, 'loc_5D1'),
        (-1, 'loc_5D7'),
    )

    def _loc_5C5(): pass

    label('loc_5C5')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_5D7')

    def _loc_5CB(): pass

    label('loc_5CB')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_5D7')

    def _loc_5D1(): pass

    label('loc_5D1')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_5D7')

    def _loc_5D7(): pass

    label('loc_5D7')

    Jump('loc_7BA')

    def _loc_5DA(): pass

    label('loc_5DA')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_67C',
    )

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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【绒毛编织帽】\n'),
            TXT(0x02, '【放弃】\n'),
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
        (0x00000000, 'loc_667'),
        (0x00000001, 'loc_66D'),
        (0x00000002, 'loc_673'),
        (-1, 'loc_679'),
    )

    def _loc_667(): pass

    label('loc_667')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_679')

    def _loc_66D(): pass

    label('loc_66D')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_679')

    def _loc_673(): pass

    label('loc_673')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_679')

    def _loc_679(): pass

    label('loc_679')

    Jump('loc_7BA')

    def _loc_67C(): pass

    label('loc_67C')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_71C',
    )

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
            TXT(0x00, '【果馅饼】\n'),
            TXT(0x01, '【绒毛编织帽】\n'),
            TXT(0x02, '【放弃】\n'),
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
        (0x00000000, 'loc_707'),
        (0x00000001, 'loc_70D'),
        (0x00000002, 'loc_713'),
        (-1, 'loc_719'),
    )

    def _loc_707(): pass

    label('loc_707')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_719')

    def _loc_70D(): pass

    label('loc_70D')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_719')

    def _loc_713(): pass

    label('loc_713')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_719')

    def _loc_719(): pass

    label('loc_719')

    Jump('loc_7BA')

    def _loc_71C(): pass

    label('loc_71C')

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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【果馅饼】\n'),
            TXT(0x02, '【绒毛编织帽】\n'),
            TXT(0x03, '【放弃】\n'),
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
        (0x00000000, 'loc_7A5'),
        (0x00000001, 'loc_7A8'),
        (0x00000002, 'loc_7AE'),
        (0x00000003, 'loc_7B4'),
        (-1, 'loc_7BA'),
    )

    def _loc_7A5(): pass

    label('loc_7A5')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_7A8(): pass

    label('loc_7A8')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_7BA')

    def _loc_7AE(): pass

    label('loc_7AE')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_7BA')

    def _loc_7B4(): pass

    label('loc_7B4')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_7BA')

    def _loc_7BA(): pass

    label('loc_7BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_A7F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180449V#000F对了，\n',
            '这是他送你的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '工作手套',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1980180504V……礼物？\n',
            '工作手套？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180505V好、好吧，\n',
            '我收下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 270, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180506V哼，真是的，\n',
            '那个家伙到底在想什么，\n',
            '我一点都不明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180507V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180454V#509F（唔…………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180455V（这、这个礼物\n',
            '　好像失败了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    SetChrDirection(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980180510V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180511V现在不是\n',
            '说这种话的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180512V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180513V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180459V#506F啊……嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x014D, 1)
    OP_28(0x0031, 0x01, 0x0040)
    OP_2B(0x0031, 0x0002)

    Jump('loc_120A')

    def _loc_A7F(): pass

    label('loc_A7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_D51',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180449V#000F对了，\n',
            '这是他送你的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '果馅饼',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_62(0x00FE, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1980180516V谢、谢谢了。\n',
            '我很高兴…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180517V不过我最近要\n',
            '控制甜食的数量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180518V尽管这样，\n',
            '却送这样的礼物给我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 270, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180519V哼！他不懂得体贴别人这点\n',
            '看来还是完全没变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180507V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180454V#509F（唔…………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180455V（这、这个礼物\n',
            '　好像失败了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    SetChrDirection(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980180510V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180511V现在不是\n',
            '说这种话的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180512V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180513V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x01B2, 1)
    OP_28(0x0031, 0x01, 0x0080)
    OP_2B(0x0031, 0x0002)

    Jump('loc_120A')

    def _loc_D51(): pass

    label('loc_D51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_FBF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180449V#506F啊……嗯，再见。\n',
            '这是他送你的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '绒毛编织帽',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1980180528V哇，好可爱呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180507V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180530V哎呀，\n',
            '他总算是稍微……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180531V……开始为我着想了呢。\n',
            '呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180532V不过既然知道该这样，\n',
            '为什么不早点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180507V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980180510V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180511V现在不是\n',
            '说这种话的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180512V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180513V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160346V#000F嗯，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x014A, 1)
    OP_28(0x0031, 0x01, 0x0020)
    OP_2B(0x0031, 0x0004)

    Jump('loc_120A')

    def _loc_FBF(): pass

    label('loc_FBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_FFB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180483V#505F（……唔～\n',
            '　没有看到合适的礼物。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FFB(): pass

    label('loc_FFB')

    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980180541V呼～这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180542V那家伙啊，\n',
            '肯定是已经反省过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 270, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180543V不过，\n',
            '就算他现在想到要写封信给我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180507V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180454V#509F（唔…………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180489V（果然还是应该送点礼物才行……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    SetChrDirection(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980180510V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180511V现在不是\n',
            '说这种话的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180512V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180513V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180459V#506F啊……嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0031, 0x01, 0x0100)

    def _loc_120A(): pass

    label('loc_120A')

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【爱之使者】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x035E, 1)
    OP_28(0x0031, 0x04, 0x10)
    OP_28(0x0031, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    Sleep(50)

    EventEnd(0x04)
    OP_4B(0x000A, 255)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
