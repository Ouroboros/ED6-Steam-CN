import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3303_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3303_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C3303_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C2',
    )

    Return()

    def _loc_C2(): pass

    label('loc_C2')

    EventBegin(0x00)

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_D1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_D1(): pass

    label('loc_D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14C',
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
            TXT(0x00, '【◇上部遇到过吉米的情况下】\n'),
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
        (0x00000000, 'loc_146'),
        (-1, 'loc_14C'),
    )

    def _loc_146(): pass

    label('loc_146')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_14C')

    def _loc_14C(): pass

    label('loc_14C')

    ChrClearFlags(0x0008, 0x0080)
    OP_72(0x0000, 0x0004)
    ChrSetPos(0x0008, 9460, 40, 112460, 90)
    ChrSetPos(0x0010, 9460, -40, 124460, 0)

    @scena.Lambda('lambda_017E')
    def lambda_017E():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_017E)

    @scena.Lambda('lambda_018C')
    def lambda_018C():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_018C)

    @scena.Lambda('lambda_019A')
    def lambda_019A():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_019A)

    @scena.Lambda('lambda_01A8')
    def lambda_01A8():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_01A8)

    WaitForThreadExit(0x0003, 0x0001)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460077V#1004F啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460078V那、那是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A')

    def _loc_21A(): pass

    label('loc_21A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_249',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460079V#052F那家伙是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A')

    def _loc_249(): pass

    label('loc_249')

    ChrTalk(
        0x0103,
        (
            '#0030460080V#023F那是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A(): pass

    label('loc_26A')

    CameraMove(11140, 0, 112460, 3000)

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460081V哈、哈、哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460082V总、总算把宝箱\n',
            '捞上来了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 9460, 10, 111010, 2000, 0x00)
    ChrWalkTo(0x0008, 11140, -50, 111010, 2000, 0x00)
    ChrSetDirection(0x0008, 0, 400)
    Sleep(1000)

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460083V没错。\n',
            '终于找到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 15, 0, 300, 3000)
    Sleep(1000)

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460084V#5P#4S哇～终于找到了～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    ChrTalk(
        0x0010,
        (
            '#1770460085V#4S#4P……终于找到了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1770460086V#3S#4P……找到了～！　#2S……到了～！　#1S……了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrSetDirection(0x0008, 270, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0008)
    Sleep(400)

    OP_62(0x0008, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrSetDirection(0x0008, 0, 400)
    Sleep(2000)

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460087V#5P#4S吉米了不起！　我爱你～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#1770460088V#4S#4P……了不起！　我爱你～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1770460089V#3S#4P……我爱你～！　#2S……爱你～！　#1S……你～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    OP_63(0x0008)

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460090V……看、看来不是\n',
            '玩这个的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FormationAddMember(ChrTable['吉米'], 0xFA, 0xFF)
    ChrSetFlags(0x0148, 0x0008)
    CreateThread(0x0101, 0x00, 0x01, 0x0001)
    CreateThread(0x00F7, 0x00, 0x01, 0x0002)
    CreateThread(0x00F8, 0x00, 0x01, 0x0003)
    CreateThread(0x00F9, 0x00, 0x01, 0x0004)

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460091V在魔兽到来之前\n',
            '得先确认里面的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05DC')
    def lambda_05DC():
        CameraMove(11140, 0, 110010, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_05DC)

    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x0008, 0x0000)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0008, 0, 0, 0, 600, 5000)
    Sleep(500)

    OP_63(0x0008)
    ChrTurnDirection(0x0008, 0x0101, 400)

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460092V哇、哇！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460093V怎、怎么是你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7CC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460094V#1007F#3P你、你在这儿玩什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460095V还是和以前一样完全不知道何谓紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460096V咦？你、你是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460097V#1006F#3P好久不见，吉米先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460098V我们曾经在卢安\n',
            '接受过你的工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460099V哇～真怀念啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460100V对了，那你们今天\n',
            '来这儿干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_935')

    def _loc_7CC(): pass

    label('loc_7CC')

    ChrTalk(
        0x0101,
        (
            '#0010460094V#1007F#3P你、你在这里玩什么啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460102V真是完全没紧张感的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460103V说、说我没紧张感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460104V哼，好歹我也去过了\n',
            '那些需要调查的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年',
        (
            '#1770460105V那么，你们到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460106V#1006F#3P我们是游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460107V你是吉米先生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460108V嗯，我就是吉米。\n',
            '有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_935(): pass

    label('loc_935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_999',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460109V#050F#4P你投宿的地方\n',
            '发出了搜寻请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460110V所以我们就来\n',
            '找你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F3')

    def _loc_999(): pass

    label('loc_999')

    ChrTalk(
        0x0103,
        (
            '#0030460111V#020F#4P你投宿的地方\n',
            '发出了搜寻请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460112V所以我们就来\n',
            '找你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F3(): pass

    label('loc_9F3')

    ChrTalk(
        0x0008,
        (
            '#1770460113V这样啊，原来你们\n',
            '是从蔡斯来接我的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460114V不过很遗憾，\n',
            '现在我还不能回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460115V其实我刚刚完成了一个\n',
            '绝世的大发现。',
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
        'loc_ACE',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460116V#064F就是那个……宝箱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3B')

    def _loc_ACE(): pass

    label('loc_ACE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B06',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460117V#033F就是那个宝箱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3B')

    def _loc_B06(): pass

    label('loc_B06')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B3B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460118V#044F就是那个宝箱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B3B(): pass

    label('loc_B3B')

    ChrTalk(
        0x0008,
        (
            '#1770460119V嗯，好不容易\n',
            '捞上来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460120V#1004F#3P捞上来的……\n',
            '莫非是从湖里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460121V真是藏在了一个\n',
            '了不得的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460122V嗯，不愧是\n',
            '大海盗希尔玛的宝藏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_CCD',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460123V#1004F#3P啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460124V那是吉米先生\n',
            '找到的海盗宝藏吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460125V哼哼，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460126V是我根据好几张古地图\n',
            '费尽千辛万苦才找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E2B')

    def _loc_CCD(): pass

    label('loc_CCD')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460127V#1004F#3P啊！？　是、是真的吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460128V#1016F……等等，虽然刚才装着惊讶了一下，\n',
            '不过那个大海盗某某某到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1770460129V你竟然不知道大海盗\n',
            '希尔玛吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460130V真令人不敢相信。\n',
            '这也算是一个卢安市民？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460131V#1016F#3P那个……这里是\n',
            '蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E2B(): pass

    label('loc_E2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_EA5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460132V#551F#4P好了，先不管那么多，\n',
            '总之动作快一点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460133V再磨磨蹭蹭的话\n',
            '就会被魔兽发现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F15')

    def _loc_EA5(): pass

    label('loc_EA5')

    ChrTalk(
        0x0103,
        (
            '#0030460134V#025F#4P好了，这些都无所谓，\n',
            '总之动作快一点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460135V再磨磨蹭蹭的话\n',
            '就会被魔兽发现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F15(): pass

    label('loc_F15')

    ChrTalk(
        0x0008,
        (
            '#1770460136V对，差点给忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460137V好、好吧。\n',
            '那么，要打开箱子喽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)
    OP_94(0x01, 0x0008, 0x0000, 0x000000C8, 0x000003E8, 0x00)
    Sleep(1000)

    OP_70(0x0000, 60)
    PlaySE(43, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010460138V#1002F#3P你、你在磨蹭什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0008)
    OP_94(0x01, 0x0008, 0x0000, 0x000000C8, 0x000003E8, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1770460139V等、等等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460140V这、这到底是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    Sleep(1000)

    PlaySE(172, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0008, 0, 0, -400, 600, 5000)

    ChrTalk(
        0x0008,
        (
            '#1770460141V哇、哇哇！？\n',
            '吓我一跳～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x00, 0x01, 0x0005)
    CreateThread(0x00F7, 0x00, 0x01, 0x0006)
    CreateThread(0x00F8, 0x00, 0x01, 0x0007)
    CreateThread(0x00F9, 0x00, 0x01, 0x0008)
    Sleep(2000)

    TerminateThread(0x0101, 0x00)
    TerminateThread(0x00F7, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010460142V#1004F#3P这、这是什么声音！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460143V#1020F难道是……陷阱！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_115D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460144V#057F#4P不知道……\n',
            '不过我有种不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1198')

    def _loc_115D(): pass

    label('loc_115D')

    ChrTalk(
        0x0103,
        (
            '#0030460145V#022F#4P不知道……\n',
            '不过我有种不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1198(): pass

    label('loc_1198')

    PlaySE(587, 0x00, 0x32)
    Sleep(200)

    PlaySE(587, 0x00, 0x32)
    Sleep(500)

    PlaySE(587, 0x00, 0x46)
    Sleep(200)

    PlaySE(587, 0x00, 0x46)
    Sleep(200)

    PlaySE(587, 0x00, 0x46)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1236',
    )

    ChrSetDirection(0x0108, 180, 400)
    Fade(500)
    ChrSetChipByIndex(0x0108, 20)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080460146V#070F呼，看来是猜中了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460147V#072F……这么快就来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1307')

    def _loc_1236(): pass

    label('loc_1236')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12A2',
    )

    ChrSetDirection(0x0104, 180, 400)
    Fade(500)
    ChrSetChipByIndex(0x0104, 14)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040460148V#035F呼，看来是猜中了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460149V……这么快就来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1307')

    def _loc_12A2(): pass

    label('loc_12A2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1307',
    )

    ChrSetDirection(0x0105, 180, 400)
    Fade(500)
    ChrSetChipByIndex(0x0105, 16)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060460150V#042F看来猜中了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460151V……这么快就来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1307(): pass

    label('loc_1307')

    CreateThread(0x0008, 0x01, 0x01, 0x0010)

    @scena.Lambda('lambda_1314')
    def lambda_1314():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1314)

    @scena.Lambda('lambda_1322')
    def lambda_1322():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1322)

    @scena.Lambda('lambda_1330')
    def lambda_1330():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1330)

    @scena.Lambda('lambda_133E')
    def lambda_133E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_133E)

    @scena.Lambda('lambda_134C')
    def lambda_134C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_134C)

    WaitForThreadExit(0x0008, 0x0001)
    PlayBGM(41)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    CreateThread(0x000A, 0x01, 0x01, 0x0009)
    CreateThread(0x000B, 0x01, 0x01, 0x000A)
    CreateThread(0x000C, 0x01, 0x01, 0x000B)
    CreateThread(0x000D, 0x01, 0x01, 0x000C)
    CreateThread(0x000E, 0x01, 0x01, 0x000D)
    CreateThread(0x000F, 0x01, 0x01, 0x000E)

    @scena.Lambda('lambda_13A9')
    def lambda_13A9():
        CameraMove(11140, 0, 95380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13A9)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(2500)

    ChrSetPos(0x0008, 10000, 20, 111560, 135)
    ChrSetPos(0x0101, 10430, -70, 109710, 225)
    ChrSetPos(0x00F7, 11930, -70, 109190, 180)
    ChrSetPos(0x00F8, 13420, -30, 109960, 135)
    ChrSetPos(0x00F9, 13630, -30, 111710, 135)
    ChrSetChipByIndex(0x0101, 8)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_142E',
    )

    ChrSetChipByIndex(0x0106, 12)

    Jump('loc_1433')

    def _loc_142E(): pass

    label('loc_142E')

    ChrSetChipByIndex(0x0103, 10)

    def _loc_1433(): pass

    label('loc_1433')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1446',
    )

    ChrSetChipByIndex(0x0107, 18)

    def _loc_1446(): pass

    label('loc_1446')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1459',
    )

    ChrSetChipByIndex(0x0104, 14)

    def _loc_1459(): pass

    label('loc_1459')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_146C',
    )

    ChrSetChipByIndex(0x0105, 16)

    def _loc_146C(): pass

    label('loc_146C')

    @scena.Lambda('lambda_1472')
    def lambda_1472():
        CameraMove(11140, 0, 111010, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1472)

    WaitForThreadExit(0x0101, 0x0001)
    ChrMoveTo(0x0008, 9380, 40, 112160, 1000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1770460152V哇、哇哇～～！\n',
            '从这里冒出来了吗～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, 7000, -3500, 119800, 135)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0009, 800)

    ChrTalk(
        0x0101,
        (
            '#0010460153V#1005F吉米先生，你背后！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1542')
    def lambda_1542():
        CameraMove(8400, 0, 116840, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1542)

    @scena.Lambda('lambda_155A')
    def lambda_155A():
        CameraSetDistance(2480, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_155A)

    @scena.Lambda('lambda_156A')
    def lambda_156A():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_156A)

    Sleep(400)

    @scena.Lambda('lambda_157F')
    def lambda_157F():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_157F')

    DispatchAsync2(0x00F7, 0x0002, lambda_157F)

    @scena.Lambda('lambda_1590')
    def lambda_1590():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1590')

    DispatchAsync2(0x00F8, 0x0002, lambda_1590)

    @scena.Lambda('lambda_15A1')
    def lambda_15A1():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_15A1')

    DispatchAsync2(0x00F9, 0x0002, lambda_15A1)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(227, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1770460154V咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp012_00.eff')
    LoadEffect(0x01, 'monster\\\\msc0591.eff')
    LoadEffect(0x02, 'monster\\\\msc0590.eff')
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_162D')
    def lambda_162D():
        OP_67(0, 5840, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_162D)

    @scena.Lambda('lambda_1645')
    def lambda_1645():
        CameraMove(8300, 0, 115820, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1645)

    @scena.Lambda('lambda_165D')
    def lambda_165D():
        CameraSetDistance(2640, 2000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_165D)

    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0800)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_1687')
    def lambda_1687():
        ChrJumpTo(0x00FE, 8610, 650, 113340, 8000, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1687)

    @scena.Lambda('lambda_16A5')
    def lambda_16A5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 100)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_16A5)

    PlaySE(228, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x00FF, 7000, -1500, 119800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    @scena.Lambda('lambda_16F6')
    def lambda_16F6():
        OP_99(0x00FE, 0x01, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_16F6)

    WaitForThreadExit(0x0009, 0x0000)
    PlaySE(229, 0x00, 0x64)
    OP_7C(0, 600, 3000, 200)

    @scena.Lambda('lambda_1721')
    def lambda_1721():
        ChrJumpTo(0x00FE, 9760, 30, 111820, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1721)

    @scena.Lambda('lambda_173F')
    def lambda_173F():
        OP_9E(0x00FE, 20, 0, 0, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_173F)

    @scena.Lambda('lambda_1759')
    def lambda_1759():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 1000, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1759)

    @scena.Lambda('lambda_1777')
    def lambda_1777():
        OP_99(0x00FE, 0x04, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1777)

    WaitForThreadExit(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 0)
    WaitForThreadExit(0x0009, 0x0000)
    ChrClearFlags(0x0009, 0x0800)
    PlaySE(229, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)

    @scena.Lambda('lambda_17B6')
    def lambda_17B6():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_17B6)

    @scena.Lambda('lambda_17D4')
    def lambda_17D4():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_17D4)

    WaitForThreadExit(0x0008, 0x0000)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)
    ChrSetDirection(0x0101, 315, 0)
    ChrSetDirection(0x00F7, 315, 0)
    ChrSetDirection(0x00F8, 315, 0)
    ChrSetDirection(0x00F9, 315, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_1827')
    def lambda_1827():
        CameraMove(10100, 0, 112800, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1827)

    @scena.Lambda('lambda_183F')
    def lambda_183F():
        OP_6C(356000, 2000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_183F)

    @scena.Lambda('lambda_184F')
    def lambda_184F():
        CameraSetDistance(3340, 2000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_184F)

    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_1869')
    def lambda_1869():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1869')

    DispatchAsync2(0x0009, 0x0003, lambda_1869)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0008, 10920, -50, 111000, 3000, 0x00)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#1770460155V#2P哇、哇哇！\n',
            '这边也有啊～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(1000)

    ChrSetFlags(0x0009, 0x0800)
    TerminateThread(0x0009, 0x03)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 0)
    OP_99(0x0009, 0x00, 0x05, 1500)
    Sleep(200)

    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    OP_99(0x0009, 0x05, 0x07, 1500)
    ChrClearFlags(0x0009, 0x0800)
    ChrSetFlags(0x0009, 0x8000)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_1932')
    def lambda_1932():
        OP_99(0x00FE, 0x00, 0x01, 1500)
        Yield()

        Jump('lambda_1932')

    DispatchAsync2(0x0009, 0x0003, lambda_1932)

    @scena.Lambda('lambda_1945')
    def lambda_1945():
        OP_7C(50, 0, 3000, 100)
        Yield()

        Jump('lambda_1945')

    DispatchAsync2(0x0009, 0x0002, lambda_1945)

    PlayEffect(0x02, 0x01, 0x0009, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010460156V#1019F这、这是什么……！？',
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
        'loc_19F3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460157V#065F啊、哎呀……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19F3(): pass

    label('loc_19F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A33',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460158V#070F呼……\n',
            '看样子是新的主人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A33(): pass

    label('loc_1A33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A69',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460159V#054F#3P小心！　敌人来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A95')

    def _loc_1A69(): pass

    label('loc_1A69')

    ChrTalk(
        0x0103,
        (
            '#0030460160V#024F#3P小心！　敌人来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A95(): pass

    label('loc_1A95')

    OP_63(0x0008)
    StopEffect(0x01, 0x02)
    TerminateThread(0x0009, 0x02)
    TerminateThread(0x0009, 0x03)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_1ABC')
    def lambda_1ABC():
        ChrJumpTo(0x00FE, 11780, 0, 110520, 1000, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1ABC)

    @scena.Lambda('lambda_1ADA')
    def lambda_1ADA():
        OP_99(0x00FE, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1ADA)

    PlaySE(163, 0x00, 0x64)
    Sleep(200)

    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    ChrSetPos(0x0010, 11780, 0, 110520, 0)
    ChrTurnDirection(0x000A, 0x0010, 0)
    ChrTurnDirection(0x000B, 0x0010, 0)
    ChrTurnDirection(0x000C, 0x0010, 0)
    ChrTurnDirection(0x000D, 0x0010, 0)
    ChrTurnDirection(0x000E, 0x0010, 0)
    ChrTurnDirection(0x000F, 0x0010, 0)

    @scena.Lambda('lambda_1B47')
    def lambda_1B47():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1B47)

    @scena.Lambda('lambda_1B5D')
    def lambda_1B5D():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1B5D)

    @scena.Lambda('lambda_1B73')
    def lambda_1B73():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1B73)

    @scena.Lambda('lambda_1B89')
    def lambda_1B89():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1B89)

    @scena.Lambda('lambda_1B9F')
    def lambda_1B9F():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_1B9F)

    @scena.Lambda('lambda_1BB5')
    def lambda_1BB5():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1BB5)

    Sleep(200)

    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    Battle(0x000001EA, 0x00000000, 0x01, 0x0000, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1C1B'),
        (-1, 'loc_1C1E'),
    )

    def _loc_1C1B(): pass

    label('loc_1C1B')

    OP_B4(0x00)

    Return()

    def _loc_1C1E(): pass

    label('loc_1C1E')

    Call(1, 0x000F)

    Return()

# id: 0x0001 offset: 0x1C23
@scena.Code('func_01_1C23')
def func_01_1C23():
    ChrSetPos(0x0101, 11700, -30, 102960, 0)
    ChrWalkTo(0x0101, 11700, -80, 109130, 2000, 0x00)

    Return()

# id: 0x0002 offset: 0x1C49
@scena.Code('func_02_1C49')
def func_02_1C49():
    Sleep(400)

    ChrSetPos(0x00F7, 11100, -10, 102320, 0)
    ChrWalkTo(0x00F7, 11100, -40, 107930, 2000, 0x00)

    Return()

# id: 0x0003 offset: 0x1C74
@scena.Code('func_03_1C74')
def func_03_1C74():
    Sleep(400)

    Sleep(200)

    ChrSetPos(0x00F8, 12540, -50, 103220, 0)
    ChrWalkTo(0x00F8, 12540, -50, 108410, 2000, 0x00)

    Return()

# id: 0x0004 offset: 0x1CA4
@scena.Code('func_04_1CA4')
def func_04_1CA4():
    Sleep(400)

    Sleep(200)

    Sleep(600)

    ChrSetPos(0x00F9, 11970, -40, 102840, 0)
    ChrWalkTo(0x00F9, 11970, -40, 107030, 2000, 0x00)

    Return()

# id: 0x0005 offset: 0x1CD9
@scena.Code('func_05_1CD9')
def func_05_1CD9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1CFD',
    )

    ChrSetDirection(0x0101, 315, 400)
    Sleep(200)

    ChrSetDirection(0x0101, 45, 400)
    Sleep(500)

    Jump('func_05_1CD9')

    def _loc_1CFD(): pass

    label('loc_1CFD')

    Return()

# id: 0x0006 offset: 0x1CFE
@scena.Code('func_06_1CFE')
def func_06_1CFE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D27',
    )

    Sleep(100)

    ChrSetDirection(0x00F7, 270, 400)
    Sleep(200)

    ChrSetDirection(0x00F7, 89, 400)
    Sleep(300)

    Jump('func_06_1CFE')

    def _loc_1D27(): pass

    label('loc_1D27')

    Return()

# id: 0x0007 offset: 0x1D28
@scena.Code('func_07_1D28')
def func_07_1D28():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D51',
    )

    Sleep(100)

    ChrSetDirection(0x00F8, 89, 400)
    Sleep(200)

    ChrSetDirection(0x00F8, 270, 400)
    Sleep(400)

    Jump('func_07_1D28')

    def _loc_1D51(): pass

    label('loc_1D51')

    Return()

