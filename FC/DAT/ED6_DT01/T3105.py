import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3105_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3105   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3105.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '格斯塔夫维修长',
            x                   = -37000,
            z                   = -3800,
            y                   = 145500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '吉拉尔',
            x                   = -20110,
            z                   = 8000,
            y                   = 121830,
            direction           = 177,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '多杰',
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '巴拉特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '蔡斯市·工房区',
            x                   = -18770,
            z                   = 8000,
            y                   = 89560,
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

# id: 0x10002 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -41010,
            triggerZ            = 8000,
            triggerY            = 122500,
            triggerRange        = 800,
            actorX              = -41010,
            actorZ              = 10200,
            actorY              = 122500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -38900,
            triggerZ            = 8400,
            triggerY            = 122040,
            triggerRange        = 800,
            actorX              = -38900,
            actorZ              = 9900,
            actorY              = 122040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x27A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_2B7',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -17880, 8000, 118110, 183)
    CreateThread(0x000E, 0x00, 0x00, func_03_66C)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44660, 8000, 129500, 5)

    Jump('loc_4DB')

    def _loc_2B7(): pass

    label('loc_2B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2F4',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -17880, 8000, 118110, 183)
    CreateThread(0x000E, 0x00, 0x00, func_03_66C)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44660, 8000, 129500, 5)

    Jump('loc_4DB')

    def _loc_2F4(): pass

    label('loc_2F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_314',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_4DB')

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_37D',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -47500, -4000, 151780, 261)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -47500, -4000, 152840, 261)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -40130, 8000, 125930, 237)
    CreateThread(0x000C, 0x00, 0x00, func_04_690)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_4DB')

    def _loc_37D(): pass

    label('loc_37D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3BD',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -44530, -4000, 142000, 176)
    ChrSetFlags(0x0008, 0x0010)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44510, -4000, 140610, 21)
    ChrSetFlags(0x0010, 0x0010)

    Jump('loc_4DB')

    def _loc_3BD(): pass

    label('loc_3BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3FA',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -58040, 4000, 125930, 187)
    CreateThread(0x0008, 0x00, 0x00, func_06_6D8)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_4DB')

    def _loc_3FA(): pass

    label('loc_3FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_404',
    )

    Jump('loc_4DB')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_441',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -49800, 8000, 117400, 3)
    CreateThread(0x0008, 0x00, 0x00, func_05_6B4)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_4DB')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_461',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_4DB')

    def _loc_461(): pass

    label('loc_461')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_481',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_4DB')

    def _loc_481(): pass

    label('loc_481')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_4A1',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_4DB')

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4DB',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -40130, 8000, 125930, 237)
    CreateThread(0x000C, 0x00, 0x00, func_04_690)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    def _loc_4DB(): pass

    label('loc_4DB')

    Return()

# id: 0x0001 offset: 0x4DC
@scena.Code('func_01_4DC')
def func_01_4DC():
    OP_16(0x02, 4000, -172000, 20000, 196691)

    Return()

# id: 0x0002 offset: 0x4EF
@scena.Code('func_02_4EF')
def func_02_4EF():
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
        'loc_514',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_656')

    def _loc_514(): pass

    label('loc_514')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_656')

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_546',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_656')

    def _loc_546(): pass

    label('loc_546')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_656')

    def _loc_55F(): pass

    label('loc_55F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_578',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_656')

    def _loc_578(): pass

    label('loc_578')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_591',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_656')

    def _loc_591(): pass

    label('loc_591')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AA',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_656')

    def _loc_5AA(): pass

    label('loc_5AA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_656')

    def _loc_5C3(): pass

    label('loc_5C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DC',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_656')

    def _loc_5DC(): pass

    label('loc_5DC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_656')

    def _loc_5F5(): pass

    label('loc_5F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60E',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_656')

    def _loc_60E(): pass

    label('loc_60E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_627',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_656')

    def _loc_627(): pass

    label('loc_627')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_640',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_656')

    def _loc_640(): pass

    label('loc_640')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_656',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_656(): pass

    label('loc_656')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_66B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_656')

    def _loc_66B(): pass

    label('loc_66B')

    Return()

# id: 0x0003 offset: 0x66C
@scena.Code('func_03_66C')
def func_03_66C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_68F',
    )

    OP_8D(0x00FE, -19390, 119560, -16690, 116060, 3000)

    Jump('func_03_66C')

    def _loc_68F(): pass

    label('loc_68F')

    Return()

# id: 0x0004 offset: 0x690
@scena.Code('func_04_690')
def func_04_690():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6B3',
    )

    OP_8D(0x00FE, -35820, 123780, -43940, 129220, 3000)

    Jump('func_04_690')

    def _loc_6B3(): pass

    label('loc_6B3')

    Return()

# id: 0x0005 offset: 0x6B4
@scena.Code('func_05_6B4')
def func_05_6B4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6D7',
    )

    OP_8D(0x00FE, -45240, 117320, -51970, 121500, 3000)

    Jump('func_05_6B4')

    def _loc_6D7(): pass

    label('loc_6D7')

    Return()

# id: 0x0006 offset: 0x6D8
@scena.Code('func_06_6D8')
def func_06_6D8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6FB',
    )

    OP_8D(0x00FE, -56420, 122640, -59470, 129340, 3000)

    Jump('func_06_6D8')

    def _loc_6FB(): pass

    label('loc_6FB')

    Return()

