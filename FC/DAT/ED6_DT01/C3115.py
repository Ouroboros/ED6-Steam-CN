import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3115_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3115   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3115.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20141._CH', 'ED6_DT06/CH20141P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯少尉',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '理查德上校',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希德少校',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黑色导力器',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917509,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1B0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_1E9)

    def _loc_1B0(): pass

    label('loc_1B0')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1BC'),
        (-1, 'loc_1CF'),
    )

    def _loc_1BC(): pass

    label('loc_1BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 1, 0x569)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 0, 0x568)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CC',
    )

    Event(0, func_03_122B)

    def _loc_1CC(): pass

    label('loc_1CC')

    Jump('loc_1CF')

    def _loc_1CF(): pass

    label('loc_1CF')

    Return()

# id: 0x0001 offset: 0x1D0
@scena.Code('func_01_1D0')
def func_01_1D0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 3, 0x56B)),
            Expr.Return,
        ),
        'loc_1DC',
    )

    PlaySE(172, 0x01, 0x46)

    def _loc_1DC(): pass

    label('loc_1DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 1, 0x569)),
            Expr.Return,
        ),
        'loc_1E8',
    )

    OP_71(0x0000, 0x0004)

    def _loc_1E8(): pass

    label('loc_1E8')

    Return()

# id: 0x0002 offset: 0x1E9
@scena.Code('func_02_1E9')
def func_02_1E9():
    EventBegin(0x00)
    CameraMove(-6060, 0, 3830, 0)
    OP_67(0, 5730, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0106, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000C, 3670, 0, 4750, 180)
    ChrSetPos(0x000A, 3550, 0, 2260, 0)
    ChrSetPos(0x0008, 2710, 0, 1010, 0)
    ChrSetPos(0x000B, 4000, 0, 770, 0)
    ChrSetPos(0x000D, 3520, 800, 2960, 0)
    ChrClearFlags(0x000D, 0x0080)
    CameraMove(4650, 0, 3040, 4000)

    ChrTalk(
        0x000A,
        (
            '#0130090987V#111F拉赛尔博士，\n',
            '这次真是太感谢您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130090988V竟然真的有掌握\n',
            '这个导力器『福音』的控制方法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130090989V我代表情报部由衷地感谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540090990V#102F哼……\n',
            '果然你就是幕后黑手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540090991V情报部理查德上校……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540090992V记得你本来是卡西乌斯的部下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130090993V#113F哦哦，说起来……\n',
            '博士和他是几十年的老交情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130090994V#110F其实我们王国军也\n',
            '一直在寻找卡西乌斯·布莱特的行踪，\n',
            '但可惜的是至今仍未有任何线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130090995V如果有什么线索的话，\n',
            '还望您能顺便告诉我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540090996V#104F不知道。\n',
            '知道了也不会告诉你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130090997V#115F呵呵……那就算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130090998V如果这个『福音』回到他手上，\n',
            '必定会对我们的工作构成很大的阻挠……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130090999V不过……即使他现在出面，\n',
            '也无法阻止整个事态的发展了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540091000V#102F『黑色导力器』……\n',
            '不，应该是说『福音』才对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091001V你们到底打算用它做什么？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091002V不，在此之前……\n',
            '我有一个问题是非问不可的。\n',
            '这个导力器你们到底是从哪里得到的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130091003V#111F当然是从某种渠道得来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091004V而我们的目的嘛……\n',
            '呵呵，很快您就能知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091005V等博士您明白一切之时，\n',
            '也会是我们让您回去的适当时机，\n',
            '在那之前，就委屈您在要塞小住一阵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540091006V#102F我可是知道你们干的坏事哦，\n',
            '这么简单就放我回去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091007V还真是令人难以置信啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130091008V#111F哈哈，随您怎么想了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091009V不过事成之后，\n',
            '我会以个人名义援助博士的研究。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091010V希望博士能发明更多的东西，\n',
            '来为我们的利贝尔王国添彩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540091011V#104F哼，我拒绝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610091012V#188F博士，\n',
            '请别把话说得那么绝情哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610091013V博士的孙女要是有个万一，\n',
            '这点我们可是保证不了哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540091014V#105F小、小丫头……\n',
            '又用这个来威胁我……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#0130091015V#115F哎呀哎呀，凯诺娜上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091016V怎么可以用这种口吻和博士谈话？\n',
            '不觉得你的交涉方法有欠优雅吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#0610091017V#182F呵呵……失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09F8')
    def lambda_09F8():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09F8)

    ChrTurnDirection(0x000A, 0x000C, 400)

    ChrTalk(
        0x000A,
        (
            '#0130091018V#110F上尉她总是有种特殊的幽默感。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091019V希望您不要误会，\n',
            '我们毕竟只是一群忧国忧民的军人罢了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091020V我可以在此对您发誓，\n',
            '把平民卷入计划绝非我的本意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0540091021V#102F忧国忧民……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091022V更加离谱的是……\n',
            '那个能引起导力停止现象的黑色导力器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091023V原来如此……\n',
            '你们的目的我总算能看出点眉目了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130091024V#112F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(106, 0x00, 0x64)
    Sleep(500)

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -850, 0, -4650, 0)

    ChrTalk(
        0x0009,
        (
            '#0140091025V#1P……打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BC9')
    def lambda_0BC9():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0BC9')

    DispatchAsync2(0x000B, 0x0001, lambda_0BC9)

    @scena.Lambda('lambda_0BDA')
    def lambda_0BDA():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0BDA')

    DispatchAsync2(0x000A, 0x0001, lambda_0BDA)

    @scena.Lambda('lambda_0BEB')
    def lambda_0BEB():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0BEB')

    DispatchAsync2(0x000C, 0x0001, lambda_0BEB)

    @scena.Lambda('lambda_0BFC')
    def lambda_0BFC():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0BFC')

    DispatchAsync2(0x0008, 0x0001, lambda_0BFC)

    @scena.Lambda('lambda_0C0D')
    def lambda_0C0D():
        CameraMove(3120, 0, 2260, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C0D)

    ChrWalkTo(0x0009, 1250, 0, 1590, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#0610091026V#180F哎呀，少尉。\n',
            '上校正和博士谈话呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610091027V可别打扰到他们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130091028V#110F啊，没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130091029V洛伦斯，就在这里报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140091030V#281F王都的行动已经开始了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140091031V和上校预计的一样，\n',
            '白翼似乎已经全部落网了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610091032V#188F这可真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)

    ChrTalk(
        0x000A,
        (
            '#0130091033V#115F呵呵……\n',
            '这样就向前迈进一大步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        CameraMove(4650, 0, 3040, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DB2)

    ChrTurnDirection(0x000A, 0x000C, 400)

    @scena.Lambda('lambda_0DD1')
    def lambda_0DD1():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_0DD1')

    DispatchAsync2(0x000B, 0x0001, lambda_0DD1)

    @scena.Lambda('lambda_0DE2')
    def lambda_0DE2():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_0DE2')

    DispatchAsync2(0x000C, 0x0001, lambda_0DE2)

    @scena.Lambda('lambda_0DF3')
    def lambda_0DF3():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_0DF3')

    DispatchAsync2(0x0008, 0x0001, lambda_0DF3)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0130091034V#111F博士，\n',
            '那么我们就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    ChrSetFlags(0x000D, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#0130091035V#110F希德少校，\n',
            '为了不要让博士感到不自在，\n',
            '请你在他身边的时候多注意一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620091036V#703F是……明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetDirection(0x000A, 225, 400)
    ChrWalkTo(0x000A, 2450, 0, 1910, 2000, 0x00)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_0F0E')
    def lambda_0F0E():
        ChrWalkTo(0x00FE, -1580, 0, -6870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F0E)

    Sleep(1000)

    @scena.Lambda('lambda_0F2E')
    def lambda_0F2E():
        ChrWalkTo(0x00FE, -1580, 0, -6870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F2E)

    Sleep(500)

    @scena.Lambda('lambda_0F4E')
    def lambda_0F4E():
        ChrWalkTo(0x00FE, -1580, 0, -6870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0F4E)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    PlaySE(230, 0x00, 0x64)
    Sleep(500)

    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    ChrTurnDirection(0x000B, 0x000C, 400)
    Sleep(500)

    @scena.Lambda('lambda_0F9B')
    def lambda_0F9B():
        CameraMove(4430, 0, 4440, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F9B)

    ChrWalkTo(0x000B, 3550, 0, 2260, 2000, 0x00)
    ChrTurnDirection(0x000B, 0x000C, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000B,
        (
            '#0620091037V#701F拉赛尔博士，\n',
            '请问您还有什么需要吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091038V一般的要求我们都能做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000B, 400)

    ChrTalk(
        0x000C,
        (
            '#0540091039V#104F#5P哼，免了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091040V#102F我一直认为你和他们不同，\n',
            '是个有骨气有原则的军人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091041V看来我真是看错你了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620091042V#703F……惭愧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091043V#700F不管博士怎么想都好，\n',
            '现在您已经是反叛者的阶下囚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091044V在此您有什么消息或口信\n',
            '要让我向您的孙女代为传达的吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0540091045V#105F#3S#5P快从我眼前消失！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620091046V#703F……失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 225, 400)
    ChrWalkTo(0x000B, -1290, 0, -5130, 4000, 0x00)
    PlaySE(106, 0x00, 0x64)
    Sleep(500)

    PlaySE(230, 0x00, 0x64)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C3107._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x122B
@scena.Code('func_03_122B')
def func_03_122B():
    FormationAddMember(0x0A, 0xFF)
    EventBegin(0x00)
    CameraMove(-250, 0, 1940, 0)
    OP_67(0, 6560, -10000, 0)
    CameraSetDistance(3000, 0)
    ChrSetPos(0x010B, -310, 0, 3630, 0)
    ChrSetPos(0x0101, -1040, 0, -6570, 0)
    ChrSetPos(0x0106, -1040, 0, -6570, 0)
    ChrSetPos(0x0102, -1040, 0, -6570, 0)
    ChrSetPos(0x0107, -1040, 0, -6570, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_12BF')
    def lambda_12BF():
        ChrWalkTo(0x00FE, -770, 0, 20, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_12BF)

    Sleep(400)

    @scena.Lambda('lambda_12DF')
    def lambda_12DF():
        ChrWalkTo(0x00FE, 160, 0, -500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_12DF)

    Sleep(400)

    @scena.Lambda('lambda_12FF')
    def lambda_12FF():
        ChrWalkTo(0x00FE, -2330, 0, -720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12FF)

    Sleep(400)

    @scena.Lambda('lambda_131F')
    def lambda_131F():
        ChrWalkTo(0x00FE, -1670, 0, -1430, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_131F)

    ChrTalk(
        0x010B,
        (
            '#0540091101V#104F怎么又来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0107, 400)

    ChrTalk(
        0x010B,
        (
            '#0540091102V#105F#3S不要烦我了！\n',
            '都说了什么也不需要……',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070091103V#560F爷、爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x010B, -270, 0, 2260, 1500, 0x00)

    ChrTalk(
        0x010B,
        (
            '#0540091104V#103F提、提妲！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091105V难道……\n',
            '我这是在做梦吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091106V#068F爷爷啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_1482')
    def lambda_1482():
        CameraMove(-250, 0, 2840, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1482)

    OP_92(0x0107, 0x010B, 400, 5000, 0x00)

    @scena.Lambda('lambda_14A8')
    def lambda_14A8():
        ChrMoveTo(0x0107, -120, 0, 2080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_14A8)

    ChrSetChipByIndex(0x0107, 6)
    ChrSetSubChip(0x0107, 0)
    ChrSetFlags(0x0107, 0x0020)
    OP_94(0x01, 0x010B, 0x00B4, 0x0000012C, 0x000007D0, 0x00)

    ChrTalk(
        0x0107,
        (
            '#0070091107V#069F#2P太、太好了！\n',
            '爷爷您平安无事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091108V呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0107, 15, 0, 300, 4000)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070091109V#068F#3S#2P呜哇哇哇哇啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091110V#100F看、看来……\n',
            '我这老骨头不是做梦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091111V还有，你们也来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091112V#006F呀嗬，博士。\n',
            '看来你还挺精神的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091113V#010F我们是受工房长先生的委托，\n',
            '前来这里营救博士您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091114V#103F怎么……\n',
            '你们竟然能想到办法潜入这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091115V#101F真不愧是卡西乌斯的孩子……\n',
            '无论是胆量还是意志都很优秀啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091116V#050F哟，老爷子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091117V很抱歉打断你们叙旧，\n',
            '还是赶快做一下逃离的准备吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091118V我们也没什么时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091119V#102F说起来，你又是谁啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091120V外表这么古怪的年轻人，\n',
            '头发像个公鸡一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091121V#055F公、公鸡……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0106, 15, 0, 300, 4000)

    ChrTalk(
        0x0106,
        (
            '#0050091122V#054F#3S说什么呀，你这老头！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091123V#001F啊哈哈。\n',
            '博士说得太形象了呀～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0107, 0x0020)
    ChrSetChipByIndex(0x0107, 65535)
    ChrMoveTo(0x0107, -290, 0, 1320, 2000, 0x00)
    ChrTurnDirection(0x0107, 0x010B, 0)

    ChrTalk(
        0x0107,
        (
            '#0070091124V#562F爷、爷爷啊……\n',
            '别说这种失礼的话啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091125V#560F这个大哥哥叫阿加特，\n',
            '他也是游击士协会的游击士，\n',
            '而且还是姐姐他们的前辈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091126V#103F哦……\n',
            '你也是游击士啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091127V#101F对了对了……\n',
            '我好像从卡西乌斯那里听说过你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091128V一个又倔又别扭的不良青年。\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091129V#057F那、那个胡子大叔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0106, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091130V#019F好啦好啦，阿加特兄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x010B, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091131V#010F博士也是，详细情况等以后再说吧。\n',
            '当务之急还是快点逃离这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091132V有什么东西要带走的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1ABE')
    def lambda_1ABE():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1ABE')

    DispatchAsync2(0x0101, 0x0002, lambda_1ABE)

    @scena.Lambda('lambda_1ACF')
    def lambda_1ACF():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1ACF')

    DispatchAsync2(0x0107, 0x0002, lambda_1ACF)

    @scena.Lambda('lambda_1AE0')
    def lambda_1AE0():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1AE0')

    DispatchAsync2(0x0106, 0x0002, lambda_1AE0)

    @scena.Lambda('lambda_1AF1')
    def lambda_1AF1():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1AF1')

    DispatchAsync2(0x010B, 0x0002, lambda_1AF1)

    ChrTalk(
        0x010B,
        (
            '#0540091133V#100F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091134V那么能不能把这个\n',
            '『卡佩尔』的中枢设备送回去？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091135V随便放在这里的话，\n',
            '准会被那帮家伙拿去做坏事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091136V#010F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, -1360, 0, 670, 3000, 0x00)
    ChrWalkTo(0x0102, -390, 0, 5540, 3000, 0x00)
    Sleep(500)

    OP_71(0x0000, 0x0004)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '演算导力器',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0364, 1)
    ChrSetDirection(0x0102, 180, 400)

    @scena.Lambda('lambda_1C40')
    def lambda_1C40():
        CameraMove(-900, 0, 1970, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C40)

    ChrWalkTo(0x0102, -1840, 0, 2029, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x010B, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010B, 0xFF)

    @scena.Lambda('lambda_1C87')
    def lambda_1C87():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_1C87)

    @scena.Lambda('lambda_1C95')
    def lambda_1C95():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C95)

    @scena.Lambda('lambda_1CA3')
    def lambda_1CA3():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_1CA3)

    ChrTalk(
        0x010B,
        (
            '#0540091137V#102F他们强迫我用它来研究\n',
            '『黑色导力器』的控制方法。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091138V虽然不能解析那东西的构造，\n',
            '但已经知道数据和控制方法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091139V那帮家伙随时都能引起那个现象。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091140V#003F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0101, 400)

    ChrTalk(
        0x010B,
        (
            '#0540091141V#104F抱歉，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091142V你们特地交给我的东西就这样……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091143V#013F请博士您不用太介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091144V他们拿提妲的安全做威胁，\n',
            '您被迫就范也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091145V#007F而且说起来，\n',
            '是我们把博士卷进这件事的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091146V#054F好了～！\n',
            '没时间啰嗦啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091147V快点准备逃跑吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091148V老爷子，赶快！\n',
            '跑的时候小心别闪到腰！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0106, 400)

    ChrTalk(
        0x010B,
        (
            '#0540091149V#102F哼，说什么呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091150V我还不至于输给你们年轻人！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070091151V#067F真、真是的，你们两个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00AD, 1, 0x569))
    OP_28(0x0044, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
