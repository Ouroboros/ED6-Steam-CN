import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1310   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '赛尔斯特队长'),
    TXT(0x02, '赛罗斯副队长'),
    TXT(0x03, '士兵艾格尔'),
    TXT(0x04, '士兵迈奇'),
    TXT(0x05, '芙拉瑟'),
    TXT(0x06, '雷伊'),
    TXT(0x07, '安东尼'),
    TXT(0x08, '小说'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1310.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1310_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3EB7
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 82120,
            z                   = 0,
            y                   = 12850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 19950,
            z                   = 0,
            y                   = 22480,
            direction           = 90,
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
            x                   = 20000,
            z                   = 0,
            y                   = 7310,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 80100,
            z                   = 0,
            y                   = 11110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 82940,
            z                   = 0,
            y                   = 52010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 20490,
            z                   = 0,
            y                   = 14850,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 20480,
            z                   = 0,
            y                   = 13660,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 77080,
            z                   = 750,
            y                   = 6240,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1703943,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 20950,
            triggerZ            = 0,
            triggerY            = 22480,
            triggerRange        = 800,
            actorX              = 19950,
            actorZ              = 1600,
            actorY              = 22480,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 20950,
            triggerZ            = 0,
            triggerY            = 7310,
            triggerRange        = 800,
            actorX              = 20000,
            actorZ              = 1600,
            actorY              = 7310,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18440,
            triggerZ            = 0,
            triggerY            = 12120,
            triggerRange        = 1000,
            actorX              = 18440,
            actorZ              = 1000,
            actorY              = 12120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x256
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_272',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26F',
    )

    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)

    def _loc_26F(): pass

    label('loc_26F')

    Jump('loc_2F6')

    def _loc_272(): pass

    label('loc_272')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2C3',
    )

    SetChrPos(0x000B, 77380, 0, 7430, 186)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_297',
    )

    ClearChrFlags(0x000F, 0x0080)

    def _loc_297(): pass

    label('loc_297')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C0',
    )

    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C0',
    )

    SetChrFlags(0x000C, 0x0010)

    def _loc_2C0(): pass

    label('loc_2C0')

    Jump('loc_2F6')

    def _loc_2C3(): pass

    label('loc_2C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    SetChrPos(0x000B, 82080, 0, 56640, 357)

    Jump('loc_2F6')

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2F6',
    )

    SetChrPos(0x000B, 19210, 0, 15060, 270)

    def _loc_2F6(): pass

    label('loc_2F6')

    Return()

# id: 0x0001 offset: 0x2F7
@scena.Code('Init')
def Init():
    OP_B1('T1310_n')
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 99)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 0, 0x1210)),
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_31D',
    )

    OP_1B(0x00, 0x00, 0x000C)

    def _loc_31D(): pass

    label('loc_31D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32E',
    )

    OP_1B(0x05, 0x00, 0x000D)

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 3, 0x10BB)),
            Expr.Return,
        ),
        'loc_33A',
    )

    SetChrFlags(0x000F, 0x0080)

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38F',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_38F(): pass

    label('loc_38F')

    Return()

