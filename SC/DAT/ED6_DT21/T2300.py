import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2300.x'
    header.mapIndex       = 86
    header.bgm            = 15
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
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '萨蒂',
            x                   = 45300,
            z                   = 0,
            y                   = 23500,
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
            name                = '卢西亚',
            x                   = -2800,
            z                   = 4000,
            y                   = 29000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '塞尔吉村长',
            x                   = 38210,
            z                   = -50,
            y                   = 17840,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '玛诺利亚间道方向',
            x                   = -2940,
            z                   = 7990,
            y                   = 68620,
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
            name                = '梅威海道方向',
            x                   = 75410,
            z                   = -40,
            y                   = 20810,
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

# id: 0x10002 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x162
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 16870,
            y           = 7000,
            z           = -7690,
            range       = -9400,
            dword_10    = 0x00001388,
            dword_14    = 0xFFFFFD80,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 27540,
            y           = 0,
            z           = 18980,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 53410,
            y           = 0,
            z           = 22710,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = 6000,
            y           = 4000,
            z           = 20210,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000F,
        ),
    )

# id: 0x10004 offset: 0x1E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 4450,
            triggerZ            = 6500,
            triggerY            = -2640,
            triggerRange        = 800,
            actorX              = 4450,
            actorZ              = 7500,
            actorY              = -2740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 37440,
            triggerZ            = -10,
            triggerY            = 19280,
            triggerRange        = 800,
            actorX              = 37440,
            actorZ              = 1500,
            actorY              = 18980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 38140,
            triggerZ            = -40,
            triggerY            = 10680,
            triggerRange        = 1000,
            actorX              = 38310,
            actorZ              = -1540,
            actorY              = 7000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_269',
    )

    ChrSetPos(0x0009, 15050, 3980, 22520, 161)

    Jump('loc_298')

    def _loc_269(): pass

    label('loc_269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_273',
    )

    Jump('loc_298')

    def _loc_273(): pass

    label('loc_273')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_27D',
    )

    Jump('loc_298')

    def _loc_27D(): pass

    label('loc_27D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_287',
    )

    Jump('loc_298')

    def _loc_287(): pass

    label('loc_287')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_298',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_298(): pass

    label('loc_298')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_2A4'),
        (-1, 'loc_2C1'),
    )

    def _loc_2A4(): pass

    label('loc_2A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 7, 0x1217)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 0, 0x1218)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2BE',
    )

    MapClearFlags(0x00000010)
    MapSetFlags(0x10000000)
    Event(0, func_07_10A2)

    def _loc_2BE(): pass

    label('loc_2BE')

    Jump('loc_2C1')

    def _loc_2C1(): pass

    label('loc_2C1')

    Return()

# id: 0x0001 offset: 0x2C2
@scena.Code('func_01_2C2')
def func_01_2C2():
    OP_16(0x02, 4000, -108000, -126000, 2293835)
    PlaySE(453, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_2E9',
    )

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E9(): pass

    label('loc_2E9')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_304',
    )

    OP_10(0x01, 0x00)
    OP_10(0x08, 0x01)
    OP_71(0x0007, 0x0004)
    OP_64(0x01, 0x0001)

    def _loc_304(): pass

    label('loc_304')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_321',
    )

    OP_72(0x0002, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0002, 0x0010)
    OP_64(0x00, 0x0001)

    Jump('loc_32B')

    def _loc_321(): pass

    label('loc_321')

    OP_71(0x0002, 0x0004)
    OP_72(0x0008, 0x0010)

    def _loc_32B(): pass

    label('loc_32B')

    Return()

