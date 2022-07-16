import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1132_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1132_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T1132.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA1E
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
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_76',
    )

    Call(1, 0x0002)

    Jump('loc_103')

    def _loc_76(): pass

    label('loc_76')

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_87',
    )

    Call(1, 0x0001)

    Jump('loc_103')

    def _loc_87(): pass

    label('loc_87')

    SetChrFlags(0x000A, 0x0010)
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '呼，受不了了。\n',
            '这种时候定期船居然停航了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了算了，麻烦这种东西\n',
            '就是只会在最紧急的时候跳出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)
    ClearChrFlags(0x000A, 0x0010)

    def _loc_103(): pass

    label('loc_103')

    Return()

# id: 0x0001 offset: 0x104
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)

    @scena.Lambda('lambda_0111')
    def lambda_0111():
        CameraMove(-86090, 0, 119620, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0111)

    SetChrPos(0x0101, -85900, 0, 119750, 270)
    SetChrPos(0x0102, -84500, 0, 119350, 270)
    SetChrPos(0x0103, -84900, 0, 120550, 270)
    SetChrFlags(0x000A, 0x0010)
    OP_4A(0x000A, 255)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    Sleep(400)

    OP_28(0x0010, 0x04, 0x04)
    OP_28(0x0010, 0x01, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010151151V#000F打扰一下可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151152V您就是哈尔德先生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#1370151153V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 90, 400)

    ChrTalk(
        0x000A,
        (
            '#1370151154V难道，\n',
            '你们是看了公告板而来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151155V#000F嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151156V呼～终于来了啊。\n',
            '我都快等不及了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151157V我有非常要紧的事情要赶去卢安办理。\n',
            '希望你们能护送我到古罗尼的山顶关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151158V如何，你们愿意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F2',
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
            TXT(0x00, '【接受】\n'),
            TXT(0x01, '【拒绝】\n'),
        ),
    )

    MenuEnd(0x0001)

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

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_336'),
        (0x00000001, 'loc_34A'),
        (-1, 'loc_3EF'),
    )

    def _loc_336(): pass

    label('loc_336')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    Call(1, 0x0003)

    Jump('loc_3EF')

    def _loc_34A(): pass

    label('loc_34A')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_28(0x0010, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010151159V#000F对不起，\n',
            '我们还有些事情要办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151160V啊～～怎么、怎么会这样～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151161V唉，这么一来，\n',
            '这次的生意就谈不成了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 270, 0)

    Jump('loc_3EF')

    def _loc_3EF(): pass

    label('loc_3EF')

    Jump('loc_2D2')

    def _loc_3F2(): pass

    label('loc_3F2')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4B(0x000A, 255)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x403
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    Fade(1000)

    @scena.Lambda('lambda_0410')
    def lambda_0410():
        CameraMove(-86090, 0, 119620, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0410)

    SetChrPos(0x0101, -85900, 0, 119750, 270)
    SetChrPos(0x0102, -84500, 0, 119350, 270)
    SetChrPos(0x0103, -84900, 0, 120550, 270)
    SetChrFlags(0x000A, 0x0010)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    OP_4A(0x000A, 255)
    SetChrDirection(0x000A, 90, 400)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#1370151162V哦，是游击士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151163V怎么样？\n',
            '能护送我到古罗尼的山顶关所吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E9',
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
            TXT(0x00, '【接受】\n'),
            TXT(0x01, '【拒绝】\n'),
        ),
    )

    MenuEnd(0x0001)

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

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_527'),
        (0x00000001, 'loc_53B'),
        (-1, 'loc_5E6'),
    )

    def _loc_527(): pass

    label('loc_527')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    Call(1, 0x0003)

    Jump('loc_5E6')

    def _loc_53B(): pass

    label('loc_53B')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_28(0x0010, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010151164V#505F唔～对不起……\n',
            '我们还有些事情要办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151160V啊～～怎么、怎么会这样～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151161V唉，这么一来，\n',
            '这次的生意就谈不成了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 270, 0)

    Jump('loc_5E6')

    def _loc_5E6(): pass

    label('loc_5E6')

    Jump('loc_4C3')

    def _loc_5E9(): pass

    label('loc_5E9')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4B(0x000A, 255)
    ClearChrFlags(0x000A, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x5FF
@scena.Code('func_03_5FF')
def func_03_5FF():
    OP_28(0x0010, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010151167V#006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151168V太好了～\n',
            '啊～～你们真是我的救星啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151169V山道上的魔兽非常多，\n',
            '只有我一个人的话实在是有点害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151170V#000F可是过了关所后又要怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151171V啊，\n',
            '我也委托了那边的游击士协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1370151172V卢安支部会派游击士\n',
            '接我过去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151173V#000F原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000A, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151174V#010F那么，接下来怎么做？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151175V现在就出发吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151176V#020F不要急，我们先各自行动，\n',
            '待会儿再汇合。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151177V因为我们也要先\n',
            '做好各种准备才能出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 45, 400)

    ChrTalk(
        0x000A,
        (
            '#1370151178V嗯，没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 90, 400)

    ChrTalk(
        0x000A,
        (
            '#1370151179V那我就在城的西门等着，\n',
            '你们好好准备吧，待会儿就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    @scena.Lambda('lambda_0867')
    def lambda_0867():
        ChrTurnDirection(0x0101, 0x000A, 0)
        Yield()

        Jump('lambda_0867')

    DispatchAsync2(0x0101, 0x0001, lambda_0867)

    @scena.Lambda('lambda_0878')
    def lambda_0878():
        ChrTurnDirection(0x0102, 0x000A, 0)
        Yield()

        Jump('lambda_0878')

    DispatchAsync2(0x0102, 0x0001, lambda_0878)

    @scena.Lambda('lambda_0889')
    def lambda_0889():
        ChrTurnDirection(0x0103, 0x000A, 0)
        Yield()

        Jump('lambda_0889')

    DispatchAsync2(0x0103, 0x0001, lambda_0889)

    @scena.Lambda('lambda_089A')
    def lambda_089A():
        ChrMoveToRelative(0x0101, 0, 0, 1000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_089A)

    @scena.Lambda('lambda_08B5')
    def lambda_08B5():
        ChrMoveToRelative(0x0102, 0, 0, -1000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_08B5)

    SetChrFlags(0x000A, 0x0040)
    ChrWalkTo(0x000A, -83000, 0, 119000, 2000, 0x00)
    ChrWalkTo(0x000A, -81300, 0, 119500, 2000, 0x00)

    @scena.Lambda('lambda_08FD')
    def lambda_08FD():
        ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_08FD)

    ChrWalkTo(0x000A, -79300, 0, 119500, 2000, 0x00)
    SetChrFlags(0x000A, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0103, 0x01)
    Sleep(800)

    @scena.Lambda('lambda_0939')
    def lambda_0939():
        ChrMoveToRelative(0x0101, 0, 0, -1000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0939)

    @scena.Lambda('lambda_0954')
    def lambda_0954():
        ChrMoveToRelative(0x0102, 0, 0, 1000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0954)

    WaitForThreadExit(0x0102, 0x0002)

    @scena.Lambda('lambda_0974')
    def lambda_0974():
        SetChrDirection(0x0101, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0974)

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(800)

    ChrTalk(
        0x0102,
        (
            '#0020151180V#010F城的西门就在梅贝尔市长官邸的旁边吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151181V#020F嗯，没错。\n',
            '那么我们就开始工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151182V#000F好～的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
