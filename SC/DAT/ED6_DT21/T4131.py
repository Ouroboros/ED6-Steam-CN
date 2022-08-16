import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4131   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4131.x'
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
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卡兰大主教',
            x                   = -50,
            z                   = 1000,
            y                   = 20410,
            direction           = 180,
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
            name                = '利瓦尔牧师',
            x                   = 2870,
            z                   = 1000,
            y                   = 18870,
            direction           = 272,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '修女诺雅',
            x                   = -71360,
            z                   = 0,
            y                   = 3640,
            direction           = 82,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '希丝娜',
            x                   = -3190,
            z                   = 150,
            y                   = 10800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 910,
            z                   = 0,
            y                   = 14450,
            direction           = 260,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 910,
            z                   = 0,
            y                   = 14450,
            direction           = 260,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '礼拜者',
            x                   = -3890,
            z                   = 1000,
            y                   = 17280,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '礼拜者',
            x                   = -2690,
            z                   = 1000,
            y                   = 17280,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '礼拜者',
            x                   = 3990,
            z                   = 150,
            y                   = 4660,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '礼拜者',
            x                   = 4970,
            z                   = 0,
            y                   = 5260,
            direction           = 210,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '礼拜者',
            x                   = -5300,
            z                   = 0,
            y                   = 7270,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
    )

# id: 0x10002 offset: 0x262
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x262
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x262
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 200,
            triggerZ            = 1000,
            triggerY            = 17890,
            triggerRange        = 400,
            actorX              = -50,
            actorZ              = 2500,
            actorY              = 20410,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -74990,
            triggerZ            = 0,
            triggerY            = 66030,
            triggerRange        = 800,
            actorX              = -74990,
            actorZ              = 1000,
            actorY              = 66030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    ChrSetPos(0x000A, -132010, 0, 6440, 340)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)

    Jump('loc_3BF')

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_31B',
    )

    ChrSetPos(0x000A, -132010, 0, 6440, 340)
    ChrSetPos(0x000E, 3250, 0, 13250, 344)
    ChrSetPos(0x000F, 4130, 0, 13250, 347)

    Jump('loc_3BF')

    def _loc_31B(): pass

    label('loc_31B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_369',
    )

    ChrSetPos(0x0009, -132010, 0, 6440, 340)
    ChrSetPos(0x000A, -75250, 0, 3670, 275)
    ChrSetPos(0x000E, 3250, 0, 13250, 344)
    ChrSetPos(0x000F, 4130, 0, 13250, 347)

    Jump('loc_3BF')

    def _loc_369(): pass

    label('loc_369')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B5',
    )

    ChrSetPos(0x0009, -132010, 0, 6440, 340)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B2',
    )

    ChrSetPos(0x000A, -540, 0, 14500, 103)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3AD',
    )

    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_3B2')

    def _loc_3AD(): pass

    label('loc_3AD')

    ChrClearFlags(0x000D, 0x0080)

    def _loc_3B2(): pass

    label('loc_3B2')

    Jump('loc_3BF')

    def _loc_3B5(): pass

    label('loc_3B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3BF',
    )

    Jump('loc_3BF')

    def _loc_3BF(): pass

    label('loc_3BF')

    Return()

# id: 0x0001 offset: 0x3C0
@scena.Code('func_01_3C0')
def func_01_3C0():
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
        'loc_3DC',
    )

    OP_B1('t4131_y')

    Jump('loc_3E5')

    def _loc_3DC(): pass

    label('loc_3DC')

    OP_B1('t4131_n')

    def _loc_3E5(): pass

    label('loc_3E5')

    Return()

