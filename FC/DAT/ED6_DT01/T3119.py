import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3119_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3119   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3119.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3119._SN', 'ED6_DT01/T3119_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT06/CH20104._CH', 'ED6_DT06/CH20104P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特莱斯主任',
            x                   = 600,
            z                   = 0,
            y                   = 10300,
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
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 111,
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
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 336,
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
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '提妲',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '威尔姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -118000,
            y           = -1000,
            z           = 23400,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -106990,
            y           = 0,
            z           = -550,
            range       = 1000,
            dword_10    = 0x000008CA,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10004 offset: 0x222
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -540,
            triggerZ            = 0,
            triggerY            = 6300,
            triggerRange        = 800,
            actorX              = -540,
            actorZ              = 900,
            actorY              = 6300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -117890,
            triggerZ            = 0,
            triggerY            = 24080,
            triggerRange        = 800,
            actorX              = -117890,
            actorZ              = 1000,
            actorY              = 24080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26A
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_27E'),
        (0x00000068, 'loc_291'),
        (0x00000064, 'loc_2A4'),
        (-1, 'loc_2AC'),
    )

    def _loc_27E(): pass

    label('loc_27E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 4, 0x514)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28E',
    )

    Event(0, func_07_153E)

    def _loc_28E(): pass

    label('loc_28E')

    Jump('loc_2AC')

    def _loc_291(): pass

    label('loc_291')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A1',
    )

    Event(0, func_09_3994)

    def _loc_2A1(): pass

    label('loc_2A1')

    Jump('loc_2AC')

    def _loc_2A4(): pass

    label('loc_2A4')

    PlaySE(14, 0x00, 0x64)

    Jump('loc_2AC')

    def _loc_2AC(): pass

    label('loc_2AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2CC',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 4680, 1000, 10760, 79)

    Jump('loc_488')

    def _loc_2CC(): pass

    label('loc_2CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2E7',
    )

    ChrSetPos(0x0008, -670, 0, 5580, 351)

    Jump('loc_488')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_318',
    )

    ChrSetPos(0x0008, -670, 0, 5580, 351)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 680, 0, 6900, 268)

    Jump('loc_488')

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_349',
    )

    ChrSetPos(0x0008, -670, 0, 5580, 351)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 680, 0, 6900, 268)

    Jump('loc_488')

    def _loc_349(): pass

    label('loc_349')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_37A',
    )

    ChrSetPos(0x0008, -670, 0, 5580, 351)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 680, 0, 6900, 268)

    Jump('loc_488')

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_389',
    )

    ChrSetFlags(0x0008, 0x0080)

    Jump('loc_488')

    def _loc_389(): pass

    label('loc_389')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_393',
    )

    Jump('loc_488')

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Return,
        ),
        'loc_3B3',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 4680, 1000, 10760, 79)

    Jump('loc_488')

    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 4, 0x514)),
            Expr.Return,
        ),
        'loc_3E4',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 4680, 1000, 10760, 79)
    ChrSetPos(0x0008, 470, 0, 6630, 225)

    Jump('loc_488')

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_404',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 4680, 1000, 10760, 79)

    Jump('loc_488')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_424',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 4680, 1000, 10760, 79)

    Jump('loc_488')

    def _loc_424(): pass

    label('loc_424')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_444',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 4680, 1000, 10760, 79)

    Jump('loc_488')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_488',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 700, 0, 9380, 353)
    ChrSetFlags(0x000C, 0x0010)
    ChrTurnDirection(0x0008, 0x000C, 0)
    ChrSetFlags(0x0008, 0x0010)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 4680, 1000, 10760, 79)

    def _loc_488(): pass

    label('loc_488')

    Return()

# id: 0x0001 offset: 0x489
@scena.Code('func_01_489')
def func_01_489():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A1',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4CE')

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4CE')

    def _loc_4B9(): pass

    label('loc_4B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4CE(): pass

    label('loc_4CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Return,
        ),
        'loc_4EE',
    )

    OP_71(0x0004, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)

    def _loc_4EE(): pass

    label('loc_4EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_57F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_50D',
    )

    OP_72(0x0007, 0x0010)
    OP_6F(0x0007, 30)

    def _loc_50D(): pass

    label('loc_50D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_577',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 7, 0x547)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 0, 0x548)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 1, 0x549)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 2, 0x54A)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 3, 0x54B)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_577',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_577(): pass

    label('loc_577')

    OP_72(0x0008, 0x0010)

    Jump('loc_583')

    def _loc_57F(): pass

    label('loc_57F')

    OP_64(0x01, 0x0001)
    def _loc_583(): pass

    label('loc_583')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_595',
    )

    OP_10(0x07, 0x01)
    OP_10(0x01, 0x00)

    def _loc_595(): pass

    label('loc_595')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 4, 0x514)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A1',
    )

    OP_64(0x00, 0x0001)

    def _loc_5A1(): pass

    label('loc_5A1')

    Return()

# id: 0x0002 offset: 0x5A2
@scena.Code('func_02_5A2')
def func_02_5A2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5B7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_5A2')

    def _loc_5B7(): pass

    label('loc_5B7')

    Return()

