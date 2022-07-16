import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2209_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2209_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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

# id: 0xFFFF offset: 0x39F8
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
@scena.Code('Init')
def Init():
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
        'loc_AAB',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_D1',
    )

    Call(1, 0x0002)

    Jump('loc_AAB')

    def _loc_D1(): pass

    label('loc_D1')

    SetChrFlags(0x0008, 0x0010)
    TalkBegin(0x0008)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)

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
        'loc_A6A',
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
        'loc_1E1',
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

    def _loc_1E1(): pass

    label('loc_1E1')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ClearChrFlags(0x0008, 0x0010)
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
        'loc_3EC',
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

    Jump('loc_4F4')

    def _loc_3EC(): pass

    label('loc_3EC')

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

    def _loc_4F4(): pass

    label('loc_4F4')

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
    SetChrDirection(0x0008, 45, 400)
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
        'loc_8F7',
    )

    ChrTurnDirection(0x0105, 0x0102, 400)

    Jump('loc_90B')

    def _loc_8F7(): pass

    label('loc_8F7')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_90B',
    )

    ChrTurnDirection(0x0136, 0x0102, 400)

    def _loc_90B(): pass

    label('loc_90B')

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
        'loc_9B5',
    )

    ChrTurnDirection(0x0105, 0x0008, 400)

    Jump('loc_9C9')

    def _loc_9B5(): pass

    label('loc_9B5')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_9C9',
    )

    ChrTurnDirection(0x0136, 0x0008, 400)

    def _loc_9C9(): pass

    label('loc_9C9')

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

    Jump('loc_AA8')

    def _loc_A6A(): pass

    label('loc_A6A')

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
    def _loc_AA8(): pass

    label('loc_AA8')

    TalkEnd(0x0008)

    def _loc_AAB(): pass

    label('loc_AAB')

    Return()

# id: 0x0002 offset: 0xAAC
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_145F',
    )

    SetChrFlags(0x0008, 0x0010)
    TalkBegin(0x0008)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)

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
        'loc_141B',
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
        'loc_BD9',
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

    def _loc_BD9(): pass

    label('loc_BD9')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ClearChrFlags(0x0008, 0x0010)
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
    SetChrDirection(0x0008, 45, 400)
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

    @scena.Lambda('lambda_12C3')
    def lambda_12C3():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12C3)

    @scena.Lambda('lambda_12D1')
    def lambda_12D1():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_12D1)

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

    @scena.Lambda('lambda_135D')
    def lambda_135D():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_135D)

    @scena.Lambda('lambda_136B')
    def lambda_136B():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_136B)

    @scena.Lambda('lambda_1379')
    def lambda_1379():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1379)

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

    Jump('loc_1459')

    def _loc_141B(): pass

    label('loc_141B')

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
    def _loc_1459(): pass

    label('loc_1459')

    TalkEnd(0x0008)

    Jump('loc_145F')

    def _loc_145F(): pass

    label('loc_145F')

    Return()

# id: 0x0003 offset: 0x1460
@scena.Code('func_03_1460')
def func_03_1460():
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
        (0x00000000, 'loc_14BF'),
        (0x00000001, 'loc_15C0'),
        (-1, 'loc_1665'),
    )

    def _loc_14BF(): pass

    label('loc_14BF')

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

    Jump('loc_1665')

    def _loc_15C0(): pass

    label('loc_15C0')

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

    Jump('loc_1665')

    def _loc_1665(): pass

    label('loc_1665')

    EventEnd(0x01)
    TalkEnd(0x0008)
    SetChrDirection(0x0008, 0, 0)

    Return()

# id: 0x0004 offset: 0x1672
@scena.Code('func_04_1672')
def func_04_1672():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_1A90',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_1814',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1777',
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

    Jump('loc_1811')

    def _loc_1777(): pass

    label('loc_1777')

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

    def _loc_1811(): pass

    label('loc_1811')

    Jump('loc_1A8D')

    def _loc_1814(): pass

    label('loc_1814')

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
    def _loc_1A8D(): pass

    label('loc_1A8D')

    Jump('loc_1BF7')

    def _loc_1A90(): pass

    label('loc_1A90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B6E',
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

    Jump('loc_1BF7')

    def _loc_1B6E(): pass

    label('loc_1B6E')

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

    def _loc_1BF7(): pass

    label('loc_1BF7')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1BFB
@scena.Code('func_05_1BFB')
def func_05_1BFB():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrDirection(0x0008, 180, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1C28',
    )

    SetChrFlags(0x0105, 0x0080)

    Jump('loc_1C3A')

    def _loc_1C28(): pass

    label('loc_1C28')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1C3A',
    )

    SetChrFlags(0x0136, 0x0080)

    def _loc_1C3A(): pass

    label('loc_1C3A')

    SetChrPos(0x0101, -20, 750, 2830, 0)
    SetChrPos(0x0102, -20, 750, 2830, 0)
    CameraMove(-20, 750, 830, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1C8E',
    )

    SetChrPos(0x0105, -20, 750, 2830, 0)

    Jump('loc_1CAC')

    def _loc_1C8E(): pass

    label('loc_1C8E')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1CAC',
    )

    SetChrPos(0x0136, -20, 750, 2830, 0)

    def _loc_1CAC(): pass

    label('loc_1CAC')

    Sleep(2000)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    SetChrDirection(0x0008, 0, 400)
    Sleep(1200)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 80)
    OP_73(0x0000)

    @scena.Lambda('lambda_1CE6')
    def lambda_1CE6():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_1CE6')

    DispatchAsync2(0x0008, 0x0001, lambda_1CE6)

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
        'loc_1F21',
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

    Jump('loc_1F54')

    def _loc_1F21(): pass

    label('loc_1F21')

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

    def _loc_1F54(): pass

    label('loc_1F54')

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

