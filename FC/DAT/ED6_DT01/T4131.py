import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
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
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
    ]

# id: 0x10001 offset: 0xEA
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '利瓦尔牧师',
            x                   = -131900,
            z                   = 0,
            y                   = 6270,
            direction           = 3,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '修女诺雅',
            x                   = 2140,
            z                   = 0,
            y                   = 15980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '修女艾伦',
            x                   = -3470,
            z                   = 0,
            y                   = 510,
            direction           = 110,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '希丝娜',
            x                   = -3160,
            z                   = 0,
            y                   = 13260,
            direction           = 352,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 4180,
            z                   = 0,
            y                   = 9260,
            direction           = 2,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 200,
            z                   = 0,
            y                   = 14310,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x20A
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
            talkFunctionIndex   = 0x000B,
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
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x252
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 7, 0x64F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26F',
    )

    ChrSetPos(0x0008, 72000, 4000, 6060, 0)

    def _loc_26F(): pass

    label('loc_26F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_2A5',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 3020, 0, 13250, 340)
    ChrSetPos(0x000F, 4040, 0, 13250, 1)

    Jump('loc_2EF')

    def _loc_2A5(): pass

    label('loc_2A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2CA',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x0008, 71980, 4000, 6250, 0)

    Jump('loc_2EF')

    def _loc_2CA(): pass

    label('loc_2CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_2D4',
    )

    Jump('loc_2EF')

    def _loc_2D4(): pass

    label('loc_2D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    Jump('loc_2EF')

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_2E8',
    )

    Jump('loc_2EF')

    def _loc_2E8(): pass

    label('loc_2E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_2EF',
    )

    def _loc_2EF(): pass

    label('loc_2EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2FE',
    )

    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_436')

    def _loc_2FE(): pass

    label('loc_2FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_30D',
    )

    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_436')

    def _loc_30D(): pass

    label('loc_30D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_32D',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x0008, 72000, 4000, 6060, 0)

    Jump('loc_436')

    def _loc_32D(): pass

    label('loc_32D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_341',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_436')

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_36D',
    )

    ChrSetPos(0x000B, -2130, 0, 15890, 180)
    ChrSetPos(0x0009, 2440, 1000, 18600, 180)

    Jump('loc_436')

    def _loc_36D(): pass

    label('loc_36D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3AA',
    )

    ChrSetPos(0x000B, -133770, 0, 64950, 15)
    ChrSetPos(0x0009, 72000, 4000, 5780, 0)
    ChrSetPos(0x000A, -71370, 0, 3320, 90)

    Jump('loc_436')

    def _loc_3AA(): pass

    label('loc_3AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3DB',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000B, -2130, 0, 15890, 180)
    ChrSetPos(0x0009, 2440, 1000, 18600, 180)

    Jump('loc_436')

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3EA',
    )

    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_436')

    def _loc_3EA(): pass

    label('loc_3EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_416',
    )

    ChrSetPos(0x000B, -2130, 0, 15890, 180)
    ChrSetPos(0x0009, 2440, 1000, 18600, 180)

    Jump('loc_436')

    def _loc_416(): pass

    label('loc_416')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_42A',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0010)

    Jump('loc_436')

    def _loc_42A(): pass

    label('loc_42A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_436',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_436(): pass

    label('loc_436')

    Return()

# id: 0x0001 offset: 0x437
@scena.Code('func_01_437')
def func_01_437():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_46A',
    )

    OP_B1('t4131_y')

    Jump('loc_473')

    def _loc_46A(): pass

    label('loc_46A')

    OP_B1('t4131_n')

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_483',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_483(): pass

    label('loc_483')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 7, 0x64F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_493',
    )

    OP_64(0x00, 0x0001)

    def _loc_493(): pass

    label('loc_493')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4A1',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_506')

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4AB',
    )

    Jump('loc_506')

    def _loc_4AB(): pass

    label('loc_4AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4B9',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_506')

    def _loc_4B9(): pass

    label('loc_4B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4C3',
    )

    Jump('loc_506')

    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4CD',
    )

    Jump('loc_506')

    def _loc_4CD(): pass

    label('loc_4CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4D7',
    )

    Jump('loc_506')

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4E1',
    )

    Jump('loc_506')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4EB',
    )

    Jump('loc_506')

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4F5',
    )

    Jump('loc_506')

    def _loc_4F5(): pass

    label('loc_4F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4FF',
    )

    Jump('loc_506')

    def _loc_4FF(): pass

    label('loc_4FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_506',
    )

    def _loc_506(): pass

    label('loc_506')

    Return()