# id: 0x0008 offset: 0x1D52
@scena.Code('func_08_1D52')
def func_08_1D52():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D76',
    )

    ChrSetDirection(0x00F9, 45, 400)
    Sleep(200)

    ChrSetDirection(0x00F9, 315, 400)
    Sleep(500)

    Jump('func_08_1D52')

    def _loc_1D76(): pass

    label('loc_1D76')

    Return()

# id: 0x0009 offset: 0x1D77
@scena.Code('func_09_1D77')
def func_09_1D77():
    ChrSetPos(0x000A, 12070, 0, 82290, 0)
    OP_62(0x000A, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000A, 12070, 40, 93620, 5000, 0x00)
    ChrWalkTo(0x000A, 8910, 40, 96970, 5000, 0x00)
    OP_62(0x000A, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000A, 8910, 20, 100840, 5000, 0x00)
    ChrWalkTo(0x000A, 11860, -10, 104370, 5000, 0x00)
    OP_62(0x000A, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000A, 11860, -10, 105520, 5000, 0x00)
    ChrWalkTo(0x000A, 15590, -10, 110800, 5000, 0x00)
    ChrTurnDirection(0x000A, 0x0101, 400)
    OP_63(0x000A)
    PlaySE(587, 0x00, 0x50)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)

    Return()

