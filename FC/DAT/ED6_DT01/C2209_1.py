import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2209_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2209_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C2200.x'
    header.mapIndex       = 84
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_96',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    Call(1, 0x0001)

    Jump('loc_93')

    def _loc_8C(): pass

    label('loc_8C')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    Call(1, 0x0002)

    def _loc_93(): pass

    label('loc_93')

    Jump('loc_9A')

    def _loc_96(): pass

    label('loc_96')

    Call(1, 0x0004)
    def _loc_9A(): pass

    label('loc_9A')

    Return()

# id: 0x0001 offset: 0x9B
@scena.Code('func_01_9B')
def func_01_9B():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x40)"),
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_AD',
    )

    Return()

    def _loc_AD(): pass

    label('loc_AD')

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B91',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_D1',
    )

    Call(1, 0x0002)

    Jump('loc_B91')

    def _loc_D1(): pass

    label('loc_D1')

    ChrSetFlags(0x0008, 0x0010)
    TalkBegin(0x0008)
    EventBegin(0x00)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0009,
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
        0x0009,
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
        0x0009,
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

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B4B',
    )

    OP_28(0x001C, 0x04, 0x02)
    OP_28(0x001C, 0x04, 0x04)
    OP_28(0x001C, 0x01, 0x0001)
    OP_28(0x001C, 0x01, 0x0002)
    OP_69(0x0009, 2000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F0',
    )

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1730160001V…………唉，\n',
            '接下来应该怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160002V如果去叫人帮忙的话，\n',
            '灯塔不就没人看守了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160003V这么说只有在这里等着了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F0(): pass

    label('loc_1F0')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160004V……哦，你们是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160005V到巴伦诺灯塔来有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160006V#000F没有啊，\n',
            '并没有什么特别的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160007V倒是老爷爷您，\n',
            '在这里做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160008V我是这里的管理员，\n',
            '也就是看守灯塔的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160009V这个大型的灯塔\n',
            '管理起来是很费力的…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_437',
    )

    ChrTalk(
        0x0008,
        (
            '#1730160010V…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160011V#501F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160012V哎呀，你们俩，\n',
            '胸前的徽章是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160013V#508F啊，没错，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160014V我们是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160015V#010F准确地说\n',
            '现在还只是准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_55D')

    def _loc_437(): pass

    label('loc_437')

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160016V…………哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160017V喂，年轻人。\n',
            '你们胸前的徽章是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160018V#007F呜…………\n',
            '徽、徽章…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160019V#017F（真是的……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160020V#010F嗯，是啊。\n',
            '我们是游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160021V准确地说\n',
            '现在还只是准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_55D(): pass

    label('loc_55D')

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160022V啊，\n',
            '为什么不早说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160023V难道你们对一位老人\n',
            '陷入如此的困境视而不见吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160024V#004F啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160025V困难什么的\n',
            '您刚才一个字也没有提到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160026V那是因为\n',
            '你们刚才没有问过我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160027V『您有什么困难吗？』\n',
            '你们为什么不这样问问？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160028V真是的…………\n',
            '年轻的游击士就只有力气，\n',
            '一点观察能力都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1730160029V…………对了。\n',
            '在这一点上，那个壮年的游击士\n',
            '就表现得完全不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160030V那是……嗯，\n',
            '大概七八年前的事情吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160031V#509F喂喂，老爷爷？\n',
            '您的困难究竟是什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160032V…………嗯？\n',
            '啊，对了对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160033V是这样的，刚才我去割草的时候，\n',
            '不小心忘了关门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160034V一群魔兽\n',
            '就趁机冲入了灯塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160035V这样一来\n',
            '我也没有办法进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160036V#006F就是说，\n',
            '只要把里面的魔兽全部消灭就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160037V嗯，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160038V不过我不知道里面究竟有多少只。\n',
            '你们千万要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160039V#505F嗯……不过魔兽\n',
            '为什么要跑到灯塔里面去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_9BA',
    )

    ChrTurnDirection(0x0105, 0x0102, 400)

    Jump('loc_9CE')

    def _loc_9BA(): pass

    label('loc_9BA')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_9CE',
    )

    ChrTurnDirection(0x0136, 0x0102, 400)

    def _loc_9CE(): pass

    label('loc_9CE')

    ChrTalk(
        0x0102,
        (
            '#0020160040V#010F我想可能是受到了七耀石吸引的缘故吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160041V因为灯塔使用的是\n',
            '特大号的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160042V嗯，说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_A87',
    )

    ChrTurnDirection(0x0105, 0x0008, 400)

    Jump('loc_A9B')

    def _loc_A87(): pass

    label('loc_A87')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_A9B',
    )

    ChrTurnDirection(0x0136, 0x0008, 400)

    def _loc_A9B(): pass

    label('loc_A9B')

    ChrTalk(
        0x0008,
        (
            '#1730160043V以前被侵入的时候，\n',
            '那些魔兽都是集中在\n',
            '灯塔的最上层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160044V#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160045V那么，\n',
            '现在就可以进去消灭魔兽吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)

    Jump('loc_B8E')

    def _loc_B4B(): pass

    label('loc_B4B')

    OP_69(0x0009, 1000)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160046V怎么样，\n',
            '可以进去消灭魔兽了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)
    def _loc_B8E(): pass

    label('loc_B8E')

    TalkEnd(0x0008)

    def _loc_B91(): pass

    label('loc_B91')

    Return()

# id: 0x0002 offset: 0xB92
@scena.Code('func_02_B92')
def func_02_B92():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1621',
    )

    ChrSetFlags(0x0008, 0x0010)
    TalkBegin(0x0008)
    EventBegin(0x00)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0009,
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
        0x0009,
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
        0x0009,
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

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15D8',
    )

    OP_28(0x001C, 0x04, 0x02)
    OP_28(0x001C, 0x04, 0x04)
    OP_28(0x001C, 0x01, 0x0001)
    OP_28(0x001C, 0x01, 0x0002)
    OP_28(0x001C, 0x01, 0x0004)
    OP_28(0x001D, 0x01, 0x0008)
    OP_28(0x001D, 0x01, 0x1000)
    OP_69(0x0009, 2000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CCE',
    )

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1730160001V…………唉，\n',
            '接下来应该怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160002V如果去叫人帮忙的话，\n',
            '灯塔不就没人看守了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160003V这么说只有在这里等着了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCE(): pass

    label('loc_CCE')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160004V……哦，你们是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160005V到巴伦诺灯塔来有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160052V#000F请问一下，\n',
            '您是看守灯塔的弗科特爷爷吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160053V嗯？\n',
            '正是本人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160012V哎呀，你们俩，\n',
            '胸前的徽章是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160013V#508F啊，没错，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160014V我们是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160015V#010F准确地说\n',
            '现在还只是准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160022V啊，\n',
            '为什么不早说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160023V难道你们对一位老人\n',
            '陷入如此的困境视而不见吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160024V#004F啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160025V困难什么的\n',
            '您刚才一个字也没有提到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160026V那是因为\n',
            '你们刚才没有问过我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160027V『您有什么困难吗？』\n',
            '你们为什么不这样问问？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160028V真是的…………\n',
            '年轻的游击士就只有力气，\n',
            '一点观察能力都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1730160029V…………对了。\n',
            '在这一点上，那个壮年的游击士\n',
            '就表现得完全不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160066V那是……嗯，\n',
            '大概七八年前的事情吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160031V#509F喂喂，老爷爷？\n',
            '您的困难究竟是什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160068V#045F（呵呵，\n',
            '　果然和工房老板说的一样。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160032V…………嗯？\n',
            '啊，对了对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160033V是这样的，刚才我去割草的时候，\n',
            '不小心忘了关门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160034V一群魔兽\n',
            '就趁机冲入了灯塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160035V这样一来\n',
            '我也没有办法进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160073V#002F……这样啊，\n',
            '在把维修工具箱交给您之前\n',
            '要先消灭魔兽对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160074V#010F也只有这个选择了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160075V什么？\n',
            '维修工具箱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160076V#010F嗯，我们接受了委托\n',
            '从卢安把维修工具箱带给您。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160077V…………不然的话，\n',
            '我们现在就不会在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160078V嗯、嗯嗯。\n',
            '你们说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160079V如果进不了灯塔，\n',
            '就连检查都没法进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160080V#002F您知道里面有多少魔兽吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160081V具体数目我也不太清楚，\n',
            '不过肯定不止一只。\n',
            '你们千万要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160082V#000F知道了。\n',
            '就是说有很多只吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160083V#505F嗯……不过魔兽\n',
            '为什么要跑到灯塔里面去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    @scena.Lambda('lambda_1462')
    def lambda_1462():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1462)

    @scena.Lambda('lambda_1470')
    def lambda_1470():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1470)

    ChrTalk(
        0x0102,
        (
            '#0020160040V#010F我想可能是受到了七耀石吸引的缘故吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160041V因为灯塔使用的是\n',
            '特大号的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160042V嗯，说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_150B')
    def lambda_150B():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_150B)

    @scena.Lambda('lambda_1519')
    def lambda_1519():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1519)

    @scena.Lambda('lambda_1527')
    def lambda_1527():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1527)

    ChrTalk(
        0x0008,
        (
            '#1730160043V以前被侵入的时候，\n',
            '那些魔兽都是集中在\n',
            '灯塔的最上层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160088V#508F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160045V那么，\n',
            '现在就可以进去消灭魔兽吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)

    Jump('loc_161B')

    def _loc_15D8(): pass

    label('loc_15D8')

    OP_69(0x0009, 1000)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160046V怎么样，\n',
            '可以进去消灭魔兽了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)
    def _loc_161B(): pass

    label('loc_161B')

    TalkEnd(0x0008)

    Jump('loc_1621')

    def _loc_1621(): pass

    label('loc_1621')

    Return()

# id: 0x0003 offset: 0x1622
@scena.Code('func_03_1622')
def func_03_1622():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1681'),
        (0x00000001, 'loc_179B'),
        (-1, 'loc_1854'),
    )

    def _loc_1681(): pass

    label('loc_1681')

    OP_28(0x001C, 0x04, 0x08)
    OP_28(0x001C, 0x01, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010160091V#006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160092V就快到定期检查的时间了，\n',
            '所以请尽量快一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160093V那些魔兽很敏捷，\n',
            '注意不要让他们逃掉啊。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160094V#012F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160095V#002F好。\n',
            '那我们就进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_21()
    NewScene('ED6_DT01/C2219._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1854')

    def _loc_179B(): pass

    label('loc_179B')

    ChrTalk(
        0x0101,
        (
            '#0010160096V#505F对不起啊，\n',
            '现在可能还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160097V很快就要到\n',
            '定期检查的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160098V所以请你们\n',
            '尽可能快一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160099V#000F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1854')

    def _loc_1854(): pass

    label('loc_1854')

    EventEnd(0x01)
    TalkEnd(0x0008)
    ChrSetDirection(0x0008, 0, 0)

    Return()

# id: 0x0004 offset: 0x1861
@scena.Code('func_04_1861')
def func_04_1861():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_1CE8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_1A2B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_197F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#1730160113V喂，我说小姑娘你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160114V魔兽消灭得怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160115V#505F唔～\n',
            '还需要一点时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1730160116V是这样吗……\n',
            '你们得抓紧点儿才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160117V如果进不了灯塔，\n',
            '我就无法进行定期检查呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A28')

    def _loc_197F(): pass

    label('loc_197F')

    ChrTalk(
        0x0008,
        (
            '#1730160118V什么？\n',
            '难道说你们还要去别的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160119V我倒是不介意…………\n',
            '不过要早点回来呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160117V如果进不了灯塔，\n',
            '我就无法进行定期检查呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A28(): pass

    label('loc_1A28')

    Jump('loc_1CE5')

    def _loc_1A2B(): pass

    label('loc_1A2B')

    OP_28(0x001D, 0x01, 0x1000)

    ChrTalk(
        0x0008,
        (
            '#1730160121V喂，我说小姑娘你们。   ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160122V嗯…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160123V哦，那个大箱子是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160124V#000F嗯，这是维修工具箱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160125V给老爷爷您检查设备用的。\n',
            '工具都在里面吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160126V哦，果然如此。\n',
            '原来已经到定期检查的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160127V#010F刚好我们接到委托，\n',
            '所以就马上把工具箱送来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160128V……可是眼下这种状况\n',
            '想要进行设备检查也不行啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160078V嗯、嗯嗯。\n',
            '你们说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160130V如果进不了灯塔，\n',
            '想要检查都没办法进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160131V#002F还是先得把魔兽消灭了才行啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1730160132V嗯，速战速决吧。\n',
            '这种下去肯定是没法开工的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160133V那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1CE5(): pass

    label('loc_1CE5')

    Jump('loc_1E77')

    def _loc_1CE8(): pass

    label('loc_1CE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DDF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#1730160113V喂，我说小姑娘你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160114V魔兽消灭得怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160115V#505F唔～\n',
            '还需要一点时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1730160137V唔～这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160138V就快到定期检查的时间了，\n',
            '你们得抓紧点儿才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E77')

    def _loc_1DDF(): pass

    label('loc_1DDF')

    ChrTalk(
        0x0008,
        (
            '#1730160118V什么？\n',
            '难道说你们还要去别的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160119V我倒是不介意…………\n',
            '不过要早点回来呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160141V定期检查的时间就要到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E77(): pass

    label('loc_1E77')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1E7B
@scena.Code('func_05_1E7B')
def func_05_1E7B():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetDirection(0x0008, 180, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1EA8',
    )

    ChrSetFlags(0x0105, 0x0080)

    Jump('loc_1EBA')

    def _loc_1EA8(): pass

    label('loc_1EA8')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1EBA',
    )

    ChrSetFlags(0x0136, 0x0080)

    def _loc_1EBA(): pass

    label('loc_1EBA')

    ChrSetPos(0x0101, -20, 750, 2830, 0)
    ChrSetPos(0x0102, -20, 750, 2830, 0)
    CameraMove(-20, 750, 830, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1F0E',
    )

    ChrSetPos(0x0105, -20, 750, 2830, 0)

    Jump('loc_1F2C')

    def _loc_1F0E(): pass

    label('loc_1F0E')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1F2C',
    )

    ChrSetPos(0x0136, -20, 750, 2830, 0)

    def _loc_1F2C(): pass

    label('loc_1F2C')

    Sleep(2000)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrSetDirection(0x0008, 0, 400)
    Sleep(1200)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 80)
    OP_73(0x0000)

    @scena.Lambda('lambda_1F66')
    def lambda_1F66():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_1F66')

    DispatchAsync2(0x0008, 0x0001, lambda_1F66)

    CreateThread(0x0009, 0x01, 0x01, 0x0008)
    CreateThread(0x0101, 0x01, 0x01, 0x0009)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x01, 0x000A)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x01, 0x000B)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(1000)

    OP_72(0x0000, 0x0800)
    PlaySE(211, 0x00, 0x64)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#1730160100V哦，还算顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160101V#001F哈哈，已经全部解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160102V#010F魔兽已经被消灭，\n',
            '没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160103V真的吗，太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21D3',
    )

    OP_28(0x001D, 0x01, 0x1000)

    ChrTalk(
        0x0008,
        (
            '#1730160104V哎呀，\n',
            '这下可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160105V#000F呵呵，真的是这样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160106V这下就可以\n',
            '把维修工具箱交给您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160075V什么？\n',
            '维修工具箱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160108V#010F其实我们是接到委托\n',
            '前来把工具箱送给您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160109V哦哦，原来如此啊。\n',
            '已经到定期检查的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220B')

    def _loc_21D3(): pass

    label('loc_21D3')

    ChrTalk(
        0x0008,
        (
            '#1730160110V哎呀，\n',
            '这下终于可以\n',
            '收下维修工具箱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_220B(): pass

    label('loc_220B')

    ChrTalk(
        0x0008,
        (
            '#1730160111V好的，\n',
            '总之我们先进入灯塔里再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160112V#000F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C2219._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x226E
@scena.Code('func_06_226E')
def func_06_226E():
    OP_28(0x001D, 0x04, 0x10)
    OP_28(0x001D, 0x01, 0x0080)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetPos(0x0101, 200, 750, 2830, 0)
    ChrSetPos(0x0102, -500, 750, 2830, 0)
    ChrSetPos(0x0105, 500, 750, 2830, 0)
    Sleep(2000)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 80)
    OP_73(0x0000)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0105, 0x0080)

    @scena.Lambda('lambda_22ED')
    def lambda_22ED():
        ChrMoveToRelative(0x0101, 0, 0, -8500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22ED)

    Sleep(500)

    @scena.Lambda('lambda_230D')
    def lambda_230D():
        ChrMoveToRelative(0x0102, 0, 0, -7500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_230D)

    Sleep(600)

    @scena.Lambda('lambda_232D')
    def lambda_232D():
        ChrMoveToRelative(0x0105, 0, 0, -6500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_232D)

    Sleep(1200)

    OP_72(0x0000, 0x0800)
    PlaySE(211, 0x00, 0x64)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    CameraMove(200, 0, -4800, 3000)
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010160218V#505F………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160219V#002F…………喂，约修亚。\n',
            '对刚才的话你怎么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160182V#010F不用想也可以知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160183V如果是七八年前，\n',
            '在时间上就很吻合了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160184V#040F请问，难道说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160185V刚才老爷爷提起的那位壮年游击士，\n',
            '是你们认识的人吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160186V#505F唔～\n',
            '说认识是理所当然的啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160187V因为那就是我们的老爸嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160188V#044F啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160189V#010F……不过，\n',
            '想要和父亲相比的确很难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160199V#007F呼，真不甘心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160200V如果是拿其他的游击士和我们做对比，\n',
            '那个老爷爷就不会有这种抱怨了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160201V#010F只要我们每天都努力加油，\n',
            '一定可以赶上父亲的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160202V…………不能因为对手太强而灰心丧气哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160203V#506F哈哈哈，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160204V#006F不过我也坚信，\n',
            '总有一天我们可以超越他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160205V#041F呵呵，\n',
            '这样才像艾丝蒂尔嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111570V#001F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160215V就这么决定了。\n',
            '我们绝对不会偷懒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160237V#010F嗯，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160217V那我们出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【扫荡灯塔的魔兽】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【运送维修工具箱】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x2868
@scena.Code('func_07_2868')
def func_07_2868():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetDirection(0x0008, 180, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2895',
    )

    ChrSetFlags(0x0105, 0x0080)

    Jump('loc_28A7')

    def _loc_2895(): pass

    label('loc_2895')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_28A7',
    )

    ChrSetFlags(0x0136, 0x0080)

    def _loc_28A7(): pass

    label('loc_28A7')

    ChrSetPos(0x0101, -20, 750, 2830, 0)
    ChrSetPos(0x0102, -20, 750, 2830, 0)
    CameraMove(-20, 750, 830, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_28FB',
    )

    ChrSetPos(0x0105, -20, 750, 2830, 0)

    Jump('loc_2919')

    def _loc_28FB(): pass

    label('loc_28FB')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2919',
    )

    ChrSetPos(0x0136, -20, 750, 2830, 0)

    def _loc_2919(): pass

    label('loc_2919')

    Sleep(2000)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrSetDirection(0x0008, 0, 400)
    Sleep(1200)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 80)
    OP_73(0x0000)

    @scena.Lambda('lambda_2953')
    def lambda_2953():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_2953')

    DispatchAsync2(0x0008, 0x0001, lambda_2953)

    CreateThread(0x0009, 0x01, 0x01, 0x0008)
    CreateThread(0x0101, 0x01, 0x01, 0x0009)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x01, 0x000A)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2994',
    )

    Sleep(500)

    CreateThread(0x0105, 0x01, 0x01, 0x000B)

    Jump('loc_29AD')

    def _loc_2994(): pass

    label('loc_2994')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_29AD',
    )

    Sleep(500)

    CreateThread(0x0136, 0x01, 0x01, 0x000B)

    def _loc_29AD(): pass

    label('loc_29AD')

    WaitForThreadExit(0x0102, 0x0001)
    Sleep(1000)

    OP_72(0x0000, 0x0800)
    PlaySE(211, 0x00, 0x64)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#1730160100V哦，还算顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160101V#001F哈哈，已经全部解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160102V#010F魔兽已经被消灭，\n',
            '没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160103V真的吗，太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160104V哎呀，\n',
            '这下可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160147V你们也辛苦了。\n',
            '干得不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160148V从今往后也要记得\n',
            '把关心别人放在首位哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160149V#508F嗯，知道了。\n',
            '老爷爷要好好保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160150V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2B80')
    def lambda_2B80():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_2B80')

    DispatchAsync2(0x0008, 0x0001, lambda_2B80)

    ChrSetPos(0x0009, 300, 750, -5000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x01,
        (
            (Expr.GetChrWork, 0x9, 0x1),
            (Expr.GetChrWork, 0x8, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x02,
        (
            (Expr.GetChrWork, 0x9, 0x2),
            (Expr.GetChrWork, 0x8, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x03,
        (
            (Expr.GetChrWork, 0x9, 0x3),
            (Expr.GetChrWork, 0x8, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0009, 0x01, 0x01, 0x000C)
    CreateThread(0x0101, 0x01, 0x01, 0x000D)
    Sleep(300)

    CreateThread(0x0102, 0x01, 0x01, 0x000E)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2C11',
    )

    Sleep(300)

    CreateThread(0x0105, 0x01, 0x01, 0x000F)

    Jump('loc_2C2A')

    def _loc_2C11(): pass

    label('loc_2C11')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2C2A',
    )

    Sleep(300)

    CreateThread(0x0136, 0x01, 0x01, 0x000F)

    def _loc_2C2A(): pass

    label('loc_2C2A')

    ChrTalk(
        0x0008,
        (
            '#1730160151V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#1730160152V……我说你们俩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)

    @scena.Lambda('lambda_2C9E')
    def lambda_2C9E():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C9E)

    @scena.Lambda('lambda_2CAC')
    def lambda_2CAC():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2CAC)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2CD2',
    )

    @scena.Lambda('lambda_2CC7')
    def lambda_2CC7():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2CC7)

    Jump('loc_2CED')

    def _loc_2CD2(): pass

    label('loc_2CD2')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2CED',
    )

    @scena.Lambda('lambda_2CE5')
    def lambda_2CE5():
        ChrTurnDirection(0x0136, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_2CE5)

    def _loc_2CED(): pass

    label('loc_2CED')

    ChrTalk(
        0x0101,
        (
            '#0010160153V#501F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160154V你们没有忘记什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160155V#505F嗯？\n',
            '好像没有忘记什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160156V是不是还应该说\n',
            '『您还有什么别的需要吗？』呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160157V#004F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160158V为什么你们不问一下我\n',
            '『您还有什么别的需要吗？』啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160159V在完成了委托之后，\n',
            '还应该记得问问委托人\n',
            '有没有其他的需要才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2EE5',
    )

    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060160160V#043F（呼，\n',
            '　做游击士也真是辛苦啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F50')

    def _loc_2EE5(): pass

    label('loc_2EE5')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2F4B',
    )

    OP_62(0x0136, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0136,
        (
            '#0060160160V#043F（呼，\n',
            '　做游击士也真是辛苦啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F50')

    def _loc_2F4B(): pass

    label('loc_2F4B')

    Sleep(1000)

    def _loc_2F50(): pass

    label('loc_2F50')

    ChrTalk(
        0x0008,
        (
            '#1730160162V当年那个壮年的游击士\n',
            '离开的时候就这么问过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160163V呼，真是的。\n',
            '你们果然不能与之相提并论呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160164V#009F哼，从刚才开始就啰里啰嗦的～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160165V那个壮年的游击士\n',
            '究竟是什么样的家伙啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160166V听老爷爷您这么说，\n',
            '他好像是个很了不起的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160167V七八年前，我承蒙过他的关照。\n',
            '但是很遗憾，我并不知道他的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160168V他可真是一个了不起的男子汉啊。\n',
            '你们是肯定\n',
            '无法和他相提并论的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160169V如果说\n',
            '他和小姑娘你有相同的地方，\n',
            '那就只有头发的颜色是完全一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160170V那个男人的头发，\n',
            '也是红色中带有一丝茶色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1730160171V……嗯？怎么回事，\n',
            '越看你的眼睛的颜色，\n',
            '越是感觉和他很相似。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160172V#014F……红色的头发，\n',
            '和艾丝蒂尔相同的眼睛颜色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160173V#004F那、那个游击士难道是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_32A3',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160174V#044F？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32D0')

    def _loc_32A3(): pass

    label('loc_32A3')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_32D0',
    )

    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060160174V#044F？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32D0(): pass

    label('loc_32D0')

    ChrTalk(
        0x0008,
        (
            '#1730160176V你们还远远没有\n',
            '达到他那样的水平啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160177V……把理想定得太高，\n',
            '就容易忽视一些细小的方面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_335F',
    )

    ChrTurnDirection(0x0105, 0x0008, 400)

    Jump('loc_3373')

    def _loc_335F(): pass

    label('loc_335F')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3373',
    )

    ChrTurnDirection(0x0136, 0x0008, 400)

    def _loc_3373(): pass

    label('loc_3373')

    ChrTalk(
        0x0008,
        (
            '#1730160178V好了，\n',
            '总之今后你们要好好加油就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160179V那么就这样吧，\n',
            '我要去继续看守灯塔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_33EE')
    def lambda_33EE():
        ChrTurnDirection(0x0101, 0x0008, 0)
        Yield()

        Jump('lambda_33EE')

    DispatchAsync2(0x0101, 0x0001, lambda_33EE)

    @scena.Lambda('lambda_33FF')
    def lambda_33FF():
        ChrTurnDirection(0x0102, 0x0008, 0)
        Yield()

        Jump('lambda_33FF')

    DispatchAsync2(0x0102, 0x0001, lambda_33FF)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_342B',
    )

    @scena.Lambda('lambda_341D')
    def lambda_341D():
        ChrTurnDirection(0x0105, 0x0008, 0)
        Yield()

        Jump('lambda_341D')

    DispatchAsync2(0x0105, 0x0001, lambda_341D)

    Jump('loc_3449')

    def _loc_342B(): pass

    label('loc_342B')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3449',
    )

    @scena.Lambda('lambda_343E')
    def lambda_343E():
        ChrTurnDirection(0x0136, 0x0008, 0)
        Yield()

        Jump('lambda_343E')

    DispatchAsync2(0x0136, 0x0001, lambda_343E)

    def _loc_3449(): pass

    label('loc_3449')

    ChrWalkTo(0x0008, 0, 750, -1170, 2000, 0x00)
    ChrSetDirection(0x0008, 0, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 80)
    OP_73(0x0000)
    ChrWalkTo(0x0008, -20, 750, 2830, 2000, 0x00)
    OP_72(0x0000, 0x0800)
    PlaySE(211, 0x00, 0x64)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_34CA',
    )

    TerminateThread(0x0105, 0xFF)

    Jump('loc_34DB')

    def _loc_34CA(): pass

    label('loc_34CA')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_34DB',
    )

    TerminateThread(0x0136, 0xFF)

    def _loc_34DB(): pass

    label('loc_34DB')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010160180V#002F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160181V……约修亚，你是怎么想的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160182V#010F不用想也可以知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160183V如果是七八年前，\n',
            '在时间上就很吻合了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_36E4',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160184V#040F请问，难道说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160185V刚才老爷爷提起的那位壮年游击士，\n',
            '是你们认识的人吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160186V#505F唔～\n',
            '说认识是理所当然的啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160187V因为那就是我们的老爸嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160188V#044F啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160189V#010F……不过，\n',
            '想要和父亲相比的确很难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38C8')

    def _loc_36E4(): pass

    label('loc_36E4')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_382B',
    )

    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060160184V#040F请问，难道说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160185V刚才老爷爷提起的那位壮年游击士，\n',
            '是你们认识的人吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160186V#505F唔～\n',
            '说认识是理所当然的啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160187V因为那就是我们的老爸嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060160188V#044F啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160189V#010F……不过，\n',
            '想要和父亲相比的确很难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38C8')

    def _loc_382B(): pass

    label('loc_382B')

    ChrTalk(
        0x0101,
        (
            '#0010160196V#004F那么，\n',
            '刚才老爷爷所说的那个游击士\n',
            '果然就是老爸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160197V#010F应该是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160198V……不过，\n',
            '想要和父亲相比的确很难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38C8(): pass

    label('loc_38C8')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160199V#007F呼，真不甘心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160200V如果是拿其他的游击士和我们做对比，\n',
            '那个老爷爷就不会有这种抱怨了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160201V#010F只要我们每天都努力加油，\n',
            '一定可以赶上父亲的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160202V…………不能因为对手太强而灰心丧气哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3ACD',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160203V#506F哈哈哈，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160204V#006F不过我也坚信，\n',
            '总有一天我们可以超越他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160205V#041F呵呵，\n',
            '这样才像艾丝蒂尔嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111570V#001F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160207V#508F就这么决定了。\n',
            '我们绝对不会偷懒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C6D')

    def _loc_3ACD(): pass

    label('loc_3ACD')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3BD9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160203V#506F哈哈哈，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160204V#006F不过我也坚信，\n',
            '总有一天我们可以超越他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060160205V#041F呵呵，\n',
            '这样才像艾丝蒂尔嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111570V#001F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160207V#508F就这么决定了。\n',
            '我们绝对不会偷懒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C6D')

    def _loc_3BD9(): pass

    label('loc_3BD9')

    ChrTalk(
        0x0101,
        (
            '#0010160203V#506F哈哈哈，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160214V#006F不过我也坚信，\n',
            '总有一天我们可以超越他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160215V就这么决定了。\n',
            '我们绝对不会偷懒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C6D(): pass

    label('loc_3C6D')

    ChrTalk(
        0x0102,
        (
            '#0020160216V#010F嗯，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160217V那我们出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【扫荡灯塔的魔兽】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)
    MapClearFlags(0x00400000)

    Return()

# id: 0x0008 offset: 0x3D04
@scena.Code('func_08_3D04')
def func_08_3D04():
    CameraMove(-750, 750, -2430, 2000)

    Return()

# id: 0x0009 offset: 0x3D16
@scena.Code('func_09_3D16')
def func_09_3D16():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_3D2C')
    def lambda_3D2C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3D2C)

    ChrWalkTo(0x00FE, 0, 750, -1170, 2000, 0x00)
    ChrWalkTo(0x00FE, -750, 750, -2430, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000A offset: 0x3D68
@scena.Code('func_0A_3D68')
def func_0A_3D68():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_3D7E')
    def lambda_3D7E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3D7E)

    ChrWalkTo(0x00FE, 0, 750, -1170, 2000, 0x00)
    ChrWalkTo(0x00FE, -740, 750, -1500, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000B offset: 0x3DBA
@scena.Code('func_0B_3DBA')
def func_0B_3DBA():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_3DD0')
    def lambda_3DD0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3DD0)

    ChrWalkTo(0x00FE, 0, 750, -1170, 2000, 0x00)
    ChrWalkTo(0x00FE, 520, 750, -1330, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000C offset: 0x3E0C
@scena.Code('func_0C_3E0C')
def func_0C_3E0C():
    OP_69(0x0009, 2000)

    Return()

# id: 0x000D offset: 0x3E14
@scena.Code('func_0D_3E14')
def func_0D_3E14():
    ChrWalkTo(0x00FE, 300, 750, -5000, 2000, 0x00)

    Return()

# id: 0x000E offset: 0x3E29
@scena.Code('func_0E_3E29')
def func_0E_3E29():
    ChrWalkTo(0x00FE, -750, 750, -2430, 2000, 0x00)
    ChrWalkTo(0x00FE, -600, 750, -3700, 2000, 0x00)

    Return()

# id: 0x000F offset: 0x3E52
@scena.Code('func_0F_3E52')
def func_0F_3E52():
    ChrWalkTo(0x00FE, -740, 750, -1500, 2000, 0x00)
    ChrWalkTo(0x00FE, -750, 750, -2430, 2000, 0x00)

    Return()

# id: 0x0010 offset: 0x3E7B
@scena.Code('func_10_3E7B')
def func_10_3E7B():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
