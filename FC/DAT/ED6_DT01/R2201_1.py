import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2201_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2201_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R2201.x'
    header.mapIndex       = 101
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xC2C
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x8000)"),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C29',
    )

    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)

    NpcTalk(
        0x0008,
        '男性的声音',
        (
            '#1770160737V呜哦哦～～来人啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0008, 0)
    ClearChrFlags(0x000A, 0x0080)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ClearChrFlags(0x000B, 0x0080)
    Fade(1000)
    OP_6C(315000, 0)
    OP_4A(0x0009, 0)
    OP_4A(0x000A, 0)
    OP_4A(0x000B, 0)
    SetChrChipByIndex(0x0009, 7)
    SetChrChipByIndex(0x000A, 7)
    SetChrChipByIndex(0x000B, 7)

    @scena.Lambda('lambda_0109')
    def lambda_0109():
        OP_69(0x0008, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0109)

    @scena.Lambda('lambda_0117')
    def lambda_0117():
        OP_92(0x0009, 0x0008, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0117)

    @scena.Lambda('lambda_012C')
    def lambda_012C():
        OP_92(0x000A, 0x0008, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_012C)

    @scena.Lambda('lambda_0141')
    def lambda_0141():
        OP_92(0x000B, 0x0008, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0141)

    OP_6C(45000, 4000)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x00B4, 0x000001F4, 0x000003E8, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0008, 0x000B, 400)
    OP_4A(0x000A, 1)
    SetChrChipByIndex(0x000A, 6)
    OP_4B(0x000A, 0)
    Sleep(400)

    ChrTurnDirection(0x0008, 0x0009, 400)
    OP_4A(0x000A, 0)
    SetChrChipByIndex(0x000A, 7)
    OP_4B(0x000A, 1)
    OP_4A(0x0009, 1)
    SetChrChipByIndex(0x0009, 6)
    OP_4B(0x0009, 0)
    Sleep(400)

    ChrTurnDirection(0x0008, 0x000A, 400)
    OP_4A(0x0009, 0)
    SetChrChipByIndex(0x0009, 7)
    OP_4B(0x0009, 1)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)

    @scena.Lambda('lambda_01F1')
    def lambda_01F1():
        OP_92(0x0009, 0x0008, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_01F1)

    @scena.Lambda('lambda_0206')
    def lambda_0206():
        OP_92(0x000A, 0x0008, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0206)

    @scena.Lambda('lambda_021B')
    def lambda_021B():
        OP_92(0x000B, 0x0008, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_021B)

    OP_4A(0x000A, 1)
    OP_4A(0x000B, 1)
    Sleep(200)

    OP_4B(0x000B, 1)
    Sleep(200)

    OP_4B(0x000A, 1)
    SetChrPos(0x0101, 69700, -6000, -9500, 0)
    SetChrPos(0x0102, 69700, -6000, -10500, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_284',
    )

    SetChrPos(0x0136, 69700, -6000, -11500, 0)

    def _loc_284(): pass

    label('loc_284')

    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2A0',
    )

    SetChrFlags(0x0136, 0x0040)

    def _loc_2A0(): pass

    label('loc_2A0')

    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_02BA')
    def lambda_02BA():
        ChrWalkTo(0x0101, 73000, -6000, -1700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02BA)

    @scena.Lambda('lambda_02D5')
    def lambda_02D5():
        ChrWalkTo(0x0102, 71500, -6000, -2000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_02D5)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_312',
    )

    @scena.Lambda('lambda_02FD')
    def lambda_02FD():
        ChrWalkTo(0x0136, 70000, -6000, -3850, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_02FD)

    def _loc_312(): pass

    label('loc_312')

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x0087, 0x000001F4, 0x000003E8, 0x00)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    SetChrChipByIndex(0x0009, 6)
    SetChrChipByIndex(0x000A, 6)
    SetChrChipByIndex(0x000B, 6)
    OP_4B(0x0009, 0)
    OP_4B(0x000A, 0)
    OP_4B(0x000B, 0)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0101, 2)
    CreateThread(0x0101, 0x01, 0x00, 0x0002)
    SetChrDirection(0x0101, 0, 0)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrChipByIndex(0x0102, 4)
    CreateThread(0x0102, 0x01, 0x00, 0x0002)
    SetChrDirection(0x0102, 0, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3A3',
    )

    WaitForThreadExit(0x0136, 0x0001)
    SetChrDirection(0x0136, 0, 0)

    def _loc_3A3(): pass

    label('loc_3A3')

    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_69(0x0101, 800)
    ChrJumpToRelative(0x0008, 0, 0, 0, 800, 12000)

    ChrTalk(
        0x0008,
        (
            '#1770160738V救、救命啊～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_40E',
    )

    ChrTalk(
        0x0136,
        (
            '#0060160739V#044F啊，不好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40E(): pass

    label('loc_40E')

    ChrTalk(
        0x0102,
        (
            '#0020100569V#012F艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160741V#005F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_46F',
    )

    TerminateThread(0x0136, 0xFF)

    def _loc_46F(): pass

    label('loc_46F')

    Battle(0x000003F3, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_488'),
        (-1, 'loc_48B'),
    )

    def _loc_488(): pass

    label('loc_488')

    OP_B4(0x00)

    Return()

    def _loc_48B(): pass

    label('loc_48B')

    EventBegin(0x00)
    OP_4A(0x0008, 255)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0101, 73500, -6000, 0, 0)
    SetChrPos(0x0102, 72120, -6080, -170, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_4E0',
    )

    SetChrPos(0x0136, 71000, -6000, -1000, 0)

    def _loc_4E0(): pass

    label('loc_4E0')

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x8, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x8, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x8, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000C, 0)
    OP_0D()
    Sleep(1000)

    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160742V#000F呼……\n',
            '还好及时解决掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_577',
    )

    ChrTurnDirection(0x0136, 0x0101, 400)

    def _loc_577(): pass

    label('loc_577')

    SetChrChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160743V#010F嗯，\n',
            '已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_5FF',
    )

    ChrTurnDirection(0x0136, 0x0008, 400)

    ChrTalk(
        0x0136,
        (
            '#0060160744V#040F请问您有没有受伤呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05E6')
    def lambda_05E6():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05E6)

    @scena.Lambda('lambda_05F4')
    def lambda_05F4():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05F4)

    Jump('loc_626')

    def _loc_5FF(): pass

    label('loc_5FF')

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160745V#010F您没有受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_626(): pass

    label('loc_626')

    ChrTalk(
        0x0008,
        (
            '#1770160746V哦哦～\n',
            '刚才真是太危险了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770160747V我还以为肯定会\n',
            '成为鱼饵了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_067C')
    def lambda_067C():
        OP_94(0x01, 0x0008, 0x0000, 0x00000834, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_067C)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160748V#002F真是的，\n',
            '竟敢自己一个人跑到这种地方来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160749V到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#1770160750V唔～\n',
            '实际上是有原因的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770160751V…………不过嘛，\n',
            '我不太方便告诉你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160752V#007F哎呀。\n',
            '不过算了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160753V#002F总之，别在这种危险的地方\n',
            '随意逛来逛去就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160754V等真的成了鱼饵就太迟了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770160755V说的是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#1770160756V今天的确是很危险啊，\n',
            '可是打工赚的钱\n',
            '就只有那么一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770160757V好吧…………\n',
            '我还要拼命发奋才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160758V#000F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8F8',
    )

    ChrTalk(
        0x0102,
        (
            '#0020160759V#010F……对了，\n',
            '接下来您打算怎么办呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160760V我们本来应该\n',
            '把您送回城里的，\n',
            '可是现在我们也有要紧事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_95D')

    def _loc_8F8(): pass

    label('loc_8F8')

    ChrTalk(
        0x0102,
        (
            '#0020160759V#010F……对了，\n',
            '接下来您打算怎么办呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160762V如果您不介意的话，\n',
            '我们就护送您到城里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_95D(): pass

    label('loc_95D')

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1770160763V不用不用，没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770160764V对于逃跑的本领我还是有自信的，\n',
            '只要在海道上就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770160765V再见了，\n',
            '谢谢你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0040)

    @scena.Lambda('lambda_09F4')
    def lambda_09F4():
        ChrTurnDirection(0x0101, 0x0008, 0)
        Yield()

        Jump('lambda_09F4')

    DispatchAsync2(0x0101, 0x0001, lambda_09F4)

    @scena.Lambda('lambda_0A05')
    def lambda_0A05():
        ChrTurnDirection(0x0102, 0x0008, 0)
        Yield()

        Jump('lambda_0A05')

    DispatchAsync2(0x0102, 0x0001, lambda_0A05)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_A70',
    )

    @scena.Lambda('lambda_0A23')
    def lambda_0A23():
        ChrTurnDirection(0x0136, 0x0008, 0)
        Yield()

        Jump('lambda_0A23')

    DispatchAsync2(0x0136, 0x0001, lambda_0A23)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x136, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x136, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x136, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_AAF')

    def _loc_A70(): pass

    label('loc_A70')

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_AAF(): pass

    label('loc_AAF')

    @scena.Lambda('lambda_0AB5')
    def lambda_0AB5():
        OP_69(0x000C, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0AB5)

    ChrWalkTo(0x0008, 70000, 0, 500, 6000, 0x00)
    ChrWalkTo(0x0008, 70000, 0, -10000, 6000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_B03',
    )

    TerminateThread(0x0136, 0x01)

    def _loc_B03(): pass

    label('loc_B03')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010160766V#007F毫无紧张感的人呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160767V#010F应该是有什么原因\n',
            '才跑到这里附近来的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160768V希望他不要再遇到危险就好了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0101, 0x0040)
    ClearChrFlags(0x0102, 0x0040)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_BAB',
    )

    ClearChrFlags(0x0136, 0x0040)

    def _loc_BAB(): pass

    label('loc_BAB')

    Fade(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_BFC',
    )

    ExecExpressionWithValue(
        0x0001,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C1A')

    def _loc_BFC(): pass

    label('loc_BFC')

    ExecExpressionWithValue(
        0x0001,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C1A(): pass

    label('loc_C1A')

    OP_69(0x0000, 1000)
    OP_28(0x001E, 0x01, 0x8000)
    EventEnd(0x00)

    def _loc_C29(): pass

    label('loc_C29')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