# id: 0x000A offset: 0x1E4D
@scena.Code('func_0A_1E4D')
def func_0A_1E4D():
    Sleep(500)

    OP_62(0x000B, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrSetPos(0x000B, 12070, 0, 82290, 0)
    ChrWalkTo(0x000B, 12070, 40, 93620, 5000, 0x00)
    ChrWalkTo(0x000B, 8910, 40, 96970, 5000, 0x00)
    OP_62(0x000B, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000B, 8910, 20, 100840, 5000, 0x00)
    ChrWalkTo(0x000B, 11860, -10, 104370, 5000, 0x00)
    OP_62(0x000B, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000B, 11860, -10, 105520, 5000, 0x00)
    ChrWalkTo(0x000B, 8420, -10, 108650, 5000, 0x00)
    ChrTurnDirection(0x000B, 0x0101, 400)
    OP_63(0x000B)
    PlaySE(587, 0x00, 0x50)
    CreateThread(0x000B, 0x00, 0x06, 0x0002)

    Return()

# id: 0x000B offset: 0x1F28
@scena.Code('func_0B_1F28')
def func_0B_1F28():
    Sleep(1000)

    OP_62(0x000C, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrSetPos(0x000C, 12070, 0, 82290, 0)
    ChrWalkTo(0x000C, 12070, 40, 93620, 5000, 0x00)
    ChrWalkTo(0x000C, 8910, 40, 96970, 5000, 0x00)
    OP_62(0x000C, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000C, 8910, 20, 100840, 5000, 0x00)
    ChrWalkTo(0x000C, 11860, -10, 104370, 5000, 0x00)
    OP_62(0x000C, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000C, 11860, -10, 105520, 5000, 0x00)
    ChrWalkTo(0x000C, 15070, -50, 108860, 5000, 0x00)
    ChrTurnDirection(0x000C, 0x0101, 400)
    OP_63(0x000C)
    PlaySE(587, 0x00, 0x50)
    CreateThread(0x000C, 0x00, 0x06, 0x0002)

    Return()

# id: 0x000C offset: 0x2003
@scena.Code('func_0C_2003')
def func_0C_2003():
    Sleep(1500)

    OP_62(0x000D, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrSetPos(0x000D, 12070, 0, 82290, 0)
    ChrWalkTo(0x000D, 12070, 40, 93620, 5000, 0x00)
    ChrWalkTo(0x000D, 8910, 40, 96970, 5000, 0x00)
    OP_62(0x000D, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000D, 8910, 20, 100840, 5000, 0x00)
    ChrWalkTo(0x000D, 11860, -10, 104370, 5000, 0x00)
    OP_62(0x000D, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000D, 11860, -10, 105520, 5000, 0x00)
    ChrWalkTo(0x000D, 10150, -20, 107200, 5000, 0x00)
    ChrTurnDirection(0x000D, 0x0101, 400)
    OP_63(0x000D)
    PlaySE(587, 0x00, 0x50)
    CreateThread(0x000D, 0x00, 0x06, 0x0002)

    Return()

# id: 0x000D offset: 0x20DE
@scena.Code('func_0D_20DE')
def func_0D_20DE():
    Sleep(2000)

    OP_62(0x000E, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrSetPos(0x000E, 12070, 0, 82290, 0)
    ChrWalkTo(0x000E, 12070, 40, 93620, 5000, 0x00)
    ChrWalkTo(0x000E, 8910, 40, 96970, 5000, 0x00)
    OP_62(0x000E, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000E, 8910, 20, 100840, 5000, 0x00)
    ChrWalkTo(0x000E, 11860, -10, 104370, 5000, 0x00)
    OP_62(0x000E, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000E, 11860, -10, 105520, 5000, 0x00)
    ChrWalkTo(0x000E, 13700, -20, 107480, 5000, 0x00)
    ChrTurnDirection(0x000E, 0x0101, 400)
    OP_63(0x000E)
    PlaySE(587, 0x00, 0x50)
    CreateThread(0x000E, 0x00, 0x06, 0x0002)

    Return()

# id: 0x000E offset: 0x21B9
@scena.Code('func_0E_21B9')
def func_0E_21B9():
    Sleep(2500)

    OP_62(0x000F, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrSetPos(0x000F, 12070, 0, 82290, 0)
    ChrWalkTo(0x000F, 12070, 40, 93620, 5000, 0x00)
    ChrWalkTo(0x000F, 8910, 40, 96970, 5000, 0x00)
    OP_62(0x000F, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000F, 8910, 20, 100840, 5000, 0x00)
    ChrWalkTo(0x000F, 11860, -10, 104370, 5000, 0x00)
    OP_62(0x000F, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrWalkTo(0x000F, 11860, -10, 105520, 5000, 0x00)
    ChrWalkTo(0x000F, 11830, -20, 106760, 5000, 0x00)
    ChrTurnDirection(0x000F, 0x0101, 400)
    OP_63(0x000F)
    PlaySE(587, 0x00, 0x50)
    CreateThread(0x000F, 0x00, 0x06, 0x0002)

    Return()

# id: 0x000F offset: 0x2294
@scena.Code('func_0F_2294')
def func_0F_2294():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    FormationDelMember(0x47, 0xFF)
    MapSetFlags(0x00000010)
    OP_72(0x0000, 0x0004)
    OP_6F(0x0000, 60)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 9960, 20, 109000, 0)
    ChrSetPos(0x0101, 10430, -70, 106710, 0)
    ChrSetPos(0x00F7, 11930, -70, 106190, 0)
    ChrSetPos(0x00F8, 13420, -30, 106960, 135)
    ChrSetPos(0x00F9, 13630, -30, 108710, 135)
    ChrTurnDirection(0x00F8, 0x0008, 0)
    ChrTurnDirection(0x00F9, 0x0008, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    CameraMove(12660, -40, 109960, 0)
    OP_67(0, 5920, -10000, 0)
    CameraSetDistance(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460161V#1007F#4P又、又一次被\n',
            '吓了一跳呢～',
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
        'loc_2408',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460162V#067F好、好华丽的\n',
            '企鹅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2408(): pass

    label('loc_2408')

    ChrTalk(
        0x0008,
        (
            '#1770460163V呼～呼～\n',
            '我还以为会死在这里呢。',
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
        'loc_24BB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460164V#070F#2P哎呀呀，这次\n',
            '总算是把它们击退了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460165V在第二波袭击到来之前\n',
            '赶快撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0108, 400)

    Jump('loc_25AA')

    def _loc_24BB(): pass

    label('loc_24BB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2538',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460166V#030F#2P呼，总算是把它们击退了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460167V在第二波袭击到来之前\n',
            '赶紧撤退比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0104, 400)

    Jump('loc_25AA')

    def _loc_2538(): pass

    label('loc_2538')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25AA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460168V#040F#2P总算是击退了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460169V在第二波袭击到来之前\n',
            '赶紧撤离比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)

    def _loc_25AA(): pass

    label('loc_25AA')

    ChrTalk(
        0x0008,
        (
            '#1770460170V明、明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460171V那、那我马上\n',
            '回收宝箱里的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirectionByPos(0x0008, 11100, 112530, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2671',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460172V#052F……不，等等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460173V#050F那个就交给我们吧。\n',
            '说不定还有什么机关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26C9')

    def _loc_2671(): pass

    label('loc_2671')

    ChrTalk(
        0x0103,
        (
            '#0030460174V#022F不，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460175V那个就交给我们吧。\n',
            '说不定还有什么机关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26C9(): pass

    label('loc_26C9')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0008, 0x00F7, 400)

    ChrTalk(
        0x0008,
        (
            '#1770460176V确、确实如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460177V#1006F#4P那么我来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_66(0x0000)

    @scena.Lambda('lambda_273E')
    def lambda_273E():
        CameraMove(11140, -50, 111010, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_273E)

    ChrWalkTo(0x0101, 11500, -30, 107780, 2000, 0x00)

    @scena.Lambda('lambda_276A')
    def lambda_276A():
        ChrTurnDirection(0x0008, 0x0101, 400)
        Yield()

        Jump('lambda_276A')

    DispatchAsync2(0x0008, 0x0001, lambda_276A)

    @scena.Lambda('lambda_277B')
    def lambda_277B():
        ChrTurnDirection(0x00F7, 0x0101, 400)
        Yield()

        Jump('lambda_277B')

    DispatchAsync2(0x00F7, 0x0001, lambda_277B)

    @scena.Lambda('lambda_278C')
    def lambda_278C():
        ChrTurnDirection(0x00F8, 0x0101, 400)
        Yield()

        Jump('lambda_278C')

    DispatchAsync2(0x00F8, 0x0001, lambda_278C)

    @scena.Lambda('lambda_279D')
    def lambda_279D():
        ChrTurnDirection(0x00F9, 0x0101, 400)
        Yield()

        Jump('lambda_279D')

    DispatchAsync2(0x00F9, 0x0001, lambda_279D)

    ChrWalkTo(0x0101, 11110, -40, 111660, 2000, 0x00)
    ChrSetDirection(0x0101, 0, 400)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    WaitForThreadExit(0x0008, 0x0000)
    OP_66(0x0001)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010460178V#1015F嗯……\n',
            '没什么特别可疑的地方了',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460179V这样应该没问题了……',
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
            (TxtCtl.SetColor, 0x2),
            '#16I银露宝珠',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010460180V#1018F好，回收完成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460181V#1004F……咦？这！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460182V怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460183V#1002F嗯、嗯。\n',
            '箱子里有张纸条哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460184V……好像是一封信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Fade(500)
    ChrSetChipByIndex(0x0101, 23)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010460185V#1011F嗯……我看看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '为了纪念我７０岁生日\n',
            '以及海盗生涯的结束，\n',
            '把我的『银露宝珠』藏在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这『宝珠』可以告知所有者\n',
            '各种危机的来临。\n',
            '我能活到今天\n',
            '全仰赖于这件宝物的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '但是，我也上年纪了。\n',
            '现在对那些追寻它的\n',
            '『骑士』们感到很头痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '所以让它沉入湖底。\n',
            '发现它的人可以随意处置。\n',
            '不过，就像我刚才所写的那样，\n',
            '它是一件会让你感到很辛苦的宝物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '……海盗希尔玛记于此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460186V#1002F…………没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 11110, -50, 110620, 6000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0008, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0008, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0008, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0008, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0008, 0x00B4, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0008, 0x0000, 0x000000C8, 0x00001B58, 0x00)
    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x00001B58, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1770460187V#3P哇～～！\n',
            '让、让我看看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460188V#1016F知、知道了，\n',
            '不用那么着急啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460189V而且，现在必须先\n',
            '返回蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2D2E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460190V#053F如果你还想和那个\n',
            '古怪的怪物战斗的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6C')

    def _loc_2D2E(): pass

    label('loc_2D2E')

    ChrTalk(
        0x0103,
        (
            '#0030460191V#027F如果你还想和那个\n',
            '古怪的怪物战斗的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D6C(): pass

    label('loc_2D6C')

    @scena.Lambda('lambda_2D72')
    def lambda_2D72():
        ChrSetDirection(0x0008, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D72)

    Sleep(250)

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#1770460192V#3P不、不不，\n',
            '就饶了我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1770460193V#3P既然如此就\n',
            '赶快回去吧。',
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
        'loc_2E32',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460194V#070F嗯，这么做比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460195V那就快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE1')

    def _loc_2E32(): pass

    label('loc_2E32')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E88',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460196V#030F这个决定十分明智。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460197V呼，那么走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE1')

    def _loc_2E88(): pass

    label('loc_2E88')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EE1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460198V#040F嗯，这个决定十分明智。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460199V那么，我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EE1(): pass

    label('loc_2EE1')

    ChrTalk(
        0x0101,
        (
            '#0010460200V#1006F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x2F1B
@scena.Code('func_10_2F1B')
def func_10_2F1B():
    OP_24(0x00AC, 0x5A)
    Sleep(100)

    OP_24(0x00AC, 0x50)
    Sleep(100)

    OP_24(0x00AC, 0x46)
    Sleep(100)

    OP_24(0x00AC, 0x3C)
    Sleep(100)

    OP_24(0x00AC, 0x32)
    Sleep(100)

    OP_24(0x00AC, 0x28)
    Sleep(100)

    OP_24(0x00AC, 0x1E)
    Sleep(100)

    OP_24(0x00AC, 0x14)
    Sleep(100)

    OP_24(0x00AC, 0x0A)
    Sleep(100)

    OP_23(0x00AC)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
