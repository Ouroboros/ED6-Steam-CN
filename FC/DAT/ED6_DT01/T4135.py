import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4135_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4135   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4135.x'
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
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '馆长',
            x                   = 1890,
            z                   = 0,
            y                   = 77500,
            direction           = 171,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '森特',
            x                   = -69000,
            z                   = 0,
            y                   = -2520,
            direction           = 79,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '莉西娅',
            x                   = 4400,
            z                   = 0,
            y                   = -5910,
            direction           = 255,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '亚鲁瓦教授',
            x                   = 470,
            z                   = 0,
            y                   = -3730,
            direction           = 282,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x14A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x14A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2580,
            triggerZ            = 0,
            triggerY            = -5970,
            triggerRange        = 800,
            actorX              = 4400,
            actorZ              = 1700,
            actorY              = -5910,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5090,
            triggerZ            = 0,
            triggerY            = 2190,
            triggerRange        = 800,
            actorX              = 5090,
            actorZ              = 800,
            actorY              = 2190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7840,
            triggerZ            = 4000,
            triggerY            = 6700,
            triggerRange        = 800,
            actorX              = 7840,
            actorZ              = 5700,
            actorY              = 6700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75860,
            triggerZ            = 0,
            triggerY            = -2000,
            triggerRange        = 800,
            actorX              = 75860,
            actorZ              = 1500,
            actorY              = -2000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 73200,
            triggerZ            = 0,
            triggerY            = 710,
            triggerRange        = 800,
            actorX              = 73200,
            actorZ              = 800,
            actorY              = 710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 68740,
            triggerZ            = 0,
            triggerY            = 7310,
            triggerRange        = 800,
            actorX              = 68740,
            actorZ              = 800,
            actorY              = 7310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 73480,
            triggerZ            = 0,
            triggerY            = 6420,
            triggerRange        = 800,
            actorX              = 73480,
            actorZ              = 800,
            actorY              = 6420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75820,
            triggerZ            = 4000,
            triggerY            = 8010,
            triggerRange        = 800,
            actorX              = 75820,
            actorZ              = 5700,
            actorY              = 8010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 71960,
            triggerZ            = 4000,
            triggerY            = 9290,
            triggerRange        = 800,
            actorX              = 71960,
            actorZ              = 4800,
            actorY              = 9290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20,
            triggerZ            = 0,
            triggerY            = 77880,
            triggerRange        = 800,
            actorX              = -20,
            actorZ              = 1700,
            actorY              = 77880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -770,
            triggerZ            = 0,
            triggerY            = 72650,
            triggerRange        = 800,
            actorX              = -770,
            actorZ              = 800,
            actorY              = 72650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7000,
            triggerZ            = 0,
            triggerY            = 66550,
            triggerRange        = 1200,
            actorX              = 7000,
            actorZ              = 800,
            actorY              = 66550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1770,
            triggerZ            = 0,
            triggerY            = 66890,
            triggerRange        = 800,
            actorX              = 1770,
            actorZ              = 800,
            actorY              = 66890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3790,
            triggerZ            = 0,
            triggerY            = 64959,
            triggerRange        = 800,
            actorX              = -3790,
            actorZ              = 800,
            actorY              = 64959,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x342
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_362',
    )

    ChrSetPos(0x0009, -69600, 0, 3910, 71)
    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_513')

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_393',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, -72260, 0, -3090, 183)
    ChrSetPos(0x000B, -73180, 0, 58630, 225)

    Jump('loc_513')

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3C4',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, -75330, 0, 2770, 173)
    ChrSetPos(0x000B, -73180, 0, 58630, 225)

    Jump('loc_513')

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3F5',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, -69770, 0, 6640, 341)
    ChrSetPos(0x000B, -73180, 0, 58630, 225)

    Jump('loc_513')

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_415',
    )

    ChrSetPos(0x000B, -73180, 0, 58630, 225)
    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_513')

    def _loc_415(): pass

    label('loc_415')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_441',
    )

    ChrSetPos(0x0009, -69200, 0, 0, 111)
    ChrSetPos(0x000B, -73180, 0, 58630, 225)

    Jump('loc_513')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_46D',
    )

    ChrSetPos(0x0009, 70400, 0, 3610, 0)
    ChrSetPos(0x000B, -72380, 0, -1410, 254)

    Jump('loc_513')

    def _loc_46D(): pass

    label('loc_46D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_499',
    )

    ChrSetPos(0x0009, -72260, 0, -3090, 183)
    ChrSetPos(0x000B, 69350, 0, 6420, 315)

    Jump('loc_513')

    def _loc_499(): pass

    label('loc_499')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4C5',
    )

    ChrSetPos(0x0009, -75330, 0, 2770, 173)
    ChrSetPos(0x000B, 72040, 0, 2370, 109)

    Jump('loc_513')

    def _loc_4C5(): pass

    label('loc_4C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4F1',
    )

    ChrSetPos(0x0009, -69770, 0, 6640, 341)
    ChrSetPos(0x000B, 3520, 0, 1550, 57)

    Jump('loc_513')

    def _loc_4F1(): pass

    label('loc_4F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_513',
    )

    ChrSetPos(0x0008, -1010, 0, -3780, 75)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x000B, 0x0010)

    def _loc_513(): pass

    label('loc_513')

    Return()

