import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4130_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4130_2 ._SN')

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
    Return()

# id: 0x0001 offset: 0x65
@scena.Code('func_01_65')
def func_01_65():
    Return()

# id: 0x0002 offset: 0x66
@scena.Code('func_02_66')
def func_02_66():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
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

    ChrSetSubChip(0x00FE, 2)

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

    ChrSetSubChip(0x00FE, 1)

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

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_BC')

    def _loc_B7(): pass

    label('loc_B7')

    ChrSetSubChip(0x00FE, 2)

    def _loc_BC(): pass

    label('loc_BC')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_137',
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

    Jump('loc_2FE')

    def _loc_137(): pass

    label('loc_137')

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

    def _loc_2FE(): pass

    label('loc_2FE')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x307
@scena.Code('func_03_307')
def func_03_307():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_32C',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_35D')

    def _loc_32C(): pass

    label('loc_32C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_342',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_35D')

    def _loc_342(): pass

    label('loc_342')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_358',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_35D')

    def _loc_358(): pass

    label('loc_358')

    ChrSetSubChip(0x00FE, 1)

    def _loc_35D(): pass

    label('loc_35D')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_3FF',
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

    Jump('loc_5BA')

    def _loc_3FF(): pass

    label('loc_3FF')

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

    def _loc_5BA(): pass

    label('loc_5BA')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x5C3
@scena.Code('func_04_5C3')
def func_04_5C3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_620',
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

    Jump('loc_757')

    def _loc_620(): pass

    label('loc_620')

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

    def _loc_757(): pass

    label('loc_757')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x75B
@scena.Code('func_05_75B')
def func_05_75B():
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