# id: 0x0002 offset: 0x507
@scena.Code('func_02_507')
def func_02_507():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_51C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_507')

    def _loc_51C(): pass

    label('loc_51C')

    Return()

# id: 0x0003 offset: 0x51D
@scena.Code('func_03_51D')
def func_03_51D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0010,
        (
            '#0360140892V#610F因为平时太忙，\n',
            '所以这次我更要好好地祷告了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360140893V看来到大圣堂\n',
            '还得把至今为止偷的懒\n',
            '一起做个忏悔才行呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x5AF
@scena.Code('func_04_5AF')
def func_04_5AF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000F,
        (
            '#0370140896V#620F真是难得，\n',
            '今天小姐竟然说要去教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x5F0
@scena.Code('func_05_5F0')
def func_05_5F0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_65E',
    )

    ChrTalk(
        0x000E,
        (
            '#0100140854V#170F对了，\n',
            '你们也是来找大主教的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100140855V大主教他刚才到祭器室去了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_931')

    def _loc_65E(): pass

    label('loc_65E')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '#0100140841V#170F哦，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140842V#001F是尤莉亚中尉啊，\n',
            '在这里做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0100140843V#170F在教会潜伏期间，\n',
            '我受到了大主教的诸多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100140844V这次是来向他表示谢意，\n',
            '并说明事情的详细情况的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140845V#501F啊，原来是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0100140846V#170F对了，\n',
            '我也要向你们表示感谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100140847V这回能够救出女王陛下和公主殿下，\n',
            '真的多亏了你们两个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100140848V如果只靠我们是无法做到的……\n',
            '真是太感谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140849V#000F哪里，如果只有我们\n',
            '而没有尤莉亚中尉的话，\n',
            '也不知道能不能成功呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140850V而且救助女王陛下这件事\n',
            '是我们理所当然应该协助的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140851V#001F所以啦，不用那么客气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0100140852V#173F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100140853V#171F是吗，谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_931(): pass

    label('loc_931')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x935
@scena.Code('func_06_935')
def func_06_935():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_942',
    )

    Jump('loc_A39')

    def _loc_942(): pass

    label('loc_942')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_94C',
    )

    Jump('loc_A39')

    def _loc_94C(): pass

    label('loc_94C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_956',
    )

    Jump('loc_A39')

    def _loc_956(): pass

    label('loc_956')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_9A6',
    )

    ChrTalk(
        0x00FE,
        (
            '大主教的教导\n',
            '真的很有意义哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家要是\n',
            '都能常来听听就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A39')

    def _loc_9A6(): pass

    label('loc_9A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_9B0',
    )

    Jump('loc_A39')

    def _loc_9B0(): pass

    label('loc_9B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_9BA',
    )

    Jump('loc_A39')

    def _loc_9BA(): pass

    label('loc_9BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_A14',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，大圣堂的礼拜堂\n',
            '不愧是洗涤心灵之处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '愿妻子也能得到\n',
            '女神的祝福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A39')

    def _loc_A14(): pass

    label('loc_A14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_A1E',
    )

    Jump('loc_A39')

    def _loc_A1E(): pass

    label('loc_A1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_A28',
    )

    Jump('loc_A39')

    def _loc_A28(): pass

    label('loc_A28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_A32',
    )

    Jump('loc_A39')

    def _loc_A32(): pass

    label('loc_A32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_A39',
    )

    def _loc_A39(): pass

    label('loc_A39')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xA3D
@scena.Code('func_07_A3D')
def func_07_A3D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_A9F',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然发生了许多事，\n',
            '但最终还是回归到了和平的日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是因为女神的指引啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3D')

    def _loc_A9F(): pass

    label('loc_A9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_AF7',
    )

    ChrTalk(
        0x00FE,
        (
            '从刚才就听到\n',
            '外面在吵吵闹闹的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不行啊……\n',
            '不能集中精神祈祷了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3D')

    def _loc_AF7(): pass

    label('loc_AF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_B38',
    )

    ChrTalk(
        0x00FE,
        (
            '那位最近新来的修女\n',
            '今天不在呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是生病了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3D')

    def _loc_B38(): pass

    label('loc_B38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_BE2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_B85',
    )

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '本来想再祈祷一会儿的，\n',
            '但也不能在这里呆到太晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BDF')

    def _loc_B85(): pass

    label('loc_B85')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '已经这么晚了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '本来想再祈祷一会儿的，\n',
            '但也不能在这里呆到太晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDF(): pass

    label('loc_BDF')

    Jump('loc_F3D')

    def _loc_BE2(): pass

    label('loc_BE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_C2E',
    )

    ChrTalk(
        0x00FE,
        (
            '我今天来大圣堂这里，\n',
            '是为了祈祷女王陛下的身体\n',
            '能够早日康复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3D')

    def _loc_C2E(): pass

    label('loc_C2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_D2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_C8B',
    )

    ChrTalk(
        0x00FE,
        (
            '大崩坏以后，\n',
            '这个世界是以教会为中心重新建立的，\n',
            '难道大家都忘记了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_C8B(): pass

    label('loc_C8B')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '导力器发明之后，\n',
            '生活就更加方便了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '人们渐渐地不再信仰女神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大崩坏以后，\n',
            '这个世界是以教会为中心重新建立的，\n',
            '难道大家都忘记了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2C(): pass

    label('loc_D2C')

    Jump('loc_F3D')

    def _loc_D2F(): pass

    label('loc_D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_E26',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_DA3',
    )

    ChrTalk(
        0x00FE,
        (
            '来教会祈祷的人数\n',
            '最近一直在减少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从主日学校毕业后\n',
            '很快就不来教会的人，\n',
            '却变得多起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E23')

    def _loc_DA3(): pass

    label('loc_DA3')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '来教会祈祷的人数\n',
            '最近一直在减少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从主日学校毕业后\n',
            '很快就不来教会的人，\n',
            '却变得多起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得真是很遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E23(): pass

    label('loc_E23')

    Jump('loc_F3D')

    def _loc_E26(): pass

    label('loc_E26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_E79',
    )

    ChrTalk(
        0x00FE,
        (
            '大主教和牧师的布教\n',
            '都讲得非常棒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '方便的话，你们也来听听吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3D')

    def _loc_E79(): pass

    label('loc_E79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_EB6',
    )

    ChrTalk(
        0x00FE,
        (
            '孕育了我生命的女神啊，\n',
            '我每天都会虔诚祈祷的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3D')

    def _loc_EB6(): pass

    label('loc_EB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_EF3',
    )

    ChrTalk(
        0x00FE,
        (
            '女神啊，今天又平平安安地过去了，\n',
            '感谢之至……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3D')

    def _loc_EF3(): pass

    label('loc_EF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_F3D',
    )

    ChrTalk(
        0x00FE,
        (
            '女神爱德丝\n',
            '一直都在保佑着我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要珍惜每一天的幸福生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F3D(): pass

    label('loc_F3D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xF41
@scena.Code('func_08_F41')
def func_08_F41():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_F4E',
    )

    Jump('loc_1479')

    def _loc_F4E(): pass

    label('loc_F4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_F58',
    )

    Jump('loc_1479')

    def _loc_F58(): pass

    label('loc_F58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_F62',
    )

    Jump('loc_1479')

    def _loc_F62(): pass

    label('loc_F62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_F6C',
    )

    Jump('loc_1479')

    def _loc_F6C(): pass

    label('loc_F6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_10DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_FA9',
    )

    ChrTalk(
        0x00FE,
        (
            '#0100141517V呵呵，今天的决赛请加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D7')

    def _loc_FA9(): pass

    label('loc_FA9')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0100141512V啊，艾丝蒂尔小姐、约修亚先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100141513V昨天你们\n',
            '平安无事地回去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141514V#008F啊，嗯，是的。\n',
            '平安无事地回去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141515V#007F（唔……\n',
            '　其实我知道她就是尤莉亚小姐，\n',
            '　不过不知道该怎么去和她谈话才好呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141516V#010F（我想跟平时一样就可以吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D7(): pass

    label('loc_10D7')

    Jump('loc_1479')

    def _loc_10DA(): pass

    label('loc_10DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_111B',
    )

    ChrTalk(
        0x00FE,
        (
            '#0100141518V现在是休息时间，\n',
            '可以从这里看看云彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1479')

    def _loc_111B(): pass

    label('loc_111B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_116C',
    )

    ChrTalk(
        0x00FE,
        (
            '#0100141519V早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100141520V早晨的弥撒\n',
            '马上就要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1479')

    def _loc_116C(): pass

    label('loc_116C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1176',
    )

    Jump('loc_1479')

    def _loc_1176(): pass

    label('loc_1176')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1468',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 5, 0x67D)),
            Expr.Return,
        ),
        'loc_11B0',
    )

    ChrTalk(
        0x00FE,
        (
            '#0100141534V昨天真的是\n',
            '多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1465')

    def _loc_11B0(): pass

    label('loc_11B0')

    SetScenaFlags(ScenaFlag(0x00CF, 5, 0x67D))

    ChrTalk(
        0x00FE,
        (
            '#0100141521V啊……你们几位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100141522V昨天承蒙你们的帮助，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141523V#004F啊，你是昨天的修女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100141524V那个……\n',
            '真是感到抱歉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100141525V得到了你们的帮助，\n',
            '但因为我的缘故，\n',
            '让你们遇到不愉快的事情了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141526V#505F不愉快？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141527V#010F你不记得了吗，\n',
            '昨天那些士兵在那里胡搅蛮缠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141528V#001F啊～那件事啊，\n',
            '不用在意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141529V#009F是那些家伙太可恶了嘛。\n',
            '根本就是脑袋有问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141530V#000F对了，\n',
            '那之后他们有平安护送你回来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100141531V是、是的，请别担心。\n',
            '他们平安地把我送了回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141532V#000F是这样啊，\n',
            '那么以后外出的时候要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100141533V好的，\n',
            '真是多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1465(): pass

    label('loc_1465')

    Jump('loc_1479')

    def _loc_1468(): pass

    label('loc_1468')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1472',
    )

    Jump('loc_1479')

    def _loc_1472(): pass

    label('loc_1472')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1479',
    )

    def _loc_1479(): pass

    label('loc_1479')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x147D
@scena.Code('func_09_147D')
def func_09_147D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_14F4',
    )

    ChrTalk(
        0x00FE,
        (
            '大街上的人们脸上都带着愉快的表情，\n',
            '看着他们让我的心情很舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '愿大家都受到\n',
            '女神爱德丝的祝福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_14F4(): pass

    label('loc_14F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_155B',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们好像\n',
            '还在搜捕亲卫队啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是说起来，\n',
            '他们至今也没能找到\n',
            '一个亲卫队的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_155B(): pass

    label('loc_155B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 7, 0x64F)),
            Expr.Return,
        ),
        'loc_15C9',
    )

    ChrTalk(
        0x00FE,
        (
            '艾伦虽然是个路痴，\n',
            '不过却相当懂得礼仪，\n',
            '而且也很热心帮助别人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她这么忙也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_15C9(): pass

    label('loc_15C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1648',
    )

    ChrTalk(
        0x00FE,
        (
            '你们……\n',
            '是来找艾伦的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想大主教应该知道\n',
            '她现在在哪儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大主教在这个大圣堂\n',
            '东南方的祭祀用具室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_1648(): pass

    label('loc_1648')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1686',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，空之女神爱德丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天又平安度过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_1686(): pass

    label('loc_1686')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_16EA',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典结束之后，\n',
            '我想在大圣堂这里\n',
            '举行一个义卖会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从现在开始就要着手准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_16EA(): pass

    label('loc_16EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_17E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1743',
    )

    ChrTalk(
        0x00FE,
        (
            '今天必须将典礼上\n',
            '使用的圣歌集整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咦，\n',
            '艾伦她去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17E0')

    def _loc_1743(): pass

    label('loc_1743')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '今天之内必须将典礼上\n',
            '使用的圣歌集整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至今为止还剩两百多本，\n',
            '看来够得辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咦，\n',
            '艾伦她去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不会又在\n',
            '什么地方迷路了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17E0(): pass

    label('loc_17E0')

    Jump('loc_1A31')

    def _loc_17E3(): pass

    label('loc_17E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_181E',
    )

    ChrTalk(
        0x00FE,
        (
            '空之女神爱德丝啊……\n',
            '今天也请您护佑我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_181E(): pass

    label('loc_181E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_18CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1874',
    )

    ChrTalk(
        0x00FE,
        (
            '奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还想拜托她办点事的……\n',
            '艾伦又跑到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CC')

    def _loc_1874(): pass

    label('loc_1874')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还想拜托她办点事的……\n',
            '艾伦又跑到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '头疼啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18CC(): pass

    label('loc_18CC')

    Jump('loc_1A31')

    def _loc_18CF(): pass

    label('loc_18CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1909',
    )

    ChrTalk(
        0x00FE,
        (
            '好，新的一天开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也要努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_1909(): pass

    label('loc_1909')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1965',
    )

    ChrTalk(
        0x00FE,
        (
            '修女艾伦\n',
            '不会出了什么事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她去了艾尔贝周游道，\n',
            '到现在都还没有回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_1965(): pass

    label('loc_1965')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1A31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_19AC',
    )

    ChrTalk(
        0x00FE,
        (
            '几天前这里\n',
            '新来了一位修女，\n',
            '刚才出去采摘药草了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_19AC(): pass

    label('loc_19AC')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '不知道到洛连特教会\n',
            '赴任的梅现在可好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是担任\n',
            '教育任务的修女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '几天前这里\n',
            '新来了一位修女，\n',
            '刚才出去采摘药草了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A31(): pass

    label('loc_1A31')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1A35
@scena.Code('func_0A_1A35')
def func_0A_1A35():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1A8E',
    )

    ChrTalk(
        0x00FE,
        (
            '能够顺利地举行诞辰庆典，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是因为\n',
            '有女神的保佑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1A8E(): pass

    label('loc_1A8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1AD3',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么那些士兵\n',
            '看上去很慌张呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1AD3(): pass

    label('loc_1AD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1C45',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1B5D',
    )

    ChrTalk(
        0x00FE,
        (
            '分离正是新的相聚的开始，\n',
            '人的一生就在\n',
            '这个过程中循环不息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人生，就是这样由一根\n',
            '所谓命运的丝线所编织而成的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C42')

    def _loc_1B5D(): pass

    label('loc_1B5D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '落叶聚还散，寒鸦栖复惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '分离正是新的相聚的开始，\n',
            '人的一生就在\n',
            '这个过程中循环不息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人生，就是这样由一根\n',
            '所谓命运的丝线所编织而成的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们人类\n',
            '虽然难以预测\n',
            '自身的命运……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但女神应该\n',
            '是知晓一切的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C42(): pass

    label('loc_1C42')

    Jump('loc_2146')

    def _loc_1C45(): pass

    label('loc_1C45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1CBD',
    )

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔大圣堂历史悠久，\n',
            '今年是设立后的１１２０周年呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该是同利贝尔王家\n',
            '在大致相同的时候兴建的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1CBD(): pass

    label('loc_1CBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1D40',
    )

    ChrTalk(
        0x00FE,
        (
            '如同游击士协会那样，\n',
            '七耀教会在整个大陆都遍布了\n',
            '等同于协会支部的分支设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，\n',
            '格兰赛尔大圣堂也是其中之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1D40(): pass

    label('loc_1D40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1E90',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1DCA',
    )

    ChrTalk(
        0x00FE,
        (
            '大崩坏之后的人们\n',
            '那种努力生存的精神\n',
            '可以说焕发出了生命之光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果换一种角度看问题，\n',
            '大崩坏也许是女神的试练呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E8D')

    def _loc_1DCA(): pass

    label('loc_1DCA')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '大崩坏之后，幸存下来的人们\n',
            '熬过了暗无天日的时代，活了下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '生活状况虽然凄苦，\n',
            '但是那种努力生存的精神\n',
            '可以说焕发出了生命之光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果换一种角度看问题，\n',
            '大崩坏也许是女神的试练呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E8D(): pass

    label('loc_1E8D')

    Jump('loc_2146')

    def _loc_1E90(): pass

    label('loc_1E90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F7B',
    )

    ChrTalk(
        0x00FE,
        (
            '只要世界存在，\n',
            '就会有夏去冬来，昼夜更替……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '播种收获都在不断重复，\n',
            '永无休止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大崩坏之后，人们虽然饱受苦痛，\n',
            '但最后仍生存下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然看着同样的事情不断重复，\n',
            '但这个世界总是一点一点地\n',
            '向着美好的方向前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1F7B(): pass

    label('loc_1F7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1FE4',
    )

    ChrTalk(
        0x00FE,
        (
            '世界起源之初，\n',
            '大地无形无态，\n',
            '由黑暗与狂风所支配。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将光明赋予大地的\n',
            '就是女神爱德丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_1FE4(): pass

    label('loc_1FE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_20F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2043',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天多亏了你们\n',
            '救了修女艾伦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是非常感谢。\n',
            '愿你们的前路充满光明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20EF')

    def _loc_2043(): pass

    label('loc_2043')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哦，你们是游击士协会的朋友吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天多亏了你们\n',
            '救了修女艾伦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她外出采摘药草却一直未归，\n',
            '让我们很是担心了一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是非常感谢。\n',
            '愿你们的前路充满光明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20EF(): pass

    label('loc_20EF')

    Jump('loc_2146')

    def _loc_20F2(): pass

    label('loc_20F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_211F',
    )

    ChrTalk(
        0x00FE,
        (
            '大街上也\n',
            '开始变得热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2146')

    def _loc_211F(): pass

    label('loc_211F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2146',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到七耀教会的大圣堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2146(): pass

    label('loc_2146')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x214A
@scena.Code('func_0B_214A')
def func_0B_214A():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x214F
@scena.Code('func_0C_214F')
def func_0C_214F():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 7, 0x64F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2787',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 71280, 4000, 4900, 0)
    ChrSetPos(0x0102, 72450, 4000, 4890, 0)
    ChrSetPos(0x0108, 71610, 4000, 4030, 0)
    ChrTurnDirection(0x0008, 0x0108, 0)
    SetScenaFlags(ScenaFlag(0x00C9, 7, 0x64F))
    OP_28(0x004B, 0x01, 0x0400)
    CameraMove(71530, 4000, 5910, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2320130366V哦，你们几位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130367V#000F嗯，那个……\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130368V#010F请问那位名叫艾伦的修女\n',
            '现在在大圣堂这里吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130369V哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130370V这么说，\n',
            '你们就是她的协助者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010130371V#004F咦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130372V#015F……看来您对情况也相当了解呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130373V#012F她的委托完成了，我们是来报告的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130374V很遗憾，\n',
            '她现在已经不在大圣堂里面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130375V今天早晨，她向我打了声招呼，\n',
            '然后就自己离开这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130376V#580F到、到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130377V很遗憾，我不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130378V因为我们和王家长期保持着良好的关系，\n',
            '所以这次就让她隐藏在了教会里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130379V不过关于这回的事件，\n',
            '她并没有告诉我详情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130380V很可能是因为\n',
            '不想给教会带来麻烦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130381V#013F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130382V不过请放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130383V在离开这里时，\n',
            '她的眼中充满了希望的光芒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130384V绝不是因为穷途末路、\n',
            '自暴自弃而离开的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130385V#007F听、听您这么一说，\n',
            '我就放心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130386V#505F可是这么一来，\n',
            '就不能和亲卫队取得联络了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130387V#072F也只能暂时这样了。\n',
            '毕竟我们也不是那么容易就能找到他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130388V#074F暂且只有把亲卫队的事放置在一旁了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130389V#012F没办法，也只有这样了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130390V看起来，\n',
            '你们好像遇到了很大的困难啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130391V女神啊，帮助那些自强不息的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2320130392V只要你们能够全力以赴的话，\n',
            '女神一定为你们指明方向的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_277A')
    def lambda_277A():
        ChrSetDirection(0x0008, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_277A)

    EventEnd(0x00)

    Jump('loc_318A')

    def _loc_2787(): pass

    label('loc_2787')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_28A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2800',
    )

    ChrTalk(
        0x0008,
        (
            '导力文明是个值得谈论的话题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '塞姆里亚人凭借他们的睿智，\n',
            '将世界以现在这个形态\n',
            '传承了下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_289F')

    def _loc_2800(): pass

    label('loc_2800')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '导力文明是个值得谈论的话题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '塞姆里亚人凭借他们的睿智，\n',
            '将世界以现在这个形态\n',
            '传承了下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们必须要\n',
            '切实地守护好它……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_289F(): pass

    label('loc_289F')

    Jump('loc_318A')

    def _loc_28A2(): pass

    label('loc_28A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2907',
    )

    ChrTalk(
        0x0008,
        (
            '用你们的眼睛\n',
            '去洞悉未知的一切吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '赶快前往应该去的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '愿女神引导你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318A')

    def _loc_2907(): pass

    label('loc_2907')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2972',
    )

    ChrTalk(
        0x0008,
        (
            '女神啊，帮助那些自强不息的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只要你们能够全力以赴的话，\n',
            '女神一定为你们指明方向的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318A')

    def _loc_2972(): pass

    label('loc_2972')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_29CB',
    )

    ChrTalk(
        0x0008,
        (
            '武术大会结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然不知道诞辰庆典会如何，\n',
            '但还是先做好准备吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318A')

    def _loc_29CB(): pass

    label('loc_29CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2B12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2A3F',
    )

    ChrTalk(
        0x0008,
        (
            '我今年还没见过\n',
            '科洛蒂娅公主\n',
            '来大圣堂这边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想必她一直在王城里\n',
            '陪伴着身体欠佳的陛下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B0F')

    def _loc_2A3F(): pass

    label('loc_2A3F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '这么说来，\n',
            '每年这个时候\n',
            '科洛蒂娅公主都会来大圣堂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了庆祝女王的诞辰庆典，\n',
            '公主都会来这里诚心祈祷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过我今年还没见到\n',
            '公主来过大圣堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想必她一直在王城里\n',
            '陪伴着身体欠佳的陛下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B0F(): pass

    label('loc_2B0F')

    Jump('loc_318A')

    def _loc_2B12(): pass

    label('loc_2B12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2C04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2B7F',
    )

    ChrTalk(
        0x0008,
        (
            '从今天开始市内的主要设施\n',
            '都成了重点巡逻的对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '刚才，\n',
            '这里也接到王国军的通告了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C01')

    def _loc_2B7F(): pass

    label('loc_2B7F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '王国军似乎\n',
            '加强了全城的警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从今天开始市内的主要设施\n',
            '都成了重点巡逻的对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '刚才，\n',
            '这里也接到王国军的通告了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C01(): pass

    label('loc_2C01')

    Jump('loc_318A')

    def _loc_2C04(): pass

    label('loc_2C04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2D1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2C3E',
    )

    ChrTalk(
        0x0008,
        (
            '教会也很想和王室\n',
            '构筑良好的关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D1B')

    def _loc_2C3E(): pass

    label('loc_2C3E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '百日战役时，\n',
            '七耀教会和游击士协会\n',
            '一同担当了调停的角色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然政教互相干涉\n',
            '绝非什么好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过只要双方充分理解，\n',
            '并能在机会适当时联手，\n',
            '就能将事情处理得很完美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '教会也很想和王室\n',
            '构筑良好的关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D1B(): pass

    label('loc_2D1B')

    Jump('loc_318A')

    def _loc_2D1E(): pass

    label('loc_2D1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2E34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2D98',
    )

    ChrTalk(
        0x0008,
        (
            '七耀教会和利贝尔王室\n',
            '常年保持着良好的关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '自从大崩坏之后，\n',
            '合作的关系至少\n',
            '维持了一千多年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E31')

    def _loc_2D98(): pass

    label('loc_2D98')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '七耀教会和利贝尔王室\n',
            '常年保持着良好的关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '自从大崩坏之后，\n',
            '合作的关系至少\n',
            '维持了一千多年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当然现在和艾莉茜雅女王的\n',
            '关系也很密切。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E31(): pass

    label('loc_2E31')

    Jump('loc_318A')

    def _loc_2E34(): pass

    label('loc_2E34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2FB0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2ED9',
    )

    ChrTalk(
        0x0008,
        (
            '大圣堂从混乱的时代开始直到今天，\n',
            '一直在这片土地上\n',
            '不懈地履行着属于自己的使命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '据说在利贝尔王国之中，\n',
            '还存在着更加古老的\n',
            '七耀教会的设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FAD')

    def _loc_2ED9(): pass

    label('loc_2ED9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '七耀教会是在大崩坏之后成立的，\n',
            '以为人们指明道路为己任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '大圣堂从混乱的时代开始直到今天，\n',
            '一直在这片土地上\n',
            '不懈地履行着属于自己的使命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '据说在利贝尔王国之中，\n',
            '还存在着更加古老的\n',
            '七耀教会的设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FAD(): pass

    label('loc_2FAD')

    Jump('loc_318A')

    def _loc_2FB0(): pass

    label('loc_2FB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3014',
    )

    ChrTalk(
        0x0008,
        (
            '为了让市民更有热情\n',
            '而举办的武术大会吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '杜南公爵是这么说的，\n',
            '真让人捉摸不透……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318A')

    def _loc_3014(): pass

    label('loc_3014')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_318A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_30AE',
    )

    ChrTalk(
        0x0008,
        (
            '城里竟然没有一个人\n',
            '知道陛下的具体情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想女管事希尔丹夫人应该知道，\n',
            '于是就想和她当面谈谈，\n',
            '却被身穿黑色盔甲的人断然拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318A')

    def _loc_30AE(): pass

    label('loc_30AE')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我本想为身体欠佳的陛下\n',
            '送些药草去的，\n',
            '于是向王城里的人询问了陛下的病状……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可是竟然没有一个人\n',
            '知道陛下的具体情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想女管事希尔丹夫人应该知道，\n',
            '于是就想和她当面谈谈，\n',
            '却被身穿黑色盔甲的人断然拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_318A(): pass

    label('loc_318A')

    TalkEnd(0x0008)

    Return()

# id: 0x000D offset: 0x318E
@scena.Code('func_0D_318E')
def func_0D_318E():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
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
