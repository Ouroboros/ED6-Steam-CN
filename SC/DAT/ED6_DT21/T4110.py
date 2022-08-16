import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4110.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拉科舒',
            x                   = 59570,
            z                   = 0,
            y                   = 58710,
            direction           = 3,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '菲利奥',
            x                   = 57660,
            z                   = 0,
            y                   = 58150,
            direction           = 53,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 7220,
            z                   = 200,
            y                   = 53570,
            direction           = 269,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '芭蒂',
            x                   = -29600,
            z                   = 4000,
            y                   = 1830,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '拉尔夫',
            x                   = -27310,
            z                   = 0,
            y                   = -4370,
            direction           = 81,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '比尔爷爷',
            x                   = 28110,
            z                   = 0,
            y                   = -950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '伊鲁妮婆婆',
            x                   = 32189,
            z                   = 0,
            y                   = 6630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '丹克',
            x                   = 91740,
            z                   = 0,
            y                   = -1110,
            direction           = 23,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10002 offset: 0x1DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1DA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1DA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1FF',
    )

    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x000E, 31320, 0, 100, 270)
    ChrSetFlags(0x000E, 0x0010)

    Jump('loc_30A')

    def _loc_1FF(): pass

    label('loc_1FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_25E',
    )

    ChrSetPos(0x000B, -27310, 0, -4370, 81)
    CreateThread(0x000B, 0x00, 0x06, func_02_331)
    ChrSetPos(0x000C, -29600, 4000, 1830, 90)
    CreateThread(0x000C, 0x00, 0x00, func_02_331)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x000E, 31320, 0, 100, 270)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_30A')

    def _loc_25E(): pass

    label('loc_25E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_29D',
    )

    ChrSetPos(0x000B, -27310, 0, -4370, 81)
    CreateThread(0x000B, 0x00, 0x06, func_02_331)
    ChrSetPos(0x000C, -29600, 4000, 1830, 90)
    CreateThread(0x000C, 0x00, 0x00, func_02_331)
    ChrSetFlags(0x000E, 0x0010)

    Jump('loc_30A')

    def _loc_29D(): pass

    label('loc_29D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_2DC',
    )

    ChrSetPos(0x000B, -27310, 0, -4370, 81)
    CreateThread(0x000B, 0x00, 0x06, func_02_331)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000C, -29600, 4000, 1830, 90)
    CreateThread(0x000C, 0x00, 0x00, func_02_331)

    Jump('loc_30A')

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EA',
    )

    Jump('loc_30A')

    def _loc_2EA(): pass

    label('loc_2EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2F9',
    )

    ChrSetFlags(0x000E, 0x0010)

    Jump('loc_30A')

    def _loc_2F9(): pass

    label('loc_2F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_303',
    )

    Jump('loc_30A')

    def _loc_303(): pass

    label('loc_303')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_30A',
    )

    def _loc_30A(): pass

    label('loc_30A')

    Return()

# id: 0x0001 offset: 0x30B
@scena.Code('func_01_30B')
def func_01_30B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_327',
    )

    OP_B1('t4110_y')

    Jump('loc_330')

    def _loc_327(): pass

    label('loc_327')

    OP_B1('t4110_n')

    def _loc_330(): pass

    label('loc_330')

    Return()

# id: 0x0002 offset: 0x331
@scena.Code('func_02_331')
def func_02_331():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_354',
    )

    OP_8D(0x00FE, -30880, 4000, -29430, 0, 2000)

    Jump('func_02_331')

    def _loc_354(): pass

    label('loc_354')

    Return()