# id: 0x0006 offset: 0x7CB
@scena.Code('func_06_7CB')
def func_06_7CB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_82C',
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

    Jump('loc_8A2')

    def _loc_82C(): pass

    label('loc_82C')

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

    def _loc_8A2(): pass

    label('loc_8A2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x8A6
@scena.Code('func_07_8A6')
def func_07_8A6():
    Call(2, 0x0008)

    Return()

# id: 0x0008 offset: 0x8AB
@scena.Code('func_08_8AB')
def func_08_8AB():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_944',
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

    Jump('loc_F22')

    def _loc_944(): pass

    label('loc_944')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_993',
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

    Jump('loc_F22')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_A35',
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

    Jump('loc_F22')

    def _loc_A35(): pass

    label('loc_A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_A9F',
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

    Jump('loc_F22')

    def _loc_A9F(): pass

    label('loc_A9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_B7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_AFE',
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

    Jump('loc_B7C')

    def _loc_AFE(): pass

    label('loc_AFE')

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

    def _loc_B7C(): pass

    label('loc_B7C')

    Jump('loc_F22')

    def _loc_B7F(): pass

    label('loc_B7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_BD9',
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

    Jump('loc_F22')

    def _loc_BD9(): pass

    label('loc_BD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_CDE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_C34',
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

    Jump('loc_CDB')

    def _loc_C34(): pass

    label('loc_C34')

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

    def _loc_CDB(): pass

    label('loc_CDB')

    Jump('loc_F22')

    def _loc_CDE(): pass

    label('loc_CDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_D4F',
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

    Jump('loc_F22')

    def _loc_D4F(): pass

    label('loc_D4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_DDB',
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

    Jump('loc_F22')

    def _loc_DDB(): pass

    label('loc_DDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_E41',
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

    Jump('loc_F22')

    def _loc_E41(): pass

    label('loc_E41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_F22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_E92',
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

    Jump('loc_F22')

    def _loc_E92(): pass

    label('loc_E92')

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

    def _loc_F22(): pass

    label('loc_F22')

    TalkEnd(0x001A)

    Return()

# id: 0x0009 offset: 0xF26
@scena.Code('func_09_F26')
def func_09_F26():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_F94',
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

    Jump('loc_16DC')

    def _loc_F94(): pass

    label('loc_F94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1050',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_FE5',
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

    Jump('loc_104D')

    def _loc_FE5(): pass

    label('loc_FE5')

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

    def _loc_104D(): pass

    label('loc_104D')

    Jump('loc_16DC')

    def _loc_1050(): pass

    label('loc_1050')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1146',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_10C1',
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

    Jump('loc_1143')

    def _loc_10C1(): pass

    label('loc_10C1')

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

    def _loc_1143(): pass

    label('loc_1143')

    Jump('loc_16DC')

    def _loc_1146(): pass

    label('loc_1146')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_126B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_11C2',
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

    Jump('loc_1268')

    def _loc_11C2(): pass

    label('loc_11C2')

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

    def _loc_1268(): pass

    label('loc_1268')

    Jump('loc_16DC')

    def _loc_126B(): pass

    label('loc_126B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_139E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_12E4',
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

    Jump('loc_139B')

    def _loc_12E4(): pass

    label('loc_12E4')

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

    def _loc_139B(): pass

    label('loc_139B')

    Jump('loc_16DC')

    def _loc_139E(): pass

    label('loc_139E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_148D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_13FD',
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

    Jump('loc_148A')

    def _loc_13FD(): pass

    label('loc_13FD')

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

    def _loc_148A(): pass

    label('loc_148A')

    Jump('loc_16DC')

    def _loc_148D(): pass

    label('loc_148D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1587',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_14F2',
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

    Jump('loc_1584')

    def _loc_14F2(): pass

    label('loc_14F2')

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

    def _loc_1584(): pass

    label('loc_1584')

    Jump('loc_16DC')

    def _loc_1587(): pass

    label('loc_1587')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1591',
    )

    Jump('loc_16DC')

    def _loc_1591(): pass

    label('loc_1591')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_15EB',
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

    Jump('loc_16DC')

    def _loc_15EB(): pass

    label('loc_15EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1676',
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

    Jump('loc_16DC')

    def _loc_1676(): pass

    label('loc_1676')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_16DC',
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

    def _loc_16DC(): pass

    label('loc_16DC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x16E0
@scena.Code('func_0A_16E0')
def func_0A_16E0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_174E',
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

    Jump('loc_1E10')

    def _loc_174E(): pass

    label('loc_174E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1774',
    )

    ChrTalk(
        0x00FE,
        (
            '街上的情况很奇怪呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E10')

    def _loc_1774(): pass

    label('loc_1774')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_17F6',
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

    Jump('loc_1E10')

    def _loc_17F6(): pass

    label('loc_17F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_18F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1853',
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

    Jump('loc_18EF')

    def _loc_1853(): pass

    label('loc_1853')

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

    def _loc_18EF(): pass

    label('loc_18EF')

    Jump('loc_1E10')

    def _loc_18F2(): pass

    label('loc_18F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1966',
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

    Jump('loc_1E10')

    def _loc_1966(): pass

    label('loc_1966')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1A93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_19F3',
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

    Jump('loc_1A90')

    def _loc_19F3(): pass

    label('loc_19F3')

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

    def _loc_1A90(): pass

    label('loc_1A90')

    Jump('loc_1E10')

    def _loc_1A93(): pass

    label('loc_1A93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1B75',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1AF4',
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

    Jump('loc_1B72')

    def _loc_1AF4(): pass

    label('loc_1AF4')

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

    def _loc_1B72(): pass

    label('loc_1B72')

    Jump('loc_1E10')

    def _loc_1B75(): pass

    label('loc_1B75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1BEF',
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

    Jump('loc_1E10')

    def _loc_1BEF(): pass

    label('loc_1BEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1CAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1C43',
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

    Jump('loc_1CAB')

    def _loc_1C43(): pass

    label('loc_1C43')

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

    def _loc_1CAB(): pass

    label('loc_1CAB')

    Jump('loc_1E10')

    def _loc_1CAE(): pass

    label('loc_1CAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1DA5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1D0F',
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

    Jump('loc_1DA2')

    def _loc_1D0F(): pass

    label('loc_1D0F')

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

    def _loc_1DA2(): pass

    label('loc_1DA2')

    Jump('loc_1E10')

    def _loc_1DA5(): pass

    label('loc_1DA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1E10',
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

    def _loc_1E10(): pass

    label('loc_1E10')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1E14
@scena.Code('func_0B_1E14')
def func_0B_1E14():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2048',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1E9E',
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

    Jump('loc_2045')

    def _loc_1E9E(): pass

    label('loc_1E9E')

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

    def _loc_2045(): pass

    label('loc_2045')

    Jump('loc_2238')

    def _loc_2048(): pass

    label('loc_2048')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_208F',
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

    Jump('loc_2238')

    def _loc_208F(): pass

    label('loc_208F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_20EB',
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

    Jump('loc_2238')

    def _loc_20EB(): pass

    label('loc_20EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_21F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_215C',
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

    Jump('loc_21F2')

    def _loc_215C(): pass

    label('loc_215C')

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

    def _loc_21F2(): pass

    label('loc_21F2')

    Jump('loc_2238')

    def _loc_21F5(): pass

    label('loc_21F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_21FF',
    )

    Jump('loc_2238')

    def _loc_21FF(): pass

    label('loc_21FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2209',
    )

    Jump('loc_2238')

    def _loc_2209(): pass

    label('loc_2209')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2213',
    )

    Jump('loc_2238')

    def _loc_2213(): pass

    label('loc_2213')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_221D',
    )

    Jump('loc_2238')

    def _loc_221D(): pass

    label('loc_221D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2227',
    )

    Jump('loc_2238')

    def _loc_2227(): pass

    label('loc_2227')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2231',
    )

    Jump('loc_2238')

    def _loc_2231(): pass

    label('loc_2231')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2238',
    )

    def _loc_2238(): pass

    label('loc_2238')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x223C
@scena.Code('func_0C_223C')
def func_0C_223C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2415',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_22D1',
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

    Jump('loc_2412')

    def _loc_22D1(): pass

    label('loc_22D1')

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

    def _loc_2412(): pass

    label('loc_2412')

    Jump('loc_2476')

    def _loc_2415(): pass

    label('loc_2415')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_241F',
    )

    Jump('loc_2476')

    def _loc_241F(): pass

    label('loc_241F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2429',
    )

    Jump('loc_2476')

    def _loc_2429(): pass

    label('loc_2429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2433',
    )

    Jump('loc_2476')

    def _loc_2433(): pass

    label('loc_2433')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_243D',
    )

    Jump('loc_2476')

    def _loc_243D(): pass

    label('loc_243D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2447',
    )

    Jump('loc_2476')

    def _loc_2447(): pass

    label('loc_2447')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2451',
    )

    Jump('loc_2476')

    def _loc_2451(): pass

    label('loc_2451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_245B',
    )

    Jump('loc_2476')

    def _loc_245B(): pass

    label('loc_245B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2465',
    )

    Jump('loc_2476')

    def _loc_2465(): pass

    label('loc_2465')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_246F',
    )

    Jump('loc_2476')

    def _loc_246F(): pass

    label('loc_246F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2476',
    )

    def _loc_2476(): pass

    label('loc_2476')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x247A
@scena.Code('func_0D_247A')
def func_0D_247A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_25C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2501',
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

    Jump('loc_25BF')

    def _loc_2501(): pass

    label('loc_2501')

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

    def _loc_25BF(): pass

    label('loc_25BF')

    Jump('loc_405B')

    def _loc_25C2(): pass

    label('loc_25C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2686',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2622',
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

    Jump('loc_2683')

    def _loc_2622(): pass

    label('loc_2622')

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

    def _loc_2683(): pass

    label('loc_2683')

    Jump('loc_405B')

    def _loc_2686(): pass

    label('loc_2686')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_26AD',
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

    Jump('loc_405B')

    def _loc_26AD(): pass

    label('loc_26AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_29D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2713',
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

    Jump('loc_29D6')

    def _loc_2713(): pass

    label('loc_2713')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2771',
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

    Jump('loc_29D6')

    def _loc_2771(): pass

    label('loc_2771')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_27F6',
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

    Jump('loc_29D6')

    def _loc_27F6(): pass

    label('loc_27F6')

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

    def _loc_29D6(): pass

    label('loc_29D6')

    Jump('loc_405B')

    def _loc_29D9(): pass

    label('loc_29D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2C87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2A35',
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

    Jump('loc_2C84')

    def _loc_2A35(): pass

    label('loc_2A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_2A97',
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

    Jump('loc_2C84')

    def _loc_2A97(): pass

    label('loc_2A97')

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

    def _loc_2C84(): pass

    label('loc_2C84')

    Jump('loc_405B')

    def _loc_2C87(): pass

    label('loc_2C87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_309B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2CC5',
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

    Jump('loc_3098')

    def _loc_2CC5(): pass

    label('loc_2CC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2D09',
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

    Jump('loc_3098')

    def _loc_2D09(): pass

    label('loc_2D09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_2D9C',
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

    Jump('loc_3098')

    def _loc_2D9C(): pass

    label('loc_2D9C')

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
        'loc_3016',
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

    Jump('loc_3098')

    def _loc_3016(): pass

    label('loc_3016')

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

    def _loc_3098(): pass

    label('loc_3098')

    Jump('loc_405B')

    def _loc_309B(): pass

    label('loc_309B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3422',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3106',
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

    Jump('loc_341F')

    def _loc_3106(): pass

    label('loc_3106')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3156',
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

    Jump('loc_341F')

    def _loc_3156(): pass

    label('loc_3156')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_320F',
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

    Jump('loc_341F')

    def _loc_320F(): pass

    label('loc_320F')

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

    def _loc_341F(): pass

    label('loc_341F')

    Jump('loc_405B')

    def _loc_3422(): pass

    label('loc_3422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3798',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_349C',
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

    Jump('loc_3795')

    def _loc_349C(): pass

    label('loc_349C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3501',
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

    Jump('loc_3795')

    def _loc_3501(): pass

    label('loc_3501')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_35A1',
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

    Jump('loc_3795')

    def _loc_35A1(): pass

    label('loc_35A1')

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

    def _loc_3795(): pass

    label('loc_3795')

    Jump('loc_405B')

    def _loc_3798(): pass

    label('loc_3798')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3B0B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_380C',
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

    Jump('loc_3B08')

    def _loc_380C(): pass

    label('loc_380C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_385C',
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

    Jump('loc_3B08')

    def _loc_385C(): pass

    label('loc_385C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_3901',
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

    Jump('loc_3B08')

    def _loc_3901(): pass

    label('loc_3901')

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

    def _loc_3B08(): pass

    label('loc_3B08')

    Jump('loc_405B')

    def _loc_3B0B(): pass

    label('loc_3B0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3DF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3B62',
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

    Jump('loc_3DF1')

    def _loc_3B62(): pass

    label('loc_3B62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Return,
        ),
        'loc_3BE1',
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

    Jump('loc_3DF1')

    def _loc_3BE1(): pass

    label('loc_3BE1')

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

    def _loc_3DF1(): pass

    label('loc_3DF1')

    Jump('loc_405B')

    def _loc_3DF4(): pass

    label('loc_3DF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_405B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3E4B',
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

    Jump('loc_405B')

    def _loc_3E4B(): pass

    label('loc_3E4B')

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

    def _loc_405B(): pass

    label('loc_405B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x405F
@scena.Code('func_0E_405F')
def func_0E_405F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4192',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_40EC',
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

    Jump('loc_418F')

    def _loc_40EC(): pass

    label('loc_40EC')

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

    def _loc_418F(): pass

    label('loc_418F')

    Jump('loc_459F')

    def _loc_4192(): pass

    label('loc_4192')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4201',
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

    Jump('loc_459F')

    def _loc_4201(): pass

    label('loc_4201')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4269',
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

    Jump('loc_459F')

    def _loc_4269(): pass

    label('loc_4269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_42D7',
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

    Jump('loc_459F')

    def _loc_42D7(): pass

    label('loc_42D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4312',
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

    Jump('loc_459F')

    def _loc_4312(): pass

    label('loc_4312')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4348',
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

    Jump('loc_459F')

    def _loc_4348(): pass

    label('loc_4348')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4399',
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

    Jump('loc_459F')

    def _loc_4399(): pass

    label('loc_4399')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_43F9',
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

    Jump('loc_459F')

    def _loc_43F9(): pass

    label('loc_43F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4478',
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

    Jump('loc_459F')

    def _loc_4478(): pass

    label('loc_4478')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4542',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_44D2',
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

    Jump('loc_453F')

    def _loc_44D2(): pass

    label('loc_44D2')

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

    def _loc_453F(): pass

    label('loc_453F')

    Jump('loc_459F')

    def _loc_4542(): pass

    label('loc_4542')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_459F',
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

    def _loc_459F(): pass

    label('loc_459F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x45A3
@scena.Code('func_0F_45A3')
def func_0F_45A3():
    Call(2, 0x0010)

    Return()

# id: 0x0010 offset: 0x45A8
@scena.Code('func_10_45A8')
def func_10_45A8():
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
        'loc_4625',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x62)
    OP_56(0x00)
    TalkEnd(0x0016)

    Return()

    def _loc_4625(): pass

    label('loc_4625')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4723',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x3E8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_46EE',
    )

    RemoveMira(1000)
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
    ChrSetStatus(0x0000, 0xFD, 1000)
    ChrSetStatus(0x0001, 0xFD, 1000)
    ChrSetStatus(0x0002, 0xFD, 1000)
    ChrSetStatus(0x0003, 0xFD, 1000)
    ChrSetStatus(0x0004, 0xFD, 1000)
    ChrSetStatus(0x0005, 0xFD, 1000)
    ChrSetStatus(0x0006, 0xFD, 1000)
    ChrSetStatus(0x0007, 0xFD, 1000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_46E0',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x000B)"),
            Expr.Return,
        ),
        'loc_46B8',
    )

    Jump('loc_46E0')

    def _loc_46B8(): pass

    label('loc_46B8')

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

    def _loc_46E0(): pass

    label('loc_46E0')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_4714')

    def _loc_46EE(): pass

    label('loc_46EE')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_4714(): pass

    label('loc_4714')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0016)

    Return()

    def _loc_4723(): pass

    label('loc_4723')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_473D',
    )

    FadeIn(300, 0)
    TalkEnd(0x0016)

    Return()

    def _loc_473D(): pass

    label('loc_473D')

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
        'loc_4C2F',
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
        'loc_4C2F',
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
        (0x00000000, 'loc_4919'),
        (0x00000001, 'loc_4946'),
        (-1, 'loc_4966'),
    )

    def _loc_4919(): pass

    label('loc_4919')

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

    Jump('loc_4966')

    def _loc_4946(): pass

    label('loc_4946')

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

    def _loc_4966(): pass

    label('loc_4966')

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
        (0x00000000, 'loc_4AA8'),
        (0x00000001, 'loc_4B11'),
        (-1, 'loc_4B86'),
    )

    def _loc_4AA8(): pass

    label('loc_4AA8')

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
    TalkSetChrName('')
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

    Jump('loc_4B86')

    def _loc_4B11(): pass

    label('loc_4B11')

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
    TalkSetChrName('')
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

    Jump('loc_4B86')

    def _loc_4B86(): pass

    label('loc_4B86')

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

    def _loc_4C2F(): pass

    label('loc_4C2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4CB7',
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

    Jump('loc_5442')

    def _loc_4CB7(): pass

    label('loc_4CB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4DB5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4D20',
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

    Jump('loc_4DB2')

    def _loc_4D20(): pass

    label('loc_4D20')

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

    def _loc_4DB2(): pass

    label('loc_4DB2')

    Jump('loc_5442')

    def _loc_4DB5(): pass

    label('loc_4DB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4EAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4E1E',
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

    Jump('loc_4EAC')

    def _loc_4E1E(): pass

    label('loc_4E1E')

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

    def _loc_4EAC(): pass

    label('loc_4EAC')

    Jump('loc_5442')

    def _loc_4EAF(): pass

    label('loc_4EAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4F19',
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

    Jump('loc_5442')

    def _loc_4F19(): pass

    label('loc_4F19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4FCE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4F5F',
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

    Jump('loc_4FCB')

    def _loc_4F5F(): pass

    label('loc_4F5F')

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

    def _loc_4FCB(): pass

    label('loc_4FCB')

    Jump('loc_5442')

    def _loc_4FCE(): pass

    label('loc_4FCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_50CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_5044',
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

    Jump('loc_50CB')

    def _loc_5044(): pass

    label('loc_5044')

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

    def _loc_50CB(): pass

    label('loc_50CB')

    Jump('loc_5442')

    def _loc_50CE(): pass

    label('loc_50CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_51AA',
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

    Jump('loc_5442')

    def _loc_51AA(): pass

    label('loc_51AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_52CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_522B',
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

    Jump('loc_52C9')

    def _loc_522B(): pass

    label('loc_522B')

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

    def _loc_52C9(): pass

    label('loc_52C9')

    Jump('loc_5442')

    def _loc_52CC(): pass

    label('loc_52CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_533C',
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

    Jump('loc_5442')

    def _loc_533C(): pass

    label('loc_533C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_53B6',
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

    Jump('loc_5442')

    def _loc_53B6(): pass

    label('loc_53B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5442',
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

    def _loc_5442(): pass

    label('loc_5442')

    TalkEnd(0x0016)

    Return()

# id: 0x0011 offset: 0x5446
@scena.Code('func_11_5446')
def func_11_5446():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5453',
    )

    Jump('loc_5576')

    def _loc_5453(): pass

    label('loc_5453')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_54A9',
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

    Jump('loc_5576')

    def _loc_54A9(): pass

    label('loc_54A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_54D5',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典之前都没什么事做呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5576')

    def _loc_54D5(): pass

    label('loc_54D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5533',
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

    Jump('loc_5576')

    def _loc_5533(): pass

    label('loc_5533')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_553D',
    )

    Jump('loc_5576')

    def _loc_553D(): pass

    label('loc_553D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5547',
    )

    Jump('loc_5576')

    def _loc_5547(): pass

    label('loc_5547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5551',
    )

    Jump('loc_5576')

    def _loc_5551(): pass

    label('loc_5551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_555B',
    )

    Jump('loc_5576')

    def _loc_555B(): pass

    label('loc_555B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5565',
    )

    Jump('loc_5576')

    def _loc_5565(): pass

    label('loc_5565')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_556F',
    )

    Jump('loc_5576')

    def _loc_556F(): pass

    label('loc_556F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5576',
    )

    def _loc_5576(): pass

    label('loc_5576')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x557A
@scena.Code('func_12_557A')
def func_12_557A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5587',
    )

    Jump('loc_5693')

    def _loc_5587(): pass

    label('loc_5587')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_55BF',
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

    Jump('loc_5693')

    def _loc_55BF(): pass

    label('loc_55BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5623',
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

    Jump('loc_5693')

    def _loc_5623(): pass

    label('loc_5623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5650',
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

    Jump('loc_5693')

    def _loc_5650(): pass

    label('loc_5650')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_565A',
    )

    Jump('loc_5693')

    def _loc_565A(): pass

    label('loc_565A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5664',
    )

    Jump('loc_5693')

    def _loc_5664(): pass

    label('loc_5664')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_566E',
    )

    Jump('loc_5693')

    def _loc_566E(): pass

    label('loc_566E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5678',
    )

    Jump('loc_5693')

    def _loc_5678(): pass

    label('loc_5678')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5682',
    )

    Jump('loc_5693')

    def _loc_5682(): pass

    label('loc_5682')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_568C',
    )

    Jump('loc_5693')

    def _loc_568C(): pass

    label('loc_568C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5693',
    )

    def _loc_5693(): pass

    label('loc_5693')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x5697
@scena.Code('func_13_5697')
def func_13_5697():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_56A4',
    )

    Jump('loc_574D')

    def _loc_56A4(): pass

    label('loc_56A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_56AE',
    )

    Jump('loc_574D')

    def _loc_56AE(): pass

    label('loc_56AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_56B8',
    )

    Jump('loc_574D')

    def _loc_56B8(): pass

    label('loc_56B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_570A',
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

    Jump('loc_574D')

    def _loc_570A(): pass

    label('loc_570A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5714',
    )

    Jump('loc_574D')

    def _loc_5714(): pass

    label('loc_5714')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_571E',
    )

    Jump('loc_574D')

    def _loc_571E(): pass

    label('loc_571E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5728',
    )

    Jump('loc_574D')

    def _loc_5728(): pass

    label('loc_5728')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5732',
    )

    Jump('loc_574D')

    def _loc_5732(): pass

    label('loc_5732')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_573C',
    )

    Jump('loc_574D')

    def _loc_573C(): pass

    label('loc_573C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5746',
    )

    Jump('loc_574D')

    def _loc_5746(): pass

    label('loc_5746')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_574D',
    )

    def _loc_574D(): pass

    label('loc_574D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x5751
@scena.Code('func_14_5751')
def func_14_5751():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_575E',
    )

    Jump('loc_58AB')

    def _loc_575E(): pass

    label('loc_575E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5768',
    )

    Jump('loc_58AB')

    def _loc_5768(): pass

    label('loc_5768')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5772',
    )

    Jump('loc_58AB')

    def _loc_5772(): pass

    label('loc_5772')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5868',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_57DF',
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

    Jump('loc_5865')

    def _loc_57DF(): pass

    label('loc_57DF')

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

    def _loc_5865(): pass

    label('loc_5865')

    Jump('loc_58AB')

    def _loc_5868(): pass

    label('loc_5868')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5872',
    )

    Jump('loc_58AB')

    def _loc_5872(): pass

    label('loc_5872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_587C',
    )

    Jump('loc_58AB')

    def _loc_587C(): pass

    label('loc_587C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5886',
    )

    Jump('loc_58AB')

    def _loc_5886(): pass

    label('loc_5886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5890',
    )

    Jump('loc_58AB')

    def _loc_5890(): pass

    label('loc_5890')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_589A',
    )

    Jump('loc_58AB')

    def _loc_589A(): pass

    label('loc_589A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_58A4',
    )

    Jump('loc_58AB')

    def _loc_58A4(): pass

    label('loc_58A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_58AB',
    )

    def _loc_58AB(): pass

    label('loc_58AB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x58AF
@scena.Code('func_15_58AF')
def func_15_58AF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_58BC',
    )

    Jump('loc_5C62')

    def _loc_58BC(): pass

    label('loc_58BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_58C6',
    )

    Jump('loc_5C62')

    def _loc_58C6(): pass

    label('loc_58C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_58D0',
    )

    Jump('loc_5C62')

    def _loc_58D0(): pass

    label('loc_58D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_58DA',
    )

    Jump('loc_5C62')

    def _loc_58DA(): pass

    label('loc_58DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_58E4',
    )

    Jump('loc_5C62')

    def _loc_58E4(): pass

    label('loc_58E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5A79',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_590D',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_593E')

    def _loc_590D(): pass

    label('loc_590D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5923',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_593E')

    def _loc_5923(): pass

    label('loc_5923')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5939',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_593E')

    def _loc_5939(): pass

    label('loc_5939')

    ChrSetSubChip(0x00FE, 0)

    def _loc_593E(): pass

    label('loc_593E')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_59D4',
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

    Jump('loc_5A71')

    def _loc_59D4(): pass

    label('loc_59D4')

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

    def _loc_5A71(): pass

    label('loc_5A71')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5C62')

    def _loc_5A79(): pass

    label('loc_5A79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5A83',
    )

    Jump('loc_5C62')

    def _loc_5A83(): pass

    label('loc_5A83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5BF7',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5AAC',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5ADD')

    def _loc_5AAC(): pass

    label('loc_5AAC')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5AC2',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_5ADD')

    def _loc_5AC2(): pass

    label('loc_5AC2')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5AD8',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_5ADD')

    def _loc_5AD8(): pass

    label('loc_5AD8')

    ChrSetSubChip(0x00FE, 0)

    def _loc_5ADD(): pass

    label('loc_5ADD')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_5B5A',
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

    Jump('loc_5BEF')

    def _loc_5B5A(): pass

    label('loc_5B5A')

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

    def _loc_5BEF(): pass

    label('loc_5BEF')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5C62')

    def _loc_5BF7(): pass

    label('loc_5BF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5C01',
    )

    Jump('loc_5C62')

    def _loc_5C01(): pass

    label('loc_5C01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5C5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_5C58',
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

    def _loc_5C58(): pass

    label('loc_5C58')

    Jump('loc_5C62')

    def _loc_5C5B(): pass

    label('loc_5C5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5C62',
    )

    def _loc_5C62(): pass

    label('loc_5C62')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x5C66
@scena.Code('func_16_5C66')
def func_16_5C66():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5C8B',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_5CA6')

    def _loc_5C8B(): pass

    label('loc_5C8B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5CA1',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_5CA6')

    def _loc_5CA1(): pass

    label('loc_5CA1')

    ChrSetSubChip(0x00FE, 2)

    def _loc_5CA6(): pass

    label('loc_5CA6')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5FEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_5D32',
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

    Jump('loc_5FEB')

    def _loc_5D32(): pass

    label('loc_5D32')

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

    def _loc_5FEB(): pass

    label('loc_5FEB')

    Jump('loc_61C4')

    def _loc_5FEE(): pass

    label('loc_5FEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5FF8',
    )

    Jump('loc_61C4')

    def _loc_5FF8(): pass

    label('loc_5FF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6002',
    )

    Jump('loc_61C4')

    def _loc_6002(): pass

    label('loc_6002')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_600C',
    )

    Jump('loc_61C4')

    def _loc_600C(): pass

    label('loc_600C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6016',
    )

    Jump('loc_61C4')

    def _loc_6016(): pass

    label('loc_6016')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6070',
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

    Jump('loc_61C4')

    def _loc_6070(): pass

    label('loc_6070')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_607A',
    )

    Jump('loc_61C4')

    def _loc_607A(): pass

    label('loc_607A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_61A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_60BF',
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

    Jump('loc_61A6')

    def _loc_60BF(): pass

    label('loc_60BF')

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

    def _loc_61A6(): pass

    label('loc_61A6')

    Jump('loc_61C4')

    def _loc_61A9(): pass

    label('loc_61A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_61B3',
    )

    Jump('loc_61C4')

    def _loc_61B3(): pass

    label('loc_61B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_61BD',
    )

    Jump('loc_61C4')

    def _loc_61BD(): pass

    label('loc_61BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_61C4',
    )

    def _loc_61C4(): pass

    label('loc_61C4')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x61CD
@scena.Code('func_17_61CD')
def func_17_61CD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_62D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_624E',
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

    Jump('loc_62D6')

    def _loc_624E(): pass

    label('loc_624E')

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

    def _loc_62D6(): pass

    label('loc_62D6')

    Jump('loc_69EB')

    def _loc_62D9(): pass

    label('loc_62D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_6328',
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

    Jump('loc_69EB')

    def _loc_6328(): pass

    label('loc_6328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_638A',
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

    Jump('loc_69EB')

    def _loc_638A(): pass

    label('loc_638A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6402',
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

    Jump('loc_69EB')

    def _loc_6402(): pass

    label('loc_6402')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_64F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_6475',
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

    Jump('loc_64F0')

    def _loc_6475(): pass

    label('loc_6475')

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

    def _loc_64F0(): pass

    label('loc_64F0')

    Jump('loc_69EB')

    def _loc_64F3(): pass

    label('loc_64F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6574',
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

    Jump('loc_69EB')

    def _loc_6574(): pass

    label('loc_6574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_65E0',
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

    Jump('loc_69EB')

    def _loc_65E0(): pass

    label('loc_65E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_66E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_6653',
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

    Jump('loc_66DF')

    def _loc_6653(): pass

    label('loc_6653')

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

    def _loc_66DF(): pass

    label('loc_66DF')

    Jump('loc_69EB')

    def _loc_66E2(): pass

    label('loc_66E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6841',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_677C',
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

    Jump('loc_683E')

    def _loc_677C(): pass

    label('loc_677C')

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

    def _loc_683E(): pass

    label('loc_683E')

    Jump('loc_69EB')

    def _loc_6841(): pass

    label('loc_6841')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_6870',
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

    Jump('loc_69EB')

    def _loc_6870(): pass

    label('loc_6870')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_68D9',
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

    Jump('loc_69EB')

    def _loc_68D9(): pass

    label('loc_68D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_69EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_6945',
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

    Jump('loc_69EB')

    def _loc_6945(): pass

    label('loc_6945')

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

    def _loc_69EB(): pass

    label('loc_69EB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x69EF
@scena.Code('func_18_69EF')
def func_18_69EF():
    Call(2, 0x0019)

    Return()

# id: 0x0019 offset: 0x69F4
@scena.Code('func_19_69F4')
def func_19_69F4():
    TalkBegin(0x000E)
    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6A04',
    )

    Jump('loc_6A0E')

    def _loc_6A04(): pass

    label('loc_6A04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6A0E',
    )

    ClearScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    def _loc_6A0E(): pass

    label('loc_6A0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_6BA7',
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
        'loc_6A8F',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x61)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_6A8F(): pass

    label('loc_6A8F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B8D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x3E8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_6B58',
    )

    RemoveMira(1000)
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
    ChrSetStatus(0x0000, 0xFD, 1000)
    ChrSetStatus(0x0001, 0xFD, 1000)
    ChrSetStatus(0x0002, 0xFD, 1000)
    ChrSetStatus(0x0003, 0xFD, 1000)
    ChrSetStatus(0x0004, 0xFD, 1000)
    ChrSetStatus(0x0005, 0xFD, 1000)
    ChrSetStatus(0x0006, 0xFD, 1000)
    ChrSetStatus(0x0007, 0xFD, 1000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6B4A',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0002)"),
            Expr.Return,
        ),
        'loc_6B22',
    )

    Jump('loc_6B4A')

    def _loc_6B22(): pass

    label('loc_6B22')

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

    def _loc_6B4A(): pass

    label('loc_6B4A')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_6B7E')

    def _loc_6B58(): pass

    label('loc_6B58')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_6B7E(): pass

    label('loc_6B7E')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000E)

    Return()

    def _loc_6B8D(): pass

    label('loc_6B8D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6BA7',
    )

    FadeIn(300, 0)
    TalkEnd(0x000E)

    Return()

    def _loc_6BA7(): pass

    label('loc_6BA7')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_6C8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_6BF8',
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

    Jump('loc_6C8A')

    def _loc_6BF8(): pass

    label('loc_6BF8')

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

    def _loc_6C8A(): pass

    label('loc_6C8A')

    Jump('loc_724F')

    def _loc_6C8D(): pass

    label('loc_6C8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_6D03',
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

    Jump('loc_724F')

    def _loc_6D03(): pass

    label('loc_6D03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6D82',
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

    Jump('loc_724F')

    def _loc_6D82(): pass

    label('loc_6D82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6DDD',
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

    Jump('loc_724F')

    def _loc_6DDD(): pass

    label('loc_6DDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6E4C',
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

    Jump('loc_724F')

    def _loc_6E4C(): pass

    label('loc_6E4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6EDA',
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

    Jump('loc_724F')

    def _loc_6EDA(): pass

    label('loc_6EDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6F51',
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

    Jump('loc_724F')

    def _loc_6F51(): pass

    label('loc_6F51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_6F96',
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

    Jump('loc_724F')

    def _loc_6F96(): pass

    label('loc_6F96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_70B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_6FDF',
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

    Jump('loc_70AE')

    def _loc_6FDF(): pass

    label('loc_6FDF')

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
    ChrSetDirection(0x000E, 180, 400)

    def _loc_70AE(): pass

    label('loc_70AE')

    Jump('loc_724F')

    def _loc_70B1(): pass

    label('loc_70B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_716A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_712E',
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

    Jump('loc_7167')

    def _loc_712E(): pass

    label('loc_712E')

    ChrTalk(
        0x000E,
        (
            '大会的预选赛好像已经结束了。\n',
            '这里客人立刻多了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7167(): pass

    label('loc_7167')

    Jump('loc_724F')

    def _loc_716A(): pass

    label('loc_716A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_724F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_71C7',
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

    Jump('loc_724F')

    def _loc_71C7(): pass

    label('loc_71C7')

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

    def _loc_724F(): pass

    label('loc_724F')

    TalkEnd(0x000E)

    Return()

# id: 0x001A offset: 0x7253
@scena.Code('func_1A_7253')
def func_1A_7253():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_7477',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_72E9',
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

    Jump('loc_7477')

    def _loc_72E9(): pass

    label('loc_72E9')

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

    def _loc_7477(): pass

    label('loc_7477')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x747B
@scena.Code('func_1B_747B')
def func_1B_747B():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7927',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 4660, 0, 540, 90)
    ChrSetPos(0x0102, 4870, 0, -630, 45)
    ChrSetPos(0x0108, 3570, 0, 140, 90)
    ChrSetSubChip(0x000C, 0)
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
        'loc_7502',
    )

    OP_28(0x004B, 0x01, 0x0100)

    def _loc_7502(): pass

    label('loc_7502')

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

    @scena.Lambda('lambda_7882')
    def lambda_7882():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_7882')

    DispatchAsync2(0x0101, 0x0001, lambda_7882)

    @scena.Lambda('lambda_7893')
    def lambda_7893():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_7893')

    DispatchAsync2(0x0102, 0x0001, lambda_7893)

    @scena.Lambda('lambda_78A4')
    def lambda_78A4():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_78A4')

    DispatchAsync2(0x0108, 0x0001, lambda_78A4)

    ChrWalkTo(0x000C, 5630, 0, -1470, 4000, 0x00)
    ChrWalkTo(0x000C, 1880, 0, -1480, 4000, 0x00)
    ChrWalkTo(0x000C, 710, 0, -5490, 4000, 0x00)

    @scena.Lambda('lambda_78F1')
    def lambda_78F1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_78F1)

    ChrWalkTo(0x000C, 710, -250, -7470, 4000, 0x00)
    ChrSetFlags(0x000C, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    EventEnd(0x00)

    Jump('loc_7EB8')

    def _loc_7927(): pass

    label('loc_7927')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_7B78',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7996',
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

    Jump('loc_7B75')

    def _loc_7996(): pass

    label('loc_7996')

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

    def _loc_7B75(): pass

    label('loc_7B75')

    Jump('loc_7EB8')

    def _loc_7B78(): pass

    label('loc_7B78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_7B82',
    )

    Jump('loc_7EB8')

    def _loc_7B82(): pass

    label('loc_7B82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_7B8C',
    )

    Jump('loc_7EB8')

    def _loc_7B8C(): pass

    label('loc_7B8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_7CB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7BFA',
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

    Jump('loc_7CB4')

    def _loc_7BFA(): pass

    label('loc_7BFA')

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

    def _loc_7CB4(): pass

    label('loc_7CB4')

    Jump('loc_7EB8')

    def _loc_7CB7(): pass

    label('loc_7CB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_7CC1',
    )

    Jump('loc_7EB8')

    def _loc_7CC1(): pass

    label('loc_7CC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_7CCB',
    )

    Jump('loc_7EB8')

    def _loc_7CCB(): pass

    label('loc_7CCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_7CD5',
    )

    Jump('loc_7EB8')

    def _loc_7CD5(): pass

    label('loc_7CD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_7CDF',
    )

    Jump('loc_7EB8')

    def _loc_7CDF(): pass

    label('loc_7CDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_7EA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7D38',
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

    Jump('loc_7EA4')

    def _loc_7D38(): pass

    label('loc_7D38')

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

    def _loc_7EA4(): pass

    label('loc_7EA4')

    Jump('loc_7EB8')

    def _loc_7EA7(): pass

    label('loc_7EA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_7EB1',
    )

    Jump('loc_7EB8')

    def _loc_7EB1(): pass

    label('loc_7EB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_7EB8',
    )

    def _loc_7EB8(): pass

    label('loc_7EB8')

    TalkEnd(0x000C)

    Return()

# id: 0x001C offset: 0x7EBC
@scena.Code('func_1C_7EBC')
def func_1C_7EBC():
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
