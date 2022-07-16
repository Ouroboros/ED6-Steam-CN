import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0120_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0120_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0120.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x17A2
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
    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_258',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DB',
    )

    ChrTalk(
        0x0008,
        (
            '#0840150383V哟，这不是\n',
            '近来很活跃的两位游击士新人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150384V最近到处都能听到\n',
            '你们努力工作的事迹哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150385V#006F是吗，不过我们还只是新手啦。\n',
            '还需要拼命加油呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150386V哈哈，有前途啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150387V不过你们来得\n',
            '还真是时候，\n',
            '我有急事要拜托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150388V在米尔西街道上的\n',
            '导力灯需要找人去更换，\n',
            '怎么样，你们愿意接受这工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0001)

    Jump('loc_255')

    def _loc_1DB(): pass

    label('loc_1DB')

    @scena.Lambda('lambda_01E1')
    def lambda_01E1():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_01E1)

    ChrTurnDirection(0x0001, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0840150389V哟，\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150390V更换导力灯的工作\n',
            '你们要接受吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_251',
    )

    Call(1, 0x0002)

    Jump('loc_255')

    def _loc_251(): pass

    label('loc_251')

    Call(1, 0x0001)

    def _loc_255(): pass

    label('loc_255')

    Jump('loc_57B')

    def _loc_258(): pass

    label('loc_258')

    ChrTalk(
        0x0008,
        (
            '#0840150391V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_578',
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
        10,
        0,
        (
            TXT(0x00, '【确认路灯的解锁密码】\n'),
            TXT(0x01, '【取消委托任务】\n'),
            TXT(0x02, '【没什么事】\n'),
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
        (0x00000000, 'loc_2FC'),
        (0x00000001, 'loc_3DE'),
        (0x00000002, 'loc_546'),
        (-1, 'loc_546'),
    )

    def _loc_2FC(): pass

    label('loc_2FC')

    ChrTalk(
        0x0008,
        (
            '#0840150392V需要交换的是城西\n',
            '米尔西街道的第六号路灯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150393V是从靠洛连特这边街道\n',
            '开始数的第六个路灯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150394V控电盘的解锁密码是\n',
            '『５４４８１８』。\n',
            '……不要忘记了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150395V那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_575')

    def _loc_3DE(): pass

    label('loc_3DE')

    OP_28(0x0006, 0x03, 0x08)
    OP_28(0x0006, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010150396V#003F实在是对不起，佛莱迪叔叔，\n',
            '我们突然有很急的事情要办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150397V是这样啊。\n',
            '那就没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150398V既然如此，那就把用于\n',
            '更换的导力灯还给我好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '导力灯',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0327, 1)
    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0840150399V办完事情后，\n',
            '请马上通知我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150400V我这边的事情也很急啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_575')

    def _loc_546(): pass

    label('loc_546')

    ChrTalk(
        0x0008,
        (
            '#0840150395V那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_575')

    def _loc_575(): pass

    label('loc_575')

    Jump('loc_271')

    def _loc_578(): pass

    label('loc_578')

    OP_5F(0x0000)
    def _loc_57B(): pass

    label('loc_57B')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x586
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E46',
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
        10,
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
        (0x00000000, 'loc_5EA'),
        (0x00000001, 'loc_D78'),
        (-1, 'loc_D78'),
    )

    def _loc_5EA(): pass

    label('loc_5EA')

    OP_28(0x0006, 0x04, 0x08)
    OP_28(0x0006, 0x04, 0x04)
    OP_28(0x0006, 0x04, 0x02)
    OP_28(0x0006, 0x01, 0x0001)
    OP_28(0x0006, 0x01, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010150402V#006F嗯，就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150403V#010F很高兴您能\n',
            '把这个任务交给我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150404V谢谢了，真是帮大忙了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150405V差点忘了说，\n',
            '今天就是任务的最后期限哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150406V那么，\n',
            '先把这个重要的东西交给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '导力灯',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0327, 1)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010150407V#000F这就是用作更换的导力灯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150408V啊，对呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150392V需要交换的是城西\n',
            '米尔西街道的第六号路灯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150393V是从靠洛连特这边街道\n',
            '开始数的第六个路灯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150411V不要弄错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150412V#000F嗯，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150413V城西米尔西街道，\n',
            '从洛连特方向开始数的第六个路灯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150414V找到那个路灯后，\n',
            '就把灯上配备的控电盘打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150415V控电盘打开后，\n',
            '还需要输入六位数的解锁密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150416V#004F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150417V是啊，六号路灯的密码是\n',
            '『５４４８１８』哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150418V#008F对，对不起佛莱迪叔叔。\n',
            '再说一遍好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150419V#010F『５４４８１８』对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150420V完全一致，\n',
            '不愧是约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150421V#009F哼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0840150422V输入数字之后控电盘就能打开了，\n',
            '之后更换掉里面的导力器就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150423V可能你们觉得这很简单，\n',
            '但是千万不能太大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150424V路灯有可能\n',
            '很早之前就已经坏掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150425V#010F原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150426V#010F导力灯发出的光，\n',
            '具有能驱赶\n',
            '大型魔兽的效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0840150427V不过也只能达到\n',
            '让人稍感安心的程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150428V因此，如果坏掉了，\n',
            '说不定会发生什么意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150429V把这件事委托给\n',
            '游击士去解决，\n',
            '是基于以防万一的考虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150430V说起来路灯就是设置在\n',
            '魔兽频繁出现的道路旁啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150431V#505F哎呀，魔兽来的话，\n',
            '我啪啪几下就收拾得干干净净了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150432V那个密码什么的不用纸记下来\n',
            '倒是很容易忘记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150433V#010F这样的话，\n',
            '输入密码的工作可以交给我来办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0840150434V具体分工就由你们自己决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150435V好了，我已经把相关的注意事项都说明了，\n',
            '那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150436V如果还有什么需要确认的，\n',
            '或者想取消任务，\n',
            '就再到这里来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_E40')

    def _loc_D78(): pass

    label('loc_D78')

    OP_28(0x0006, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010150437V#505F抱歉啊，佛莱迪叔叔，\n',
            '我们还有其他事情要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150397V是这样啊。\n',
            '那就没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150399V办完事情后，\n',
            '请马上通知我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150400V我这边的事情也很急啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_E40')

    def _loc_E40(): pass

    label('loc_E40')

    OP_5F(0x0000)

    Jump('Init')

    def _loc_E46(): pass

    label('loc_E46')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0xE51
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11C8',
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
        10,
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
        (0x00000000, 'loc_EB5'),
        (0x00000001, 'loc_10F7'),
        (-1, 'loc_10F7'),
    )

    def _loc_EB5(): pass

    label('loc_EB5')

    OP_28(0x0006, 0x04, 0x08)

    ChrTalk(
        0x0101,
        (
            '#0010150441V#006F嗯，刚才的事情已经办完了，\n',
            '这件工作就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150442V我再次说明一下，\n',
            '先把这个交给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '导力灯',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0327, 1)
    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0840150443V再次确认这次任务的要点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150392V需要交换的是城西\n',
            '米尔西街道的第六号路灯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150393V是从靠洛连特这边街道\n',
            '开始数的第六个路灯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150446V控电盘的解锁密码是\n',
            '『５４４８１８』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150447V……嗯，基本上就这么多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150448V好了，那么\n',
            '接下来就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150449V如果还有什么需要确认的，\n',
            '或者想取消任务，\n',
            '就再到这里来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_11C5')

    def _loc_10F7(): pass

    label('loc_10F7')

    OP_28(0x0006, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010150450V#003F实在是对不起，佛莱迪叔叔，\n',
            '我们还有一些事情要办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150397V是这样啊。\n',
            '那就没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150399V办完事情后，\n',
            '请马上通知我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150400V我这边的事情也很急啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_11C5')

    def _loc_11C5(): pass

    label('loc_11C5')

    Jump('ReInit')

    def _loc_11C8(): pass

    label('loc_11C8')

    OP_5F(0x0000)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0003 offset: 0x11D6
@scena.Code('func_03_11D6')
def func_03_11D6():
    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0006, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11EC',
    )

    Jump('loc_1210')

    def _loc_11EC(): pass

    label('loc_11EC')

    ChrTalk(
        0x0008,
        (
            '看到这句话就表示有Ｂｕｇ发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1210(): pass

    label('loc_1210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1727',
    )

    EventBegin(0x00)
    OP_28(0x0006, 0x04, 0x10)
    OP_28(0x0006, 0x01, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010150586V#001F呀嗬～佛莱迪叔叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150587V哟，是艾丝蒂尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150588V从你的表情来看，\n',
            '事情已经顺利完成了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010150589V#006F嗯⊙\n',
            '还算顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150590V……虽然还是发生了一些小事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150591V#010F为了慎重起见，\n',
            '先向佛莱迪先生汇报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '米尔西街道的事件汇报完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0840150592V哦……果然是出故障了啊。\n',
            '一定是因为更换日期太迟了的缘故。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150593V实在是抱歉。\n',
            '因为我的疏忽让你们遇到了危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150594V#000F没关系的，\n',
            '不用道歉啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150595V#000F这是我们份内的事情嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150596V#010F工作中的危险\n',
            '也是我们游击士应该承担的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150597V谢谢啊。\n',
            '有你这句话我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0840150598V……对了，请收下这个，\n',
            '以表我的歉意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '收下了',
            (TxtCtl.SetColor, 0x2),
            '妨碍２',
            (TxtCtl.SetColor, 0x0),
            '的结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x02C2, 1)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010150599V#004F这是，结晶回路？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150600V没错，妨碍２的结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150601V它可以在对方\n',
            '准备发出魔法时中止其发动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150602V如果能熟练使用的话，\n',
            '这东西可是很有用的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150603V#001F嗯，非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150604V#010F劳您费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0840150605V哪里哪里，是我感谢你们两个才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150606V有什么关于导力器的问题的话\n',
            '就随时找我来谈好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150607V以后我们工房的生意\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【更换路灯】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x01)

    Jump('loc_1799')

    def _loc_1727(): pass

    label('loc_1727')

    ChrTalk(
        0x0008,
        (
            '#0840150606V有什么关于导力器的问题的话\n',
            '就随时找我来谈好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840150607V以后我们工房的生意\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1799(): pass

    label('loc_1799')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