# id: 0x0006 offset: 0x1FAD
@scena.Code('func_06_1FAD')
def func_06_1FAD():
    OP_28(0x001D, 0x04, 0x10)
    OP_28(0x001D, 0x01, 0x0080)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    SetChrPos(0x0101, 200, 750, 2830, 0)
    SetChrPos(0x0102, -500, 750, 2830, 0)
    SetChrPos(0x0105, 500, 750, 2830, 0)
    Sleep(2000)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 80)
    OP_73(0x0000)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0105, 0x0080)

    @scena.Lambda('lambda_202C')
    def lambda_202C():
        ChrMoveToRelative(0x0101, 0, 0, -8500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_202C)

    Sleep(500)

    @scena.Lambda('lambda_204C')
    def lambda_204C():
        ChrMoveToRelative(0x0102, 0, 0, -7500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_204C)

    Sleep(600)

    @scena.Lambda('lambda_206C')
    def lambda_206C():
        ChrMoveToRelative(0x0105, 0, 0, -6500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_206C)

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
    SetChrName('')

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
    SetChrName('')

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
    ClearMapFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x253E
@scena.Code('func_07_253E')
def func_07_253E():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrDirection(0x0008, 180, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_256B',
    )

    SetChrFlags(0x0105, 0x0080)

    Jump('loc_257D')

    def _loc_256B(): pass

    label('loc_256B')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_257D',
    )

    SetChrFlags(0x0136, 0x0080)

    def _loc_257D(): pass

    label('loc_257D')

    SetChrPos(0x0101, -20, 750, 2830, 0)
    SetChrPos(0x0102, -20, 750, 2830, 0)
    CameraMove(-20, 750, 830, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_25D1',
    )

    SetChrPos(0x0105, -20, 750, 2830, 0)

    Jump('loc_25EF')

    def _loc_25D1(): pass

    label('loc_25D1')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_25EF',
    )

    SetChrPos(0x0136, -20, 750, 2830, 0)

    def _loc_25EF(): pass

    label('loc_25EF')

    Sleep(2000)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    SetChrDirection(0x0008, 0, 400)
    Sleep(1200)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 80)
    OP_73(0x0000)

    @scena.Lambda('lambda_2629')
    def lambda_2629():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_2629')

    DispatchAsync2(0x0008, 0x0001, lambda_2629)

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
        'loc_266A',
    )

    Sleep(500)

    CreateThread(0x0105, 0x01, 0x01, 0x000B)

    Jump('loc_2683')

    def _loc_266A(): pass

    label('loc_266A')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2683',
    )

    Sleep(500)

    CreateThread(0x0136, 0x01, 0x01, 0x000B)

    def _loc_2683(): pass

    label('loc_2683')

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

    @scena.Lambda('lambda_2829')
    def lambda_2829():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_2829')

    DispatchAsync2(0x0008, 0x0001, lambda_2829)

    SetChrPos(0x0009, 300, 750, -5000, 0)

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
        'loc_28BA',
    )

    Sleep(300)

    CreateThread(0x0105, 0x01, 0x01, 0x000F)

    Jump('loc_28D3')

    def _loc_28BA(): pass

    label('loc_28BA')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_28D3',
    )

    Sleep(300)

    CreateThread(0x0136, 0x01, 0x01, 0x000F)

    def _loc_28D3(): pass

    label('loc_28D3')

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

    @scena.Lambda('lambda_293D')
    def lambda_293D():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_293D)

    @scena.Lambda('lambda_294B')
    def lambda_294B():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_294B)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2971',
    )

    @scena.Lambda('lambda_2966')
    def lambda_2966():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2966)

    Jump('loc_298C')

    def _loc_2971(): pass

    label('loc_2971')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_298C',
    )

    @scena.Lambda('lambda_2984')
    def lambda_2984():
        ChrTurnDirection(0x0136, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_2984)

    def _loc_298C(): pass

    label('loc_298C')

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
        'loc_2B5C',
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

    Jump('loc_2BC2')

    def _loc_2B5C(): pass

    label('loc_2B5C')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2BBD',
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

    Jump('loc_2BC2')

    def _loc_2BBD(): pass

    label('loc_2BBD')

    Sleep(1000)

    def _loc_2BC2(): pass

    label('loc_2BC2')

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
        'loc_2ED4',
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

    Jump('loc_2EFC')

    def _loc_2ED4(): pass

    label('loc_2ED4')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2EFC',
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

    def _loc_2EFC(): pass

    label('loc_2EFC')

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
        'loc_2F81',
    )

    ChrTurnDirection(0x0105, 0x0008, 400)

    Jump('loc_2F95')

    def _loc_2F81(): pass

    label('loc_2F81')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2F95',
    )

    ChrTurnDirection(0x0136, 0x0008, 400)

    def _loc_2F95(): pass

    label('loc_2F95')

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

    @scena.Lambda('lambda_3006')
    def lambda_3006():
        ChrTurnDirection(0x0101, 0x0008, 0)
        Yield()

        Jump('lambda_3006')

    DispatchAsync2(0x0101, 0x0001, lambda_3006)

    @scena.Lambda('lambda_3017')
    def lambda_3017():
        ChrTurnDirection(0x0102, 0x0008, 0)
        Yield()

        Jump('lambda_3017')

    DispatchAsync2(0x0102, 0x0001, lambda_3017)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3043',
    )

    @scena.Lambda('lambda_3035')
    def lambda_3035():
        ChrTurnDirection(0x0105, 0x0008, 0)
        Yield()

        Jump('lambda_3035')

    DispatchAsync2(0x0105, 0x0001, lambda_3035)

    Jump('loc_3061')

    def _loc_3043(): pass

    label('loc_3043')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3061',
    )

    @scena.Lambda('lambda_3056')
    def lambda_3056():
        ChrTurnDirection(0x0136, 0x0008, 0)
        Yield()

        Jump('lambda_3056')

    DispatchAsync2(0x0136, 0x0001, lambda_3056)

    def _loc_3061(): pass

    label('loc_3061')

    ChrWalkTo(0x0008, 0, 750, -1170, 2000, 0x00)
    SetChrDirection(0x0008, 0, 0)
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
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_30E2',
    )

    TerminateThread(0x0105, 0xFF)

    Jump('loc_30F3')

    def _loc_30E2(): pass

    label('loc_30E2')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_30F3',
    )

    TerminateThread(0x0136, 0xFF)

    def _loc_30F3(): pass

    label('loc_30F3')

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
        'loc_32CA',
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

    Jump('loc_3481')

    def _loc_32CA(): pass

    label('loc_32CA')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_33F3',
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

    Jump('loc_3481')

    def _loc_33F3(): pass

    label('loc_33F3')

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

    def _loc_3481(): pass

    label('loc_3481')

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
        'loc_3659',
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

    Jump('loc_37D1')

    def _loc_3659(): pass

    label('loc_3659')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_374C',
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

    Jump('loc_37D1')

    def _loc_374C(): pass

    label('loc_374C')

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

    def _loc_37D1(): pass

    label('loc_37D1')

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
    SetChrName('')

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
    ClearMapFlags(0x00400000)

    Return()

