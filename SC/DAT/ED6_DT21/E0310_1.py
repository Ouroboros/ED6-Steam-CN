import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0310_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0310_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0310.x'
    header.mapIndex       = 1
    header.bgm            = 116
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/E0310._SN', 'ED6_DT21/E0310_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_180',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_112',
    )

    ChrTalk(
        0x00FE,
        (
            '右舷，飞翔引擎……回路连接完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从预想输出功率的５０％\n',
            '开始进行模拟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_17A')

    def _loc_112(): pass

    label('loc_112')

    ChrTalk(
        0x00FE,
        (
            '在输出功率的５０％到７０％之间\n',
            '通过增加负荷来测试电路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果舷外支架有异常，\n',
            '就立即停止测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17A(): pass

    label('loc_17A')

    TalkEnd(0x00FE)

    Jump('loc_1332')

    def _loc_180(): pass

    label('loc_180')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_18A',
    )

    Jump('loc_1332')

    def _loc_18A(): pass

    label('loc_18A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_194',
    )

    Jump('loc_1332')

    def _loc_194(): pass

    label('loc_194')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_3B6',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24D',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，殿下……您辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚刚先完成了\n',
            '各项机能的检查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正如拉赛尔博士所说，\n',
            '损伤出奇地轻微。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种程度靠我们自己\n',
            '就足以进行修复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_2A1')

    def _loc_24D(): pass

    label('loc_24D')

    ChrTalk(
        0x00FE,
        (
            '正如拉赛尔博士所说，\n',
            '损伤出奇地轻微。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种程度靠我们自己\n',
            '就足以进行修复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A1(): pass

    label('loc_2A1')

    Jump('loc_3B0')

    def _loc_2A4(): pass

    label('loc_2A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35A',
    )

    ChrTalk(
        0x00FE,
        (
            '刚刚先完成了\n',
            '各项机能的检查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正如博士所说，\n',
            '损伤比想象中的要小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '舵总算还没问题，\n',
            '导力机关也平安无事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '努力一下的话应该\n',
            '可以靠我们自己来修复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_3B0')

    def _loc_35A(): pass

    label('loc_35A')

    ChrTalk(
        0x00FE,
        (
            '正如博士所说，\n',
            '损伤比想象中的要小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '努力一下的话应该\n',
            '可以靠我们自己来修复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B0(): pass

    label('loc_3B0')

    TalkEnd(0x00FE)

    Jump('loc_1332')

    def _loc_3B6(): pass

    label('loc_3B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_5EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59F',
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
        'loc_455',
    )

    Jump('loc_497')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_471',
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

    Jump('loc_497')

    def _loc_471(): pass

    label('loc_471')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_48D',
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

    Jump('loc_497')

    def _loc_48D(): pass

    label('loc_48D')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_497(): pass

    label('loc_497')

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
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F4',
    )

    ChrTalk(
        0x00FE,
        (
            '离这次作战结束\n',
            '就只剩下那座塔了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51D')

    def _loc_4F4(): pass

    label('loc_4F4')

    ChrTalk(
        0x00FE,
        (
            '离这次作战结束\n',
            '就只剩下那座塔了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51D(): pass

    label('loc_51D')

    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '呼，埃尔赛尤号啊。\n',
            '你也辛苦了。\n',
            '总是四处奔波，一定累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们很快就能回王都了。\n',
            '拜托你再坚持一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_5E8')

    def _loc_59F(): pass

    label('loc_59F')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '埃尔赛尤号啊。\n',
            '拜托你再坚持一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们很快就能回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)
    def _loc_5E8(): pass

    label('loc_5E8')

    Jump('loc_1332')

    def _loc_5EB(): pass

    label('loc_5EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_7BC',
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
        'loc_682',
    )

    Jump('loc_6C4')

    def _loc_682(): pass

    label('loc_682')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_69E',
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

    Jump('loc_6C4')

    def _loc_69E(): pass

    label('loc_69E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_6BA',
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

    Jump('loc_6C4')

    def _loc_6BA(): pass

    label('loc_6BA')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6C4(): pass

    label('loc_6C4')

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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_777',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……？　你是谁？\n',
            '不好意思，请别跟我说话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '海风很强啊。\n',
            '保持姿势很困难哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要让这么大的船\n',
            '悬停在空中\n',
            '不容易呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_7B1')

    def _loc_777(): pass

    label('loc_777')

    ChrTalk(
        0x00FE,
        (
            '可恶…\n',
            '风会使船不安定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我不喜欢\n',
            '沿海地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7B1(): pass

    label('loc_7B1')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_1332')

    def _loc_7BC(): pass

    label('loc_7BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_9C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_882',
    )

    TalkBegin(0x00FE)
    OP_4A(0x000F, 255)

    ChrTalk(
        0x000E,
        (
            '这个塔也一样被\n',
            '黑色的障壁笼罩着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '博士正在调查……\n',
            '……目前还没有结论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……不过接近它一定很危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯，我有同感。\n',
            '总之要保持距离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_4B(0x000F, 255)
    TalkEnd(0x00FE)

    Jump('loc_9C5')

    def _loc_882(): pass

    label('loc_882')

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
        'loc_912',
    )

    Jump('loc_954')

    def _loc_912(): pass

    label('loc_912')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_92E',
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

    Jump('loc_954')

    def _loc_92E(): pass

    label('loc_92E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_94A',
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

    Jump('loc_954')

    def _loc_94A(): pass

    label('loc_94A')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_954(): pass

    label('loc_954')

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

    ChrTalk(
        0x000E,
        (
            '这个塔也一样被\n',
            '黑色的障壁笼罩着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '那东西\n',
            '究竟是什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    def _loc_9C5(): pass

    label('loc_9C5')

    Jump('loc_1332')

    def _loc_9C8(): pass

    label('loc_9C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_C42',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AFA',
    )

    TalkBegin(0x00FE)
    OP_4A(0x000F, 255)

    ChrTalk(
        0x000F,
        (
            '塔的导力场有异常……\n',
            '………别太靠近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '还有风……\n',
            '……注意别被卷走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '没问题的。\n',
            '我们和塔有一段距离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过，究竟是什么呢？\n',
            '那个像黑色墙壁一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '你说的导力场异常也是\n',
            '那东西所造成的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '………不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '不过……得小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_4B(0x000F, 255)
    TalkEnd(0x00FE)

    Jump('loc_C3F')

    def _loc_AFA(): pass

    label('loc_AFA')

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
        'loc_B8A',
    )

    Jump('loc_BCC')

    def _loc_B8A(): pass

    label('loc_B8A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_BA6',
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

    Jump('loc_BCC')

    def _loc_BA6(): pass

    label('loc_BA6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BC2',
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

    Jump('loc_BCC')

    def _loc_BC2(): pass

    label('loc_BC2')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BCC(): pass

    label('loc_BCC')

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

    ChrTalk(
        0x000E,
        (
            '当然，小心\n',
            '总是没有坏处的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '总之要好好保持\n',
            '和塔之间的距离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    def _loc_C3F(): pass

    label('loc_C3F')

    Jump('loc_1332')

    def _loc_C42(): pass

    label('loc_C42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_D91',
    )

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
        'loc_CD9',
    )

    Jump('loc_D1B')

    def _loc_CD9(): pass

    label('loc_CD9')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_CF5',
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

    Jump('loc_D1B')

    def _loc_CF5(): pass

    label('loc_CF5')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D11',
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

    Jump('loc_D1B')

    def _loc_D11(): pass

    label('loc_D11')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D1B(): pass

    label('loc_D1B')

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

    ChrTalk(
        0x00FE,
        (
            '呼，看来\n',
            '被干掉了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '操控技术不错吧？\n',
            '嘿嘿，不愧是本大爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Jump('loc_1332')

    def _loc_D91(): pass

    label('loc_D91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_1332',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 2, 0x1A6A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F83',
    )

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
        'loc_E30',
    )

    Jump('loc_E72')

    def _loc_E30(): pass

    label('loc_E30')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E4C',
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

    Jump('loc_E72')

    def _loc_E4C(): pass

    label('loc_E4C')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_E68',
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

    Jump('loc_E72')

    def _loc_E68(): pass

    label('loc_E68')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E72(): pass

    label('loc_E72')

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

    ChrTalk(
        0x00FE,
        (
            '哟，你们就是\n',
            '那帮游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是舵手勒克司。\n',
            '现在负责操舵这艘船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，这次恐怕\n',
            '没有你们的出场的机会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '才一两头龙而已……\n',
            '根本不是『埃尔赛尤』的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之你们就尽管放心，\n',
            '好好地参观一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x034D, 2, 0x1A6A))
    ChrSetSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Jump('loc_1332')

    def _loc_F83(): pass

    label('loc_F83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1125',
    )

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
        'loc_101A',
    )

    Jump('loc_105C')

    def _loc_101A(): pass

    label('loc_101A')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1036',
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

    Jump('loc_105C')

    def _loc_1036(): pass

    label('loc_1036')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1052',
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

    Jump('loc_105C')

    def _loc_1052(): pass

    label('loc_1052')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_105C(): pass

    label('loc_105C')

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

    ChrTalk(
        0x00FE,
        (
            '总之你们就尽管放心，\n',
            '好好地参观一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '另外，旁边那个叫艾柯的家伙\n',
            '请你们别和她计较。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然看起来傲慢又失礼，\n',
            '不过本性是相当善良的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrSetSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Jump('loc_1332')

    def _loc_1125(): pass

    label('loc_1125')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1282',
    )

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
        'loc_11BC',
    )

    Jump('loc_11FE')

    def _loc_11BC(): pass

    label('loc_11BC')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11D8',
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

    Jump('loc_11FE')

    def _loc_11D8(): pass

    label('loc_11D8')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_11F4',
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

    Jump('loc_11FE')

    def _loc_11F4(): pass

    label('loc_11F4')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11FE(): pass

    label('loc_11FE')

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

    ChrTalk(
        0x00FE,
        (
            '总之你们就尽管放心，\n',
            '好好地参加一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '另外，请你们别和\n',
            '艾柯那家伙计较。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Jump('loc_1332')

    def _loc_1282(): pass

    label('loc_1282')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12F1',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '１号、３号弹库开放测试ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '继续准备开放２号、４号。\n',
            '结晶回路，依序进行连接……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    TalkEnd(0x00FE)

    Jump('loc_1332')

    def _loc_12F1(): pass

    label('loc_12F1')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '１号、３号弹库开放测试ＯＫ。\n',
            '继续准备开放２号、４号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    def _loc_1332(): pass

    label('loc_1332')

    Return()

# id: 0x0002 offset: 0x1333
@scena.Code('func_02_1333')
def func_02_1333():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_16A6',
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
        'loc_13CA',
    )

    Jump('loc_140C')

    def _loc_13CA(): pass

    label('loc_13CA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_13E6',
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

    Jump('loc_140C')

    def _loc_13E6(): pass

    label('loc_13E6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1402',
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

    Jump('loc_140C')

    def _loc_1402(): pass

    label('loc_1402')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_140C(): pass

    label('loc_140C')

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
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14BE',
    )

    ChrTalk(
        0x00FE,
        (
            '<FIXME>あ、大尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>これから飛翔機関の\n',
            '試験を始めるところです……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>……大尉も、どうかご武運を……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169B')

    def _loc_14BE(): pass

    label('loc_14BE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1551',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正要展开\n',
            '飞翔引擎的测试……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这个成功的话，\n',
            '就只剩等待殿下归舰了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请让我最后……\n',
            '再祈祷一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_15A1')

    def _loc_1551(): pass

    label('loc_1551')

    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '控制系统，导力压正常……\n',
            '各接应系统也无异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……测试准备完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A1(): pass

    label('loc_15A1')

    Jump('loc_169B')

    def _loc_15A4(): pass

    label('loc_15A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_164B',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正要开始进行\n',
            '飞翔引擎的测试……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，中枢塔的探索，\n',
            '和舷外支架的回收……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这些难题还没有解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请让我最后……\n',
            '再祈祷一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_169B')

    def _loc_164B(): pass

    label('loc_164B')

    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '控制系统，导力压正常……\n',
            '各接应系统也无异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……测试准备完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_169B(): pass

    label('loc_169B')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_16A6(): pass

    label('loc_16A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_177F',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_172E',
    )

    ChrTalk(
        0x00FE,
        (
            '照明终于恢复了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来还有飞行系统的维修\n',
            '和操舵系统的调整……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许可以让它飞起来\n',
            '也说不定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1779')

    def _loc_172E(): pass

    label('loc_172E')

    ChrTalk(
        0x00FE,
        (
            '照明终于恢复了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来还有飞行系统的修理\n',
            '和操舵系统的调整……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1779(): pass

    label('loc_1779')

    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_177F(): pass

    label('loc_177F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_1BDC',
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
        'loc_1816',
    )

    Jump('loc_1858')

    def _loc_1816(): pass

    label('loc_1816')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1832',
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

    Jump('loc_1858')

    def _loc_1832(): pass

    label('loc_1832')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_184E',
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

    Jump('loc_1858')

    def _loc_184E(): pass

    label('loc_184E')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1858(): pass

    label('loc_1858')

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
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0453, 7, 0x229F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1AA4',
    )

    ChrTalk(
        0x00FE,
        (
            '我听大尉说了……\n',
            '你是空贼团的那个女孩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别妨碍我工作……\n',
            '……这一点我得事先声明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#211F哈哈，真是个无知的家伙～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '完全不知道\n',
            '我能帮上多大的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……是吗……\n',
            '那我就拭目以待了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那么，你能不能\n',
            '赶紧消失到别处去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#213F……什………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你妨碍到我工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一开始就说过\n',
            '别妨碍我的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#216F……唔～～～……！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F（算、算了算了……\n',
            '  克制一下啊。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（你打算和别人\n',
            '  一见面就吵架吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1052F（乔丝特……\n',
            '  这回你得认输了。 ）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#215F（呜～～～～～～……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x0453, 7, 0x229F))

    Jump('loc_1BD1')

    def _loc_1AA4(): pass

    label('loc_1AA4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B2B',
    )

    ChrTalk(
        0x00FE,
        (
            '可别妨碍我的工作啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要遵守到这一点，\n',
            '什么都不做也无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#216F（这、这个女人，真让人讨厌……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BD1')

    def _loc_1B2B(): pass

    label('loc_1B2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B9B',
    )

    ChrTalk(
        0x00FE,
        (
            '空贼团和我们的\n',
            '情况好像也差不多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也会尽可能地\n',
            '帮助他们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这是命令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1BD1')

    def _loc_1B9B(): pass

    label('loc_1B9B')

    ChrTalk(
        0x00FE,
        (
            '我们也会帮助\n',
            '空贼团的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这是\n',
            '命令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BD1(): pass

    label('loc_1BD1')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_1BDC(): pass

    label('loc_1BDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_1DA2',
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
        'loc_1C73',
    )

    Jump('loc_1CB5')

    def _loc_1C73(): pass

    label('loc_1C73')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1C8F',
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

    Jump('loc_1CB5')

    def _loc_1C8F(): pass

    label('loc_1C8F')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1CAB',
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

    Jump('loc_1CB5')

    def _loc_1CAB(): pass

    label('loc_1CAB')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CB5(): pass

    label('loc_1CB5')

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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D54',
    )

    ChrTalk(
        0x00FE,
        (
            '迫降之后，探测器\n',
            '一直出现反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都是一些超乎常识的\n',
            '强力导力反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这里到底有什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1D97')

    def _loc_1D54(): pass

    label('loc_1D54')

    ChrTalk(
        0x00FE,
        (
            '迫降之后，探测器\n',
            '一直出现反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这里到底有什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D97(): pass

    label('loc_1D97')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_1DA2(): pass

    label('loc_1DA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_2024',
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
        'loc_1E39',
    )

    Jump('loc_1E7B')

    def _loc_1E39(): pass

    label('loc_1E39')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1E55',
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

    Jump('loc_1E7B')

    def _loc_1E55(): pass

    label('loc_1E55')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1E71',
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

    Jump('loc_1E7B')

    def _loc_1E71(): pass

    label('loc_1E71')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1E7B(): pass

    label('loc_1E7B')

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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F72',
    )

    ChrTalk(
        0x00FE,
        (
            '导力场的混乱\n',
            '变得越来越大了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目前塔上\n',
            '还没有变化……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F20',
    )

    ChrTalk(
        0x00FE,
        (
            '公主殿下也请……\n',
            '……多多保重……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F43')

    def _loc_1F20(): pass

    label('loc_1F20')

    ChrTalk(
        0x00FE,
        (
            '你们也要……\n',
            '……多加小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F43(): pass

    label('loc_1F43')

    ChrTalk(
        0x00FE,
        (
            '这种现象……\n',
            '说不定也许是某种前兆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_2019')

    def _loc_1F72(): pass

    label('loc_1F72')

    ChrTalk(
        0x00FE,
        (
            '导力场的混乱\n',
            '变得越来越大了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种现象……\n',
            '说不定也许是某种前兆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FF6',
    )

    ChrTalk(
        0x00FE,
        (
            '公主殿下也请……\n',
            '……多多保重……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2019')

    def _loc_1FF6(): pass

    label('loc_1FF6')

    ChrTalk(
        0x00FE,
        (
            '你们也要……\n',
            '……多加小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2019(): pass

    label('loc_2019')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_2024(): pass

    label('loc_2024')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_2229',
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
        'loc_20BB',
    )

    Jump('loc_20FD')

    def _loc_20BB(): pass

    label('loc_20BB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_20D7',
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

    Jump('loc_20FD')

    def _loc_20D7(): pass

    label('loc_20D7')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_20F3',
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

    Jump('loc_20FD')

    def _loc_20F3(): pass

    label('loc_20F3')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_20FD(): pass

    label('loc_20FD')

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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21D2',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀…………………\n',
            '……辛苦了…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力场异常的原因\n',
            '目前还没掌握……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是知道了原因……\n',
            '早就能拟定对策了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来麻烦还要……\n',
            '持续一阵子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_221E')

    def _loc_21D2(): pass

    label('loc_21D2')

    ChrTalk(
        0x00FE,
        (
            '导力场异常的原因\n',
            '目前还没掌握……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来麻烦还要……\n',
            '持续一阵子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_221E(): pass

    label('loc_221E')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_2229(): pass

    label('loc_2229')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_2325',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_22E4',
    )

    ChrTalk(
        0x000E,
        (
            '这个塔也一样被\n',
            '黑色的障壁笼罩着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '博士正在调查……\n',
            '……目前还没有结论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……不过接近它一定很危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯，我有同感。\n',
            '总之要保持距离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_231F')

    def _loc_22E4(): pass

    label('loc_22E4')

    ChrTalk(
        0x000F,
        (
            '塔周边的导力场\n',
            '现在依然异常……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '还不能够接近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_231F(): pass

    label('loc_231F')

    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_2325(): pass

    label('loc_2325')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_2495',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_244E',
    )

    ChrTalk(
        0x000F,
        (
            '塔的导力场很不寻常……\n',
            '………别太靠近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '还有风……\n',
            '……注意别被吹走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '没问题的。\n',
            '我们和塔有一段距离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过，究竟是什么呢？\n',
            '那个像黑色墙壁一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '你说的导力场异常也是\n',
            '那个东西造成的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '………不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '不过……得小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_248F')

    def _loc_244E(): pass

    label('loc_244E')

    ChrTalk(
        0x000F,
        (
            '如果继续接近的话\n',
            '风险就太高了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '调查队伍从地面接近，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_248F(): pass

    label('loc_248F')

    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_2495(): pass

    label('loc_2495')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_2687',
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
        'loc_252C',
    )

    Jump('loc_256E')

    def _loc_252C(): pass

    label('loc_252C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2548',
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

    Jump('loc_256E')

    def _loc_2548(): pass

    label('loc_2548')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2564',
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

    Jump('loc_256E')

    def _loc_2564(): pass

    label('loc_2564')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_256E(): pass

    label('loc_256E')

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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2629',
    )

    ChrTalk(
        0x00FE,
        (
            '……赶快去观察一下龙的情况如何。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战果的确认\n',
            '对士兵来说也是重要的任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你们也不想被已经\n',
            '打倒了的敌人从背后偷袭吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_267C')

    def _loc_2629(): pass

    label('loc_2629')

    ChrTalk(
        0x00FE,
        (
            '……赶快去观察一下龙的情况如何！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战果的确认\n',
            '对士兵来说也是重要的任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_267C(): pass

    label('loc_267C')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_2687(): pass

    label('loc_2687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_2B8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 3, 0x1A6B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_281E',
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
        'loc_2726',
    )

    Jump('loc_2768')

    def _loc_2726(): pass

    label('loc_2726')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2742',
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

    Jump('loc_2768')

    def _loc_2742(): pass

    label('loc_2742')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_275E',
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

    Jump('loc_2768')

    def _loc_275E(): pass

    label('loc_275E')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2768(): pass

    label('loc_2768')

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

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听说了……\n',
            '你们是担任观察员的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可别妨碍我们的作战……\n',
            '……我想说的只有这些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x034D, 3, 0x1A6B))
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_281E(): pass

    label('loc_281E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_296D',
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
        'loc_28B5',
    )

    Jump('loc_28F7')

    def _loc_28B5(): pass

    label('loc_28B5')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_28D1',
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

    Jump('loc_28F7')

    def _loc_28D1(): pass

    label('loc_28D1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28ED',
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

    Jump('loc_28F7')

    def _loc_28ED(): pass

    label('loc_28ED')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_28F7(): pass

    label('loc_28F7')

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

    ChrTalk(
        0x00FE,
        (
            '寒暄应该也已经结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你们该返回工作岗位了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_296D(): pass

    label('loc_296D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2AB4',
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
        'loc_2A04',
    )

    Jump('loc_2A46')

    def _loc_2A04(): pass

    label('loc_2A04')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2A20',
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

    Jump('loc_2A46')

    def _loc_2A20(): pass

    label('loc_2A20')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2A3C',
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

    Jump('loc_2A46')

    def _loc_2A3C(): pass

    label('loc_2A3C')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A46(): pass

    label('loc_2A46')

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

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你们就没别的事可做了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_2AB4(): pass

    label('loc_2AB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B48',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '……周围空域没有导力反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……重复……\n',
            '周围空域没有导力反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……各巡逻艇接下来\n',
            '继续进行指定的巡逻任务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    TalkEnd(0x00FE)

    Jump('loc_2B8D')

    def _loc_2B48(): pass

    label('loc_2B48')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '周围空域没有导力反应……\n',
            '各巡逻艇继续进行指定的巡逻任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    def _loc_2B8D(): pass

    label('loc_2B8D')

    Return()

# id: 0x0003 offset: 0x2B8E
@scena.Code('func_03_2B8E')
def func_03_2B8E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_2D9A',
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
        'loc_2C25',
    )

    Jump('loc_2C67')

    def _loc_2C25(): pass

    label('loc_2C25')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2C41',
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

    Jump('loc_2C67')

    def _loc_2C41(): pass

    label('loc_2C41')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2C5D',
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

    Jump('loc_2C67')

    def _loc_2C5D(): pass

    label('loc_2C5D')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C67(): pass

    label('loc_2C67')

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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D2F',
    )

    ChrTalk(
        0x00FE,
        (
            '『山猫号』的修理工作\n',
            '似乎也进行得很顺利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于飞行系统的修复\n',
            '全都仰赖博士所提供的建议……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼团的各位也\n',
            '坦率地表达了自己的敬意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_2D8F')

    def _loc_2D2F(): pass

    label('loc_2D2F')

    ChrTalk(
        0x00FE,
        (
            '『山猫号』的修理工作\n',
            '似乎也进行得很顺利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来拉赛尔博士的建议\n',
            '提供了相当大的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D8F(): pass

    label('loc_2D8F')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_2D9A(): pass

    label('loc_2D9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_2F66',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F02',
    )

    ChrTalk(
        0x0010,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P这里是埃尔赛尤号……\n',
            '……山猫号，请回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P……重复一次，山猫号请回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            (TxtCtl.SetColor, 0x5),
            '#2P#1S啊啊，这里是山猫号……',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            (TxtCtl.SetColor, 0x5),
            '#2P#1S接收信号良好……\n',
            '埃尔赛尤号，你们那里听得清楚吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P埃尔赛尤呼叫山猫号……\n',
            '我们这边的信号也很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P贵舰现在有\n',
            '什么物资不足吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P重复……\n',
            '山猫号，有什么物资不足吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_2F60')

    def _loc_2F02(): pass

    label('loc_2F02')

    ChrTalk(
        0x0010,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P山猫号，你们那边有什么\n',
            '物资不足吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            (TxtCtl.SetColor, 0x0),
            '#1P重复……\n',
            '山猫号，有什么物资不足吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F60(): pass

    label('loc_2F60')

    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_2F66(): pass

    label('loc_2F66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_32B6',
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
        'loc_2FFD',
    )

    Jump('loc_303F')

    def _loc_2FFD(): pass

    label('loc_2FFD')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3019',
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

    Jump('loc_303F')

    def _loc_3019(): pass

    label('loc_3019')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3035',
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

    Jump('loc_303F')

    def _loc_3035(): pass

    label('loc_3035')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_303F(): pass

    label('loc_303F')

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
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0459, 7, 0x22CF)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3181',
    )

    ChrTalk(
        0x00FE,
        (
            '你就是空贼小姑娘吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客套话就不说了，空贼艇的\n',
            '通讯器材没有问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#210F应该没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '操舵室也没受到\n',
            '什么严重损伤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样啊，那么我们也\n',
            '进行一下通讯的准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等你的哥哥们平安返回\n',
            '后就可以马上联系到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#211F啊，嗯！\n',
            '拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0459, 7, 0x22CF))

    Jump('loc_32AB')

    def _loc_3181(): pass

    label('loc_3181')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_31DA',
    )

    ChrTalk(
        0x00FE,
        (
            '我们也在准备和\n',
            '空贼艇进行通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你哥哥他们\n',
            '要是没事就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32AB')

    def _loc_31DA(): pass

    label('loc_31DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3253',
    )

    ChrTalk(
        0x00FE,
        (
            '有空贼团在说明\n',
            '他们的船也在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，也许还可以用导力通讯\n',
            '和他们取得联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有空的话\n',
            '试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_32AB')

    def _loc_3253(): pass

    label('loc_3253')

    ChrTalk(
        0x00FE,
        (
            '有空贼团在就代表\n',
            '他们的船应该也在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '顺利的话，或许可以通过\n',
            '导力通讯取得联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32AB(): pass

    label('loc_32AB')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_32B6(): pass

    label('loc_32B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_3413',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33AF',
    )

    ChrTalk(
        0x00FE,
        (
            '通讯设备都正常呢。\n',
            '任何地方都没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起这些，我倒是更在意\n',
            '那些有时候会串线过来的信号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很遗憾，因为经过了加密\n',
            '无法得知内容……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那些似乎是\n',
            '『结社』的通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定他们也在\n',
            '探索着这座城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_340D')

    def _loc_33AF(): pass

    label('loc_33AF')

    ChrTalk(
        0x00FE,
        (
            '有时候会串线过来的信号，\n',
            '似乎是结社他们之间的联系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定他们也在\n',
            '探索着浮游都市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_340D(): pass

    label('loc_340D')

    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_3413(): pass

    label('loc_3413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_371A',
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
        'loc_34AA',
    )

    Jump('loc_34EC')

    def _loc_34AA(): pass

    label('loc_34AA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_34C6',
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

    Jump('loc_34EC')

    def _loc_34C6(): pass

    label('loc_34C6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_34E2',
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

    Jump('loc_34EC')

    def _loc_34E2(): pass

    label('loc_34E2')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_34EC(): pass

    label('loc_34EC')

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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3658',
    )

    ChrTalk(
        0x00FE,
        (
            '看来各地遭受的攻击\n',
            '也逐渐在平息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35C1',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来只要压制住最后的塔，\n',
            '就能让事件告一段落了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盼望大家凯旋归来……\n',
            '我们全体乘务员都在为你们祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3652')

    def _loc_35C1(): pass

    label('loc_35C1')

    ChrTalk(
        0x00FE,
        (
            '接下来各位只要压制住最后的塔，\n',
            '就能让事件告一段落了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但不知为什么，总觉得\n',
            '心中不太舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来还是因为不知道\n',
            '敌人的目的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3652(): pass

    label('loc_3652')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_370F')

    def _loc_3658(): pass

    label('loc_3658')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36B9',
    )

    ChrTalk(
        0x00FE,
        (
            '明明是最后的塔了，\n',
            '心里还是堵得慌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来还是因为不知道\n',
            '敌人的目的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_370F')

    def _loc_36B9(): pass

    label('loc_36B9')

    ChrTalk(
        0x00FE,
        (
            '明明终于到最后的塔了，\n',
            '心里还是堵得慌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来还是因为不知道\n',
            '敌人的目的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_370F(): pass

    label('loc_370F')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_371A(): pass

    label('loc_371A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_383E',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37AC',
    )

    ChrTalk(
        0x00FE,
        (
            '埃尔赛尤号呼叫守备队……\n',
            '玛诺利亚守备队，请报告情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '重复一次，这里是埃尔赛尤号。\n',
            '玛诺利亚守备队，请报告情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_3838')

    def _loc_37AC(): pass

    label('loc_37AC')

    ChrTalk(
        0x00FE,
        (
            '玛诺利亚守备队，这里是埃尔赛尤号。\n',
            '支援的警备艇正在向你们接近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '支援部队不久后即将到达玛诺利亚。\n',
            '重复，即将到达玛诺利亚上空……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3838(): pass

    label('loc_3838')

    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_383E(): pass

    label('loc_383E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_38F1',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38A1',
    )

    ChrTalk(
        0x00FE,
        (
            '蔡斯的战斗\n',
            '好象仍然很激烈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一旦有新的情报，\n',
            '我会立刻告知的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38EB')

    def _loc_38A1(): pass

    label('loc_38A1')

    ChrTalk(
        0x00FE,
        (
            '蔡斯的战斗\n',
            '好象仍然很激烈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么新的情报，\n',
            '我会马上告知的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38EB(): pass

    label('loc_38EB')

    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_38F1(): pass

    label('loc_38F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_39DB',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3969',
    )

    ChrTalk(
        0x00FE,
        (
            '埃尔赛尤号呼叫司令部……\n',
            '埃尔赛尤号呼叫司令部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到达目标上空……\n',
            '重复，到达目标……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_39D5')

    def _loc_3969(): pass

    label('loc_3969')

    ChrTalk(
        0x00FE,
        (
            '在目标上空发现可疑影子。\n',
            '目前判断无法直接降落……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将由地面派遣调查队。\n',
            '重复，由地面派遣调查队……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39D5(): pass

    label('loc_39D5')

    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_39DB(): pass

    label('loc_39DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_3B3D',
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
        'loc_3A72',
    )

    Jump('loc_3AB4')

    def _loc_3A72(): pass

    label('loc_3A72')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3A8E',
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

    Jump('loc_3AB4')

    def _loc_3A8E(): pass

    label('loc_3A8E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3AAA',
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

    Jump('loc_3AB4')

    def _loc_3AAA(): pass

    label('loc_3AAA')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3AB4(): pass

    label('loc_3AB4')

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

    ChrTalk(
        0x00FE,
        (
            '龙看来已完全进入睡眠状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在即便是整个人跳上去，\n',
            '也应该不会有任何危险才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Jump('loc_3E3F')

    def _loc_3B3D(): pass

    label('loc_3B3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_3E3F',
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
        'loc_3BD4',
    )

    Jump('loc_3C16')

    def _loc_3BD4(): pass

    label('loc_3BD4')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3BF0',
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

    Jump('loc_3C16')

    def _loc_3BF0(): pass

    label('loc_3BF0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3C0C',
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

    Jump('loc_3C16')

    def _loc_3C0C(): pass

    label('loc_3C0C')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3C16(): pass

    label('loc_3C16')

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
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 4, 0x1A6C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CC1',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，辛苦了……\n',
            '你们是观察员吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是主管本舰通讯的\n',
            '报务员利昂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然只是短期合作，\n',
            '不过还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    SetScenaFlags(ScenaFlag(0x034D, 4, 0x1A6C))

    Jump('loc_3E37')

    def _loc_3CC1(): pass

    label('loc_3CC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3D14',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然只是短期合作，\n',
            '不过还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也让我们竭尽彼此所能吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E37')

    def _loc_3D14(): pass

    label('loc_3D14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DC3',
    )

    ChrTalk(
        0x00FE,
        (
            '埃尔赛尤呼叫科尔波０１……\n',
            '……埃尔赛尤呼叫科尔波０１。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '周围空域没有反应……\n',
            '……重复，周围没有反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '贵舰请继续巡逻……\n',
            '……重复，贵舰请继续……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_3E37')

    def _loc_3DC3(): pass

    label('loc_3DC3')

    ChrTalk(
        0x00FE,
        (
            '埃尔赛尤呼叫戈尔斯０２……\n',
            '……埃尔赛尤呼叫戈尔斯０２。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '戈尔斯02，我是埃尔赛尤。\n',
            '……请报告状况，重复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E37(): pass

    label('loc_3E37')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    def _loc_3E3F(): pass

    label('loc_3E3F')

    Return()

# id: 0x0004 offset: 0x3E40
@scena.Code('func_04_3E40')
def func_04_3E40():
    TalkBegin(0x00FE)
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_3F9F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3EAA',
    )

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '等候各位归舰！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '愿女神赐福各位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_3F9C')

    def _loc_3EAA(): pass

    label('loc_3EAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F32',
    )

    ChrTalk(
        0x00FE,
        (
            '各位，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在要进行左舷舷外支架的\n',
            '回收和修复工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于结社也有可能发动袭击，\n',
            '因此现在还不能松懈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_3F9C')

    def _loc_3F32(): pass

    label('loc_3F32')

    ChrTalk(
        0x00FE,
        (
            '我们现在要进行左舷舷外支架的\n',
            '回收和修复工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于结社也有可能发动袭击，\n',
            '因此现在还不能松懈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F9C(): pass

    label('loc_3F9C')

    Jump('loc_48E2')

    def _loc_3F9F(): pass

    label('loc_3F9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_40FD',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_409C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_403D',
    )

    ChrTalk(
        0x00FE,
        (
            '出现在『琥珀之塔』上的，\n',
            '似乎是一个很小的孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结社真是一个\n',
            '让人摸不清的组织啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请殿下也\n',
            '一定要格外小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_4099')

    def _loc_403D(): pass

    label('loc_403D')

    ChrTalk(
        0x00FE,
        (
            '虽说是小孩子，\n',
            '但也一定是结社的手下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也许是我多操心了，\n',
            '不过也请殿下要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4099(): pass

    label('loc_4099')

    Jump('loc_40FA')

    def _loc_409C(): pass

    label('loc_409C')

    ChrTalk(
        0x00FE,
        (
            '出现在『琥珀之塔』上的，\n',
            '似乎是一个很小的孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结社真是一个\n',
            '让人摸不清的组织啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_40FA(): pass

    label('loc_40FA')

    Jump('loc_48E2')

    def _loc_40FD(): pass

    label('loc_40FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_4389',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42A3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 0, 0x1E40)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4244',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '殿下也要前往塔那边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请殿下一定要\n',
            '凡事谨慎行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有什么万一的话，\n',
            '我们的队长也有可能会上塔支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#045F是、是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过请不必担心。\n',
            '因为我和大家在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是这样子吗……\n',
            '那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0018, 0x0101, 400)
    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '那么，各位游击士，\n',
            '殿下就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x03C8, 0, 0x1E40))

    Jump('loc_42A0')

    def _loc_4244(): pass

    label('loc_4244')

    ChrTalk(
        0x00FE,
        (
            '请殿下也一定要\n',
            '凡事谨慎行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有什么万一的话，\n',
            '我们的队长也有可能会上塔支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42A0(): pass

    label('loc_42A0')

    Jump('loc_4386')

    def _loc_42A3(): pass

    label('loc_42A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_432A',
    )

    ChrTalk(
        0x00FE,
        (
            '好像有一名女性只身\n',
            '登上了『红莲之塔』呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '真是一位巾帼英雄呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我们的队长也\n',
            '有可能这么做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_4386')

    def _loc_432A(): pass

    label('loc_432A')

    ChrTalk(
        0x00FE,
        (
            '竟然一个人登上塔顶，\n',
            '真是一位了不起的女性啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我们的队长也\n',
            '有可能这么做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4386(): pass

    label('loc_4386')

    Jump('loc_48E2')

    def _loc_4389(): pass

    label('loc_4389')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_4602',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44B0',
    )

    ChrTalk(
        0x00FE,
        (
            '在笼罩塔顶的黑色障壁之中，\n',
            '还有延伸在内部的另一个空间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来『四轮之塔』\n',
            '并不是单纯的塔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '殿下也请多加小心。\n',
            '前方不知还有多少\n',
            '危险在等待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，这段时间\n',
            '请你们好好留守。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '是！　祝您旗开得胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_44F3')

    def _loc_44B0(): pass

    label('loc_44B0')

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '舰艇的事就交给我们吧。\n',
            '殿下也请多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    def _loc_44F3(): pass

    label('loc_44F3')

    Jump('loc_45FF')

    def _loc_44F6(): pass

    label('loc_44F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4599',
    )

    ChrTalk(
        0x00FE,
        (
            '在笼罩塔顶的黑色障壁之中，\n',
            '还有延伸在内部的另一个空间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来『四轮之塔』\n',
            '并不是单纯的塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能有我们所想象不到的\n',
            '特殊用途也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_45FF')

    def _loc_4599(): pass

    label('loc_4599')

    ChrTalk(
        0x00FE,
        (
            '在笼罩塔顶的黑色障壁之中，\n',
            '还有延伸在内部的另一个空间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来『四轮之塔』\n',
            '并不是单纯的塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45FF(): pass

    label('loc_45FF')

    Jump('loc_48E2')

    def _loc_4602(): pass

    label('loc_4602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_47BB',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4692',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_465E',
    )

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目前\n',
            '舰内没有异常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_468F')

    def _loc_465E(): pass

    label('loc_465E')

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '辛苦了！\n',
            '舰内没有异常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    def _loc_468F(): pass

    label('loc_468F')

    Jump('loc_47B8')

    def _loc_4692(): pass

    label('loc_4692')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4758',
    )

    ChrTalk(
        0x00FE,
        (
            '诸位，辛苦了。\n',
            '舰内的构造已经掌握了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '降落用的升降机\n',
            '是设置在货舱里面哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那边的楼梯一路走到底，\n',
            '靠船尾那一侧的就是货舱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '附近还有工房室，\n',
            '你们最好也能去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_47B8')

    def _loc_4758(): pass

    label('loc_4758')

    ChrTalk(
        0x00FE,
        (
            '降落用的升降机\n',
            '是设置在货舱里面哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那边的楼梯一路走到底，\n',
            '靠船尾那一侧的就是货舱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47B8(): pass

    label('loc_47B8')

    Jump('loc_48E2')

    def _loc_47BB(): pass

    label('loc_47BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_47FE',
    )

    ChrTalk(
        0x00FE,
        (
            '诸位，请抓紧时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙掉落在\n',
            '舰首旁的水面上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48E2')

    def _loc_47FE(): pass

    label('loc_47FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_48E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4894',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，游击士们。\n',
            '各位工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这里往上走就是舰桥，\n',
            '往下则是作战室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于舰内相当宽广，\n',
            '新来的人经常会迷路哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_48E2')

    def _loc_4894(): pass

    label('loc_4894')

    ChrTalk(
        0x00FE,
        (
            '往上走就是舰桥，\n',
            '往下则是作战室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从左右两边的舱门\n',
            '可以前往上甲板。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48E2(): pass

    label('loc_48E2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x48E6
@scena.Code('func_05_48E6')
def func_05_48E6():
    TalkBegin(0x00FE)
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_4B04',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A1C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49B4',
    )

    ChrTalk(
        0x00FE,
        (
            '距离完成陛下的命令\n',
            '就只剩下一座塔了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们全体乘务员都在衷心祈祷\n',
            '殿下能够微笑归来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F谢谢。\n',
            '拜托你们留守了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_4A19')

    def _loc_49B4(): pass

    label('loc_49B4')

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '我们全体乘务员都在衷心祈祷\n',
            '殿下能够旗开得胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请您一定要带着微笑归舰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    def _loc_4A19(): pass

    label('loc_4A19')

    Jump('loc_4B01')

    def _loc_4A1C(): pass

    label('loc_4A1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AAD',
    )

    ChrTalk(
        0x00FE,
        (
            '各位，辛苦了。\n',
            '终于只剩最后一座塔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在完成陛下的命令之前，\n',
            '请千万不要放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也希望各位\n',
            '能够好运常在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_4B01')

    def _loc_4AAD(): pass

    label('loc_4AAD')

    ChrTalk(
        0x00FE,
        (
            '虽然是最后一座塔了，\n',
            '但请千万不要放松警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也希望各位\n',
            '能够好运常在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B01(): pass

    label('loc_4B01')

    Jump('loc_5020')

    def _loc_4B04(): pass

    label('loc_4B04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_4C5D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B75',
    )

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '为了回应守备队的奋战，\n',
            '我们也在竭尽全力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请殿下也多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_4C5A')

    def _loc_4B75(): pass

    label('loc_4B75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C04',
    )

    ChrTalk(
        0x00FE,
        (
            '在卢安近郊也有\n',
            '『结社』的部队袭来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来他们的手下，\n',
            '一直潜伏在王国中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们今后也要\n',
            '更进一步加强警戒才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_4C5A')

    def _loc_4C04(): pass

    label('loc_4C04')

    ChrTalk(
        0x00FE,
        (
            '看来『结社』的手下\n',
            '一直潜伏在王国中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们今后也要\n',
            '更进一步加强警戒才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C5A(): pass

    label('loc_4C5A')

    Jump('loc_5020')

    def _loc_4C5D(): pass

    label('loc_4C5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_4E3B',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CEA',
    )

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在殿下外出期间，\n',
            '我们会好好守护本舰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请放心地\n',
            '完成您的使命吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_4D48')

    def _loc_4CEA(): pass

    label('loc_4CEA')

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '在殿下外出期间，\n',
            '我们会好好守护本舰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请放心地\n',
            '完成您的使命吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    def _loc_4D48(): pass

    label('loc_4D48')

    Jump('loc_4E38')

    def _loc_4D4B(): pass

    label('loc_4D4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4DCE',
    )

    ChrTalk(
        0x00FE,
        (
            '看来蔡斯的\n',
            '情况非常不妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，守备队\n',
            '一定能支撑下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为在危急的情况下，\n',
            '应该能得到要塞的支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_4E38')

    def _loc_4DCE(): pass

    label('loc_4DCE')

    ChrTalk(
        0x00FE,
        (
            '蔡斯的情况虽然也不容乐观，\n',
            '不过暂且应该还支撑得住吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟在危急的情况下\n',
            '应该能得到要塞的支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E38(): pass

    label('loc_4E38')

    Jump('loc_5020')

    def _loc_4E3B(): pass

    label('loc_4E3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_5020',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4F5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EFE',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才科洛蒂娅殿下\n',
            '上了甲板……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知是不是我的心理作用，\n',
            '她的脸色似乎不像平时那么好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来殿下还是在为祖国的困境\n',
            '而伤神劳心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，好可怜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_4F58')

    def _loc_4EFE(): pass

    label('loc_4EFE')

    ChrTalk(
        0x00FE,
        (
            '科洛蒂娅殿下的脸色\n',
            '似乎不像平时那么好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来殿下还在为祖国的困境\n',
            '而伤神劳心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F58(): pass

    label('loc_4F58')

    Jump('loc_5020')

    def _loc_4F5B(): pass

    label('loc_4F5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FD5',
    )

    ChrTalk(
        0x00FE,
        (
            '诸位游击士，\n',
            '请你们好好保护\n',
            '科洛蒂娅殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0019, 0x0105, 400)
    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '也请殿下……\n',
            '多加保重贵体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_5020')

    def _loc_4FD5(): pass

    label('loc_4FD5')

    ChrTalk(
        0x00FE,
        (
            '请你们好好保护\n',
            '科洛蒂娅殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0019, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '也请殿下……\n',
            '多加保重贵体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5020(): pass

    label('loc_5020')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x5024
@scena.Code('func_06_5024')
def func_06_5024():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5096',
    )

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '殿下……\n',
            '请您一定要平安无事。',
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全体乘务员都在祈祷\n',
            '殿下能够旗开得胜。',
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5152')

    def _loc_5096(): pass

    label('loc_5096')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5107',
    )

    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '上尉……\n',
            '请您一定要平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全体乘务员都在祈祷\n',
            '上尉能够旗开得胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5152')

    def _loc_5107(): pass

    label('loc_5107')

    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)

    ChrTalk(
        0x00FE,
        (
            '辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了准备飞翔引擎的测试，\n',
            '大家都聚集到舰桥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5152(): pass

    label('loc_5152')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x5156
@scena.Code('func_07_5156')
def func_07_5156():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#160F◆无台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x5172
@scena.Code('func_08_5172')
def func_08_5172():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_55BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5218',
    )

    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#0110390502V#270F<FIXME>む……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390503V探索の方は進んでいるか？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390321V#1011F<FIXME>うん、えっと……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x0013)

    Return()

    def _loc_5218(): pass

    label('loc_5218')

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
        (0x00000000, 'loc_5276'),
        (0x00000001, 'loc_5570'),
        (0x00000002, 'loc_55B4'),
        (-1, 'loc_55B7'),
    )

    def _loc_5276(): pass

    label('loc_5276')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_540D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5397',
    )

    ChrTalk(
        0x0015,
        (
            '#0110390505V#270F说实话我真没想到能在\n',
            '这么短的时间内修复。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390506V不愧是利贝尔王国……\n',
            '技术人员的水平也很高啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390507V维修员中好像也有人\n',
            '受到过拉赛尔博士的熏陶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390508V#272F身为有心促进祖国的技术力\n',
            '却力有未遂的军人，\n',
            '实在是羡慕至极啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    Jump('loc_540A')

    def _loc_5397(): pass

    label('loc_5397')

    ChrTalk(
        0x0015,
        (
            '#0110390509V#277F维修员中好像也有人\n',
            '受到过拉赛尔博士的熏陶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390510V如果可以的话\n',
            '真想带两三个人回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_540A(): pass

    label('loc_540A')

    Jump('loc_556D')

    def _loc_540D(): pass

    label('loc_540D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54F8',
    )

    ChrTalk(
        0x0015,
        (
            '#0110390511V#272F哎呀，竟然在这么短的时间内\n',
            '修复到如此程度……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390512V#270F不愧是利贝尔王国……\n',
            '技术人员的水平也很高啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390513V维修员中好像也有人\n',
            '受到过拉赛尔博士的熏陶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390514V真是令人羡慕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    Jump('loc_556D')

    def _loc_54F8(): pass

    label('loc_54F8')

    ChrTalk(
        0x0015,
        (
            '#0110390515V#276F维修员中好像也有人\n',
            '受到过拉赛尔博士的熏陶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390516V如果可以的话\n',
            '真想就这样带回帝国去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_556D(): pass

    label('loc_556D')

    Jump('loc_55B7')

    def _loc_5570(): pass

    label('loc_5570')

    ChrTalk(
        0x0015,
        (
            '#0110390517V#277F<FIXME>ん……？\n',
            '編成を組みなおすのか？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0007)

    Jump('loc_55B7')

    def _loc_55B4(): pass

    label('loc_55B4')

    Jump('loc_55B7')

    def _loc_55B7(): pass

    label('loc_55B7')

    Jump('loc_59CC')

    def _loc_55BA(): pass

    label('loc_55BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_55C4',
    )

    Jump('loc_59CC')

    def _loc_55C4(): pass

    label('loc_55C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_55CE',
    )

    Jump('loc_59CC')

    def _loc_55CE(): pass

    label('loc_55CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_59CC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_569C',
    )

    ChrTalk(
        0x0015,
        (
            '#0110390518V#270F首先应该从恢复舰内照明\n',
            '以及确保通路方面开始作业吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390519V因为要动员兵力，\n',
            '就必须先有运输通道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390520V在正式的工程展开之前\n',
            '整顿好这些是非常重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59CC')

    def _loc_569C(): pass

    label('loc_569C')

    ChrTalk(
        0x0015,
        (
            '#0110390521V#270F应该优先进行恢复照明\n',
            '以及确保通路的作业吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390522V因为要动员兵力，\n',
            '就必须先整备好运输通道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390523V在正式的工程展开之前，\n',
            '我打算尽可能地做好准备。',
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
        'loc_59CC',
    )

    ChrTurnDirection(0x0015, 0x0104, 400)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0455, 5, 0x22AD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_597A',
    )

    ChrTalk(
        0x0015,
        (
            '#0110390524V#272F所以说，不好意思，\n',
            '这个吊儿郎当的家伙就交给你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390525V把他丢在舰内的话，\n',
            '老实说我会感到非常为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040390526V#032F你找了这么多借口……\n',
            '其实只是想和尤莉亚上尉\n',
            '两人独处吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390527V你明明已经有我了，\n',
            '却还要去追求女性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390528V#039F啊～你这个没良心的！！\n',
            '难道你想要的只是我的身体！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#0110390529V#274F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390530V……我要说的\n',
            '你们都明白了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390531V#1002F……嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390532V#1035F我们会负责看管他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0455, 5, 0x22AD))

    Jump('loc_59CC')

    def _loc_597A(): pass

    label('loc_597A')

    ChrTurnDirection(0x0015, 0x0104, 400)
    Sleep(400)

    ChrTalk(
        0x0015,
        (
            '#0110390533V#272F那么，各位……\n',
            '这个吊儿郎当的家伙就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_59CC(): pass

    label('loc_59CC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x59D0
@scena.Code('func_09_59D0')
def func_09_59D0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_5E6F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5BB3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B1D',
    )

    ChrTalk(
        0x0016,
        (
            '#0270390723V#140F<FIXME>ふう、何とか\n',
            '船の修理もうまく行きそうですな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390724Vこれで結社の企みを阻止できれば\n',
            '文句なしのハッピーエンドですぜ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390725V#141F俺たちブン屋も\n',
            'きっちり仕事させてもらう\n',
            'つもりですからね。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390726Vここはひとつ、\n',
            'パァッと派手なのを頼みますぜ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_5BB0')

    def _loc_5B1D(): pass

    label('loc_5B1D')

    ChrTalk(
        0x0016,
        (
            '#0270390725V#141F<FIXME>俺たちブン屋も\n',
            'きっちり仕事させてもらう\n',
            'つもりですからね。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390726Vここはひとつ、\n',
            'パァッと派手なのを頼みますぜ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BB0(): pass

    label('loc_5BB0')

    Jump('loc_5E6F')

    def _loc_5BB3(): pass

    label('loc_5BB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5DDD',
    )

    ChrTalk(
        0x0016,
        (
            '#0270390729V#140F虽然我之前还担心了一阵子，\n',
            '不过船的维修看来进行得很顺利呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390730V多亏有了拉赛尔博士，\n',
            '这下子总算是得救了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390731V#141F接下来如果能阻止结社的企图，\n',
            '就是真正圆满的大结局了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390732V我会把特刊的\n',
            '头条位置空出来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390733V希望你们能带来让整个王国沸腾的\n',
            '华丽大结局啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5DD7',
    )

    ChrTurnDirection(0x0016, 0x010F, 400)

    ChrTalk(
        0x0016,
        (
            '#0270390734V#147F<FIXME>あ、ユリア大尉にも\n',
            '是非特集号の見出しに\n',
            '登場してもらって……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100390735V#176F<FIXME>……謹んでお断り申し上げる。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0270390736V#145F<FIXME>（はあ、やっぱダメか……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DD7(): pass

    label('loc_5DD7')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_5E6F')

    def _loc_5DDD(): pass

    label('loc_5DDD')

    ChrTalk(
        0x0016,
        (
            '#0270390737V#141F如果能阻止『结社』的企图，\n',
            '就是真正圆满的大结局了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390738V我会把特刊的\n',
            '头条位置空出来的。\n',
            '期待你们上演的华丽活跃剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E6F(): pass

    label('loc_5E6F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x5E73
@scena.Code('func_0A_5E73')
def func_0A_5E73():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_6076',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6011',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0017,
        (
            '#0280390739V#150F呀呵～！\n',
            '小艾你们好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390740V看起来你们好像要去\n',
            '一个很麻烦的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390741V不过，希望你们能\n',
            '一起回到这里来哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390742V我会为你们拍下\n',
            '打到坏人的纪念照的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390743V#1008F纪、纪念照……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390744V#1054F好像是去旅游一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0280390745V#151F嘿嘿～我的想法不错吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390746V我希望大家都能永远记得\n',
            '我们曾经一起来过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    Jump('loc_6076')

    def _loc_6011(): pass

    label('loc_6011')

    ChrTalk(
        0x0017,
        (
            '#0280390747V#150F最后大家在一起\n',
            '拍张纪念照吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390748V所以，希望大家能\n',
            '一起回到这里来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6076(): pass

    label('loc_6076')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x607A
@scena.Code('func_0B_607A')
def func_0B_607A():
    TalkBegin(0x00FE)
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
        (0x00000000, 'loc_60DB'),
        (0x00000001, 'loc_6819'),
        (0x00000002, 'loc_684D'),
        (-1, 'loc_6850'),
    )

    def _loc_60DB(): pass

    label('loc_60DB')

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
        'loc_637B',
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
            '#0090390756V#416F总、总之……\n',
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
    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    SetScenaFlags(ScenaFlag(0x0454, 0, 0x22A0))

    Jump('loc_6816')

    def _loc_637B(): pass

    label('loc_637B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6404',
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

    Jump('loc_6816')

    def _loc_6404(): pass

    label('loc_6404')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_6504',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64AD',
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
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Jump('loc_6501')

    def _loc_64AD(): pass

    label('loc_64AD')

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

    def _loc_6501(): pass

    label('loc_6501')

    Jump('loc_6816')

    def _loc_6504(): pass

    label('loc_6504')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_6816',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 4, 0x22C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67B1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010390768V#1011F雪拉姐\n',
            '在这里帮忙修理吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0030390769V#020F拉赛尔博士托我\n',
            '检查照明设备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390770V看来似乎很快就能\n',
            '换回正常的照明了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_669A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390771V#561F对、对不起，雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390772V这种事原本\n',
            '应该是我来做的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#0030390773V#021F呵呵，不用客气',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390774V#525F提妲你就集中精力\n',
            '进行探索去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070390775V#560F是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67AB')

    def _loc_669A(): pass

    label('loc_669A')

    ChrTalk(
        0x0101,
        (
            '#0010390776V#1018F啊，已经亮起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390777V#1040F看来修理进行得很顺利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390778V#021F嗯，大家都在努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390779V#525F你们不好好努力的话\n',
            '也会没有面子的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390780V#1006F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390781V#1040F我们会尽快进行探索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_67AB(): pass

    label('loc_67AB')

    SetScenaFlags(ScenaFlag(0x0458, 4, 0x22C4))

    Jump('loc_6816')

    def _loc_67B1(): pass

    label('loc_67B1')

    ChrTalk(
        0x0008,
        (
            '#0030390782V#020F舰内似乎很快就能\n',
            '明亮起来了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390783V目前修复工作\n',
            '看来进行得很顺利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6816(): pass

    label('loc_6816')

    Jump('loc_6853')

    def _loc_6819(): pass

    label('loc_6819')

    ChrTalk(
        0x0008,
        (
            '#0030340489V#020F哎呀？要更换成员了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0007)

    Jump('loc_6853')

    def _loc_684D(): pass

    label('loc_684D')

    Jump('loc_6853')

    def _loc_6850(): pass

    label('loc_6850')

    Jump('loc_6853')

    def _loc_6853(): pass

    label('loc_6853')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x6857
@scena.Code('func_0C_6857')
def func_0C_6857():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    PlaySE(122, 0x01, 0x50)
    OP_71(0x0003, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_76(0x0007, 0x00000002, 0x0001, -4, -1, 0, 0x00, 0x00)
    CameraMove(20, 2000, 97320, 0)
    OP_67(0, 5160, -10000, 0)
    CameraSetDistance(3270, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    OP_BB(0x04, 0x01, 0x0000001D)
    OP_BD()
    ChrSetChipByIndex(0x000A, 20)
    ChrSetChipByIndex(0x0011, 21)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0015, 1630, 250, 97420, 90)
    ChrSetPos(0x0011, -3630, 200, 97420, 270)
    ChrSetPos(0x0101, -1840, 2000, 91330, 0)
    ChrSetPos(0x0102, -750, 2000, 91300, 0)
    ChrSetPos(0x000B, -190, 2000, 89100, 0)
    ChrSetPos(0x0014, -2650, 2000, 88000, 0)
    ChrSetPos(0x0016, -1580, 2000, 87900, 0)
    ChrSetPos(0x0017, -1170, 2000, 87000, 0)
    ChrSetPos(0x0013, -2790, 2000, 90230, 0)
    ChrSetPos(0x0009, -650, 2000, 90170, 0)
    ChrSetPos(0x0008, -1850, 2000, 89910, 0)
    ChrSetPos(0x0012, -3280, 2000, 88660, 0)
    ChrSetPos(0x000A, -2130, 2000, 92320, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    OP_4A(0x000A, 255)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetSubChip(0x000C, 0)
    ChrSetSubChip(0x000E, 0)
    ChrSetSubChip(0x000F, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetChipByIndex(0x000E, 10)
    ChrSetChipByIndex(0x000F, 8)
    ChrSetChipByIndex(0x0010, 9)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000C, -920, 2100, 93680, 0)
    ChrSetPos(0x000E, -1040, 100, 99020, 0)
    ChrSetPos(0x000F, -3400, 100, 98950, 315)
    ChrSetPos(0x0010, 1300, 100, 98950, 45)

    @scena.Lambda('lambda_6ABD')
    def lambda_6ABD():
        OP_7C(1, 1, 2000, 100)
        Yield()

        Jump('lambda_6ABD')

    DispatchAsync2(0x0101, 0x0003, lambda_6ABD)

    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100390001V#176F#2P──安定翼收纳完成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390002V#178F持续加速至最大战速，\n',
            '前往湖上的浮游都市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3530390003V#5P是，长官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0015, 5)
    Sleep(300)

    ChrTalk(
        0x0015,
        (
            '#0110390004V#270F#5P如果敌人出来迎击呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x000C, 2)
    Sleep(200)

    ChrTalk(
        0x000C,
        (
            '#0100390005V#176F#6P……这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390006V#170F如果遇到阻碍的话，就请您强行突破，\n',
            '不过首要目的还是在都市着陆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0110390007V#272F#5P明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390008V#275F顺便说一下，请不必对我客套。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390009V军衔姑且不论，既然\n',
            '我现在的职务是炮兵，\n',
            '就要服从你的指挥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390010V#171F#6P……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6D15')
    def lambda_6D15():
        CameraMove(-650, 2000, 93400, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6D15)

    @scena.Lambda('lambda_6D2D')
    def lambda_6D2D():
        OP_67(0, 5790, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6D2D)

    Sleep(100)

    ChrSetSubChip(0x0015, 3)
    Sleep(100)

    ChrSetSubChip(0x000C, 0)
    Sleep(200)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010390011V#1004F#6P哎，穆拉先生\n',
            '还会担任炮手啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390012V#031F因为他曾在帝国导力化\n',
            '程度最高的机甲师团服役。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390013V别看他长这样，那方面的工作\n',
            '基本上都能胜任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0110390014V#276F#5P……『别看他长这样』是多余的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390015V#1006F#6P原来是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010390016V#1004F#5P对了，奥利维尔，\n',
            '你是什么时候换了衣服的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6EC8')
    def lambda_6EC8():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6EC8)

    Sleep(50)

    @scena.Lambda('lambda_6EDB')
    def lambda_6EDB():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_6EDB)

    Sleep(50)

    @scena.Lambda('lambda_6EEE')
    def lambda_6EEE():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6EEE)

    @scena.Lambda('lambda_6EFC')
    def lambda_6EFC():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6EFC)

    @scena.Lambda('lambda_6F0A')
    def lambda_6F0A():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_6F0A)

    Sleep(50)

    @scena.Lambda('lambda_6F1D')
    def lambda_6F1D():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6F1D)

    @scena.Lambda('lambda_6F2B')
    def lambda_6F2B():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6F2B)

    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020390017V#1040F#5P不是要以帝国皇子的\n',
            '身份进行视察吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390018V#031F#4P哈哈哈。\n',
            '那只是冠冕堂皇的说辞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390019V#030F这段旅程一结束，\n',
            '我那自由且优雅的生活\n',
            '就要宣告终止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390020V至少在那之前，\n',
            '让我再穿一穿这种轻松的服饰吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080390021V#071F#2P哈哈……\n',
            '可以说是你最后的轻松时光吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390022V#025F#6P呼，要是被埃雷波尼亚的\n',
            '国民知道的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390023V#035F#4P就算被知道了\n',
            '我也完全不介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0040390024V#037F#5P如何？二位记者，\n',
            '要不要在利贝尔通讯上爆这个料呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0270390025V#143F哟，真的可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0280390026V#151F那我们就要\n',
            '把照片拍个够了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0110390027V#274F#5P拜托，别把这家伙的\n',
            '胡言乱语都当真了……',
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
            '#0010390028V#1016F#5P嗯，先不说这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390029V#1015F奈尔先生，你们怎么\n',
            '又不知不觉地跟上船来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_726B')
    def lambda_726B():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_726B)

    @scena.Lambda('lambda_7279')
    def lambda_7279():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_7279)

    Sleep(50)

    @scena.Lambda('lambda_728C')
    def lambda_728C():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_728C)

    @scena.Lambda('lambda_729A')
    def lambda_729A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_729A)

    @scena.Lambda('lambda_72A8')
    def lambda_72A8():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_72A8)

    Sleep(100)

    ChrTalk(
        0x000A,
        (
            '#0060390030V#1382F#5P和古代龙事件时一样，\n',
            '是祖母指名让你们随行的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0270390031V#141F嗯，正如您所说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390032V是陛下为我们向卡西乌斯\n',
            '准将美言了几句。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390033V于是我们就作为\n',
            '随军记者登舰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0280390034V#151F我们在哈肯大门也拍下了\n',
            '公主殿下你们的英姿了呢⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390035V请期待冲洗出来的照片哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060390036V#1165F#5P谢、谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050390037V#551F#6P真拿你没办法……\n',
            '怎么一点紧张感也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070320659V#067F#5P哈、哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 0, 400)
    Sleep(300)

    ChrTalk(
        0x0013,
        (
            '#0070390039V#560F#6P说到这个，爷爷。\n',
            '『零力场发生器』的情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_74DB')
    def lambda_74DB():
        CameraMove(-1680, 2000, 94250, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_74DB)

    @scena.Lambda('lambda_74F3')
    def lambda_74F3():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_74F3)

    @scena.Lambda('lambda_7501')
    def lambda_7501():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_7501)

    Sleep(50)

    @scena.Lambda('lambda_7514')
    def lambda_7514():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7514)

    @scena.Lambda('lambda_7522')
    def lambda_7522():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_7522)

    Sleep(50)

    @scena.Lambda('lambda_7535')
    def lambda_7535():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7535)

    @scena.Lambda('lambda_7543')
    def lambda_7543():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7543)

    @scena.Lambda('lambda_7551')
    def lambda_7551():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_7551)

    Sleep(50)

    @scena.Lambda('lambda_7564')
    def lambda_7564():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7564)

    @scena.Lambda('lambda_7572')
    def lambda_7572():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_7572)

    @scena.Lambda('lambda_7580')
    def lambda_7580():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_7580)

    Sleep(500)

    ChrSetSubChip(0x0011, 1)
    Sleep(200)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0011,
        (
            '#0540390040V#100F#5P嗯，现在的状况很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390041V没什么意外的话\n',
            '应该能支撑到降落在\n',
            '浮游都市才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180390042V#1064F#4P请、请等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390043V换句话说……\n',
            '有什么意外就麻烦了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540390044V#104F#5P嗯，\n',
            '肯定会坠落吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390045V#1019F#6P别说得这么干脆啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    Sleep(100)

    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(171, 0x00, 0x64)
    Sleep(800)

    PlaySE(171, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    PlaySE(171, 0x00, 0x64)
    Sleep(700)

    ChrSetSubChip(0x000F, 1)
    Sleep(200)

    ChrSetSubChip(0x0011, 0)
    Sleep(100)

    ChrSetSubChip(0x0011, 2)

    ChrTalk(
        0x000F,
        (
            '#3540390046V#2P雷达有反应……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540390047V#2P隐形舰艇５艘，\n',
            '正急速接近中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(119)
    Sleep(500)

    @scena.Lambda('lambda_77CD')
    def lambda_77CD():
        CameraMove(20, 2000, 97320, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_77CD)

    @scena.Lambda('lambda_77E5')
    def lambda_77E5():
        OP_67(0, 5160, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_77E5)

    ChrSetSubChip(0x0015, 4)

    @scena.Lambda('lambda_7802')
    def lambda_7802():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_7802)

    @scena.Lambda('lambda_7810')
    def lambda_7810():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_7810)

    Sleep(50)

    @scena.Lambda('lambda_7823')
    def lambda_7823():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7823)

    @scena.Lambda('lambda_7831')
    def lambda_7831():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_7831)

    Sleep(50)

    @scena.Lambda('lambda_7844')
    def lambda_7844():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_7844)

    @scena.Lambda('lambda_7852')
    def lambda_7852():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_7852)

    Sleep(50)

    @scena.Lambda('lambda_7865')
    def lambda_7865():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7865)

    @scena.Lambda('lambda_7873')
    def lambda_7873():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_7873)

    Sleep(50)

    @scena.Lambda('lambda_7886')
    def lambda_7886():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7886)

    @scena.Lambda('lambda_7894')
    def lambda_7894():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_7894)

    Sleep(50)

    @scena.Lambda('lambda_78A7')
    def lambda_78A7():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_78A7)

    ChrSetSubChip(0x000F, 0)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0015,
        (
            '#0110390048V#270F#5P来了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390049V#1042F似乎是『方舟』所搭载的\n',
            '高速艇呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540390050V#102F#5P呼，总算识破了\n',
            '敌人的隐形技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390051V#177F#2P──准备展开主炮！\n',
            '维持最大战速强行突破！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390052V#177F只攻击挡路的舰艇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#1K#5P YES·SIR！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000F,
        (
            '#1K#6P YES·SIR！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0010,
        (
            '#3850390055V#1K#4P YES·SIR！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    OP_56(0x01)
    OP_59()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    NewScene('ED6_DT21/E0810._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x7A3A
@scena.Code('func_0D_7A3A')
def func_0D_7A3A():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    OP_71(0x0003, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_76(0x0007, 0x00000000, 0x0001, -30, 0, 0, 0x00, 0x00)
    OP_76(0x0007, 0x00000001, 0x0001, -5, 0, 0, 0x00, 0x00)
    OP_76(0x0007, 0x00000002, 0x0001, -7, -1, 0, 0x00, 0x00)
    PlaySE(122, 0x01, 0x50)
    CameraMove(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    CameraSetDistance(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    ChrSetChipByIndex(0x000A, 20)
    ChrSetChipByIndex(0x0011, 21)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0015, 1630, 200, 97420, 90)
    ChrSetPos(0x0011, -3630, 200, 97420, 270)
    ChrSetPos(0x0101, -1840, 2000, 91330, 0)
    ChrSetPos(0x0102, -750, 2000, 91300, 0)
    ChrSetPos(0x000B, -190, 2000, 89100, 0)
    ChrSetPos(0x0014, -2650, 2000, 88000, 0)
    ChrSetPos(0x0016, -1580, 2000, 87900, 0)
    ChrSetPos(0x0017, -1170, 2000, 87000, 0)
    ChrSetPos(0x0013, -2790, 2000, 90230, 0)
    ChrSetPos(0x0009, -650, 2000, 90170, 0)
    ChrSetPos(0x0008, -1850, 2000, 89910, 0)
    ChrSetPos(0x0012, -3280, 2000, 88660, 0)
    ChrSetPos(0x000A, -2130, 2000, 92320, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    OP_4A(0x000A, 255)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetSubChip(0x000C, 0)
    ChrSetSubChip(0x000E, 0)
    ChrSetSubChip(0x000F, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetChipByIndex(0x000E, 10)
    ChrSetChipByIndex(0x000F, 8)
    ChrSetChipByIndex(0x0010, 9)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000C, -920, 2100, 93680, 0)
    ChrSetPos(0x000E, -1040, 100, 99020, 0)
    ChrSetPos(0x000F, -3400, 100, 98950, 315)
    ChrSetPos(0x0010, 1300, 100, 98950, 45)

    @scena.Lambda('lambda_7CC1')
    def lambda_7CC1():
        OP_7C(1, 1, 2000, 100)
        Yield()

        Jump('lambda_7CC1')

    DispatchAsync2(0x0101, 0x0003, lambda_7CC1)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#3540390056V#2P１号、２号、５号敌舰已击坠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540390057V#2P３号和４号\n',
            '也已经完全甩开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390058V#1018F#6P成功了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080390059V#070F#4P嗯，真漂亮！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040390060V#035F#4P哎呀……\n',
            '这就是最尖端的空战吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0110390061V#277F#5P嗯……\n',
            '这座主炮很厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390062V威力非常强大，\n',
            '而且射击精度高，后坐力也小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0011, 2)
    Sleep(200)

    ChrTalk(
        0x0011,
        (
            '#0540390063V#101F#6P哇哈哈，那当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390064V#100F本来我还想装上和雷达\n',
            '连动的迎击炮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390065V#104F不过，这个课题就留到下次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(171, 0x00, 0x64)
    Sleep(800)

    PlaySE(171, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    PlaySE(171, 0x00, 0x64)
    Sleep(700)

    ChrSetSubChip(0x000F, 1)
    Sleep(200)

    Sleep(100)

    ChrTalk(
        0x000F,
        (
            '#3540390046V#2P雷达有反应……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540390067V#2P８点钟方向\n',
            '有一艘全长２５０亚矩的\n',
            '巨型战舰正在接近中……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x000F, 0)
    ChrSetSubChip(0x0011, 0)

    ChrTalk(
        0x0101,
        (
            '#0010390068V#1020F#6P那、那是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180390069V#1063F#4P就是那艘『方舟』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x000C, 2)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0100390070V#178F#5P……约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390071V你了解『方舟』的\n',
            '基本性能和武装吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390072V#1035F机动性和最大战速\n',
            '都不及『埃尔赛尤』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390073V#1042F但是，它不仅有强力的主炮，\n',
            '舰身还被无数的自动炮塔所守护着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390074V攻击、防御都一样无懈可击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390075V#176F#5P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x000C, 0)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0100390076V#177F#2P向４点钟方向全速脱离！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390077V一边躲开敌人战列舰的追击，\n',
            '一边朝浮游都市上空前进！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3530390078V#5P是，长官！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x03, 0x01, 0x000F)
    OP_20(0x000003E8)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_C4(0x00, 0x00000010)
    Yield()
    FadeIn(1, 0)
    PlayMovie(0x00, 'ED6_DT43.dat', 0x0000, 0x0001)
    def _loc_8272(): pass

    label('loc_8272')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_828C',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_8289',
    )

    Jump('loc_828C')

    def _loc_8289(): pass

    label('loc_8289')

    Jump('loc_8272')

    def _loc_828C(): pass

    label('loc_828C')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    OP_C4(0x01, 0x00000010)
    CameraMove(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    CameraSetDistance(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    StopEffect(0x00, 0x00)
    OP_20(0x000007D0)
    Sleep(1000)

    PlaySE(122, 0x01, 0x50)
    FadeIn(1000, 0)
    OP_0D()
    OP_21()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#3540390079V#2P……已脱离『方舟』的\n',
            '射程范围了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060390080V#1167F#6P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070390081V#562F#6P好、好可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030390082V#025F#6P真是惊心动魄啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390083V#1007F#6P嗯，心脏跳得好快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390084V#1006F不过，现在可以说已经\n',
            '完全躲过敌人的攻击了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390085V#1042F#2P不……还不能掉以轻心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050390086V#057F#4P嗯，这个对手不能用常理来衡量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390087V直到最后一刻\n',
            '都不能够大意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(171, 0x00, 0x64)
    Sleep(800)

    PlaySE(171, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    PlaySE(171, 0x00, 0x64)
    Sleep(700)

    ChrSetSubChip(0x000F, 1)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#3540390088V#2P前方的云散开了……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3540390089V已经来到浮游都市上空……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x03, 0x01, 0x000F)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetSubChip(0x000F, 0)
    OP_C4(0x00, 0x00000010)
    FadeIn(1, 0)
    PlayMovie(0x00, 'ED6_DT44.dat', 0x0083, 0x0001)
    def _loc_85C5(): pass

    label('loc_85C5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_85DF',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_85DC',
    )

    Jump('loc_85DF')

    def _loc_85DC(): pass

    label('loc_85DC')

    Jump('loc_85C5')

    def _loc_85DF(): pass

    label('loc_85DF')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(2000)

    OP_C4(0x01, 0x00000010)
    CameraMove(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    CameraSetDistance(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    LoadChip('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP', 29)
    ChrSetSubChip(0x0017, 0)
    ChrSetChipByIndex(0x0017, 29)
    ChrSetSubChip(0x0011, 2)
    ChrSetSubChip(0x0015, 4)
    StopEffect(0x00, 0x00)
    PlaySE(122, 0x01, 0x50)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#3530390090V#5P到、到达都市上空了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390091V#1020F#6P………好壮观……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060390092V#1162F#6P这个……\n',
            '就是古代塞姆里亚文明的精华吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180390093V#1063F#4P……真是超乎想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540390094V#102F#6P嗯……前方可以\n',
            '看到一根巨大的柱子般的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390095V应该是这座都市的\n',
            '重要设施之一才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390096V如果要着陆的话，\n',
            '在那附近可能会比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x000C, 1)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0100390097V#176F#2P明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390098V#178F艾柯，周围情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x000F, 1)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#3540390099V#2P……是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540390100V#2P５０塞尔矩以内\n',
            '没有敌舰的反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3540390101V#2P可以认为已经完全\n',
            '甩掉了『方舟』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390102V#176F#2P好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x000C, 0)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0100390103V#170F#2P勒克司，一边减速一边\n',
            '降落在前方的『柱子』附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000F, 0)

    ChrTalk(
        0x000E,
        (
            '#3530390104V#5P是，长官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8976')
    def lambda_8976():
        CameraMove(-420, 2000, 92420, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8976)

    @scena.Lambda('lambda_898E')
    def lambda_898E():
        OP_67(0, 5790, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_898E)

    OP_62(0x0017, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    WaitForThreadExit(0x0101, 0x0001)
    OP_63(0x0017)
    Fade(250)
    ChrSetSubChip(0x0017, 0)
    ChrSetChipByIndex(0x0017, 23)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0017,
        (
            '#0280390105V#153F#4P咦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_89FA')
    def lambda_89FA():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_89FA)

    @scena.Lambda('lambda_8A08')
    def lambda_8A08():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_8A08)

    Sleep(50)

    @scena.Lambda('lambda_8A1B')
    def lambda_8A1B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8A1B)

    @scena.Lambda('lambda_8A29')
    def lambda_8A29():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_8A29)

    Sleep(50)

    @scena.Lambda('lambda_8A3C')
    def lambda_8A3C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_8A3C)

    @scena.Lambda('lambda_8A4A')
    def lambda_8A4A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8A4A)

    @scena.Lambda('lambda_8A58')
    def lambda_8A58():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_8A58)

    Sleep(50)

    @scena.Lambda('lambda_8A6B')
    def lambda_8A6B():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_8A6B)

    @scena.Lambda('lambda_8A79')
    def lambda_8A79():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_8A79)

    Sleep(50)

    @scena.Lambda('lambda_8A8C')
    def lambda_8A8C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_8A8C)

    @scena.Lambda('lambda_8A9A')
    def lambda_8A9A():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_8A9A)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010390106V#1004F#5P怎么了？朵洛希？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0270390107V#142F#5P怎么了？\n',
            '感光结晶回路用完了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0280390108V#154F#4P啊，不是的。\n',
            '这个没有问题～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390109V我发觉前面好像有奇怪的\n',
            '东西在接近～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0016,
        (
            '#0270390110V#144F#5P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390111V#1020F#5P不、不会吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    @scena.Lambda('lambda_8CC6')
    def lambda_8CC6():
        CameraMove(20, 2000, 97320, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8CC6)

    @scena.Lambda('lambda_8CDE')
    def lambda_8CDE():
        OP_67(0, 5160, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8CDE)

    @scena.Lambda('lambda_8CF6')
    def lambda_8CF6():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_8CF6)

    @scena.Lambda('lambda_8D04')
    def lambda_8D04():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8D04)

    @scena.Lambda('lambda_8D12')
    def lambda_8D12():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_8D12)

    Sleep(50)

    @scena.Lambda('lambda_8D25')
    def lambda_8D25():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8D25)

    @scena.Lambda('lambda_8D33')
    def lambda_8D33():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_8D33)

    Sleep(50)

    @scena.Lambda('lambda_8D46')
    def lambda_8D46():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8D46)

    Sleep(50)

    @scena.Lambda('lambda_8D59')
    def lambda_8D59():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_8D59)

    Sleep(50)

    @scena.Lambda('lambda_8D6C')
    def lambda_8D6C():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_8D6C)

    Sleep(50)

    @scena.Lambda('lambda_8D7F')
    def lambda_8D7F():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_8D7F)

    @scena.Lambda('lambda_8D8D')
    def lambda_8D8D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_8D8D)

    ChrSetSubChip(0x0015, 4)
    ChrSetSubChip(0x0011, 2)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    OP_21()

    ChrTalk(
        0x000C,
        (
            '#0100390112V#173F#2P──那、那是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x03, 0x01, 0x000F)
    FadeOut(1200, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/E0810._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x8DFA
@scena.Code('func_0E_8DFA')
def func_0E_8DFA():
    EventBegin(0x00)
    LoadChip('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP', 29)
    LoadChip('ED6_DT27/CH03015._CH', 'ED6_DT27/CH03015P._CP', 30)
    LoadChip('ED6_DT07/CH00025._CH', 'ED6_DT07/CH00025P._CP', 31)
    LoadChip('ED6_DT07/CH00035._CH', 'ED6_DT07/CH00035P._CP', 32)
    LoadChip('ED6_DT07/CH00055._CH', 'ED6_DT07/CH00055P._CP', 33)
    LoadChip('ED6_DT07/CH00065._CH', 'ED6_DT07/CH00065P._CP', 34)
    LoadChip('ED6_DT07/CH00075._CH', 'ED6_DT07/CH00075P._CP', 35)
    LoadChip('ED6_DT27/CH03085._CH', 'ED6_DT27/CH03085P._CP', 36)
    LoadChip('ED6_DT27/CH03215._CH', 'ED6_DT27/CH03215P._CP', 37)
    LoadChip('ED6_DT06/CH20087._CH', 'ED6_DT06/CH20087P._CP', 38)
    LoadChip('ED6_DT06/CH20122._CH', 'ED6_DT06/CH20122P._CP', 39)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    OP_71(0x0003, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_76(0x0007, 0x00000002, 0x0001, -4, -1, 0, 0x00, 0x00)
    PlaySE(122, 0x01, 0x50)
    CameraMove(-340, 2000, 93880, 0)
    OP_67(0, 5960, -10000, 0)
    CameraSetDistance(3100, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetChipByIndex(0x000A, 20)
    ChrSetChipByIndex(0x0011, 21)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetPos(0x0015, 1630, 200, 97420, 90)
    ChrSetPos(0x0011, -3630, 200, 97420, 270)
    ChrSetPos(0x000C, -1090, 2000, 93560, 0)
    ChrSetPos(0x0101, -1840, 2000, 91330, 0)
    ChrSetPos(0x0102, -750, 2000, 91300, 0)
    ChrSetPos(0x000B, -190, 2000, 89100, 0)
    ChrSetPos(0x0014, -2650, 2000, 88000, 0)
    ChrSetPos(0x0016, -1580, 2000, 87900, 0)
    ChrSetPos(0x0017, -1170, 2000, 87000, 0)
    ChrSetPos(0x0013, -2790, 2000, 90230, 0)
    ChrSetPos(0x0009, -760, 2000, 90170, 0)
    ChrSetPos(0x0008, -1790, 2000, 89910, 0)
    ChrSetPos(0x0012, -3280, 2000, 88660, 0)
    ChrSetPos(0x000A, -2130, 2000, 92320, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    TerminateThread(0x000C, 0x00)
    OP_4A(0x000A, 255)
    ChrSetChipByIndex(0x0101, 29)
    ChrSetChipByIndex(0x0102, 30)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetChipByIndex(0x0009, 32)
    ChrSetChipByIndex(0x0012, 33)
    ChrSetChipByIndex(0x0013, 34)
    ChrSetChipByIndex(0x000B, 35)
    ChrSetChipByIndex(0x0014, 36)
    ChrSetChipByIndex(0x000A, 37)
    ChrSetChipByIndex(0x0016, 38)
    ChrSetChipByIndex(0x0017, 39)
    PlaySE(133, 0x00, 0x64)

    @scena.Lambda('lambda_9087')
    def lambda_9087():
        OP_7C(100, 0, 1000, 3000)
        Yield()

        Jump('lambda_9087')

    DispatchAsync2(0x0101, 0x0003, lambda_9087)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010390115V#1000F#4P啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390116V#1030F………刚才是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540390117V#100F#2P不好！\n',
            '左翼被切断了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540390118V反重力力场也在下降！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3530390119V#1P舵、舵变得难以掌控了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0015, 4)
    Sleep(200)

    ChrTalk(
        0x0015,
        (
            '#0110390120V#270F……我来帮忙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    ChrSetPos(0x0015, 580, 0, 97840, 270)
    ChrSetSubChip(0x0015, 0)
    ChrSetChipByIndex(0x0015, 24)
    OP_0D()
    ChrWalkTo(0x0015, -1880, 0, 98090, 5000, 0x00)
    ChrWalkTo(0x0015, -1740, 0, 99040, 5000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0100390121V#170F#4P可恶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390122V全体人员准备抗冲击！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390123V埃尔赛尤号，紧急着陆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_23(0x0085)
    OP_23(0x007A)
    OP_0D()
    TerminateThread(0x0101, 0x03)
    Sleep(2000)

    OP_C4(0x00, 0x00000010)
    FadeIn(1, 0)
    PlayMovie(0x00, 'ED6_DT45.dat', 0x0000, 0x0001)
    def _loc_9299(): pass

    label('loc_9299')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_92B3',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_92B0',
    )

    Jump('loc_92B3')

    def _loc_92B0(): pass

    label('loc_92B0')

    Jump('loc_9299')

    def _loc_92B3(): pass

    label('loc_92B3')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(2000)

    OP_C4(0x01, 0x00000010)
    OP_AD('ED6_DT24/C_VIS149._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    PlaySE(133, 0x00, 0x64)
    Sleep(3000)

    OP_23(0x0085)
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x930B
@scena.Code('func_0F_930B')
def func_0F_930B():
    OP_24(0x007A, 0x46)
    Sleep(200)

    OP_24(0x007A, 0x3C)
    Sleep(200)

    OP_24(0x007A, 0x32)
    Sleep(200)

    OP_24(0x007A, 0x28)
    Sleep(200)

    OP_24(0x007A, 0x1E)
    Sleep(200)

    OP_24(0x007A, 0x14)
    Sleep(200)

    OP_23(0x007A)

    Return()

# id: 0x0010 offset: 0x9345
@scena.Code('func_10_9345')
def func_10_9345():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_23(0x007A)
    LoadChip('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP', 5)
    LoadChip('ED6_DT07/CH00065._CH', 'ED6_DT07/CH00065P._CP', 6)
    LoadChip('ED6_DT26/CH20376._CH', 'ED6_DT26/CH20376P._CP', 29)
    LoadChip('ED6_DT27/CH03015._CH', 'ED6_DT27/CH03015P._CP', 30)
    LoadChip('ED6_DT07/CH00025._CH', 'ED6_DT07/CH00025P._CP', 31)
    LoadChip('ED6_DT07/CH00035._CH', 'ED6_DT07/CH00035P._CP', 32)
    LoadChip('ED6_DT27/CH03215._CH', 'ED6_DT27/CH03215P._CP', 33)
    LoadChip('ED6_DT07/CH00055._CH', 'ED6_DT07/CH00055P._CP', 34)
    LoadChip('ED6_DT26/CH20216._CH', 'ED6_DT26/CH20216P._CP', 35)
    LoadChip('ED6_DT07/CH00075._CH', 'ED6_DT07/CH00075P._CP', 36)
    LoadChip('ED6_DT27/CH03085._CH', 'ED6_DT27/CH03085P._CP', 37)
    LoadChip('ED6_DT06/CH20087._CH', 'ED6_DT06/CH20087P._CP', 38)
    LoadChip('ED6_DT26/CH20285._CH', 'ED6_DT26/CH20285P._CP', 39)
    LoadChip('ED6_DT06/CH20104._CH', 'ED6_DT06/CH20104P._CP', 40)
    LoadChip('ED6_DT06/CH20028._CH', 'ED6_DT06/CH20028P._CP', 41)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 29)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 30)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 32)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x000A, 33)
    ChrSetSubChip(0x0012, 0)
    ChrSetChipByIndex(0x0012, 34)
    ChrSetSubChip(0x0013, 0)
    ChrSetChipByIndex(0x0013, 35)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 36)
    ChrSetSubChip(0x0014, 0)
    ChrSetChipByIndex(0x0014, 37)
    ChrSetSubChip(0x0016, 0)
    ChrSetChipByIndex(0x0016, 38)
    ChrSetSubChip(0x0017, 0)
    ChrSetChipByIndex(0x0017, 39)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetSubChip(0x0011, 24)
    ChrSetChipByIndex(0x0011, 21)
    ChrSetFlags(0x0015, 0x0002)
    ChrSetSubChip(0x0015, 24)
    ChrSetChipByIndex(0x0015, 19)
    ChrSetSubChip(0x000C, 0)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetFlags(0x000E, 0x0002)
    ChrSetSubChip(0x000E, 24)
    ChrSetChipByIndex(0x000E, 10)
    ChrSetFlags(0x000F, 0x0002)
    ChrSetSubChip(0x000F, 24)
    ChrSetChipByIndex(0x000F, 8)
    ChrSetFlags(0x0010, 0x0002)
    ChrSetSubChip(0x0010, 24)
    ChrSetChipByIndex(0x0010, 9)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    CameraMove(790, 2000, 90690, 0)
    OP_67(0, 6200, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TerminateThread(0x000C, 0x00)
    OP_4A(0x000A, 255)
    ChrSetFlags(0x0017, 0x0004)
    ChrSetFlags(0x0017, 0x0040)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0016, 1300, 2000, 88300, 90)
    ChrSetPos(0x0017, 2000, 1900, 87630, 180)
    ChrSetPos(0x000C, -1960, 2000, 93000, 180)
    ChrSetPos(0x000A, -2110, 2000, 92110, 0)
    ChrSetPos(0x0009, 0, 2000, 88300, 0)
    ChrSetPos(0x0008, -1200, 2000, 88440, 45)
    ChrSetPos(0x0013, -2800, 2000, 89500, 90)
    ChrSetPos(0x0012, -2600, 2000, 88360, 0)
    ChrSetPos(0x000B, -2100, 2000, 86560, 0)
    ChrSetPos(0x0101, -300, 1500, 90550, 270)
    ChrSetPos(0x0102, -400, 2000, 91290, 180)
    ChrSetPos(0x0014, 600, 2000, 90100, 270)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0800)
    ChrClearFlags(0x0101, 0x0001)
    ChrSetSubChip(0x0101, 4)
    ChrSetFlags(0x0015, 0x0004)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0015, 1630, 200, 97420, 90)
    ChrSetPos(0x0011, -3630, 200, 97420, 270)
    SetMessageWindowPos(150, 100, -1, -1)
    TalkSetChrName('少年的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0020390124V……………艾………蒂尔…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390125V……艾丝……尔………醒醒………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(250, 120, -1, -1)
    TalkSetChrName('青年的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0180390126V……你没事吧……\n',
            '………艾丝……蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(180, 200, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010390127V#1003F……嗯…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(100)

    ChrSetSubChip(0x0101, 7)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010390128V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180390129V#1062F#2P太好了……你醒了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390130V#1043F#5P你没事吧？\n',
            '有没有受伤？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 3000)
    ChrSetSubChip(0x0101, 5)
    Sleep(700)

    ChrTalk(
        0x0101,
        (
            '#0010390131V#1013F#4P啊……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrSetPos(0x0101, -340, 2000, 90400, 270)
    ChrSetFlags(0x0101, 0x0001)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetDirection(0x0101, 270, 0)
    OP_0D()
    Sleep(300)

    OP_9E(0x0101, 15, 0, 300, 3000)
    Fade(250)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    ChrSetDirection(0x0101, 45, 400)
    Sleep(500)

    Fade(250)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 65535)
    OP_0D()
    Fade(250)
    ChrSetSubChip(0x0014, 0)
    ChrSetChipByIndex(0x0014, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010390132V#1025F#6P……只是膝盖\n',
            '稍微擦伤而已……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390133V#1003F………大家呢………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9935')
    def lambda_9935():
        CameraMove(-230, 2000, 89260, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9935)

    @scena.Lambda('lambda_994D')
    def lambda_994D():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_994D)

    Sleep(100)

    @scena.Lambda('lambda_9960')
    def lambda_9960():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9960)

    Sleep(100)

    @scena.Lambda('lambda_9973')
    def lambda_9973():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_9973)

    WaitForThreadExit(0x0101, 0x0001)
    OP_9E(0x0012, 15, 0, 500, 3000)
    Fade(250)
    ChrSetSubChip(0x0012, 0)
    ChrSetChipByIndex(0x0012, 15)
    OP_0D()
    Sleep(300)

    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x0012,
        (
            '#0050390134V#552F#6P嗯，总算都没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0013, 15, 0, 300, 3000)
    Fade(250)
    ChrSetSubChip(0x0013, 0)
    ChrSetChipByIndex(0x0013, 6)
    ChrSetDirection(0x0013, 90, 0)
    OP_0D()
    Sleep(300)

    OP_9E(0x0013, 15, 0, 300, 3000)
    Fade(250)
    ChrSetSubChip(0x0013, 0)
    ChrSetChipByIndex(0x0013, 16)
    ChrSetDirection(0x0013, 90, 0)
    OP_0D()

    ChrTalk(
        0x0013,
        (
            '#0070390135V#562F#6P……呼、呼………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000A, 15, 0, 500, 3000)
    Fade(250)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x000A, 20)
    ChrTurnDirection(0x0013, 0x0101, 400)
    OP_0D()
    ChrSetDirection(0x000A, 180, 400)
    Sleep(200)

    ChrSetDirection(0x000C, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#0060390136V#1381F我、我……没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 15, 0, 300, 3000)
    Fade(250)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 1)
    OP_0D()
    Sleep(300)

    ChrTurnDirection(0x0009, 0x0101, 0)

    ChrTalk(
        0x0009,
        (
            '#0040390137V#034F哎呀呀……\n',
            '好惊险啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 15, 0, 500, 3000)
    Fade(250)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    ChrClearFlags(0x0008, 0x0004)
    OP_0D()
    Sleep(300)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0030390138V#025F#6P呼……\n',
            '还以为没救了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000B, 15, 0, 500, 3000)
    Fade(250)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrClearFlags(0x000B, 0x0004)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0080390139V#572F#6P可以说是\n',
            '九死一生呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0017, 0xFFFFFED4, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0017,
        (
            '#0280390140V#151F#5P……嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390141V这么多东西……\n',
            '我怎么吃得完嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0x00000096, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0016,
        (
            '#0270390142V#145F#6P唉……真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390143V#144F喂，朵洛希！\n',
            '已经是早上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0017, 15, 0, 500, 3000)
    Fade(500)
    ChrSetSubChip(0x0017, 0)
    ChrSetChipByIndex(0x0017, 23)
    ChrSetPos(0x0017, 2430, 2000, 87860, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0017,
        (
            '#0280390144V#153F#2P啊……奈尔前辈……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetSubChip(0x0016, 0)
    ChrSetChipByIndex(0x0016, 22)
    ChrTurnDirection(0x0016, 0x0017, 0)
    OP_0D()
    Sleep(300)

    @scena.Lambda('lambda_9D51')
    def lambda_9D51():
        CameraMove(-1070, 2000, 94550, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9D51)

    @scena.Lambda('lambda_9D69')
    def lambda_9D69():
        OP_67(0, 6250, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9D69)

    @scena.Lambda('lambda_9D81')
    def lambda_9D81():
        CameraSetDistance(3300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_9D81)

    ChrSetDirection(0x000C, 0, 200)
    ChrWalkTo(0x000C, -1920, 2000, 94380, 1000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100390145V#178F#6P你们怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrClearFlags(0x0015, 0x0002)
    ChrSetSubChip(0x0015, 2)
    ChrSetChipByIndex(0x0015, 19)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0015,
        (
            '#0110390146V#272F#5P……没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_9E(0x0011, 15, 0, 500, 3000)
    Fade(250)
    ChrClearFlags(0x0011, 0x0002)
    ChrSetSubChip(0x0011, 1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0011,
        (
            '#0540390147V#102F#5P总、总算平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000F, 15, 0, 500, 3000)
    Fade(250)
    ChrClearFlags(0x000F, 0x0002)
    ChrSetSubChip(0x000F, 0)
    ChrSetChipByIndex(0x000F, 8)
    OP_0D()
    ChrSetSubChip(0x000F, 1)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#3540390148V#2P……没问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000E, 15, 0, 500, 3000)
    Fade(250)
    ChrClearFlags(0x000E, 0x0002)
    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x000E, 10)
    OP_0D()
    ChrSetSubChip(0x000E, 1)
    Sleep(300)

    ChrTalk(
        0x000E,
        (
            '#3530390149V#5P我、我们这边也还好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0010, 15, 0, 500, 3000)
    Fade(250)
    ChrClearFlags(0x0010, 0x0002)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x0010, 9)
    OP_0D()
    ChrSetSubChip(0x0010, 2)
    Sleep(300)

    ChrTalk(
        0x0010,
        (
            '#3850390150V#5P还、还以为要死了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0100390151V#176F#6P……简直是奇迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390152V#175F或者说……\n',
            '只是对方手下留情了吗……',
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
            '#0010390153V#1020F#5P对、对了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A02A')
    def lambda_A02A():
        CameraMove(130, 2000, 91180, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A02A)

    @scena.Lambda('lambda_A042')
    def lambda_A042():
        OP_67(0, 5740, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A042)

    @scena.Lambda('lambda_A05A')
    def lambda_A05A():
        CameraSetDistance(3300, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A05A)

    @scena.Lambda('lambda_A06A')
    def lambda_A06A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_A06A)

    Sleep(50)

    @scena.Lambda('lambda_A07D')
    def lambda_A07D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A07D)

    Sleep(50)

    @scena.Lambda('lambda_A090')
    def lambda_A090():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_A090)

    Sleep(50)

    @scena.Lambda('lambda_A0A3')
    def lambda_A0A3():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_A0A3)

    Sleep(50)

    @scena.Lambda('lambda_A0B6')
    def lambda_A0B6():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_A0B6)

    Sleep(50)

    ChrSetDirection(0x000C, 180, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010390154V#1020F#6P刚才骑在攻击埃尔赛尤的\n',
            '那个黑色家伙上的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390155V#1035F#5P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390156V#1042F肯定是莱维没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050390157V#057F#6P……那家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080390158V#074F#6P这样看来的话，\n',
            '或许的确是手下留情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390159V#072F只要他愿意的话，\n',
            '我们已经完全被击落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390160V#1007F#6P……心情真复杂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390161V#1043F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0060390162V#1163F#5P说起来……\n',
            '我们坠落在哪里了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100390163V#176F#5P好像是在浮游都市的外围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390164V#178F看来先到外面去\n',
            '确认一下状况比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5900._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0xA334
@scena.Code('func_11_A334')
def func_11_A334():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    PlaySE(122, 0x01, 0x50)
    OP_6F(0x000C, 0)
    CameraMove(1350, 2000, 100510, 0)
    OP_67(0, 5430, -10000, 0)
    CameraSetDistance(3100, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetChipByIndex(0x0015, 19)
    ChrSetChipByIndex(0x000A, 20)
    ChrSetChipByIndex(0x0011, 21)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetPos(0x0015, 1630, 200, 97420, 90)
    ChrSetPos(0x0011, -3630, 200, 97420, 270)
    ChrSetPos(0x000C, -920, 2100, 93680, 0)
    ChrSetPos(0x000A, -2130, 2000, 92320, 0)
    ChrSetPos(0x0013, -1810, 2000, 91450, 0)
    ChrSetPos(0x0008, -420, 2000, 91880, 0)
    ChrSetPos(0x0012, -2780, 2000, 90100, 0)
    ChrSetPos(0x0009, 90, 2000, 90050, 0)
    ChrSetPos(0x0014, -1020, 2000, 90470, 0)
    ChrSetPos(0x000B, -2200, 2000, 88980, 0)
    ChrSetPos(0x0016, -990, 2000, 88600, 0)
    ChrSetPos(0x0017, 100, 2000, 88430, 0)
    ChrSetPos(0x0010, 1300, 100, 98950, 45)
    ChrSetSubChip(0x0010, 0)
    ChrSetChipByIndex(0x0010, 9)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    TerminateThread(0x000C, 0x00)
    TerminateThread(0x0016, 0x00)
    TerminateThread(0x0017, 0x00)
    TerminateThread(0x0010, 0x00)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0015, 255)
    ChrSetSubChip(0x0015, 1)
    ChrSetSubChip(0x0010, 1)
    ChrSetSubChip(0x0011, 2)
    ChrSetSubChip(0x000F, 2)
    OP_76(0x0007, 0x00000000, 0x0001, -9, 0, 0, 0x00, 0x00)
    OP_76(0x0007, 0x00000001, 0x0001, -2, 0, 0, 0x00, 0x00)
    OP_76(0x0007, 0x00000002, 0x0001, -2, 0, 0, 0x00, 0x00)

    @scena.Lambda('lambda_A545')
    def lambda_A545():
        CameraMove(670, 2000, 94500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A545)

    @scena.Lambda('lambda_A55D')
    def lambda_A55D():
        OP_67(0, 5400, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A55D)

    @scena.Lambda('lambda_A575')
    def lambda_A575():
        CameraSetDistance(3420, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A575)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0030421142V#023F#6P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0180421143V#1067F#6P没、没赶得上吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0050421144V#055F#6P不、不会吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0070421145V#065F#5P讨、讨厌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_62(0x0013, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0013,
        (
            '#0070421146V#069F#5P#3S不要啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060421147V#1166F#6P尤莉亚小姐！\n',
            '拜托了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060421148V从避难通道的方向来考虑\n',
            '艾丝蒂尔她们\n',
            '应该在西北边！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060421149V请把埃尔赛尤号开往那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100421150V#175F#5P……非常抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100421151V即便是殿下的命令，\n',
            '也请恕我……无法遵命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0110421152V#272F#5P……埃尔赛尤号的动力\n',
            '也没有完全恢复。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110421153V如果现在再次接近浮游都市，\n',
            '肯定会被卷入崩塌之中的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110421154V#276F是这样吧，拉赛尔博士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0540421155V#102F#6P……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060421156V#1169F#6P……怎、怎么会…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040421157V#034F#6P哈哈……真失败……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040421158V想要缓和气氛，\n',
            '脑子里却一片空白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080421159V#572F#6P……嗯，我也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0270421160V#145F#6P这两个家伙……呜呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270421161V都已经走到这一步了……\n',
            '……竟然会变成这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0280421162V#156F#4P小艾……\n',
            '……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0017,
        (
            '#0280421163V#153F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A9E6')
    def lambda_A9E6():
        CameraMove(890, 2000, 93900, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A9E6)

    @scena.Lambda('lambda_A9FE')
    def lambda_A9FE():
        OP_67(0, 5800, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A9FE)

    @scena.Lambda('lambda_AA16')
    def lambda_AA16():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_AA16)

    Sleep(50)

    @scena.Lambda('lambda_AA29')
    def lambda_AA29():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_AA29)

    Sleep(50)

    @scena.Lambda('lambda_AA3C')
    def lambda_AA3C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_AA3C)

    Sleep(50)

    @scena.Lambda('lambda_AA4F')
    def lambda_AA4F():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_AA4F)

    Sleep(50)

    @scena.Lambda('lambda_AA62')
    def lambda_AA62():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_AA62)

    Sleep(50)

    @scena.Lambda('lambda_AA75')
    def lambda_AA75():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_AA75)

    Sleep(50)

    @scena.Lambda('lambda_AA88')
    def lambda_AA88():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_AA88)

    Sleep(50)

    ChrSetDirection(0x0016, 90, 400)
    Sleep(500)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0016,
        (
            '#0270421164V#142F#6P喂……朵洛希……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270421165V这种时候\n',
            '……你就安静一点吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0280421166V#150F#4P不，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280421167V#151F基库好像\n',
            '很高兴地飞出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0270421168V#143F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0100421169V#173F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)

    @scena.Lambda('lambda_ABB8')
    def lambda_ABB8():
        CameraMove(1350, 2000, 100510, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_ABB8)

    @scena.Lambda('lambda_ABD0')
    def lambda_ABD0():
        OP_67(0, 4000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_ABD0)

    @scena.Lambda('lambda_ABE8')
    def lambda_ABE8():
        CameraSetDistance(3100, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_ABE8)

    @scena.Lambda('lambda_ABF8')
    def lambda_ABF8():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_ABF8)

    Sleep(50)

    @scena.Lambda('lambda_AC0B')
    def lambda_AC0B():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_AC0B)

    Sleep(50)

    @scena.Lambda('lambda_AC1E')
    def lambda_AC1E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_AC1E)

    Sleep(50)

    @scena.Lambda('lambda_AC31')
    def lambda_AC31():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_AC31)

    Sleep(50)

    @scena.Lambda('lambda_AC44')
    def lambda_AC44():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_AC44)

    Sleep(50)

    @scena.Lambda('lambda_AC57')
    def lambda_AC57():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_AC57)

    Sleep(50)

    @scena.Lambda('lambda_AC6A')
    def lambda_AC6A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_AC6A)

    Sleep(50)

    ChrSetDirection(0x0016, 0, 400)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0xAC99
@scena.Code('func_12_AC99')
def func_12_AC99():
    ChrSetChipByIndex(0x0018, 30)
    ChrSetChipByIndex(0x0019, 30)
    ChrSetChipByIndex(0x001A, 30)
    ChrSetSubChip(0x0018, 0)
    ChrSetSubChip(0x0019, 0)
    ChrSetSubChip(0x001A, 0)
    OP_4A(0x0018, 0)
    OP_4A(0x0019, 0)
    OP_4A(0x001A, 0)
    Sleep(2000)

    ChrSetChipByIndex(0x0018, 27)
    ChrSetChipByIndex(0x0019, 27)
    ChrSetChipByIndex(0x001A, 27)
    ChrSetSubChip(0x0018, 0)
    ChrSetSubChip(0x0019, 0)
    ChrSetSubChip(0x001A, 0)
    OP_4B(0x0018, 0)
    OP_4B(0x0019, 0)
    OP_4B(0x001A, 0)

    Return()

# id: 0x0013 offset: 0xACF3
@scena.Code('func_13_ACF3')
def func_13_ACF3():
    EventBegin(0x00)
    OP_4A(0x000C, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x000A, 255)
    ChrClearFlags(0x000C, 0x0004)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetSubChip(0x000C, 0)
    ChrSetSubChip(0x0015, 0)
    ChrSetSubChip(0x000A, 0)
    ChrSetPos(0x000C, -1810, 2000, 90510, 180)
    ChrSetPos(0x0015, -580, 2000, 90700, 180)
    ChrSetPos(0x0101, -2080, 2000, 88160, 0)
    ChrSetPos(0x0102, -820, 2000, 88110, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD90',
    )

    ChrSetPos(0x00F8, -3320, 2000, 88590, 90)
    ChrSetPos(0x00F9, -1560, 2000, 86680, 0)

    Jump('loc_ADF5')

    def _loc_AD90(): pass

    label('loc_AD90')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ADC2',
    )

    ChrSetPos(0x00F8, -1560, 2000, 86680, 0)
    ChrSetPos(0x00F9, -3320, 2000, 88590, 90)

    Jump('loc_ADF5')

    def _loc_ADC2(): pass

    label('loc_ADC2')

    ChrSetPos(0x00F8, -2300, 2000, 86650, 0)
    ChrSetPos(0x00F9, -680, 2000, 86590, 0)
    ChrSetPos(0x000A, -3320, 2000, 88590, 90)

    def _loc_ADF5(): pass

    label('loc_ADF5')

    CameraMove(30, 1650, 90010, 0)
    OP_67(0, 4500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(45000, 0)
    OP_6E(258, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0100401262V#176F#3P<FIXME>……そうか…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 4, 0x223C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AEDB',
    )

    ChrTalk(
        0x0102,
        (
            '#0020401263V#1042F#4P<FIXME>……ええ、これから\n',
            '《中枢塔》内部の\n',
            '探索に入るところです。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF32')

    def _loc_AEDB(): pass

    label('loc_AEDB')

    ChrTalk(
        0x0102,
        (
            '#0020401264V#1042F#4P……ええ、現在\n',
            '《中枢塔》内部の探索を\n',
            '進めているところです。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF32(): pass

    label('loc_AF32')

    ChrTalk(
        0x0015,
        (
            '#0110401265V#272F#6P<FIXME>《中枢塔》……\n',
            '都市機能を統括している\n',
            '場所のようだな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110401266V#270F《輝く環》、そして\n',
            '我々の敵がそこにいるのは\n',
            '間違いないだろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100401267V#176F#3P<FIXME>…………よし。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100401268V#178F私も探索に参加しよう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B059',
    )

    OP_62(0x00F6, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B097')

    def _loc_B059(): pass

    label('loc_B059')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B080',
    )

    OP_62(0x00F6, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B097')

    def _loc_B080(): pass

    label('loc_B080')

    OP_62(0x00F6, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B097(): pass

    label('loc_B097')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B0C3',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B101')

    def _loc_B0C3(): pass

    label('loc_B0C3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B0EA',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B101')

    def _loc_B0EA(): pass

    label('loc_B0EA')

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B101(): pass

    label('loc_B101')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B1E6',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B13B',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B179')

    def _loc_B13B(): pass

    label('loc_B13B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B162',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B179')

    def _loc_B162(): pass

    label('loc_B162')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B179(): pass

    label('loc_B179')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B1A5',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B1E3')

    def _loc_B1A5(): pass

    label('loc_B1A5')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B1CC',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B1E3')

    def _loc_B1CC(): pass

    label('loc_B1CC')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B1E3(): pass

    label('loc_B1E3')

    Jump('loc_B2D1')

    def _loc_B1E6(): pass

    label('loc_B1E6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B20D',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B24B')

    def _loc_B20D(): pass

    label('loc_B20D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B234',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B24B')

    def _loc_B234(): pass

    label('loc_B234')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B24B(): pass

    label('loc_B24B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B277',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B2B5')

    def _loc_B277(): pass

    label('loc_B277')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B29E',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B2B5')

    def _loc_B29E(): pass

    label('loc_B29E')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B2B5(): pass

    label('loc_B2B5')

    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    def _loc_B2D1(): pass

    label('loc_B2D1')

    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B2EE',
    )

    ChrSetDirection(0x0105, 45, 400)

    Jump('loc_B2F5')

    def _loc_B2EE(): pass

    label('loc_B2EE')

    ChrSetDirection(0x000A, 45, 400)

    def _loc_B2F5(): pass

    label('loc_B2F5')

    ChrTalk(
        0x0101,
        (
            '#0010401269V#1004F#6P<FIXME>えっ…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100401270V#170F#3P<FIXME>私も自分の足で\n',
            '外の状況を把握しておきたい。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100401271V#176Fそれに……\n',
            'どうやら《中枢塔》からは\n',
            '様々な都市機能に干渉できるようだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100401272V#178F何もせず、このまま\n',
            '放置しておくのも危険だろう。',
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
        'loc_B46C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401273V#1164F#5P<FIXME>でもユリアさん、\n',
            'アルセイユの修理の方は……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4BB')

    def _loc_B46C(): pass

    label('loc_B46C')

    ChrTalk(
        0x000A,
        (
            '#0060401273V#1164F#5P<FIXME>でもユリアさん、\n',
            'アルセイユの修理の方は……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B4BB(): pass

    label('loc_B4BB')

    ChrSetDirection(0x000C, 215, 400)

    ChrTalk(
        0x000C,
        (
            '#0100401275V#171F#3P<FIXME>ふふ、大きな作業は\n',
            'あらかた片付きました。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100401276V#170F飛翔機関のテストも\n',
            '必要な指示は出してあります。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100401277V後は博士やクルーたちに\n',
            '任せておけば問題ないでしょう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010401278V#1011F#6P<FIXME>そ、そっか……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010401279V#1006Fうん、ユリアさんが\n',
            '手を貸してくれるなら、\n',
            '大いに心強いわね！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0015, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0015)
    Sleep(300)

    ChrTalk(
        0x0015,
        (
            '#0110401280V#270F#6P<FIXME>……ならば自分も\n',
            '協力させてもらおう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B69D',
    )

    OP_62(0x00F6, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B6DB')

    def _loc_B69D(): pass

    label('loc_B69D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B6C4',
    )

    OP_62(0x00F6, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B6DB')

    def _loc_B6C4(): pass

    label('loc_B6C4')

    OP_62(0x00F6, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B6DB(): pass

    label('loc_B6DB')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B707',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B745')

    def _loc_B707(): pass

    label('loc_B707')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B72E',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B745')

    def _loc_B72E(): pass

    label('loc_B72E')

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B745(): pass

    label('loc_B745')

    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B846',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B79B',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B7D9')

    def _loc_B79B(): pass

    label('loc_B79B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B7C2',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B7D9')

    def _loc_B7C2(): pass

    label('loc_B7C2')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B7D9(): pass

    label('loc_B7D9')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B805',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B843')

    def _loc_B805(): pass

    label('loc_B805')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B82C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B843')

    def _loc_B82C(): pass

    label('loc_B82C')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B843(): pass

    label('loc_B843')

    Jump('loc_B931')

    def _loc_B846(): pass

    label('loc_B846')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B86D',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B8AB')

    def _loc_B86D(): pass

    label('loc_B86D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B894',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B8AB')

    def _loc_B894(): pass

    label('loc_B894')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B8AB(): pass

    label('loc_B8AB')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B8D7',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B915')

    def _loc_B8D7(): pass

    label('loc_B8D7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B8FE',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B915')

    def _loc_B8FE(): pass

    label('loc_B8FE')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B915(): pass

    label('loc_B915')

    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    def _loc_B931(): pass

    label('loc_B931')

    Sleep(500)

    ChrSetDirection(0x000C, 90, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B975',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401281V#33F#2P<FIXME>ほう……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B975(): pass

    label('loc_B975')

    ChrTalk(
        0x000C,
        (
            '#0100401282V#173F#3P<FIXME>しょ、少佐……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0110401283V#272F#6P<FIXME>この付近の安全は\n',
            '確保できたのだろう。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110401284Vならば自分がここにいても\n',
            '出来ることは少ない。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110401285V#277F武人は武人らしく、\n',
            '役立たせてもらおう。',
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
        'loc_BB24',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401286V#31F#2P<FIXME>なるほどね……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040401287V#37Fユリアさんが出かけてしまったら\n',
            '寂しいというわけだね？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0110401288V#276F#6P<FIXME>……誰のためだと思っている。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC3D')

    def _loc_BB24(): pass

    label('loc_BB24')

    ChrTalk(
        0x000C,
        (
            '#0100401289V#172F#3P<FIXME>で、ですが\n',
            '少佐の手をお借りするのは……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0015, 270, 400)

    ChrTalk(
        0x0015,
        (
            '#0110401290V#277F#4P<FIXME>……いらぬ気遣いだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110401291V正直に言わせてもらえば、\n',
            'あのお調子者を外に出すのが\n',
            '些#2Rいささ#か心配ということだからな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0100401292V#170F#3P<FIXME>少佐…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC3D(): pass

    label('loc_BC3D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BC52',
    )

    ChrSetDirection(0x0015, 180, 400)

    def _loc_BC52(): pass

    label('loc_BC52')

    ChrTalk(
        0x0015,
        (
            '#0110401293V#277F#6P<FIXME>……というわけだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110401294V我々の手を借りたいときは\n',
            'いつでも言ってくれ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370643V#1006F#6P<FIXME>うん、分かったわ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020401296V#1040F#4P<FIXME>こちらこそ、\n',
            '宜しくお願いします。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x000C, -1090, 2200, 93560, 0)
    ChrSetPos(0x0015, 130, 2000, 91480, 0)
    ChrSetPos(0x0101, -1130, 2000, 87700, 180)
    ChrSetPos(0x0102, -1130, 2000, 87700, 180)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BDBE',
    )

    ChrSetPos(0x00F8, -1130, 2000, 87700, 180)
    ChrSetPos(0x00F9, -1130, 2000, 87700, 180)

    Jump('loc_BDF1')

    def _loc_BDBE(): pass

    label('loc_BDBE')

    ChrSetPos(0x00F8, -1130, 2000, 87700, 180)
    ChrSetPos(0x00F9, -1130, 2000, 87700, 180)
    ChrSetPos(0x000A, -910, 2000, 89640, 0)

    def _loc_BDF1(): pass

    label('loc_BDF1')

    ChrSetFlags(0x000C, 0x0004)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetSubChip(0x000C, 0)
    ChrSetSubChip(0x0015, 0)
    ChrSetSubChip(0x000A, 0)
    CreateThread(0x0015, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CameraMove(-1130, 2000, 87700, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x045A, 6, 0x22D6))
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x00, 85)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0xFE, 0)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['天琴'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['反射大衣Ⅱ'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['合成防护靴Ⅱ'], 0xFF)
    AddCraft(ChrTable['尤莉亚上尉'], 0x0000)
    OP_BB(0x0E, 0x06, 0x0000011A)
    OP_37(0x0E, 0x80, 0x03)
    OP_37(0x0E, 0x81, 0x03)
    OP_37(0x0E, 0x82, 0x02)
    OP_37(0x0E, 0x83, 0x03)
    OP_37(0x0E, 0x84, 0x02)
    OP_37(0x0E, 0x85, 0x02)
    OP_37(0x0E, 0x86, 0x02)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['范围'], 0x00)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['行动力３'], 0x01)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['省ＥＰ４'], 0x03)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['ＨＰ４'], 0x04)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['防御４'], 0x05)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['回避４'], 0x06)
    ChrSetStatus(ChrTable['穆拉'], 0x00, 86)
    ChrSetStatus(ChrTable['穆拉'], 0xFE, 0)
    EquipCmd(ChrTable['穆拉'], ItemTable['耀晶破坏者'], 0xFF)
    EquipCmd(ChrTable['穆拉'], ItemTable['反射大衣Ⅱ'], 0xFF)
    EquipCmd(ChrTable['穆拉'], ItemTable['合成防护靴Ⅱ'], 0xFF)
    AddCraft(ChrTable['穆拉'], 0x0000)
    OP_BB(0x0F, 0x06, 0x00000114)
    OP_37(0x0F, 0x80, 0x02)
    OP_37(0x0F, 0x81, 0x03)
    OP_37(0x0F, 0x82, 0x02)
    OP_37(0x0F, 0x83, 0x02)
    OP_37(0x0F, 0x84, 0x02)
    OP_37(0x0F, 0x85, 0x03)
    OP_37(0x0F, 0x86, 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['ＨＰ４'], 0x00)
    EquipCmd(ChrTable['穆拉'], ItemTable['行动力３'], 0x01)
    EquipCmd(ChrTable['穆拉'], ItemTable['攻击４'], 0x02)
    EquipCmd(ChrTable['穆拉'], ItemTable['阴阳'], 0x03)
    EquipCmd(ChrTable['穆拉'], ItemTable['移动３'], 0x04)
    EquipCmd(ChrTable['穆拉'], ItemTable['防御４'], 0x05)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