# id: 0x0003 offset: 0x5B8
@scena.Code('func_03_5B8')
def func_03_5B8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_710',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_640',
    )

    ChrTalk(
        0x00FE,
        (
            '说真的，我很想开一个晚会\n',
            '庆祝博士能够平安无事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过说不定军队的耳目还在附近。\n',
            '现在还是暂且忍耐一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70D')

    def _loc_640(): pass

    label('loc_640')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '哦，\n',
            '这不是我们的正义使者吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～我从工房船里面\n',
            '偷偷看了那么一眼，\n',
            '真的是紧张坏了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当士兵们聚在\n',
            '集装箱周围的时候，\n',
            '我以为你们死定了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不由自主就和\n',
            '在我身边的雷曼抱成一团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70D(): pass

    label('loc_70D')

    Jump('loc_AD4')

    def _loc_710(): pass

    label('loc_710')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_7D3',
    )

    ChrTalk(
        0x00FE,
        (
            '从导力停止现象\n',
            '联想到了一种新的维护方法……\n',
            '有试一试的价值呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……就算这么说，\n',
            '当然也得等到『卡佩尔』\n',
            '拿回来之后才能进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士协会也很努力，\n',
            '我要对他们充满信心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD4')

    def _loc_7D3(): pass

    label('loc_7D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_872',
    )

    ChrTalk(
        0x00FE,
        (
            '就算没有演算导力器，\n',
            '还可以做一些其他的工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好趁这个机会，\n',
            '将库存整理一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果『卡佩尔』在的话，\n',
            '工作效率就比现在要高多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD4')

    def _loc_872(): pass

    label('loc_872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_90F',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到『卡佩尔』会被抢走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，抢走它\n',
            '到底要做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算在中央工房里，\n',
            '能完全理解『卡佩尔』的人\n',
            '也只有开发它的拉赛尔博士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD4')

    def _loc_90F(): pass

    label('loc_90F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_964',
    )

    ChrTalk(
        0x00FE,
        (
            '哦……\n',
            '演算导力器的情况\n',
            '怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从仪表来看\n',
            '工作应该是正常的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD4')

    def _loc_964(): pass

    label('loc_964')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_A67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_9E4',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上回来一看，\n',
            '演算导力器的状况\n',
            '竟然神奇地恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这到底是怎么回事？\n',
            '难道是导力停止的原因？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A64')

    def _loc_9E4(): pass

    label('loc_9E4')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '今天早上回来一看，\n',
            '演算导力器的状况\n',
            '竟然神奇地恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明不管怎么修\n',
            '都没办法弄好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A64(): pass

    label('loc_A64')

    Jump('loc_AD4')

    def _loc_A67(): pass

    label('loc_A67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_AD4',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，真是麻烦呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里刚刚修好，\n',
            '那里又出了不同的毛病。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去\n',
            '简直就是没完没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD4(): pass

    label('loc_AD4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xAD8
@scena.Code('func_04_AD8')
def func_04_AD8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_C39',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B50',
    )

    ChrTalk(
        0x00FE,
        (
            '按照工房长的指示，\n',
            '我们把『卡佩尔』藏了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不知道军队的家伙们\n',
            '什么时候会过来检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C36')

    def _loc_B50(): pass

    label('loc_B50')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '啊，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢啊。\n',
            '把『卡佩尔』夺了回来，\n',
            '干得真是漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博士也平安无事，\n',
            '心情很久没有这么愉快过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，不过按照工房长的指示，\n',
            '我们把『卡佩尔』藏了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不知道军队的家伙们\n',
            '什么时候会过来检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C36(): pass

    label('loc_C36')

    Jump('loc_1487')

    def _loc_C39(): pass

    label('loc_C39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_D02',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听工房长说了。\n',
            '虽然我不知道详细的情况，\n',
            '不过终于要进行营救作战了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我翘首企盼着你们\n',
            '能够将博士和『卡佩尔』带回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请加油。\n',
            '愿女神爱德丝保佑你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1487')

    def _loc_D02(): pass

    label('loc_D02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_D3B',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博士能够平安无事就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1487')

    def _loc_D3B(): pass

    label('loc_D3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_DF0',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '总之就算没有『卡佩尔』，\n',
            '我们也能先尽量\n',
            '做一些其他工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为成熟的男人，\n',
            '任何时候都不能消沉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士协会也在努力，\n',
            '我们能做的只有相信他们，默默等待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1487')

    def _loc_DF0(): pass

    label('loc_DF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_E64',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '怎么会这样……\n',
            '『卡佩尔』竟然被盗走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是对不起拉赛尔博士啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1487')

    def _loc_E64(): pass

    label('loc_E64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_F44',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F10',
    )

    MapSetFlags(0x00000080)
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
        0,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '询问烟草的事情\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EDC',
    )

    Call(1, 0x0002)

    Return()

    def _loc_EDC(): pass

    label('loc_EDC')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哟，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们要找的东西找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F41')

    def _loc_F10(): pass

    label('loc_F10')

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哟，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们要找的东西找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_F41(): pass

    label('loc_F41')

    Jump('loc_1487')

    def _loc_F44(): pass

    label('loc_F44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1067',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F97',
    )

    ChrTalk(
        0x00FE,
        (
            '你们可以亲自去触摸面板试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很快就能够掌握操作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1064')

    def _loc_F97(): pass

    label('loc_F97')

    ChrTalk(
        0x00FE,
        (
            '维修长是飞艇坪的负责人，\n',
            '我想你们一到那里就会找到他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '汽油的储存地点\n',
            '导力器生产工场\n',
            '就在中央工房的地下区域。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们找那里的员工\n',
            '就可以要到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '如果还有什么问题的话就再来询问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1064(): pass

    label('loc_1064')

    Jump('loc_1487')

    def _loc_1067(): pass

    label('loc_1067')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_11F6',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_111C',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上回来一看，\n',
            '演算导力器\n',
            '已经没有什么问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果进行顺利的话，\n',
            '这个机器今天\n',
            '应该能照常使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然不清楚原因，\n',
            '不过现在感觉十分开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11F3')

    def _loc_111C(): pass

    label('loc_111C')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哦～早上好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '我还真是吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天早上回来一看，\n',
            '演算导力器\n',
            '已经没有什么问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果进行顺利的话，\n',
            '这个机器今天\n',
            '应该能照常使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然不清楚原因，\n',
            '不过现在感觉十分开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11F3(): pass

    label('loc_11F3')

    Jump('loc_1487')

    def _loc_11F6(): pass

    label('loc_11F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_13D8',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1259',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '再检查一遍\n',
            '库存的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '这个工作真是花费时间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13D5')

    def _loc_1259(): pass

    label('loc_1259')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才被叫走\n',
            '真的不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊，特莱斯主任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '演算导力器的情况\n',
            '现在如何了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还需要更多时间\n',
            '来找出故障所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我估计暂时\n',
            '是没有办法弄好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F唔～是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#561F对不起，\n',
            '我也帮不上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系，别放在心上。\n',
            '反正最近也用不到它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有别的事，\n',
            '还要再拜托你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，好的，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13D5(): pass

    label('loc_13D5')

    Jump('loc_1487')

    def _loc_13D8(): pass

    label('loc_13D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1487',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这里的演算导力器\n',
            '出了点问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们试着做了许多调整，\n',
            '可是导力器好像还是\n',
            '没有丝毫的改善迹象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '问题发生在模式切换的时候，\n',
            '你觉得会是\n',
            '哪里出了毛病呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1487(): pass

    label('loc_1487')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x148B
@scena.Code('func_05_148B')
def func_05_148B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1524',
    )

    ChrTalk(
        0x00FE,
        (
            '#0070091644V#560F嗯…是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091645V既然模式切换会发生问题，\n',
            '那可能是储存器方面出了毛病。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091646V那些地方\n',
            '都已经检查过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1524(): pass

    label('loc_1524')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1528
@scena.Code('func_06_1528')
def func_06_1528():
    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 2, 0x542))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    SetScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Return()

# id: 0x0007 offset: 0x153E
@scena.Code('func_07_153E')
def func_07_153E():
    EventBegin(0x00)
    CameraMove(1330, 0, 10350, 0)
    ChrSetPos(0x0101, -480, 0, 1250, 0)
    ChrSetPos(0x0102, -1790, 0, 1330, 0)
    FadeIn(1000, 0)
    CameraMove(150, 0, 4860, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010071303V#509F呜哇～这个房间好像很厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071304V#010F看来这里\n',
            '应该就是演算室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1960071305V#4P啊，你们…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 950, 0, 6910, 3000, 0x00)
    ChrWalkTo(0x0008, -790, 0, 4040, 3000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1960071306V#5P没见过你们啊，\n',
            '到演算室来有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071307V#5P我是这里的\n',
            '技术主任特莱斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071308V#010F初次见面，我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071309V#501F其实我们是受拉赛尔博士委托\n',
            '来调查东西的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x00B4, 0x000001F4, 0x00000BB8, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1960071310V#5P拉、拉赛尔博士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071311V#5P不、不、不会\n',
            '又是什么麻烦事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071312V#007F又、又是……\n',
            '博士真的一点信用都没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071313V#5P不不，这个嘛……\n',
            '我当然知道博士是个天才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071314V#5P这台导力演算器『卡佩尔』\n',
            '也是博士开发的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071315V#5P但是呢，只要和他扯上关系，\n',
            '麻烦总是络绎不绝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071316V#5P不过还好有提妲在他身边，\n',
            '不然惹出的麻烦会更多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071317V#506F啊哈哈……\n',
            '我能理解你的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071318V#006F不过这次\n',
            '应该不会给你们添麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071319V#010F我们只是想查一下\n',
            '中央工房保管备用品的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071320V#5P哦，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071321V#5P保管备用品的地方……\n',
            '这个应该很容易就能查到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071322V#5P机会难得，\n',
            '我就教你们搜索的方法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 400)

    @scena.Lambda('lambda_1A86')
    def lambda_1A86():
        CameraMove(340, 0, 6200, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1A86)

    @scena.Lambda('lambda_1A9E')
    def lambda_1A9E():
        ChrWalkTo(0x00FE, 470, 0, 6630, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1A9E)

    Sleep(500)

    @scena.Lambda('lambda_1ABE')
    def lambda_1ABE():
        ChrWalkTo(0x00FE, -50, 0, 4990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1ABE)

    Sleep(200)

    @scena.Lambda('lambda_1ADE')
    def lambda_1ADE():
        ChrWalkTo(0x00FE, -1280, 0, 4930, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1ADE)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 270, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 45, 400)

    ChrTalk(
        0x0008,
        (
            '#1960071323V这个圆筒型的装置\n',
            '就是导力演算器『卡佩尔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071324V在如今的时代里，\n',
            '飞艇的航空管理控制中\n',
            '会用到各种各样的导力演算器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071325V但这个卡佩尔\n',
            '具备了当今世界上\n',
            '最快的信息处理速度和高度泛用性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071326V从构造物质的强度计算到信息的搜索，\n',
            '没有什么能难倒它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071327V那么，信息搜索的方法是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 225, 200)

    ChrTalk(
        0x0008,
        (
            '#1960071328V首先使用正面的这个控制板，\n',
            '转换到信息搜索模式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071329V这样一来，\n',
            '导力信号会通过配线访问记忆导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071330V记忆导力器里装载有\n',
            '大量管理和记载信息的\n',
            '被称为光感应的特殊结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071331V如果有需要的信息，\n',
            '就能简单地将其引导出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071332V——刚才说的这些都明白了吧？',
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

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
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
            TXT(0x00, '『完全明白！』\n'),
            TXT(0x01, '『莫名其妙！』\n'),
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
        (0x00000000, 'loc_1E1A'),
        (0x00000001, 'loc_1F21'),
        (-1, 'loc_1F96'),
    )

    def _loc_1E1A(): pass

    label('loc_1E1A')

    ChrTalk(
        0x0101,
        (
            '#0010071333V#502F嗯，完全明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071334V#014F好厉害啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071335V这么新的技术，\n',
            '连我都有点不太不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010071336V#007F骗你的啦，真不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071337V#509F说实话，\n',
            '我完全不知道刚才在说什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F96')

    def _loc_1F21(): pass

    label('loc_1F21')

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010071338V#509F简直是莫名其妙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071339V从头到尾，\n',
            '完全不明白是什么意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F96')

    def _loc_1F96(): pass

    label('loc_1F96')

    ChrTalk(
        0x0008,
        (
            '#1960071340V算了，详细原理还是跳过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071341V模式已经转换好了，\n',
            '接下来就实际操作一下控制板吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071342V你们很快就会知道怎么用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_65(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x00A2, 4, 0x514))
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x0008 offset: 0x203F
@scena.Code('func_08_203F')
def func_08_203F():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-200, 0, 7100, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Return,
        ),
        'loc_21D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 3, 0x533)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2191',
    )

    SetScenaFlags(ScenaFlag(0x00A6, 3, 0x533))
    OP_28(0x0041, 0x01, 0x0008)

    ChrTalk(
        0x0107,
        (
            '#0070080913V#065F啊啊！？\n',
            '『卡佩尔』被……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080914V#057F『卡佩尔』？\n',
            '那是什么东西啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080915V#012F是拉赛尔博士开发的\n',
            '导力演算器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080916V看来中枢部分\n',
            '被别人强行拔走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080917V#004F就是那些家伙拿走的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080918V#015F嗯，可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D1')

    def _loc_2191(): pass

    label('loc_2191')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力演算器\n',
            '『卡佩尔』的中枢被拿走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_21D1(): pass

    label('loc_21D1')

    EventEnd(0x01)

    Return()

    def _loc_21D4(): pass

    label('loc_21D4')

    FadeOut(300, 0, 100)
    PlaySE(157, 0x00, 0x64)
    TalkSetChrName('CAPEL')
    SetMessageWindowPos(250, 78, 36, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1SThe Orbal Calculater\n',
            'CAPEL SYSTEM Ver.7.0\n',
            'Copyright(C) Z.C.F. 1197-1202\n',
            'MODE:Information Retrieval\n',
            '#200W　#20W\n',
            'MEMORY_CHECK#100W..........#20WOK!\n',
            '#200W　#20W\n',
            '正在访问数据库。\n',
            '请选择搜索项目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_22C5(): pass

    label('loc_22C5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3563',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        55,
        80,
        1,
        (
            TXT(0x00, '【中央工房关联】　　\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2313'),
        (-1, 'loc_3553'),
    )

    def _loc_2313(): pass

    label('loc_2313')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3543',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        55,
        153,
        1,
        (
            TXT(0x00, '【设立·沿革】\n'),
            TXT(0x01, '【技术一览】\n'),
            TXT(0x02, '【关联信息搜索】　　\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_237C'),
        (0x00000001, 'loc_29D5'),
        (0x00000002, 'loc_321E'),
        (-1, 'loc_3533'),
    )

    def _loc_237C(): pass

    label('loc_237C')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１５４】（Ｓ…七耀历）\n',
            'Ｃ·爱普斯泰恩博士于列曼自治州去世。\n',
            '【Ｓ１１５５】\n',
            'Ａ·拉赛尔博士回到利贝尔王国。\n',
            '回国后提倡普及导力器技术，\n',
            '但是没得到世人的认可和支持。\n',
            '【Ｓ１１５７】\n',
            '拉赛尔博士带领蔡斯的钟表工匠普及导力器。\n',
            '同年，『蔡斯技术工房』（即之后的中央工房）设立。\n',
            '【Ｓ１１６０】\n',
            '埃德佳Ⅲ世在视察蔡斯技术工房后提供巨额资金建设工\n',
            '房。拉赛尔博士出任首任工房长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１６２】\n',
            '埃德佳Ⅲ世去世。艾莉茜雅Ⅱ世即位。\n',
            '【Ｓ１１６４】\n',
            '『伦格兰德大桥』落成。\n',
            '【Ｓ１１６８】\n',
            '首部导力飞艇『加拉托拉巴号』诞生。\n',
            '（经过３９次飞行实验失败后的产物）\n',
            '【Ｓ１１７３】\n',
            '蔡斯技术工房开始对共和国乌尔努社和帝国莱恩福尔特\n',
            '社输出导力器技术。工房改名为『中央工房』。\n',
            '【Ｓ１１７５】\n',
            '飞艇公社设立。定期船『林德号』开始服役。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１７７】\n',
            '定期船『赛希莉亚号』开始服役。\n',
            '【Ｓ１１７８】\n',
            '移动工房船『莱普尼兹号』开始服役。\n',
            '【Ｓ１１８０】\n',
            '中央工房搬迁（即现在的建筑物）。\n',
            '开掘卡鲁迪亚平原丘陵的一角，地下工房建成。\n',
            '【Ｓ１１８２】\n',
            '拉赛尔工房长退休。\n',
            '玛多克技术主任出任第二任工房长。\n',
            '【Ｓ１１８５】\n',
            '自然科学和医学研究部门设立。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１８７】\n',
            '客船『埃迪鲁那号』在卡尔瓦德领海沉没。\n',
            '尤迪斯王太子夫妇去世。\n',
            '【Ｓ１１９０】\n',
            '与爱普斯泰恩财团合作，\n',
            '发表了『导力网络』的构想。\n',
            '【Ｓ１１９２】\n',
            '『百日战役』爆发。\n',
            '中央工房被埃雷波尼亚帝国接管。\n',
            '拉赛尔博士在雷斯顿要塞开发出警备飞艇，\n',
            '并将其用于反攻作战中，取得了显赫的战功，\n',
            '从此警备飞艇作为王国军的主力兵器而被使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S【Ｓ１１９３】\n',
            '利贝尔王国和埃雷波尼亚帝国缔结和平条约。\n',
            '战后，王国再次向帝国输出导力器。\n',
            '【Ｓ１１９７】\n',
            '导力演算器『卡佩尔』Ver.1完成。\n',
            '【Ｓ１１９９】\n',
            '高速巡洋舰『埃尔赛尤号』开发工程开始。\n',
            '【Ｓ１２０２】\n',
            '高速巡洋舰『埃尔赛尤号』竣工，进入试飞阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3540')

    def _loc_29D5(): pass

    label('loc_29D5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_320E',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        2,
        55,
        259,
        1,
        (
            TXT(0x00, '【导力器】\n'),
            TXT(0x01, '【结晶回路】\n'),
            TXT(0x02, '【七耀石】\n'),
            TXT(0x03, '【飞行船】\n'),
            TXT(0x04, '【导力兵器】\n'),
            TXT(0x05, '【战术导力器】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2A63'),
        (0x00000001, 'loc_2BEC'),
        (0x00000002, 'loc_2CB6'),
        (0x00000003, 'loc_2DCE'),
        (0x00000004, 'loc_2F03'),
        (0x00000005, 'loc_3078'),
        (-1, 'loc_31FE'),
    )

    def _loc_2A63(): pass

    label('loc_2A63')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力器（Orbment）\n',
            '在半世纪前由Ｃ·爱普斯泰恩博士所发明，是能从七耀\n',
            '石中提取导力，从而引发各种各样现象的机械装置的总\n',
            '称。导力器内部的构造和齿轮的运动，使加工七耀石而\n',
            '成的结晶回路相互干涉，可以引发丰富多彩的现象。导\n',
            '力器的实用性，除了能产生丰富现象以外，还在于拥有\n',
            '『经过一段时间内部的导力可以自然恢复』这种特异的\n',
            '便利性。另外，经济效率也要远远地领先于各种外燃、\n',
            '内燃引擎设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_320B')

    def _loc_2BEC(): pass

    label('loc_2BEC')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：结晶回路（Quartz）\n',
            '将七耀石的碎片（耀晶片，Sepith）精制、加工而成的\n',
            '具有结晶构造的回路。作为能量源的同时，本身还是引\n',
            '起各种各样现象的装置。但结晶回路必须安装在导力器\n',
            '内才可以发挥作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_320B')

    def _loc_2CB6(): pass

    label('loc_2CB6')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：七耀石（Septium）\n',
            '是在大陆全土分布的７种贵重矿石的总称。因被人们称\n',
            '为『古代的宝石』、『神秘的象征』而变得珍重。近代\n',
            '一种将体积过小不能成为宝石的碎片（耀晶片）精制加\n',
            '工制作出结晶回路的技术被发明出来，因此导致七耀石\n',
            '资源的重要性在大陆诸国之间一夜之间变得十分重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_320B')

    def _loc_2DCE(): pass

    label('loc_2DCE')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力飞艇\n',
            '导力飞艇可以称得上是导力技术精华凝聚而成的结晶。\n',
            '集合了用于重力制御的大型飞翔装置和供给大量能量的\n',
            '导力机关两大技术，使得如此大的飞艇在空中飞行成为\n',
            '可能。\n',
            '为了实现高效率的导力传送和十分复杂的船体控制，最\n',
            '新的飞艇大多搭载了高性能的导力演算器。２０亚矩以\n',
            '上的大型飞艇又被称为『飞船』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_320B')

    def _loc_2F03(): pass

    label('loc_2F03')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：导力兵器\n',
            '即以导力枪、导力炮作为代表，使用导力技术的兵器体\n',
            '系。现在已成为大多数国家军队的主力装备。\n',
            '导力枪枪管内具有能将能量按照螺旋线聚集并高速射出\n',
            '豆粒大小的金属子弹的构造，与发射火药的枪相比，填\n',
            '弹量大幅增加，而且还能够调节枪的威力。\n',
            '导力炮则可以发射封装了能量的炮弹（导力弹）并产生\n',
            '爆炸，与发射火药的炮相比，其后坐力小，而且也可以\n',
            '自由调节威力大小。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_320B')

    def _loc_3078(): pass

    label('loc_3078')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：战术导力器\n',
            '可以发动导力魔法的导力器。大小和怀表差不多，内部\n',
            '构造则相当精致优雅。\n',
            '战术导力器具有安装结晶回路后能够提高持有者能力的\n',
            '设计，使内部结晶回路与持有者达到同步，引发出『共\n',
            '鸣现象』，以代替传统释放魔法所需的复杂的齿轮和驱\n',
            '动装置，使持有者能够发动各种导力魔法。\n',
            '而且，根据复数结晶回路属性和势能的组合不同，持有\n',
            '者能够使用的导力魔法也会发生变化，具有相当的灵活\n',
            '性。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_320B')

    def _loc_31FE(): pass

    label('loc_31FE')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_320B')

    def _loc_320B(): pass

    label('loc_320B')

    Jump('loc_29D5')

    def _loc_320E(): pass

    label('loc_320E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0002)

    Jump('loc_3540')

    def _loc_321E(): pass

    label('loc_321E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3523',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        2,
        55,
        255,
        1,
        (
            TXT(0x00, '【内燃引擎设备】\n'),
            TXT(0x01, '【汽油】\n'),
            TXT(0x02, '【运输车】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_327B'),
        (0x00000001, 'loc_335D'),
        (0x00000002, 'loc_3425'),
        (-1, 'loc_3513'),
    )

    def _loc_327B(): pass

    label('loc_327B')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：内燃引擎设备\n',
            '在机关装置内燃烧燃料以获得能量的动力源。与导力机\n',
            '关相比经济效率低下，而且还会产生噪音、废气等各种\n',
            '问题，因此已经停止开发和生产。\n',
            '\n',
            '『内燃引擎设备』\n',
            '库存量：１台\n',
            '管理责任人：格斯塔夫维修长',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003F, 0x01, 0x0200)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_3520')

    def _loc_335D(): pass

    label('loc_335D')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：汽油\n',
            '将天然产生的液态碳氢化合物（石油）分馏、精制而成\n',
            '的液体。常作为内燃引擎设备的燃料以及工业生产的溶\n',
            '剂使用。\n',
            '\n',
            '『共和国产汽油』\n',
            '库存：中型桶×２０\n',
            '保管地点：导力器生产工场',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003F, 0x01, 0x0400)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_3520')

    def _loc_3425(): pass

    label('loc_3425')

    OP_28(0x0029, 0x01, 0x8000)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S项目：运输车\n',
            '使用导力机关驱动的各种车辆的总称。因为乘坐的舒适\n',
            '度较差，速度也很慢，所以基本不用于客运方面，而主\n',
            '要用来进行中短距离的货物运输。\n',
            '\n',
            '『运输车用驱动导力器』\n',
            '库存量：不明\n',
            '保管地点：地下工场搬入口',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0028, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_3510',
    )

    OP_28(0x0029, 0x01, 0x0008)

    def _loc_3510(): pass

    label('loc_3510')

    Jump('loc_3520')

    def _loc_3513(): pass

    label('loc_3513')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3520')

    def _loc_3520(): pass

    label('loc_3520')

    Jump('loc_321E')

    def _loc_3523(): pass

    label('loc_3523')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0002)

    Jump('loc_3540')

    def _loc_3533(): pass

    label('loc_3533')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3540')

    def _loc_3540(): pass

    label('loc_3540')

    Jump('loc_2313')

    def _loc_3543(): pass

    label('loc_3543')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0001)

    Jump('loc_3560')

    def _loc_3553(): pass

    label('loc_3553')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3560')

    def _loc_3560(): pass

    label('loc_3560')

    Jump('loc_22C5')

    def _loc_3563(): pass

    label('loc_3563')

    SetMessageWindowPos(72, 320, 56, 3)

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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3991',
    )

    SetScenaFlags(ScenaFlag(0x00A2, 6, 0x516))
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1960071343V看起来，\n',
            '你们找到要找的东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071344V#004F哇～\n',
            '好像魔法箱一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071345V#014F导力演算器……\n',
            '真是超出想象的惊人技术啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071346V#5P提出这个基本概念的人\n',
            '好像是拉赛尔博士的师傅，\n',
            '也就是导力器的发明者爱普斯泰恩博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071347V#5P不过，能把它发展到这种地步，\n',
            '拉赛尔博士也确实是天才啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071348V#5P唉，话虽如此，\n',
            '要是为人能再沉稳点就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071349V#019F哈哈……\n',
            '人无完人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071350V#501F对了，说到管理内燃引擎的\n',
            '格斯塔夫维修长这个人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071351V他在哪里啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071352V#5P维修长是飞艇坪的责任人，\n',
            '你们去那里应该能找到他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071353V#5P还有，关于汽油方面，\n',
            '就要到中央工房地下区域的\n',
            '导力器生产工场去找找。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071354V#5P你们找那里的员工问问\n',
            '应该就能要到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071355V#010F内燃引擎设备是找\n',
            '飞艇坪的格斯塔夫维修长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071356V而汽油就是找\n',
            '导力器生产工场的员工对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071357V#001F谢谢您！真是帮大忙了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1960071358V#5P哪里哪里。\n',
            '还有什么需要的话再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 225, 0)
    OP_4B(0x0008, 255)

    def _loc_3991(): pass

    label('loc_3991')

    EventEnd(0x01)

    Return()

# id: 0x0009 offset: 0x3994
@scena.Code('func_09_3994')
def func_09_3994():
    EventBegin(0x00)
    CameraMove(-101380, 0, -1870, 0)
    ChrSetPos(0x0101, -101860, 0, -2090, 270)
    ChrSetPos(0x0102, -101400, 0, -890, 270)
    ChrSetPos(0x0106, -101230, 0, -3040, 270)
    ChrSetPos(0x0107, -100640, 0, -1840, 270)
    ChrSetPos(0x0009, -117950, 0, -1340, 280)
    ChrSetPos(0x000A, -116160, 0, 710, 41)
    ChrSetPos(0x000B, -116560, 0, -600, 204)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0020)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetPos(0x000E, -117490, 0, 22060, 328)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    CameraMove(-103580, 0, -540, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010080891V#004F咦，为什么门会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#2620080892V#2P……久等了。\n',
            '最后的目标已经到手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#2630080893V#2P好……\n',
            '那就马上撤离吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#2630080894V#2P已经准备好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x0009, -118930, 0, 21810, 0)
    ChrSetPos(0x000A, -117340, 0, 21040, 328)
    ChrSetPos(0x000B, -117550, 0, 22790, 0)

    ChrTalk(
        0x0102,
        (
            '#0020080895V#016F刚才的声音是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(82)

    ChrTalk(
        0x0106,
        (
            '#0050080896V#054F快！\n',
            '导力梯那边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0106, 6)
    OP_72(0x0008, 0x0010)
    OP_6F(0x0008, 30)

    @scena.Lambda('lambda_3C56')
    def lambda_3C56():
        CameraMove(-117150, 0, -90, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3C56)

    @scena.Lambda('lambda_3C6E')
    def lambda_3C6E():
        ChrWalkTo(0x00FE, -115020, 0, -1200, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3C6E)

    Sleep(400)

    @scena.Lambda('lambda_3C8E')
    def lambda_3C8E():
        ChrWalkTo(0x00FE, -118160, 0, -1120, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C8E)

    Sleep(200)

    @scena.Lambda('lambda_3CAE')
    def lambda_3CAE():
        ChrWalkTo(0x00FE, -116570, 0, -820, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3CAE)

    Sleep(100)

    @scena.Lambda('lambda_3CCE')
    def lambda_3CCE():
        ChrWalkTo(0x00FE, -117140, 0, -1780, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3CCE)

    Sleep(800)

    @scena.Lambda('lambda_3CEE')
    def lambda_3CEE():
        CameraMove(-117430, 0, 16500, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_3CEE)

    @scena.Lambda('lambda_3D06')
    def lambda_3D06():
        OP_67(0, 3630, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D06)

    @scena.Lambda('lambda_3D1E')
    def lambda_3D1E():
        CameraSetDistance(3490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D1E)

    @scena.Lambda('lambda_3D2E')
    def lambda_3D2E():
        OP_6C(21000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3D2E)

    WaitForThreadExit(0x0106, 0x0001)

    @scena.Lambda('lambda_3D43')
    def lambda_3D43():
        ChrWalkTo(0x00FE, -117320, 0, 860, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3D43)

    WaitForThreadExit(0x0106, 0x0001)

    @scena.Lambda('lambda_3D63')
    def lambda_3D63():
        ChrWalkTo(0x00FE, -118130, 0, 9400, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3D63)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_3D83')
    def lambda_3D83():
        ChrWalkTo(0x00FE, -119470, 0, 8900, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D83)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_3DA3')
    def lambda_3DA3():
        ChrWalkTo(0x00FE, -117320, 0, 8650, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3DA3)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_3DC3')
    def lambda_3DC3():
        ChrWalkTo(0x00FE, -118400, 0, 7920, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3DC3)

    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080897V#005F找到了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3E06')
    def lambda_3E06():
        ChrSetDirection(0x00FE, 303, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3E06)

    @scena.Lambda('lambda_3E14')
    def lambda_3E14():
        ChrTurnDirection(0x0009, 0x0106, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3E14)

    @scena.Lambda('lambda_3E22')
    def lambda_3E22():
        ChrTurnDirection(0x000A, 0x0106, 800)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3E22)

    ChrTurnDirection(0x000B, 0x0106, 800)
    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050080898V#052F是你们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0107,
        (
            '#0070080899V#065F爷、爷爷！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2620080900V唔……\n',
            '阿加特·科洛斯纳！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2630080901V麻烦的家伙又来了……\n',
            '现在我们可没功夫跟你耗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000B, 0x0004)

    @scena.Lambda('lambda_3F11')
    def lambda_3F11():
        ChrWalkTo(0x00FE, -118140, 0, 25690, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_3F11)

    Sleep(500)

    @scena.Lambda('lambda_3F31')
    def lambda_3F31():
        ChrWalkTo(0x00FE, -117680, 0, 25220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_3F31)

    @scena.Lambda('lambda_3F4C')
    def lambda_3F4C():
        ChrMoveTo(0x00FE, -118020, 0, 22380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3F4C)

    Sleep(50)

    @scena.Lambda('lambda_3F6C')
    def lambda_3F6C():
        ChrWalkTo(0x00FE, -117680, 0, 26220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3F6C)

    @scena.Lambda('lambda_3F87')
    def lambda_3F87():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_3F87')

    DispatchAsync2(0x000A, 0x0001, lambda_3F87)

    @scena.Lambda('lambda_3F98')
    def lambda_3F98():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_3F98')

    DispatchAsync2(0x000B, 0x0001, lambda_3F98)

    @scena.Lambda('lambda_3FA9')
    def lambda_3FA9():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_3FA9')

    DispatchAsync2(0x0009, 0x0001, lambda_3FA9)

    ChrTalk(
        0x0101,
        (
            '#0010080902V#005F站、站住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3FDB')
    def lambda_3FDB():
        ChrMoveTo(0x00FE, -118240, 0, 25120, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3FDB)

    @scena.Lambda('lambda_3FF6')
    def lambda_3FF6():
        CameraMove(-118050, 0, 23420, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3FF6)

    @scena.Lambda('lambda_400E')
    def lambda_400E():
        ChrWalkTo(0x00FE, -118140, 0, 23070, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_400E)

    ChrTalk(
        0x0106,
        (
            '#0050080903V#10A #054F休想逃走，混帐！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    @scena.Lambda('lambda_405A')
    def lambda_405A():
        ChrWalkTo(0x00FE, -118720, 0, 21930, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_405A)

    Sleep(200)

    @scena.Lambda('lambda_407A')
    def lambda_407A():
        ChrWalkTo(0x00FE, -117680, 0, 21610, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_407A)

    Sleep(500)

    @scena.Lambda('lambda_409A')
    def lambda_409A():
        ChrWalkTo(0x00FE, -118160, 0, 20240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_409A)

    Sleep(100)

    OP_70(0x0008, 0)
    WaitForThreadExit(0x0106, 0x0001)
    Fade(500)
    ChrSetChipByIndex(0x0106, 6)
    CameraMove(-118180, 0, 22740, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050080904V#550F可恶……\n',
            '又被他们逃跑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080905V#003F就、就差那么一步……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0107,
        (
            '#0070080906V#065F怎、怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080907V为什么他们要把爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080908V#012F不管怎样，\n',
            '快从紧急通道追下去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080909V那些黑衣人好像打算\n',
            '就这样从中央工房逃走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0106, 65535)
    ChrTurnDirection(0x0106, 0x0107, 800)

    ChrTalk(
        0x0106,
        (
            '#0050080910V#057F哼，要逃的话，\n',
            '除了从正门之外就是隧道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080911V#054F小鬼们，给我快点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080912V#005F不用你说我也知道啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(2000)
    StopEffect(0x01, 0x02)
    SetScenaFlags(ScenaFlag(0x00A6, 2, 0x532))
    OP_28(0x0041, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x42D5
@scena.Code('func_0A_42D5')
def func_0A_42D5():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '按了按钮，没有任何反应。\n',
            '导力梯好像不能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x433E
@scena.Code('func_0B_433E')
def func_0B_433E():
    OP_13(0x009A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