# id: 0x0003 offset: 0x355
@scena.Code('func_03_355')
def func_03_355():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_43D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3C1',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫为了保护仓库\n',
            '好像去了港口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是不是在我的教育下终于\n',
            '觉醒了工作的热情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43A')

    def _loc_3C1(): pass

    label('loc_3C1')

    ChrTalk(
        0x00FE,
        (
            '隔壁的那家主人我好像\n',
            '在哪儿见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过当我想看清他的脸时\n',
            '他就躲到店里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概是个容易害羞的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_43A(): pass

    label('loc_43A')

    Jump('loc_706')

    def _loc_43D(): pass

    label('loc_43D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_4E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_49A',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，隔壁的空房\n',
            '似乎找到房客了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道会搬来\n',
            '一个怎样的人呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E4')

    def _loc_49A(): pass

    label('loc_49A')

    ChrTalk(
        0x00FE,
        (
            '听说我丈夫卷入了一个事件\n',
            '我可担心死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他没事真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_4E4(): pass

    label('loc_4E4')

    Jump('loc_706')

    def _loc_4E7(): pass

    label('loc_4E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_588',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我给在港口工作的丈夫\n',
            '送去了亲手特制的便当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是对他压力\n',
            '他也受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是所谓的大棒和萝卜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是参考帝国的伟人\n',
            '写的书哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_706')

    def _loc_588(): pass

    label('loc_588')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F1',
    )

    ChrTalk(
        0x00FE,
        (
            '因为我丈夫赖床，我就把穿着\n',
            '睡衣的他直接拖到外面，让他上班去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是为了他好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_706')

    def _loc_5F1(): pass

    label('loc_5F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_677',
    )

    ChrTalk(
        0x00FE,
        (
            '我想了很久……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就因为我没好好提醒丈夫，\n',
            '结果就把他给惯坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算今后被说成是狠心的妻子\n',
            '我也要为了丈夫拼了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_706')

    def _loc_677(): pass

    label('loc_677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_706',
    )

    ChrTalk(
        0x00FE,
        (
            '自从在卢安的游戏吧大败之后\n',
            '我丈夫就在港口认真工作着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为那件事他终于清醒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我想这么认为，\n',
            '不过还不能放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_706(): pass

    label('loc_706')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x70A
@scena.Code('func_04_70A')
def func_04_70A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_79D',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然因为导力器不能用，\n',
            '我也消沉了一阵子，\n',
            '不过还是只能努力活下去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我妻子艾德尔也在\n',
            '店里努力工作，\n',
            '我也必须努力不输给她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB0')

    def _loc_79D(): pass

    label('loc_79D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_81F',
    )

    ChrTalk(
        0x00FE,
        (
            '听说一部分港口的设施\n',
            '被坦克给破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '住在隔壁的丹克先生\n',
            '好像也被特务兵抓走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他不要受伤什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB0')

    def _loc_81F(): pass

    label('loc_81F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_8DB',
    )

    ChrTalk(
        0x00FE,
        (
            '市民们在柏斯的教会祈祷\n',
            '生意兴隆，修女可生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，女神\n',
            '确实不是财神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像共和国有些人信奉\n',
            '掌管生意兴隆的神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……如果我妻子知道了\n',
            '一定会飞去共和国的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB0')

    def _loc_8DB(): pass

    label('loc_8DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_984',
    )

    ChrTalk(
        0x00FE,
        (
            '洛连特的教会虽然简陋，不过迪拜恩\n',
            '教区长是个很容易让人留下印象的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '沉稳又有威严，\n',
            '对草药也很有研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '确实可以说是个\n',
            '与教区长身份相符的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB0')

    def _loc_984(): pass

    label('loc_984')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_A2F',
    )

    ChrTalk(
        0x00FE,
        (
            '不久前我和妻子一起\n',
            '周游了利贝尔所有的七耀教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然妻子的目的\n',
            '是购物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在卡兰大主教的劝说下\n',
            '她总结了一篇周游的游记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～我要努力了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB0')

    def _loc_A2F(): pass

    label('loc_A2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_AB0',
    )

    ChrTalk(
        0x00FE,
        (
            '我的妻子在东街区\n',
            '经营着百货商店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你问我是干什么的？\n',
            '唔～大概可以说是宗教家之类的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我绝不是家庭妇男哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AB0(): pass

    label('loc_AB0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xAB4
@scena.Code('func_05_AB4')
def func_05_AB4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B0D',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～导力器都不能用了，\n',
            '真不方便啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望女王\n',
            '能赶紧想想办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7A')

    def _loc_B0D(): pass

    label('loc_B0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_C5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF7',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会时我丈夫\n',
            '通宵帮我占座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以有时得献一下媚，\n',
            '让他明年也能替我努力㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呵呵，一半是玩笑啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '努力做家务\n',
            '是因为我爱他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我平时之所以会任性\n',
            '是因为想看到他为了我\n',
            '竭尽所能的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_C58')

    def _loc_BF7(): pass

    label('loc_BF7')

    ChrTalk(
        0x00FE,
        (
            '我其实很想每天\n',
            '好好地为他做家务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是这样一来就\n',
            '看不到他为了我\n',
            '竭尽所能的样子了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C58(): pass

    label('loc_C58')

    Jump('loc_E7A')

    def _loc_C5B(): pass

    label('loc_C5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_C94',
    )

    ChrTalk(
        0x00FE,
        (
            '哼哼哼～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么赶快开始\n',
            '准备晚饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7A')

    def _loc_C94(): pass

    label('loc_C94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_CC4',
    )

    ChrTalk(
        0x00FE,
        (
            '哼哼哼～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啦啦啦、啦啦啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7A')

    def _loc_CC4(): pass

    label('loc_CC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D22',
    )

    ChrTalk(
        0x00FE,
        (
            '这个叫希德\n',
            '中校的人强不强呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光看照片的话感觉\n',
            '也没什么了不起的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7A')

    def _loc_D22(): pass

    label('loc_D22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_DB9',
    )

    ChrTalk(
        0x00FE,
        (
            '尤莉亚上尉和卡西乌斯准将\n',
            '打的话谁比较强呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，这可难以估计……\n',
            '得再收集些情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，让我先生去\n',
            '侦察一下军队的演习吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7A')

    def _loc_DB9(): pass

    label('loc_DB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_E3F',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军的卡西乌斯准将\n',
            '是百日战役的英雄吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这样的人参加武术大会的话\n',
            '一定会引起轰动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一定要特别注意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7A')

    def _loc_E3F(): pass

    label('loc_E3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_E7A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，明年快点来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真期待下一届武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7A(): pass

    label('loc_E7A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xE7E
@scena.Code('func_06_E7E')
def func_06_E7E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_E8B',
    )

    Jump('loc_1323')

    def _loc_E8B(): pass

    label('loc_E8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_EFE',
    )

    ChrTalk(
        0x00FE,
        (
            '好烫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '白天还好，\n',
            '有阳光的温暖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚上做饭可是\n',
            '非常麻烦的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得注意不要\n',
            '引发火灾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1323')

    def _loc_EFE(): pass

    label('loc_EFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_F53',
    )

    ChrTalk(
        0x00FE,
        (
            '怎、怎么办，太奇怪了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你、你们，帮帮我！\n',
            '我妻子今天也在做家务！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1323')

    def _loc_F53(): pass

    label('loc_F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_103D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FDA',
    )

    ChrTalk(
        0x00FE,
        (
            '…………奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天妻子一直\n',
            '在做着家务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，这样一来我当然省力了……\n',
            '不过她不会是在图谋着什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_103A')

    def _loc_FDA(): pass

    label('loc_FDA')

    ChrTalk(
        0x00FE,
        (
            '虽然妻子一个人做家务\n',
            '我是轻松多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还要分析她有什么企图，\n',
            '搞得我完全无法休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_103A(): pass

    label('loc_103A')

    Jump('loc_1323')

    def _loc_103D(): pass

    label('loc_103D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1082',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，难得白天妻子\n',
            '也会做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以偶尔休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1323')

    def _loc_1082(): pass

    label('loc_1082')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10EC',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，今天也一如既往地\n',
            '一天就这么过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神啊，难道说我的\n',
            '人生就像这样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1323')

    def _loc_10EC(): pass

    label('loc_10EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1182',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会时\n',
            '为了妻子通宵排队，\n',
            '终于抢到了最前排的位子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可这么做似乎反而\n',
            '助长了妻子的任性……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉自己好像被\n',
            '差使得更厉害了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1323')

    def _loc_1182(): pass

    label('loc_1182')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_12A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1252',
    )

    ChrTalk(
        0x00FE,
        (
            '她让我买东西时顺便\n',
            '买本武术大会的特辑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，希望她除了零食以外\n',
            '不要再增加家里的经济负担了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妻子都等不及武术大会了，\n',
            '现在就在预估冠军人选。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可参加的人都还没确定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_12A5')

    def _loc_1252(): pass

    label('loc_1252')

    ChrTalk(
        0x00FE,
        (
            '妻子都等不及武术大会了，\n',
            '现在就在预估冠军人选。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可参加的人都还没确定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12A5(): pass

    label('loc_12A5')

    Jump('loc_1323')

    def _loc_12A8(): pass

    label('loc_12A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1323',
    )

    ChrTalk(
        0x00FE,
        (
            '妻子至今还沉浸在\n',
            '武术大会的兴奋中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关心明年的武术大会是可以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在我希望\n',
            '她能帮着干点家务哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1323(): pass

    label('loc_1323')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1327
@scena.Code('func_07_1327')
def func_07_1327():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13A0',
    )

    ChrTalk(
        0x00FE,
        (
            '没什么啦，我们年轻时\n',
            '还没导力器之类的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果想成是回到过去的话，\n',
            '就一点都不会觉得不方便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164E')

    def _loc_13A0(): pass

    label('loc_13A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_13DF',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，老婆子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们生活中最\n',
            '重要的是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164E')

    def _loc_13DF(): pass

    label('loc_13DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1446',
    )

    ChrTalk(
        0x00FE,
        (
            '很久没见孙子了，真想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到了我这个年纪，最希望的是\n',
            '儿子媳妇能带着孙子来看看我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164E')

    def _loc_1446(): pass

    label('loc_1446')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_148D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，今天的天气也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天气好的时候\n',
            '心情也会开朗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164E')

    def _loc_148D(): pass

    label('loc_148D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_14E4',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，已经傍晚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神，感谢您今天\n',
            '也赐给我们一天的和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164E')

    def _loc_14E4(): pass

    label('loc_14E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_156B',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然发生了那么\n',
            '可耻的政变……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约的签字仪式\n',
            '能安然无恙就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有卡西乌斯准将在\n',
            '我想是没有问题的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164E')

    def _loc_156B(): pass

    label('loc_156B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1608',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，三国之间的\n',
            '互不侵犯条约真是了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然能顺利地让帝国和\n',
            '共和国互相收刀入鞘……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说艾莉茜雅女王是利贝尔的\n',
            '骄傲一点也不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164E')

    def _loc_1608(): pass

    label('loc_1608')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_164E',
    )

    ChrTalk(
        0x00FE,
        (
            '今天天气真不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔也想和老伴去\n',
            '艾尔贝离宫散步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_164E(): pass

    label('loc_164E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1652
@scena.Code('func_08_1652')
def func_08_1652():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16EC',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说是回到了过去，\n',
            '不过还是有不方便的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还是要忍耐再忍耐……\n',
            '这一点永远是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要忍耐，女王陛下\n',
            '一定会想办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_16EC(): pass

    label('loc_16EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_178D',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，老头子，\n',
            '最重要的不就是忍耐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论遇到什么样的困境，\n',
            '忍耐下去的话一定会有所好转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果拥有能忍耐的坚强的心，\n',
            '一定能得到幸福的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_178D(): pass

    label('loc_178D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1807',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，我在百货商店\n',
            '看见了一个穿白衣服的女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这让我想起来孙儿们。\n',
            '不知道他们现在怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_1807(): pass

    label('loc_1807')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_18A2',
    )

    ChrTalk(
        0x00FE,
        (
            '临近签字仪式，城里的气氛\n',
            '好像一下子变得活跃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是最喜欢\n',
            '热闹的王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这里是我遇到老头子的地方，\n',
            '也是和他一起生活的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_18A2(): pass

    label('loc_18A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A13',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199D',
    )

    ChrTalk(
        0x00FE,
        (
            '世界如果能朝好的方向\n',
            '发展就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真的不知道现在\n',
            '这个世界是怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从前一切都是\n',
            '那么地简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从导力革命以来，\n',
            '世风就渐渐地变化了……\n',
            '我们感到很不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望这世界上的所有人\n',
            '都能抱持着感恩的心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1A10')

    def _loc_199D(): pass

    label('loc_199D')

    ChrTalk(
        0x00FE,
        (
            '自从导力革命以来，\n',
            '世风就渐渐地变化了……\n',
            '我们感到很不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望这世界上的所有人\n',
            '都能抱持着感恩的心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A10(): pass

    label('loc_1A10')

    Jump('loc_1B1F')

    def _loc_1A13(): pass

    label('loc_1A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1A71',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子啊……\n',
            '火太大的话血压会上升的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '茶马上就好了，\n',
            '你先坐下来歇着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_1A71(): pass

    label('loc_1A71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1AD4',
    )

    ChrTalk(
        0x00FE,
        (
            '我能和老头子\n',
            '这样自由地生活\n',
            '都是拜女王陛下所赐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，真的要感谢\n',
            '女王陛下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_1AD4(): pass

    label('loc_1AD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1B1F',
    )

    ChrTalk(
        0x00FE,
        (
            '以前经常和老头子\n',
            '散步去离宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政变之后\n',
            '还一次也没去过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B1F(): pass

    label('loc_1B1F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1B23
@scena.Code('func_09_1B23')
def func_09_1B23():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈……\n',
            '而且港口又封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明政变的影响好不容易\n',
            '过去了，一切刚走上正规。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话\n',
            '不是又要失业了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1BA3
@scena.Code('func_0A_1BA3')
def func_0A_1BA3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '看来妻子很\n',
            '为我担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在工作休息时也不偷懒，\n',
            '而是帮助妻子做家务哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
