import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4130_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4130_2 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4130.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7C7B
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
    Return()

# id: 0x0001 offset: 0x65
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x66
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8B',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_BC')

    def _loc_8B(): pass

    label('loc_8B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A1',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_BC')

    def _loc_A1(): pass

    label('loc_A1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B7',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_BC')

    def _loc_B7(): pass

    label('loc_B7')

    SetChrSubChip(0x00FE, 2)

    def _loc_BC(): pass

    label('loc_BC')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_12D',
    )

    ChrTalk(
        0x001F,
        (
            '#0540140839V#100F阿加特与卡西乌斯相比\n',
            '虽然还有些不够成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140840V但这回可多亏有他在啊。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CC')

    def _loc_12D(): pass

    label('loc_12D')

    SetScenaFlags(ScenaFlag(0x00DE, 0, 0x6F0))
    SetScenaFlags(ScenaFlag(0x0002, 7, 0x17))

    ChrTalk(
        0x001F,
        (
            '#0540140831V#104F哎呀呀，逃亡的生活\n',
            '对于我这一把老骨头而言真是艰苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140832V#000F阿加特给你们添了不少乱吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0540140833V#100F不，并非如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140834V他把我们照顾得非常好。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140835V#100F选择的逃走路线\n',
            '也没有让我们不方便，\n',
            '都是经过了细心考虑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140836V#104F阿加特这小子真是好得没话说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140837V#004F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0540140838V#101F与卡西乌斯相比\n',
            '虽然还有些不够成熟，\n',
            '但这回可多亏有他在啊。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CC(): pass

    label('loc_2CC')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x2D5
@scena.Code('func_03_2D5')
def func_03_2D5():
    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2FA',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_32B')

    def _loc_2FA(): pass

    label('loc_2FA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_310',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_32B')

    def _loc_310(): pass

    label('loc_310')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_326',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_32B')

    def _loc_326(): pass

    label('loc_326')

    SetChrSubChip(0x00FE, 1)

    def _loc_32B(): pass

    label('loc_32B')

    SetChrDirection(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_3C3',
    )

    ChrTalk(
        0x001E,
        (
            '#0070140829V#560F终于实现和爷爷一起\n',
            '吃冰淇淋的愿望了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070140830V#562F本来还想和阿加特大哥哥\n',
            '一起来这里吃的，\n',
            '结果被他拒绝了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_556')

    def _loc_3C3(): pass

    label('loc_3C3')

    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))
    SetScenaFlags(ScenaFlag(0x00DE, 1, 0x6F1))

    ChrTalk(
        0x001E,
        (
            '#0070140821V#560F啊……\n',
            '艾丝蒂尔姐姐和约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140822V#501F提妲，\n',
            '你好像很开心嘛。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0070140823V#061F嘿嘿，\n',
            '因为终于实现和爷爷一起\n',
            '吃冰淇淋的愿望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140824V#001F啊～真不错呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0070140825V#061F嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070140826V#064F本来还想和阿加特大哥哥\n',
            '一起来这里吃的，\n',
            '结果被他拒绝了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140827V#509F要阿加特吃冰淇淋……\n',
            '哈哈，被拒绝也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0070140828V#562F呜呜……\n',
            '冰淇淋很好吃的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_556(): pass

    label('loc_556')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x55F
@scena.Code('func_04_55F')
def func_04_55F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_5B2',
    )

    ChrTalk(
        0x001D,
        (
            '#0050140713V#053F武术大会啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140720V的确是个一试身手的好机会。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CB')

    def _loc_5B2(): pass

    label('loc_5B2')

    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))
    SetScenaFlags(ScenaFlag(0x00DD, 6, 0x6EE))

    ChrTalk(
        0x001D,
        (
            '#0050140713V#053F武术大会啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140714V的确是个一试身手的好机会。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140715V#050F而且那个『不动金』这次也参加了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140716V#000F阿加特，\n',
            '你明年也来参加如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0050140717V#053F……哼，虽然是有兴趣，\n',
            '但我可不想被别人看热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140718V#509F真是一点都不老实的说法～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CB(): pass

    label('loc_6CB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x6CF
@scena.Code('func_05_6CF')
def func_05_6CF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '由特务兵来镇守王都，\n',
            '王都守卫队却撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是难以理解，\n',
            '而且根本不知道\n',
            '是谁下达的这个命令啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x73F
@scena.Code('func_06_73F')
def func_06_73F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_7A0',
    )

    ChrTalk(
        0x00FE,
        (
            '对于最近发生的事情，\n',
            '我们也是一头雾水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之王都的正规军\n',
            '基本上都撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_816')

    def _loc_7A0(): pass

    label('loc_7A0')

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    ChrTalk(
        0x00FE,
        (
            '对于发生的事情，\n',
            '我们也是一头雾水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之王都的正规军\n',
            '基本上都撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '这么一来可如何是好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_816(): pass

    label('loc_816')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x81A
@scena.Code('func_07_81A')
def func_07_81A():
    Call(2, 0x0008)

    Return()

# id: 0x0008 offset: 0x81F
@scena.Code('func_08_81F')
def func_08_81F():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_8B8',
    )

    ChrTalk(
        0x001A,
        (
            '政变的发动人\n',
            '竟然是那位理查德上校……\n',
            '让我好震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '不过，\n',
            '能防范于未然实在是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '真的是应该要感谢\n',
            '亲卫队和游击士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_8B8(): pass

    label('loc_8B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_907',
    )

    ChrTalk(
        0x001A,
        (
            '要发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '那些王都的守卫队士兵\n',
            '已经匆忙地撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_907(): pass

    label('loc_907')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_9A9',
    )

    ChrTalk(
        0x001A,
        (
            '为了筹备庆典的取材，\n',
            '大家都在忙着做准备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '但说实话，\n',
            '庆典到底会怎样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '女王陛下那边目前也\n',
            '没有任何公告发表，\n',
            '而且还有传言说会中止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_9A9(): pass

    label('loc_9A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_A13',
    )

    ChrTalk(
        0x001A,
        (
            '武术大会的优胜者\n',
            '好像是朵洛希认识的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '她呀，高兴过头了，\n',
            '一边跳着舞一边跑回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_A13(): pass

    label('loc_A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_AF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_A72',
    )

    ChrTalk(
        0x001A,
        (
            '一大早，\n',
            '朵洛希就拿着照相机\n',
            '跑到竞技场去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '我看她好像充满干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF0')

    def _loc_A72(): pass

    label('loc_A72')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x001A,
        (
            '早上好。\n',
            '今天是武术大会总决赛的日子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '一大早，\n',
            '朵洛希就拿着照相机\n',
            '跑到竞技场去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '我看她好像充满干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF0(): pass

    label('loc_AF0')

    Jump('loc_E96')

    def _loc_AF3(): pass

    label('loc_AF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_B4D',
    )

    ChrTalk(
        0x001A,
        (
            '最近，\n',
            '王国军的人每天都会过来检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '我们通讯社\n',
            '并没有做什么坏事对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_B4D(): pass

    label('loc_B4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_C52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_BA8',
    )

    ChrTalk(
        0x001A,
        (
            '理查德上校\n',
            '真是个很棒的男人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '我也好想去\n',
            '对他进行采访取材呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4F')

    def _loc_BA8(): pass

    label('loc_BA8')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x001A,
        (
            '理查德上校\n',
            '真是个很棒的男人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '举止文雅，知识渊博，\n',
            '风度翩翩，一表人才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '我也好想去\n',
            '对他进行采访取材呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '下次拜托奈尔\n',
            '看看能不能带我去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C4F(): pass

    label('loc_C4F')

    Jump('loc_E96')

    def _loc_C52(): pass

    label('loc_C52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_CC3',
    )

    ChrTalk(
        0x001A,
        (
            '刚才奈尔记者\n',
            '从外面回来了。\n',
            '感觉有好一阵子没见到他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '他这个人啊，\n',
            '经常会突然失踪好几天呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_CC3(): pass

    label('loc_CC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_D4F',
    )

    ChrTalk(
        0x001A,
        (
            '本社的记者们\n',
            '白天外出取材，\n',
            '经常不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '奈尔记者更是\n',
            '很少呆在通讯社里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '经常都无法和他取得联络，\n',
            '真是麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_D4F(): pass

    label('loc_D4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_DB5',
    )

    ChrTalk(
        0x001A,
        (
            '下班之后约朵洛希\n',
            '一起去外面玩的计划又泡汤了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '别看她那个样子，\n',
            '其实工作很忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_DB5(): pass

    label('loc_DB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_E96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_E06',
    )

    ChrTalk(
        0x001A,
        (
            '现在编辑室的人\n',
            '都外出采访去了，\n',
            '如果有什么事可以让我转告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_E06(): pass

    label('loc_E06')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x001A,
        (
            '欢迎来到利贝尔通讯社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '一楼是接待处，二楼是编辑室，\n',
            '三楼是器材室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '现在编辑室的人\n',
            '都外出采访去了，\n',
            '如果有什么事可以让我转告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E96(): pass

    label('loc_E96')

    TalkEnd(0x001A)

    Return()

# id: 0x0009 offset: 0xE9A
@scena.Code('func_09_E9A')
def func_09_E9A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_F08',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来就去\n',
            '最近引起热门话题的\n',
            '冰淇淋店进行取材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天东街区的那个店铺\n',
            '客人特别多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1650')

    def _loc_F08(): pass

    label('loc_F08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_FC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_F59',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔前辈他\n',
            '被军队逮捕了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸亏我是\n',
            '文化专栏的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC1')

    def _loc_F59(): pass

    label('loc_F59')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '奈尔前辈他\n',
            '被军队逮捕了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就知道\n',
            '他迟早会落到如此下场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸亏我是\n',
            '文化专栏的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FC1(): pass

    label('loc_FC1')

    Jump('loc_1650')

    def _loc_FC4(): pass

    label('loc_FC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_10BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1035',
    )

    ChrTalk(
        0x00FE,
        (
            '本打算去到柏斯的\n',
            '『安特洛丝餐厅』取材的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么办啊……\n',
            '只能写一篇别的报道来代替了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B7')

    def _loc_1035(): pass

    label('loc_1035')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '哇呀呀，\n',
            '定期船停飞了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本打算去到柏斯的\n',
            '『安特洛丝餐厅』取材的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么办啊……\n',
            '只能写一篇别的报道来代替了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B7(): pass

    label('loc_10B7')

    Jump('loc_1650')

    def _loc_10BA(): pass

    label('loc_10BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_11DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1136',
    )

    ChrTalk(
        0x00FE,
        (
            '取材的方式是\n',
            '去美味的店品尝料理，\n',
            '然后展示在文化专栏里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要做出可以向\n',
            '奈尔前辈炫耀的东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DC')

    def _loc_1136(): pass

    label('loc_1136')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '这次就以现在热门的餐厅\n',
            '为主题作一期特辑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '取材的方式是\n',
            '去美味的店品尝料理，\n',
            '然后展示在文化专栏里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要做出可以向\n',
            '奈尔前辈炫耀的东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11DC(): pass

    label('loc_11DC')

    Jump('loc_1650')

    def _loc_11DF(): pass

    label('loc_11DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1312',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1258',
    )

    ChrTalk(
        0x00FE,
        (
            '朵洛希虽说是个新人，\n',
            '不过实力确实非常强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，让她进入我们通讯社的\n',
            '总编的眼光更加令人佩服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_130F')

    def _loc_1258(): pass

    label('loc_1258')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '朵洛希虽说是个新人，\n',
            '不过实力确实非常强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是拍武术大会的照片，\n',
            '还是料理的照片，\n',
            '她总能选择最佳的角度去拍摄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，让她进入我们通讯社的\n',
            '总编的眼光更加令人佩服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_130F(): pass

    label('loc_130F')

    Jump('loc_1650')

    def _loc_1312(): pass

    label('loc_1312')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1401',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1371',
    )

    ChrTalk(
        0x00FE,
        (
            '很多作家或者撰稿人\n',
            '每逢截稿的时间临近\n',
            '就会犯感冒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人头疼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13FE')

    def _loc_1371(): pass

    label('loc_1371')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '很多作家或者撰稿人\n',
            '每逢截稿的时间临近\n',
            '就会犯感冒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能是太过拼命，\n',
            '结果把身体弄坏了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再或者就是装病，\n',
            '总之很让人头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13FE(): pass

    label('loc_13FE')

    Jump('loc_1650')

    def _loc_1401(): pass

    label('loc_1401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_14FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1466',
    )

    ChrTalk(
        0x00FE,
        (
            '唉唉，\n',
            '我乘坐定期船去外地取原稿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果到了之后\n',
            '才被作者告知还没有写好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F8')

    def _loc_1466(): pass

    label('loc_1466')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '唉唉，\n',
            '我乘坐定期船去外地取原稿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果到了之后\n',
            '才被作者告知还没有写好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果导力通信能够更加普及的话，\n',
            '联络起来就会方便了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F8(): pass

    label('loc_14F8')

    Jump('loc_1650')

    def _loc_14FB(): pass

    label('loc_14FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1505',
    )

    Jump('loc_1650')

    def _loc_1505(): pass

    label('loc_1505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_155F',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我要乘坐定期船\n',
            '去外地取原稿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要早点做好准备\n',
            '才不至于延误乘船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1650')

    def _loc_155F(): pass

    label('loc_155F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_15EA',
    )

    ChrTalk(
        0x00FE,
        (
            '《利贝尔通讯》的文化专栏\n',
            '是由我来担当编辑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本专栏通常会刊登\n',
            '连载小说和读者的意见，\n',
            '也会对一些热门话题进行取材报道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1650')

    def _loc_15EA(): pass

    label('loc_15EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1650',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '如果不能快点取回作者的原稿，\n',
            '我会被责骂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奈尔和诺蒂亚\n',
            '都要比总编严厉许多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1650(): pass

    label('loc_1650')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1654
@scena.Code('func_0A_1654')
def func_0A_1654():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_16C2',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '这次又麻烦奈尔帮我的忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '下次一定要让他教教我\n',
            '怎么样才能弄到好新闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D84')

    def _loc_16C2(): pass

    label('loc_16C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_16E8',
    )

    ChrTalk(
        0x00FE,
        (
            '街上的情况很奇怪呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D84')

    def _loc_16E8(): pass

    label('loc_16E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_176A',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔从刚来杂志社的时候\n',
            '就会做些让人目瞪口呆的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过大概正因为如此，\n',
            '才能抢在别人之前报道一些独家新闻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D84')

    def _loc_176A(): pass

    label('loc_176A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1866',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_17C7',
    )

    ChrTalk(
        0x00FE,
        (
            '那个狐狸眼睛的女上尉，\n',
            '实在让人生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管走到哪里\n',
            '都要挖苦别人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1863')

    def _loc_17C7(): pass

    label('loc_17C7')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '理查德上校是很不错，\n',
            '但情报部和特务兵\n',
            '那些家伙就不敢恭维了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是那个\n',
            '长着狐狸眼睛的女上尉，\n',
            '实在让人生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管走到哪里\n',
            '都要挖苦别人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1863(): pass

    label('loc_1863')

    Jump('loc_1D84')

    def _loc_1866(): pass

    label('loc_1866')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_18DA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼，情报部的监视非常严，\n',
            '取材也寸步难行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们这样做，\n',
            '和当年埃雷波尼亚帝国的宪兵有什么区别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D84')

    def _loc_18DA(): pass

    label('loc_18DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1A07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1967',
    )

    ChrTalk(
        0x00FE,
        (
            '我和奈尔常常都会\n',
            '围绕着杂志报道方针的问题\n',
            '与总编极力争辩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总编总能以\n',
            '一副笑脸哄着我们，\n',
            '我们很吃他的怀柔政策呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A04')

    def _loc_1967(): pass

    label('loc_1967')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '总编是一个不可思议的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和奈尔常常都会\n',
            '围绕着杂志报道方针的问题\n',
            '与总编极力争辩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总编总能以\n',
            '一副笑脸哄着我们，\n',
            '我们很吃他的怀柔政策呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A04(): pass

    label('loc_1A04')

    Jump('loc_1D84')

    def _loc_1A07(): pass

    label('loc_1A07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1AE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1A68',
    )

    ChrTalk(
        0x00FE,
        (
            '直到今天早上\n',
            '奈尔还在调查什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是发现了什么\n',
            '好的新闻线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE6')

    def _loc_1A68(): pass

    label('loc_1A68')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '直到今天早上\n',
            '奈尔还在调查什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是发现了什么\n',
            '好的新闻线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～作为前辈，\n',
            '我也不能就这样输给他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AE6(): pass

    label('loc_1AE6')

    Jump('loc_1D84')

    def _loc_1AE9(): pass

    label('loc_1AE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1B63',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '大会今年改成了团体赛，\n',
            '想拍摄好的确很困难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能的话，\n',
            '真想找个好一点的摄影师\n',
            '来替我拍摄啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D84')

    def _loc_1B63(): pass

    label('loc_1B63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1C22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1BB7',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯正在准备\n',
            '出版武术大会的特刊哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要努力取材啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1F')

    def _loc_1BB7(): pass

    label('loc_1BB7')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '今天终于到大会的正式赛了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯正在准备\n',
            '出版武术大会的特刊哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要努力取材啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C1F(): pass

    label('loc_1C1F')

    Jump('loc_1D84')

    def _loc_1C22(): pass

    label('loc_1C22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1D19',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1C83',
    )

    ChrTalk(
        0x00FE,
        (
            '还是老样子，\n',
            '奈尔又是一去不复返。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚回来没多久，\n',
            '就立刻又飞奔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D16')

    def _loc_1C83(): pass

    label('loc_1C83')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '还是老样子，\n',
            '奈尔又是一去不复返。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚回来没多久，\n',
            '就立刻又飞奔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他脸色不太健康\n',
            '是因为吸烟的缘故，\n',
            '但体力至少是常人的一倍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D16(): pass

    label('loc_1D16')

    Jump('loc_1D84')

    def _loc_1D19(): pass

    label('loc_1D19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1D84',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，真是的，\n',
            '再不快点，预选赛就要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，器材带上了，\n',
            '取材用的通行许可证也带上了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D84(): pass

    label('loc_1D84')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1D88
@scena.Code('func_0B_1D88')
def func_0B_1D88():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1F8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1E08',
    )

    ChrTalk(
        0x000A,
        (
            '#0280140870V#151F听我说，\n',
            '奈尔前辈都告诉我了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280140864V因为这次的报道，\n',
            '前辈和我很有可能会获得\n',
            '菲利策奖哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F87')

    def _loc_1E08(): pass

    label('loc_1E08')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x00DE, 3, 0x6F3))

    ChrTalk(
        0x000A,
        (
            '#0280140862V#151F啊，是小艾你们啊～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280140863V#150F听我说，\n',
            '奈尔前辈都告诉我了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280140864V因为这次的报道，\n',
            '前辈和我很有可能会获得\n',
            '菲利策奖哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140865V#505F菲利策？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140866V#010F在新闻、文学和音乐等领域\n',
            '取得年度最佳成绩的人被授予的奖项。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140867V对于记者而言，\n',
            '毫无疑问是最高荣誉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140868V#004F啊～真不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280140869V#151F嘿嘿嘿，\n',
            '这也是托小艾你们的福啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F87(): pass

    label('loc_1F87')

    Jump('loc_2152')

    def _loc_1F8A(): pass

    label('loc_1F8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1FCC',
    )

    ChrTalk(
        0x000A,
        (
            '#0280130365V#151F呜～哇！\n',
            '奈尔前辈还活着，\n',
            '真是太好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2152')

    def _loc_1FCC(): pass

    label('loc_1FCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_201E',
    )

    ChrTalk(
        0x000A,
        (
            '#0280130363V#152F啊，拜托了～！\n',
            '小艾～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130359V一定要救救奈尔前辈～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2152')

    def _loc_201E(): pass

    label('loc_201E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_210F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_2085',
    )

    ChrTalk(
        0x000A,
        (
            '#0280130361V#154F唔～…………\n',
            '虽然总编让我去找奈尔前辈～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130362V但上哪去找呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_210C')

    def _loc_2085(): pass

    label('loc_2085')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x000A,
        (
            '#0280111973V#151F呀，是小艾你们啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111974V恭喜你们获得优胜。\n',
            '真是激动人心的比赛呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111975V我太兴奋了，\n',
            '就咔嚓咔嚓地拍个不停呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_210C(): pass

    label('loc_210C')

    Jump('loc_2152')

    def _loc_210F(): pass

    label('loc_210F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2119',
    )

    Jump('loc_2152')

    def _loc_2119(): pass

    label('loc_2119')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2123',
    )

    Jump('loc_2152')

    def _loc_2123(): pass

    label('loc_2123')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_212D',
    )

    Jump('loc_2152')

    def _loc_212D(): pass

    label('loc_212D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2137',
    )

    Jump('loc_2152')

    def _loc_2137(): pass

    label('loc_2137')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2141',
    )

    Jump('loc_2152')

    def _loc_2141(): pass

    label('loc_2141')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_214B',
    )

    Jump('loc_2152')

    def _loc_214B(): pass

    label('loc_214B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2152',
    )

    def _loc_2152(): pass

    label('loc_2152')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2156
@scena.Code('func_0C_2156')
def func_0C_2156():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_230C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_21E1',
    )

    ChrTalk(
        0x00FE,
        (
            '#0270140877V#141F对于你们精彩表现的话题，\n',
            '读者的反响尤为强烈呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140878V如果以后有什么有趣的消息，\n',
            '还要靠你们提供了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2309')

    def _loc_21E1(): pass

    label('loc_21E1')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    SetScenaFlags(ScenaFlag(0x00DE, 4, 0x6F4))

    ChrTalk(
        0x00FE,
        (
            '#0270140872V#141F哟，艾丝蒂尔、约修亚！\n',
            '这次真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140873V多亏了你们，\n',
            '这次与政变相关的特刊简直卖疯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140874V对于你们精彩表现的话题，\n',
            '读者的反响尤为强烈呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140875V虽然最后根据协会的意向，\n',
            '没有刊登出你们的名字。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140876V#147F对了，如果以后有什么好的线索，\n',
            '还要靠你们提供了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2309(): pass

    label('loc_2309')

    Jump('loc_236D')

    def _loc_230C(): pass

    label('loc_230C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2316',
    )

    Jump('loc_236D')

    def _loc_2316(): pass

    label('loc_2316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2320',
    )

    Jump('loc_236D')

    def _loc_2320(): pass

    label('loc_2320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_232A',
    )

    Jump('loc_236D')

    def _loc_232A(): pass

    label('loc_232A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2334',
    )

    Jump('loc_236D')

    def _loc_2334(): pass

    label('loc_2334')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_233E',
    )

    Jump('loc_236D')

    def _loc_233E(): pass

    label('loc_233E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2348',
    )

    Jump('loc_236D')

    def _loc_2348(): pass

    label('loc_2348')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2352',
    )

    Jump('loc_236D')

    def _loc_2352(): pass

    label('loc_2352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_235C',
    )

    Jump('loc_236D')

    def _loc_235C(): pass

    label('loc_235C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2366',
    )

    Jump('loc_236D')

    def _loc_2366(): pass

    label('loc_2366')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_236D',
    )

    def _loc_236D(): pass

    label('loc_236D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x2371
@scena.Code('func_0D_2371')
def func_0D_2371():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_24B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_23F8',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校的\n',
            '政变报道特辑反响强烈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '转瞬之间销量就已经赶上了\n',
            '理查德上校介绍特辑\n',
            '和戴尔蒙市长被捕特辑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B6')

    def _loc_23F8(): pass

    label('loc_23F8')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '理查德上校的\n',
            '政变报道特辑反响强烈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '转瞬之间销量就已经赶上了\n',
            '理查德上校介绍特辑\n',
            '和戴尔蒙市长被捕特辑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如此有冲击力的事件，\n',
            '与报道有关的质问非常多，\n',
            '回答起来也很麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24B6(): pass

    label('loc_24B6')

    Jump('loc_3F52')

    def _loc_24B9(): pass

    label('loc_24B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_257D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2519',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才协会发联络过来，\n',
            '说在艾贝尔离宫找到奈尔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～太好了太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257A')

    def _loc_2519(): pass

    label('loc_2519')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '刚才游击士协会\n',
            '发联络过来说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在艾贝尔离宫\n',
            '找到奈尔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～太好了太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_257A(): pass

    label('loc_257A')

    Jump('loc_3F52')

    def _loc_257D(): pass

    label('loc_257D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_25A4',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔的事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F52')

    def _loc_25A4(): pass

    label('loc_25A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_28D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_260A',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '我正有事要找奈尔呢……\n',
            '他跑到哪里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '这几天都没有看到他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CD')

    def _loc_260A(): pass

    label('loc_260A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2668',
    )

    ChrTalk(
        0x00FE,
        (
            '我正有事要找奈尔呢，\n',
            '可这几天都没有看到他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '这种事情早已经习惯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CD')

    def _loc_2668(): pass

    label('loc_2668')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_26ED',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '我正有事要找奈尔呢……\n',
            '他跑到哪里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '这几天都没有看到他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '这种事情早已经习惯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CD')

    def _loc_26ED(): pass

    label('loc_26ED')

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，你们是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也正有事要找他呢，\n',
            '可这几天都没有看到他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '这种事情早已经习惯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28CD(): pass

    label('loc_28CD')

    Jump('loc_3F52')

    def _loc_28D0(): pass

    label('loc_28D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2B7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_292C',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '朵洛希她今天也要去竞技场取材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '碰到她的话帮我打个招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B7B')

    def _loc_292C(): pass

    label('loc_292C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_298E',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，今天是总决赛哦。\n',
            '我会支持你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '朵洛希她今天也要去竞技场取材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B7B')

    def _loc_298E(): pass

    label('loc_298E')

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，今天你们\n',
            '要进行武术大会的决赛了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的工作太忙，不能去竞技场了，\n',
            '就在这里给你们加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，谢谢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B7B(): pass

    label('loc_2B7B')

    Jump('loc_3F52')

    def _loc_2B7E(): pass

    label('loc_2B7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2F92',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2BBC',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，\n',
            '我们社的记者人人都很有个性呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F8F')

    def _loc_2BBC(): pass

    label('loc_2BBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2C00',
    )

    ChrTalk(
        0x00FE,
        (
            '我还想着\n',
            '他难得会呆在杂志社里，\n',
            '原来是在等你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F8F')

    def _loc_2C00(): pass

    label('loc_2C00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_2C93',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '我们社的记者\n',
            '人人都很有个性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此，\n',
            '每到讨论问题的时候\n',
            '场面简直就像在吵架一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过许多优秀的文章\n',
            '也是那样诞生的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F8F')

    def _loc_2C93(): pass

    label('loc_2C93')

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            Expr.Return,
        ),
        'loc_2F0D',
    )

    ChrTalk(
        0x0101,
        (
            '#000F嗯，是啊。\n',
            '我们刚和他见过面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，我还想着\n',
            '他难得会呆在杂志社里，\n',
            '原来是在等你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～除了开会的日子，\n',
            '能看到他简直是太稀罕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他平常一直都在外面\n',
            '到处奔波寻找新闻素材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F8F')

    def _loc_2F0D(): pass

    label('loc_2F0D')

    ChrTalk(
        0x0101,
        (
            '#000F嗯，是啊。\n',
            '今天我们和他约好了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是这样啊，\n',
            '他现在就在编辑室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '编辑室在出版社的二层。\n',
            '你们赶快去找他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F8F(): pass

    label('loc_2F8F')

    Jump('loc_3F52')

    def _loc_2F92(): pass

    label('loc_2F92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3319',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2FFD',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，军队的情报部\n',
            '要求对我们的报道进行审查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队本来应该\n',
            '没有这样的权利才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3316')

    def _loc_2FFD(): pass

    label('loc_2FFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_304D',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔他啊，\n',
            '好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3316')

    def _loc_304D(): pass

    label('loc_304D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_3106',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '自从女王陛下生病以来，\n',
            '情报部的家伙们就经常来制造麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然还蛮横无理地\n',
            '要求对我们的报道进行审查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国\n',
            '保障国民的言论自由，\n',
            '他们根本没有这样的权利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3316')

    def _loc_3106(): pass

    label('loc_3106')

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F啊，这个嘛，\n',
            '其实不是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来，\n',
            '他好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3316(): pass

    label('loc_3316')

    Jump('loc_3F52')

    def _loc_3319(): pass

    label('loc_3319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_368F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3393',
    )

    ChrTalk(
        0x00FE,
        (
            '我听记者们说了，\n',
            '你们是参加武术大会的选手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奈尔知道以后，\n',
            '说要去采访你们，\n',
            '然后就跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_368C')

    def _loc_3393(): pass

    label('loc_3393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_33F8',
    )

    ChrTalk(
        0x00FE,
        (
            '听说你们\n',
            '是参加武术大会的选手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奈尔知道以后，\n',
            '说要去采访你们，\n',
            '然后就跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_368C')

    def _loc_33F8(): pass

    label('loc_33F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_3498',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听记者们说了。\n',
            '你们是参加武术大会的选手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奈尔知道以后\n',
            '说要去采访你们，\n',
            '然后就跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们没有遇见他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_368C')

    def _loc_3498(): pass

    label('loc_3498')

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说你们\n',
            '是参加武术大会的选手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奈尔知道以后\n',
            '说要去采访你们，\n',
            '然后就跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们没有遇见他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_368C(): pass

    label('loc_368C')

    Jump('loc_3F52')

    def _loc_368F(): pass

    label('loc_368F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3A02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3703',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始\n',
            '武术大会终于进入正式赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为要出特刊，\n',
            '所以本社的记者们\n',
            '一早就外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39FF')

    def _loc_3703(): pass

    label('loc_3703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3753',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔他啊，\n',
            '好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39FF')

    def _loc_3753(): pass

    label('loc_3753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_37F8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '从今天开始\n',
            '武术大会终于进入正式赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道诞辰庆典会如何，\n',
            '但肯定也会很热闹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为要出特刊，\n',
            '所以本社的记者们\n',
            '一早就外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39FF')

    def _loc_37F8(): pass

    label('loc_37F8')

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F啊，其实不是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来，\n',
            '他好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39FF(): pass

    label('loc_39FF')

    Jump('loc_3F52')

    def _loc_3A02(): pass

    label('loc_3A02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3CEB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3A59',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔他啊，\n',
            '好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CE8')

    def _loc_3A59(): pass

    label('loc_3A59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_3AD8',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然本刊刊登了\n',
            '女王陛下身体欠佳的报道，\n',
            '但这个消息确实缺乏可信度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '还是没有得到确凿的证明呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CE8')

    def _loc_3AD8(): pass

    label('loc_3AD8')

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F啊，这个嘛，\n',
            '其实不是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来，\n',
            '他好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CE8(): pass

    label('loc_3CE8')

    Jump('loc_3F52')

    def _loc_3CEB(): pass

    label('loc_3CEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3F52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3D42',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔他啊，\n',
            '好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F52')

    def _loc_3D42(): pass

    label('loc_3D42')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '哦，你们胸前的徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '莫非是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎？您是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从奈尔和朵洛希那里\n',
            '听说过很多你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F啊，这个嘛，\n',
            '其实不是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来，\n',
            '他好像又外出取材了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想短时间内\n',
            '他应该回不来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F52(): pass

    label('loc_3F52')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x3F56
@scena.Code('func_0E_3F56')
def func_0E_3F56():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4089',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3FE3',
    )

    ChrTalk(
        0x00FE,
        (
            '连游击士和亲卫队\n',
            '攻入城内的场面都有，\n',
            '这部分报道相当有魄力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来《利贝尔通讯》的发行量\n',
            '又要大幅上涨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4086')

    def _loc_3FE3(): pass

    label('loc_3FE3')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '很久没有看到过\n',
            '如此精彩的报道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连游击士和亲卫队\n',
            '攻入城内的场面都有，\n',
            '这部分报道相当有魄力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来《利贝尔通讯》的发行量\n',
            '又要大幅上涨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4086(): pass

    label('loc_4086')

    Jump('loc_4496')

    def _loc_4089(): pass

    label('loc_4089')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_40F8',
    )

    ChrTalk(
        0x00FE,
        (
            '这几天阅读了\n',
            '很多书籍和新闻，\n',
            '从中得到了不少启示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我们看不见的地方，\n',
            '似乎正有暗流涌动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_40F8(): pass

    label('loc_40F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4160',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得亲卫队的人们\n',
            '虽然有些作风古板……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那份自律和严谨\n',
            '看上去就让人心情很愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_4160(): pass

    label('loc_4160')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_41CE',
    )

    ChrTalk(
        0x00FE,
        (
            '关于女王病情的详情，\n',
            '现在也没有对外发表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '陛下本人也没有作出声明，\n',
            '我怀疑真的是生病了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_41CE(): pass

    label('loc_41CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4209',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～驱赶早上的睡意，\n',
            '还是喝杯咖啡最有效了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_4209(): pass

    label('loc_4209')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_423F',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '士兵为什么都那样\n',
            '粗暴不知礼节呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_423F(): pass

    label('loc_423F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4290',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，书籍是心灵的养料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要更加广泛地\n',
            '阅读各方面的书籍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_4290(): pass

    label('loc_4290')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_42F0',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的老板以前\n',
            '是外交使节的一员呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他好像去过帝国、共和国\n',
            '等等很多的国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_42F0(): pass

    label('loc_42F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_436F',
    )

    ChrTalk(
        0x00FE,
        (
            '我是属于那种只要知道\n',
            '比赛结果就满足了的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竞技场的人太多了，\n',
            '与其到那里去，\n',
            '还不如静静地在这里看看书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4496')

    def _loc_436F(): pass

    label('loc_436F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4439',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_43C9',
    )

    ChrTalk(
        0x00FE,
        (
            '最近的《利贝尔通讯》\n',
            '给人的感觉有些平淡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一点都不让人吃惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4436')

    def _loc_43C9(): pass

    label('loc_43C9')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '最近《利贝尔通讯》\n',
            '给人的感觉有些平淡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基本上都是\n',
            '普普通通的新闻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一点都不让人吃惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4436(): pass

    label('loc_4436')

    Jump('loc_4496')

    def _loc_4439(): pass

    label('loc_4439')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4496',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，这个地方很舒适嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里一边喝咖啡\n',
            '一边看书的话，\n',
            '时间很快就过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4496(): pass

    label('loc_4496')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x449A
@scena.Code('func_0F_449A')
def func_0F_449A():
    Call(2, 0x0010)

    Return()

# id: 0x0010 offset: 0x449F
@scena.Code('func_10_449F')
def func_10_449F():
    TalkBegin(0x0016)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '欢迎品尝「巨匠咖喱饭」1000米拉\n'),
            TXT(0x03, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_451C',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x62)
    OP_56(0x00)
    TalkEnd(0x0016)

    Return()

    def _loc_451C(): pass

    label('loc_451C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_461A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x3E8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_45E5',
    )

    SubMira(1000)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '巨匠咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFD, 1000)
    SetChrStatus(0x0001, 0xFD, 1000)
    SetChrStatus(0x0002, 0xFD, 1000)
    SetChrStatus(0x0003, 0xFD, 1000)
    SetChrStatus(0x0004, 0xFD, 1000)
    SetChrStatus(0x0005, 0xFD, 1000)
    SetChrStatus(0x0006, 0xFD, 1000)
    SetChrStatus(0x0007, 0xFD, 1000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45D7',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x000B)"),
            Expr.Return,
        ),
        'loc_45AF',
    )

    Jump('loc_45D7')

    def _loc_45AF(): pass

    label('loc_45AF')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '巨匠咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45D7(): pass

    label('loc_45D7')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_460B')

    def _loc_45E5(): pass

    label('loc_45E5')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_460B(): pass

    label('loc_460B')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0016)

    Return()

    def _loc_461A(): pass

    label('loc_461A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4634',
    )

    FadeIn(300, 0)
    TalkEnd(0x0016)

    Return()

    def _loc_4634(): pass

    label('loc_4634')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 7, 0x6F7)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B26',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0212)"),
            (Expr.Eval, "OP_40(0x0213)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0214)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0215)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0216)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0217)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0218)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0219)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x021A)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x021B)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x021C)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B26',
    )

    ChrTalk(
        0x0016,
        (
            '咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '……请问，\n',
            '难道你们有全部的《红耀石》吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '哦哦，果然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '每当有新的一卷出版，\n',
            '我都想在第一时间去买来看，\n',
            '可总是错过机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '现在总算完结了，\n',
            '我想从头到尾好好读一遍……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '可是现在到处\n',
            '都已经销售一空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '客人……\n',
            '请允许我提出一个无理的愿望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '能不能把整套书\n',
            '转让给我呢？',
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
        32,
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4810'),
        (0x00000001, 'loc_483D'),
        (-1, 'loc_485D'),
    )

    def _loc_4810(): pass

    label('loc_4810')

    SetScenaFlags(ScenaFlag(0x00DE, 7, 0x6F7))

    ChrTalk(
        0x0016,
        (
            '哦哦，是真的吗？\n',
            '太感谢你们了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_485D')

    def _loc_483D(): pass

    label('loc_483D')

    ChrTalk(
        0x0016,
        (
            '是吗……那也没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0016)

    Return()

    def _loc_485D(): pass

    label('loc_485D')

    ChrTalk(
        0x0016,
        (
            '我曾经作为外交使节\n',
            '被派遣到东方各国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '那个时候我买了不少\n',
            '引以为豪的东方收藏品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '我就从其中拿出一样\n',
            '作为书的还礼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '看起来客人们好像是游击士。\n',
            '对了…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '那就从这两样武器中\n',
            '选择一样你们喜欢的吧。',
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
        32,
        0,
        (
            TXT(0x00, '【太极棍】\n'),
            TXT(0x01, '【黑千鸟·白千鸟】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_499F'),
        (0x00000001, 'loc_4A08'),
        (-1, 'loc_4A7D'),
    )

    def _loc_499F(): pass

    label('loc_499F')

    ChrTalk(
        0x0101,
        (
            '#001F那我就要这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0011, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '太极棍',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_4A7D')

    def _loc_4A08(): pass

    label('loc_4A08')

    ChrTalk(
        0x0102,
        (
            '#010F那么，我就选这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0030, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '黑千鸟·白千鸟',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_4A7D')

    def _loc_4A7D(): pass

    label('loc_4A7D')

    ChrTalk(
        0x0016,
        (
            '哦哦，这个真是很适合你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '我打算从今天起\n',
            '早点关店停止营业，\n',
            '一口气把小说读完。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '非常感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x0212, 1)
    RemoveItem(0x0213, 1)
    RemoveItem(0x0214, 1)
    RemoveItem(0x0215, 1)
    RemoveItem(0x0216, 1)
    RemoveItem(0x0217, 1)
    RemoveItem(0x0218, 1)
    RemoveItem(0x0219, 1)
    RemoveItem(0x021A, 1)
    RemoveItem(0x021B, 1)
    RemoveItem(0x021C, 1)
    TalkEnd(0x0016)

    Return()

    def _loc_4B26(): pass

    label('loc_4B26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4BAE',
    )

    ChrTalk(
        0x0016,
        (
            '唉，\n',
            '没想到表面上是在召开武术大会，\n',
            '暗地里却是在策划政变。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '话说回来，\n',
            '像理查德上校这样的人\n',
            '怎么还会感到不满足呢。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5339')

    def _loc_4BAE(): pass

    label('loc_4BAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4CAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4C17',
    )

    ChrTalk(
        0x0016,
        (
            '我感到军队的警戒\n',
            '好像又提高了一个层次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '这件事事先也没有\n',
            '向我们市民通知一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CA9')

    def _loc_4C17(): pass

    label('loc_4C17')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x0016,
        (
            '王国军撤离之后，\n',
            '街上到处都有黑衣士兵在警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '这件事事先也没有\n',
            '向我们市民通知一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '虽然没有发生什么事情，\n',
            '但总是觉得有些不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CA9(): pass

    label('loc_4CA9')

    Jump('loc_5339')

    def _loc_4CAC(): pass

    label('loc_4CAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4DA6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4D15',
    )

    ChrTalk(
        0x0016,
        (
            '刚才来的特务兵\n',
            '嘴里嘟囔个不停……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '对于搜捕亲卫队的事，\n',
            '市民好像不是很配合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DA3')

    def _loc_4D15(): pass

    label('loc_4D15')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x0016,
        (
            '刚才来的特务兵\n',
            '嘴里嘟囔个不停……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '对于搜捕亲卫队的事，\n',
            '市民好像不是很配合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '呵呵，主要还是因为\n',
            '亲卫队平时很受大家欢迎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DA3(): pass

    label('loc_4DA3')

    Jump('loc_5339')

    def _loc_4DA6(): pass

    label('loc_4DA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4E10',
    )

    ChrTalk(
        0x0016,
        (
            '武术大会的优胜者\n',
            '好像已经产生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '王城里的利贝尔宫廷料理\n',
            '可都是十分丰盛的，好羡慕呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5339')

    def _loc_4E10(): pass

    label('loc_4E10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4EC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4E56',
    )

    ChrTalk(
        0x0016,
        (
            '各位客人要不要尝尝\n',
            '本店引以为荣的『浓缩咖啡』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EC2')

    def _loc_4E56(): pass

    label('loc_4E56')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x0016,
        (
            '你们好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '各位客人要不要尝尝\n',
            '本店引以为荣的『浓缩咖啡』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '对解除睡意非常有效哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EC2(): pass

    label('loc_4EC2')

    Jump('loc_5339')

    def _loc_4EC5(): pass

    label('loc_4EC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4FC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4F3B',
    )

    ChrTalk(
        0x0016,
        (
            '刚才来的士兵说什么\n',
            '晚上９点以后严禁外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '没办法，\n',
            '还是早些关店门，\n',
            '一边听音乐一边看书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4FC2')

    def _loc_4F3B(): pass

    label('loc_4F3B')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x0016,
        (
            '刚才，\n',
            '王国军的士兵们到店里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '他们说什么\n',
            '晚上９点以后严禁外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '没办法，\n',
            '还是早些关店门，\n',
            '一边听音乐一边看书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FC2(): pass

    label('loc_4FC2')

    Jump('loc_5339')

    def _loc_4FC5(): pass

    label('loc_4FC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_50A1',
    )

    ChrTalk(
        0x0016,
        (
            '这个西街区，\n',
            '在王都格兰赛尔的街区当中\n',
            '也算是相当安静的区域了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '为了要开这家店，\n',
            '我曾经到处寻找地方，\n',
            '最后发现还是这里最好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '或许是在城里工作久了，\n',
            '比起喧闹的场所，\n',
            '我还是偏爱温馨和平静的角落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5339')

    def _loc_50A1(): pass

    label('loc_50A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_51C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_5122',
    )

    ChrTalk(
        0x0016,
        (
            '我过去因为工作的关系\n',
            '到过好多的国家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '当时可以说\n',
            '吃遍了各国的美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '呵呵，饮食文化真是深奥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51C0')

    def _loc_5122(): pass

    label('loc_5122')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x0016,
        (
            '哎呀，我过去因为工作的关系\n',
            '去过好多的国家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '当时可以说\n',
            '吃遍了各国的美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '这里卖的咖喱饭\n',
            '就是其中一种哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '呵呵，饮食文化真是深奥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51C0(): pass

    label('loc_51C0')

    Jump('loc_5339')

    def _loc_51C3(): pass

    label('loc_51C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5233',
    )

    ChrTalk(
        0x0016,
        (
            '哟，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '本店会让顾客\n',
            '享受到宾至如归\n',
            '而又舒适悠闲的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '各位不要有任何拘束感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5339')

    def _loc_5233(): pass

    label('loc_5233')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_52AD',
    )

    ChrTalk(
        0x0016,
        (
            '旁边的建筑就是现在大受欢迎的\n',
            '《利贝尔通讯》的出版社办公楼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '那里的记者和编辑\n',
            '也常到这里来吃饭休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5339')

    def _loc_52AD(): pass

    label('loc_52AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5339',
    )

    ChrTalk(
        0x0016,
        (
            '你们，欢迎光临。\n',
            '这里是巴拉尔咖啡厅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '只要是与咖啡有关的，\n',
            '这里可以满足你们的各种需要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '请你们放松心情，\n',
            '好好享用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5339(): pass

    label('loc_5339')

    TalkEnd(0x0016)

    Return()

# id: 0x0011 offset: 0x533D
@scena.Code('func_11_533D')
def func_11_533D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_534A',
    )

    Jump('loc_546D')

    def _loc_534A(): pass

    label('loc_534A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_53A0',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '那么一会儿去吃冰淇淋如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我知道有一家店的\n',
            '冰淇淋很好吃哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_546D')

    def _loc_53A0(): pass

    label('loc_53A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_53CC',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典之前都没什么事做呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_546D')

    def _loc_53CC(): pass

    label('loc_53CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_542A',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '我觉得明年肯定会变回个人战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话～\n',
            '我只给约修亚君一个人加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_546D')

    def _loc_542A(): pass

    label('loc_542A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5434',
    )

    Jump('loc_546D')

    def _loc_5434(): pass

    label('loc_5434')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_543E',
    )

    Jump('loc_546D')

    def _loc_543E(): pass

    label('loc_543E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5448',
    )

    Jump('loc_546D')

    def _loc_5448(): pass

    label('loc_5448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5452',
    )

    Jump('loc_546D')

    def _loc_5452(): pass

    label('loc_5452')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_545C',
    )

    Jump('loc_546D')

    def _loc_545C(): pass

    label('loc_545C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5466',
    )

    Jump('loc_546D')

    def _loc_5466(): pass

    label('loc_5466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_546D',
    )

    def _loc_546D(): pass

    label('loc_546D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x5471
@scena.Code('func_12_5471')
def func_12_5471():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_547E',
    )

    Jump('loc_558A')

    def _loc_547E(): pass

    label('loc_547E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_54B6',
    )

    ChrTalk(
        0x00FE,
        (
            '超级不爽啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在要做些什么好呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_558A')

    def _loc_54B6(): pass

    label('loc_54B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_551A',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '诞辰庆典真的会如期举办吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我刚才去打听了一下～\n',
            '女王陛下似乎病了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_558A')

    def _loc_551A(): pass

    label('loc_551A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5547',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '洛伦斯大人竟然输掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_558A')

    def _loc_5547(): pass

    label('loc_5547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5551',
    )

    Jump('loc_558A')

    def _loc_5551(): pass

    label('loc_5551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_555B',
    )

    Jump('loc_558A')

    def _loc_555B(): pass

    label('loc_555B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5565',
    )

    Jump('loc_558A')

    def _loc_5565(): pass

    label('loc_5565')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_556F',
    )

    Jump('loc_558A')

    def _loc_556F(): pass

    label('loc_556F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5579',
    )

    Jump('loc_558A')

    def _loc_5579(): pass

    label('loc_5579')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5583',
    )

    Jump('loc_558A')

    def _loc_5583(): pass

    label('loc_5583')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_558A',
    )

    def _loc_558A(): pass

    label('loc_558A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x558E
@scena.Code('func_13_558E')
def func_13_558E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_559B',
    )

    Jump('loc_5644')

    def _loc_559B(): pass

    label('loc_559B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_55A5',
    )

    Jump('loc_5644')

    def _loc_55A5(): pass

    label('loc_55A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_55AF',
    )

    Jump('loc_5644')

    def _loc_55AF(): pass

    label('loc_55AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5601',
    )

    ChrTalk(
        0x00FE,
        (
            '金小组，\n',
            '优胜万岁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最后的最后，\n',
            '还是我支持的队伍取得了胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5644')

    def _loc_5601(): pass

    label('loc_5601')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_560B',
    )

    Jump('loc_5644')

    def _loc_560B(): pass

    label('loc_560B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5615',
    )

    Jump('loc_5644')

    def _loc_5615(): pass

    label('loc_5615')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_561F',
    )

    Jump('loc_5644')

    def _loc_561F(): pass

    label('loc_561F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5629',
    )

    Jump('loc_5644')

    def _loc_5629(): pass

    label('loc_5629')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5633',
    )

    Jump('loc_5644')

    def _loc_5633(): pass

    label('loc_5633')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_563D',
    )

    Jump('loc_5644')

    def _loc_563D(): pass

    label('loc_563D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5644',
    )

    def _loc_5644(): pass

    label('loc_5644')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x5648
@scena.Code('func_14_5648')
def func_14_5648():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5655',
    )

    Jump('loc_57A2')

    def _loc_5655(): pass

    label('loc_5655')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_565F',
    )

    Jump('loc_57A2')

    def _loc_565F(): pass

    label('loc_565F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5669',
    )

    Jump('loc_57A2')

    def _loc_5669(): pass

    label('loc_5669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_575F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_56D6',
    )

    ChrTalk(
        0x00FE,
        (
            '因为我和他都支持同一个小组，\n',
            '所以很合得来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比赛结束之后\n',
            '我们就来这里一起喝酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_575C')

    def _loc_56D6(): pass

    label('loc_56D6')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '因为我和他都支持同一个小组，\n',
            '所以很合得来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比赛结束之后\n',
            '我们就来这里一起喝酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天肯定也会彻夜狂欢吧。\n',
            '哈哈哈～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_575C(): pass

    label('loc_575C')

    Jump('loc_57A2')

    def _loc_575F(): pass

    label('loc_575F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5769',
    )

    Jump('loc_57A2')

    def _loc_5769(): pass

    label('loc_5769')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5773',
    )

    Jump('loc_57A2')

    def _loc_5773(): pass

    label('loc_5773')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_577D',
    )

    Jump('loc_57A2')

    def _loc_577D(): pass

    label('loc_577D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5787',
    )

    Jump('loc_57A2')

    def _loc_5787(): pass

    label('loc_5787')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5791',
    )

    Jump('loc_57A2')

    def _loc_5791(): pass

    label('loc_5791')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_579B',
    )

    Jump('loc_57A2')

    def _loc_579B(): pass

    label('loc_579B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_57A2',
    )

    def _loc_57A2(): pass

    label('loc_57A2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x57A6
@scena.Code('func_15_57A6')
def func_15_57A6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_57B3',
    )

    Jump('loc_5B1D')

    def _loc_57B3(): pass

    label('loc_57B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_57BD',
    )

    Jump('loc_5B1D')

    def _loc_57BD(): pass

    label('loc_57BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_57C7',
    )

    Jump('loc_5B1D')

    def _loc_57C7(): pass

    label('loc_57C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_57D1',
    )

    Jump('loc_5B1D')

    def _loc_57D1(): pass

    label('loc_57D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_57DB',
    )

    Jump('loc_5B1D')

    def _loc_57DB(): pass

    label('loc_57DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5957',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5804',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_5835')

    def _loc_5804(): pass

    label('loc_5804')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_581A',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_5835')

    def _loc_581A(): pass

    label('loc_581A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5830',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_5835')

    def _loc_5830(): pass

    label('loc_5830')

    SetChrSubChip(0x00FE, 0)

    def _loc_5835(): pass

    label('loc_5835')

    SetChrDirection(0x00FE, 0, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_58C1',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040141621V#037F哎呀，\n',
            '和雪拉君可不是在这样的\n',
            '节奏和气氛下喝酒呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141620V和她喝酒的时候，\n',
            '总有一种欲生欲死的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_594F')

    def _loc_58C1(): pass

    label('loc_58C1')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#0040141618V#037F哈·哈·哈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141619V哎呀～\n',
            '和雪拉君可不是在这样的\n',
            '节奏和气氛下喝酒呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141620V和她喝酒的时候，\n',
            '总有一种欲生欲死的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_594F(): pass

    label('loc_594F')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_5B1D')

    def _loc_5957(): pass

    label('loc_5957')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5961',
    )

    Jump('loc_5B1D')

    def _loc_5961(): pass

    label('loc_5961')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5ABC',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_598A',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_59BB')

    def _loc_598A(): pass

    label('loc_598A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_59A0',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_59BB')

    def _loc_59A0(): pass

    label('loc_59A0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_59B6',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_59BB')

    def _loc_59B6(): pass

    label('loc_59B6')

    SetChrSubChip(0x00FE, 0)

    def _loc_59BB(): pass

    label('loc_59BB')

    SetChrDirection(0x00FE, 0, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_5A2E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040141626V#037F呵，食物可以滋润心灵，\n',
            '创造生命……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141627V哎呀呀，\n',
            '厨师真是伟大的存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AB4')

    def _loc_5A2E(): pass

    label('loc_5A2E')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#0040141623V#037F哈·哈·哈，\n',
            '夜幕降临了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141624V来吧，继续畅饮吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141625V#509F奥利维尔明明这么瘦，\n',
            '为什么能装下那么多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AB4(): pass

    label('loc_5AB4')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_5B1D')

    def _loc_5ABC(): pass

    label('loc_5ABC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5AC6',
    )

    Jump('loc_5B1D')

    def _loc_5AC6(): pass

    label('loc_5AC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5B16',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_5B13',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040141628V#038F唔，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141629V青春诚短暂，恋爱吧少女……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B13(): pass

    label('loc_5B13')

    Jump('loc_5B1D')

    def _loc_5B16(): pass

    label('loc_5B16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5B1D',
    )

    def _loc_5B1D(): pass

    label('loc_5B1D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x5B21
@scena.Code('func_16_5B21')
def func_16_5B21():
    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B46',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_5B61')

    def _loc_5B46(): pass

    label('loc_5B46')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B5C',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_5B61')

    def _loc_5B5C(): pass

    label('loc_5B5C')

    SetChrSubChip(0x00FE, 2)

    def _loc_5B61(): pass

    label('loc_5B61')

    SetChrDirection(0x00FE, 180, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5E59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_5BE3',
    )

    ChrTalk(
        0x0010,
        (
            '#0080140711V#070F我打算暂时留在这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140712V难得来到这里，\n',
            '等和各位高手较量过之后\n',
            '再回国也不迟嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E56')

    def _loc_5BE3(): pass

    label('loc_5BE3')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x00DD, 7, 0x6EF))

    ChrTalk(
        0x0010,
        (
            '#0080140697V#073F哟，是你们俩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140698V#010F金大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140699V#000F对了，\n',
            '金大哥你接下来准备做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140700V真的要回去共和国吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080140701V#070F不，\n',
            '在共和国没有发生什么大事，\n',
            '我准备在这儿呆一段时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140702V这个国家有几位\n',
            '很著名的年轻游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140703V#071F难得来一趟，\n',
            '等和他们切磋了技艺之后\n',
            '再回国也不迟嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140704V#505F著名的游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080140705V#074F是啊……\n',
            '首先是对面的『重剑阿加特』，\n',
            '然后是『银闪雪拉扎德』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140706V而且……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140707V#070F一定得和你们俩也较量一下才行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140708V#008F哇，这真有些难为情啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140709V#006F不过，我很期待！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140710V#010F到时候还要请您手下留情。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E56(): pass

    label('loc_5E56')

    Jump('loc_6007')

    def _loc_5E59(): pass

    label('loc_5E59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5E63',
    )

    Jump('loc_6007')

    def _loc_5E63(): pass

    label('loc_5E63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5E6D',
    )

    Jump('loc_6007')

    def _loc_5E6D(): pass

    label('loc_5E6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5E77',
    )

    Jump('loc_6007')

    def _loc_5E77(): pass

    label('loc_5E77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5E81',
    )

    Jump('loc_6007')

    def _loc_5E81(): pass

    label('loc_5E81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5ED1',
    )

    ChrTalk(
        0x0010,
        (
            '#0080111471V#078F明天就是决赛了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111472V记得多吃点，睡个好觉哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6007')

    def _loc_5ED1(): pass

    label('loc_5ED1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5EDB',
    )

    Jump('loc_6007')

    def _loc_5EDB(): pass

    label('loc_5EDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5FEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_5F1B',
    )

    ChrTalk(
        0x0010,
        (
            '#0080111478V#079F嗝，怎么样？\n',
            '你们也来喝吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FE9')

    def _loc_5F1B(): pass

    label('loc_5F1B')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0010,
        (
            '#0080111473V#079F哦哦～！\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111474V怎么样？\n',
            '你们也来喝吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111475V#509F我们可是未成年人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0081040006V#076F什么，不愿喝我的酒吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111477V#019F哈哈，\n',
            '好像已经完全喝醉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FE9(): pass

    label('loc_5FE9')

    Jump('loc_6007')

    def _loc_5FEC(): pass

    label('loc_5FEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5FF6',
    )

    Jump('loc_6007')

    def _loc_5FF6(): pass

    label('loc_5FF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6000',
    )

    Jump('loc_6007')

    def _loc_6000(): pass

    label('loc_6000')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_6007',
    )

    def _loc_6007(): pass

    label('loc_6007')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x6010
@scena.Code('func_17_6010')
def func_17_6010():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_611C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_6091',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然是理查德上校\n',
            '策动的这起政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前接受杂志的访谈\n',
            '说的那些了不起的话，\n',
            '也只是表面文章而已吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6119')

    def _loc_6091(): pass

    label('loc_6091')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '竟然是理查德上校\n',
            '策动的这起政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前接受杂志的访谈\n',
            '说的那些了不起的话，\n',
            '也只是表面文章而已吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想到就觉得震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6119(): pass

    label('loc_6119')

    Jump('loc_682E')

    def _loc_611C(): pass

    label('loc_611C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_616B',
    )

    ChrTalk(
        0x00FE,
        (
            '街上全是黑衣士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么要把以往的\n',
            '那些士兵们替换掉了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_616B(): pass

    label('loc_616B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_61CD',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典马上就到了，\n',
            '王城里面如果能快点\n',
            '发布公告就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要这样就中止啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_61CD(): pass

    label('loc_61CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6245',
    )

    ChrTalk(
        0x00FE,
        (
            '大会明明都结束了，\n',
            '士兵的数量却一点也没有减少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下又身体欠佳，\n',
            '最近怎么总是令人讨厌的消息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_6245(): pass

    label('loc_6245')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6336',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_62B8',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天晚上满街都是士兵，\n',
            '回家的时候被他们叫住了四次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道我的样子\n',
            '真的像是一个坏人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6333')

    def _loc_62B8(): pass

    label('loc_62B8')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上满街都是士兵，\n',
            '回家的时候被他们叫住了四次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道我的样子\n',
            '真的像是一个坏人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人泄气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6333(): pass

    label('loc_6333')

    Jump('loc_682E')

    def _loc_6336(): pass

    label('loc_6336')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_63B7',
    )

    ChrTalk(
        0x00FE,
        (
            '自从《利贝尔通讯》刊登采访以来，\n',
            '理查德上校的人气\n',
            '最近一段时间急剧上升啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论男女老少，\n',
            '支持他的人都很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_63B7(): pass

    label('loc_63B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6423',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然『巴拉尔』咖啡厅的\n',
            '帝国风味早点也很不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我更喜欢这个店里的\n',
            '利贝尔风味的早餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_6423(): pass

    label('loc_6423')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_6525',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_6496',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '难道说造成柏斯混乱的空贼\n',
            '也参加了比武大会吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们不在监狱服役，这样好吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6522')

    def _loc_6496(): pass

    label('loc_6496')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '难道说造成柏斯混乱的空贼\n',
            '也参加了比武大会吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他们的确很有实力，\n',
            '比赛也很有意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是不在监狱服役好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6522(): pass

    label('loc_6522')

    Jump('loc_682E')

    def _loc_6525(): pass

    label('loc_6525')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6684',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_65BF',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会原本是军人用来\n',
            '展示武技和进行演习的活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从现在的女王陛下继位以来，\n',
            '就逐渐转变成普通民众\n',
            '也可以参与的开放式比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6681')

    def _loc_65BF(): pass

    label('loc_65BF')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '武术大会原本是军人用来\n',
            '展示武技和进行演习的活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从现在的女王陛下继位以来，\n',
            '就逐渐转变成普通民众\n',
            '也可以参与的开放式比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那个时候开始，\n',
            '普通民众也可以\n',
            '报名参加大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6681(): pass

    label('loc_6681')

    Jump('loc_682E')

    def _loc_6684(): pass

    label('loc_6684')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_66B3',
    )

    ChrTalk(
        0x00FE,
        (
            '哎哟，吓得我\n',
            '被通心粉给哽住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_66B3(): pass

    label('loc_66B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_671C',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会变更为团体赛，\n',
            '这还是头一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是那个\n',
            '差劲公爵出的主意，\n',
            '不过也算挺有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_671C(): pass

    label('loc_671C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_682E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_6788',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队因为有制造恐怖活动的嫌疑，\n',
            '正在被王国军追捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这类事情还真是接连不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_682E')

    def _loc_6788(): pass

    label('loc_6788')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '亲卫队因为有制造恐怖活动的嫌疑，\n',
            '正在被王国军追捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯的空贼带来的混乱，\n',
            '卢安的市长被捕事件，\n',
            '蔡斯的导力停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这类事情还真是接连不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_682E(): pass

    label('loc_682E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x6832
@scena.Code('func_18_6832')
def func_18_6832():
    Call(2, 0x0019)

    Return()

# id: 0x0019 offset: 0x6837
@scena.Code('func_19_6837')
def func_19_6837():
    TalkBegin(0x000E)
    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6847',
    )

    Jump('loc_6851')

    def _loc_6847(): pass

    label('loc_6847')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6851',
    )

    ClearScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    def _loc_6851(): pass

    label('loc_6851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_69EA',
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '欢迎品尝「劲霸浓鱼汤」1000米拉\n'),
            TXT(0x03, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_68D2',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x61)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_68D2(): pass

    label('loc_68D2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69D0',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x3E8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_699B',
    )

    SubMira(1000)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '劲霸浓鱼汤',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFD, 1000)
    SetChrStatus(0x0001, 0xFD, 1000)
    SetChrStatus(0x0002, 0xFD, 1000)
    SetChrStatus(0x0003, 0xFD, 1000)
    SetChrStatus(0x0004, 0xFD, 1000)
    SetChrStatus(0x0005, 0xFD, 1000)
    SetChrStatus(0x0006, 0xFD, 1000)
    SetChrStatus(0x0007, 0xFD, 1000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_698D',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0002)"),
            Expr.Return,
        ),
        'loc_6965',
    )

    Jump('loc_698D')

    def _loc_6965(): pass

    label('loc_6965')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '劲霸浓鱼汤',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_698D(): pass

    label('loc_698D')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_69C1')

    def _loc_699B(): pass

    label('loc_699B')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_69C1(): pass

    label('loc_69C1')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000E)

    Return()

    def _loc_69D0(): pass

    label('loc_69D0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_69EA',
    )

    FadeIn(300, 0)
    TalkEnd(0x000E)

    Return()

    def _loc_69EA(): pass

    label('loc_69EA')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_6AD0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_6A3B',
    )

    ChrTalk(
        0x000E,
        (
            '虽然发生了许多事情，\n',
            '但现在终于可以平静地生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6ACD')

    def _loc_6A3B(): pass

    label('loc_6A3B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000E,
        (
            '看到女王陛下健康的样子，\n',
            '我就放心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '亲卫队的嫌疑\n',
            '也只是被人嫁祸了而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然发生了许多事情，\n',
            '但现在终于可以平静地生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6ACD(): pass

    label('loc_6ACD')

    Jump('loc_7092')

    def _loc_6AD0(): pass

    label('loc_6AD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_6B46',
    )

    ChrTalk(
        0x000E,
        (
            '这几位士兵好像也对\n',
            '当前的状况不太清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过就算发生了什么事情，\n',
            '也不会那么容易就让我们知晓的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_6B46(): pass

    label('loc_6B46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6BC5',
    )

    ChrTalk(
        0x000E,
        (
            '武术大会虽然结束了，\n',
            '但士兵的数量一点都不见减少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '亲卫队的人策划了\n',
            '这次的恐怖事件的说法\n',
            '果然是真的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_6BC5(): pass

    label('loc_6BC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6C20',
    )

    ChrTalk(
        0x000E,
        (
            '今天奥利维尔先生没有来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '听说他们取得了优胜，\n',
            '本来想特地庆贺一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_6C20(): pass

    label('loc_6C20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6C8F',
    )

    ChrTalk(
        0x000E,
        (
            '啊～\n',
            '我也想去竞技场看比赛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '干我们这种工作，\n',
            '在别人在玩乐的时候，\n',
            '自己却非要工作不可啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_6C8F(): pass

    label('loc_6C8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6D1D',
    )

    ChrTalk(
        0x000E,
        (
            '刚才，\n',
            '王国军的人来了，\n',
            '告诉我说只能营业到晚上９点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '唉～\n',
            '难得最近的生意那么好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '９点就关门的话，\n',
            '酒廊就名不副实了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_6D1D(): pass

    label('loc_6D1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6D94',
    )

    ChrTalk(
        0x000E,
        (
            '奥利维尔先生，\n',
            '你们今天要参加武术大会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我往年支持的亲卫队\n',
            '今年不能来参加，\n',
            '所以就给你们加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_6D94(): pass

    label('loc_6D94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_6DD9',
    )

    ChrTalk(
        0x000E,
        (
            '第一天的比赛\n',
            '好像已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '结果究竟如何呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_6DD9(): pass

    label('loc_6DD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6EF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_6E22',
    )

    ChrTalk(
        0x000E,
        (
            '你们都是奥利维尔先生的朋友吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '比赛要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6EF1')

    def _loc_6E22(): pass

    label('loc_6E22')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000E, 0x0104, 0)

    ChrTalk(
        0x000E,
        (
            '哎呀，奥利维尔先生，\n',
            '昨天撞到的头没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F哈·哈·哈，你看呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#030F我那充满世间博爱的热烈心跳\n',
            '将会持续到永恒的那一刻。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯，看来是没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000E, 180, 400)

    def _loc_6EF1(): pass

    label('loc_6EF1')

    Jump('loc_7092')

    def _loc_6EF4(): pass

    label('loc_6EF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6FAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_6F71',
    )

    ChrTalk(
        0x000E,
        (
            '哎呀……仔细看看，\n',
            '这不是经常在这里演奏的奥利维尔先生吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '又是因为对女性纠缠不休\n',
            '而被打飞的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6FAA')

    def _loc_6F71(): pass

    label('loc_6F71')

    ChrTalk(
        0x000E,
        (
            '大会的预选赛好像已经结束了。\n',
            '这里客人立刻多了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6FAA(): pass

    label('loc_6FAA')

    Jump('loc_7092')

    def _loc_6FAD(): pass

    label('loc_6FAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_7092',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_700A',
    )

    ChrTalk(
        0x000E,
        (
            '说亲卫队的人是\n',
            '恐怖分子什么的，\n',
            '我难以相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '肯定是哪里搞错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7092')

    def _loc_700A(): pass

    label('loc_700A')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000E,
        (
            '说亲卫队的人是\n',
            '恐怖分子什么的，\n',
            '我难以相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽说他们很少到这里来，\n',
            '但我知道他们都是很正直的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '肯定是哪里搞错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7092(): pass

    label('loc_7092')

    TalkEnd(0x000E)

    Return()

# id: 0x001A offset: 0x7096
@scena.Code('func_1A_7096')
def func_1A_7096():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_728D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7122',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330140728V#840F立下了那么多功绩，\n',
            '你们俩现在已经是\n',
            '优秀的正游击士了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330140723V不要就此满足，\n',
            '要向更高的目标发起冲击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_728D')

    def _loc_7122(): pass

    label('loc_7122')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0330140721V#840F哟，\n',
            '这回的事件解决得不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330140722V立下了那么多功绩，\n',
            '你们俩现在已经是\n',
            '优秀的正游击士了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330140723V不要就此满足，\n',
            '要向更高的目标发起冲击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140724V#000F嘿嘿，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140725V#010F克鲁茨大哥，\n',
            '你的身体已经没什么大碍了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330140726V#841F啊，\n',
            '你看看，棒得很啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330140727V#845F遗憾的是……\n',
            '到底是谁消除了我的记忆，\n',
            '我怎么也想不起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_728D(): pass

    label('loc_728D')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x7291
@scena.Code('func_1B_7291')
def func_1B_7291():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_76ED',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 4660, 0, 540, 90)
    SetChrPos(0x0102, 4870, 0, -630, 45)
    SetChrPos(0x0108, 3570, 0, 140, 90)
    SetChrSubChip(0x000C, 0)
    ChrTurnDirection(0x000C, 0x0108, 0)
    SetScenaFlags(ScenaFlag(0x00C9, 2, 0x64A))
    OP_28(0x004B, 0x01, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0020)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0040)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0080)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7318',
    )

    OP_28(0x004B, 0x01, 0x0100)

    def _loc_7318(): pass

    label('loc_7318')

    CameraMove(5350, 0, 360, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010130100V#006F库拉茨大哥，终于找到你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0310130101V#820F哦……\n',
            '优胜组出现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310130102V晚宴后不是在城里住得好好的吗。\n',
            '怎么这么快就回来了啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310130103V想必一定是吃了\n',
            '不少美味佳肴吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130104V#007F的确是很美味……\n',
            '不过美味的同时事情却是不简单啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0310130105V#820F事情却是不简单？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向库拉茨说明了\n',
            '至今为止发生的事情和女王的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000C,
        (
            '#0310130106V#822F…………………………\n',
            '……喂喂，没搞错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130107V#072F很遗憾，确实是真的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130108V我可以用我的称号作为担保。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0310130109V#824F『不动金』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310130110V你所担保的事情\n',
            '肯定是勿庸置疑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310130111V#823F好，我明白了，\n',
            '让我也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130112V#006F谢谢你，库拉茨大哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130113V#012F首先要召开作战会议，\n',
            '请到游击士协会去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130114V大家都会集中在那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0310130115V#822F明白了，待会儿见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7648')
    def lambda_7648():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_7648')

    DispatchAsync2(0x0101, 0x0001, lambda_7648)

    @scena.Lambda('lambda_7659')
    def lambda_7659():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_7659')

    DispatchAsync2(0x0102, 0x0001, lambda_7659)

    @scena.Lambda('lambda_766A')
    def lambda_766A():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_766A')

    DispatchAsync2(0x0108, 0x0001, lambda_766A)

    ChrWalkTo(0x000C, 5630, 0, -1470, 4000, 0x00)
    ChrWalkTo(0x000C, 1880, 0, -1480, 4000, 0x00)
    ChrWalkTo(0x000C, 710, 0, -5490, 4000, 0x00)

    @scena.Lambda('lambda_76B7')
    def lambda_76B7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_76B7)

    ChrWalkTo(0x000C, 710, -250, -7470, 4000, 0x00)
    SetChrFlags(0x000C, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    EventEnd(0x00)

    Jump('loc_7C06')

    def _loc_76ED(): pass

    label('loc_76ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_7902',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7752',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310140740V我们以后可能就要\n',
            '#820F一起执行任务了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310140739V到时候还要多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_78FF')

    def _loc_7752(): pass

    label('loc_7752')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0310140730V#821F哟，英雄们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140731V#000F库拉茨大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310140732V#821F你们两个干得真漂亮。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310140733V竟然还只是准游击士，\n',
            '简直不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140734V#001F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140735V#000F其实这是大家共同努力\n',
            '所换回来的美好结果呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140736V#505F到了最后还是老爸出手相助的，\n',
            '我们的本领还没到家啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310140737V#820F……说真的，\n',
            '你们已经做得很好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310140738V我们以后可能就要\n',
            '一起执行任务了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310140739V到时候还要多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_78FF(): pass

    label('loc_78FF')

    Jump('loc_7C06')

    def _loc_7902(): pass

    label('loc_7902')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_790C',
    )

    Jump('loc_7C06')

    def _loc_790C(): pass

    label('loc_790C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_7916',
    )

    Jump('loc_7C06')

    def _loc_7916(): pass

    label('loc_7916')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_7A28',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_797A',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310111961V#821F咦？\n',
            '那个金发的兄弟到哪里去了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310111962V他的枪法\n',
            '有相当的水准呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7A25')

    def _loc_797A(): pass

    label('loc_797A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0310111963V#821F哦哦，\n',
            '这不是优胜组的成员吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310111964V今天的比赛，\n',
            '我们都认真地观摩了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310111953V虽然说我们也想取得优胜，\n',
            '不过这个冠军让你们拿了\n',
            '我们一点也没觉得遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7A25(): pass

    label('loc_7A25')

    Jump('loc_7C06')

    def _loc_7A28(): pass

    label('loc_7A28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_7A32',
    )

    Jump('loc_7C06')

    def _loc_7A32(): pass

    label('loc_7A32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_7A3C',
    )

    Jump('loc_7C06')

    def _loc_7A3C(): pass

    label('loc_7A3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_7A46',
    )

    Jump('loc_7C06')

    def _loc_7A46(): pass

    label('loc_7A46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_7A50',
    )

    Jump('loc_7C06')

    def _loc_7A50(): pass

    label('loc_7A50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_7BF5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7AA4',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310111945V就算是游击士，\n',
            '也要保证良好的睡眠，\n',
            '早饭也要吃好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BF2')

    def _loc_7AA4(): pass

    label('loc_7AA4')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0310111943V哟，\n',
            '你们也是来吃早饭的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111944V#000F啊，是库拉茨大哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111945V就算是游击士，\n',
            '也要保证良好的睡眠，\n',
            '早饭也要吃好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111946V你们在协会的研修中也学了吧。\n',
            '如果没有休息好，判断力和身体都会迟钝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111947V#010F哈哈，\n',
            '艾丝蒂尔只有对这一点是完全理解的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111948V#000F喂……\n',
            '那个『只有』是什么意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BF2(): pass

    label('loc_7BF2')

    Jump('loc_7C06')

    def _loc_7BF5(): pass

    label('loc_7BF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_7BFF',
    )

    Jump('loc_7C06')

    def _loc_7BFF(): pass

    label('loc_7BFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_7C06',
    )

    def _loc_7C06(): pass

    label('loc_7C06')

    TalkEnd(0x000C)

    Return()

# id: 0x001C offset: 0x7C0A
@scena.Code('func_1C_7C0A')
def func_1C_7C0A():
    TalkBegin(0x0020)

    ChrTalk(
        0x00FE,
        (
            '到底是怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是被马踢了一脚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0020)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
