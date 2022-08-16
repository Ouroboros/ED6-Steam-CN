import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0500   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0500.x'
    header.mapIndex       = 18
    header.bgm            = 16
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵安托斯',
            x                   = 1400,
            z                   = 0,
            y                   = 21400,
            direction           = 0,
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
            name                = '士兵拉科斯',
            x                   = -3300,
            z                   = 0,
            y                   = 21400,
            direction           = 0,
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
            name                = '士兵斯科特',
            x                   = 2420,
            z                   = 0,
            y                   = -19010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '士兵哈罗德',
            x                   = 16920,
            z                   = 120,
            y                   = -7750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 2420,
            z                   = 0,
            y                   = -19010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 16920,
            z                   = 120,
            y                   = -7750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '米尔西街道方向',
            x                   = -1980,
            z                   = -410,
            y                   = -40440,
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
            name                = '东柏斯街道方向',
            x                   = 440,
            z                   = -510,
            y                   = 41850,
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

# id: 0x10002 offset: 0x1B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 5680,
            triggerZ            = -260,
            triggerY            = -27360,
            triggerRange        = 1500,
            actorX              = 5680,
            actorZ              = 1700,
            actorY              = -27360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9630,
            triggerZ            = -150,
            triggerY            = 27430,
            triggerRange        = 1500,
            actorX              = -9630,
            actorZ              = 1700,
            actorY              = 27430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -13270,
            triggerZ            = -30,
            triggerY            = -5630,
            triggerRange        = 1000,
            actorX              = -12930,
            actorZ              = -800,
            actorY              = -2830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x21E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_228',
    )

    Jump('loc_248')

    def _loc_228(): pass

    label('loc_228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_248',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)

    def _loc_248(): pass

    label('loc_248')

    Return()

# id: 0x0001 offset: 0x249
@scena.Code('func_01_249')
def func_01_249():
    OP_16(0x02, 4000, -129000, -127000, 2293765)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_275',
    )

    OP_6F(0x0001, 420)
    OP_6F(0x0002, 420)

    def _loc_275(): pass

    label('loc_275')

    Return()

# id: 0x0002 offset: 0x276
@scena.Code('func_02_276')
def func_02_276():
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
        'loc_29B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3DD')

    def _loc_29B(): pass

    label('loc_29B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B4',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3DD')

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CD',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3DD')

    def _loc_2CD(): pass

    label('loc_2CD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E6',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3DD')

    def _loc_2E6(): pass

    label('loc_2E6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FF',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3DD')

    def _loc_2FF(): pass

    label('loc_2FF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_318',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3DD')

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_331',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_3DD')

    def _loc_331(): pass

    label('loc_331')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_3DD')

    def _loc_34A(): pass

    label('loc_34A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_363',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_3DD')

    def _loc_363(): pass

    label('loc_363')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37C',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_3DD')

    def _loc_37C(): pass

    label('loc_37C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_395',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_3DD')

    def _loc_395(): pass

    label('loc_395')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AE',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_3DD')

    def _loc_3AE(): pass

    label('loc_3AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C7',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_3DD')

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DD',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3DD')

    def _loc_3F2(): pass

    label('loc_3F2')

    Return()

# id: 0x0003 offset: 0x3F3
@scena.Code('func_03_3F3')
def func_03_3F3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_54C',
    )

    Sleep(3000)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 17290, -60, -24940, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, -21570, -120, -25580, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, -21690, -260, -29240, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 4090, -270, -28620, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 4180, -240, -30280, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 11280, -470, -30200, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 11290, 80, -10340, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 16950, 10, -10520, 2500, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 16920, 120, -7750, 2500, 0x00)

    Jump('func_03_3F3')

    def _loc_54C(): pass

    label('loc_54C')

    Return()