# id: 0x0001 offset: 0x514
@scena.Code('func_01_514')
def func_01_514():
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
        'loc_547',
    )

    OP_B1('t4135_y')

    Jump('loc_550')

    def _loc_547(): pass

    label('loc_547')

    OP_B1('t4135_n')

    def _loc_550(): pass

    label('loc_550')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_560',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_560(): pass

    label('loc_560')

    Return()

# id: 0x0002 offset: 0x561
@scena.Code('func_02_561')
def func_02_561():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_576',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_561')

    def _loc_576(): pass

    label('loc_576')

    Return()

# id: 0x0003 offset: 0x577
@scena.Code('func_03_577')
def func_03_577():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_584',
    )

    Jump('loc_160A')

    def _loc_584(): pass

    label('loc_584')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_70D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_621',
    )

    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#0150141637V#130F越是困难的任务，\n',
            '越要充分休息才能取得良好的结果哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141636V#132F哈哈，\n',
            '我这一年里可是不停地在休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70A')

    def _loc_621(): pass

    label('loc_621')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#0150141633V#130F哦，是约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141634V从你的脸色来看，\n',
            '好像相当紧张啊，\n',
            '怎么回事呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141635V越是困难的任务，\n',
            '越要充分休息才能取得良好的结果哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141636V#132F哈哈，\n',
            '我这一年里可是不停地在休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70A(): pass

    label('loc_70A')

    Jump('loc_160A')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_A5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_7A1',
    )

    ChrTalk(
        0x000B,
        (
            '#0150141652V#132F我对王城里面的样子相当感兴趣……\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141653V不过照现在这种情况看来，\n',
            '只有等王城再次向普通市民开放了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A59')

    def _loc_7A1(): pass

    label('loc_7A1')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '#0150141639V#130F说起来，\n',
            '利贝尔王室的历史似乎相当悠久呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141640V如果追寻源头的话，\n',
            '可是要回溯到一千多年以前呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141641V#004F咦～\n',
            '利贝尔王室那么早就有了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150141642V#132F是的，正因为如此，\n',
            '我对王城里面的样子相当感兴趣……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141643V艾丝蒂尔你们昨天\n',
            '被招待进王城做客了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141644V方便的话，\n',
            '可以把你们的见闻告诉我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141645V#505F唔……这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141646V好像体会到了历史传统的厚重感……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141647V#010F我觉得确实有不少地方值得一看。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141648V不过，\n',
            '我们也没有时间将每个角落都逛一遍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141649V或许不能给教授太多的参考吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150141650V#131F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141651V好可惜啊，\n',
            '只有等王城再次向普通市民开放了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A59(): pass

    label('loc_A59')

    Jump('loc_160A')

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_F20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_AEB',
    )

    ChrTalk(
        0x00FE,
        (
            '#0150141674V#132F多亏了艾丝蒂尔你们的大力协助，\n',
            '我的研究才会那么顺利。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141675V近期肯定会做出成果让你们看的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1D')

    def _loc_AEB(): pass

    label('loc_AEB')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '#0150141654V#130F呀，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141655V#132F我看到了，决赛很精彩，\n',
            '恭喜你们取得优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111570V#001F嘿嘿，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141657V……对了，\n',
            '#501F亚鲁瓦教授你这边又怎样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141658V研究有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150141659V#130F嗯，\n',
            '资料馆委托的古代文书的解析很顺利……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141660V也找到了很多我向往以久的文献。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141661V要做的事真是很多啊，\n',
            '不过时间好像怎么都不够用呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141662V#004F啊～……\n',
            '我要对你刮目相看了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141663V#007F教授到底不愧是\n',
            '醉心于研究的学者呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141664V要是我的话，\n',
            '肯定不可能做到像你那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141665V#010F哈哈，\n',
            '首先要让艾丝蒂尔一直坐在椅子上不动，\n',
            '这点就做不到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141666V#007F嗯嗯，\n',
            '我一坐下就感到非常困，\n',
            '必须得活动活动身体才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141667V#001F对了，\n',
            '正所谓只有流动的水中\n',
            '才会有鱼儿生存嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141668V我想和这是一样的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141669V#018F呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141670V#509F唔，你有什么不满吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141671V#506F不、不过，\n',
            '研究能顺利地进行实在是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0150141672V#132F哈哈，\n',
            '这也多亏了艾丝蒂尔你们的大力协助啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141673V近期肯定会做出成果让你们看的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F1D(): pass

    label('loc_F1D')

    Jump('loc_160A')

    def _loc_F20(): pass

    label('loc_F20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_FED',
    )

    ChrTalk(
        0x000B,
        (
            '#0150141678V#130F呼，\n',
            '整整三天都埋头在资料馆里搞研究，　\n',
            '好久没有去晒晒太阳了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141679V我也感觉到有些累了，\n',
            '为了转换心情就出去转转吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141680V偶尔奢侈一下，\n',
            '去尝尝冰淇淋也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_160A')

    def _loc_FED(): pass

    label('loc_FED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1066',
    )

    ChrTalk(
        0x000B,
        (
            '#0150141676V#130F哎呀，找到不少似乎可以\n',
            '当作研究材料的资料呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141677V我打算马上着手解析古文书。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_160A')

    def _loc_1066(): pass

    label('loc_1066')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1182',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_10E0',
    )

    ChrTalk(
        0x000B,
        (
            '#0150141681V#130F呵呵，\n',
            '这些可都是没有公开过的收藏品啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141683V哎呀，\n',
            '真是又开心又紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_117F')

    def _loc_10E0(): pass

    label('loc_10E0')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '#0150141681V#130F呵呵，\n',
            '这些可都是没有公开过的收藏品啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141682V我来看看，\n',
            '究竟会有些什么样的宝贝呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141683V哎呀，\n',
            '真是又开心又紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_117F(): pass

    label('loc_117F')

    Jump('loc_160A')

    def _loc_1182(): pass

    label('loc_1182')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_12A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_11CD',
    )

    ChrTalk(
        0x000B,
        (
            '#0150141686V#130F想象力对于考古学而言\n',
            '可是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_129D')

    def _loc_11CD(): pass

    label('loc_11CD')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '#0150141687V#130F唔～\n',
            '这些展品我都很感兴趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141688V那边的浮雕\n',
            '很可能是大崩坏之前的产物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141689V不觉得其风格和\n',
            '四轮之塔的内部有些相似吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141690V想象力对于考古学而言\n',
            '可是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_129D(): pass

    label('loc_129D')

    Jump('loc_160A')

    def _loc_12A0(): pass

    label('loc_12A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1488',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1352',
    )

    ChrTalk(
        0x00FE,
        (
            '#0150141691V#132F利贝尔各地散布着的遗迹\n',
            '可能是古代塞姆里亚文明的遗物啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141692V实地调查已经完成了，\n',
            '接下来就是参考各种文献，\n',
            '让考察获得更多进展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1485')

    def _loc_1352(): pass

    label('loc_1352')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0150141693V#130F卢安近郊的大型水道桥『艾尔·雷登』……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141694V环绕王都格兰赛尔的长城『亚宁堡』……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141695V以及散布在各地的『四轮之塔』……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141696V#132F这些都有可能是\n',
            '古代塞姆里亚文明的遗迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141692V实地调查已经完成了，\n',
            '接下来就是参考各种文献，\n',
            '让考察获得更多进展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1485(): pass

    label('loc_1485')

    Jump('loc_160A')

    def _loc_1488(): pass

    label('loc_1488')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_15D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_14FD',
    )

    ChrTalk(
        0x000B,
        (
            '#0150141698V#130F是立刻展开研究呢，\n',
            '还是先到街上游览呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141699V哈哈，真是举棋不定呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D3')

    def _loc_14FD(): pass

    label('loc_14FD')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '#0150141700V#130F不愧是王都格兰赛尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141701V恐怖事件基本没有造成什么影响，\n',
            '街道依旧那么热闹。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141702V唔，是立刻展开研究工作呢，\n',
            '还是先到街上游览呢……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141699V哈哈，真是举棋不定呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15D3(): pass

    label('loc_15D3')

    Jump('loc_160A')

    def _loc_15D6(): pass

    label('loc_15D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_160A',
    )

    ChrTalk(
        0x000B,
        (
            '#0150141704V#130F承蒙您的关照了，馆长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_160A(): pass

    label('loc_160A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x160E
@scena.Code('func_04_160E')
def func_04_160E():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x1613
@scena.Code('func_05_1613')
def func_05_1613():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1666',
    )

    ChrTalk(
        0x000A,
        (
            '亚鲁瓦教授\n',
            '跑到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我还想听听\n',
            '教授的特别演讲呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_1666(): pass

    label('loc_1666')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_16C0',
    )

    ChrTalk(
        0x000A,
        (
            '外面的情况\n',
            '似乎和平常不太一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '刚才还吵吵嚷嚷的，\n',
            '现在一下就安静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_16C0(): pass

    label('loc_16C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_17A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_171B',
    )

    ChrTalk(
        0x000A,
        (
            '诞辰庆典\n',
            '准备得怎么样了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总不能让女王陛下\n',
            '带着病体参加吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A1')

    def _loc_171B(): pass

    label('loc_171B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '武术大会结束以后，\n',
            '感觉街上也安静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，诞辰庆典方面\n',
            '准备得怎么样了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总不能让女王陛下\n',
            '带着病体参加吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17A1(): pass

    label('loc_17A1')

    Jump('loc_1A40')

    def _loc_17A4(): pass

    label('loc_17A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_17FF',
    )

    ChrTalk(
        0x000A,
        (
            '武术大会\n',
            '平安无事地结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '亚鲁瓦教授\n',
            '去看比赛了，\n',
            '我真有点羡慕他呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_17FF(): pass

    label('loc_17FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1859',
    )

    ChrTalk(
        0x000A,
        (
            '今天终于到了\n',
            '武术大会总决赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我不能去看比赛，\n',
            '呆在这儿心里直痒痒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_1859(): pass

    label('loc_1859')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_18A4',
    )

    ChrTalk(
        0x000A,
        (
            '刚才收到了一封\n',
            '从柏斯寄给馆长的快递。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '必须快点交给他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_18A4(): pass

    label('loc_18A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_18E5',
    )

    ChrTalk(
        0x000A,
        (
            '本资料馆内\n',
            '禁止吸烟和摄影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '请客人予以配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_18E5(): pass

    label('loc_18E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_193D',
    )

    ChrTalk(
        0x000A,
        (
            '本来在研究者中\n',
            '奇怪的人就不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但亚鲁瓦教授\n',
            '更让人感到不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_193D(): pass

    label('loc_193D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_197C',
    )

    ChrTalk(
        0x000A,
        (
            '唔～武术大会开始后，\n',
            '到馆里来的游客变得稀少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_197C(): pass

    label('loc_197C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_19DE',
    )

    ChrTalk(
        0x000A,
        (
            '最近在街道上\n',
            '也时常见到王国军的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是因为亲卫队使用的飞艇\n',
            '停泊在空港吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A40')

    def _loc_19DE(): pass

    label('loc_19DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1A40',
    )

    ChrTalk(
        0x000A,
        (
            '欢迎光临\n',
            '格兰赛尔历史资料馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在正在举行\n',
            '『利贝尔现代化之路』\n',
            '收藏资料主题展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A40(): pass

    label('loc_1A40')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x1A44
@scena.Code('func_06_1A44')
def func_06_1A44():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1AA5',
    )

    ChrTalk(
        0x00FE,
        (
            '外面很是热闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等我手头的工作做完后，\n',
            '也要到街上去\n',
            '体验一下庆典的氛围。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2346')

    def _loc_1AA5(): pass

    label('loc_1AA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1B77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1B02',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才王国军的士兵\n',
            '也到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是为了搜捕\n',
            '亲卫队的人而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B74')

    def _loc_1B02(): pass

    label('loc_1B02')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '昨天王国军的士兵\n',
            '也到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是为了搜捕\n',
            '亲卫队的人而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '士兵们都是一幅\n',
            '很焦急的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B74(): pass

    label('loc_1B74')

    Jump('loc_2346')

    def _loc_1B77(): pass

    label('loc_1B77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1C52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1BE0',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才接到了馆长\n',
            '从柏斯传来的消息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像因为定期船全部停航\n',
            '而无法回王都来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C4F')

    def _loc_1BE0(): pass

    label('loc_1BE0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '刚才接到了馆长\n',
            '从柏斯传来的消息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像因为定期船全部停航\n',
            '而无法回王都来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C4F(): pass

    label('loc_1C4F')

    Jump('loc_2346')

    def _loc_1C52(): pass

    label('loc_1C52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1CAA',
    )

    ChrTalk(
        0x00FE,
        (
            '馆长收到了一封信，\n',
            '就急急忙忙地出差去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在也许\n',
            '已经到柏斯了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2346')

    def _loc_1CAA(): pass

    label('loc_1CAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1D32',
    )

    ChrTalk(
        0x00FE,
        (
            '馆长把今天的决赛门票\n',
            '送给了亚鲁瓦教授。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真羡慕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，他们谁去看比赛和我无关，\n',
            '反正我是要留在这里干活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2346')

    def _loc_1D32(): pass

    label('loc_1D32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1E85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1DB4',
    )

    ChrTalk(
        0x00FE,
        (
            '古代文明繁荣的时候，\n',
            '还存在着人类以外的\n',
            '拥有高度智慧的生物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其中的代表就是\n',
            '一种被称为『古代龙』的龙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E82')

    def _loc_1DB4(): pass

    label('loc_1DB4')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '古代文明繁荣的时候，\n',
            '还存在着人类以外的\n',
            '拥有高度智慧的生物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其中的代表就是\n',
            '一种被称为『古代龙』的龙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸存下来的少数古代龙\n',
            '数十年前还在柏斯附近的地方生活，\n',
            '但最近以来再也没有人见到过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E82(): pass

    label('loc_1E82')

    Jump('loc_2346')

    def _loc_1E85(): pass

    label('loc_1E85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1FA1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1EFD',
    )

    ChrTalk(
        0x00FE,
        (
            '这里所展示的文物是\n',
            '以前沉在瓦雷利亚湖底的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '搞不好，\n',
            '瓦雷利亚湖底\n',
            '也沉睡着巨大的遗迹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F9E')

    def _loc_1EFD(): pass

    label('loc_1EFD')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    TalkSetChrName('≡１Ｆ东展示室')

    ChrTalk(
        0x00FE,
        (
            '这里所展示的文物是\n',
            '以前沉在瓦雷利亚湖底的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一次偶然的机会\n',
            '被渔夫给捞上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '搞不好，\n',
            '瓦雷利亚湖底\n',
            '也沉睡着巨大的遗迹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F9E(): pass

    label('loc_1F9E')

    Jump('loc_2346')

    def _loc_1FA1(): pass

    label('loc_1FA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_20D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_202D',
    )

    ChrTalk(
        0x00FE,
        (
            '大崩坏之后，残存下来的人们\n',
            '有着一段非常悲惨的历史。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现今人们的生活\n',
            '已经安定下来了，\n',
            '但这都是导力革命之后的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_202D(): pass

    label('loc_202D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '大崩坏之后，残存下来的人们\n',
            '有着一段非常悲惨的历史。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接二连三的战乱、贫困、流行病……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现今人们的生活\n',
            '已经安定下来了，\n',
            '但这都是导力革命之后的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20D1(): pass

    label('loc_20D1')

    Jump('loc_2346')

    def _loc_20D4(): pass

    label('loc_20D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2148',
    )

    ChrTalk(
        0x00FE,
        (
            '大崩坏之前的\n',
            '相关资料基本上\n',
            '都没有保存下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过说实话，\n',
            '那时的文明发达的程度\n',
            '似乎比现在还高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2346')

    def _loc_2148(): pass

    label('loc_2148')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_226E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_21C1',
    )

    ChrTalk(
        0x00FE,
        (
            '今天本应是把市民聚集起来\n',
            '开展研讨会的日子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在每年的武术大会\n',
            '和诞辰庆典期间都要休会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_226B')

    def _loc_21C1(): pass

    label('loc_21C1')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '今天本应是把市民聚集起来\n',
            '开展研讨会的日子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在每年的武术大会\n',
            '和诞辰庆典期间都要休会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你问为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是因为无法聚集\n',
            '足够的人来参加研讨会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_226B(): pass

    label('loc_226B')

    Jump('loc_2346')

    def _loc_226E(): pass

    label('loc_226E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2346',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_22A2',
    )

    ChrTalk(
        0x00FE,
        (
            '资料馆并非\n',
            '只是展示资料而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2346')

    def _loc_22A2(): pass

    label('loc_22A2')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '资料馆并非\n',
            '只是展示资料而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像这样对收集来的资料\n',
            '进行整理分类保管\n',
            '也是资料馆的任务之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时还要接待\n',
            '像亚鲁瓦教授这样\n',
            '来讨论研究的学术派客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2346(): pass

    label('loc_2346')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x234A
@scena.Code('func_07_234A')
def func_07_234A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_23CF',
    )

    ChrTalk(
        0x00FE,
        (
            '我到柏斯出差的时候，\n',
            '定期船停航给我带来很大麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '外出期间虽然发生了许多事情，\n',
            '但资料馆完好无损，这就很好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A1C')

    def _loc_23CF(): pass

    label('loc_23CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_23D9',
    )

    Jump('loc_2A1C')

    def _loc_23D9(): pass

    label('loc_23D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_23E3',
    )

    Jump('loc_2A1C')

    def _loc_23E3(): pass

    label('loc_23E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_23ED',
    )

    Jump('loc_2A1C')

    def _loc_23ED(): pass

    label('loc_23ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2552',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2474',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我需要去和一个\n',
            '研究柏斯古代生物的学者见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '过了中午我就要去搭乘定期船，\n',
            '所以没办法去观看今天的决赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_254F')

    def _loc_2474(): pass

    label('loc_2474')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '其实我非常想去竞技场\n',
            '看武术大会的总决赛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过今天我需要去和一个\n',
            '研究柏斯古代生物的学者见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '过了中午我就要去搭乘定期船，\n',
            '所以没办法去观看比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '遗憾也没有办法，\n',
            '唯有将门票让给亚鲁瓦教授了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_254F(): pass

    label('loc_254F')

    Jump('loc_2A1C')

    def _loc_2552(): pass

    label('loc_2552')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_25AA',
    )

    ChrTalk(
        0x00FE,
        (
            '明天武术大会的决赛\n',
            '我也打算去看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '实际上我连票都已经买好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A1C')

    def _loc_25AA(): pass

    label('loc_25AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_26F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2639',
    )

    ChrTalk(
        0x00FE,
        (
            '作为学术调查的对象，\n',
            '我很想将古代遗物\n',
            '也收入本资料馆里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但就算向负责管理的\n',
            '七耀教会提出申请，\n',
            '他们也不会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26EE')

    def _loc_2639(): pass

    label('loc_2639')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '据说古代遗物\n',
            '也和塞姆里亚文明\n',
            '有着很深的联系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为学术调查的对象，\n',
            '我很想将古代遗物\n',
            '也收入本资料馆里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但就算向负责管理的\n',
            '七耀教会提出申请，\n',
            '他们也不会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26EE(): pass

    label('loc_26EE')

    Jump('loc_2A1C')

    def _loc_26F1(): pass

    label('loc_26F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_27E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2765',
    )

    ChrTalk(
        0x00FE,
        (
            '亚鲁瓦教授\n',
            '对我们这儿的未公开资料\n',
            '也一并进行了调查研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定还会有\n',
            '新的历史性发现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27E2')

    def _loc_2765(): pass

    label('loc_2765')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '亚鲁瓦教授是个很沉稳的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他对我们这儿的未公开资料\n',
            '也一并进行了调查研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定还会有\n',
            '新的历史性发现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27E2(): pass

    label('loc_27E2')

    Jump('loc_2A1C')

    def _loc_27E5(): pass

    label('loc_27E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2955',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2875',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然主张『七至宝』只是\n',
            '单纯的传说的学者也不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但各地残留下的遗迹是\n',
            '塞姆里亚文明遗物的推测，\n',
            '还是有几分可能性的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2952')

    def _loc_2875(): pass

    label('loc_2875')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '上天赐予古代人的\n',
            '蕴藏着力量的『七至宝』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至今为止，\n',
            '还是没有发现能说明\n',
            '其为何物的相关文献。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也有不少学者\n',
            '主张那只是传说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但各地残留下的遗迹是\n',
            '塞姆里亚文明遗物的推测，\n',
            '还是有几分可能性的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2952(): pass

    label('loc_2952')

    Jump('loc_2A1C')

    def _loc_2955(): pass

    label('loc_2955')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_29D4',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～亚鲁瓦教授的研究\n',
            '和我的兴趣不谋而合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '七至宝之一的『辉之环』\n',
            '长眠于利贝尔某处的传说，\n',
            '实在含义颇深啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A1C')

    def _loc_29D4(): pass

    label('loc_29D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2A1C',
    )

    ChrTalk(
        0x00FE,
        (
            '您客气了，亚鲁瓦教授。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我刚才就想着\n',
            '你是不是快要到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A1C(): pass

    label('loc_2A1C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x2A20
@scena.Code('func_08_2A20')
def func_08_2A20():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【『四轮之塔』的外壁】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　这块朴素的石壁，是从『大崩坏』后所建\n',
            '的『四轮之塔』上作为研究资料切割出来的。\n',
            '其上所绘制的纹样是同时代建筑物中的典型，\n',
            '据说描述的是持杖的祭司，以及展翅的神祗的\n',
            '身姿。关于其与七耀教会成立之后的代表神格\n',
            '『空之女神』的关系，各方面的研究仍在进行\n',
            '中。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x2B92
@scena.Code('func_09_2B92')
def func_09_2B92():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历１１５０～１２００年\n',
            '　　　　　　　～导力革命以后的世界～】\n',
            '　　Ｃ·爱普斯泰恩博士发明导力器后仅仅五\n',
            '十年。世界以惊人的速度进步着，接连不断地\n',
            '开拓岀导力技术新的应用领域。堪称其象征的\n',
            '就是飞艇。\n',
            '　　\n',
            '　　利贝尔王国定期飞艇的运航已经成为国民\n',
            '们习以为常的交通方式，近年来埃雷波尼亚帝\n',
            '国等其他国家也开始正式引进飞艇制造业，使\n',
            '得飞艇级的船体逐步实用化。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x2D2E
@scena.Code('func_0A_2D2E')
def func_0A_2D2E():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历以前\n',
            '　　　　　～古代塞姆里亚文明～】\n',
            '　　距今约１２００年前，当时繁荣绝顶的塞\n',
            '姆里亚文明突然迎来了终结，失去了文明的人\n',
            '们开始度过漫长的暗黑时代。\n',
            '　　\n',
            '　　第一层的展示物据考证是『大崩坏』之后\n',
            '所制造的遗物。虽然据判断并非古代文明的直\n',
            '接遗物，但因受到其深刻影响，学术方面的价\n',
            '值极高。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x2E89
@scena.Code('func_0B_2E89')
def func_0B_2E89():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【古代的照明器具】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　专用于焚烧篝火的容器。在塔之类被认为\n',
            '与祭祀仪式有关联的建筑物中频繁被使用，其\n',
            '具体用途不仅仅是照明，在宗教上可能也拥有\n',
            '某种程度的意义。当然这点目前还只是推测罢\n',
            '了。  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x2FA2
@scena.Code('func_0C_2FA2')
def func_0C_2FA2():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【浮雕石柱】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　刻有优美雕刻的石柱。在瓦雷利亚湖的湖\n',
            '底被打捞上来，可以看出与『四轮之塔』的壁\n',
            '画类似的纹样在其上也被反复使用。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x3082
@scena.Code('func_0D_3082')
def func_0D_3082():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【瓷工艺的地板】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　遗迹内部彩色镶嵌的瓷工艺地板。将破碎\n',
            '的天然石块巧妙拼接，作出朴素而美妙的花纹\n',
            '样式。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x314C
@scena.Code('func_0E_314C')
def func_0E_314C():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历１～５００年左右\n',
            '　　　　　　　　～暗黑时代的到来～】\n',
            '　　由于『大崩坏』而导致文明尽失，世界陷\n',
            '入了长期的混乱时代。\n',
            '　　大小各异的国家、势力使得无尽的战争持\n',
            '续了约５００年间，后世称此时代为『暗黑时\n',
            '代』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0x3253
@scena.Code('func_0F_3253')
def func_0F_3253():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【骑士们的武具】\n',
            '　　　　　　　　年代：七耀历５００年左右\n',
            '　　日夜征战的时代中，战士们的集团拥有社\n',
            '会性的强大影响力，最终成长为特权的骑士阶\n',
            '级。\n',
            '　　他们佩戴着如展品所示的武具投身沙场，\n',
            '获得战利品和领土，势力不断扩大。\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0010 offset: 0x3362
@scena.Code('func_10_3362')
def func_10_3362():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历５００～１１００年左右\n',
            '　　　　　　～七耀教会带来的安定期～】\n',
            '　　七耀教会登上历史舞台，正值暗黑时代末\n',
            '期，七耀历５００年左右。\n',
            '　　以『空之女神』为中心所整理的教义，通\n',
            '过教会救济民众的社会活动，瞬间深入人心。\n',
            '　　它的权威很快成长到连贵族、骑士阶级也\n',
            '无法忽视的地步，其后以教会为中心的新秩序\n',
            '便逐步形成了。\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0011 offset: 0x34D1
@scena.Code('func_11_34D1')
def func_11_34D1():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【古代文明的遗物——\n',
            '　　　　　　　　『古代遗产』】\n',
            '　　　　　　　　　　　　　　　年代：不明\n',
            '　　『古代遗产』是从各地发现的古代遗迹中\n',
            '出土的诸如器物、杖等形态各异、不可思议的\n',
            '遗物。\n',
            '　　在七耀教会的教义中，作为与女神赐予的\n',
            '『七至宝』相关的物品，其回收成为教会必须\n',
            '履行的义务之一。展品的『古代遗产』也是教\n',
            '会所回收的物品。\n',
            '　　许多传闻称其拥有超常的力量，但此展品\n',
            '已经失去能力，无法启动。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0012 offset: 0x368C
@scena.Code('func_12_368C')
def func_12_368C():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀教会的祭具】\n',
            '　　　　　　　　年代：七耀历９００年左右\n',
            '　　七耀教会创造岀种种的宗教艺术，由此开\n',
            '始教会开拓出一个稳定的时代。据考证，『空\n',
            '之女神』的圣像也是由此时起被塑造为现今的\n',
            '姿态。此外，现在所使用的祭祀道具多数也是\n',
            '在这个时代被定型的。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0013 offset: 0x37B8
@scena.Code('func_13_37B8')
def func_13_37B8():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀教会圣典的抄本】\n',
            '　　　　　　　　年代：七耀历５００年左右\n',
            '　　暗黑时代末期的原始七耀教会所使用的圣\n',
            '典抄本。中世纪没有印刷技术，因此这本书是\n',
            '由人手工抄写在兽皮制的纸张上的。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x38A2
@scena.Code('func_14_38A2')
def func_14_38A2():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【中世纪的纺纱机】\n',
            '　　　　　　　　年代：七耀历９００年左右\n',
            '　　纺纱用的手工机械。到了稳定的中世纪，\n',
            '农民的生活逐渐富裕，作为商品作物的棉花栽\n',
            '培日渐繁盛。为了货币增收，这个时代的手工\n',
            '业也开始发展。\n',
            '　　',
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
