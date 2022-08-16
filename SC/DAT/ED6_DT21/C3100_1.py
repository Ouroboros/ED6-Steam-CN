import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3100_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C3100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    OP_4A(0x0009, 255)
    Fade(1000)
    ChrSetPos(0x0101, -70, 0, -5570, 0)
    ChrSetPos(0x00F7, 880, 150, -6000, 0)
    ChrSetPos(0x00F8, -320, 200, -7040, 0)
    ChrSetPos(0x00F9, 1170, 210, -7190, 0)
    CameraMove(570, 0, -3460, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3110450001V这是王国军的根据地\n',
            '雷斯顿水上要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450002V民间人士\n',
            '请勿进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450003V#1000F#3P那个，我们\n',
            '是看了公告板而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_230',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450004V#050F#2P应该会有\n',
            '和特别训练相关的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450005V你没从上级那里听说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28D')

    def _loc_230(): pass

    label('loc_230')

    ChrTalk(
        0x0103,
        (
            '#0030450006V#020F#2P应该会有\n',
            '和特别训练相关的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450007V你没从上级那里听说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28D(): pass

    label('loc_28D')

    ChrTalk(
        0x00FE,
        (
            '#3110450008V哦，那件事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450009V刚刚，司令部\n',
            '有通知下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450010V不是王国军的成员却要参与训练，\n',
            '实在是辛苦各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450011V#1015F#3P没什么，这也是工作嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450012V#1006F那么，\n',
            '能不能帮我们向负责人传达一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450013V哦，这倒没什么问题，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450014V你们几位已经\n',
            '准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450015V#1011F#3P什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450016V不，因为训练已经开始\n',
            '很长时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450017V进入要塞后一定会立即\n',
            '要求你们参加模拟战斗训练的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450018V因此，装备的变更等等\n',
            '还是事先在这里处理完比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450019V#1000F#3P啊，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450020V这样的话，\n',
            '稍微需要一点时间准备呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_574',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450021V#050F#2P确实需要准备准备……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450022V抱歉，能不能稍等一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C6')

    def _loc_574(): pass

    label('loc_574')

    ChrTalk(
        0x0103,
        (
            '#0030450023V#020F#2P确实需要准备准备……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450024V抱歉，能不能稍等一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C6(): pass

    label('loc_5C6')

    ChrTalk(
        0x00FE,
        (
            '#3110450025V没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450026V那么，准备好之后\n',
            '再跟我说一声吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 255)
    OP_28(0x006D, 0x01, 0x0001)
    OP_28(0x006D, 0x04, 0x04)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x625
@scena.Code('func_01_625')
def func_01_625():
    EventBegin(0x00)
    OP_4A(0x0009, 255)
    Fade(1000)
    ChrSetPos(0x0101, -70, 0, -5570, 0)
    ChrSetPos(0x00F7, 880, 150, -6000, 0)
    ChrSetPos(0x00F8, -320, 200, -7040, 0)
    ChrSetPos(0x00F9, 1170, 210, -7190, 0)
    CameraMove(570, 0, -3460, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3110450027V哟，准备好了吗？',
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
        'loc_737',
    )

    OP_28(0x006D, 0x01, 0x0002)
    OP_28(0x006D, 0x04, 0x08)
    Call(1, 0x0002)

    Jump('loc_78C')

    def _loc_737(): pass

    label('loc_737')

    ChrTalk(
        0x00FE,
        (
            '#3110450028V哎呀，还没好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3110450029V不抓紧一点\n',
            '训练要结束了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_4B(0x0009, 255)

    def _loc_78C(): pass

    label('loc_78C')

    Return()

# id: 0x0002 offset: 0x78D
@scena.Code('func_02_78D')
def func_02_78D():
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x000B, -690, 0, 7060, 180)
    ChrSetPos(0x000D, 870, 0, 7440, 180)
    ChrSetPos(0x000E, -1090, 0, 8810, 180)
    ChrSetPos(0x000F, -290, 0, 8810, 180)
    ChrSetPos(0x0010, 510, 0, 8810, 180)
    ChrSetPos(0x0011, 1300, 0, 8810, 180)

    ChrTalk(
        0x00FE,
        (
            '#3110450030V好，那我去\n',
            '向队长传达……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)
    ChrSetDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#3110450031V看来不必了……\n',
            '他自己出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450032V#1004F#3P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_70(0x0000, 450)
    Sleep(1000)

    Fade(1000)
    CameraMove(-240, 9150, -5410, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0009, 0, 0, -3780, 0)
    ChrSetPos(0x0101, -540, 0, -5810, 0)
    ChrSetPos(0x00F7, 660, 0, -5820, 0)
    ChrSetPos(0x00F8, -670, 220, -7420, 0)
    ChrSetPos(0x00F9, 820, 230, -7580, 0)
    OP_0D()
    CreateThread(0x0009, 0x01, 0x01, 0x0004)

    @scena.Lambda('lambda_0967')
    def lambda_0967():
        OP_67(0, 6930, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0967)

    @scena.Lambda('lambda_097F')
    def lambda_097F():
        CameraMove(0, 0, -4270, 8000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_097F)

    @scena.Lambda('lambda_0997')
    def lambda_0997():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_0997)

    Sleep(2000)

    @scena.Lambda('lambda_09AC')
    def lambda_09AC():
        ChrTurnDirection(0x0101, 0x000B, 400)
        Yield()

        Jump('lambda_09AC')

    DispatchAsync2(0x0101, 0x0001, lambda_09AC)

    @scena.Lambda('lambda_09BD')
    def lambda_09BD():
        ChrTurnDirection(0x00F7, 0x000B, 400)
        Yield()

        Jump('lambda_09BD')

    DispatchAsync2(0x00F7, 0x0001, lambda_09BD)

    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_09F8')
    def lambda_09F8():
        ChrWalkTo(0x000B, -690, 0, -3960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_09F8)

    @scena.Lambda('lambda_0A13')
    def lambda_0A13():
        ChrWalkTo(0x000D, 870, 0, -3580, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0A13)

    @scena.Lambda('lambda_0A2E')
    def lambda_0A2E():
        ChrWalkTo(0x0010, 510, 0, -2190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0A2E)

    Sleep(35)

    @scena.Lambda('lambda_0A4E')
    def lambda_0A4E():
        ChrWalkTo(0x000E, -1090, 0, -2190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0A4E)

    Sleep(25)

    @scena.Lambda('lambda_0A6E')
    def lambda_0A6E():
        ChrWalkTo(0x000F, -290, 0, -2190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0A6E)

    @scena.Lambda('lambda_0A89')
    def lambda_0A89():
        ChrWalkTo(0x0011, 1300, 0, -2190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0A89)

    TerminateThread(0x00FE, 0x01)
    WaitForThreadExit(0x000B, 0x0001)
    TerminateThread(0x000B, 0x00)
    OP_4A(0x000B, 0)
    WaitForThreadExit(0x000D, 0x0001)
    TerminateThread(0x000D, 0x00)
    OP_4A(0x000D, 0)
    WaitForThreadExit(0x0010, 0x0001)
    TerminateThread(0x0010, 0x00)
    OP_4A(0x0010, 0)
    WaitForThreadExit(0x000E, 0x0001)
    TerminateThread(0x000E, 0x00)
    OP_4A(0x000E, 0)
    WaitForThreadExit(0x000F, 0x0001)
    TerminateThread(0x000F, 0x00)
    OP_4A(0x000F, 0)
    TerminateThread(0x0011, 0x00)
    OP_4A(0x0011, 0)
    WaitForThreadExit(0x00F8, 0x0000)
    OP_73(0x0000)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0101, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010450033V#1004F啊……希德少校！？',
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
        'loc_B5A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450034V#052F真是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B5A(): pass

    label('loc_B5A')

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620230535V#701F哈哈，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230536V拉赛尔博士绑架事件的事情\n',
            '给你们添了不少麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230537V一直想如果有机会的话\n',
            '要好好地向你们道歉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450038V#1016F啊哈哈，没关系啦。\n',
            '你不是也放我们逃跑了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620230540V#703F是吗……\n',
            '你们能这么想我真是松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450040V#1006F对了，我们今天\n',
            '是看了公告板而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450041V好像是在进行\n',
            '特别训练吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620450042V#701F嗯，本来只是像往常一样的\n',
            '定期训练……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450043V不过，摩尔根将军马上\n',
            '就要来视察这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450044V为了鼓舞士气，\n',
            '我紧急变更了训练内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450045V#1007F原来如此，可以理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450046V要是被那个大嗓门喝斥下来\n',
            '那可真不好受啊。',
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
        'loc_E26',
    )

    ChrTalk(
        0x0103,
        (
            '#0030450047V#021F呵呵，的确如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E49')

    def _loc_E26(): pass

    label('loc_E26')

    ChrTalk(
        0x0105,
        (
            '#0060450048V#041F呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E49(): pass

    label('loc_E49')

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620450049V#703F本来这工作属于\n',
            '卡西乌斯准将的管辖范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450050V不过很不凑巧，他刚好不在。\n',
            '所以就由我暂时负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450051V#1011F哦，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450052V#1015F是吗……\n',
            '老爸他平时也在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620450053V#701F这次他很快就会回来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450054V如果你们在蔡斯逗留一段时间的话，\n',
            '我想应该有机会遇见他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450055V#1017F啊，嗯……也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 225, 400)

    ChrTalk(
        0x000D,
        (
            '#3170450056V希德中校，时间已经……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 45, 400)

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620450057V#700F哦，聊过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450058V#703F那么，贝尔克副队长。\n',
            '接下来的说明就由你负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450059V#1015F咦，中校……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450060V我记得以前\n',
            '好像是希德少校吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450061V#702F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450062V其实有任免命令下达，\n',
            '我晋升为中校了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200588V#1011F噢～原来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230545V#1001F恭喜你，希德中校！',
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
        'loc_11CF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450065V#051F哈哈，这不是很好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230548V像你这样优秀的人\n',
            '应该要得到嘉奖才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11CF(): pass

    label('loc_11CF')

    ChrTalk(
        0x000B,
        (
            '#0620230549V#701F那个……谢谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450068V我只是履行了身为士官的义务而已，\n',
            '你们这么说，真有点不太好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450069V#1006F你看看，又来了～\n',
            '你真是太谦虚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450070V嗯，说得一点也没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450071V中校你应该再\n',
            '自豪一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 45, 400)

    ChrTalk(
        0x000B,
        (
            '#0620450072V#700F贝尔克副队长……\n',
            '你忘记了自己的职责吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450073V……失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1336')
    def lambda_1336():
        ChrSetDirection(0x000D, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1336)

    Sleep(250)

    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000D,
        (
            '#3170450074V那么，我就赶快\n',
            '说明委托的内容吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 0, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_13DF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450075V#050F委托内容就是参加训练吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450076V那具体应该做点什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1430')

    def _loc_13DF(): pass

    label('loc_13DF')

    ChrTalk(
        0x0103,
        (
            '#0030450077V#020F委托内容就是参加训练吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450078V具体应该做点什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1430(): pass

    label('loc_1430')

    ChrTalk(
        0x000D,
        (
            '#3170450079V希望你们参加模拟战斗，\n',
            '对手就是士兵们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450080V战斗预定为二连战，\n',
            '中间没有休息时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450081V不把握好节奏的话，\n',
            '就有可能成为苦战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450082V#1015F没有休息的连战啊……\n',
            '这、这好像有点难度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450083V确实不容易……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450084V你们的任务是通过战斗\n',
            '为士兵们做出示范。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450085V所以希望你们不要手下留情，\n',
            '要以必胜的信念进行战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450086V#1002F……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1610',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450087V#051F这不用你提醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1635')

    def _loc_1610(): pass

    label('loc_1610')

    ChrTalk(
        0x0103,
        (
            '#0030450088V#525F这不用你提醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1635(): pass

    label('loc_1635')

    ChrTalk(
        0x000B,
        (
            '#0620450089V#701F哈哈，真是值得信赖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450090V那么，带诸位游击士\n',
            '去训练场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450091V是，了解！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620450092V#700F待会儿训练场见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 0, 400)

    @scena.Lambda('lambda_16DD')
    def lambda_16DD():
        ChrTurnDirection(0x0101, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16DD)

    @scena.Lambda('lambda_16EB')
    def lambda_16EB():
        ChrSetDirection(0x000E, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_16EB)

    ChrSetDirection(0x000F, 0, 400)
    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1705')
    def lambda_1705():
        ChrWalkTo(0x000B, -690, 0, 7060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1705)

    Sleep(20)

    @scena.Lambda('lambda_1725')
    def lambda_1725():
        ChrWalkTo(0x000E, -1090, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1725)

    Sleep(30)

    @scena.Lambda('lambda_1745')
    def lambda_1745():
        ChrWalkTo(0x000F, -290, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1745)

    Sleep(2000)

    ChrWalkTo(0x000D, 870, 0, -4040, 2000, 0x00)

    ChrTalk(
        0x000D,
        (
            '#3170450093V那么就由我来带路。\n',
            '跟我来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 0, 400)

    @scena.Lambda('lambda_17AD')
    def lambda_17AD():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_17AD)

    ChrSetDirection(0x0011, 0, 400)
    TerminateThread(0x0010, 0x01)

    @scena.Lambda('lambda_17C6')
    def lambda_17C6():
        ChrWalkTo(0x000D, 870, 0, 7440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_17C6)

    Sleep(30)

    @scena.Lambda('lambda_17E6')
    def lambda_17E6():
        ChrWalkTo(0x0010, 510, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_17E6)

    Sleep(20)

    @scena.Lambda('lambda_1806')
    def lambda_1806():
        ChrWalkTo(0x0011, 1300, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1806)

    Sleep(1000)

    @scena.Lambda('lambda_1826')
    def lambda_1826():
        ChrWalkTo(0x0101, -540, 0, 5790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1826)

    Sleep(150)

    @scena.Lambda('lambda_1846')
    def lambda_1846():
        ChrWalkTo(0x00F7, 660, 0, 5790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1846)

    Sleep(250)

    @scena.Lambda('lambda_1866')
    def lambda_1866():
        ChrWalkTo(0x00F8, -670, 0, 7170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1866)

    @scena.Lambda('lambda_1881')
    def lambda_1881():
        ChrWalkTo(0x00F9, 820, 0, 7170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1881)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C3101._SN', 0, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x18B3
@scena.Code('func_03_18B3')
def func_03_18B3():
    EventBegin(0x00)
    CameraMove(500, 80, -3600, 0)
    OP_67(0, 8080, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -70, 0, -5570, 0)
    ChrSetPos(0x00F7, 880, 150, -6000, 0)
    ChrSetPos(0x00F8, -320, 200, -7040, 0)
    ChrSetPos(0x00F9, 1170, 210, -7190, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x000B, -540, 0, -3960, 180)
    ChrSetPos(0x000D, 820, 0, -3580, 180)
    ChrSetPos(0x000E, -1300, 0, -2190, 180)
    ChrSetPos(0x000F, -400, 0, -2190, 180)
    ChrSetPos(0x0010, 400, 0, -2190, 180)
    ChrSetPos(0x0011, 1300, 0, -2190, 180)
    ChrSetPos(0x0009, 2440, 0, -4250, 180)
    OP_4A(0x0009, 255)
    OP_6F(0x0000, 450)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_1A87',
    )

    ChrTalk(
        0x000B,
        (
            '#0620450232V#701F#1P──诸位游击士。\n',
            '让你们今天特意过来真不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450233V今后也许还会\n',
            '请你们进行协助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450234V到时候\n',
            '也请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006D, 0x01, 0x0080)
    OP_28(0x006D, 0x04, 0x10)

    Jump('loc_1B6B')

    def _loc_1A87(): pass

    label('loc_1A87')

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1B6B',
    )

    ChrTalk(
        0x000B,
        (
            '#0620450235V#703F#1P──诸位游击士。\n',
            '让你们今天特意过来真不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450236V很遗憾，\n',
            '训练成果并不是很好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450237V#701F今后也许还会\n',
            '请你们进行协助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450234V到时候\n',
            '也请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006D, 0x01, 0x0100)
    OP_28(0x006D, 0x04, 0x80)
    OP_28(0x006D, 0x04, 0x40)

    def _loc_1B6B(): pass

    label('loc_1B6B')

    ChrTalk(
        0x0101,
        (
            '#0010450239V#1006F#3P嗯，我们才要请你们多多关照呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1C14',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450240V#050F#2P我们也希望尽可能地\n',
            '和军方多合作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450241V有需要的话请随时\n',
            '与协会联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C7A')

    def _loc_1C14(): pass

    label('loc_1C14')

    ChrTalk(
        0x0103,
        (
            '#0030450242V#020F#2P我们也希望尽可能地\n',
            '和军方多合作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450243V有需要的话请随时\n',
            '与协会联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C7A(): pass

    label('loc_1C7A')

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_1EDB',
    )

    ChrTalk(
        0x000B,
        (
            '#0620450244V#701F#1P就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450245V那么最后──\n',
            '我要把这个交给诸位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450246V──贝尔克副队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3170450247V是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x000D, 0x0000, 0x000003E8, 0x000007D0, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['斗魂扎头巾']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['斗魂扎头巾'], 1)
    Sleep(500)

    OP_94(0x01, 0x000D, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

    ChrTalk(
        0x000B,
        (
            '#0620450248V#701F#1P虽是微不足道的东西，\n',
            '就当成对你们协助训练的谢礼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450249V请你们有效地利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450250V#1001F#3P谢谢你，希德中校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1E51',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450251V#051F#2P不好意思了，真是好东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E7D')

    def _loc_1E51(): pass

    label('loc_1E51')

    ChrTalk(
        0x0103,
        (
            '#0030450252V#021F#2P呵呵，真是好东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E7D(): pass

    label('loc_1E7D')

    ChrTalk(
        0x000B,
        (
            '#0620450253V#701F#1P那我就先告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450254V我衷心期待着与诸位\n',
            '再度相会的日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F1D')

    def _loc_1EDB(): pass

    label('loc_1EDB')

    ChrTalk(
        0x000B,
        (
            '#0620450255V#701F#1P承蒙夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620450256V那我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1F1D(): pass

    label('loc_1F1D')

    @scena.Lambda('lambda_1F23')
    def lambda_1F23():
        ChrSetDirection(0x000E, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1F23)

    @scena.Lambda('lambda_1F31')
    def lambda_1F31():
        ChrSetDirection(0x000F, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1F31)

    @scena.Lambda('lambda_1F3F')
    def lambda_1F3F():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1F3F)

    @scena.Lambda('lambda_1F4D')
    def lambda_1F4D():
        ChrSetDirection(0x0011, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1F4D)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_1F60')
    def lambda_1F60():
        ChrSetDirection(0x000B, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1F60)

    Sleep(250)

    ChrSetDirection(0x000D, 180, 400)
    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_1F7F')
    def lambda_1F7F():
        ChrWalkTo(0x000B, -540, 0, 7060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1F7F)

    @scena.Lambda('lambda_1F9A')
    def lambda_1F9A():
        ChrWalkTo(0x000D, 820, 0, 7440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1F9A)

    @scena.Lambda('lambda_1FB5')
    def lambda_1FB5():
        ChrWalkTo(0x000E, -1300, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1FB5)

    @scena.Lambda('lambda_1FD0')
    def lambda_1FD0():
        ChrWalkTo(0x000F, -400, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1FD0)

    @scena.Lambda('lambda_1FEB')
    def lambda_1FEB():
        ChrWalkTo(0x0010, 400, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1FEB)

    @scena.Lambda('lambda_2006')
    def lambda_2006():
        ChrWalkTo(0x0011, 1300, 0, 8810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2006)

    Sleep(1000)

    OP_70(0x0000, 0)
    Sleep(350)

    CreateThread(0x0009, 0x01, 0x01, 0x0005)
    OP_73(0x0000)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0011, 0x0001)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    EventEnd(0x00)
    OP_4B(0x0009, 255)

    Return()

# id: 0x0004 offset: 0x204A
@scena.Code('func_04_204A')
def func_04_204A():
    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x00FE, 2450, 0, -3780, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0005 offset: 0x206D
@scena.Code('func_05_206D')
def func_05_206D():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x0009, 0, 0, -3780, 2000, 0x00)
    ChrWalkTo(0x0009, 0, 0, -3230, 2000, 0x00)
    ChrSetDirection(0x0009, 180, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
