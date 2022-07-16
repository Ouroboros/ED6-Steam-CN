import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3104   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3104.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x189D
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
        ('ED6_DT06/CH20141._CH', 'ED6_DT06/CH20141P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xB2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xB2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xB2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xB2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_C5',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_C5(): pass

    label('loc_C5')

    Return()

# id: 0x0001 offset: 0xC6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B9, 6, 0x5CE)),
            (Expr.TestScenaFlags, ScenaFlag(0x00B9, 7, 0x5CF)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_E3')

    def _loc_DE(): pass

    label('loc_DE')

    PlaySE(461, 0x01, 0x64)

    def _loc_E3(): pass

    label('loc_E3')

    Return()

# id: 0x0002 offset: 0xE4
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x10000000)
    FormationAddMember(0x05, 0xFF)
    FormationAddMember(0x06, 0xFF)
    FormationAddMember(0x0A, 0xFF)
    EventBegin(0x00)
    OP_66(0x0000)
    CameraMove(3160, 0, 9050, 0)
    OP_67(-16400, 26840, -56180, 0)
    CameraSetDistance(1000, 0)
    OP_6C(16000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 24790, 110, -35590, 270)
    SetChrPos(0x0102, 25200, 30, -36550, 270)
    SetChrPos(0x0106, 22990, 20, -36670, 90)
    SetChrPos(0x010B, 23610, 10, -37570, 45)
    SetChrPos(0x0107, 23250, 30, -35430, 90)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0198')
    def lambda_0198():
        CameraMove(24300, 60, -35590, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0198)

    Sleep(4000)

    @scena.Lambda('lambda_01B5')
    def lambda_01B5():
        OP_67(-16400, 37480, -56180, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_01B5)

    @scena.Lambda('lambda_01CD')
    def lambda_01CD():
        CameraSetDistance(800, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_01CD)

    Sleep(4000)

    Fade(1000)
    TerminateThread(0x0101, 0xFF)
    OP_66(0x0001)
    CameraMove(24380, 30, -36240, 0)
    OP_67(0, 37430, -45510, 0)
    CameraSetDistance(600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010091375V#002F呼……\n',
            '总算逃出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091376V看来还没有搜查到这边来呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091377V#010F希德少校刚才下令搜查\n',
            '也是为了故意牵制他们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091378V#013F不过再磨磨蹭蹭的话，\n',
            '追踪部队恐怕就要追来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091379V得先带博士逃到安全的地方……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091380V#102F………唔……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091381V#063F#3P姐姐、哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091382V#006F啊，不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091383V我们一定会\n',
            '保护好提妲和博士的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0106)

    ChrTalk(
        0x0106,
        (
            '#0050091384V#050F……不。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091385V你们俩在这里撤手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091386V#580F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091387V#012F什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091388V#053F经过这次的事件，\n',
            '我已经完全被情报部的那帮家伙盯上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091389V而且老爷子和提妲\n',
            '也同样会被他们追踪下去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091390V#051F我带他们两个逃走，\n',
            '你们也赶快逃去安全的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070091391V#064F阿加特大哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091392V#102F原来如此，变成这样了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091393V的确有道理，\n',
            '不能再让你们卷入这件事里了，\n',
            '总之和我们在一起的人越少越好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091394V#104F可以的话，\n',
            '我也不想把提妲卷进来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091395V但考虑到她可能会被抓作人质，\n',
            '还不如让她和我一起比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x010B, 400)

    ChrTalk(
        0x0107,
        (
            '#0070091396V#560F爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091397V#005F等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091398V只有我们安全逃走，\n',
            '这种做法我绝对接受不了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091399V约修亚也这么想吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06C8')
    def lambda_06C8():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_06C8)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091400V#013F不……\n',
            '阿加特兄说得很正确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091401V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091402V#012F从逃亡还有潜伏的角度来说，\n',
            '一起行动的人越多，\n',
            '隐蔽起来就越困难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091403V所以由阿加特兄单独\n',
            '带博士他们一起逃比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091404V#015F你的心情我很理解……\n',
            '但这次还是听阿加特兄的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091405V#580F怎、怎么这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091406V#053F不错嘛，约修亚，\n',
            '任何时候都这么明白事理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091407V#050F艾丝蒂尔。\n',
            '就在这里坦率地分手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091408V#003F但、但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091409V虽然道理我也明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091410V#063F#3P艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091411V#104F嗯……\n',
            '看来还是一副难以接受的样子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091412V#100F这样吧……\n',
            '你们能不能代我完成一项工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0944')
    def lambda_0944():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0944)

    @scena.Lambda('lambda_0952')
    def lambda_0952():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0952)

    @scena.Lambda('lambda_0960')
    def lambda_0960():
        ChrTurnDirection(0x00FE, 0x010B, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0960)

    ChrTurnDirection(0x0102, 0x010B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091413V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091414V#102F首先，希望你们能前往王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091415V到了王都之后，\n',
            '去见格兰赛尔城的艾莉茜雅陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010091416V#005F和女王陛下见面？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091417V#014F此话怎讲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091418V#102F那个『黑色导力器』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091419V原本是理查德上校不知从哪里得到的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091420V#104F他把『黑色导力器』叫做『福音』。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091421V#012F『福音』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091422V#053F嘁……\n',
            '很华丽的名字嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091423V#104F这个『福音』之前好像\n',
            '被某人偷偷地从情报部取了出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091424V然后又被做成包裹寄给了卡西乌斯。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091425V然而，之前的那个导力停止事件\n',
            '让情报部知道了导力器的所在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091426V#102F那些黑衣人『特务兵』\n',
            '袭击中央工房的真正原因，\n',
            '既不是我，也不是演算导力器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091427V他们只是为了回收那东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091428V#002F是、是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091429V#012F原来如此……\n',
            '这样一来，很多事就说得通了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091430V#102F理查德上校很有可能\n',
            '想利用那东西在王都做些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091431V如果我猜得没错……\n',
            '应该会发生非常糟糕的事态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091432V希望你们把这件事传达给女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091433V#505F非常糟糕的事态……\n',
            '是指那个导力停止现象吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091434V#104F不……\n',
            '恐怕利用那个是为了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091435V#102F抱歉。\n',
            '我只能言尽于此了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091436V总之，我希望你们能早日\n',
            '把那个『福音』的事禀告陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091437V作为逃亡中的我的代理人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091438V#007F唉……真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091439V#006F听了这么一番话，\n',
            '我们想拒绝都拒绝不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091440V#010F如果博士您没问题的话，\n',
            '我们很乐意接受这个神圣的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091441V#101F抱歉，那就拜托你们俩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F0F')
    def lambda_0F0F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0F0F)

    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070091442V#063F#3P那、那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091443V艾丝蒂尔姐姐。\n',
            '……约修亚哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F6D')
    def lambda_0F6D():
        SetChrDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0F6D)

    @scena.Lambda('lambda_0F7B')
    def lambda_0F7B():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F7B)

    ChrTurnDirection(0x0102, 0x0107, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091444V#010F提妲……\n',
            '我们要暂时分别了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091445V#003F不好意思……\n',
            '之后我们不能陪你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091446V#065F#3P没、没有的事……\n',
            '你们根本不用和我道歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091447V#562F我一直都受姐姐你们的照顾……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091448V对我那么的好、那么的亲切，\n',
            '对我简直就像妹妹一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091449V#069F……呜呜……呜哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091450V#004F提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_10E3')
    def lambda_10E3():
        CameraMove(25380, 30, -36240, 1000)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_10E3)

    @scena.Lambda('lambda_10FB')
    def lambda_10FB():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_10FB')

    DispatchAsync2(0x0101, 0x0001, lambda_10FB)

    @scena.Lambda('lambda_110C')
    def lambda_110C():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_110C')

    DispatchAsync2(0x0102, 0x0001, lambda_110C)

    @scena.Lambda('lambda_111D')
    def lambda_111D():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_111D')

    DispatchAsync2(0x0106, 0x0001, lambda_111D)

    @scena.Lambda('lambda_112E')
    def lambda_112E():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_112E')

    DispatchAsync2(0x010B, 0x0001, lambda_112E)

    OP_92(0x0107, 0x0101, 400, 5000, 0x00)

    @scena.Lambda('lambda_114D')
    def lambda_114D():
        OP_94(0x01, 0x0107, 0x0000, 0x0000012C, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_114D)

    Yield()
    SetChrDirection(0x0107, 0, 0)
    SetChrChipByIndex(0x0107, 0)
    SetChrSubChip(0x0107, 1)
    SetChrFlags(0x0107, 0x0020)
    SetChrFlags(0x0107, 0x0040)
    SetChrDirection(0x0101, 292, 0)
    OP_94(0x01, 0x0101, 0x00B4, 0x0000012C, 0x000007D0, 0x00)
    WaitForThreadExit(0x0107, 0x0003)

    ChrTalk(
        0x0107,
        (
            '#0070091451V#069F#3P谢、谢谢你们救了爷爷……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091452V呜……还有……\n',
            '谢谢你们对我那么好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091453V#067F……我最喜欢……你们俩了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091454V#008F嗯……\n',
            '我也最喜欢你了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091455V#019F#2P和你在一起我们也很开心……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091456V我们也要谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091457V#053F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091458V#050F虽然依依不舍，\n',
            '但还是就到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091459V眼泪留到再会那一刻再流吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091460V#007F呜……真是……\n',
            '你这没血没泪的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x010B, 0xFF)
    ClearChrFlags(0x0107, 0x0020)
    SetChrChipByIndex(0x0107, 65535)
    ChrTurnDirection(0x0107, 0x0101, 0)
    OP_94(0x01, 0x0107, 0x00B4, 0x00000258, 0x000007D0, 0x00)

    @scena.Lambda('lambda_137A')
    def lambda_137A():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_137A)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091461V#501F不过……\n',
            '我们也要和你暂别一段时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091462V虽然发生了很多事，\n',
            '但和你一起工作得到了很多经验。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091463V谢谢了，阿加特前辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091464V#055F哎呀……\n',
            '不要叫得那么肉麻啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091465V#001F啊哈哈，害羞了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091466V#551F真是的……\n',
            '不愧是大叔的女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091467V#051F约修亚，\n',
            '注意看好这个冲动的家伙哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091468V除了武术可以独当一面之外，\n',
            '其他方面都是让人放心不下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091469V#009F哼，要你多管闲事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091470V#019F#2P哈哈，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091471V#010F阿加特兄也要多加小心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091472V博士和提妲就拜托你了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091473V#051F啊啊，交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091474V那么……\n',
            '我们先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091475V#101F再见了！\n',
            '卡西乌斯的孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091476V#069F保、保重啊！\n',
            '艾丝蒂尔姐姐、约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091477V#006F嗯！提妲你们也是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091478V#010F#2P愿女神保佑你们！\n',
            '请各位务必小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1699')
    def lambda_1699():
        CameraMove(21340, 70, -35800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1699)

    SetChrDirection(0x0106, 315, 400)

    @scena.Lambda('lambda_16B8')
    def lambda_16B8():
        ChrWalkTo(0x00FE, 10360, 80, -33360, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_16B8)

    SetChrDirection(0x0107, 270, 400)

    @scena.Lambda('lambda_16DA')
    def lambda_16DA():
        ChrWalkTo(0x00FE, 10220, 90, -34260, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_16DA)

    Sleep(400)

    SetChrDirection(0x010B, 315, 400)

    @scena.Lambda('lambda_1701')
    def lambda_1701():
        ChrWalkTo(0x00FE, 10360, 80, -33360, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_1701)

    SetChrDirection(0x0101, 270, 400)
    Sleep(2000)

    OP_20(0x000009C4)
    FadeOut(2000, 0, -1)
    OP_24(0x01CD, 0x5A)
    Sleep(200)

    OP_24(0x01CD, 0x50)
    Sleep(200)

    OP_24(0x01CD, 0x46)
    Sleep(200)

    OP_24(0x01CD, 0x3C)
    Sleep(200)

    OP_24(0x01CD, 0x32)
    Sleep(200)

    OP_24(0x01CD, 0x28)
    Sleep(200)

    OP_24(0x01CD, 0x1E)
    Sleep(200)

    OP_24(0x01CD, 0x14)
    Sleep(200)

    OP_24(0x01CD, 0x0A)
    Sleep(200)

    OP_24(0x01CD, 0x00)
    OP_0D()
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS048._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    WaitEffect(0x14, 0x00)
    SetScenaFlags(ScenaFlag(0x00B9, 6, 0x5CE))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xF3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

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
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_180B',
    )

    ShowSaveMenu()

    def _loc_180B(): pass

    label('loc_180B')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x00AE, 1, 0x571))
    SetScenaFlags(ScenaFlag(0x00A6, 3, 0x533))
    SetScenaFlags(ScenaFlag(0x00B9, 7, 0x5CF))
    OP_B8(0x06)
    OP_B8(0x05)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x0A, 0xFF)
    OP_28(0x0054, 0x04, 0x02)
    OP_28(0x0054, 0x04, 0x04)

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_1856',
    )

    Jump('loc_1881')

    def _loc_1856(): pass

    label('loc_1856')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_1869',
    )

    OP_2B(0x0043, 0x0001)

    Jump('loc_1881')

    def _loc_1869(): pass

    label('loc_1869')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_187C',
    )

    OP_2B(0x0043, 0x0002)

    Jump('loc_1881')

    def _loc_187C(): pass

    label('loc_187C')

    OP_2B(0x0043, 0x0003)

    def _loc_1881(): pass

    label('loc_1881')

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/R4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x188E
@scena.Code('func_03_188E')
def func_03_188E():
    Return()

# id: 0x0004 offset: 0x188F
@scena.Code('func_04_188F')
def func_04_188F():
    Return()

# id: 0x0005 offset: 0x1890
@scena.Code('func_05_1890')
def func_05_1890():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