# id: 0x0008 offset: 0x385E
@scena.Code('func_08_385E')
def func_08_385E():
    CameraMove(-750, 750, -2430, 2000)

    Return()

# id: 0x0009 offset: 0x3870
@scena.Code('func_09_3870')
def func_09_3870():
    ClearChrFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_3886')
    def lambda_3886():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3886)

    ChrWalkTo(0x00FE, 0, 750, -1170, 2000, 0x00)
    ChrWalkTo(0x00FE, -750, 750, -2430, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000A offset: 0x38C2
@scena.Code('func_0A_38C2')
def func_0A_38C2():
    ClearChrFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_38D8')
    def lambda_38D8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_38D8)

    ChrWalkTo(0x00FE, 0, 750, -1170, 2000, 0x00)
    ChrWalkTo(0x00FE, -740, 750, -1500, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000B offset: 0x3914
@scena.Code('func_0B_3914')
def func_0B_3914():
    ClearChrFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_392A')
    def lambda_392A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_392A)

    ChrWalkTo(0x00FE, 0, 750, -1170, 2000, 0x00)
    ChrWalkTo(0x00FE, 520, 750, -1330, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000C offset: 0x3966
@scena.Code('func_0C_3966')
def func_0C_3966():
    OP_69(0x0009, 2000)

    Return()

# id: 0x000D offset: 0x396E
@scena.Code('func_0D_396E')
def func_0D_396E():
    ChrWalkTo(0x00FE, 300, 750, -5000, 2000, 0x00)

    Return()

# id: 0x000E offset: 0x3983
@scena.Code('func_0E_3983')
def func_0E_3983():
    ChrWalkTo(0x00FE, -750, 750, -2430, 2000, 0x00)
    ChrWalkTo(0x00FE, -600, 750, -3700, 2000, 0x00)

    Return()

# id: 0x000F offset: 0x39AC
@scena.Code('func_0F_39AC')
def func_0F_39AC():
    ChrWalkTo(0x00FE, -740, 750, -1500, 2000, 0x00)
    ChrWalkTo(0x00FE, -750, 750, -2430, 2000, 0x00)

    Return()

# id: 0x0010 offset: 0x39D5
@scena.Code('func_10_39D5')
def func_10_39D5():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