# id: 0x0007 offset: 0x6FC
@scena.Code('func_07_6FC')
def func_07_6FC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_74D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '都不通知一下就检查，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军真是的，\n',
            '实在太乱来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D18')

    def _loc_74D(): pass

    label('loc_74D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_7A7',
    )

    ChrTalk(
        0x00FE,
        (
            '一会儿『赛希莉亚号』\n',
            '就要开过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须马上开始\n',
            '确认下拢岸的状况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D18')

    def _loc_7A7(): pass

    label('loc_7A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_81B',
    )

    ChrTalk(
        0x00FE,
        (
            '工房船现在\n',
            '马上就要出航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '却比预定去要塞的时间提前了很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D18')

    def _loc_81B(): pass

    label('loc_81B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_873',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '这样飞船起航就告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '趁这段时间整理一下货物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D18')

    def _loc_873(): pass

    label('loc_873')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_93D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_8F7',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，这种时候\n',
            '真是羡慕雷曼那家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙兼任驾驶员，\n',
            '飞行前为了调整身体状态，\n',
            '早早地就回家去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_93A')

    def _loc_8F7(): pass

    label('loc_8F7')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '呼，明天还是要去要塞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近的工作\n',
            '好像很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_93A(): pass

    label('loc_93A')

    Jump('loc_D18')

    def _loc_93D(): pass

    label('loc_93D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_9BA',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房的事件\n',
            '应该解决了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎？\n',
            '犯人到现在都还没抓到？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那还真是糟糕啊。\n',
            '下次不会来袭击工房船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D18')

    def _loc_9BA(): pass

    label('loc_9BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_B52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_A75',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，都是因为那个公爵大人，\n',
            '搞得大家都对王家的印象变差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，很久以前\n',
            '那种快乐纯粹的女王诞辰庆典\n',
            '是很难再出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该死，那个混账公爵。\n',
            '还我的诞辰庆典来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4F')

    def _loc_A75(): pass

    label('loc_A75')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '之前的休假\n',
            '我去参观了\n',
            '艾尔·雷登瀑布……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟遇到那个叫杜什么的公爵，\n',
            '那个王家的人微服出行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且那个人\n',
            '还蛮横任性得要命。\n',
            '真是倒了大霉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，大家都没想到\n',
            '王家的人竟会是那个样子。\n',
            '真是失望透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B4F(): pass

    label('loc_B4F')

    Jump('loc_D18')

    def _loc_B52(): pass

    label('loc_B52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_BD5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B89',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '差不多该到返航的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BD2')

    def _loc_B89(): pass

    label('loc_B89')

    ChrTalk(
        0x00FE,
        (
            '怎么样？很漂亮吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可是中央工房引以为傲的\n',
            '『莱普尼兹号』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BD2(): pass

    label('loc_BD2')

    Jump('loc_D18')

    def _loc_BD5(): pass

    label('loc_BD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_CCA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_C40',
    )

    ChrTalk(
        0x00FE,
        (
            '工房好像还没找出\n',
            '昨天那种现象的原因所在吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，\n',
            '希望不要再发生这种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CC7')

    def _loc_C40(): pass

    label('loc_C40')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上，导力供应停止了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还好不是在白天发生，\n',
            '真是万幸呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在飞艇上出现这种情况，\n',
            '真不知道会发生什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CC7(): pass

    label('loc_CC7')

    Jump('loc_D18')

    def _loc_CCA(): pass

    label('loc_CCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D18',
    )

    ChrTalk(
        0x00FE,
        (
            '好的，拢岸准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来，\n',
            '要快点进行出发前的检查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D18(): pass

    label('loc_D18')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xD1C
@scena.Code('func_08_D1C')
def func_08_D1C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_DDF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560091531V#690F哦，稍微晚了些真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560091532V要塞那边又来要求我们出动了。\n',
            '我想今天之内\n',
            '就可以做好准备了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560091533V嗯，希望和平时一样\n',
            '不要发生什么意外就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_DDF(): pass

    label('loc_DDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_F11',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560091534V#690F哦，是提妲丫头。\n',
            '没有受伤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091535V#060F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091536V啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091537V啊……是、是的！\n',
            '没事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0560091538V#690F怎么啦？\n',
            '你一直在发呆啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560091539V不过，没受伤的话，\n',
            '那比什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091540V#060F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_F11(): pass

    label('loc_F11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1047',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F56',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560071605V#690F哦，是提妲丫头。\n',
            '多多保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1047')

    def _loc_F56(): pass

    label('loc_F56')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0560071599V#690F哦，是提妲丫头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071600V又是拉赛尔老爷子的差使吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071601V#060F啊，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071602V要到亚尔摩村去一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0560071603V#690F是吗，那么\n',
            '多多保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071604V#060F嗯，\n',
            '那么我们就出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1047(): pass

    label('loc_1047')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x104B
@scena.Code('func_09_104B')
def func_09_104B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_106B',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵－噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1085')

    def _loc_106B(): pass

    label('loc_106B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1085',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1085(): pass

    label('loc_1085')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1089
@scena.Code('func_0A_1089')
def func_0A_1089():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 2, 0x602)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1479',
    )

    SetScenaFlags(ScenaFlag(0x00C0, 4, 0x604))
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -20510, 8000, 119230, 0)
    ChrSetPos(0x0102, -18980, 8000, 119430, 0)

    @scena.Lambda('lambda_10CA')
    def lambda_10CA():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10CA)

    @scena.Lambda('lambda_10DA')
    def lambda_10DA():
        CameraSetDistance(2750, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_10DA)

    CameraMove(-20210, 8000, 122050, 2000)

    ChrTalk(
        0x0009,
        (
            '#1970100284V啊，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100285V就像刚才我说的，\n',
            '飞艇什么时候能来还不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100286V实在抱歉，\n',
            '你们在游击士协会等一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯～其实……\n',
            '我们稍微改变了一下计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100288V#010F抱歉，\n',
            '搭乘手续能取消吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100289V是这样吗……\n',
            '唉，也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100290V在定期船到来之前，\n',
            '不需要付取消手续费的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100291V把刚才的船票\n',
            '还给我就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100292V#000F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把两张船票还给了接待员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    RemoveItem(0x036A, 2)

    ChrTalk(
        0x0009,
        (
            '#1970100293V哦……\n',
            '好像是军用警备飞艇来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100294V来的还真早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那、那么\n',
            '我们赶快……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_135E')
    def lambda_135E():
        ChrWalkTo(0x00FE, -20180, 8000, 103080, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_135E)

    ChrTalk(
        0x0102,
        (
            '#0020100296V#010F麻烦您了，\n',
            '真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13A9')
    def lambda_13A9():
        ChrWalkTo(0x00FE, -18440, 8000, 103080, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_13A9)

    ChrTalk(
        0x0009,
        (
            '啊啊。\n',
            '欢迎下次再来乘坐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0610100298V#180F哼哼……\n',
            '还真是忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610100299V首先，还是去\n',
            '拜见一下工房长吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，不愧是上校大人……\n',
            '能想出这样的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2187')

    def _loc_1479(): pass

    label('loc_1479')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 2, 0x602)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_163C',
    )

    SetScenaFlags(ScenaFlag(0x00C0, 2, 0x602))
    OP_28(0x0054, 0x01, 0x0002)
    EventBegin(0x00)
    OP_69(0x0009, 1000)

    ChrTalk(
        0x0009,
        (
            '#1970100192V啊，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100193V我已经从雾香那里听说了。\n',
            '现在就办理搭乘手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100195V那么，在这张单子上\n',
            '填写姓名和联络方式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100196V#010F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔\n',
            '办理了搭乘手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#1970100197V好了，\n',
            '这个就是你们的船票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100198V定期船到了之后，\n',
            '把这个出示给乘务员就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '得到两张船票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x036A, 2)
    EventEnd(0x01)

    Jump('loc_2187')

    def _loc_163C(): pass

    label('loc_163C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C65',
    )

    SetScenaFlags(ScenaFlag(0x00A2, 7, 0x517))
    MapClearFlags(0x00000001)
    OP_69(0x0009, 1000)

    ChrTalk(
        0x0009,
        (
            '#1970071394V哟！要乘坐飞行船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071395V去西面的定期船的话\n',
            '正好刚刚开走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071396V#000F没有啊，\n',
            '我们不是来乘飞行船的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071397V格斯塔夫维修长\n',
            '我想让你们两人办点事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071398V什么，找大叔的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071399V大叔的话，\n',
            '现在不在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071400V#000F哎！出去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071401V是呀。有两三天了。\n',
            '去了雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071402V好像很急，是个有\n',
            '军用警备飞艇的家伙的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071403V#000F到雷斯顿要塞呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071404V#010F是位于瓦雷利亚湖畔的\n',
            '王国军最大的军事基地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071405V在蔡斯地区的北侧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071406V#000F呼～～这样的话\n',
            '就不是简单能回来的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071407V博士要的准备，怎么办呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071408V虽然不知道你们有什么事，\n',
            '但我想他差不多要回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071409V刚刚有连络通信过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071410V#000F哎……\n',
            '下一班定期船已经来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071411V不是的，真是不听人说话的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#20A莱普尼兹号进入飞艇坪（※假定）',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010071413V#000F橙色的定期船……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071414V哎呀！\n',
            '有那样的定期船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071415V#010F不……\n',
            '那好像不是定期船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071416V无论哪里形状都不同，\n',
            '还带有作业用的扶手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071417V#000F嗯，的确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071418V这是中央工房所有的\n',
            '工房船《莱普尼兹号》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071419V虽然和定期船是相同型号，\n',
            '但追加了各种设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071420V这个主要是用来\n',
            '大型设备的支持和制品的搬运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071421V#000F哎～～！\n',
            '飞空的工房呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071422V那么维修长\n',
            '应该在那艘船上吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071423V就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071424V你们快点\n',
            '去找他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071425V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071426V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0000, 1000)
    MapSetFlags(0x00000001)

    Jump('loc_2187')

    def _loc_1C65(): pass

    label('loc_1C65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1CDB',
    )

    ChrTalk(
        0x0009,
        (
            '#1970100201V嗯？怎么了？\n',
            '手续已经办好了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100202V定期船到了之后，\n',
            '凭刚才的票就可以乘坐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2187')

    def _loc_1CDB(): pass

    label('loc_1CDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1D3B',
    )

    ChrTalk(
        0x0009,
        (
            '哟，你们也很忙呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像工房船\n',
            '有很紧急的任务要执行。\n',
            '这边也已经乱成一团了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2187')

    def _loc_1D3B(): pass

    label('loc_1D3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1DAF',
    )

    ChrTalk(
        0x0009,
        (
            '『赛希莉亚号』\n',
            '已经按预定的时间出航了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔，就趁现在难得的空闲\n',
            '集中精神看《利贝尔通讯》吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2187')

    def _loc_1DAF(): pass

    label('loc_1DAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1EFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1E56',
    )

    ChrTalk(
        0x0009,
        (
            '嗯嗯，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '说到封面……\n',
            '最近《利贝尔通讯》上面的照片\n',
            '都变得好漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，一想到这个，\n',
            '就很期待下期的封面啊。\n',
            '……偷偷告诉你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF7')

    def _loc_1E56(): pass

    label('loc_1E56')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '中央工房的骚动\n',
            '好像是起严重的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '竟然敢袭击中央工房，\n',
            '世上还有这样无法无天的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唉，这样一来\n',
            '下期《利贝尔通讯》的封面\n',
            '就会是蔡斯了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EF7(): pass

    label('loc_1EF7')

    Jump('loc_2187')

    def _loc_1EFA(): pass

    label('loc_1EFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1FBF',
    )

    ChrTalk(
        0x0009,
        (
            '那个，你们看过\n',
            '《利贝尔通讯》最新一期了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '听说卢安的市长\n',
            '是个无法无天的坏家伙，\n',
            '已经被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，空贼事件也好，\n',
            '这个叫戴尔蒙的家伙也好……\n',
            '最近这个世界真是不太平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2187')

    def _loc_1FBF(): pass

    label('loc_1FBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1FE3',
    )

    ChrTalk(
        0x0009,
        (
            '你们见到维修长了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2187')

    def _loc_1FE3(): pass

    label('loc_1FE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2114',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2066',
    )

    ChrTalk(
        0x0009,
        (
            '听说，最后好像是游击士\n',
            '解决了这次空贼事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的，明明发生了这么严重的事情，\n',
            '王国军却什么事也做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2111')

    def _loc_2066(): pass

    label('loc_2066')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '我读过利贝尔通讯了，\n',
            '前段时间柏斯的空贼骚动\n',
            '好像闹得很大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '定期船停航了，\n',
            '对我们接待员来说可真是噩梦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要把事情向客人解释清楚，\n',
            '可是一件很难的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2111(): pass

    label('loc_2111')

    Jump('loc_2187')

    def _loc_2114(): pass

    label('loc_2114')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2187',
    )

    ChrTalk(
        0x0009,
        (
            '目前，西向航线的『赛希莉亚号』\n',
            '正停靠在飞艇坪中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '去往格兰赛尔的旅客，\n',
            '请前往入口处准备登船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2187(): pass

    label('loc_2187')

    TalkEnd(0x0009)

    Return()

# id: 0x000B offset: 0x218B
@scena.Code('func_0B_218B')
def func_0B_218B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 2, 0x572)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23AC',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0008,
        (
            '#0561130001V#690F出发去雷斯顿要塞吗？',
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
            TXT(0x00, '出发\n'),
            TXT(0x01, '整理装备\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2223'),
        (0x00000001, 'loc_236B'),
        (-1, 'loc_23A9'),
    )

    def _loc_2223(): pass

    label('loc_2223')

    SetScenaFlags(ScenaFlag(0x00AC, 1, 0x561))
    OP_28(0x0043, 0x01, 0x0400)
    OP_28(0x0044, 0x04, 0x02)
    OP_28(0x0044, 0x04, 0x04)

    ChrTalk(
        0x0008,
        (
            '#0560090606V#690F好，\n',
            '那么快上去吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090607V工房船《莱普尼兹号》\n',
            '出发去雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#800F游击士的各位，\n',
            '博士的事就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '另外……\n',
            '请保护好提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22E4')
    def lambda_22E4():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22E4)

    @scena.Lambda('lambda_22F2')
    def lambda_22F2():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_22F2)

    @scena.Lambda('lambda_2300')
    def lambda_2300():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2300)

    ChrTurnDirection(0x0107, 0x000A, 400)

    ChrTalk(
        0x0107,
        (
            '#060F工房长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，都交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090612V#010F那么我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0011)

    Jump('loc_23A9')

    def _loc_236B(): pass

    label('loc_236B')

    SetScenaFlags(ScenaFlag(0x00AE, 2, 0x572))

    ChrTalk(
        0x0008,
        (
            '#0561130002V#690F我知道了。\n',
            '准备好了就告诉我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_23A9(): pass

    label('loc_23A9')

    Jump('loc_2FDC')

    def _loc_23AC(): pass

    label('loc_23AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 0, 0x560)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E57',
    )

    EventBegin(0x00)
    ChrSetPos(0x0101, -46160, -4000, 141480, 90)
    ChrSetPos(0x0106, -44780, -4000, 140260, 0)
    ChrSetPos(0x0107, -45700, -4000, 140390, 45)
    ChrSetPos(0x0102, -45780, -4000, 142250, 135)
    Fade(1000)

    @scena.Lambda('lambda_2409')
    def lambda_2409():
        OP_6C(45000, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2409)

    CameraMove(-45150, -4000, 141460, 0)

    ChrTalk(
        0x000A,
        (
            '#0550090555V#800F噢，等一下，\n',
            '你们准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F是啊，随时都能出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F《莱普尼兹号》的\n',
            '准备也完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#800F啊，我们运气真好，\n',
            '军队急着要我们发货。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090559V正好准备出发\n',
            '要去雷斯顿要塞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090560V随时都可以出发呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#000F随时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090562V那个橙色的飞行船\n',
            '可我怎么没找到呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 315, 400)
    Sleep(200)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrWalkTo(0x0102, -47490, -4000, 143600, 2000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020090563V#010F艾丝蒂尔，往下面看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_25F7')
    def lambda_25F7():
        ChrWalkTo(0x0101, -47480, -4000, 142560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25F7)

    @scena.Lambda('lambda_2612')
    def lambda_2612():
        OP_6C(314000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2612)

    CameraMove(-49360, -4000, 145960, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F啊，竟然在那里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090565V那么我们要\n',
            '下到下面去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F呵呵，姐姐，\n',
            '不用下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_26CA')
    def lambda_26CA():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_26CA')

    DispatchAsync2(0x000A, 0x0002, lambda_26CA)

    @scena.Lambda('lambda_26DB')
    def lambda_26DB():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_26DB')

    DispatchAsync2(0x0107, 0x0002, lambda_26DB)

    @scena.Lambda('lambda_26EC')
    def lambda_26EC():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_26EC')

    DispatchAsync2(0x0106, 0x0002, lambda_26EC)

    Sleep(1000)

    ChrSetDirection(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#000F为什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呀，飞行船的轨道……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F呀，你们不知道呀吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090571V这里的飞行场都是\n',
            '用超乎常识的方法造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F超，超乎常识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_27B0')
    def lambda_27B0():
        ChrWalkTo(0x0101, -47480, -4000, 142560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27B0)

    @scena.Lambda('lambda_27CB')
    def lambda_27CB():
        OP_6C(314000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27CB)

    CameraMove(-49360, -4000, 145960, 2000)
    OP_6F(0x0000, 500)
    OP_70(0x0000, 1200)

    @scena.Lambda('lambda_27FA')
    def lambda_27FA():
        OP_6C(339000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27FA)

    CameraMove(-55390, -4000, 147110, 1500)

    @scena.Lambda('lambda_281B')
    def lambda_281B():
        CameraSetDistance(2200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_281B)

    OP_67(0, 21600, -10000, 2000)

    @scena.Lambda('lambda_283C')
    def lambda_283C():
        CameraSetDistance(3500, 3100)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_283C)

    @scena.Lambda('lambda_284C')
    def lambda_284C():
        OP_6C(27000, 3100)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_284C)

    CameraMove(-36640, -4000, 148800, 3100)
    ChrSetPos(0x0101, -46240, -4000, 141000, 90)
    ChrSetPos(0x0102, -46280, -4000, 142120, 90)

    @scena.Lambda('lambda_288F')
    def lambda_288F():
        CameraSetDistance(5500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_288F)

    @scena.Lambda('lambda_289F')
    def lambda_289F():
        OP_67(0, 11000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_289F)

    OP_6C(90000, 5000)
    OP_73(0x0000)
    Sleep(1000)

    @scena.Lambda('lambda_28C8')
    def lambda_28C8():
        CameraSetDistance(3500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28C8)

    CameraMove(-45210, -4000, 142090, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F大致上我开始\n',
            '对这种事渐渐习惯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，想要弄清楚结构的话\n',
            '得花一番工夫呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#800F而且这个\n',
            '飞行场的构造也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F知道了，\n',
            '是拉赛尔博士吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '提妲。\n',
            '你的爷爷真是\n',
            '无所不能呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F呵呵……\n',
            '我也同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -36460, -4000, 144380, 270)

    ChrTalk(
        0x0008,
        (
            '#690F哟，久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-40270, -4000, 143040, 1000)

    ChrTalk(
        0x0107,
        (
            '#060F呀，维修长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A2F')
    def lambda_2A2F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2A2F')

    DispatchAsync2(0x000A, 0x0002, lambda_2A2F)

    @scena.Lambda('lambda_2A40')
    def lambda_2A40():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2A40')

    DispatchAsync2(0x0102, 0x0002, lambda_2A40)

    @scena.Lambda('lambda_2A51')
    def lambda_2A51():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2A51')

    DispatchAsync2(0x0101, 0x0002, lambda_2A51)

    @scena.Lambda('lambda_2A62')
    def lambda_2A62():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2A62')

    DispatchAsync2(0x0107, 0x0002, lambda_2A62)

    @scena.Lambda('lambda_2A73')
    def lambda_2A73():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2A73')

    DispatchAsync2(0x0106, 0x0002, lambda_2A73)

    @scena.Lambda('lambda_2A84')
    def lambda_2A84():
        CameraMove(-44110, -3800, 143890, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A84)

    @scena.Lambda('lambda_2A9C')
    def lambda_2A9C():
        ChrWalkTo(0x00FE, -46070, -4000, 145500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2A9C)

    @scena.Lambda('lambda_2AB7')
    def lambda_2AB7():
        ChrWalkTo(0x00FE, -46450, -4000, 144410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2AB7)

    Sleep(100)

    @scena.Lambda('lambda_2AD7')
    def lambda_2AD7():
        ChrWalkTo(0x00FE, -46340, -4000, 143490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_2AD7)

    Sleep(100)

    @scena.Lambda('lambda_2AF7')
    def lambda_2AF7():
        ChrWalkTo(0x00FE, -46250, -4000, 142590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_2AF7)

    ChrWalkTo(0x0008, -43100, -3800, 144030, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0560090581V#690F提妲呀，\n',
            '事情我已经听工房长说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090582V没想到老爷子\n',
            '会遇到这样的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '能帮上忙的话，\n',
            '我们维修员随时乐意效劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890001V#060F谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F不好意思，麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F不要客气，\n',
            '老爷子也是我的恩人呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090587V那么\n',
            '我们已经准备好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130012V出发去雷斯顿要塞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x000A, 0xFF)
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
            TXT(0x00, '出发\n'),
            TXT(0x01, '整理装备\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2CCE'),
        (0x00000001, 'loc_2E16'),
        (-1, 'loc_2E54'),
    )

    def _loc_2CCE(): pass

    label('loc_2CCE')

    SetScenaFlags(ScenaFlag(0x00AC, 1, 0x561))
    OP_28(0x0043, 0x01, 0x0400)
    OP_28(0x0044, 0x04, 0x02)
    OP_28(0x0044, 0x04, 0x04)

    ChrTalk(
        0x0008,
        (
            '#0560090589V#690F好，\n',
            '那么快上去吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090590V工房船《莱普尼兹号》\n',
            '出发去雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#800F游击士的各位，\n',
            '博士的事就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '另外……\n',
            '请保护好提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2D8F')
    def lambda_2D8F():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D8F)

    @scena.Lambda('lambda_2D9D')
    def lambda_2D9D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2D9D)

    @scena.Lambda('lambda_2DAB')
    def lambda_2DAB():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2DAB)

    ChrTurnDirection(0x0107, 0x000A, 400)

    ChrTalk(
        0x0107,
        (
            '#060F工房长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，都交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090595V#010F那么我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0011)

    Jump('loc_2E54')

    def _loc_2E16(): pass

    label('loc_2E16')

    SetScenaFlags(ScenaFlag(0x00AE, 2, 0x572))

    ChrTalk(
        0x0008,
        (
            '#0561130013V#690F我知道了。\n',
            '准备好了就告诉我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_2E54(): pass

    label('loc_2E54')

    Jump('loc_2FDC')

    def _loc_2E57(): pass

    label('loc_2E57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2EE3',
    )

    ChrTalk(
        0x000A,
        (
            '#0550090597V#800F这边现在\n',
            '也正由格斯塔夫维修长\n',
            '指挥进行起飞前的准备呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090598V如果你们准备好了，\n',
            '就再到这儿来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FDC')

    def _loc_2EE3(): pass

    label('loc_2EE3')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '#0550090599V#800F哦哦，是你们啊。\n',
            '已经准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090600V#010F非常抱歉，\n',
            '可能还要再费些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090601V#800F是吗，这边现在\n',
            '也正由格斯塔夫维修长\n',
            '指挥进行起飞前的准备呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090602V如果你们准备好了，\n',
            '就再到这儿来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FDC(): pass

    label('loc_2FDC')

    Return()

# id: 0x000C offset: 0x2FDD
@scena.Code('func_0C_2FDD')
def func_0C_2FDD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_308F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_303B',
    )

    ChrTalk(
        0x00FE,
        (
            '看起来定期船\n',
            '好像会晚点很长时间啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是先回家\n',
            '再做打算吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_308C')

    def _loc_303B(): pass

    label('loc_303B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '看起来定期船\n',
            '好像会晚点很长时间啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说军队要盘检，\n',
            '真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_308C(): pass

    label('loc_308C')

    Jump('loc_325E')

    def _loc_308F(): pass

    label('loc_308F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3148',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_30C1',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来\n',
            '我是不是来得太早了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3145')

    def _loc_30C1(): pass

    label('loc_30C1')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哦～早上好啊。\n',
            '你们也是要去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我呀，\n',
            '是要去飞艇公社办些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还想赶快把工作搞定，\n',
            '顺便参观诞辰庆典……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3145(): pass

    label('loc_3145')

    Jump('loc_325E')

    def _loc_3148(): pass

    label('loc_3148')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_325E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_31B0',
    )

    ChrTalk(
        0x00FE,
        (
            '飞艇的技术\n',
            '真是越来越进步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乘坐定期船\n',
            '到多杰的故乡\n',
            '也不再是遥远的梦想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_325E')

    def _loc_31B0(): pass

    label('loc_31B0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '今天早上，\n',
            '偶然遇到了来自共和国的\n',
            '导力器商人多杰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为他要在飞艇坪参观，\n',
            '我就热情地为他介绍了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看，多杰。\n',
            '那是器材的搬入口，\n',
            '造船设施就在那个地下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_325E(): pass

    label('loc_325E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x3262
@scena.Code('func_0D_3262')
def func_0D_3262():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3302',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_32C6',
    )

    ChrTalk(
        0x00FE,
        (
            '我将来也要\n',
            '把飞艇作为商品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但在那之前，\n',
            '我的城镇得有个飞艇坪才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3302')

    def _loc_32C6(): pass

    label('loc_32C6')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '现在只能感叹眼前的景象了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3302(): pass

    label('loc_3302')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x3306
@scena.Code('func_0E_3306')
def func_0E_3306():
    Call(0, 0x000A)

    Return()

# id: 0x000F offset: 0x330B
@scena.Code('func_0F_330B')
def func_0F_330B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A30',
    )

    SetScenaFlags(ScenaFlag(0x00A3, 0, 0x518))
    OP_28(0x003F, 0x01, 0x0800)

    If(
        (
            (Expr.Eval, "OP_29(0x003F, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_3331',
    )

    OP_28(0x003F, 0x01, 0x2000)

    def _loc_3331(): pass

    label('loc_3331')

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '年长的维修员',
        (
            '唔……？\n',
            '这位小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-42300, -3800, 143800, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010120381V#000F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '年长的维修员',
        (
            '#0561130003V这个《莱普尼兹号》\n',
            '无关人员是不能进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '年长的维修员',
        (
            '#0561130004V对不起，请你们离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，我们就是有关人员哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们找格斯塔夫维修长\n',
            '有些事情商量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '年长的维修员',
        (
            '呀，你们找我什么事呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F叔叔是\n',
            '维修长呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们把\n',
            '拉赛尔博士委托想要借内燃引擎设备\n',
            '的事说明了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#690F呀，\n',
            '是拉赛尔老爷子的事呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071436V是要内燃引擎设备的话，\n',
            '那来得正好呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F稍微等一下呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -42300, -3800, 143800, 0)

    ChrTalk(
        0x0101,
        (
            '#000F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    CameraMove(-43500, -3800, 143700, 1000)

    ChrTalk(
        0x0008,
        (
            '#690F嘿。\n',
            '很重，小心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0008, 0x0000, 700, 3000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们得到了内燃引擎设备设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0008, -42300, -3800, 143800, 3000, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_370F',
    )

    ChrTalk(
        0x0101,
        (
            '#000F哇哇……\n',
            '的确是沉甸甸的呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '的确是沉甸甸的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0561130005V#690F哎！想不到\n',
            '小姑娘还很能干嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130006V哈哈，我很中意你呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37BB')

    def _loc_370F(): pass

    label('loc_370F')

    ChrTalk(
        0x0102,
        (
            '#010F确实是很重……\n',
            '不过也不至于重到拿不动就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0561130007V#690F哎……\n',
            '现在的年轻人\n',
            '小姑娘还很能干嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130008V哈哈，我很中意你呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F您过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37BB(): pass

    label('loc_37BB')

    ChrTalk(
        0x0008,
        (
            '#690F不过，这也真是个\n',
            '有趣的偶然呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071452V刚从军方里还回来后\n',
            '马上就被老爷子借走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F从军方，怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560071455V#690F啊，那个货样\n',
            '被王国军借了一阵子。。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071456V好像什么研究要用到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071457V总算是\n',
            '今天还回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～。\n',
            '的确是很偶然呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呀，不……没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 1, 0x519)),
            Expr.Return,
        ),
        'loc_398C',
    )

    ChrTalk(
        0x0102,
        (
            '#0020071462V#010F需要的东西都已经拿到了，\n',
            '快点回博士那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39C4')

    def _loc_398C(): pass

    label('loc_398C')

    ChrTalk(
        0x0102,
        (
            '#0020071464V#010F剩下的就是汽油了。\n',
            '去地下工场吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39C4(): pass

    label('loc_39C4')

    ChrTalk(
        0x0101,
        (
            '#0010071465V#000F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '维修长，ＴＨＡＮＫ　ＹＯＵ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F噢。\n',
            '帮我向老爷子问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    EventEnd(0x00)

    def _loc_3A30(): pass

    label('loc_3A30')

    Return()

# id: 0x0010 offset: 0x3A31
@scena.Code('func_10_3A31')
def func_10_3A31():
    EventBegin(0x00)
    ChrSetPos(0x0108, -45670, -4000, 146000, 0)
    ChrSetPos(0x0101, -46540, -4000, 147540, 0)
    ChrSetPos(0x0102, -47220, -4000, 146840, 0)
    ChrSetPos(0x0107, -47150, -4000, 145610, 0)
    ChrTurnDirection(0x0101, 0x0108, 0)
    ChrTurnDirection(0x0102, 0x0108, 0)
    ChrTurnDirection(0x0107, 0x0108, 0)
    ChrTurnDirection(0x0108, 0x0102, 0)
    CameraMove(-45760, -4000, 146000, 0)
    OP_67(0, 9090, -10000, 0)
    CameraSetDistance(2650, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    SetScenaFlags(ScenaFlag(0x00AB, 1, 0x559))

    ChrTalk(
        0x0108,
        (
            '#0080090001V#070F……真是不好意思，\n',
            '特地要你们来送我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这是当然的啰，\n',
            '我们受了你那么多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090003V#010F金，你就这样\n',
            '乘定期船直接去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F啊，我还有\n',
            '其他事必须去办。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040005V办完事我也\n',
            '帮忙调查\n',
            '绑架事件的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0107, 400)

    ChrTalk(
        0x0108,
        (
            '#070F对不起了，小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F没这回事的啦。\n',
            '你已经帮了我很多忙了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090008V真的\n',
            '多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080090009V#070F哈哈……\n',
            '你能这么说真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '开往王都的定期船\n',
            '《赛希莉亚号》马上就要起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '请没有上船的乘客尽快上船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0108,
        (
            '#0080090012V#070F呀……\n',
            '差不多要出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D03')
    def lambda_3D03():
        CameraMove(-40990, -4000, 146200, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D03)

    @scena.Lambda('lambda_3D1B')
    def lambda_3D1B():
        CameraSetDistance(3360, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D1B)

    @scena.Lambda('lambda_3D2B')
    def lambda_3D2B():
        OP_6C(32000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3D2B)

    ChrSetFlags(0x0108, 0x0004)
    ChrWalkTo(0x0108, -46100, -4000, 145280, 3000, 0x00)
    ChrWalkTo(0x0108, -45970, -4000, 144050, 3000, 0x00)

    @scena.Lambda('lambda_3D68')
    def lambda_3D68():
        ChrWalkTo(0x00FE, -44880, -4000, 146000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D68)

    @scena.Lambda('lambda_3D83')
    def lambda_3D83():
        ChrWalkTo(0x00FE, -46120, -4000, 145560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3D83)

    @scena.Lambda('lambda_3D9E')
    def lambda_3D9E():
        ChrWalkTo(0x00FE, -46090, -4000, 144690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3D9E)

    ChrWalkTo(0x0108, -36340, -4000, 145090, 3000, 0x00)
    ChrTurnDirection(0x0108, 0x0107, 400)

    ChrTalk(
        0x0108,
        (
            '#0080090013V#070F那再见了，\n',
            '有机会还会碰面的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090015V对了，金要在\n',
            '利贝尔呆到什么时候呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F明确时间还不知道……\n',
            '我想会呆到女王生日庆典吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，那样的话\n',
            '也许会再见面的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090018V#010F到时候还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F呵呵，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x3F09
@scena.Code('func_11_3F09')
def func_11_3F09():
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0106, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x000A, 0xFF)
    ChrSetPos(0x000B, -45980, 0, 129680, 0)
    ChrClearFlags(0x000B, 0x0080)
    Fade(1000)
    CameraMove(-40270, -4000, 145060, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)

    ChrTalk(
        0x000A,
        (
            '#800F拜托你们了，游击士的各位……\n',
            '（※假定莱普尼兹号出发动画）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊，等一下～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3FEC')
    def lambda_3FEC():
        CameraMove(-45610, -3800, 142980, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3FEC)

    @scena.Lambda('lambda_4004')
    def lambda_4004():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_4004')

    DispatchAsync2(0x000A, 0x0001, lambda_4004)

    ChrWalkTo(0x000B, -46510, -4000, 144200, 5000, 0x00)

    ChrTalk(
        0x000B,
        (
            '#150F哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090645V啊，走掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#800F哎呀……\n',
            '朵洛希呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    ChrWalkTo(0x000A, -46550, -4000, 142020, 2000, 0x00)
    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#150F啊，工房长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090648V刚才的船上，\n',
            '艾丝蒂尔他们乘着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#800F是呀……\n',
            '你怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0281080004V#150F游击会的\n',
            '接待员告诉我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090651V我和编辑部连络后\n',
            '知道了不得了的事，\n',
            '我想不告诉他们不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0551250001V#800F不得了的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#150F呀……\n',
            '这个是公告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0281080005V在王都的亲卫队\n',
            '以反逆罪被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#800F什，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/E0012._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x4206
@scena.Code('func_12_4206')
def func_12_4206():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 2, 0x602)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5045',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00C0, 3, 0x603))
    OP_28(0x0054, 0x01, 0x0004)
    OP_28(0x0054, 0x01, 0x0008)
    ChrSetPos(0x000C, -46060, 0, 127820, 0)
    ChrClearFlags(0x000C, 0x0080)

    ChrTalk(
        0x000C,
        (
            '#2030100203V喵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4259')
    def lambda_4259():
        CameraMove(-46010, -1000, 131740, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4259)

    @scena.Lambda('lambda_4271')
    def lambda_4271():
        OP_67(0, 7390, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4271)

    @scena.Lambda('lambda_4289')
    def lambda_4289():
        CameraSetDistance(3700, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4289)

    @scena.Lambda('lambda_4299')
    def lambda_4299():
        OP_6C(158000, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_4299)

    Sleep(3000)

    ChrSetPos(0x0101, -45400, -4000, 140210, 0)
    ChrSetPos(0x0102, -46510, -4000, 139810, 0)

    @scena.Lambda('lambda_42D0')
    def lambda_42D0():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_42D0')

    DispatchAsync2(0x0101, 0x0003, lambda_42D0)

    @scena.Lambda('lambda_42E1')
    def lambda_42E1():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_42E1')

    DispatchAsync2(0x0102, 0x0003, lambda_42E1)

    @scena.Lambda('lambda_42F2')
    def lambda_42F2():
        ChrWalkTo(0x00FE, -45800, -4000, 138560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_42F2)

    @scena.Lambda('lambda_430D')
    def lambda_430D():
        CameraMove(-45610, -4000, 139000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_430D)

    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#000F啊，那只猫是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100205V#010F就是那个时候\n',
            '钻进集装箱里的那只猫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100206V我记得，\n',
            '好像是叫做安东尼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2030100207V喵呜～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈～真可爱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是的，都是因为你，\n',
            '害我吓了一大跳呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100210V你是不是该反省一下呢，嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2030100274V咪呜？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F都不听我说话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈，说不定\n',
            '它是在装傻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0008, -47160, 0, 129750, 0)
    ChrClearFlags(0x0008, 0x0080)

    ChrTalk(
        0x0008,
        (
            '哦，是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_44B1')
    def lambda_44B1():
        CameraMove(-46010, -4000, 137720, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_44B1)

    @scena.Lambda('lambda_44C9')
    def lambda_44C9():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_44C9')

    DispatchAsync2(0x0101, 0x0003, lambda_44C9)

    @scena.Lambda('lambda_44DA')
    def lambda_44DA():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_44DA')

    DispatchAsync2(0x0102, 0x0003, lambda_44DA)

    @scena.Lambda('lambda_44EB')
    def lambda_44EB():
        ChrWalkTo(0x00FE, -46370, -4000, 137940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_44EB)

    Sleep(1000)

    @scena.Lambda('lambda_450B')
    def lambda_450B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_450B')

    DispatchAsync2(0x0101, 0x0003, lambda_450B)

    @scena.Lambda('lambda_451C')
    def lambda_451C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_451C')

    DispatchAsync2(0x0102, 0x0003, lambda_451C)

    @scena.Lambda('lambda_452D')
    def lambda_452D():
        ChrWalkTo(0x00FE, -45750, 0, 128289, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_452D)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F啊，维修长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F工房长都告诉我了。\n',
            '能成功救出博士，干得真是漂亮啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100217V博士对我们这些技术人员来说，\n',
            '算是师傅一样的人物了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100218V我也要好好感谢你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrWalkTo(0x0101, -45280, -4000, 138840, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，这也多亏了\n',
            '维修长你们的帮忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100220V我真是被那孩子\n',
            '吓坏了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那个，\n',
            '果然是你故意把它放进去的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F啊哈哈，要想欺骗敌人，\n',
            '首先要瞒过伙伴才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，\n',
            '你们来飞艇坪有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，受博士的委托，\n',
            '现在要赶去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F要乘坐１１点的飞艇，\n',
            '看来好像来得早了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F啊啊……\n',
            '好像要稍微迟到一会儿呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130009V因为还要花点时间卸货，\n',
            '你们到街上再转一会儿\n',
            '我想也没关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, -47640, 0, 129250, 0)

    ChrTalk(
        0x0009,
        (
            '喂，你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_481E')
    def lambda_481E():
        ChrWalkTo(0x0009, -45320, -3750, 137370, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_481E)

    @scena.Lambda('lambda_4839')
    def lambda_4839():
        CameraMove(-46700, -2500, 134910, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4839)

    @scena.Lambda('lambda_4851')
    def lambda_4851():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4851')

    DispatchAsync2(0x0101, 0x0002, lambda_4851)

    @scena.Lambda('lambda_4862')
    def lambda_4862():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4862')

    DispatchAsync2(0x0102, 0x0002, lambda_4862)

    @scena.Lambda('lambda_4873')
    def lambda_4873():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4873')

    DispatchAsync2(0x0008, 0x0002, lambda_4873)

    Sleep(1500)

    @scena.Lambda('lambda_4889')
    def lambda_4889():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4889')

    DispatchAsync2(0x0101, 0x0002, lambda_4889)

    @scena.Lambda('lambda_489A')
    def lambda_489A():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_489A')

    DispatchAsync2(0x0102, 0x0002, lambda_489A)

    @scena.Lambda('lambda_48AB')
    def lambda_48AB():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_48AB')

    DispatchAsync2(0x0008, 0x0002, lambda_48AB)

    @scena.Lambda('lambda_48BC')
    def lambda_48BC():
        CameraMove(-46010, -4000, 137720, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_48BC)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0102, 0)

    ChrTalk(
        0x0008,
        (
            '#690F什么啊，这不是吉拉尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130010V什么事这么慌张？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#1970100232V正好，\n',
            '老爹也在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100233V实际上，事情变得麻烦起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F你说什么，麻烦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100235V嗯，\n',
            '从飞艇公社来的联络说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100236V定期船可能要\n',
            '晚几个小时才能到达呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F喂喂，\n',
            '到底是怎么回事啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100240V又有空贼作乱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100241V啊，说起来也差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100242V据说，有一伙打算妨碍\n',
            '女王的生日庆典的恐怖分子\n',
            '不知道在哪里潜伏着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100243V为了调查这件事，\n',
            '所有的空降庭都被军队设下了哨卡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（那，那个是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（大概是为了\n',
            '搜寻逃走的博士他们吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#1970100246V所以，开往王都的飞艇\n',
            '现在还滞留在卢安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100247V取而代之的好像是\n',
            '雷斯顿要塞的军用警备飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F原来如此，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100249V不过这样一来，\n',
            '你不是就要很忙了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#1970100250V是啊，\n',
            '不把这件事告诉旅客们不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100251V就因为这样，\n',
            '你们也得再等一段时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100252V对了……\n',
            '如果你们愿意在游击士协会等的话，\n',
            '我去帮你们联系一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100254V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, -47370, 0, 129250, 3000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0009, -18300, 8000, 121700, 180)

    ChrTalk(
        0x0008,
        (
            '#690F……真是可疑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100256V如果军队那伙人这样干的话，\n',
            '莱普尼兹号肯定也会被检查的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100257V我这就去和工房长说这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4DF9')
    def lambda_4DF9():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4DF9')

    DispatchAsync2(0x0101, 0x0002, lambda_4DF9)

    @scena.Lambda('lambda_4E0A')
    def lambda_4E0A():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4E0A')

    DispatchAsync2(0x0102, 0x0002, lambda_4E0A)

    ChrTalk(
        0x0101,
        (
            '#000F对啊，要是调查昨天那件事的话\n',
            '就不好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4E4F')
    def lambda_4E4F():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4E4F')

    DispatchAsync2(0x0008, 0x0002, lambda_4E4F)

    ChrTalk(
        0x0102,
        (
            '#010F请一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#690F哈哈，我还没有老得不中用到\n',
            '让你们这些小孩子担心的份儿上呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130011V那么告辞了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrWalkTo(0x0008, -47370, 0, 129250, 3000, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F约修亚……\n',
            '这样岂不是很危险吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F嗯……\n',
            '这样的话乘定期船就危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然要花点时间，\n',
            '还是走街道比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呜，还以为好不容易\n',
            '可以乘坐久违的飞艇了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100266V我饶不了你，理查德上校！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F算了算了。\n',
            '当成是继续修行不也很好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么我们赶快去接待那里\n',
            '把搭乘手续取消吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000C, 0x0080)
    EventEnd(0x00)

    def _loc_5045(): pass

    label('loc_5045')

    Return()

# id: 0x0013 offset: 0x5046
@scena.Code('func_13_5046')
def func_13_5046():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往王都格兰赛尔\n',
            '≡　开往卢安市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　　利贝尔飞艇公社',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x50E0
@scena.Code('func_14_50E0')
def func_14_50E0():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞艇坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '『利贝尔飞艇公社』　',
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