# id: 0x0002 offset: 0x32C
@scena.Code('func_02_32C')
def func_02_32C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_359',
    )

    def _loc_333(): pass

    label('loc_333')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_356',
    )

    OP_8D(0x00FE, 16309, 21410, 13470, 24720, 3000)

    Jump('loc_333')

    def _loc_356(): pass

    label('loc_356')

    Jump('loc_5C8')

    def _loc_359(): pass

    label('loc_359')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36C',
    )

    Return()

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B4',
    )

    ChrSetPos(0x00FE, 45290, -10, 21290, 0)
    ChrWalkTo(0x00FE, 39460, -120, 15990, 3500, 0x00)
    ChrWalkTo(0x00FE, 5160, 4000, 15170, 3500, 0x00)

    Jump('loc_424')

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_424',
    )

    ChrSetPos(0x00FE, 5130, 4030, 10940, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3030, 4030, 13020, 3500, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_424(): pass

    label('loc_424')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C8',
    )

    ChrWalkTo(0x00FE, 5160, 4000, 15170, 3500, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 7040, 4030, 12860, 3500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 5130, 4030, 10940, 3500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3030, 4030, 13020, 3500, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C5',
    )

    ChrWalkTo(0x00FE, 39460, -120, 15990, 3500, 0x00)
    ChrWalkTo(0x00FE, 45290, -10, 21290, 3500, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54E',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_54E(): pass

    label('loc_54E')

    ChrSetDirection(0x00FE, 90, 400)
    ChrSetDirection(0x00FE, 180, 400)
    ChrSetDirection(0x00FE, 270, 400)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59B',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)

    def _loc_59B(): pass

    label('loc_59B')

    Sleep(1500)

    ChrSetDirection(0x00FE, 250, 400)
    ChrWalkTo(0x00FE, 39460, -120, 15990, 3500, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5C5(): pass

    label('loc_5C5')

    Jump('loc_424')

    def _loc_5C8(): pass

    label('loc_5C8')

    Return()

# id: 0x0003 offset: 0x5C9
@scena.Code('func_03_5C9')
def func_03_5C9():
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    TalkBegin(0x0008)
    OP_63(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5EF',
    )

    OP_0D()
    OP_A9(0x71)
    OP_56(0x00)
    TalkEnd(0x0008)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

    def _loc_5EF(): pass

    label('loc_5EF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_603',
    )

    TalkEnd(0x0008)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

    def _loc_603(): pass

    label('loc_603')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_6CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_683',
    )

    ChrTalk(
        0x0008,
        (
            '导力器不能使用\n',
            '我们也很为难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过家里的婆婆\n',
            '却完全不介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '老人的智慧和经验\n',
            '真是厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_6CC')

    def _loc_683(): pass

    label('loc_683')

    ChrTalk(
        0x0008,
        (
            '婆婆即使没有导力器\n',
            '也完全没事的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '简直比龟甲还……结实呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CC(): pass

    label('loc_6CC')

    Jump('loc_9D4')

    def _loc_6CF(): pass

    label('loc_6CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_729',
    )

    ChrTalk(
        0x0008,
        (
            '附近的海岸好像有军队的警备艇\n',
            '被迫降落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好像还有伤员\n',
            '在旅店休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D4')

    def _loc_729(): pass

    label('loc_729')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_7C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_780',
    )

    ChrTalk(
        0x0008,
        (
            '上次的时候\n',
            '还是个孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这次的选举对我来说\n',
            '是第一次经历。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C5')

    def _loc_780(): pass

    label('loc_780')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我在这次选举中\n',
            '是第一次投票哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '打算好好看人品\n',
            '来投票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C5(): pass

    label('loc_7C5')

    Jump('loc_9D4')

    def _loc_7C8(): pass

    label('loc_7C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_817',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临，\n',
            '要买花吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不仅有欣赏用的,\n',
            '还有能做料理的花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D4')

    def _loc_817(): pass

    label('loc_817')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_8E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_86E',
    )

    ChrTalk(
        0x0008,
        (
            '孩子们好像也完全\n',
            '恢复了精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然空之女神\n',
            '在守护着我们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E2')

    def _loc_86E(): pass

    label('loc_86E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '孩子们好像也完全\n',
            '恢复了精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '纵火事件的时候\n',
            '还以为会变成怎样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然空之女神\n',
            '在守护着我们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E2(): pass

    label('loc_8E2')

    Jump('loc_9D4')

    def _loc_8E5(): pass

    label('loc_8E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            Expr.Return,
        ),
        'loc_98A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_93A',
    )

    ChrTalk(
        0x0008,
        (
            '太阳已经\n',
            '升得这么高了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '差不多到\n',
            '主日学校结束的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_987')

    def _loc_93A(): pass

    label('loc_93A')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '哎呀，太阳已经\n',
            '升得这么高了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '差不多到\n',
            '主日学校结束的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_987(): pass

    label('loc_987')

    Jump('loc_9D4')

    def _loc_98A(): pass

    label('loc_98A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_9D4',
    )

    ChrTalk(
        0x0008,
        (
            '一个打扮奇怪的\n',
            '神父刚才经过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那就是新的巡回神父吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9D4(): pass

    label('loc_9D4')

    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x9DB
@scena.Code('func_04_9DB')
def func_04_9DB():
    TalkBegin(0x00FE)
    OP_63(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_A8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A4B',
    )

    ChrTalk(
        0x00FE,
        (
            '好想去找\n',
            '孤儿院的大家玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈又说\n',
            '不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说有很多\n',
            '可怕～的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_A89')

    def _loc_A4B(): pass

    label('loc_A4B')

    ChrTalk(
        0x00FE,
        (
            '妈妈说，不能\n',
            '出去村子外面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说有很多\n',
            '可怕～的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A89(): pass

    label('loc_A89')

    Jump('loc_D2D')

    def _loc_A8C(): pass

    label('loc_A8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B32',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AFC',
    )

    ChrTalk(
        0x00FE,
        (
            '卢西亚\n',
            '也不是来去玩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是妈妈要我\n',
            '来找柴火的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～有没有好的树枝\n',
            '落下呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_B2F')

    def _loc_AFC(): pass

    label('loc_AFC')

    ChrTalk(
        0x00FE,
        (
            '是妈妈要我\n',
            '来找柴火哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，了不起吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B2F(): pass

    label('loc_B2F')

    Jump('loc_D2D')

    def _loc_B32(): pass

    label('loc_B32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_B88',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，赶快\n',
            '到上学的日子就好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以和波利他们\n',
            '在外面尽情的玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2D')

    def _loc_B88(): pass

    label('loc_B88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_C16',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_BC0',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～不过，叔叔他\n',
            '为什么不回家呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C13')

    def _loc_BC0(): pass

    label('loc_BC0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我们家是住宿酒馆，\n',
            '有很多喝醉的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '叔叔他，\n',
            '好像碰到很痛苦的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C13(): pass

    label('loc_C13')

    Jump('loc_D2D')

    def _loc_C16(): pass

    label('loc_C16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_D2D',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CE7',
    )

    ChrTurnDirection(0x00FE, 0x0109, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_C6A',
    )

    ChrTalk(
        0x00FE,
        (
            '老师，下次来的时候\n',
            '也要再读书给我们听哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE4')

    def _loc_C6A(): pass

    label('loc_C6A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '啊～是凯文老师～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老师，再读书给我们听哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#1062F哦，交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '卢西亚\n',
            '也要乖乖的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，等你哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE4(): pass

    label('loc_CE4')

    Jump('loc_D2D')

    def _loc_CE7(): pass

    label('loc_CE7')

    ChrTalk(
        0x00FE,
        (
            '今天的老师是个很快乐的人呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，下次的主日学校也好期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2D(): pass

    label('loc_D2D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xD31
@scena.Code('func_05_D31')
def func_05_D31():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_E23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_DAD',
    )

    ChrTalk(
        0x00FE,
        (
            '身为贵族的前市长被逮捕，\n',
            '平民出身的候选人在竞争其继任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '此次的市长选举\n',
            '真像是时代变化的象征。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E20')

    def _loc_DAD(): pass

    label('loc_DAD')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '诺曼氏和波尔多斯氏\n',
            '都是平民出身，\n',
            '两人都是出色的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前的选举\n',
            '都是从贵族中选出的，\n',
            '时代真是变了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E20(): pass

    label('loc_E20')

    Jump('loc_104C')

    def _loc_E23(): pass

    label('loc_E23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_EF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_E7E',
    )

    ChrTalk(
        0x00FE,
        (
            '上次选举时\n',
            '这里是投票所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '许多人相信戴尔蒙家\n',
            '的家名而投了票……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EEF')

    def _loc_E7E(): pass

    label('loc_E7E')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '上次选举时\n',
            '这里曾经是投票所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔，怎么看都很狭窄啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概还是只有拜托\n',
            '白之木莲亭合作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EEF(): pass

    label('loc_EEF')

    Jump('loc_104C')

    def _loc_EF2(): pass

    label('loc_EF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_F5D',
    )

    ChrTalk(
        0x00FE,
        (
            '孤儿院开始重建工程时，\n',
            '村里的年轻人好像\n',
            '也都去帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望他们能一直\n',
            '保持这种心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104C')

    def _loc_F5D(): pass

    label('loc_F5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_104C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_FC2',
    )

    ChrTalk(
        0x00FE,
        (
            '前市长引起的事件\n',
            '对玛诺利亚来说也是重伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生大事件之后\n',
            '游客也都不来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104C')

    def _loc_FC2(): pass

    label('loc_FC2')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哎呀，旅行的人吗？\n',
            '欢迎来到玛诺利亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '烧掉的孤儿院也被重建，\n',
            '一切恢复到平常的生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后就等待\n',
            '下任的市长被选出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_104C(): pass

    label('loc_104C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1050
@scena.Code('func_06_1050')
def func_06_1050():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            Expr.Return,
        ),
        'loc_1061',
    )

    TalkEnd(0x00FF)
    Call(0, 0x0009)

    Jump('loc_10A1')

    def _loc_1061(): pass

    label('loc_1061')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '主日学校·授课中',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    def _loc_10A1(): pass

    label('loc_10A1')

    Return()

# id: 0x0007 offset: 0x10A2
@scena.Code('func_07_10A2')
def func_07_10A2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10B3',
    )

    Call(0, 0x000A)

    def _loc_10B3(): pass

    label('loc_10B3')

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, 64319, 0, 21000, 270)
    ChrSetPos(0x00F7, 64170, 0, 19800, 270)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xF7, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xF7, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xF7, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6C(45000, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC06._CH', 0x00, 0x07D0)
    ShowPlaceName('玛诺利亚')
    FadeIn(2000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1296',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210137V#050F玛诺利亚啊……\n',
            '捐款被抢事件以来都没来过啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210138V还是那么悠闲的村子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210139V#1006F#5P这不是很好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210140V阿加特的故乡拉文努村\n',
            '也很悠闲，多好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210141V#552F哼，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210142V#053F总之，主日学校\n',
            '好像在村里进行呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210143V去确认一下情况吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15F7')

    def _loc_1296(): pass

    label('loc_1296')

    ChrTalk(
        0x0103,
        (
            '#0030210144V#021F玛诺利亚村啊。\n',
            '好久没来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210145V#020F不过说实话\n',
            '包括卢安我也很少来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210146V#1004F#5P哦，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210147V我还以为老爸和雪拉姐\n',
            '都是在洛连特以外的地方\n',
            '到处跑的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210148V#020F我的行动范围\n',
            '还是以洛连特周边为主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210149V柏斯和王都也都会常去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210150V不特定所属支部的\n',
            '也就是阿加特吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210151V#1011F#5P这么一说确实是，\n',
            '阿加特很有流浪者的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210152V#1015F不过，我好像不记得\n',
            '有在洛连特见过阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210153V#027F洛连特因为有卡西乌斯老师在\n',
            '好像他就不大愿意来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210154V他有些难以面对老师\n',
            '或是自卑之类的情结。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210155V#1016F#5P啊哈哈……\n',
            '这方面倒是有点可爱呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210156V#1017F阿加特他们\n',
            '现在在干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210157V#020F调查才刚刚开始，\n',
            '还是要靠摸索吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210158V#021F好了，主日学校\n',
            '好像在村里进行呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210159V先去确认地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15F7(): pass

    label('loc_15F7')

    ChrTalk(
        0x0101,
        (
            '#0010210160V#1006F#5P嗯，ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0243, 0, 0x1218))
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x1622
@scena.Code('func_08_1622')
def func_08_1622():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 1, 0x1219)),
            Expr.Return,
        ),
        'loc_162A',
    )

    Return()

    def _loc_162A(): pass

    label('loc_162A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1644',
    )

    Call(0, 0x000A)
    FadeIn(0, 0)

    def _loc_1644(): pass

    label('loc_1644')

    EventBegin(0x00)
    ChrSetDirection(0x0000, 180, 0)
    ChrSetDirection(0x0001, 180, 0)

    ChrTalk(
        0x0101,
        (
            '#0010210161V#1026F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    StopEffect(0x85, 0x00)

    @scena.Lambda('lambda_167B')
    def lambda_167B():
        CameraMove(2428, 6000, -13190, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_167B)

    @scena.Lambda('lambda_1693')
    def lambda_1693():
        CameraSetDistance(8450, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1693)

    @scena.Lambda('lambda_16A3')
    def lambda_16A3():
        OP_6C(60000, 7000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_16A3)

    @scena.Lambda('lambda_16B3')
    def lambda_16B3():
        OP_67(0, 5095, -10000, 7000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_16B3)

    OP_12(0x000186A0, 0x0003D090, 0x00001B58)
    Sleep(7000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, 5180, 6000, -10280, 180)
    ChrSetPos(0x00F7, 6160, 6000, -8180, 180)
    CameraMove(5470, 6010, -12430, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_67(0, 8140, -10000, 0)
    OP_12(0x00000000, 0x00000000, 0x00000000)
    Sleep(500)

    @scena.Lambda('lambda_1750')
    def lambda_1750():
        ChrWalkTo(0x0101, 5180, 6010, -12580, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1750)

    @scena.Lambda('lambda_176B')
    def lambda_176B():
        ChrWalkTo(0x00F7, 6160, 6000, -12560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_176B)

    FadeIn(1000, 0)
    WaitForThreadExit(0x00F7, 0x0001)
    OP_AD('ED6_DT24/C_VIS023._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    Sleep(2000)

    OP_AE(0x000003E8)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210162V#1025F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_181C',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050210163V#052F#4P什么，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1856')

    def _loc_181C(): pass

    label('loc_181C')

    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030210164V#023F#4P艾丝蒂尔……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1856(): pass

    label('loc_1856')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210165V#1016F#5P啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210166V在这里和约修亚一起\n',
            '吃过午饭……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210167V#1025F想起一点往事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18FD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210168V#552F#4P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1923')

    def _loc_18FD(): pass

    label('loc_18FD')

    ChrTalk(
        0x0103,
        (
            '#0030210169V#522F#4P……这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1923(): pass

    label('loc_1923')

    ChrTalk(
        0x0101,
        (
            '#0010210170V#1008F#5P啊，不过，\n',
            '其实不算什么重要的回忆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210171V#1007F我就像连自己的心情\n',
            '也没注意到的孩子一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210172V完全不在意别人的眼光，\n',
            '还满不在乎地给约修亚\n',
            '喂饭什么的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210173V唉，想必约修亚\n',
            '相当受不了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A79',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210174V#051F#4P哼，现在也还是\n',
            '很孩子气啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210175V怎样？\n',
            '在这里稍事休息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD6')

    def _loc_1A79(): pass

    label('loc_1A79')

    ChrTalk(
        0x0103,
        (
            '#0030210176V#021F#4P呵呵……\n',
            '很像艾丝蒂尔呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210177V#027F怎样？\n',
            '在这里稍事休息？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AD6(): pass

    label('loc_1AD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            Expr.Return,
        ),
        'loc_1B5B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010210178V#1012F#5P不了，现在\n',
            '可不能再停留了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210179V#1011F比起这个，得先去确认\n',
            '主日学校是不是还在上课才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C09')

    def _loc_1B5B(): pass

    label('loc_1B5B')

    ChrTalk(
        0x0101,
        (
            '#0010210178V#1012F#5P不了，现在\n',
            '可不能再停留了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210181V#1011F比起这个，机会难得，\n',
            '去孤儿院看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210182V想和老师他们打个招呼，\n',
            '还要打听关于『白影』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C09(): pass

    label('loc_1C09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1C39',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210183V#051F#4P啊啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C5F')

    def _loc_1C39(): pass

    label('loc_1C39')

    ChrTalk(
        0x0103,
        (
            '#0030210184V#020F#4P嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C5F(): pass

    label('loc_1C5F')

    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetScenaFlags(ScenaFlag(0x0243, 1, 0x1219))
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x1C9A
@scena.Code('func_09_1C9A')
def func_09_1C9A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CB4',
    )

    Call(0, 0x000A)
    FadeIn(0, 0)

    def _loc_1CB4(): pass

    label('loc_1CB4')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 5780, 6000, -2110, 266)
    ChrSetPos(0x00F7, 5900, 6000, -3190, 271)
    CameraMove(4140, 6480, -3460, 0)
    OP_67(0, 8060, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(245000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '主日学校·授课中',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010210185V#1011F啊，主日学校\n',
            '好像在这里开课呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210186V#1015F好像还没结束的样子，\n',
            '在上什么课呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1E2F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210187V#051F#6P看看里面吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210188V也有可能已经结束了，\n',
            '但是忘记取掉贴纸了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E96')

    def _loc_1E2F(): pass

    label('loc_1E2F')

    ChrTalk(
        0x0103,
        (
            '#0030210189V#020F#6P看看里面的情况怎样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210190V也有可能已经结束了，\n',
            '但是忘记取掉贴纸了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E96(): pass

    label('loc_1E96')

    ChrTalk(
        0x0101,
        (
            '#0010210191V#1006F嗯，看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 4540, 6470, -2250, 2000, 0x00)
    ChrSetDirection(0x0101, 270, 0)
    Sleep(500)

    OP_6F(0x0008, 0)
    OP_70(0x0008, 3)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210192V#1015F（嗯～我看看……）',
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
            '#0010210193V#1004F（咦，那个人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x1F6A
@scena.Code('func_0A_1F6A')
def func_0A_1F6A():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1FE4'),
        (0x00000001, 'loc_1FEA'),
        (-1, 'loc_1FF0'),
    )

    def _loc_1FE4(): pass

    label('loc_1FE4')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1FF0')

    def _loc_1FEA(): pass

    label('loc_1FEA')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1FF0')

    def _loc_1FF0(): pass

    label('loc_1FF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1FFE',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_2002')

    def _loc_1FFE(): pass

    label('loc_1FFE')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_2002(): pass

    label('loc_2002')

    Return()

# id: 0x000B offset: 0x2003
@scena.Code('func_0B_2003')
def func_0B_2003():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '      卢安市长选举\n',
            '※投票日请务必\n',
            '　前往投票所\n',
            '　　　　　选举管理委员会',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x207D
@scena.Code('func_0C_207D')
def func_0C_207D():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_20B5')
    def lambda_20B5():
        CameraMove(38050, -50, 9240, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_20B5)

    @scena.Lambda('lambda_20CD')
    def lambda_20CD():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_20CD)

    @scena.Lambda('lambda_20DD')
    def lambda_20DD():
        OP_6C(315000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_20DD)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2164',
    )

    OP_C0(0x0E, 0x00000015, 0x000094FC, 0xFFFFFFD8, 0x000029B8, 0x000000B4, 0x000095A6, 0xFFFFF9FC, 0x00001B58)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_2173')

    def _loc_2164(): pass

    label('loc_2164')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2173',
    )

    EventEnd(0x01)

    def _loc_2173(): pass

    label('loc_2173')

    Return()

# id: 0x000D offset: 0x2174
@scena.Code('func_0D_2174')
def func_0D_2174():
    OP_13(0x0058)

    Return()

# id: 0x000E offset: 0x2178
@scena.Code('func_0E_2178')
def func_0E_2178():
    OP_13(0x0057)

    Return()

# id: 0x000F offset: 0x217C
@scena.Code('func_0F_217C')
def func_0F_217C():
    OP_13(0x0059)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