# id: 0x0002 offset: 0x3E6
@scena.Code('func_02_3E6')
def func_02_3E6():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x3EB
@scena.Code('func_03_3EB')
def func_03_3EB():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_44B',
    )

    ChrTalk(
        0x0008,
        (
            '开始了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很遗憾，这次的事件\n',
            '并非女神的试练……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_44B(): pass

    label('loc_44B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_5B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52D',
    )

    ChrTalk(
        0x0008,
        (
            '在阻止特务兵这一观点上\n',
            '可以说他是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可不管怎么说，任务\n',
            '都是回收古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '泼出去的水\n',
            '收不回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽说是迫不得已，\n',
            '但也必须责罚他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当然，他……\n',
            '凯文神父应该是有思想准备的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_5B2')

    def _loc_52D(): pass

    label('loc_52D')

    ChrTalk(
        0x0008,
        (
            '在阻止特务兵这一观点上\n',
            '可以说他是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可不管怎么说，他的任务\n',
            '都是回收古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽说是迫不得已，\n',
            '但也必须责罚他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B2(): pass

    label('loc_5B2')

    Jump('loc_983')

    def _loc_5B5(): pass

    label('loc_5B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_628',
    )

    ChrTalk(
        0x0008,
        (
            '……穿白色礼服的少女？\n',
            '不，没来过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我记得几天前有个\n',
            '和父母一起来过的\n',
            '女孩子是这身打扮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_628(): pass

    label('loc_628')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_741',
    )

    ChrTalk(
        0x0008,
        (
            '刚才历史资料馆有来\n',
            '问过关于他们发现的\n',
            '古代遗物的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '教会确实有义务回收、\n',
            '调查古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '教会中也确实有\n',
            '这方面的专门组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '原因在于\n',
            '教会的中立性，\n',
            '也只能这么说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过资料馆收到的\n',
            '古代遗物已经失去了力量，\n',
            '不属于要回收的对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_7C1')

    def _loc_741(): pass

    label('loc_741')

    ChrTalk(
        0x0008,
        (
            '教会确实有义务回收、\n',
            '调查古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '教会中也确实有\n',
            '这方面的专门组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '原因在于\n',
            '教会的中立性，\n',
            '也只能这么说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C1(): pass

    label('loc_7C1')

    Jump('loc_983')

    def _loc_7C4(): pass

    label('loc_7C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_875',
    )

    ChrTalk(
        0x0008,
        (
            '这座大圣堂和利贝尔王室\n',
            '有悠久的渊源。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '签字仪式的事儿也\n',
            '顺势承担下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是教会的本质说到底都是中立的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '唯一能做的就是\n',
            '一边向女神祈祷一边关注。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983')

    def _loc_875(): pass

    label('loc_875')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_983',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_94C',
    )

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '哟，莫非你\n',
            '就是那个人说的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F……那个人？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F我在这里应该\n',
            '没有熟人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，女神\n',
            '帮助那些帮助自己的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '愿你走上正确的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_983')

    def _loc_94C(): pass

    label('loc_94C')

    ChrTalk(
        0x0008,
        (
            '女神帮助那些帮助自己的人……\n',
            '愿你走上正确的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_983(): pass

    label('loc_983')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x987
@scena.Code('func_04_987')
def func_04_987():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_AB3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A4F',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有两个\n',
            '可疑的男人把给凯文\n',
            '神父的东西放下就走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然东西不大，\n',
            '可是包装得很严实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大主教大人要我马上\n',
            '呈交给凯文神父，我就照办了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里面到底是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_AB0')

    def _loc_A4F(): pass

    label('loc_A4F')

    ChrTalk(
        0x00FE,
        (
            '刚才有两个\n',
            '可疑的男人把给凯文\n',
            '神父的东西放下就走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然东西不大，\n',
            '可是包装得很严实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AB0(): pass

    label('loc_AB0')

    Jump('loc_E1E')

    def _loc_AB3(): pass

    label('loc_AB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_BAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B54',
    )

    ChrTalk(
        0x00FE,
        (
            '关于『星杯骑士团』，\n',
            '我也不是很了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是大主教大人也不是\n',
            '全部都了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在骑士团的职务的关系下，\n',
            '可能这样也是\n',
            '不得已的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_BA8')

    def _loc_B54(): pass

    label('loc_B54')

    ChrTalk(
        0x00FE,
        (
            '关于『星杯骑士团』，\n',
            '我也不是很了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是大主教大人也不是\n',
            '全部都了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BA8(): pass

    label('loc_BA8')

    Jump('loc_E1E')

    def _loc_BAB(): pass

    label('loc_BAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_C02',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，你好像有烦恼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神啊，请你指引\n',
            '他们所迷失的道路吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E1E')

    def _loc_C02(): pass

    label('loc_C02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C63',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才傍晚的弥撒\n',
            '做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，我看到了\n',
            '那个游击士，\n',
            '是不是发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E1E')

    def _loc_C63(): pass

    label('loc_C63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_CFE',
    )

    ChrTalk(
        0x00FE,
        (
            '这次从总部派来的那个\n',
            '凯文神父真是个奇怪的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为神职者来说看上去略显轻薄，\n',
            '我都有点担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莫非巡回神父中有很多\n',
            '那样的人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E1E')

    def _loc_CFE(): pass

    label('loc_CFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_E1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB1',
    )

    ChrTalk(
        0x00FE,
        (
            '前几天我去圣海姆门的时候，\n',
            '碰到了那场地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说好歹是平息了，\n',
            '不过蔡斯的人们现在\n',
            '应该也还抱有不安吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为地震毫无预兆，\n',
            '不知何时就会发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_E1E')

    def _loc_DB1(): pass

    label('loc_DB1')

    ChrTalk(
        0x00FE,
        (
            '虽说好歹是平息了，\n',
            '不过蔡斯的人们现在\n',
            '应该也还抱有不安吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为地震毫无预兆，\n',
            '不知何时就会发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E1E(): pass

    label('loc_E1E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xE22
@scena.Code('func_05_E22')
def func_05_E22():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_EB8',
    )

    ChrTalk(
        0x00FE,
        (
            '凯文神父和大主教大人\n',
            '说话到很晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来就马上出去了……\n',
            '还没有回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来这次的事大主教大人和\n',
            '凯文神父似乎知道一些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11AA')

    def _loc_EB8(): pass

    label('loc_EB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_F32',
    )

    ChrTalk(
        0x00FE,
        (
            '在昨晚的事件中有很多亲卫队\n',
            '士兵受伤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，空之女神爱德丝啊……\n',
            '请保佑那些勇敢而又有气节的人们吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11AA')

    def _loc_F32(): pass

    label('loc_F32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_F9D',
    )

    ChrTalk(
        0x00FE,
        (
            '有封信是给\n',
            '凯文神父的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可他本人却还没\n',
            '返回大圣堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '到底去了哪儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11AA')

    def _loc_F9D(): pass

    label('loc_F9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_102A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Return,
        ),
        'loc_1000',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有游击士\n',
            '来向我打听情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过已经回去了，\n',
            '估计应该到协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1027')

    def _loc_1000(): pass

    label('loc_1000')

    ChrTalk(
        0x00FE,
        (
            '那家人我记得，\n',
            '给人很深的印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1027(): pass

    label('loc_1027')

    Jump('loc_11AA')

    def _loc_102A(): pass

    label('loc_102A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1131',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10D6',
    )

    ChrTalk(
        0x00FE,
        (
            '上次我碰到了\n',
            '巡回神父凯文先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然大主教大人说巡回\n',
            '神父的工作很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过凯文先生\n',
            '完全没给人那样的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这工作真的很累吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_112E')

    def _loc_10D6(): pass

    label('loc_10D6')

    ChrTalk(
        0x00FE,
        (
            '虽然大主教大人说巡回\n',
            '神父的工作很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过凯文先生\n',
            '完全没给人那样的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_112E(): pass

    label('loc_112E')

    Jump('loc_11AA')

    def _loc_1131(): pass

    label('loc_1131')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_11AA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，终于\n',
            '圣歌集的修理结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从修女艾伦\n',
            '消失以后\n',
            '我就变得很忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能早点找到\n',
            '接替她的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11AA(): pass

    label('loc_11AA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x11AE
@scena.Code('func_06_11AE')
def func_06_11AE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11E2',
    )

    ChrTalk(
        0x00FE,
        (
            '这种时候真的该\n',
            '向女神献上祈祷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134C')

    def _loc_11E2(): pass

    label('loc_11E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1219',
    )

    ChrTalk(
        0x00FE,
        (
            '空之女神啊！\n',
            '希望这座城市能重获安宁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134C')

    def _loc_1219(): pass

    label('loc_1219')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1247',
    )

    ChrTalk(
        0x00FE,
        (
            '祈祷是让人心情平静的最佳方式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134C')

    def _loc_1247(): pass

    label('loc_1247')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12A7',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才历史资料馆的\n',
            '馆长来了这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给大主教大人看了一样东西，\n',
            '那是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134C')

    def _loc_12A7(): pass

    label('loc_12A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1308',
    )

    ChrTalk(
        0x00FE,
        (
            '希望互不侵犯条约能让帝国和\n',
            '共和国的人们友好相处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神……请引导我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134C')

    def _loc_1308(): pass

    label('loc_1308')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_134C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们也是来祈祷的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神永远\n',
            '守护着我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_134C(): pass

    label('loc_134C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1350
@scena.Code('func_07_1350')
def func_07_1350():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000C,
        (
            '#0050250381V#050F艾丝蒂尔，你那边的\n',
            '询问已经结束了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250382V我这边还要花点时间，\n',
            '完了的话就回协会等我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x13CE
@scena.Code('func_08_13CE')
def func_08_13CE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000D,
        (
            '#0030250383V#020F艾丝蒂尔，你那边的\n',
            '询问已经结束了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250384V我这边还要花点时间，\n',
            '完了的话就回协会等我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x144C
@scena.Code('func_09_144C')
def func_09_144C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1459',
    )

    Jump('loc_1553')

    def _loc_1459(): pass

    label('loc_1459')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1490',
    )

    ChrTalk(
        0x00FE,
        (
            '要让心情平静，\n',
            '祈祷是最好的方式，奶奶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1553')

    def _loc_1490(): pass

    label('loc_1490')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_14BF',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，奶奶。\n',
            '你到底在祈求些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1553')

    def _loc_14BF(): pass

    label('loc_14BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_14F6',
    )

    ChrTalk(
        0x00FE,
        (
            '彩色玻璃……\n',
            '在夕阳下显得更加美丽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1553')

    def _loc_14F6(): pass

    label('loc_14F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1525',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，说起来\n',
            '这玻璃窗还真漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1553')

    def _loc_1525(): pass

    label('loc_1525')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1553',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，奶奶。\n',
            '格兰赛尔的教堂真宽敞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1553(): pass

    label('loc_1553')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1557
@scena.Code('func_0A_1557')
def func_0A_1557():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1564',
    )

    Jump('loc_167D')

    def _loc_1564(): pass

    label('loc_1564')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1599',
    )

    ChrTalk(
        0x00FE,
        (
            '是啊，老头子……\n',
            '这也是女神的恩惠啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_167D')

    def _loc_1599(): pass

    label('loc_1599')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_15E0',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，我得保密。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为人们说愿望\n',
            '说出来就不灵了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_167D')

    def _loc_15E0(): pass

    label('loc_15E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_160C',
    )

    ChrTalk(
        0x00FE,
        (
            '是啊，很有幻想的美感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_167D')

    def _loc_160C(): pass

    label('loc_160C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1637',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子，这个\n',
            '叫彩色玻璃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_167D')

    def _loc_1637(): pass

    label('loc_1637')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_167D',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么宽敞的地方，可以把\n',
            '我们家都装进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_167D(): pass

    label('loc_167D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1681
@scena.Code('func_0B_1681')
def func_0B_1681():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_168E',
    )

    Jump('loc_179E')

    def _loc_168E(): pass

    label('loc_168E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_16C5',
    )

    ChrTalk(
        0x00FE,
        (
            '女神啊……求你保佑我们兄弟\n',
            '一路平安吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_179E')

    def _loc_16C5(): pass

    label('loc_16C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_16FE',
    )

    ChrTalk(
        0x00FE,
        (
            '……嗯，我知道了。\n',
            '再给我一点时间好不好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_179E')

    def _loc_16FE(): pass

    label('loc_16FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1731',
    )

    ChrTalk(
        0x00FE,
        (
            '女神啊……\n',
            '请饶恕我弟弟的言行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_179E')

    def _loc_1731(): pass

    label('loc_1731')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1774',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，首先合上眼睛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后把手放在\n',
            '胸前祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_179E')

    def _loc_1774(): pass

    label('loc_1774')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_179E',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，你真是……稍微\n',
            '老实一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_179E(): pass

    label('loc_179E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x17A2
@scena.Code('func_0C_17A2')
def func_0C_17A2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_17AF',
    )

    Jump('loc_189A')

    def _loc_17AF(): pass

    label('loc_17AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_17D5',
    )

    ChrTalk(
        0x00FE,
        (
            '我说，我们早点回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189A')

    def _loc_17D5(): pass

    label('loc_17D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_181D',
    )

    ChrTalk(
        0x00FE,
        (
            '你说好今天要\n',
            '陪我玩的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不能在女神面前\n',
            '撒谎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189A')

    def _loc_181D(): pass

    label('loc_181D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1854',
    )

    ChrTalk(
        0x00FE,
        (
            '已经傍晚了啊……\n',
            '弥撒真是像在上刑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189A')

    def _loc_1854(): pass

    label('loc_1854')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_187F',
    )

    ChrTalk(
        0x00FE,
        (
            '不嘛不嘛～！\n',
            '我绝不要祈祷～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189A')

    def _loc_187F(): pass

    label('loc_187F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_189A',
    )

    ChrTalk(
        0x00FE,
        (
            '教堂太无聊了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_189A(): pass

    label('loc_189A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x189E
@scena.Code('func_0D_189E')
def func_0D_189E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_18AB',
    )

    Jump('loc_19B6')

    def _loc_18AB(): pass

    label('loc_18AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_18D4',
    )

    ChrTalk(
        0x00FE,
        (
            '女神，感谢您\n',
            '保佑我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B6')

    def _loc_18D4(): pass

    label('loc_18D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1905',
    )

    ChrTalk(
        0x00FE,
        (
            '女神，今天也请您\n',
            '保佑我们安康……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B6')

    def _loc_1905(): pass

    label('loc_1905')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1932',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，傍晚的弥撒\n',
            '结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B6')

    def _loc_1932(): pass

    label('loc_1932')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1982',
    )

    ChrTalk(
        0x00FE,
        (
            '大圣堂的庄严肃穆\n',
            '真是感人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后是不是该\n',
            '认真地来教堂呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B6')

    def _loc_1982(): pass

    label('loc_1982')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_19B6',
    )

    ChrTalk(
        0x00FE,
        (
            '这就是格兰赛尔大圣堂……\n',
            '果然名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19B6(): pass

    label('loc_19B6')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x19BA
@scena.Code('func_0E_19BA')
def func_0E_19BA():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
