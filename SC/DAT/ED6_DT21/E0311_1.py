import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0311_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0311_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0311.x'
    header.mapIndex       = 1
    header.bgm            = 116
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/E0311._SN', 'ED6_DT21/E0311_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BB',
    )

    TalkBegin(0x00FE)

    Jump('loc_1B2')

    def _loc_BB(): pass

    label('loc_BB')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_14B',
    )

    Jump('loc_18D')

    def _loc_14B(): pass

    label('loc_14B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_167',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_18D')

    def _loc_167(): pass

    label('loc_167')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_183',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_18D')

    def _loc_183(): pass

    label('loc_183')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_18D(): pass

    label('loc_18D')

    ExecExpressionWithValue(
        0x00FE,
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
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0010)

    def _loc_1B2(): pass

    label('loc_1B2')

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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_210'),
        (0x00000001, 'loc_118A'),
        (0x00000002, 'loc_11BE'),
        (-1, 'loc_11C1'),
    )

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_809',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 0, 0x22A0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4BE',
    )

    ChrTurnDirection(0x0008, 0x010B, 0)

    ChrTalk(
        0x0008,
        (
            '#0030390542V#021F哎呀，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390543V#021F呵呵，想不到会以\n',
            '这种方式重逢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390544V#214F这话是我要说的才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390545V真是的，一有什么事\n',
            '你就拿出鞭子来抽人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390546V#027F我只是稍微\n',
            '疼爱你一下而已嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390547V#525F如果你喜欢被抽的话，\n',
            '下次要不要再用力一点呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390548V#216F从、从你嘴里说出来，\n',
            '就不像是在开玩笑了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390549V#413F总、总之……\n',
            '既然已经到了这个地步，\n',
            '我们就没什么好说的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390550V#020F若是互相仇视的话，\n',
            '只是在帮结社的忙而已呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390551V不如我们暂时停战吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390552V就让我期待\n',
            '你的作战能力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390553V#210F哼哼……\n',
            '你、你等着瞧好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 0)
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x0454, 0, 0x22A0))

    Jump('loc_806')

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54E',
    )

    ChrTurnDirection(0x0008, 0x010B, 0)

    ChrTalk(
        0x0008,
        (
            '#0030390554V#020F嗯嗯，既然如此，\n',
            '从前的事情就不必再提。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390555V我们就彼此合作、\n',
            '一起对抗结社吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 0)

    Jump('loc_806')

    def _loc_54E(): pass

    label('loc_54E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_710',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_650',
    )

    ChrTalk(
        0x0008,
        (
            '#0030390556V#027F左舷的回收如果成功的话，\n',
            '修理作业似乎就算大致完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390557V我们也在等待\n',
            '回收的结果如何。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390558V#026F真希望你们探索回来时,\n',
            '就能够飞起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390559V#525F总之只能相信拉赛尔博士,\n',
            '然后等待结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_70D')

    def _loc_650(): pass

    label('loc_650')

    ChrTalk(
        0x0008,
        (
            '#0030390556V#027F左舷的回收如果成功的话，\n',
            '修理作业似乎就算大致完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390561V希望等你们探索回来时,\n',
            '就能够飞起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390559V#525F总之只能相信拉赛尔博士,\n',
            '然后等待结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70D(): pass

    label('loc_70D')

    Jump('loc_806')

    def _loc_710(): pass

    label('loc_710')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B2',
    )

    ChrTalk(
        0x0008,
        (
            '#0030390563V#020F呼，照明总算\n',
            '顺利恢复了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390564V但愿工程能够\n',
            '因此有所进展……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390565V那么，我也该去找一些\n',
            '力所能及的事情来做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_806')

    def _loc_7B2(): pass

    label('loc_7B2')

    ChrTalk(
        0x0008,
        (
            '#0030390566V#020F照明顺利恢复了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390567V但愿工程能够\n',
            '因此有所进展……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_806(): pass

    label('loc_806')

    Jump('loc_1187')

    def _loc_809(): pass

    label('loc_809')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_B0C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 0, 0x22A0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A8A',
    )

    ChrTalk(
        0x0008,
        (
            '#0030390568V#020F呵呵，想不到会以\n',
            '这种方式重逢呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390569V#210F哼，这是我该说的才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390545V真是的，一有什么事\n',
            '你就拿出鞭子来抽人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390573V#020F哎呀？我只是稍微\n',
            '疼爱你一下而已嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390574V如果你喜欢被抽的话，\n',
            '下次我也可以令你如愿以偿哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390571V#210F从、从你嘴里说出来，\n',
            '就不像是在开玩笑了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390572V总、总之……\n',
            '既然已经到了这个地步，\n',
            '我们就没什么好说的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390550V#020F若是互相仇视的话，\n',
            '只是在帮结社的忙而已呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390551V不如我们暂时停战吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390552V就让我期待\n',
            '你的作战能力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390553V#210F哼哼……\n',
            '你、你等着瞧好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x0454, 0, 0x22A0))

    Jump('loc_B09')

    def _loc_A8A(): pass

    label('loc_A8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_B01',
    )

    ChrTalk(
        0x0008,
        (
            '#0030390579V#020F嗯嗯，既然如此，\n',
            '从前的事情就不必再提。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390555V我们就彼此合作、\n',
            '一起对抗结社吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B09')

    def _loc_B01(): pass

    label('loc_B01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 4, 0x22C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B09',
    )

    def _loc_B09(): pass

    label('loc_B09')

    Jump('loc_1187')

    def _loc_B0C(): pass

    label('loc_B0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_B16',
    )

    Jump('loc_1187')

    def _loc_B16(): pass

    label('loc_B16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_F39',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C9, 2, 0x1E4A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E9E',
    )

    ChrTalk(
        0x0008,
        (
            '#0030340460V#026F还剩下一座塔……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340461V虽然还不清楚敌人的目的，\n',
            '不过肯定快要接近尾声了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340462V#1002F嗯……\n',
            '确实是这样。',
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
        'loc_C38',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340463V#050F总之结果就留到\n',
            '以后去分析吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340464V目前必须先前往最后那座塔\n',
            '阻止他们的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBA')

    def _loc_C38(): pass

    label('loc_C38')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340465V#070F不过，现在分析结果\n',
            '还为时过早吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340466V目前必须先前往最后那座塔\n',
            '阻止结社的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBA')

    def _loc_CB8(): pass

    label('loc_CB8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D39',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340467V#1060F不过，现在考虑结果\n',
            '还为时过早吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340468V目前必须先前往最后那座塔\n',
            '阻止他们的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBA')

    def _loc_D39(): pass

    label('loc_D39')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DBA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340469V#042F不过，现在分析结果\n',
            '或许还为时过早呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340470V目前必须先前往最后那座塔\n',
            '阻止结社的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DBA(): pass

    label('loc_DBA')

    ChrTalk(
        0x0008,
        (
            '#0030340471V#020F嗯，没错。\n',
            '今后再去分析也不迟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340472V#1035F为了将来不会后悔，\n',
            '现在应该迅速行动才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340473V#1015F终于到最后的塔了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340474V#1002F加上还有玲这个敌人，\n',
            '大家提高警觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x03C9, 2, 0x1E4A))

    Jump('loc_F36')

    def _loc_E9E(): pass

    label('loc_E9E')

    ChrTalk(
        0x0008,
        (
            '#0030340475V#026F塔也只剩下一座了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340476V#022F虽然还不清楚敌人的目的，\n',
            '不过肯定快要接近尾声了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340477V你们一路上\n',
            '也要提高警觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_F36(): pass

    label('loc_F36')

    Jump('loc_1187')

    def _loc_F39(): pass

    label('loc_F39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_F43',
    )

    Jump('loc_1187')

    def _loc_F43(): pass

    label('loc_F43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_1187',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C9, 1, 0x1E49)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1124',
    )

    ChrTalk(
        0x0008,
        (
            '#0030340478V#020F看来这次要轮到金先生出场了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340479V#025F呼，真遗憾。\n',
            '没有人陪我一起喝酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080340480V#071F哈哈，抱歉。\n',
            '等回来后再奉陪你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340481V#1019F喝酒是无所谓，不过雪拉姐，\n',
            '你可别一时大意喝多了哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340482V说不定之后\n',
            '还有你出场的机会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030340483V#525F呵呵，没问题啦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340484V葡萄酒是\n',
            '醉不倒我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340485V#1016F嗯、嗯……\n',
            '我可没在说酒的种类的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340486V#1048F感觉又被混过去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x03C9, 1, 0x1E49))

    Jump('loc_1187')

    def _loc_1124(): pass

    label('loc_1124')

    ChrTalk(
        0x0008,
        (
            '#0030340487V#020F那么，你们\n',
            '一路上要小心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340488V我在会这里待命，\n',
            '需要的时候就叫我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1187(): pass

    label('loc_1187')

    Jump('loc_11C4')

    def _loc_118A(): pass

    label('loc_118A')

    ChrTalk(
        0x0008,
        (
            '#0030340489V#020F哎呀，要更换成员了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0005)

    Jump('loc_11C4')

    def _loc_11BE(): pass

    label('loc_11BE')

    Jump('loc_11C4')

    def _loc_11C1(): pass

    label('loc_11C1')

    Jump('loc_11C4')

    def _loc_11C4(): pass

    label('loc_11C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11D6',
    )

    TalkEnd(0x00FE)

    Jump('loc_11DE')

    def _loc_11D6(): pass

    label('loc_11D6')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    def _loc_11DE(): pass

    label('loc_11DE')

    Return()

# id: 0x0002 offset: 0x11DF
@scena.Code('func_02_11DF')
def func_02_11DF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1C3F',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1276',
    )

    Jump('loc_12B8')

    def _loc_1276(): pass

    label('loc_1276')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1292',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_12B8')

    def _loc_1292(): pass

    label('loc_1292')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_12AE',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_12B8')

    def _loc_12AE(): pass

    label('loc_12AE')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_12B8(): pass

    label('loc_12B8')

    ExecExpressionWithValue(
        0x00FE,
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
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0010)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_133B'),
        (0x00000001, 'loc_1BE9'),
        (0x00000002, 'loc_1C2E'),
        (-1, 'loc_1C31'),
    )

    def _loc_133B(): pass

    label('loc_133B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 2, 0x2232)),
            Expr.Return,
        ),
        'loc_17D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 7, 0x223F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1626',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 6, 0x229E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_159C',
    )

    ChrTalk(
        0x0009,
        (
            '#0040390581V#031F哟，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390582V你们漂亮地战胜了\n',
            '『怪盗绅士』嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390583V#1002F嗯，好不容易呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390584V#1007F虽然最后还是\n',
            '和以前一样地被他逃掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390585V#1040F不过，我们确实\n',
            '已经击败了他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390586V应该不必担心\n',
            '他会继续介入了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390587V#035F呼……\n',
            '虽然是敌人，但也让人佩服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390588V不过，我还真想和他\n',
            '将来在某处再次相逢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390589V哪方才是真正理解美的人，\n',
            '一定要一决雌雄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390590V#1015F随便你吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390591V#1019F不过拜托别给\n',
            '其它人添麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1596',
    )

    ChrTalk(
        0x0110,
        (
            '#0110390592V#272F<FIXME>……同感だ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1596(): pass

    label('loc_1596')

    SetScenaFlags(ScenaFlag(0x0453, 6, 0x229E))

    Jump('loc_1623')

    def _loc_159C(): pass

    label('loc_159C')

    ChrTalk(
        0x0009,
        (
            '#0040390593V#031F如此漂亮的告别手法，\n',
            '果然不负『怪盗绅士』之名。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390594V呼，真不愧是我的宿敌……\n',
            '虽然是敌人，但也让人佩服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1623(): pass

    label('loc_1623')

    Jump('loc_17D3')

    def _loc_1626(): pass

    label('loc_1626')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1750',
    )

    ChrTalk(
        0x0009,
        (
            '#0040390595V#035F看来『怪盗绅士』\n',
            '应该不会再插手战斗了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390588V不过，我还真想和他\n',
            '将来在某处再次相逢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390589V哪方才是真正理解美的人，\n',
            '一定要一决雌雄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_171C',
    )

    ChrTalk(
        0x0110,
        (
            '#0110390598V#272F<FIXME>（……やはり同類か。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_171C(): pass

    label('loc_171C')

    ChrTalk(
        0x0101,
        (
            '#0010390599V#1019F（变态宝座决定战……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_17D3')

    def _loc_1750(): pass

    label('loc_1750')

    ChrTalk(
        0x0009,
        (
            '#0040390600V#035F还真想和『怪盗绅士』\n',
            '将来在某处再次相逢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390601V究竟谁才是真正理解美学的人，\n',
            '下次一定要决出胜负才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_17D3(): pass

    label('loc_17D3')

    Jump('loc_1BE6')

    def _loc_17D6(): pass

    label('loc_17D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1BE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1978',
    )

    ChrSetSubChip(0x0009, 0)

    ChrTalk(
        0x000B,
        (
            '#0080390602V#070F虽然想过将来有一天\n',
            '还能像这样子喝酒……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390603V不过你们这么快就回来了\n',
            '总觉得喝起来有点不够劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390604V#031F呼，本来还真想\n',
            '让他稍微再焦急一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390605V不过宰相大人比我想象的还要性急呢。\n',
            '这样一来就不能再继续拖延下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080390606V#075F真是的，不过想不到\n',
            '这样的人居然会是皇子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390607V帝国的臣民\n',
            '真令人同情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_1A40')

    def _loc_1978(): pass

    label('loc_1978')

    ChrTalk(
        0x0009,
        (
            '#0040390608V#035F可以的话，我还真想\n',
            '让他稍微再焦急一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390609V不过宰相大人比我想象的还要性急呢。\n',
            '这样一来就不能再继续拖延下去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390610V无法上演感动的会面，\n',
            '实在是相当没有面子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A40(): pass

    label('loc_1A40')

    Jump('loc_1BE6')

    def _loc_1A43(): pass

    label('loc_1A43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B71',
    )

    ChrTalk(
        0x0009,
        (
            '#0040390611V#030F看来我们的旅程\n',
            '也已经进入最后乐章了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390612V呵呵，我满心期待着\n',
            '适合点缀最后一幕的终曲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390613V#037F等一切都料理妥当后\n',
            '就去格兰赛尔城开场派对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390614V那次晚餐会的怨念……\n',
            '这一次我一定要发泄出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390615V#1016F想、想不到你还真会记恨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_1BE6')

    def _loc_1B71(): pass

    label('loc_1B71')

    ChrTalk(
        0x0009,
        (
            '#0040390611V#030F看来我们的旅程\n',
            '也已经进入最后乐章了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390617V呵呵，我满心期待着\n',
            '适合点缀最后一幕的终曲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BE6(): pass

    label('loc_1BE6')

    Jump('loc_1C34')

    def _loc_1BE9(): pass

    label('loc_1BE9')

    ChrTalk(
        0x0009,
        (
            '#0040310432V#035F呵呵，看来你们需要\n',
            '我这个天才的力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0005)

    Jump('loc_1C34')

    def _loc_1C2E(): pass

    label('loc_1C2E')

    Jump('loc_1C34')

    def _loc_1C31(): pass

    label('loc_1C31')

    Jump('loc_1C34')

    def _loc_1C34(): pass

    label('loc_1C34')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_252A')

    def _loc_1C3F(): pass

    label('loc_1C3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_1EA1',
    )

    TalkBegin(0x00FE)
    CreateThread(0x0009, 0x00, 0x00, 0x0003)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_1CAE'),
        (0x00000001, 'loc_1E50'),
        (0x00000002, 'loc_1E95'),
        (-1, 'loc_1E98'),
    )

    def _loc_1CAE(): pass

    label('loc_1CAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DCE',
    )

    ChrTalk(
        0x0009,
        (
            '#0040310425V#035F哟，各位好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310426V你们还喜欢\n',
            '我的鲁特琴演奏吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310427V#1019F真是的，也不看看时候……\n',
            '你怎么还这么悠闲自在的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310428V#035F呵呵，我是想给在这里休息的\n',
            '人们提供安宁的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310429V探索的准备我也做好了，\n',
            '你们就放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_1E4D')

    def _loc_1DCE(): pass

    label('loc_1DCE')

    ChrTalk(
        0x0009,
        (
            '#0040310430V#035F我是想为在休息室里休息的\n',
            '人们提供心灵上更深层的宁静……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310431V呼，这就是我们诗人\n',
            '所背负的使命哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E4D(): pass

    label('loc_1E4D')

    Jump('loc_1E9B')

    def _loc_1E50(): pass

    label('loc_1E50')

    ChrTalk(
        0x0009,
        (
            '#0040310432V#035F呵呵，看来你们需要\n',
            '我这个天才的力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0005)

    Jump('loc_1E9B')

    def _loc_1E95(): pass

    label('loc_1E95')

    Jump('loc_1E9B')

    def _loc_1E98(): pass

    label('loc_1E98')

    Jump('loc_1E9B')

    def _loc_1E9B(): pass

    label('loc_1E9B')

    TalkEnd(0x00FE)

    Jump('loc_252A')

    def _loc_1EA1(): pass

    label('loc_1EA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_252A',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1F38',
    )

    Jump('loc_1F7A')

    def _loc_1F38(): pass

    label('loc_1F38')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F54',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F7A')

    def _loc_1F54(): pass

    label('loc_1F54')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1F70',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F7A')

    def _loc_1F70(): pass

    label('loc_1F70')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F7A(): pass

    label('loc_1F7A')

    ExecExpressionWithValue(
        0x00FE,
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
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 0, 0x1A20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2455',
    )

    ChrTalk(
        0x0009,
        (
            '#0040310433V#030F哟，艾丝蒂尔。\n',
            '你在舰内散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310434V#1011F嗯，算是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310435V#1019F对了，我说你……\n',
            '作战前怎么还在喝酒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310436V#035F呼，这是提前庆祝的酒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310437V庆祝天才诗人和传说中的\n',
            '龙之间命运的邂逅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310438V#1015F先不提什么天才诗人……\n',
            '传说中的…………龙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310439V#1000F难道帝国也有\n',
            '龙的传说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310440V#031F嗯，当然有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310441V在离柏斯不远的南部地区\n',
            '就有很多龙的传说和目击传闻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310442V『百日战役』之前，\n',
            '在帝国科学院的号召下，\n',
            '还曾经组织规划了调查队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310443V#1004F哦～好正式啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310444V对帝国人来说，古代龙\n',
            '果然也是未知的存在呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310445V#030F嗯，你大体上\n',
            '可以这么认为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310446V不过，帝国人的想法\n',
            '却更为干脆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310447V#1011F干脆……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310448V#030F也就是说与利贝尔王国\n',
            '相较之下还要更加现实哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310449V这次的事件如果发生在帝国，\n',
            '肯定会立即下达捕杀的命令吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310450V#035F因为坚决抵抗外敌\n',
            '是帝国人一贯的做法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310451V管他是龙还是什么的，\n',
            '一律都要统统消灭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310452V#1016F感、感觉杀气腾腾的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310453V#034F毕竟以武力来安邦，\n',
            '是埃雷波尼亚帝国的风格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310454V这对于身为爱与和平使者的诗人来说\n',
            '是略感悲哀遗憾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0344, 0, 0x1A20))

    Jump('loc_2522')

    def _loc_2455(): pass

    label('loc_2455')

    ChrTalk(
        0x0009,
        (
            '#0040310455V#035F虽然龙逃往帝国\n',
            '也是个相当有意思的情节……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310456V#030F不过一旦成为现实，或许会被\n',
            '尽可能地当成新纷争的借口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310457V摩尔根将军应该也是再三考虑过\n',
            '这种状况后才进行指挥的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2522(): pass

    label('loc_2522')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    def _loc_252A(): pass

    label('loc_252A')

    Return()

# id: 0x0003 offset: 0x252B
@scena.Code('func_03_252B')
def func_03_252B():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_25BB',
    )

    Jump('loc_25FD')

    def _loc_25BB(): pass

    label('loc_25BB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_25D7',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_25FD')

    def _loc_25D7(): pass

    label('loc_25D7')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_25F3',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_25FD')

    def _loc_25F3(): pass

    label('loc_25F3')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_25FD(): pass

    label('loc_25FD')

    ExecExpressionWithValue(
        0x00FE,
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
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0010)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_2680'),
        (0x00000001, 'loc_369E'),
        (0x00000002, 'loc_36CA'),
        (-1, 'loc_36CD'),
    )

    def _loc_2680(): pass

    label('loc_2680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_2A1A',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2886',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2818',
    )

    ChrSetSubChip(0x000B, 0)

    ChrTalk(
        0x000B,
        (
            '#0080390602V#070F虽然想过将来有一天\n',
            '还能像这样子喝酒……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390603V不过你们这么快就回来了\n',
            '总觉得喝起来有点不够劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390604V#031F呼，本来还真想\n',
            '让他稍微再焦急一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390605V不过宰相大人比我想象的还要性急呢。\n',
            '这样一来就不能再继续拖延下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080390606V#075F真是的，不过想不到\n',
            '这样的人居然会是皇子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390607V帝国的臣民\n',
            '真令人同情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_2883')

    def _loc_2818(): pass

    label('loc_2818')

    ChrTalk(
        0x000B,
        (
            '#0080390625V#075F真是的……\n',
            '这样的人居然会是皇子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390626V真不禁要为帝国的\n',
            '臣民流下同情的眼泪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2883(): pass

    label('loc_2883')

    Jump('loc_2A17')

    def _loc_2886(): pass

    label('loc_2886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2990',
    )

    ChrTalk(
        0x000B,
        (
            '#0080390627V#070F哎呀哎呀，终于可以在船内\n',
            '放松休息一下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390628V#072F不过，我们的工作\n',
            '恐怕从现在起才正式开始吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390629V在中枢塔之中应该会接连\n',
            '遭遇到比以往更严酷的战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390630V万一遇到什么危险的话，\n',
            '不要勉强，先回到这里再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_2A17')

    def _loc_2990(): pass

    label('loc_2990')

    ChrTalk(
        0x000B,
        (
            '#0080390631V#072F在中枢塔之中应该会接连\n',
            '遭遇到比以往更严酷的战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390630V万一遇到什么危险的话，\n',
            '不要勉强，先回到这里再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A17(): pass

    label('loc_2A17')

    Jump('loc_369B')

    def _loc_2A1A(): pass

    label('loc_2A1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_2BCC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B4A',
    )

    ChrTalk(
        0x000B,
        (
            '#0080340490V#072F最后等待着我们的执行者是\n',
            '『歼灭天使』玲啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340491V她那一套将我们玩弄于\n',
            '股掌的纯熟手段，\n',
            '实在无法想象是如何学来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340492V#572F那个女孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340493V说不定背负着\n',
            '不简单的过去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340494V毕竟要获得强大的力量，\n',
            '就必须付出相应的代价才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_2BC9')

    def _loc_2B4A(): pass

    label('loc_2B4A')

    ChrTalk(
        0x000B,
        (
            '#0080340495V#072F她那一套将我们玩弄于股掌的纯熟手段，\n',
            '实在无法想象是如何学来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340496V说不定背负着\n',
            '不简单的过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BC9(): pass

    label('loc_2BC9')

    Jump('loc_369B')

    def _loc_2BCC(): pass

    label('loc_2BCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_2E55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 3, 0x1E43)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DD7',
    )

    ChrTalk(
        0x000B,
        (
            '#0080340497V#070F哦，你们几个要\n',
            '进入下一座塔了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340498V#1040F嗯，做好准备就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340499V#1011F金先生正在\n',
            '稍做休息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080340500V#070F嗯，老实说\n',
            '我是很想休息一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340501V不过现在可不是时候。\n',
            '你们需要的话我就马上出动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030340502V#021F呵呵，不用勉强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340503V你已经击退了那个瓦鲁特，\n',
            '就稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340504V#1040F嗯，不能勉强自己哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080340505V#070F哈哈，谢谢大家的关心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340506V不过你们不用客气。\n',
            '需要帮忙的话请尽管开口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x03C8, 3, 0x1E43))

    Jump('loc_2E52')

    def _loc_2DD7(): pass

    label('loc_2DD7')

    ChrTalk(
        0x000B,
        (
            '#0080340507V#070F说实话是想休息一下，\n',
            '不过现在可不是时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340508V需要我的拳头帮忙时，\n',
            '不用客气，叫我一声就行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E52(): pass

    label('loc_2E52')

    Jump('loc_369B')

    def _loc_2E55(): pass

    label('loc_2E55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_2E5F',
    )

    Jump('loc_369B')

    def _loc_2E5F(): pass

    label('loc_2E5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_369B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 0, 0x1E28)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3636',
    )

    ChrTalk(
        0x000B,
        (
            '#0080340509V#070F哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F06',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340510V#020F咦，今天是一个人吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340511V一个人静静地喝酒，\n',
            '在你身上还真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FB6')

    def _loc_2F06(): pass

    label('loc_2F06')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F79',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340512V#051F哎，今天是一个人哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340513V一个人静静地喝酒，\n',
            '在你身上还真是少见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FB6')

    def _loc_2F79(): pass

    label('loc_2F79')

    ChrTalk(
        0x0102,
        (
            '#0020340514V#1044F咦，今天是一个人？\n',
            '实在是相当罕见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FB6(): pass

    label('loc_2FB6')

    ChrTalk(
        0x000B,
        (
            '#0080340515V#071F哈哈，因为\n',
            '能和我喝酒的朋友已经回国去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340516V尽管没能赶上，\n',
            '不过还是敬他一杯送别的酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340517V#1015F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340518V金先生确实是经常和\n',
            '奥利维尔对饮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340519V#1041F想想的话，\n',
            '这个组合似乎也挺不可思议的呢。',
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
        'loc_30F3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340520V#048F呵呵，确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318E')

    def _loc_30F3(): pass

    label('loc_30F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3129',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340521V#560F嘿嘿，也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318E')

    def _loc_3129(): pass

    label('loc_3129')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_315D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340522V#051F嘿嘿，确实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318E')

    def _loc_315D(): pass

    label('loc_315D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_318E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340523V#021F呵呵，确实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_318E(): pass

    label('loc_318E')

    ChrTalk(
        0x000B,
        (
            '#0080340524V#074F是啊，除了喜欢酒之外\n',
            '几乎没有什么共通点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340525V#070F但说不定正因为这样，\n',
            '我们两个才会一拍即合的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340526V因为人们都会寻求\n',
            '自身所欠缺的事物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340527V#1011F原来如此……这也有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3377',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340528V#525F也好，今后\n',
            '你就找我一起喝酒吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340529V一个人喝对身体不好哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340530V#1015F咦？可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340531V（和雪拉姐一起喝，\n',
            '  我觉得对身体更不好……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340532V#1048F（……被她听见会挨鞭子的哦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35C5')

    def _loc_3377(): pass

    label('loc_3377')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34DB',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340533V#1060F也好，如果方便的话，\n',
            '下次请找我一起喝酒吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340534V毕竟一个人喝\n',
            '对身体也不好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340535V#1004F咦？可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340536V神父\n',
            '可以喝酒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180340537V#1068F严格来说\n',
            '当然不可以……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340538V#1066F不过一点点的话\n',
            '相信女神也会宽恕我的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340539V#1019F真、真是油腔滑调～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35C5')

    def _loc_34DB(): pass

    label('loc_34DB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_354F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340540V#051F也好，以后就\n',
            '找我们一起喝酒吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340541V虽然不像那家伙\n',
            '那么会制造气氛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35C5')

    def _loc_354F(): pass

    label('loc_354F')

    ChrTalk(
        0x0102,
        (
            '#0020340542V#1040F如果觉得方便的话，\n',
            '以后请找我们一起作陪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340543V虽然我不会喝酒，\n',
            '不过聊天还是可以的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35C5(): pass

    label('loc_35C5')

    ChrTalk(
        0x000B,
        (
            '#0080340544V#070F不好意思。\n',
            '让你们这么费心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340545V嗯，难得有这样的提议，\n',
            '过几天我再来邀约吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x03C5, 0, 0x1E28))

    Jump('loc_369B')

    def _loc_3636(): pass

    label('loc_3636')

    ChrTalk(
        0x000B,
        (
            '#0080340546V#070F我暂时还要\n',
            '在这里多喝几杯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340547V如果需要帮忙的话，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_369B(): pass

    label('loc_369B')

    Jump('loc_36D0')

    def _loc_369E(): pass

    label('loc_369E')

    ChrTalk(
        0x000B,
        (
            '#0080340548V#070F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0005)

    Jump('loc_36D0')

    def _loc_36CA(): pass

    label('loc_36CA')

    Jump('loc_36D0')

    def _loc_36CD(): pass

    label('loc_36CD')

    Jump('loc_36D0')

    def _loc_36D0(): pass

    label('loc_36D0')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x36D9
@scena.Code('func_04_36D9')
def func_04_36D9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_3742',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3705',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_3736')

    def _loc_3705(): pass

    label('loc_3705')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_371B',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_3736')

    def _loc_371B(): pass

    label('loc_371B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3731',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_3736')

    def _loc_3731(): pass

    label('loc_3731')

    ChrSetSubChip(0x00FE, 0)

    def _loc_3736(): pass

    label('loc_3736')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    def _loc_3742(): pass

    label('loc_3742')

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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_37A0'),
        (0x00000001, 'loc_3CA2'),
        (0x00000002, 'loc_3CCE'),
        (-1, 'loc_3CD1'),
    )

    def _loc_37A0(): pass

    label('loc_37A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_3935',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 5, 0x1E45)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38DD',
    )

    ChrTalk(
        0x0010,
        (
            '#0050390534V#051F哦，雪拉扎德。\n',
            '这次轮到你出场了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030390535V#025F嗯，看来是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390536V不能陪你喝酒实在很遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0050390537V#051F喝酒无所谓，需要我帮忙的话\n',
            '随时叫我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390538V……需要时尽管说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030390539V#525F呵呵，谢谢你了。\n',
            '我会记住这个人情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x03C8, 5, 0x1E45))
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_3932')

    def _loc_38DD(): pass

    label('loc_38DD')

    ChrTalk(
        0x0010,
        (
            '#0050390540V#051F要帮忙的话\n',
            '随时叫我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390541V……需要时尽管说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    def _loc_3932(): pass

    label('loc_3932')

    Jump('loc_3C9F')

    def _loc_3935(): pass

    label('loc_3935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_3C9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 4, 0x1E44)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B8F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_39E0',
    )

    ChrTalk(
        0x0010,
        (
            '#0050340443V#053F『瘦狼』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340444V在蔡斯时，我们几个\n',
            '对他根本束手无策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340445V#050F不过你要是在的话\n',
            '说不定情况会好一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A74')

    def _loc_39E0(): pass

    label('loc_39E0')

    ChrTalk(
        0x0010,
        (
            '#0050340446V#053F『瘦狼』瓦鲁特吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340447V听说大家在蔡斯时\n',
            '被他整得很惨呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340445V#050F不过你要是在的话\n',
            '说不定情况会好一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A74(): pass

    label('loc_3A74')

    ChrTalk(
        0x0108,
        (
            '#0080340449V#070F别那么抬举我。\n',
            '行不行得通，\n',
            '得要较量过后才知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340450V如果有兴趣的话\n',
            '你也一起过来如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0108, 400)

    ChrTalk(
        0x0010,
        (
            '#0050320701V#051F嘿，也对，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340452V我会准备妥当的。\n',
            '有需要的话随时叫我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340453V#1006F啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340430V#1040F拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x03C8, 4, 0x1E44))

    Jump('loc_3C9F')

    def _loc_3B8F(): pass

    label('loc_3B8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3C1A',
    )

    ChrTurnDirection(0x0010, 0x0108, 0)

    ChrTalk(
        0x0010,
        (
            '#0050340455V#050F『瘦狼』……\n',
            '那家伙的武技可是绝非寻常。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340456V#051F嘿嘿，我真想见识\n',
            '你能跟他对抗到什么程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C9F')

    def _loc_3C1A(): pass

    label('loc_3C1A')

    ChrTurnDirection(0x0010, 0x0108, 0)

    ChrTalk(
        0x0010,
        (
            '#0050340457V#050F『瘦狼』瓦鲁特吗……\n',
            '似乎是个掌握极强武技的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340458V#051F嘿嘿，你和他\n',
            '之间的战斗一定很精彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C9F(): pass

    label('loc_3C9F')

    Jump('loc_3CD4')

    def _loc_3CA2(): pass

    label('loc_3CA2')

    ChrTalk(
        0x0010,
        (
            '#0050340459V#050F要更换成员了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0005)

    Jump('loc_3CD4')

    def _loc_3CCE(): pass

    label('loc_3CCE')

    Jump('loc_3CD4')

    def _loc_3CD1(): pass

    label('loc_3CD1')

    Jump('loc_3CD4')

    def _loc_3CD4(): pass

    label('loc_3CD4')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x3CDD
@scena.Code('func_05_3CDD')
def func_05_3CDD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_4164',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034E, 2, 0x1A72)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40E7',
    )

    ChrTalk(
        0x000D,
        (
            '#0600310240V#160F……怎么，原来是你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310241V#1000F怎么了？摩尔根将军，\n',
            '你怎么会一个人在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310242V#160F嗯，我正在重新\n',
            '检查一遍作战计划。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310243V即使看上去很完美的计划，\n',
            '过些时间再回顾一下的话\n',
            '也能够找出漏洞来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310244V#1002F那么……\n',
            '发现什么缺陷了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310245V#163F不，现在还没有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310246V只要没发生太大的意外，\n',
            '这次作战应该能取得成功。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310247V#165F很遗憾，这次应该是\n',
            '没有你们出场的机会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310248V#1015F嗯，那就最好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310249V#1002F不过紧要关头\n',
            '我们还是会帮忙的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310250V因为你准许我们登舰，\n',
            '就代表多少对我们有些期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310251V#160F当然，我是有这个意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310252V不过必须等我们的作战完成后，\n',
            '你们几个才能够自由行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310253V作战行动时毕竟\n',
            '还是要听从我们的指挥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310254V#1006F没问题，我明白的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310255V我们会先乖乖地\n',
            '在一旁观看你们的表演。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600310256V#165F哼……小姑娘口气倒不小。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310257V在和龙对战之前\n',
            '还有一些时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310258V你们就趁这个时候\n',
            '就尽量准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034E, 2, 0x1A72))

    Jump('loc_4164')

    def _loc_40E7(): pass

    label('loc_40E7')

    ChrTalk(
        0x000D,
        (
            '#0600310259V#160F必须等我们的作战完成后，\n',
            '你们游击士才能够自由行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310253V作战行动时毕竟\n',
            '还是要听从我们的指挥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4164(): pass

    label('loc_4164')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x4168
@scena.Code('func_06_4168')
def func_06_4168():
    TalkBegin(0x001C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_43D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_4341',
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
            TXT(0x01, '买东西(道具)\n'),
            TXT(0x02, '买东西(食材)\n'),
            TXT(0x03, '招牌菜『苦味菜肉蛋卷』　1800米拉\n'),
            TXT(0x04, '离开\n'),
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
        'loc_420C',
    )

    OP_A9(0x2C)
    TalkEnd(0x001C)

    Return()

    def _loc_420C(): pass

    label('loc_420C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_421F',
    )

    OP_A9(0x2B)
    TalkEnd(0x001C)

    Return()

    def _loc_421F(): pass

    label('loc_421F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_432D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x708),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_42F8',
    )

    RemoveMira(1800)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '苦味菜肉蛋卷',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 2500)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 2500)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 2500)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 2500)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 2500)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 2500)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 2500)
    ChrSetStatus(ChrTable['金'], 0xFD, 2500)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 2500)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42EA',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x000C)"),
            Expr.Return,
        ),
        'loc_42BE',
    )

    Jump('loc_42EA')

    def _loc_42BE(): pass

    label('loc_42BE')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '苦味菜肉蛋卷',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42EA(): pass

    label('loc_42EA')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_431E')

    def _loc_42F8(): pass

    label('loc_42F8')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_431E(): pass

    label('loc_431E')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x001C)

    Return()

    def _loc_432D(): pass

    label('loc_432D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_433E',
    )

    TalkEnd(0x001C)

    Return()

    def _loc_433E(): pass

    label('loc_433E')

    Jump('loc_43D9')

    def _loc_4341(): pass

    label('loc_4341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_43D9',
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
            TXT(0x01, '买东西(道具)\n'),
            TXT(0x02, '买东西(食材)\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43B5',
    )

    OP_A9(0x2A)
    TalkEnd(0x001C)

    Return()

    def _loc_43B5(): pass

    label('loc_43B5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43C8',
    )

    OP_A9(0x2B)
    TalkEnd(0x001C)

    Return()

    def _loc_43C8(): pass

    label('loc_43C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43D9',
    )

    TalkEnd(0x001C)

    Return()

    def _loc_43D9(): pass

    label('loc_43D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_4688',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4584',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44DE',
    )

    ChrTalk(
        0x001C,
        (
            '<FIXME>……よう、大尉。\n',
            'いよいよ都市の中枢の\n',
            '探索に入るらしいな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '<FIXME>ま、腕の立つあんたのことだ。\n',
            '特に心配はしてねえが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '<FIXME>クルーの中には\n',
            '不安に思ってるヤツも多い。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '<FIXME>早めに帰ってきてくれよ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4581')

    def _loc_44DE(): pass

    label('loc_44DE')

    ChrTalk(
        0x001C,
        (
            '<FIXME>《アルセイユ》もどうにか\n',
            '飛べるようにはできるだろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '<FIXME>……早めに帰ってきてくれよ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '<FIXME>帰還の時には、やっぱ\n',
            'あんたの指揮が必要だ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4581(): pass

    label('loc_4581')

    Jump('loc_4685')

    def _loc_4584(): pass

    label('loc_4584')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_462D',
    )

    ChrTalk(
        0x001C,
        (
            '……哟，是你们啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '终于要开始探索\n',
            '都市的中枢了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '『埃尔赛尤』也应该能\n',
            '飞起来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……你们一定要平安返回啊。\n',
            '大家要一起回到陆地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4685')

    def _loc_462D(): pass

    label('loc_462D')

    ChrTalk(
        0x001C,
        (
            '『埃尔赛尤』也应该能\n',
            '飞起来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '你们一定要平安返回啊。\n',
            '大家要一起回到陆地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4685(): pass

    label('loc_4685')

    Jump('loc_5090')

    def _loc_4688(): pass

    label('loc_4688')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_475E',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4713',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46F1',
    )

    ChrTalk(
        0x001C,
        (
            '嗯……\n',
            '鲁特琴弹得真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '看来这演奏家的自称\n',
            '可不是吹牛的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4710')

    def _loc_46F1(): pass

    label('loc_46F1')

    ChrTalk(
        0x001C,
        (
            '嗯……\n',
            '鲁特琴弹得真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4710(): pass

    label('loc_4710')

    Jump('loc_475B')

    def _loc_4713(): pass

    label('loc_4713')

    ChrTalk(
        0x001C,
        (
            '看来要和空贼团\n',
            '合作了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '想不到那位尤莉亚\n',
            '竟然真的同意了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_475B(): pass

    label('loc_475B')

    Jump('loc_5090')

    def _loc_475E(): pass

    label('loc_475E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_4837',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47E6',
    )

    ChrTalk(
        0x001C,
        (
            '由于在作战前\n',
            '囤积了很多物品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我店内的商品种类\n',
            '也比之前丰富许多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '你们就尽情地享受\n',
            '购物的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4834')

    def _loc_47E6(): pass

    label('loc_47E6')

    ChrTalk(
        0x001C,
        (
            '由于在作战前\n',
            '囤积了很多物品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我店内的商品种类\n',
            '也比之前丰富许多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4834(): pass

    label('loc_4834')

    Jump('loc_5090')

    def _loc_4837(): pass

    label('loc_4837')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_4910',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48C5',
    )

    ChrTalk(
        0x001C,
        (
            '………………………………\n',
            '……哦，是你们啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我的店也\n',
            '总算整理完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '在进行探索之前\n',
            '好好补充一下装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_490D')

    def _loc_48C5(): pass

    label('loc_48C5')

    ChrTalk(
        0x001C,
        (
            '我的店也\n',
            '总算整理完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '在进行探索之前\n',
            '好好补充一下装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_490D(): pass

    label('loc_490D')

    Jump('loc_5090')

    def _loc_4910(): pass

    label('loc_4910')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_4E21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_4A20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49C9',
    )

    ChrTalk(
        0x001C,
        (
            '『四轮之塔』也\n',
            '只剩下一座了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……这个任务也终于\n',
            '快要完成了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '但是，在空中旅行的时候，\n',
            '总是起飞和降落最危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……尽可能地小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4A1D')

    def _loc_49C9(): pass

    label('loc_49C9')

    ChrTalk(
        0x001C,
        (
            '在空中旅行的时候，\n',
            '总是起飞和降落最危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '越到最后……\n',
            '就越要小心行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A1D(): pass

    label('loc_4A1D')

    Jump('loc_4E1E')

    def _loc_4A20(): pass

    label('loc_4A20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_4B3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4ACA',
    )

    ChrTalk(
        0x001C,
        (
            '……王国各地\n',
            '据说都在发生事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '地方部队光是要应付这些，\n',
            '恐怕就已经疲于奔命了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……把塔的任务交给游击士，\n',
            '真可以说是大大的成功啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4B3A')

    def _loc_4ACA(): pass

    label('loc_4ACA')

    ChrTalk(
        0x001C,
        (
            '……把塔的任务交给游击士，\n',
            '从战略上来看是正确的决断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '这种漂亮的用人方式，\n',
            '真像是卡西乌斯准将的风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B3A(): pass

    label('loc_4B3A')

    Jump('loc_4E1E')

    def _loc_4B3D(): pass

    label('loc_4B3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_4D3D',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4C8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C05',
    )

    ChrTalk(
        0x001C,
        (
            '那张座位上的女人…\n',
            '酒量看起来相当不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我也想来上一杯，不过很不巧，\n',
            '现在正在作战前的待命状态……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '酒会降低人的判断能力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……我还是先忍着点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4C8A')

    def _loc_4C05(): pass

    label('loc_4C05')

    ChrTalk(
        0x001C,
        (
            '酒会让人幸福，\n',
            '同时也会降低人的理智……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '从这个事实可以导出一个\n',
            '极为单纯的结论……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '那就是——理智\n',
            '正是我们不幸的元凶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C8A(): pass

    label('loc_4C8A')

    Jump('loc_4D3A')

    def _loc_4C8D(): pass

    label('loc_4C8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D01',
    )

    ChrTalk(
        0x001C,
        (
            '哟，你们调查辛苦了。\n',
            '在出发前先填饱肚子怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '适度地吃点东西，\n',
            '紧要关头时就拿得出力气来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_4D3A')

    def _loc_4D01(): pass

    label('loc_4D01')

    ChrTalk(
        0x001C,
        (
            '在出发前先填饱肚子怎么样？\n',
            '事先吃点东西比较有力气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D3A(): pass

    label('loc_4D3A')

    Jump('loc_4E1E')

    def _loc_4D3D(): pass

    label('loc_4D3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_4E1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4DDB',
    )

    ChrTalk(
        0x001C,
        (
            '哦，是你们啊……\n',
            '怎么又来了？挺好奇的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '这里从日用品到食品，\n',
            '各种商品一应俱全……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……如果需要什么东西，\n',
            '可以随时过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4E1E')

    def _loc_4DDB(): pass

    label('loc_4DDB')

    ChrTalk(
        0x001C,
        (
            '这里是舰内的小卖部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '如果需要什么东西，\n',
            '可以随时过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E1E(): pass

    label('loc_4E1E')

    Jump('loc_5090')

    def _loc_4E21(): pass

    label('loc_4E21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_5090',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FEF',
    )

    ChrTalk(
        0x001C,
        (
            '哟，欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我叫凯西……\n',
            '是亲卫队的厨师，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '同时也经营小卖部，\n',
            '不过现在还没开张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……下次有机会\n',
            '再前来快乐地购物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 0, 0x1A20)),
            Expr.Return,
        ),
        'loc_4FE9',
    )

    ChrTalk(
        0x0101,
        (
            '#1011F咦，小卖部没营业？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#1015F……可是那里\n',
            '有个人正在喝酒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '那是我请他喝的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我在检查酒的残量时，\n',
            '他跑过来跟我聊天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我见他相当精于此道，\n',
            '于是就请他喝了一杯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x001C, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#1004F是、是这么回事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '(奥利维尔自称美食家，\n',
            '看来也不像是在吹牛啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FE9(): pass

    label('loc_4FE9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_5090')

    def _loc_4FEF(): pass

    label('loc_4FEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 0, 0x1A20)),
            Expr.Return,
        ),
        'loc_5049',
    )

    ChrTalk(
        0x001C,
        (
            '那个金发男人……\n',
            '好像是帝国人的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……不过对于\n',
            '葡萄酒的品味不坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5090')

    def _loc_5049(): pass

    label('loc_5049')

    ChrTalk(
        0x001C,
        (
            '抱歉，现在还没开张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '下次有机会的话\n',
            '再前来快乐地购物吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5090(): pass

    label('loc_5090')

    TalkEnd(0x001C)

    Return()

# id: 0x0007 offset: 0x5094
@scena.Code('func_07_5094')
def func_07_5094():
    TalkBegin(0x00FE)
    ChrSetFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_50B9',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_50EA')

    def _loc_50B9(): pass

    label('loc_50B9')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_50CF',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_50EA')

    def _loc_50CF(): pass

    label('loc_50CF')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_50E5',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_50EA')

    def _loc_50E5(): pass

    label('loc_50E5')

    ChrSetSubChip(0x00FE, 0)

    def _loc_50EA(): pass

    label('loc_50EA')

    ChrSetDirection(0x00FE, 0, 0)
    ChrClearFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5191',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5165',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，好久没有听过现场\n',
            '演奏的鲁特琴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '音乐果然是好东西呢。\n',
            '令人心情舒坦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_518E')

    def _loc_5165(): pass

    label('loc_5165')

    ChrTalk(
        0x00FE,
        (
            '音乐果然是好东西呢。\n',
            '令人心情舒坦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_518E(): pass

    label('loc_518E')

    Jump('loc_522B')

    def _loc_5191(): pass

    label('loc_5191')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51E3',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，接下来\n',
            '该去填饱肚子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等一下又要\n',
            '到现场去接班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_522B')

    def _loc_51E3(): pass

    label('loc_51E3')

    ChrTalk(
        0x00FE,
        (
            '那么，接下来\n',
            '该去填饱肚子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '问问凯西今天有什么\n',
            '招牌菜吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_522B(): pass

    label('loc_522B')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x5234
@scena.Code('func_08_5234')
def func_08_5234():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_534E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52EE',
    )

    ChrTalk(
        0x00FE,
        (
            '当长期出航时，\n',
            '我每天都在这里用餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在严肃的工作中，\n',
            '只有这是唯一的乐趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不让我们吃腻，\n',
            '天天都要变换不同的菜色。\n',
            '所以厨师的责任也十分重大哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_534E')

    def _loc_52EE(): pass

    label('loc_52EE')

    ChrTalk(
        0x00FE,
        (
            '当长期出航时，\n',
            '我每天都在这里用餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸好厨师的水平相当高，\n',
            '我们都觉得这是我们的福气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_534E(): pass

    label('loc_534E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x5352
@scena.Code('func_09_5352')
def func_09_5352():
    TalkBegin(0x00FE)
    ChrSetFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5377',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_53A8')

    def _loc_5377(): pass

    label('loc_5377')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_538D',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_53A8')

    def _loc_538D(): pass

    label('loc_538D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_53A3',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_53A8')

    def _loc_53A3(): pass

    label('loc_53A3')

    ChrSetSubChip(0x00FE, 0)

    def _loc_53A8(): pass

    label('loc_53A8')

    ChrSetDirection(0x00FE, 180, 0)
    ChrClearFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5404',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，我先过来\n',
            '休息一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过很快就要\n',
            '到外面去接班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_543B')

    def _loc_5404(): pass

    label('loc_5404')

    ChrTalk(
        0x00FE,
        (
            '呼，我先过来\n',
            '休息一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，吃饭了吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_543B(): pass

    label('loc_543B')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x5444
@scena.Code('func_0A_5444')
def func_0A_5444():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_5451',
    )

    Jump('loc_56B9')

    def _loc_5451(): pass

    label('loc_5451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_55CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5556',
    )

    ChrTalk(
        0x00FE,
        (
            '……热气从表面看来虽然消散了，\n',
            '但实际上还停留在大气之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……被吸收了导力也一样，\n',
            '必定会被保存在某个地方才对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……『里塔』的存在……\n',
            '…………被折叠的次元……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那些蒸发掉的导力的去处，\n',
            '也会在那里找到某些提示吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_55C8')

    def _loc_5556(): pass

    label('loc_5556')

    ChrTalk(
        0x00FE,
        (
            '……『里塔』的存在……\n',
            '…………被折叠的次元……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那些蒸发掉的导力的去处，\n',
            '也会在那里找到某些提示吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_55C8(): pass

    label('loc_55C8')

    Jump('loc_56B9')

    def _loc_55CB(): pass

    label('loc_55CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_56B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5663',
    )

    ChrTalk(
        0x00FE,
        (
            '听说蔡斯那边\n',
            '正陷入了危急的状况中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，看来我们的研究\n',
            '也要快点拿出成果来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下子必须要一鼓作气地\n',
            '努力工作才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_56B9')

    def _loc_5663(): pass

    label('loc_5663')

    ChrTalk(
        0x00FE,
        (
            '听说蔡斯那边\n',
            '正陷入了危急的状况中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，看来我们的研究\n',
            '也要快点拿出成果来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56B9(): pass

    label('loc_56B9')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
