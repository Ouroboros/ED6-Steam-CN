import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2700_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2700   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2700.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2700._SN', 'ED6_DT01/T2700_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
        ('ED6_DT06/CH20059._CH', 'ED6_DT06/CH20059P._CP'),
        ('ED6_DT06/CH20113._CH', 'ED6_DT06/CH20113P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '哈恩队长',
            x                   = 5500,
            z                   = 5000,
            y                   = 0,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = 4500,
            z                   = 5000,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡露娜',
            x                   = -15300,
            z                   = 100,
            y                   = -11300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '士兵尼克斯',
            x                   = 18400,
            z                   = 5000,
            y                   = 1400,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '士兵威尔斯',
            x                   = -19800,
            z                   = 0,
            y                   = -2200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '梅尔凯斯',
            x                   = 4710,
            z                   = 5000,
            y                   = 2490,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '阿伊纳街道',
            x                   = -62340,
            z                   = 0,
            y                   = -1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡鲁迪亚隧道',
            x                   = 21320,
            z                   = 5000,
            y                   = 460,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x25A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x25A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x25A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 19830,
            triggerZ            = 5000,
            triggerY            = -50,
            triggerRange        = 800,
            actorX              = 19830,
            actorZ              = 6000,
            actorY              = -50,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -45890,
            triggerZ            = 0,
            triggerY            = 2240,
            triggerRange        = 1500,
            actorX              = -45890,
            actorZ              = 1700,
            actorY              = 2240,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2A2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2AC',
    )

    Jump('loc_2C8')

    def _loc_2AC(): pass

    label('loc_2AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2BB',
    )

    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_2C8')

    def _loc_2BB(): pass

    label('loc_2BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C8',
    )

    ChrClearFlags(0x0010, 0x0080)

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2E3',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_2E3(): pass

    label('loc_2E3')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_2F3'),
        (0x00000064, 'loc_32A'),
        (-1, 'loc_346'),
    )

    def _loc_2F3(): pass

    label('loc_2F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_314',
    )

    OP_28(0x0023, 0x01, 0x0001)
    Event(1, 0x0000)

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 3, 0x503)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_327',
    )

    SetScenaFlags(ScenaFlag(0x00A0, 3, 0x503))
    Event(0, func_0A_13ED)

    def _loc_327(): pass

    label('loc_327')

    Jump('loc_346')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_340',
    )

    SetScenaFlags(ScenaFlag(0x00A0, 1, 0x501))
    Event(0, func_09_F36)

    Jump('loc_343')

    def _loc_340(): pass

    label('loc_340')

    SetScenaFlags(ScenaFlag(0x00A7, 4, 0x53C))

    def _loc_343(): pass

    label('loc_343')

    Jump('loc_346')

    def _loc_346(): pass

    label('loc_346')

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x358
@scena.Code('func_01_358')
def func_01_358():
    OP_16(0x02, 4000, -146000, -128000, 196687)
    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_382',
    )

    OP_72(0x0002, 0x0010)
    OP_65(0x00, 0x0001)

    Jump('loc_395')

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 3, 0x503)),
            Expr.Return,
        ),
        'loc_395',
    )

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 160)

    def _loc_395(): pass

    label('loc_395')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1E),
            (Expr.PushLong, 0x11C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A9',
    )

    OP_28(0x002A, 0x01, 0x2000)

    def _loc_3A9(): pass

    label('loc_3A9')

    OP_1C(0x01, 0x00, 0x000E)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3C6'),
        (0x00000065, 'loc_3C6'),
        (0x00000066, 'loc_3CE'),
        (0x00000067, 'loc_3CE'),
        (-1, 'loc_3D6'),
    )

    def _loc_3C6(): pass

    label('loc_3C6')

    PlaySE(462, 0x01, 0x64)

    Jump('loc_3D6')

    def _loc_3CE(): pass

    label('loc_3CE')

    PlaySE(458, 0x01, 0x64)

    Jump('loc_3D6')

    def _loc_3D6(): pass

    label('loc_3D6')

    Return()