# id: 0x0002 offset: 0x390
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B5',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_4F7')

    def _loc_3B5(): pass

    label('loc_3B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CE',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_4F7')

    def _loc_3CE(): pass

    label('loc_3CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E7',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_4F7')

    def _loc_3E7(): pass

    label('loc_3E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_400',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_4F7')

    def _loc_400(): pass

    label('loc_400')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_419',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_4F7')

    def _loc_419(): pass

    label('loc_419')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_432',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_4F7')

    def _loc_432(): pass

    label('loc_432')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44B',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_4F7')

    def _loc_44B(): pass

    label('loc_44B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_464',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_4F7')

    def _loc_464(): pass

    label('loc_464')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47D',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_4F7')

    def _loc_47D(): pass

    label('loc_47D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_496',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_4F7')

    def _loc_496(): pass

    label('loc_496')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AF',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_4F7')

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C8',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_4F7')

    def _loc_4C8(): pass

    label('loc_4C8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E1',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_4F7')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F7',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_4F7(): pass

    label('loc_4F7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_50C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_4F7')

    def _loc_50C(): pass

    label('loc_50C')

    Return()

# id: 0x0003 offset: 0x50D
@scena.Code('func_03_50D')
def func_03_50D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_616',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CF',
    )

    ChrTalk(
        0x00FE,
        (
            '听说王立学院中\n',
            '出事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还听说军队马上\n',
            '派遣了守备队…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能有这么快的应对措施，\n',
            '多亏了通信装置的恢复啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来最可怕的事情\n',
            '就是信息和情报的无法传送了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_613')

    def _loc_5CF(): pass

    label('loc_5CF')

    ChrTalk(
        0x00FE,
        (
            '听说军队向王立学院\n',
            '派遣了部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也加强警备\n',
            '比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_613(): pass

    label('loc_613')

    Jump('loc_C7A')

    def _loc_616(): pass

    label('loc_616')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_75B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6DB',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏了那些发生器，\n',
            '通信总算是恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来，至少\n',
            '王国军可以进行整体规划行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还有很多困难要克服，\n',
            '不过凭卡西乌斯准将的指挥能力，\n',
            '相信一定没有问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_758')

    def _loc_6DB(): pass

    label('loc_6DB')

    ChrTalk(
        0x00FE,
        (
            '多亏了那些发生器，\n',
            '通信总算是恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还有很多困难要克服，\n',
            '不过凭卡西乌斯准将的指挥能力，\n',
            '相信一定没有问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_758(): pass

    label('loc_758')

    Jump('loc_C7A')

    def _loc_75B(): pass

    label('loc_75B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_81D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7B6',
    )

    ChrTalk(
        0x00FE,
        (
            '希望暂时别再\n',
            '发生什么意外了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '士兵们也需要\n',
            '稍微缓解一下神经啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81A')

    def _loc_7B6(): pass

    label('loc_7B6')

    ChrTalk(
        0x00FE,
        (
            '我们的警备状态\n',
            '终于解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当队长的话就\n',
            '不能示弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望暂时别再\n',
            '发生什么意外了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_81A(): pass

    label('loc_81A')

    Jump('loc_C7A')

    def _loc_81D(): pass

    label('loc_81D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_8AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_84F',
    )

    ChrTalk(
        0x00FE,
        (
            '传说中的龙\n',
            '竟然真的出现了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A7')

    def _loc_84F(): pass

    label('loc_84F')

    ChrTalk(
        0x00FE,
        (
            '传说中的龙\n',
            '竟然真的出现了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，看来空之女神\n',
            '真的很眷顾\n',
            '我们王国军呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_8A7(): pass

    label('loc_8A7')

    Jump('loc_C7A')

    def _loc_8AA(): pass

    label('loc_8AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_9B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_91F',
    )

    ChrTalk(
        0x00FE,
        (
            '不但平息了王都的动乱，\n',
            '国内的不安分者也全部被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样我们守备部队\n',
            '就可以高枕无忧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9B1')

    def _loc_91F(): pass

    label('loc_91F')

    ChrTalk(
        0x00FE,
        (
            '原情报部队的上校会出现，\n',
            '真是让人不敢相信…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平息了那个事件，\n',
            '国内的不安分者也全部被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样我们守备部队\n',
            '就可以高枕无忧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_9B1(): pass

    label('loc_9B1')

    Jump('loc_C7A')

    def _loc_9B4(): pass

    label('loc_9B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_A87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_A25',
    )

    ChrTalk(
        0x00FE,
        (
            '听说王立学院中\n',
            '潜藏着一名犯罪组织的成员啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '稍微一不留神就会被他们趁虚而入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A84')

    def _loc_A25(): pass

    label('loc_A25')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '听说王立学院中\n',
            '潜藏着一名犯罪组织的成员啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队高层也对那组织\n',
            '展开严密的调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A84(): pass

    label('loc_A84')

    Jump('loc_C7A')

    def _loc_A87(): pass

    label('loc_A87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_B74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AEA',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安市的市长选举\n',
            '马上也要投票了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的选举\n',
            '要是能平安结束就好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B71')

    def _loc_AEA(): pass

    label('loc_AEA')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '卢安市的市长选举\n',
            '马上也要投票了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然最近一直处于混乱状况，\n',
            '不过选举还是进入到白热化状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然应该不会出什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B71(): pass

    label('loc_B71')

    Jump('loc_C7A')

    def _loc_B74(): pass

    label('loc_B74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_C7A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BD1',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军\n',
            '依然保持着高度警戒状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的余党和空贼团\n',
            '都去向不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7A')

    def _loc_BD1(): pass

    label('loc_BD1')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '王国军\n',
            '依然保持着高度警戒状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的余党和空贼团\n',
            '都去向不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼团也就罢了，\n',
            '但特务部队实在是个隐患啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再怎么说，\n',
            '他们也是正规的精锐部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C7A(): pass

    label('loc_C7A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xC7E
@scena.Code('func_04_C7E')
def func_04_C7E():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_D5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D0A',
    )

    ChrTalk(
        0x0009,
        (
            '导力器不能用了，\n',
            '现在想做料理也很难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不能使用导力炉\n',
            '真是让人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那个神奇的发生器\n',
            '真想要1个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_D5A')

    def _loc_D0A(): pass

    label('loc_D0A')

    ChrTalk(
        0x0009,
        (
            '导力器不能用了，\n',
            '现在想做料理也很难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那个神奇的发生器\n',
            '真想要１个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D5A(): pass

    label('loc_D5A')

    Jump('loc_19F9')

    def _loc_D5D(): pass

    label('loc_D5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E09',
    )

    ChrTalk(
        0x0009,
        (
            '以前袭击这里的红莲士兵\n',
            '还带着武装精良的魔兽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然不知道他们的来历，\n',
            '不过确实是强敌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在那些家伙要是再来的话\n',
            '就真的无法抵挡了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_E69')

    def _loc_E09(): pass

    label('loc_E09')

    ChrTalk(
        0x0009,
        (
            '那些红莲士兵们\n',
            '还带着武装精良的魔兽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在那些家伙要是再来的话\n',
            '就真的无法抵挡了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E69(): pass

    label('loc_E69')

    Jump('loc_19F9')

    def _loc_E6C(): pass

    label('loc_E6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 4, 0x122C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_129C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_FB8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_EF0',
    )

    ChrTalk(
        0x0009,
        (
            '不管怎么说，这次的事件\n',
            '协会也出了很多力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '高层打算和协会深度合作，\n',
            '我也觉得这方针是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB5')

    def _loc_EF0(): pass

    label('loc_EF0')

    ChrTalk(
        0x0009,
        (
            '哟，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不管怎么说，这次的事件\n',
            '协会也出了很多力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '最近高层领导们决定\n',
            '和协会加强合作的方针，\n',
            '果然这是正确的方针啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '军队要是和游击士联手的话，\n',
            '一定可以克服任何的困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_FB5(): pass

    label('loc_FB5')

    Jump('loc_1299')

    def _loc_FB8(): pass

    label('loc_FB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_109F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1031',
    )

    ChrTalk(
        0x0009,
        (
            '龙好像逃到\n',
            '迷雾峡谷中去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那里的雾很浓，\n',
            '飞船根本飞不进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……呼，真是厉害的生物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109C')

    def _loc_1031(): pass

    label('loc_1031')

    ChrTalk(
        0x0009,
        (
            '龙好像逃到\n',
            '迷雾峡谷中去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那里的雾很浓，\n',
            '飞船根本飞不进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……呼，真是厉害的生物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_109C(): pass

    label('loc_109C')

    Jump('loc_1299')

    def _loc_109F(): pass

    label('loc_109F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1128',
    )

    ChrTalk(
        0x0009,
        (
            '最近我们关所的警备\n',
            '多少也是轻松一点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '能回到平常状态，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这下子终于也有空\n',
            '做些自己喜欢吃的料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1299')

    def _loc_1128(): pass

    label('loc_1128')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_11CF',
    )

    ChrTalk(
        0x0009,
        (
            '王立学院的事情…\n',
            '协会已经通知我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '似乎是一名犯罪组织的成员，\n',
            '呼～又出现奇怪的家伙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是一波未平一波又起。\n',
            '正义的一方总是得不到喘息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1299')

    def _loc_11CF(): pass

    label('loc_11CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1229',
    )

    ChrTalk(
        0x0009,
        (
            '这附近的魔兽\n',
            '都十分强悍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '之前有个准游击士小哥\n',
            '打不过它们逃回来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1299')

    def _loc_1229(): pass

    label('loc_1229')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1299',
    )

    ChrTalk(
        0x0009,
        (
            '关所的警备\n',
            '还是很严密的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '情报部的余党\n',
            '似乎还潜伏在各地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '总之要和游击士协会\n',
            '联手应对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1299(): pass

    label('loc_1299')

    Jump('loc_19F9')

    def _loc_129C(): pass

    label('loc_129C')

    OP_A2(0x122C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1738',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_14C4',
    )

    ChrTalk(
        0x0009,
        (
            '啊！？我还以为是谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊！好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '上次一起打退魔兽之后就没再见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1337',
    )

    ChrTalk(
        0x0103,
        (
            '#023F嘿，有这种事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1395')

    def _loc_1337(): pass

    label('loc_1337')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_136A',
    )

    ChrTalk(
        0x0104,
        (
            '#033F噢～～……\n',
            '有那种事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1395')

    def _loc_136A(): pass

    label('loc_136A')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1395',
    )

    ChrTalk(
        0x0108,
        (
            '#073F喔，还有那种事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1395(): pass

    label('loc_1395')

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，那次确实是\n',
            '第一次和阿加特并肩战斗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哈哈，那时真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过…\n',
            '今天有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F啊，其实我们\n',
            '正在寻找通缉魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '顺便就来\n',
            '这里看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那可辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样的话，\n',
            '在这里稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这附近的通缉魔兽\n',
            '都十分强悍的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F谢谢啦。\n',
            '那就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1735')

    def _loc_14C4(): pass

    label('loc_14C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1735',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0106, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊！？我还以为是谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊！好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '上次一起打退魔兽之后就没再见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1571',
    )

    ChrTalk(
        0x0107,
        (
            '#064F啊……\n',
            '有那种事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15FB')

    def _loc_1571(): pass

    label('loc_1571')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_159D',
    )

    ChrTalk(
        0x0103,
        (
            '#023F嘿，有这种事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15FB')

    def _loc_159D(): pass

    label('loc_159D')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15D0',
    )

    ChrTalk(
        0x0104,
        (
            '#033F噢～～……\n',
            '有那种事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15FB')

    def _loc_15D0(): pass

    label('loc_15D0')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15FB',
    )

    ChrTalk(
        0x0108,
        (
            '#073F喔，还有那种事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15FB(): pass

    label('loc_15FB')

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，那次确实是\n',
            '第一次和阿加特并肩战斗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '哈哈，那时真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过…\n',
            '今天有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F啊，其实我们\n',
            '正在寻找通缉魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '顺便就来\n',
            '这里看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)

    ChrTalk(
        0x0009,
        (
            '那可辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样的话，\n',
            '在这里稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这附近的通缉魔兽\n',
            '都十分强悍的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F谢谢啦。\n',
            '那就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1735(): pass

    label('loc_1735')

    Jump('loc_19F9')

    def _loc_1738(): pass

    label('loc_1738')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_17E6',
    )

    ChrTalk(
        0x0009,
        (
            '啊！？我还以为是谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊！好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '上次一起打退魔兽之后就没再见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，还有那种事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F那时确实是\n',
            '第一次和阿加特并肩战斗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189C')

    def _loc_17E6(): pass

    label('loc_17E6')

    ChrTurnDirection(0x0009, 0x0101, 0)

    ChrTalk(
        0x0009,
        (
            '啊！？我还以为是谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '上次在这里一起打退\n',
            '魔兽之后就一直没见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F嘿，有这种事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，那时还是第一次\n',
            '和阿加特并肩作战呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_189C(): pass

    label('loc_189C')

    ChrTalk(
        0x0009,
        (
            '哈哈，那时真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过…\n',
            '今天有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1901',
    )

    ChrTalk(
        0x0106,
        (
            '#050F啊，只是顺路\n',
            '过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1927')

    def _loc_1901(): pass

    label('loc_1901')

    ChrTalk(
        0x0103,
        (
            '#020F没什么，只是顺路\n',
            '过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1927(): pass

    label('loc_1927')

    ChrTalk(
        0x0009,
        (
            '原来如此。\n',
            '是在修行中吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哈，难得来一趟。\n',
            '就在这里稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这附近的魔兽可是很强的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯，谢谢了。\n',
            '那就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好了，我也要回去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果有事的话\n',
            '就再来找我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_19F9(): pass

    label('loc_19F9')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x19FD
@scena.Code('func_05_19FD')
def func_05_19FD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1B13',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AAE',
    )

    ChrTalk(
        0x00FE,
        (
            '导力枪无法使用\n',
            '对我们来说是最大的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除了士官以上的长官，\n',
            '普通的士兵并不会什么剑术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是那群红莲士兵再来袭击的话\n',
            '我们还能应付得了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1B10')

    def _loc_1AAE(): pass

    label('loc_1AAE')

    ChrTalk(
        0x00FE,
        (
            '导力枪无法使用\n',
            '对我们来说是最大的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除了士官以上的长官，\n',
            '普通的士兵并不会什么剑术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B10(): pass

    label('loc_1B10')

    Jump('loc_2147')

    def _loc_1B13(): pass

    label('loc_1B13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C28',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BC9',
    )

    ChrTalk(
        0x00FE,
        (
            '空中出现了奇怪的东西，\n',
            '导力器也无法使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国这次\n',
            '真是面临重大危机了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如、如果帝国\n',
            '在这时候乘人之危的话…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……还、还是不要想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1C25')

    def _loc_1BC9(): pass

    label('loc_1BC9')

    ChrTalk(
        0x00FE,
        (
            '空中出现了奇怪的东西，\n',
            '导力器也无法使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国这次\n',
            '真是面临重大危机了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C25(): pass

    label('loc_1C25')

    Jump('loc_2147')

    def _loc_1C28(): pass

    label('loc_1C28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1C9C',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然不知道具体过程，\n',
            '不过龙的骚乱总算是平息了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，摩尔根将军在关键时刻\n',
            '果然还是值得信赖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2147')

    def _loc_1C9C(): pass

    label('loc_1C9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1D77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1D03',
    )

    ChrTalk(
        0x00FE,
        (
            '龙明明在峡谷，\n',
            '为什么我们要在这里警戒？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队这种机构\n',
            '就是这样不讲究效率啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D74')

    def _loc_1D03(): pass

    label('loc_1D03')

    ChrTalk(
        0x00FE,
        (
            '呼，进入警备状态之后\n',
            '又要开始夜间巡逻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，龙在峡谷吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么我们古罗尼关所\n',
            '也要警备呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1D74(): pass

    label('loc_1D74')

    Jump('loc_2147')

    def _loc_1D77(): pass

    label('loc_1D77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1F59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 3, 0x10BB)),
            Expr.Return,
        ),
        'loc_1DE4',
    )

    ChrTalk(
        0x00FE,
        (
            '这样一来，剩下的乐趣\n',
            '就只有副队长的料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不是很懂，\n',
            '不过那真是职业水准啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F56')

    def _loc_1DE4(): pass

    label('loc_1DE4')

    ChrTalk(
        0x00FE,
        (
            '啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这本书本来打算\n',
            '吃完晚饭再看的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过看得太入神，\n',
            '这么快就已经看完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个关所里\n',
            '真是没什么娱乐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，这本书就送你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000F, 0x0080)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 ７卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 ７卷'], 1)
    OP_A2(0x10BB)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '这样一来，剩下的乐趣\n',
            '就只有副队长的料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不是很懂，\n',
            '不过那真是职业水准啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近比较有时间，\n',
            '经常在厨房里待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F56(): pass

    label('loc_1F56')

    Jump('loc_2147')

    def _loc_1F59(): pass

    label('loc_1F59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1FE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1F98',
    )

    ChrTalk(
        0x00FE,
        (
            '今天轮到副队长做饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FE6')

    def _loc_1F98(): pass

    label('loc_1F98')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '今天轮到副队长做饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～今天会做\n',
            '什么菜呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FE6(): pass

    label('loc_1FE6')

    Jump('loc_2147')

    def _loc_1FE9(): pass

    label('loc_1FE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_203D',
    )

    ChrTalk(
        0x00FE,
        (
            '柴火已经准备好了，\n',
            '食材也准备完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～接下来\n',
            '总算可以休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2147')

    def _loc_203D(): pass

    label('loc_203D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2147',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_20A4',
    )

    ChrTalk(
        0x00FE,
        (
            '说起这里的乐趣，\n',
            '也就只剩下副队长的料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他退役之后\n',
            '完全可以开家餐厅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2147')

    def _loc_20A4(): pass

    label('loc_20A4')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '哈哈～在山上真是\n',
            '没有什么乐趣可言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说卢安开了新的\n',
            '游戏吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起这里的乐趣，\n',
            '也就只剩下副队长的料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他退役之后\n',
            '完全可以开家餐厅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2147(): pass

    label('loc_2147')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x214B
@scena.Code('func_06_214B')
def func_06_214B():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_224D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F4',
    )

    ChrTalk(
        0x000A,
        (
            '虽然现在关所这么严格，\n',
            '谁也不能通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呼～其实这种时候\n',
            '也不会有人来旅行啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '除了真的很闲很闲的人，\n',
            '也就只有你们游击士会来这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_224A')

    def _loc_21F4(): pass

    label('loc_21F4')

    ChrTalk(
        0x000A,
        (
            '虽然现在关所这么严格，\n',
            '谁也不能通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呼～其实这种时候\n',
            '也不会有人来旅行啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_224A(): pass

    label('loc_224A')

    Jump('loc_26A9')

    def _loc_224D(): pass

    label('loc_224D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2324',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22EF',
    )

    ChrTalk(
        0x000A,
        (
            '大门的开关坏了，\n',
            '所以现在的通行检查更加严格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，你们游击士是\n',
            '可以自由通行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '上面有命令下达。\n',
            '和协会的合作是必不可少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_2321')

    def _loc_22EF(): pass

    label('loc_22EF')

    ChrTalk(
        0x000A,
        (
            '你们游击士\n',
            '可以自由通行的。\n',
            '上面下达过命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2321(): pass

    label('loc_2321')

    Jump('loc_26A9')

    def _loc_2324(): pass

    label('loc_2324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2388',
    )

    ChrTalk(
        0x000A,
        (
            '听说那条龙\n',
            '终于不再作乱了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '连飞行舰队都出动了，\n',
            '这样的结果也是可以预料到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A9')

    def _loc_2388(): pass

    label('loc_2388')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2441',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_23DF',
    )

    ChrTalk(
        0x000A,
        (
            '情报部的余党…\n',
            '然后又出现古代龙…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的，\n',
            '这也太夸张了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_243E')

    def _loc_23DF(): pass

    label('loc_23DF')

    ChrTalk(
        0x000A,
        (
            '还要继续警备啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '情报部的余党…\n',
            '然后又出现古代龙…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的，\n',
            '这也太夸张了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_243E(): pass

    label('loc_243E')

    Jump('loc_26A9')

    def _loc_2441(): pass

    label('loc_2441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_253B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_24AE',
    )

    ChrTalk(
        0x000A,
        (
            '卢安的新市长\n',
            '已经选中诺曼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '他虽然主张发展观光旅游业，\n',
            '但也考虑到了港湾的维持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2538')

    def _loc_24AE(): pass

    label('loc_24AE')

    ChrTalk(
        0x000A,
        (
            '卢安的新市长\n',
            '已经选中诺曼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '他虽然主张发展观光旅游业，\n',
            '但也考虑到了港湾的维持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呼，果然把两边处理平衡\n',
            '才能得人心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_2538(): pass

    label('loc_2538')

    Jump('loc_26A9')

    def _loc_253B(): pass

    label('loc_253B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_25DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2581',
    )

    ChrTalk(
        0x000A,
        (
            '啊啊～能不能尽快\n',
            '将情报部的余党统统抓捕起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25DA')

    def _loc_2581(): pass

    label('loc_2581')

    OP_A2(0x0001)

    ChrTalk(
        0x000A,
        (
            '这样的警备状态\n',
            '究竟要持续到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '夜里出来巡逻的时候\n',
            '真是寒风刺骨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25DA(): pass

    label('loc_25DA')

    Jump('loc_26A9')

    def _loc_25DD(): pass

    label('loc_25DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_264A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_261B',
    )

    ChrTalk(
        0x000A,
        (
            '不过无论工不工作，\n',
            '领的薪水都是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2647')

    def _loc_261B(): pass

    label('loc_261B')

    OP_A2(0x0001)

    ChrTalk(
        0x000A,
        (
            '最近都没有客人，\n',
            '这里也暂时停业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2647(): pass

    label('loc_2647')

    Jump('loc_26A9')

    def _loc_264A(): pass

    label('loc_264A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_26A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2676',
    )

    ChrTalk(
        0x000A,
        (
            '难道你们\n',
            '喜欢爬山吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A9')

    def _loc_2676(): pass

    label('loc_2676')

    OP_A2(0x0001)

    ChrTalk(
        0x000A,
        (
            '竟然现在还来这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还真是有闲心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A9(): pass

    label('loc_26A9')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x26AD
@scena.Code('func_07_26AD')
def func_07_26AD():
    TalkBegin(0x000C)

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_26C1',
    )

    Call(1, 0x0000)

    Jump('loc_2DC1')

    def _loc_26C1(): pass

    label('loc_26C1')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_27B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_278B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_271C',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在参观\n',
            '这里的设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '能不能别打扰我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2788')

    def _loc_271C(): pass

    label('loc_271C')

    ChrTalk(
        0x00FE,
        (
            '啊，各位…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再来这里\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在参观\n',
            '这里的设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '能不能别打扰我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2788(): pass

    label('loc_2788')

    Jump('loc_27B6')

    def _loc_278B(): pass

    label('loc_278B')

    ChrTalk(
        0x00FE,
        (
            '我还要继续\n',
            '参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_27B6(): pass

    label('loc_27B6')

    Jump('loc_2DC1')

    def _loc_27B9(): pass

    label('loc_27B9')

    ChrTalk(
        0x00FE,
        (
            '呼，总算\n',
            '来到关所了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就一直待在这里\n',
            '绝对不能回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果\n',
            '不安排人来迎接我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F（嗯……！？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F（啊、这个人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x00FE, 0x0010)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(700)

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊？你还记得我吗？\n',
            '我是王立学院的芙拉瑟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29F1',
    )

    ChrTalk(
        0x0101,
        (
            '#1018F啊、嗯！\n',
            '当然记得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F你好啊，芙拉瑟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真没想到能在这种地方\n',
            '再见到你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '啊？！科洛丝竟然也在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们两个\n',
            '为什么会来这种地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯、我们的工作\n',
            '是来这里寻找通缉魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '倒是芙拉瑟你，\n',
            '为什么会在关所呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD0')

    def _loc_29F1(): pass

    label('loc_29F1')

    ChrTalk(
        0x0101,
        (
            '#1001F啊、嗯！\n',
            '当然记得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '幽灵骚乱的时候\n',
            '曾经在王立学院见过面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，能再次见面真是高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，为什么\n',
            '要来这种地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯、我们的工作\n',
            '是来这里寻找通缉魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '倒是芙拉瑟你，\n',
            '为什么会在关所呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AD0(): pass

    label('loc_2AD0')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '……………啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1015F嗯？怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x00FE,
        (
            '啊，没、没什么……\n',
            '什么事也没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(30)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '那、什…么……\n',
            '那个、就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(600)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '对了！社会参观…\n',
            '我来关所进行社会参观考察！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '准备用做休假时的\n',
            '研究课题！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F嘿～是这样啊。\n',
            '你还真是用心学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C89',
    )

    ChrTalk(
        0x0105,
        (
            '#044F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（有那样的课题吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D49')

    def _loc_2C89(): pass

    label('loc_2C89')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CD8',
    )

    ChrTalk(
        0x0107,
        (
            '#560F社会参观吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '学院的课题好有趣啊，\n',
            '真是让提妲羡慕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D49')

    def _loc_2CD8(): pass

    label('loc_2CD8')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D13',
    )

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，不愧是王国\n',
            '最好的学校啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D49')

    def _loc_2D13(): pass

    label('loc_2D13')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D49',
    )

    ChrTalk(
        0x0108,
        (
            '#070F嗯，不愧是王立学院\n',
            '的学生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D49(): pass

    label('loc_2D49')

    ChrTalk(
        0x00FE,
        (
            '那么，我还在\n',
            '参观中，所以…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#1008F啊、抱歉！\n',
            '打扰你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F那么、再见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，再见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007A, 0x01, 0x4000)
    OP_A2(0x0004)

    def _loc_2DC1(): pass

    label('loc_2DC1')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x2DC5
@scena.Code('func_08_2DC5')
def func_08_2DC5():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 7, 0x20AF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32B4',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，各位游击士。\n',
            '能在这里见面真是奇遇啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E74',
    )

    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#064F啊！雷伊先生！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊、你为什么会\n',
            '在这种地方呢？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)
    OP_A2(0x20B0)

    Jump('loc_2EC0')

    def _loc_2E74(): pass

    label('loc_2E74')

    ChrTalk(
        0x0101,
        (
            '#1004F啊……！？\n',
            '是中央工房的人啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为、为什么会在这种地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    def _loc_2EC0(): pass

    label('loc_2EC0')

    ChrTalk(
        0x00FE,
        (
            '嗯，其实我刚从『埃尔赛尤』下船，\n',
            '现在正好返回蔡斯的途中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经帮完博士的忙了，\n',
            '接下来就该回实验室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F所、所以要\n',
            '步行去蔡斯吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F不过，现在似乎\n',
            '也没有别的交通工具啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1040F不如我们\n',
            '把你送回去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '哈哈～不用担心。\n',
            '有人和我同行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000E, 255)
    ChrTurnDirection(0x000E, 0x0000, 400)
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x000E,
        (
            '喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#1001F哈哈……\n',
            '安东尼也在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '其实它真的很可靠呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '另外我还准备了\n',
            '各种对抗魔兽的食品武器…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……对了，难得见面，\n',
            '不如你们也试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['极光不可思议玉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['极光不可思议玉'], 1)

    ChrTalk(
        0x00FE,
        (
            '我发明的攻击性食品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时你们也可以自己制作，\n',
            '有兴趣的话试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_AC(0x0045)"),
            Expr.Return,
        ),
        'loc_3134',
    )

    Jump('loc_317B')

    def _loc_3134(): pass

    label('loc_3134')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['极光不可思议玉']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_317B(): pass

    label('loc_317B')

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#1016F啊、谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '让、让他一个人回去\n',
            '真的没问题吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1048F其实我也很担心呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1040F……不过、他本人已经说没问题……\n',
            '那，路上请一定小心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '特别是卡鲁迪亚隧道，\n',
            '那里现在非常危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '呵呵，多谢忠告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，下次在蔡斯再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x000E,
        (
            '喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000E, 0, 400)
    OP_4B(0x000E, 255)
    OP_A2(0x20AF)

    Jump('loc_333D')

    def _loc_32B4(): pass

    label('loc_32B4')

    ChrTalk(
        0x00FE,
        (
            '已经帮完博士的忙了，\n',
            '我必须要早点回实验室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能把温室交给蒂亚利\n',
            '一个人照看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，再见啦，各位。\n',
            '下次在蔡斯再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_333D(): pass

    label('loc_333D')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x3341
@scena.Code('func_09_3341')
def func_09_3341():
    TalkBegin(0x000E)
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x3357
@scena.Code('func_0A_3357')
def func_0A_3357():
    Call(0, 0x0004)

    Return()

# id: 0x000B offset: 0x335C
@scena.Code('func_0B_335C')
def func_0B_335C():
    Call(0, 0x0006)

    Return()

# id: 0x000C offset: 0x3361
@scena.Code('func_0C_3361')
def func_0C_3361():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3590',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3476',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33FC',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201399V#020F通过这里就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220134V接下来要去的应该是蔡斯地区。\n',
            '还是乘坐定期船去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3473')

    def _loc_33FC(): pass

    label('loc_33FC')

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201399V#020F通过这里就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220134V接下来要去的应该是蔡斯地区。\n',
            '还是乘坐定期船去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3473(): pass

    label('loc_3473')

    Jump('loc_3572')

    def _loc_3476(): pass

    label('loc_3476')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3572',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34FF',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201403V#050F前方就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220138V接下来要去的应该是蔡斯地区。\n',
            '还是去乘坐定期船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3572')

    def _loc_34FF(): pass

    label('loc_34FF')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201403V#050F前方就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220138V接下来要去的应该是蔡斯地区。\n',
            '还是去乘坐定期船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3572(): pass

    label('loc_3572')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_37BC')

    def _loc_3590(): pass

    label('loc_3590')

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3699',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_361F',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201399V#020F通过这里就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201400V现在没时间去其它的地方了，\n',
            '集中解决卢安的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3696')

    def _loc_361F(): pass

    label('loc_361F')

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201399V#020F通过这里就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201400V现在没时间去其它的地方了，\n',
            '集中解决卢安的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3696(): pass

    label('loc_3696')

    Jump('loc_37A1')

    def _loc_3699(): pass

    label('loc_3699')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_37A1',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3728',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201403V#050F前方就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201404V现在没时间去其它的地方了，\n',
            '赶快集中精力解决卢安的工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37A1')

    def _loc_3728(): pass

    label('loc_3728')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050201403V#050F前方就是柏斯地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201404V现在没时间去其它的地方了，\n',
            '赶快集中精力解决卢安的工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37A1(): pass

    label('loc_37A1')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_37BC(): pass

    label('loc_37BC')

    Return()

# id: 0x000D offset: 0x37BD
@scena.Code('func_0D_37BD')
def func_0D_37BD():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3A96',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_383C',
    )

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080311445V#070F嗯，那边就是卢安了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080311446V也没什么事要去那边，\n',
            '还是赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A93')

    def _loc_383C(): pass

    label('loc_383C')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38B1',
    )

    ChrTurnDirection(0x0109, 0x0000, 400)

    ChrTalk(
        0x0109,
        (
            '#0180311447V#1060F那边就是卢安了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180311448V也没什么特别的事要过去，\n',
            '还是回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A93')

    def _loc_38B1(): pass

    label('loc_38B1')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3932',
    )

    ChrTurnDirection(0x0104, 0x0000, 400)

    ChrTalk(
        0x0104,
        (
            '#0040311449V#030F嗯，通过这里\n',
            '就是卢安地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040311450V现在还没必要过去吧，\n',
            '今天还是回去好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A93')

    def _loc_3932(): pass

    label('loc_3932')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39A8',
    )

    ChrTurnDirection(0x0105, 0x0000, 400)

    ChrTalk(
        0x0105,
        (
            '#0060311451V#040F前方就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060311452V也没什么重要的事，\n',
            '今天还是回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A93')

    def _loc_39A8(): pass

    label('loc_39A8')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A1A',
    )

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220141V#050F前边就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311454V也没什么事情，\n',
            '今天还是回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A93')

    def _loc_3A1A(): pass

    label('loc_3A1A')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A93',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030311455V#020F前面就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030311456V反正也没有什么事要过去，\n',
            '不如早点回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A93(): pass

    label('loc_3A93')

    Jump('loc_3C6E')

    def _loc_3A96(): pass

    label('loc_3A96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3B7E',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B12',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311445V#070F嗯，那边就是卢安了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080311458V现在的当务之急是抓捕龙！\n',
            '赶快去迷雾峡谷吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B7B')

    def _loc_3B12(): pass

    label('loc_3B12')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050220141V#050F前边就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311460V现在的首要任务是龙！\n',
            '赶快去迷雾峡谷吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B7B(): pass

    label('loc_3B7B')

    Jump('loc_3C6E')

    def _loc_3B7E(): pass

    label('loc_3B7E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BF1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080311461V#070F喂，那边就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080271276V现在没空去其他的地方了，\n',
            '赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C6E')

    def _loc_3BF1(): pass

    label('loc_3BF1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C07',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_3C0E')

    def _loc_3C07(): pass

    label('loc_3C07')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_3C0E(): pass

    label('loc_3C0E')

    ChrTalk(
        0x0106,
        (
            '#0050220141V#050F前边就是卢安地区了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311464V现在没空去其他的地方了，\n',
            '赶快回去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C6E(): pass

    label('loc_3C6E')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000E offset: 0x3C8A
@scena.Code('func_0E_3C8A')
def func_0E_3C8A():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CDD',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_3E98')

    def _loc_3CDD(): pass

    label('loc_3CDD')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
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
            TXT(0x00, '在这里休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E7D',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 0x00000032)
    OP_73(0x0005)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0005, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_3E7D(): pass

    label('loc_3E7D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E97',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_3E97(): pass

    label('loc_3E97')

    Return()

    def _loc_3E98(): pass

    label('loc_3E98')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