# id: 0x0004 offset: 0x54D
@scena.Code('func_04_54D')
def func_04_54D():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_678',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_611',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才阿斯顿队长\n',
            '来巡视过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这样的状况下\n',
            '他竟然还那么冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '优秀的人在这种时候\n',
            '就会体现出其非凡之处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是我心中仅次于卡西乌斯准将\n',
            '的王国军人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_675')

    def _loc_611(): pass

    label('loc_611')

    ChrTalk(
        0x00FE,
        (
            '现在这样的时候，\n',
            '阿斯顿队长却可以保持如此冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是优秀的人，\n',
            '在这种时候就体现出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_675(): pass

    label('loc_675')

    Jump('loc_9DB')

    def _loc_678(): pass

    label('loc_678')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_778',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_71D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～在大门恢复正常之前\n',
            '绝不能放松警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连导力枪也不能用了，\n',
            '真是让人绝望啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这种时候\n',
            '如果那群红衣猎兵来袭的话\n',
            '可就麻烦了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_775')

    def _loc_71D(): pass

    label('loc_71D')

    ChrTalk(
        0x00FE,
        (
            '呼～在大门恢复正常之前\n',
            '绝不能放松警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连导力枪也不能用了，\n',
            '真是让人绝望啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_775(): pass

    label('loc_775')

    Jump('loc_9DB')

    def _loc_778(): pass

    label('loc_778')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_7E8',
    )

    ChrTalk(
        0x00FE,
        (
            '解决了龙的事件后，\n',
            '将军阁下也松了一口气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市也重新开张营业了，\n',
            '和平的日子终于回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_7E8(): pass

    label('loc_7E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_8CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_847',
    )

    ChrTalk(
        0x00FE,
        (
            '龙的捕获作战\n',
            '似乎很艰难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很着急……\n',
            '但我们什么忙也帮不上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C9')

    def _loc_847(): pass

    label('loc_847')

    ChrTalk(
        0x00FE,
        (
            '龙的捕获作战\n',
            '似乎很艰难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很着急……\n',
            '但我们什么忙也帮不上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这种情况\n',
            '就只能把一切都交给飞行舰队了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_8C9(): pass

    label('loc_8C9')

    Jump('loc_9DB')

    def _loc_8CC(): pass

    label('loc_8CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_9DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_939',
    )

    ChrTalk(
        0x00FE,
        (
            '东侧的阿斯顿队长\n',
            '真是个了不起的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在洛连特警备的时候\n',
            '就发挥了优秀的指挥才能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9DB')

    def _loc_939(): pass

    label('loc_939')

    ChrTalk(
        0x00FE,
        (
            '东侧的阿斯顿队长\n',
            '真是个了不起的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在洛连特警备的时候\n',
            '就发挥了优秀的指挥才能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论发生什么情况他也不会有丝毫动摇，\n',
            '真是值得我们学习的榜样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_9DB(): pass

    label('loc_9DB')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x9DF
@scena.Code('func_05_9DF')
def func_05_9DF():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_A4E',
    )

    ChrTalk(
        0x00FE,
        (
            '队长他们在百日战争中\n',
            '都有过实战经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能在这种时候保持冷静，\n',
            '大概和那时的经验也有关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C96')

    def _loc_A4E(): pass

    label('loc_A4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_AB2',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船停航之后\n',
            '旅行者也少了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，这种非常时期，\n',
            '无论去哪里也都没多少人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C96')

    def _loc_AB2(): pass

    label('loc_AB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_B14',
    )

    ChrTalk(
        0x00FE,
        (
            '龙的骚乱\n',
            '似乎已经平息了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然最后靠飞行舰队解决的，\n',
            '但是到底做了些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C96')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_BA1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_B53',
    )

    ChrTalk(
        0x00FE,
        (
            '（发抖）……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但愿龙不要再来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B9E')

    def _loc_B53(): pass

    label('loc_B53')

    ChrTalk(
        0x00FE,
        (
            '龙、龙会从口中\n',
            '喷出火焰的吧……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希、希望它不要\n',
            '再来这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_B9E(): pass

    label('loc_B9E')

    Jump('loc_C96')

    def _loc_BA1(): pass

    label('loc_BA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_C96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_C08',
    )

    ChrTalk(
        0x00FE,
        (
            '大雾的那天，\n',
            '大门这边的工作忙死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种夸张的大雾……\n',
            '希望别再有第二次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C96')

    def _loc_C08(): pass

    label('loc_C08')

    ChrTalk(
        0x00FE,
        (
            '在大雾的那天\n',
            '大门这边的工作忙死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，负责护卫的游击士\n',
            '肯定更辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那种大雾之下，不管几个人同行\n',
            '也可能会走丢的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_C96(): pass

    label('loc_C96')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xC9A
@scena.Code('func_06_C9A')
def func_06_C9A():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_D0C',
    )

    ChrTalk(
        0x00FE,
        (
            '听说异变出现的时候\n',
            '所有飞行中的警备艇\n',
            '全部被迫降落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（发抖）……\n',
            '没去坐飞船真是万幸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105E')

    def _loc_D0C(): pass

    label('loc_D0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E19',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB6',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏了那个奇怪的装置\n',
            '把通信器似乎修好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但听了各地的报告之后\n',
            '心情却越来越暗淡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，大雾事件刚过去，\n',
            '最近怎么这么多倒霉事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_E16')

    def _loc_DB6(): pass

    label('loc_DB6')

    ChrTalk(
        0x00FE,
        (
            '但听了各地的报告之后\n',
            '心情却越来越暗淡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，这样下去，利贝尔王国\n',
            '的未来会怎样呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E16(): pass

    label('loc_E16')

    Jump('loc_105E')

    def _loc_E19(): pass

    label('loc_E19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_F28',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E9F',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的工作很轻松呢。\n',
            '每天都很悠闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在洛连特的任务\n',
            '虽然也顺利完成了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过果然还是这边\n',
            '最适合我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F25')

    def _loc_E9F(): pass

    label('loc_E9F')

    ChrTalk(
        0x00FE,
        (
            '洛连特的警备结束了，\n',
            '我也回归原本的工作岗位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那边工作的时候\n',
            '总是很紧张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是这里轻松啊。\n',
            '每天都很悠闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F25(): pass

    label('loc_F25')

    Jump('loc_105E')

    def _loc_F28(): pass

    label('loc_F28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_105E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_F8D',
    )

    ChrTalk(
        0x00FE,
        (
            '空贼团已经\n',
            '不足为惧了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在他们的首领被抓住后，\n',
            '贼团众们便已经溃不成军了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105E')

    def _loc_F8D(): pass

    label('loc_F8D')

    ChrTalk(
        0x00FE,
        (
            '柏斯的空贼团余党\n',
            '好像又现身了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说他们的手段\n',
            '相当娴熟呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，我也不用\n',
            '担心那个啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟那些家伙\n',
            '也不会造成太大影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在他们的首领被抓住后，\n',
            '现在的空贼团余党已经\n',
            '群龙无首了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_105E(): pass

    label('loc_105E')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1062
@scena.Code('func_07_1062')
def func_07_1062():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_111F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10CA',
    )

    ChrTalk(
        0x00FE,
        (
            '需要用到导力的东西\n',
            '似乎全部都不能用了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天连搬运车\n',
            '也停住不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_111C')

    def _loc_10CA(): pass

    label('loc_10CA')

    ChrTalk(
        0x00FE,
        (
            '需要用到导力的东西\n',
            '似乎全部都不能用了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可、可是我的枪也是\n',
            '导力式的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_111C(): pass

    label('loc_111C')

    Jump('loc_12F5')

    def _loc_111F(): pass

    label('loc_111F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_117C',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，你们是\n',
            '游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么可以自由通行。\n',
            '我们已经收到命令了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_11B9')

    def _loc_117C(): pass

    label('loc_117C')

    ChrTalk(
        0x00FE,
        (
            '只要是游击士\n',
            '就可以通行自由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们已经收到命令了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B9(): pass

    label('loc_11B9')

    Jump('loc_12F5')

    def _loc_11BC(): pass

    label('loc_11BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_128E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1211',
    )

    ChrTalk(
        0x00FE,
        (
            '洛连特市的警备\n',
            '一直惊险不断，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能平安无事回来\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_128B')

    def _loc_1211(): pass

    label('loc_1211')

    ChrTalk(
        0x00FE,
        (
            '洛连特市的警备\n',
            '一直惊险不断，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的视线非常差，\n',
            '几步之外的东西就看不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能平安无事回来\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_128B(): pass

    label('loc_128B')

    Jump('loc_12F5')

    def _loc_128E(): pass

    label('loc_128E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_12F5',
    )

    ChrTalk(
        0x00FE,
        (
            '不知为什么，\n',
            '这里的警备体制还是没有解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无所谓啦，反正对我来说\n',
            '一直都是相同的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12F5(): pass

    label('loc_12F5')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x12F9
@scena.Code('func_08_12F9')
def func_08_12F9():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_1377',
    )

    ChrTalk(
        0x00FE,
        (
            '我们是从哈肯大门那边调来的\n',
            '阿斯顿部队的补充部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '暂时要负责守卫\n',
            '这个关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这段时间内请多多指教了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1377(): pass

    label('loc_1377')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x137B
@scena.Code('func_09_137B')
def func_09_137B():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_13DD',
    )

    ChrTalk(
        0x00FE,
        (
            '我们补充部队的几个伙伴\n',
            '到洛连特去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～其实我也想到洛连特那里\n',
            '负责警备啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13DD(): pass

    label('loc_13DD')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x13E1
@scena.Code('func_0A_13E1')
def func_0A_13E1():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1419')
    def lambda_1419():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1419)

    @scena.Lambda('lambda_1429')
    def lambda_1429():
        OP_6C(225000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_1429)

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
        'loc_157A',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x101, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x0E, 0x00000002, 0xFFFFCC2A, 0xFFFFFFE2, 0xFFFFEA02, 0x00000168, 0xFFFFCD7E, 0xFFFFFCE0, 0xFFFFF4F2)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushReg, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1574',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_156E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_156B',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0004)
    Sleep(400)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在威尔特桥发现钓鱼场的事情\n',
            '已经记录在游击士手册上记录了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_156B(): pass

    label('loc_156B')

    Jump('loc_1574')

    def _loc_156E(): pass

    label('loc_156E')

    OP_28(0x0073, 0x01, 0x0400)

    def _loc_1574(): pass

    label('loc_1574')

    OP_0D()
    EventEnd(0x01)

    Jump('loc_1589')

    def _loc_157A(): pass

    label('loc_157A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1589',
    )

    EventEnd(0x01)

    def _loc_1589(): pass

    label('loc_1589')

    Return()

# id: 0x000B offset: 0x158A
@scena.Code('func_0B_158A')
def func_0B_158A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　洛连特市　１７２塞尔矩\n',
            '西　柏斯市　　４２０塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x15F2
@scena.Code('func_0C_15F2')
def func_0C_15F2():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　柏斯市　　４２０塞尔矩\n',
            '东　洛连特市　１７２塞尔矩',
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