# id: 0x0002 offset: 0x3D7
@scena.Code('func_02_3D7')
def func_02_3D7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3D7')

    def _loc_3EC(): pass

    label('loc_3EC')

    Return()

# id: 0x0003 offset: 0x3ED
@scena.Code('func_03_3ED')
def func_03_3ED():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_410',
    )

    OP_8D(0x00FE, 13000, 2500, 1500, 0, 1500)

    Jump('func_03_3ED')

    def _loc_410(): pass

    label('loc_410')

    Return()

# id: 0x0004 offset: 0x411
@scena.Code('func_04_411')
def func_04_411():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_697',
    )

    ChrTalk(
        0x00FE,
        (
            '#1860170632V已经有空了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1860170633V如果可以的话，\n',
            '能请你们帮帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        (0x00000000, 'loc_4D1'),
        (0x00000001, 'loc_577'),
        (-1, 'loc_697'),
    )

    def _loc_4D1(): pass

    label('loc_4D1')

    OP_28(0x0023, 0x04, 0x08)

    ChrTalk(
        0x0101,
        (
            '#0010150127V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170635V谢谢了，真是帮大忙了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170636V那么就先到楼下去，\n',
            '我把详细的情况告诉你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    EventBegin(0x00)
    NewScene('ED6_DT01/T2710._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_697')

    def _loc_577(): pass

    label('loc_577')

    OP_28(0x0023, 0x01, 0x4000)

    ChrTalk(
        0x0101,
        (
            '#0010170626V#003F抱歉，\n',
            '现在大概不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170638V那还真是麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170639V那我们唯有\n',
            '先靠自己去说服他吧，\n',
            '虽然知道自己对这种事不是很擅长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170640V等办完事情，\n',
            '就请尽快过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170630V#010F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170642V唔，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 0)

    Jump('loc_697')

    def _loc_697(): pass

    label('loc_697')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x69B
@scena.Code('func_05_69B')
def func_05_69B():
    TalkBegin(0x000D)

    ChrTalk(
        0x00FE,
        (
            '#0320050561V呼，总算是完成了任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320050562V这里虽然很凉爽，\n',
            '但要一直站岗就很辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x0006 offset: 0x705
@scena.Code('func_06_705')
def func_06_705():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_859',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_79C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哟，是旅行者啊，\n',
            '还真是少见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在大家都去王都的时候，\n',
            '你们却要到卢安去观光游览吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '这也许另有一番趣味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_856')

    def _loc_79C(): pass

    label('loc_79C')

    ChrTalk(
        0x00FE,
        (
            '仔细想想，\n',
            '在观光的时候如果周围的人很少，\n',
            '行动不就更加自由了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里既有名胜古迹，\n',
            '又有便宜旅店……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，话又说回来，\n',
            '诞辰庆典只有现在这个时间才有哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔，苦恼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_856(): pass

    label('loc_856')

    Jump('loc_D74')

    def _loc_859(): pass

    label('loc_859')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_8EC',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，这么快就解除了对旅客的盘查，\n',
            '真是出乎预料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又要回复到\n',
            '以往的警戒状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道具体原因，\n',
            '但应该是抓住犯人了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D74')

    def _loc_8EC(): pass

    label('loc_8EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_93B',
    )

    ChrTalk(
        0x00FE,
        (
            '……现在关所正处于戒严状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，\n',
            '值勤期间禁止窃窃私语。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D74')

    def _loc_93B(): pass

    label('loc_93B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_A6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9F7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我们关所\n',
            '也收到了联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨日，\n',
            '蔡斯的所有导力器\n',
            '一下子都不能使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果相同的情况\n',
            '在卢安也发生的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '伦格兰德大桥就会\n',
            '一直打开而不能合上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A6A')

    def _loc_9F7(): pass

    label('loc_9F7')

    ChrTalk(
        0x00FE,
        (
            '中央工房\n',
            '制作出了许多奇怪的东西。\n',
            '它是个很大的建筑物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个造成导力停止的东西\n',
            '究竟是怎么制造出来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A6A(): pass

    label('loc_A6A')

    Jump('loc_D74')

    def _loc_A6D(): pass

    label('loc_A6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B10',
    )

    ChrTalk(
        0x00FE,
        (
            '过了这门，\n',
            '再往前走就是蔡斯地区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里面的卡鲁迪亚隧道\n',
            '和外面很不一样哦………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我能保证，对任何旅行者来说，\n',
            '这都会是一次非常新奇的旅程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D74')

    def _loc_B10(): pass

    label('loc_B10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_BB3',
    )

    ChrTalk(
        0x00FE,
        (
            '过了这门，\n',
            '再往前走就是蔡斯地区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里面的卡鲁迪亚隧道\n',
            '和外面很不一样哦………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我能保证，对任何旅行者来说，\n',
            '这都会是一次非常新奇的旅程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D74')

    def _loc_BB3(): pass

    label('loc_BB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_D0E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_CB0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C55',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '队长和副长都在\n',
            '拼命写刚才的报告书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我听说过公爵的传言，\n',
            '不过没想到会这么糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天由我来站岗\n',
            '真是太幸运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAD')

    def _loc_C55(): pass

    label('loc_C55')

    ChrTalk(
        0x00FE,
        (
            '虽然我听说过公爵的传言，\n',
            '不过没想到会这么糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天由我来站岗\n',
            '真是太幸运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CAD(): pass

    label('loc_CAD')

    Jump('loc_D0B')

    def _loc_CB0(): pass

    label('loc_CB0')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_CE4',
    )

    ChrTalk(
        0x00FE,
        (
            '好像有个蛮不讲理的人\n',
            '到关所来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0B')

    def _loc_CE4(): pass

    label('loc_CE4')

    ChrTalk(
        0x00FE,
        (
            '好像有个蛮不讲理的人\n',
            '到关所来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D0B(): pass

    label('loc_D0B')

    Jump('loc_D74')

    def _loc_D0E(): pass

    label('loc_D0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_D74',
    )

    ChrTalk(
        0x00FE,
        (
            '在这里站岗可以欣赏美丽的景色，\n',
            '空气也很清新，真是一份好差事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过到了冬天就辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D74(): pass

    label('loc_D74')

    TalkEnd(0x000E)

    Return()

# id: 0x0007 offset: 0xD78
@scena.Code('func_07_D78')
def func_07_D78():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 1, 0x501)),
            Expr.Return,
        ),
        'loc_DD9',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，欢迎你们来到\n',
            '『艾尔·雷登』关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要办通行手续的话，\n',
            '请到里面的柜台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EFC')

    def _loc_DD9(): pass

    label('loc_DD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_EB4',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_E32',
    )

    ChrTalk(
        0x00FE,
        (
            '有个看上去挺有钱的大叔\n',
            '一边抱怨一边走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB1')

    def _loc_E32(): pass

    label('loc_E32')

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_E78',
    )

    ChrTalk(
        0x00FE,
        (
            '从刚才开始\n',
            '里面就很吵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道发生什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB1')

    def _loc_E78(): pass

    label('loc_E78')

    ChrTalk(
        0x00FE,
        (
            '从刚才开始\n',
            '里面就很吵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道发生什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB1(): pass

    label('loc_EB1')

    Jump('loc_EFC')

    def _loc_EB4(): pass

    label('loc_EB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_EFC',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才从雷斯顿要塞\n',
            '有命令传达了过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是什么样的命令呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EFC(): pass

    label('loc_EFC')

    TalkEnd(0x000F)

    Return()

# id: 0x0008 offset: 0xF00
@scena.Code('func_08_F00')
def func_08_F00():
    TalkBegin(0x0010)

    ChrTalk(
        0x00FE,
        (
            '在遗迹这样的地方还会有瀑布，\n',
            '真是罕见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0010)

    Return()

# id: 0x0009 offset: 0xF36
@scena.Code('func_09_F36')
def func_09_F36():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(5900, 12000, 13400, 0)
    OP_6C(85000, 0)
    CameraSetDistance(8000, 0)
    OP_12(0x00007D00, 0x0003D090, 0x00000000)
    ChrSetPos(0x0101, -51400, 0, -1100, 90)
    ChrSetPos(0x0102, -52500, 0, -300, 90)
    ChrSetPos(0x0105, -52500, 0, -2100, 90)
    FadeIn(2000, 0)
    OP_12(0x00007D00, 0x0001FBD0, 0x00002EE0)

    @scena.Lambda('lambda_0FBC')
    def lambda_0FBC():
        CameraSetDistance(2800, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FBC)

    @scena.Lambda('lambda_0FCC')
    def lambda_0FCC():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FCC)

    Sleep(3000)

    @scena.Lambda('lambda_0FE1')
    def lambda_0FE1():
        CameraMove(-50000, 0, -1500, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FE1)

    Sleep(9000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 4, 0x53C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1066',
    )

    ChrTalk(
        0x0101,
        (
            '#0010070205V#501F#2P哎……\n',
            '这里的气氛真好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070206V与其说是关所，倒不如说是观光胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D5')

    def _loc_1066(): pass

    label('loc_1066')

    ChrTalk(
        0x0101,
        (
            '#0010070207V#501F#2P之前也来过这里……\n',
            '这里的气氛真好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070208V与其说是关所，倒不如说是观光胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D5(): pass

    label('loc_10D5')

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060070209V#040F其实，每年慕名前来\n',
            '观赏瀑布的观光客也不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1126')
    def lambda_1126():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1126)

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070210V#006F#2P啊，是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070211V嗯～～\n',
            '卢安地区的风景名胜还真不少呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070212V如果不是因为那个公爵捣乱的话，\n',
            '我也真想在这住一段时间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070213V#041F呵呵，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070214V#048F不过，我觉得洛连特\n',
            '也是个宁静得让人舒心的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070215V#004F#2P啊，这样说……\n',
            '科洛丝也去过洛连特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070216V#041F是的，\n',
            '五大都市我全部都去过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070217V#040F对了，\n',
            '过了这里就是蔡斯市……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070218V那是一个非常著名的城市，\n',
            '我想你们到了那里一定会大吃一惊的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070219V#000F#2P哎～是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070220V#001F嗯……\n',
            '开始有点期待了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020070221V#010F好了，\n',
            '我们这就进去办理通行手续吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070222V#006F#2P嗯，ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x13ED
@scena.Code('func_0A_13ED')
def func_0A_13ED():
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-5200, 5000, 7200, 0)
    ChrSetPos(0x0101, -5000, 5000, 6600, 90)
    ChrSetPos(0x0105, -6300, 5000, 7100, 90)
    ChrSetPos(0x0102, -6300, 5000, 5800, 90)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 160)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_145D')
    def lambda_145D():
        CameraSetDistance(5000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_145D)

    @scena.Lambda('lambda_146D')
    def lambda_146D():
        CameraMove(10900, 9200, 14500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_146D)

    @scena.Lambda('lambda_1485')
    def lambda_1485():
        OP_6C(24000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1485)

    Sleep(5000)

    ChrSetPos(0x000B, 10300, 6400, 3150, 0)
    ChrSetPos(0x000A, 900, 5000, 800, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x0101, 8300, 5000, 2500, 0)
    ChrSetPos(0x0105, 6800, 5000, 2500, 0)
    ChrSetPos(0x0102, 7700, 5000, 1000, 0)

    ChrTalk(
        0x0101,
        (
            '#0010070242V#001F#1P呜哇～好壮观啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_151E')
    def lambda_151E():
        CameraSetDistance(2800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_151E)

    @scena.Lambda('lambda_152E')
    def lambda_152E():
        CameraMove(7800, 5000, 2500, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_152E)

    Sleep(5000)

    ChrTalk(
        0x0101,
        (
            '#0010070243V#501F#4P嗯～虽说是瀑布，\n',
            '但却不是自然的河流，\n',
            '而是从水道流下而形成的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070244V#010F#4P我记得这条水道\n',
            '好像是叫『罗蔡水道』吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070245V是在中世纪建造的水道桥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060070246V#040F#3P是的，这里的水可是从\n',
            '瓦雷利亚湖直接流过来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070247V#007F#4P呼，在没有导力器的情况下，\n',
            '竟然也能完成这么大的工程啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070248V#006F#3P那么，那边的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16E9')
    def lambda_16E9():
        OP_6C(90000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16E9)

    @scena.Lambda('lambda_16F9')
    def lambda_16F9():
        CameraMove(17680, 5000, -70, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_16F9)

    @scena.Lambda('lambda_1711')
    def lambda_1711():
        CameraSetDistance(4250, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1711)

    @scena.Lambda('lambda_1721')
    def lambda_1721():
        OP_67(0, 3980, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1721)

    @scena.Lambda('lambda_1739')
    def lambda_1739():
        OP_6E(345, 4000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_1739)

    @scena.Lambda('lambda_1749')
    def lambda_1749():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1749)

    @scena.Lambda('lambda_1757')
    def lambda_1757():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1757)

    ChrSetDirection(0x0105, 90, 400)

    @scena.Lambda('lambda_176C')
    def lambda_176C():
        ChrWalkTo(0x00FE, 11400, 5000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_176C)

    Sleep(800)

    @scena.Lambda('lambda_178C')
    def lambda_178C():
        ChrWalkTo(0x00FE, 10900, 5000, -900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_178C)

    Sleep(300)

    @scena.Lambda('lambda_17AC')
    def lambda_17AC():
        ChrWalkTo(0x00FE, 9800, 5000, 700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_17AC)

    WaitForThreadExit(0x0101, 0x0002)
    ChrSetDirection(0x0101, 90, 0)
    WaitForThreadExit(0x0102, 0x0002)
    ChrSetDirection(0x0102, 90, 0)
    WaitForThreadExit(0x0105, 0x0002)
    ChrSetDirection(0x0105, 90, 0)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020070249V#010F……看来那边就是卡鲁迪亚隧道的入口了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070250V#501F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_20(0x000005DC)
    Fade(1000)
    ChrTurnDirection(0x0102, 0x0105, 0)
    ChrTurnDirection(0x0101, 0x0105, 0)
    ChrTurnDirection(0x0105, 0x0101, 0)
    ChrSetDirection(0x000B, 180, 0)
    CameraMove(11300, 5000, 540, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_21()
    PlayBGM(88)

    ChrTalk(
        0x0101,
        (
            '#0010070251V#505F……差不多要告别了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070252V#047F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070253V#040F对了，艾丝蒂尔你们\n',
            '打算巡游整个王国一周吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070254V说不定到了王都，\n',
            '我们还有机会再见面哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070255V#004F咦，真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070256V#045F嗯，因为我打算在\n',
            '女王诞辰庆典举行的时候回王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070257V也算是家里的亲戚聚会吧，\n',
            '不得不出席的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070258V#010F距离女王诞辰庆典，\n',
            '大概还有一个月吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070259V确实，\n',
            '那时候我们也差不多该到王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070260V#006F啊，那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070261V亲戚那里的事办完之后，\n',
            '一定要和王都的协会联络一下哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070262V那样应该就能再见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070263V#041F嗯，我一定会联络的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070264V#048F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070265V实在是太感谢你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070266V你们俩为大家所做的一切，\n',
            '我科洛丝，绝对不会忘记的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070267V#008F真、真是的～\n',
            '你又跟我们客气起来了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070268V#019F应该是我们说谢谢才对，\n',
            '这段时间承蒙你多方照顾了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070269V算是彼此彼此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070270V#542F哪里的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070271V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070272V#049F那个时候……和市长对决时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070273V我说了一些自以为是的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070274V『你终究还是只在乎你自己』……\n',
            '『真是可怜的人』什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070275V但是……\n',
            '我自己不也是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070276V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070277V#047F那句话就是我内心的写照，\n',
            '一直不断逃避自己的立场的写照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070278V孤儿院也好，学院也好，\n',
            '都只不过是我逃避的场所而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070279V#040F但是……\n',
            '艾丝蒂尔你们\n',
            '教会了我一样很重要的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070280V无论何时\n',
            '都要勇往直前的那份决心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070281V还有，守护身边的人的那份坚强……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070282V#041F谢谢，多亏了你们，\n',
            '我现在总算也有些勇气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070283V#506F虽、虽然不是很明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070284V能给你帮上忙，\n',
            '我们两个也会感到很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F63')
    def lambda_1F63():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1F63')

    DispatchAsync2(0x0105, 0x0003, lambda_1F63)

    OP_92(0x0101, 0x0105, 600, 2000, 0x00)
    Fade(500)
    ChrSetPos(0x0105, 10000, 5000, 640, 90)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0105, 0x0002)
    ChrClearFlags(0x0105, 0x0001)
    ChrSetChipByIndex(0x0105, 7)
    ChrSetSubChip(0x0105, 1)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060070285V#540F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070286V#008F#2P嘿嘿……\n',
            '保重啦，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070287V#508F下次王都见吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070288V#048F嗯……一定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440070289V#310F啾～啾～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetPos(0x0105, 9800, 5000, 700, 90)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0105, 0x0002)
    ChrSetFlags(0x0105, 0x0001)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetSubChip(0x0105, 0)
    OP_0D()
    OP_94(0x01, 0x0101, 0x00B4, 0x000001F4, 0x000007D0, 0x00)
    ChrTurnDirection(0x0101, 0x000B, 400)
    TerminateThread(0x0105, 0xFF)
    ChrTurnDirection(0x0105, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070290V#001F#2P啊哈，\n',
            '基库也会一起到王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440070291V#311F啾～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0105, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070292V#004F#2P……哎，我说你\n',
            '不会真的打算到王都来吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070293V科洛丝不是说过\n',
            '你习惯住在这附近的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440070294V#310F啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070295V#041F呵呵……\n',
            '基库可是很特别的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070296V我想一定会再见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070297V#506F#2P嗯……\n',
            '其实我只是想开个玩笑啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070298V#019F哈哈，\n',
            '到最后还被基库吓了一跳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070299V#010F那么……\n',
            '我们差不多该出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070300V#006F#2P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)
    ChrSetDirection(0x0105, 90, 400)

    ChrTalk(
        0x0105,
        (
            '#0060070301V#040F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070302V修行之旅，要继续加油啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070303V还有的是……\n',
            '祝愿你们早日找到卡西乌斯先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440070304V#311F啾～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070305V#006F#2P嗯……谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070306V#010F那么，保重了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 0)

    @scena.Lambda('lambda_23DE')
    def lambda_23DE():
        CameraMove(14900, 5000, 0, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_23DE)

    @scena.Lambda('lambda_23F6')
    def lambda_23F6():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_23F6)

    @scena.Lambda('lambda_2404')
    def lambda_2404():
        ChrMoveTo(0x00FE, 24300, 5000, -300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2404)

    Sleep(200)

    @scena.Lambda('lambda_2424')
    def lambda_2424():
        ChrMoveTo(0x00FE, 20300, 5000, 300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2424)

    Sleep(500)

    @scena.Lambda('lambda_2444')
    def lambda_2444():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2444)

    @scena.Lambda('lambda_2452')
    def lambda_2452():
        ChrMoveTo(0x00FE, 24300, 5000, 300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2452)

    Sleep(3500)

    OP_72(0x0002, 0x0800)
    PlaySE(223, 0x00, 0x64)
    OP_70(0x0002, 0)
    OP_73(0x0002)
    OP_71(0x0002, 0x0800)
    CameraMove(11300, 5000, 540, 1500)

    ChrTalk(
        0x0105,
        (
            '#0060070307V#049F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440070308V#310F啾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000B, 400)

    ChrTalk(
        0x0105,
        (
            '#0060070309V#542F#2P嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070310V一定，还能再见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    OP_20(0x000005DC)

    NpcTalk(
        0x000A,
        '女性的声音',
        (
            '#0100070311V#2P——科洛丝。\n',
            '让你久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    TerminateThread(0x000B, 0xFF)

    @scena.Lambda('lambda_2592')
    def lambda_2592():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2592)

    @scena.Lambda('lambda_25A0')
    def lambda_25A0():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_25A0)

    @scena.Lambda('lambda_25AE')
    def lambda_25AE():
        ChrWalkTo(0x00FE, 6600, 5000, 800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_25AE)

    CameraMove(8800, 5000, 680, 2000)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060070312V#040F……尤莉亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070313V你不是要从雷斯顿要塞回去的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0100070314V#170F啊啊，\n',
            '我从行程里抽出了一点时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100070315V#170F关于那件事，\n',
            '还有一些情况要回王都汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070316V#048F谢谢，辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440070317V#311F啾～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000A, 0x0040)
    ChrSetSubChip(0x000B, 4)
    Sleep(100)

    ChrSetSubChip(0x000B, 3)
    Sleep(100)

    ChrSetChipByIndex(0x000B, 3)
    ChrSetSubChip(0x000B, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_2713')
    def lambda_2713():
        ChrWalkTo(0x00FE, 6120, 5500, 1430, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2713)

    Sleep(300)

    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x000A, 6120, 5000, 470, 2000, 0x00)
    WaitForThreadExit(0x000B, 0x0001)
    CreateThread(0x000B, 0x01, 0x00, func_0B_2AE9)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Sleep(500)

    ChrSetDirection(0x000A, 315, 300)

    @scena.Lambda('lambda_2774')
    def lambda_2774():
        ChrSetDirection(0x00FE, 225, 300)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2774)

    ChrTalk(
        0x000A,
        (
            '#0100070318V#174F#4P喂、喂，基库，\n',
            '不要这样胡闹啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100070319V你啊，\n',
            '有没有好好坚守护卫任务啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A5(0x0002)
    OP_97(0x000B, 6120, 470, -180000, 6000, 0x0001)
    OP_97(0x000B, 6120, 470, -180000, 4000, 0x0001)
    OP_97(0x000B, 6120, 470, -45000, 2000, 0x0001)
    ChrSetFlags(0x000B, 0x0020)

    @scena.Lambda('lambda_2834')
    def lambda_2834():
        OP_99(0x00FE, 0x00, 0x07, 5000)
        Yield()

        Jump('lambda_2834')

    DispatchAsync2(0x000B, 0x0002, lambda_2834)

    @scena.Lambda('lambda_2847')
    def lambda_2847():
        ChrMoveTo(0x00FE, 5850, 5200, 820, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2847)

    ChrSetDirection(0x000B, 180, 200)
    WaitForThreadExit(0x000B, 0x0001)
    TerminateThread(0x000B, 0x02)
    Fade(500)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000A, 0x0020)
    ChrSetChipByIndex(0x000A, 8)
    ChrSetSubChip(0x000A, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0440070320V#310F啾啾☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070321V#041F呵呵……\n',
            '我可是经常给基库添麻烦呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070322V是吧，基库？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440070323V#311F啾～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0100070324V#176F#4P真是个得意忘形的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0105, 400)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#0100070325V#170F……科洛丝，\n',
            '『埃尔赛尤号』就停在大道外面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100070326V到飞艇上再详细说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070327V#047F我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070328V#049F……校园生活\n',
            '也要暂时告一段落了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070329V在回王都之前，\n',
            '还是和老师他们打声招呼吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A4A')
    def lambda_2A4A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2A4A)

    CameraMove(14900, 5000, 0, 1800)

    ChrTalk(
        0x0105,
        (
            '#0060070330V#040F（艾丝蒂尔、约修亚。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070331V（为了不输给你们两个……\n',
            '　我今后一定会拼命努力的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(2000, 0)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/R3400._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x2AE9
@scena.Code('func_0B_2AE9')
def func_0B_2AE9():
    OP_A6(0x0002)
    def _loc_2AEC(): pass

    label('loc_2AEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B0D',
    )

    OP_97(0x00FE, 6120, 470, -360000, 8000, 0x0001)
    Yield()

    Jump('loc_2AEC')

    def _loc_2B0D(): pass

    label('loc_2B0D')

    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x000C offset: 0x2B11
@scena.Code('func_0C_2B11')
def func_0C_2B11():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x2B65
@scena.Code('func_0D_2B65')
def func_0D_2B65():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　卢安市　１７５赛尔矩\n',
            '东　蔡斯市　４４８赛尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x2BC9
@scena.Code('func_0E_2BC9')
def func_0E_2BC9():
    TalkBegin(0x00FF)
    Sleep(200)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
