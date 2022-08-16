import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0131_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0131_2 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0131.x'
    header.mapIndex       = 7
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    EventBegin(0x00)
    OP_26(209)
    OP_26(349)
    OP_26(524)
    ChrSetPos(0x0101, 37030, 0, 75500, 135)
    ChrSetPos(0x00F8, 37530, 0, 73700, 0)
    ChrSetPos(0x00F9, 36660, 0, 73320, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_115',
    )

    ChrSetPos(0x00F9, 37530, 0, 73700, 0)
    ChrSetPos(0x00F8, 36660, 0, 73320, 0)

    def _loc_115(): pass

    label('loc_115')

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x0103, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_137',
    )

    ChrSetFlags(0x0104, 0x0080)

    def _loc_137(): pass

    label('loc_137')

    CameraMove(43180, 0, 66690, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)

    @scena.Lambda('lambda_017A')
    def lambda_017A():
        CameraMove(36390, 0, 75300, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_017A)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010470698V#1007F#1P唉，最后还是不放心\n',
            '一起来了，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470699V#1002F……雪拉姐她们\n',
            '好象还没来。',
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
        'loc_251',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470700V#063F嗯……也许是邀请失败了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    Jump('loc_357')

    def _loc_251(): pass

    label('loc_251')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470701V#040F应该还在协会\n',
            '说服爱娜小姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    Jump('loc_357')

    def _loc_29D(): pass

    label('loc_29D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470702V#070F也许在协会里还要花些工夫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    Jump('loc_357')

    def _loc_2E8(): pass

    label('loc_2E8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_357',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470703V#551F应该还在协会里\n',
            '说服爱娜吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470704V真是的，爱娜还真是麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    def _loc_357(): pass

    label('loc_357')

    ChrTalk(
        0x0101,
        (
            '#0010470705V#1015F#1P不管了，我们就\n',
            '坐下慢慢等吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0103, 48000, -500, 70290, 270)
    ChrSetPos(0x0026, 48000, -500, 68920, 270)
    ChrSetPos(0x0025, 48000, -500, 71150, 270)
    ChrSetPos(0x0027, 48000, -500, 69890, 270)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0027, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_438',
    )

    ChrSetDirection(0x0106, 135, 400)

    ChrTalk(
        0x0106,
        (
            '#0050470706V#050F不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470707V没那个必要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_552')

    def _loc_438(): pass

    label('loc_438')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_496',
    )

    ChrSetDirection(0x0108, 135, 400)

    ChrTalk(
        0x0108,
        (
            '#0080470708V#070F不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470709V看来似乎已经\n',
            '没必要等了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_552')

    def _loc_496(): pass

    label('loc_496')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FA',
    )

    ChrSetDirection(0x0105, 135, 400)

    ChrTalk(
        0x0105,
        (
            '#0060470710V#040F嗯…艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470711V似乎没有\n',
            '那个必要了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_552')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_552',
    )

    ChrSetDirection(0x0107, 135, 400)

    ChrTalk(
        0x0107,
        (
            '#0070470712V#064F啊～可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070470713V看来已经不必等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_552(): pass

    label('loc_552')

    ChrTalk(
        0x0101,
        (
            '#0010470714V#1011F#2P哎哎……～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    @scena.Lambda('lambda_0584')
    def lambda_0584():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0584)

    Sleep(200)

    @scena.Lambda('lambda_0597')
    def lambda_0597():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_0597)

    @scena.Lambda('lambda_05A5')
    def lambda_05A5():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_05A5)

    @scena.Lambda('lambda_05B3')
    def lambda_05B3():
        CameraMove(42950, 0, 70140, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_05B3)

    @scena.Lambda('lambda_05CB')
    def lambda_05CB():
        OP_6C(326000, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_05CB)

    @scena.Lambda('lambda_05DB')
    def lambda_05DB():
        OP_6E(250, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_05DB)

    WaitForThreadExit(0x0013, 0x0000)
    WaitForThreadExit(0x0013, 0x0001)
    WaitForThreadExit(0x0013, 0x0002)
    CreateThread(0x0103, 0x00, 0x02, 0x0001)
    CreateThread(0x0026, 0x00, 0x02, 0x0002)
    CreateThread(0x0025, 0x00, 0x02, 0x0003)
    CreateThread(0x0027, 0x00, 0x02, 0x0004)
    WaitForThreadExit(0x0027, 0x0000)

    ChrTalk(
        0x0103,
        (
            '#0030470715V#020F#5P特意把你叫出来真不好意思啊，爱娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470716V接待处那里没什么问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0026, 0x0103, 400)

    ChrTalk(
        0x0026,
        (
            '#0350470717V#742F嗯，已经让利吉暂时\n',
            '帮我照看着了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470718V接受委托者的请求\n',
            '也是和接待一样重要的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0025, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0025,
        (
            '#3600470719V真对不起啊，百忙之中还把你叫来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0026, 0x0025, 400)

    ChrTalk(
        0x0026,
        (
            '#0350470720V#740F没关系，不用介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470721V有什么话就\n',
            '赶快和我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470722V#031F呵～那么就开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470723V请、请多多关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    CameraMove(36390, 0, 75300, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(250, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010470724V#1020F#2P真、真的来了啊。',
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
        'loc_8A0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470725V#070F嗯，好像是借口说有委托者\n',
            '需要商讨才把她带来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_97F')

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470726V#050F呵，好像是借口说有委托者\n',
            '需要商讨才把她带来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_97F')

    def _loc_8F5(): pass

    label('loc_8F5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_94A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470727V#542F好像是和她说有委托者\n',
            '需要商谈才把她叫来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_97F')

    def _loc_94A(): pass

    label('loc_94A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_97F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470728V#067F是有事商谈吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_97F(): pass

    label('loc_97F')

    ChrTalk(
        0x0101,
        (
            '#0010470729V#1015F#2P嗯，这个也确实是\n',
            '商谈，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470730V#1007F爱娜姐\n',
            '到时会不会发怒呢。',
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
        'loc_D99',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A3D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470731V#561F不、不过…\n',
            '为什么连奥利维尔也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2F')

    def _loc_A3D(): pass

    label('loc_A3D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A88',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470732V#045F可、可是\n',
            '奥利维尔先生什么时候也…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2F')

    def _loc_A88(): pass

    label('loc_A88')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ADF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470733V#552F那个倒也罢了，\n',
            '但奥利维尔那家伙为什么也在那里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2F')

    def _loc_ADF(): pass

    label('loc_ADF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B2F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470734V#073F话说回来，奥利维尔\n',
            '是什么时候跑到那里的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B2F(): pass

    label('loc_B2F')

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010470735V#1019F#2P说、说起来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470736V那家伙应该在\n',
            '协会里才对吧。',
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
        'loc_C10',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470737V#075F大概是偷听到了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470738V一有这种事，那家伙的\n',
            '嗅觉就灵敏了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D99')

    def _loc_C10(): pass

    label('loc_C10')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C96',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470739V#551F一定是偷听到之后\n',
            '就死皮赖脸硬跟过来的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470740V一有这种事就有他，\n',
            '真是个敏锐的大笨蛋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D99')

    def _loc_C96(): pass

    label('loc_C96')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D16',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470741V#067F一定是在协会里偷听到之后\n',
            '就跟着过来了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070470742V#562F不、不愧是奥利维尔先生啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D99')

    def _loc_D16(): pass

    label('loc_D16')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D99',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470743V#045F一定是在协会听到之后\n',
            '就硬跟来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470744V如果是奥利维尔先生的话\n',
            '这么做就再正常不过了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D99(): pass

    label('loc_D99')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_72(0x0001, 0x0004)
    ChrSetPos(0x0101, 38060, 0, 75490, 180)
    ChrSetChipByIndex(0x0103, 21)
    ChrSetSubChip(0x0103, 0)
    ChrSetFlags(0x0103, 0x0004)
    ChrSetPos(0x0103, 41700, 200, 67710, 225)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EF3',
    )

    ChrSetChipByIndex(0x0101, 35)
    ChrSetSubChip(0x0101, 1)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetPos(0x0101, 41440, 1580, 77300, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E84',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E2A',
    )

    ChrSetChipByIndex(0x00F9, 22)

    Jump('loc_E66')

    def _loc_E2A(): pass

    label('loc_E2A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E3F',
    )

    ChrSetChipByIndex(0x00F9, 23)

    Jump('loc_E66')

    def _loc_E3F(): pass

    label('loc_E3F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E54',
    )

    ChrSetChipByIndex(0x00F9, 24)

    Jump('loc_E66')

    def _loc_E54(): pass

    label('loc_E54')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E66',
    )

    ChrSetChipByIndex(0x00F9, 25)

    def _loc_E66(): pass

    label('loc_E66')

    ChrSetSubChip(0x00F9, 2)
    ChrSetFlags(0x00F9, 0x0004)
    ChrSetPos(0x00F9, 39580, 1620, 77050, 110)

    Jump('loc_EF0')

    def _loc_E84(): pass

    label('loc_E84')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E99',
    )

    ChrSetChipByIndex(0x00F8, 22)

    Jump('loc_ED5')

    def _loc_E99(): pass

    label('loc_E99')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EAE',
    )

    ChrSetChipByIndex(0x00F8, 23)

    Jump('loc_ED5')

    def _loc_EAE(): pass

    label('loc_EAE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EC3',
    )

    ChrSetChipByIndex(0x00F8, 24)

    Jump('loc_ED5')

    def _loc_EC3(): pass

    label('loc_EC3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ED5',
    )

    ChrSetChipByIndex(0x00F8, 25)

    def _loc_ED5(): pass

    label('loc_ED5')

    ChrSetSubChip(0x00F8, 2)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetPos(0x00F8, 39580, 1620, 77050, 110)
    def _loc_EF0(): pass

    label('loc_EF0')

    Jump('loc_FF0')

    def _loc_EF3(): pass

    label('loc_EF3')

    OP_72(0x0002, 0x0004)
    ChrSetChipByIndex(0x0101, 35)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetPos(0x0101, 40320, 1620, 78700, 180)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F2D',
    )

    ChrSetChipByIndex(0x00F8, 22)

    Jump('loc_F69')

    def _loc_F2D(): pass

    label('loc_F2D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F42',
    )

    ChrSetChipByIndex(0x00F8, 23)

    Jump('loc_F69')

    def _loc_F42(): pass

    label('loc_F42')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F57',
    )

    ChrSetChipByIndex(0x00F8, 24)

    Jump('loc_F69')

    def _loc_F57(): pass

    label('loc_F57')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F69',
    )

    ChrSetChipByIndex(0x00F8, 25)

    def _loc_F69(): pass

    label('loc_F69')

    ChrSetSubChip(0x00F8, 2)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetPos(0x00F8, 39580, 1620, 77050, 110)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F99',
    )

    ChrSetChipByIndex(0x00F9, 22)

    Jump('loc_FD5')

    def _loc_F99(): pass

    label('loc_F99')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FAE',
    )

    ChrSetChipByIndex(0x00F9, 23)

    Jump('loc_FD5')

    def _loc_FAE(): pass

    label('loc_FAE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FC3',
    )

    ChrSetChipByIndex(0x00F9, 24)

    Jump('loc_FD5')

    def _loc_FC3(): pass

    label('loc_FC3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FD5',
    )

    ChrSetChipByIndex(0x00F9, 25)

    def _loc_FD5(): pass

    label('loc_FD5')

    ChrSetSubChip(0x00F9, 1)
    ChrSetFlags(0x00F9, 0x0004)
    ChrSetPos(0x00F9, 41440, 1580, 77300, 270)
    def _loc_FF0(): pass

    label('loc_FF0')

    ChrSetDirection(0x000C, 180, 0)
    OP_4A(0x000C, 255)
    ChrSetFlags(0x0026, 0x0004)
    ChrSetFlags(0x0026, 0x0040)
    ChrSetPos(0x0026, 38290, -50, 67720, 114)
    ChrSetChipByIndex(0x0027, 17)
    ChrSetSubChip(0x0027, 0)
    ChrSetFlags(0x0027, 0x0004)
    ChrSetFlags(0x0027, 0x0040)
    ChrSetPos(0x0027, 39710, 80, 68530, 180)
    ChrSetChipByIndex(0x0025, 14)
    ChrSetSubChip(0x0025, 0)
    ChrSetFlags(0x0025, 0x0004)
    ChrSetFlags(0x0025, 0x0040)
    ChrSetPos(0x0025, 39690, 40, 66460, 0)
    ChrClearFlags(0x0028, 0x0080)
    ChrSetSubChip(0x0028, 28)
    ChrClearFlags(0x0033, 0x0080)
    ChrSetSubChip(0x0033, 5)
    ChrClearFlags(0x0034, 0x0080)
    ChrSetSubChip(0x0034, 5)
    ChrClearFlags(0x0035, 0x0080)
    ChrSetSubChip(0x0035, 5)
    ChrClearFlags(0x0036, 0x0080)
    ChrSetSubChip(0x0036, 5)
    CameraMove(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(25)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0027,
        (
            '#0040470745V#030F#2P──那么，先干一杯吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470746V为了庆祝这次美妙的会面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470747V#021F嗯嗯，说的对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470748V#743F#1P啊，我是没问题，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470749V安敦先生要不要紧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470750V在谈话前就先喝酒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470751V不、不要紧！\n',
            '大家开始喝吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470752V别看我这副样子，\n',
            '但酒量可是很强的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470753V#740F#1P啊，那可失礼了。\n',
            '果然是真人不露相啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470754V#031F#2P呵呵，那就干杯吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    CameraMove(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1326',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470755V#045F马、马上就开始喝了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1432')

    def _loc_1326(): pass

    label('loc_1326')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_138B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470756V#065F直接就开始喝了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070470757V#561F……已经开始喝上了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1432')

    def _loc_138B(): pass

    label('loc_138B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13CE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470758V#070F喔～这么快就\n',
            '开始喝了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1432')

    def _loc_13CE(): pass

    label('loc_13CE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1432',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470759V#050F喂喂……\n',
            '这哪里算是什么商谈，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470760V直接就开始喝酒了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1432(): pass

    label('loc_1432')

    ChrTalk(
        0x0101,
        (
            '#0010470761V#1002F可是，为什么连奥利维尔\n',
            '也在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470762V#1015F……难道他也服了那个药？',
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
        'loc_1502',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470763V#050F大概是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470764V不然坐在爱娜面前他怎么\n',
            '还露得出那种笑容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164A')

    def _loc_1502(): pass

    label('loc_1502')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1564',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470765V#070F啊啊，应该是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470766V不然他哪里还挤得出那种笑脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164A')

    def _loc_1564(): pass

    label('loc_1564')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470767V#062F嗯、嗯……\n',
            '我也是那么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070470768V#067F不然的话，奥利维尔先生\n',
            '不可能这么自信满满的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164A')

    def _loc_15E7(): pass

    label('loc_15E7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_164A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470769V#040F啊啊……可能吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470770V从他那自信的态度来看应该没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_164A(): pass

    label('loc_164A')

    CameraMove(36700, 0, 74470, 1500)

    ChrTalk(
        0x0027,
        (
            '#0040470771V#031F#2P──哈哈哈哈哈哈哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470772V再来再来～～\n',
            '──爱娜又在开玩笑了～～真是的啦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470773V#1007F#1P是，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    CameraMove(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(
        0x0026,
        (
            '#0350470774V#744F#1P──好了，咱们还是\n',
            '进入正题吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470775V#740F找我出来，究竟有\n',
            '什么事情要说呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470776V嗯，嗯……\n',
            '啊啊……这个…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0025, 13)
    ChrClearFlags(0x0025, 0x0004)
    ChrJumpTo(0x0025, 38970, 0, 66280, 400, 5000)

    ChrTalk(
        0x0025,
        (
            '#3600470777V那、那个……爱娜小姐！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0026, 165, 0)

    ChrTalk(
        0x0026,
        (
            '#0350470778V#740F#1P在……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470779V请…请你和我…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470780V#4S请你和我交往吧！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0026, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2500)

    OP_63(0x0026)

    ChrTalk(
        0x0026,
        (
            '#0350470781V#743F#1P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470782V交往……\n',
            '那个……你是指那个意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470783V是、就是那样！\n',
            '请多关照！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470784V没…没有你的话\n',
            '我就活不下去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470785V#745F#1P怎、怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470786V突然说出这种话…\n',
            '真是为难啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0027, 2)

    ChrTalk(
        0x0027,
        (
            '#0040470787V#030F#2P呵呵，爱娜\n',
            '会感到困惑也是正常的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470788V男女之间的事情\n',
            '本来就不能以理性来判断……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470789V这可不是经过考虑后就能\n',
            '马上给出回答的问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0025, 30, 400)

    ChrTalk(
        0x0025,
        (
            '#3600470790V可、可是…\n',
            '不回答的话实在太让我为难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470791V难道我只能怀着如此强烈的相思之情\n',
            '痛苦地渡过余生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0027, 0)

    ChrTalk(
        0x0027,
        (
            '#0040470792V#030F#2P呵～冷静点，年轻人。\n',
            '我倒是有个绝妙的好主意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470793V就在这里以决斗的方式\n',
            '来决定结果如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0026, 114, 400)

    ChrTalk(
        0x0026,
        (
            '#0350470794V#743F#1P决斗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0103, 2)

    ChrTalk(
        0x0103,
        (
            '#0030470795V#023F……这…怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470796V#035F#2P决斗的舞台就是这家酒馆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470797V至于决斗的方式，\n',
            '不用我多说也该明白了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470798V原，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470799V#742F#1P……是比拼酒量对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470800V#027F很有趣的提议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0027, 2)

    ChrTalk(
        0x0027,
        (
            '#0040470801V#035F#2P可是这样比的话，\n',
            '安敦先生实在太可怜了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470802V应该给爱娜增加一些附加条件才公平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470803V#742F#1P这个倒是没问题，不过……\n',
            '到底是什么附加条件呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470804V#037F#2P条件就是我也加入\n',
            '安敦一方，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470805V换言之，\n',
            '就是二对一啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470806V#744F#1P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470807V#742F好，\n',
            '我接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470808V#525F呵呵，不愧是爱娜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470809V那么，让我来担任\n',
            '这场决斗的见证人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470810V#742F#1P不过，我也\n',
            '有个条件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0025, 0x0026, 400)

    ChrTalk(
        0x0025,
        (
            '#3600470811V什、什么条件呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470812V#742F#1P既然是决斗，\n',
            '就要喝这家店里度数最强的酒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470813V不好意思了，因为我\n',
            '的时间有限。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0027, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0025, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0027,
        (
            '#0040470814V#034F#2P明、明白了……\n',
            '（真不愧是爱娜啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x0025, 14)
    ChrSetSubChip(0x0025, 0)
    ChrSetFlags(0x0025, 0x0004)
    ChrSetPos(0x0025, 39690, 50, 66460, 0)
    ChrClearFlags(0x002A, 0x0080)
    ChrSetSubChip(0x002A, 29)
    ChrClearFlags(0x002B, 0x0080)
    ChrSetSubChip(0x002B, 29)
    ChrClearFlags(0x002C, 0x0080)
    ChrSetSubChip(0x002C, 29)
    ChrSetSubChip(0x0028, 29)
    ChrSetPos(0x000C, 37670, 0, 66970, 62)
    ChrSetSubChip(0x0033, 1)
    ChrSetSubChip(0x0034, 1)
    ChrSetSubChip(0x0035, 1)
    ChrSetSubChip(0x0027, 0)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#3590470815V我…我想这些\n',
            '应该足够了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#3590470816V就算是熊，喝这么多\n',
            '也会醉倒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470817V#740F#1P谢谢，\n',
            '福克纳先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x00, 0x02, 0x0005)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030470818V#027F好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470819V现在就\n',
            '开始如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470820V#035F#2P呵呵，早准备好了，随时可以开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470821V#742F#1P啊啊，那就开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470822V好、好！\n',
            '拼了～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    CameraMove(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010470823V#1002F……开始了啊。',
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
        'loc_2275',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470824V#050F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470825V不知道要比拼多久呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2391')

    def _loc_2275(): pass

    label('loc_2275')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22D8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470826V#063F嗯、嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070470827V如果那药\n',
            '真的有效就好了，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2391')

    def _loc_22D8(): pass

    label('loc_22D8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2335',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470828V#070F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470829V不知道那两个人\n',
            '究竟能撑多久……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2391')

    def _loc_2335(): pass

    label('loc_2335')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2391',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470830V#043F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470831V那个药如果\n',
            '真的有用就好了，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2391(): pass

    label('loc_2391')

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    ChrSetSubChip(0x0103, 2)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0025,
        (
            '#3600470832V呜啊啊～第５杯！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470833V呜呜～空腹喝酒果然\n',
            '不舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470834V#030F#2P呵，我正好也喝干\n',
            '第５杯了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470835V#020F 2个人加起来\n',
            '正好是１０杯啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470836V还挺不错的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470837V#740F#1P嗯，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470838V不过你们要是喝太猛的话，\n',
            '过一会儿也许会突然醉倒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470839V哪里哪里。\n',
            '这么点酒怎么可能醉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470840V#031F#2P哈哈，说的对，我也是\n',
            '一点醉意都没有呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470841V来！继续啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    CameraMove(36700, 0, 77610, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010470842V#1002F嗯……\n',
            '两个人发挥都不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470843V#1015F果然是那药\n',
            '生效了。',
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
        'loc_26AB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470844V#042F不过爱娜小姐的表情\n',
            '也是一点变化都没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27A3')

    def _loc_26AB(): pass

    label('loc_26AB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2718',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470845V#561F不过爱娜姐姐好像\n',
            '也一点反应都没有啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070470846V她明明没有服药啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27A3')

    def _loc_2718(): pass

    label('loc_2718')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_275B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470847V#052F爱娜的脸色\n',
            '也一点都没变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27A3')

    def _loc_275B(): pass

    label('loc_275B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27A3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470848V#070F不过爱娜君的脸色\n',
            '也完全没有变化啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27A3(): pass

    label('loc_27A3')

    ChrTalk(
        0x0101,
        (
            '#0010470849V#1016F所以说……\n',
            '爱娜姐真是深不可测啊～～。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470850V不过这么一来的话\n',
            '恐怕就要进入持久战了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x002D, 0x0080)
    ChrSetSubChip(0x002D, 29)
    ChrClearFlags(0x002E, 0x0080)
    ChrSetSubChip(0x002E, 29)
    ChrSetPos(0x002D, 41440, 0, 66610, 15)
    ChrSetPos(0x002E, 41090, 0, 66050, 30)
    CameraMove(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0026,
        (
            '#0350470851V#744F#1P呼……这是第２０杯了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470852V#740F……你们怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470853V我…我是第１０杯～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470854V#037F#2P我也喝了１０杯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470855V#027F这样的话，他们也是２０杯…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470856V爱娜啊，这次他们实在是很顽强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470857V#743F#1P是啊，真令人吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470858V好像从刚开始时\n',
            '就一直没有示弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470859V哼哼哼哼。\n',
            '我早就说过吧？我的酒量可是一流的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470860V不…不过，嗓子里好像\n',
            '有团火在烧一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470861V#034F#2P确、确实啊……\n',
            '简直像就要被烧伤了一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470862V#036F爱…爱娜，\n',
            '你难道就一点感觉也没有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0027, 2)

    ChrTalk(
        0x0026,
        (
            '#0350470863V#741F#1P哎呀，你们的嗓子怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470864V难道突然感冒了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0025, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0027, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0027,
        (
            '#0040470865V#034F#2P明知故问……\n',
            '真，真过分啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470866V#740F#1P如果感觉身体不舒服的话\n',
            '就不要太勉强了，硬撑下去',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470867V会给店主添麻烦的哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470868V啊，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470869V#035F#2P呵，那么就继续吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x002F, 0x0080)
    ChrSetSubChip(0x002F, 29)
    ChrClearFlags(0x0030, 0x0080)
    ChrSetSubChip(0x0030, 29)
    ChrSetSubChip(0x0027, 0)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0027,
        (
            '#0040470870V#037F#2P十…十五杯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470871V咳咳咳……\n',
            '啊～胃里好像已经着火了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470872V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0027, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0103, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    ChrSetSubChip(0x0103, 0)

    ChrTalk(
        0x0027,
        (
            '#0040470873V#033F#2P嗯嗯……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470874V#023F安敦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0025, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0025,
        (
            '#3600470875V哈……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470876V怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470877V#743F#1P身体不舒服吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470878V看你的表情\n',
            '似乎非常呆滞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470879V不，不是的……\n',
            '我…没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470880V#530F#2P（安敦兄！！\n',
            '振作一点啊！！)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470881V(药的效力\n',
            ' 还没消失呢！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470882V（是、是的！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470883V#035F#2P（别忘了爱娜也\n',
            ' 喝下了同样多的酒……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470884V(不管她是怎样的酒豪，\n',
            ' 喝到这种地步肯定也快到极限了。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470885V(可、可是…奥利维尔……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470886V(爱娜的脸色\n',
            '好像完全都没有……变化啊)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0027, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetSubChip(0x0027, 2)
    Sleep(400)

    ChrTalk(
        0x0027,
        (
            '#0040470887V#032F#2P（唔…！嗯嗯……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470888V#740F#1P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470889V你们两个怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0027, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0027, 0)
    Sleep(400)

    ChrTalk(
        0x0027,
        (
            '#0040470890V#039F#2P（可恶，你要还是男人\n',
            '的话就不要去管那些小事！)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470891V(拿出全部的毅力来！\n',
            ' 用你的爱和勇气来打败她吧！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470892V(了、了解！！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470893V#743F#1P真的没事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470894V如果身体感觉到异常的话，\n',
            '最好还是早点放弃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470895V#035F#2P呵，多谢你的关心，\n',
            '但遗憾的是我们一点投降的意思也没有啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470896V#520F对～对～！真正的决斗现在才刚开始啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470897V好啊！大家继续决胜负吧～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(300000, 0)
    OP_6E(230, 0)
    ChrClearFlags(0x0031, 0x0080)
    ChrSetSubChip(0x0031, 29)
    ChrClearFlags(0x0032, 0x0080)
    ChrSetSubChip(0x0032, 29)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetFlags(0x0025, 0x0004)
    ChrSetFlags(0x0025, 0x0040)
    ChrSetPos(0x0025, 39690, 40, 66460, 0)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0026,
        (
            '#0350470898V#745F#1P……呼～第３６杯！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470899V１…８…杯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470900V#037F#2P我…也是１…８杯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470901V#740F#1P你们两个看起来好痛苦啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470902V难道还要继续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470903V#037F#2P哈哈哈哈哈哈。\n',
            '事到如今，怎么还问这种话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470904V哈哈，说的对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470905V要是在这时放弃的话…\n',
            '岂不是成了男人中的窝囊废……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#3600470906V……哎、哎呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0103, 0)

    ChrTalk(
        0x0103,
        (
            '#0030470907V#023F安敦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3480')
    def lambda_3480():
        CameraMove(40270, 0, 67330, 1000)

        ExitThread()

    DispatchAsync(0x0026, 0x0000, lambda_3480)

    @scena.Lambda('lambda_3498')
    def lambda_3498():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_3498)

    OP_9E(0x0025, 20, 0, 500, 4000)
    ChrClearFlags(0x0025, 0x0100)
    ChrSetChipByIndex(0x0025, 13)
    ChrSetPos(0x0025, 40480, 0, 66130, 0)
    ChrSetChipByIndex(0x0025, 13)
    OP_D1(0x0025, 20000, 0, 0, 0)

    @scena.Lambda('lambda_34EE')
    def lambda_34EE():
        OP_D1(0x0025, 60000, -15000, -90000, 200)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_34EE)

    ExecExpressionWithValue(
        0x0025,
        0x2D,
        (
            (Expr.PushLong, 0x44C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x2E,
        (
            (Expr.PushLong, 0x44C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x2F,
        (
            (Expr.PushLong, 0x44C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    PlaySE(209, 0x00, 0x64)
    ChrClearFlags(0x002D, 0x0100)
    ChrClearFlags(0x002E, 0x0100)

    ExecExpressionWithValue(
        0x002D,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3553')
    def lambda_3553():
        ChrJumpTo(0x002D, 41980, 0, 66950, 300, 3500)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_3553)

    @scena.Lambda('lambda_3571')
    def lambda_3571():
        OP_D1(0x002D, 30000, -15000, -80000, 200)

        ExitThread()

    DispatchAsync(0x002D, 0x0002, lambda_3571)

    @scena.Lambda('lambda_358B')
    def lambda_358B():
        OP_D1(0x002E, 60000, -15000, -135000, 200)

        ExitThread()

    DispatchAsync(0x002E, 0x0002, lambda_358B)

    PlaySE(349, 0x00, 0x64)
    WaitForThreadExit(0x002D, 0x0002)

    ExecExpressionWithValue(
        0x002D,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002D,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002D,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x002E, 0x0002)

    ExecExpressionWithValue(
        0x002E,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x2F,
        (
            (Expr.PushLong, 0x384),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0027, 1)
    ChrSetSubChip(0x0103, 1)
    OP_0D()
    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0026, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0027, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0027,
        (
            '#0040470908V#036F#2P安…安敦老兄！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470909V#743F#1P哎呀，不得了啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_36A0')
    def lambda_36A0():
        CameraMove(41230, 0, 67950, 1000)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_36A0)

    @scena.Lambda('lambda_36B8')
    def lambda_36B8():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_36B8)

    CreateThread(0x0026, 0x01, 0x02, 0x000C)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetFlags(0x0103, 0x0040)
    ChrClearFlags(0x0103, 0x0004)
    ChrJumpTo(0x0103, 41440, 0, 67170, 200, 5000)
    ChrSetDirection(0x0103, 180, 0)
    ChrClearFlags(0x0027, 0x0004)
    ChrSetChipByIndex(0x0027, 16)
    ChrJumpTo(0x0027, 40510, 0, 68760, 400, 5000)
    ChrSetChipByIndex(0x0027, 36)
    ChrWalkTo(0x0027, 40800, 0, 68760, 4000, 0x01)
    ChrSetSubChip(0x0027, 3)
    WaitForThreadExit(0x0025, 0x0001)

    ChrTalk(
        0x0027,
        (
            '#0040470910V#038F#2P……哎…哎呀……！？',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0027, 20, 0, 500, 4000)
    CloseMessageWindow()
    OP_59()
    ChrSetSubChip(0x0027, 0)
    ChrSetFlags(0x0027, 0x0004)
    ChrJumpTo(0x0027, 41900, 240, 68500, 400, 4000)
    ChrSetChipByIndex(0x0027, 18)

    ExecExpressionWithValue(
        0x0027,
        0x2D,
        (
            (Expr.PushLong, 0x3B6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x2E,
        (
            (Expr.PushLong, 0x3B6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x2F,
        (
            (Expr.PushLong, 0x3B6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(524, 0x00, 0x64)
    ChrJumpTo(0x0027, 42150, 240, 68500, 400, 4000)
    ChrSetDirection(0x0103, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470911V#025F#1P哎呀～连奥利维尔都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470912V#742F#1P两个人都振作一点啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrClearFlags(0x0101, 0x0004)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3887',
    )

    ChrClearFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F8, 0x0040)
    ChrClearFlags(0x00F8, 0x0004)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetPos(0x00F8, 42530, 1500, 78540, 180)

    def _loc_3887(): pass

    label('loc_3887')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38B9',
    )

    ChrClearFlags(0x00F9, 0x0080)
    ChrSetFlags(0x00F9, 0x0040)
    ChrClearFlags(0x00F9, 0x0004)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetPos(0x00F9, 42960, 1500, 78910, 180)

    def _loc_38B9(): pass

    label('loc_38B9')

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetPos(0x0101, 42860, 1500, 77720, 180)

    @scena.Lambda('lambda_38D5')
    def lambda_38D5():
        CameraMove(41380, 0, 69390, 3000)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_38D5)

    CreateThread(0x0101, 0x00, 0x02, 0x0006)
    Sleep(600)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_390A',
    )

    CreateThread(0x00F9, 0x00, 0x02, 0x0008)

    Jump('loc_3934')

    def _loc_390A(): pass

    label('loc_390A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3921',
    )

    CreateThread(0x00F8, 0x00, 0x02, 0x0008)

    Jump('loc_3934')

    def _loc_3921(): pass

    label('loc_3921')

    CreateThread(0x00F8, 0x00, 0x02, 0x0008)
    Sleep(600)

    CreateThread(0x00F9, 0x00, 0x02, 0x0009)

    def _loc_3934(): pass

    label('loc_3934')

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010470913V#1020F#2P奥、奥利维尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470914V#038F#4P呜、嗯～～嗯……',
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
        'loc_39FD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470915V#551F都已经翻白眼了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050470916V看来药的效果\n',
            '已经过去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B3B')

    def _loc_39FD(): pass

    label('loc_39FD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A71',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470917V#075F不行了啊……\n',
            '已经完全烂醉如泥了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080470918V嗯，看来药的效果\n',
            '已经过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B3B')

    def _loc_3A71(): pass

    label('loc_3A71')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3ADC',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470919V#043F完、完全醉到不成样子了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060470920V看来是药劲已经\n',
            '过去了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B3B')

    def _loc_3ADC(): pass

    label('loc_3ADC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B3B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470921V#561F彻、彻底烂醉如泥了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070470922V难道药效已经过去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B3B(): pass

    label('loc_3B3B')

    ChrTalk(
        0x0103,
        (
            '#0030470923V#025F#1P真是遗憾啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470924V本以为今天能把\n',
            '爱娜灌醉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470925V唉，看来药这种东西\n',
            '也只能应付一时而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470926V#743F#1P药……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470927V#1015F#2P……其实呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C14')
    def lambda_3C14():
        CameraMove(40560, 0, 66540, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_3C14)

    WaitForThreadExit(0x0013, 0x0000)
    ChrSetPos(0x0024, 39760, -500, 61000, 0)
    ChrSetRGBAMask(0x0024, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0024, 0x0080)

    @scena.Lambda('lambda_3C52')
    def lambda_3C52():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 800)

        ExitThread()

    DispatchAsync(0x0024, 0x0003, lambda_3C52)

    ChrWalkTo(0x0024, 39760, 0, 64440, 2000, 0x00)
    ChrSetDirection(0x0024, 50, 400)

    ChrTalk(
        0x0024,
        (
            '#1080470928V唉，这样可不行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3CA5')
    def lambda_3CA5():
        ChrTurnDirection(0x00FE, 0x0024, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3CA5)

    @scena.Lambda('lambda_3CB3')
    def lambda_3CB3():
        ChrTurnDirection(0x00FE, 0x0024, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_3CB3)

    @scena.Lambda('lambda_3CC1')
    def lambda_3CC1():
        ChrTurnDirection(0x00FE, 0x0024, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_3CC1)

    @scena.Lambda('lambda_3CCF')
    def lambda_3CCF():
        ChrTurnDirection(0x00FE, 0x0024, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_3CCF)

    ChrTurnDirection(0x0026, 0x0024, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470929V#023F#1P啊！教区长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D0A')
    def lambda_3D0A():
        CameraMove(41450, 0, 68050, 2500)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_3D0A)

    @scena.Lambda('lambda_3D22')
    def lambda_3D22():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_3D22')

    DispatchAsync2(0x0101, 0x0003, lambda_3D22)

    @scena.Lambda('lambda_3D33')
    def lambda_3D33():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_3D33')

    DispatchAsync2(0x0103, 0x0003, lambda_3D33)

    @scena.Lambda('lambda_3D44')
    def lambda_3D44():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_3D44')

    DispatchAsync2(0x00F8, 0x0003, lambda_3D44)

    @scena.Lambda('lambda_3D55')
    def lambda_3D55():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_3D55')

    DispatchAsync2(0x00F9, 0x0003, lambda_3D55)

    @scena.Lambda('lambda_3D66')
    def lambda_3D66():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_3D66')

    DispatchAsync2(0x0026, 0x0003, lambda_3D66)

    ChrWalkTo(0x0024, 41750, 0, 64849, 2000, 0x00)
    ChrWalkTo(0x0024, 42570, 0, 65590, 2000, 0x00)
    ChrSetDirection(0x0024, 315, 400)
    WaitForThreadExit(0x0013, 0x0000)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    TerminateThread(0x0026, 0x03)

    ChrTalk(
        0x0026,
        (
            '#0350470930V#743F#1P啊，您怎么会来这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0024, 0x0026, 400)

    ChrTalk(
        0x0024,
        (
            '#1080470931V#4P嗯，我听说你在这里和\n',
            '两个年轻人在拼酒，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470932V#4P忽然想起有些事情还没和他们说明，\n',
            '就马上赶来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470933V#4P不过好像还是迟了一步啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470934V#1007F嗯…他们两个都已经\n',
            '完全醉倒不起了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470935V看来是药的效力\n',
            '已经过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0024, 0x0101, 400)

    ChrTalk(
        0x0024,
        (
            '#1080470936V#4P不，其实这药的效果是\n',
            '可以持续一整晚的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470937V#4P大概他们是两个人一人一半\n',
            '将药分吃了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470938V#4P要是不服够规定的用量\n',
            '自然不会有什么效果啊……',
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
            '#0010470939V#1008F啊……',
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
        'loc_4049',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470940V#561F原、原来如此……\n',
            '原来～是这样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_411D')

    def _loc_4049(): pass

    label('loc_4049')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4094',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470941V#053F原来如此啊……\n',
            '所以才会失去药效吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_411D')

    def _loc_4094(): pass

    label('loc_4094')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40DB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470942V#070F原来如此……\n',
            '这就是自作自受吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_411D')

    def _loc_40DB(): pass

    label('loc_40DB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_411D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470943V#047F原来如此……\n',
            '所以才会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_411D(): pass

    label('loc_411D')

    ChrTalk(
        0x0024,
        (
            '#1080470944V#4P大家以后在吃药时一定要仔细遵照\n',
            '说明书上的用法用量服用才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470945V#745F#1P呼～原来如此，\n',
            '是这么一回事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470946V我早就觉得奇怪了，\n',
            '奥利维尔突然兴致冲冲地\n',
            '跑来邀约我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191053V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470948V不过这样一来他心中的恶梦\n',
            '又再次加深了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470949V#4P好了，这两个人就\n',
            '交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470950V#4P他们可是喝下了过量\n',
            '的烈酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470951V#740F#1P嗯嗯，那就拜托您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470952V我也得赶快\n',
            '回协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0024, 0x0026, 400)

    ChrTalk(
        0x0024,
        (
            '#1080470953V#4P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470954V#743F#1P嗯？您怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470955V#4P没、没什么…爱娜啊……\n',
            '你也太能喝了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470956V#4P明明喝了这么多，\n',
            '竟然一点醉意都没有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470957V#741F#1P啊，这点酒\n',
            '根本不算什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470958V就喝酒而言，\n',
            '这种程度只是陪他们玩玩而已了。',
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
        'loc_4463',
    )

    OP_62(0x00F6, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_44A1')

    def _loc_4463(): pass

    label('loc_4463')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_448A',
    )

    OP_62(0x00F6, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_44A1')

    def _loc_448A(): pass

    label('loc_448A')

    OP_62(0x00F6, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_44A1(): pass

    label('loc_44A1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44C8',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_4506')

    def _loc_44C8(): pass

    label('loc_44C8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44EF',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_4506')

    def _loc_44EF(): pass

    label('loc_44EF')

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_4506(): pass

    label('loc_4506')

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_457D',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_453F',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_457D')

    def _loc_453F(): pass

    label('loc_453F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4566',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_457D')

    def _loc_4566(): pass

    label('loc_4566')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_457D(): pass

    label('loc_457D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45EF',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45B1',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_45EF')

    def _loc_45B1(): pass

    label('loc_45B1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45D8',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_45EF')

    def _loc_45D8(): pass

    label('loc_45D8')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_45EF(): pass

    label('loc_45EF')

    @scena.Lambda('lambda_45F5')
    def lambda_45F5():
        ChrSetDirection(0x0000, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_45F5)

    @scena.Lambda('lambda_4603')
    def lambda_4603():
        ChrSetDirection(0x0001, 180, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4603)

    @scena.Lambda('lambda_4611')
    def lambda_4611():
        ChrSetDirection(0x0002, 180, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4611)

    @scena.Lambda('lambda_461F')
    def lambda_461F():
        ChrSetDirection(0x0003, 180, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_461F)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010470959V#1020F#2P啊啊！？',
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
        'loc_4683',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470960V#073F唔…怎么会…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_473D')

    def _loc_4683(): pass

    label('loc_4683')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_46C5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470961V#055F……她好像不是在开玩笑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_473D')

    def _loc_46C5(): pass

    label('loc_46C5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4708',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470962V#045F真…真是豪气十足\n',
            '的回答啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_473D')

    def _loc_4708(): pass

    label('loc_4708')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_473D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470963V#065F骗、骗人的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_473D(): pass

    label('loc_473D')

    ChrTalk(
        0x0103,
        (
            '#0030470964V#025F#5P简直就是个无底洞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470965V#4P……是吗。\n',
            '那就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#1080470966V#4P确实有些酒气，\n',
            '但一点都没醉倒是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470967V#740F#1P那、我就先失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0026, 0x0103, 400)
    ChrTurnDirection(0x0103, 0x0026, 400)

    ChrTalk(
        0x0026,
        (
            '#0350470968V#741F#1P好啦，雪拉扎德。\n',
            '这里的残局就交给你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470969V对了，别忘了\n',
            '让奥利维尔掏酒钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_487B')
    def lambda_487B():
        ChrTurnDirection(0x00FE, 0x0026, 400)
        Yield()

        Jump('lambda_487B')

    DispatchAsync2(0x0101, 0x0000, lambda_487B)

    @scena.Lambda('lambda_488C')
    def lambda_488C():
        ChrTurnDirection(0x00FE, 0x0026, 400)
        Yield()

        Jump('lambda_488C')

    DispatchAsync2(0x0103, 0x0000, lambda_488C)

    @scena.Lambda('lambda_489D')
    def lambda_489D():
        ChrTurnDirection(0x00FE, 0x0026, 400)
        Yield()

        Jump('lambda_489D')

    DispatchAsync2(0x00F8, 0x0000, lambda_489D)

    @scena.Lambda('lambda_48AE')
    def lambda_48AE():
        ChrTurnDirection(0x00FE, 0x0026, 400)
        Yield()

        Jump('lambda_48AE')

    DispatchAsync2(0x00F9, 0x0000, lambda_48AE)

    @scena.Lambda('lambda_48BF')
    def lambda_48BF():
        ChrTurnDirection(0x00FE, 0x0026, 400)
        Yield()

        Jump('lambda_48BF')

    DispatchAsync2(0x0024, 0x0000, lambda_48BF)

    @scena.Lambda('lambda_48D0')
    def lambda_48D0():
        OP_69(0x0027, 1500)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_48D0)

    CreateThread(0x0026, 0x00, 0x02, 0x000A)
    WaitForThreadExit(0x0026, 0x0002)

    ChrTalk(
        0x0027,
        (
            '#0040470970V#038F#4P呜、呜呜呜……\n',
            '不愧是爱娜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470971V如此无懈可击的你…\n',
            '我最喜欢了…………嗝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x0026, 0x0080)
    OP_28(0x0076, 0x01, 0x0008)
    OP_28(0x0076, 0x01, 0x0010)
    OP_28(0x0076, 0x01, 0x0020)

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_4984',
    )

    OP_28(0x0076, 0x01, 0x4000)

    def _loc_4984(): pass

    label('loc_4984')

    OP_28(0x0076, 0x04, 0x10)
    UnlockAchievement(0x01, 0x0004, 0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(23, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【千杯不醉的秘药】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0001 offset: 0x49DC
@scena.Code('func_01_49DC')
def func_01_49DC():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_49F2')
    def lambda_49F2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_49F2)

    ChrWalkTo(0x00FE, 42000, 0, 70290, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x0002 offset: 0x4A1A
@scena.Code('func_02_4A1A')
def func_02_4A1A():
    Sleep(1000)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_4A35')
    def lambda_4A35():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4A35)

    ChrWalkTo(0x00FE, 43000, 0, 68920, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0003 offset: 0x4A5D
@scena.Code('func_03_4A5D')
def func_03_4A5D():
    Sleep(1400)

    ChrSetRGBAMask(0x0025, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0025, 0x0080)

    @scena.Lambda('lambda_4A78')
    def lambda_4A78():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0025, 0x0003, lambda_4A78)

    ChrWalkTo(0x0025, 43000, 0, 71150, 2000, 0x00)
    ChrSetDirection(0x0025, 180, 400)

    Return()

# id: 0x0004 offset: 0x4AA0
@scena.Code('func_04_4AA0')
def func_04_4AA0():
    Sleep(2000)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_4ABB')
    def lambda_4ABB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4ABB)

    ChrWalkTo(0x00FE, 44100, 0, 69890, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0005 offset: 0x4AE3
@scena.Code('func_05_4AE3')
def func_05_4AE3():
    ChrSetFlags(0x00FE, 0x0040)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 33340, 0, 69460, 5000, 0x00)
    ChrWalkTo(0x00FE, 33340, 0, 71760, 5000, 0x00)
    ChrWalkTo(0x00FE, 33480, 1620, 75220, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0008)
    ChrClearFlags(0x00FE, 0x0040)

    Return()

# id: 0x0006 offset: 0x4B41
@scena.Code('func_06_4B41')
def func_06_4B41():
    ChrWalkTo(0x00FE, 42860, 0, 74000, 5000, 0x00)
    ChrWalkTo(0x00FE, 42150, 0, 69840, 5000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0007 offset: 0x4B71
@scena.Code('func_07_4B71')
def func_07_4B71():
    ChrClearFlags(0x00FE, 0x1000)
    ChrWalkTo(0x00FE, 42340, 0, 65970, 2000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0008 offset: 0x4B92
@scena.Code('func_08_4B92')
def func_08_4B92():
    ChrWalkTo(0x00FE, 42530, 0, 74000, 5000, 0x00)
    ChrWalkTo(0x00FE, 43170, 0, 69700, 5000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0009 offset: 0x4BC2
@scena.Code('func_09_4BC2')
def func_09_4BC2():
    ChrWalkTo(0x00FE, 42960, 0, 74000, 5000, 0x00)
    ChrWalkTo(0x00FE, 41290, 0, 69690, 5000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x000A offset: 0x4BF2
@scena.Code('func_0A_4BF2')
def func_0A_4BF2():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 40680, 0, 62550, 2000, 0x00)

    @scena.Lambda('lambda_4C13')
    def lambda_4C13():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4C13)

    ChrWalkTo(0x00FE, 40680, -500, 56000, 2000, 0x00)

    Return()

# id: 0x000B offset: 0x4C34
@scena.Code('func_0B_4C34')
def func_0B_4C34():
    EventBegin(0x00)
    CameraMove(38400, 0, 68270, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(315000, 0)
    OP_6E(230, 0)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0103, 0x0080)
    ChrClearFlags(0x0103, 0x0008)
    ChrSetFlags(0x0026, 0x0004)
    ChrSetFlags(0x0026, 0x0040)
    ChrSetPos(0x0026, 38290, -100, 67720, 114)
    ChrSetChipByIndex(0x0027, 17)
    ChrSetSubChip(0x0027, 0)
    ChrSetFlags(0x0027, 0x0004)
    ChrSetFlags(0x0027, 0x0040)
    ChrSetPos(0x0027, 39710, 80, 68530, 180)
    ChrSetChipByIndex(0x0025, 14)
    ChrSetSubChip(0x0025, 0)
    ChrSetFlags(0x0025, 0x0004)
    ChrSetFlags(0x0025, 0x0040)
    ChrSetPos(0x0025, 39690, 40, 66460, 0)
    OP_72(0x0001, 0x0004)
    ChrSetChipByIndex(0x0103, 21)
    ChrSetSubChip(0x0103, 0)
    ChrSetFlags(0x0103, 0x0004)
    ChrSetPos(0x0103, 41700, 200, 67710, 225)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetSubChip(0x002D, 29)
    ChrClearFlags(0x002E, 0x0080)
    ChrSetSubChip(0x002E, 29)
    ChrSetPos(0x002D, 41440, 0, 66610, 15)
    ChrSetPos(0x002E, 41090, 0, 66050, 30)

    ChrTalk(
        0x0025,
        (
            '#3600470906V……啊、哎呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0025, 20, 0, 500, 4000)
    ChrClearFlags(0x0025, 0x0100)
    ChrSetChipByIndex(0x0025, 13)
    ChrSetPos(0x0025, 40480, 0, 66130, 0)
    ChrSetChipByIndex(0x0025, 13)
    OP_D1(0x0025, 20000, 0, 0, 0)

    @scena.Lambda('lambda_4DBA')
    def lambda_4DBA():
        OP_D1(0x0025, 60000, -15000, -90000, 200)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_4DBA)

    ExecExpressionWithValue(
        0x0025,
        0x2D,
        (
            (Expr.PushLong, 0x44C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x2E,
        (
            (Expr.PushLong, 0x44C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x2F,
        (
            (Expr.PushLong, 0x44C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrClearFlags(0x002D, 0x0100)
    ChrClearFlags(0x002E, 0x0100)

    ExecExpressionWithValue(
        0x002D,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_4E1A')
    def lambda_4E1A():
        ChrJumpTo(0x002D, 41980, 0, 66950, 300, 3500)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_4E1A)

    @scena.Lambda('lambda_4E38')
    def lambda_4E38():
        OP_D1(0x002D, 30000, -15000, -80000, 200)

        ExitThread()

    DispatchAsync(0x002D, 0x0002, lambda_4E38)

    @scena.Lambda('lambda_4E52')
    def lambda_4E52():
        OP_D1(0x002E, 60000, -15000, -135000, 200)

        ExitThread()

    DispatchAsync(0x002E, 0x0002, lambda_4E52)

    WaitForThreadExit(0x002D, 0x0002)

    ExecExpressionWithValue(
        0x002D,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002D,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002D,
        0x2F,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x002E, 0x0002)

    ExecExpressionWithValue(
        0x002E,
        0x2D,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x2E,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x2F,
        (
            (Expr.PushLong, 0x384),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0027, 1)
    ChrSetSubChip(0x0103, 1)
    OP_0D()
    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0026, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0027, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0027,
        (
            '#0040470973V#036F安、安敦老兄！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470974V#743F#1P哎呀，不得了啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_4F5F')
    def lambda_4F5F():
        CameraMove(41230, 0, 67950, 1000)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_4F5F)

    @scena.Lambda('lambda_4F77')
    def lambda_4F77():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_4F77)

    CreateThread(0x0026, 0x01, 0x02, 0x000C)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetFlags(0x0103, 0x0040)
    ChrClearFlags(0x0103, 0x0004)
    ChrJumpTo(0x0103, 41440, 0, 67170, 200, 5000)
    ChrSetDirection(0x0103, 180, 0)
    ChrClearFlags(0x0027, 0x0004)
    ChrSetChipByIndex(0x0027, 16)
    ChrJumpTo(0x0027, 40510, 0, 68760, 400, 5000)
    ChrSetChipByIndex(0x0027, 36)
    ChrWalkTo(0x0027, 40800, 0, 68760, 4000, 0x01)
    ChrSetSubChip(0x0027, 3)
    WaitForThreadExit(0x0025, 0x0001)

    ChrTalk(
        0x0027,
        (
            '#0040470975V#038F#2P……哎…哎呀……！？',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0027, 20, 0, 500, 4000)
    CloseMessageWindow()
    OP_59()
    ChrSetSubChip(0x0027, 0)
    ChrSetFlags(0x0027, 0x0004)
    ChrJumpTo(0x0027, 41900, 240, 68500, 400, 4000)
    ChrSetChipByIndex(0x0027, 18)

    ExecExpressionWithValue(
        0x0027,
        0x2D,
        (
            (Expr.PushLong, 0x3B6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x2E,
        (
            (Expr.PushLong, 0x3B6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x2F,
        (
            (Expr.PushLong, 0x3B6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrJumpTo(0x0027, 42150, 240, 68500, 400, 4000)
    ChrSetDirection(0x0103, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470976V#025F#1P哎呀～连奥利维尔也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0350470977V#743F#1P两个人都振作一点啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrClearFlags(0x0101, 0x0004)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5141',
    )

    ChrClearFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F8, 0x0040)
    ChrClearFlags(0x00F8, 0x0004)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetPos(0x00F8, 42530, 1500, 78540, 180)

    def _loc_5141(): pass

    label('loc_5141')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5173',
    )

    ChrClearFlags(0x00F9, 0x0080)
    ChrSetFlags(0x00F9, 0x0040)
    ChrClearFlags(0x00F9, 0x0004)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetPos(0x00F9, 42960, 1500, 78910, 180)

    def _loc_5173(): pass

    label('loc_5173')

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetPos(0x0101, 42860, 1500, 77720, 180)

    @scena.Lambda('lambda_518F')
    def lambda_518F():
        CameraMove(41380, 0, 69390, 3000)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_518F)

    CreateThread(0x0101, 0x00, 0x02, 0x0006)
    Sleep(600)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51C4',
    )

    CreateThread(0x00F9, 0x00, 0x02, 0x0008)

    Jump('loc_51EE')

    def _loc_51C4(): pass

    label('loc_51C4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51DB',
    )

    CreateThread(0x00F8, 0x00, 0x02, 0x0008)

    Jump('loc_51EE')

    def _loc_51DB(): pass

    label('loc_51DB')

    CreateThread(0x00F8, 0x00, 0x02, 0x0008)
    Sleep(600)

    CreateThread(0x00F9, 0x00, 0x02, 0x0009)

    def _loc_51EE(): pass

    label('loc_51EE')

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010470978V#1020F#2P奥、奥利维尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0040470979V#038F#4P呜、嗯～～嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5258')
    def lambda_5258():
        CameraMove(40560, 0, 66540, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_5258)

    WaitForThreadExit(0x0013, 0x0000)
    ChrSetPos(0x0024, 39760, -500, 61000, 0)
    ChrSetRGBAMask(0x0024, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0024, 0x0080)

    @scena.Lambda('lambda_5296')
    def lambda_5296():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 800)

        ExitThread()

    DispatchAsync(0x0024, 0x0003, lambda_5296)

    ChrWalkTo(0x0024, 39760, 0, 64440, 2000, 0x00)
    ChrSetDirection(0x0024, 50, 400)

    ChrTalk(
        0x0024,
        (
            '#1080470928V唉，这样可不行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_52E9')
    def lambda_52E9():
        CameraMove(41450, 0, 68050, 2500)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_52E9)

    @scena.Lambda('lambda_5301')
    def lambda_5301():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_5301')

    DispatchAsync2(0x0101, 0x0003, lambda_5301)

    @scena.Lambda('lambda_5312')
    def lambda_5312():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_5312')

    DispatchAsync2(0x0103, 0x0003, lambda_5312)

    @scena.Lambda('lambda_5323')
    def lambda_5323():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_5323')

    DispatchAsync2(0x00F8, 0x0003, lambda_5323)

    @scena.Lambda('lambda_5334')
    def lambda_5334():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_5334')

    DispatchAsync2(0x00F9, 0x0003, lambda_5334)

    @scena.Lambda('lambda_5345')
    def lambda_5345():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_5345')

    DispatchAsync2(0x0026, 0x0003, lambda_5345)

    ChrWalkTo(0x0024, 41750, 0, 64849, 2000, 0x00)
    ChrWalkTo(0x0024, 42570, 0, 65590, 2000, 0x00)
    ChrSetDirection(0x0024, 315, 400)
    WaitForThreadExit(0x0013, 0x0000)

    Return()

# id: 0x000C offset: 0x5385
@scena.Code('func_0C_5385')
def func_0C_5385():
    ChrClearFlags(0x0026, 0x0004)
    ChrJumpTo(0x0026, 37760, 0, 67360, 400, 5000)
    OP_62(0x0026, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0026, 38470, 0, 65740, 3000, 0x00)
    ChrWalkTo(0x0026, 40340, 0, 64930, 3000, 0x00)
    ChrWalkTo(0x0026, 40680, 0, 65540, 3000, 0x00)
    ChrSetDirection(0x0026, 0, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
