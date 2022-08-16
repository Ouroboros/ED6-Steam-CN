import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1210   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1210.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT26/CH20365._CH', 'ED6_DT26/CH20365P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH01493._CH', 'ED6_DT07/CH01493P._CP'),
        ('ED6_DT07/CH02083._CH', 'ED6_DT07/CH02083P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT26/CH20365._CH', 'ED6_DT26/CH20365P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            direction           = 0,
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
            name                = '莱森村长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '摩尔根将军',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奥兰橘婆婆',
            x                   = -25500,
            z                   = 0,
            y                   = 5060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '梅洛涅',
            x                   = -3080,
            z                   = 0,
            y                   = 3140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '碧尔奈婆婆',
            x                   = 5920,
            z                   = 0,
            y                   = 49500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '巴德斯',
            x                   = -25900,
            z                   = 0,
            y                   = 8660,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x252
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x252
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x252
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -26120,
            triggerZ            = 0,
            triggerY            = 47750,
            triggerRange        = 1000,
            actorX              = -26120,
            actorZ              = 1000,
            actorY              = 47750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x276
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2A3',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -2100, 0, 48460, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A0',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_2A0(): pass

    label('loc_2A0')

    Jump('loc_36B')

    def _loc_2A3(): pass

    label('loc_2A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2F1',
    )

    ChrSetPos(0x000F, 7570, 0, 46210, 90)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -2100, 0, 48460, 0)
    ChrSetPos(0x000D, -31510, 0, 2960, 197)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2EE',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_2EE(): pass

    label('loc_2EE')

    Jump('loc_36B')

    def _loc_2F1(): pass

    label('loc_2F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_36B',
    )

    ChrSetPos(0x0008, -24200, 400, 47000, 0)
    ChrSetPos(0x0009, -25480, 0, 46660, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x000F, 7570, 0, 46210, 90)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -2100, 0, 48460, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x000D, -31510, 0, 2960, 197)

    def _loc_36B(): pass

    label('loc_36B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_381',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_09_1F1D)

    Jump('loc_3A5')

    def _loc_381(): pass

    label('loc_381')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_38D'),
        (-1, 'loc_3A5'),
    )

    def _loc_38D(): pass

    label('loc_38D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 3, 0x1A83)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A2',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0C_3C73)

    def _loc_3A2(): pass

    label('loc_3A2')

    Jump('loc_3A5')

    def _loc_3A5(): pass

    label('loc_3A5')

    Return()

# id: 0x0001 offset: 0x3A6
@scena.Code('func_01_3A6')
def func_01_3A6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_B1('T1210_n')

    Jump('loc_3D5')

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 3, 0x1A83)),
            Expr.Return,
        ),
        'loc_3CC',
    )

    OP_B1('T1210_y')

    Jump('loc_3D5')

    def _loc_3CC(): pass

    label('loc_3CC')

    OP_B1('T1210_n')

    def _loc_3D5(): pass

    label('loc_3D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3E6(): pass

    label('loc_3E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3F0',
    )

    Jump('loc_3FE')

    def _loc_3F0(): pass

    label('loc_3F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_3FE',
    )

    OP_6F(0x0001, 10)

    def _loc_3FE(): pass

    label('loc_3FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_420',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x00)
    OP_10(0x02, 0x00)
    OP_10(0x03, 0x00)
    OP_10(0x08, 0x01)
    OP_10(0x09, 0x01)
    OP_10(0x0A, 0x01)
    OP_10(0x0B, 0x01)

    Jump('loc_43F')

    def _loc_420(): pass

    label('loc_420')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_43F',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x00)
    OP_10(0x02, 0x00)
    OP_10(0x03, 0x00)
    OP_10(0x04, 0x01)
    OP_10(0x05, 0x01)
    OP_10(0x06, 0x01)
    OP_10(0x07, 0x01)

    def _loc_43F(): pass

    label('loc_43F')

    Return()

# id: 0x0002 offset: 0x440
@scena.Code('func_02_440')
def func_02_440():
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
        'loc_465',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_5A7')

    def _loc_465(): pass

    label('loc_465')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_5A7')

    def _loc_47E(): pass

    label('loc_47E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_497',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_5A7')

    def _loc_497(): pass

    label('loc_497')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B0',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_5A7')

    def _loc_4B0(): pass

    label('loc_4B0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C9',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_5A7')

    def _loc_4C9(): pass

    label('loc_4C9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_5A7')

    def _loc_4E2(): pass

    label('loc_4E2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FB',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_5A7')

    def _loc_4FB(): pass

    label('loc_4FB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_514',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_5A7')

    def _loc_514(): pass

    label('loc_514')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_5A7')

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_546',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_5A7')

    def _loc_546(): pass

    label('loc_546')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_5A7')

    def _loc_55F(): pass

    label('loc_55F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_578',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_5A7')

    def _loc_578(): pass

    label('loc_578')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_591',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_5A7')

    def _loc_591(): pass

    label('loc_591')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A7',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_5A7(): pass

    label('loc_5A7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5BC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5A7')

    def _loc_5BC(): pass

    label('loc_5BC')

    Return()

# id: 0x0003 offset: 0x5BD
@scena.Code('func_03_5BD')
def func_03_5BD():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_61A',
    )

    ChrTalk(
        0x00FE,
        (
            '以前传说中的龙\n',
            '大部分都是很善良的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该没有像这次这样\n',
            '粗暴的龙吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69E')

    def _loc_61A(): pass

    label('loc_61A')

    ChrTalk(
        0x00FE,
        (
            '龙原来真的存在啊。\n',
            '还以为只是传说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，以前传说中的龙\n',
            '大部分都是很善良的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该没有像这次这样\n',
            '粗暴的龙吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_69E(): pass

    label('loc_69E')

    TalkEnd(0x0010)

    Return()

# id: 0x0004 offset: 0x6A2
@scena.Code('func_04_6A2')
def func_04_6A2():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_755',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_71B',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来导力器\n',
            '为什么会停呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和孩子们在眺望的\n',
            '那个奇怪的岛一样的东西，\n',
            '有什么关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_752')

    def _loc_71B(): pass

    label('loc_71B')

    ChrTalk(
        0x00FE,
        (
            '还是第一次遇到\n',
            '导力器停止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是什么原因呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_752(): pass

    label('loc_752')

    Jump('loc_C65')

    def _loc_755(): pass

    label('loc_755')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_801',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B4',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子他\n',
            '今天也去看果树园了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器不能动\n',
            '他好像也完全不在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_7FE')

    def _loc_7B4(): pass

    label('loc_7B4')

    ChrTalk(
        0x00FE,
        (
            '老头子他\n',
            '今天也去看果树园了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候\n',
            '真希望他在家里帮帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7FE(): pass

    label('loc_7FE')

    Jump('loc_C65')

    def _loc_801(): pass

    label('loc_801')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_8AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_85E',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子他\n',
            '好像和年轻人一起工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道为什么，\n',
            '总算关系变好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AB')

    def _loc_85E(): pass

    label('loc_85E')

    ChrTalk(
        0x00FE,
        (
            '老头子他\n',
            '好像和年轻人一起工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，那个老顽固总算\n',
            '接受了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_8AB(): pass

    label('loc_8AB')

    Jump('loc_C65')

    def _loc_8AE(): pass

    label('loc_8AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_A53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 2, 0x1A4A)),
            Expr.Return,
        ),
        'loc_8F7',
    )

    ChrTalk(
        0x00FE,
        (
            '愿女神\n',
            '保佑你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也会在这里\n',
            '为你们祈祷的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A50')

    def _loc_8F7(): pass

    label('loc_8F7')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0106, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '还以为是谁呢，\n',
            '这不是阿加特吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不是受了伤\n',
            '躺在床上吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F啊啊，刚刚下床。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#050F婆婆这里\n',
            '没受到龙的伤害吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，所幸没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些还都\n',
            '都是多亏了女神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#552F女神保佑啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '确实这次\n',
            '真需要她保佑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，你倒是\n',
            '难得这么诚心嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会为你祈祷，\n',
            '让女神也保佑保佑你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0349, 2, 0x1A4A))

    def _loc_A50(): pass

    label('loc_A50')

    Jump('loc_C65')

    def _loc_A53(): pass

    label('loc_A53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_B84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AF3',
    )

    ChrTalk(
        0x00FE,
        (
            '在战争中房子几乎\n',
            '都被燃烧弹烧掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然炮击目标似乎是\n',
            '以森林为阵地的王国军……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但无论是什么目的，\n',
            '这都是惨无人道的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B81')

    def _loc_AF3(): pass

    label('loc_AF3')

    ChrTalk(
        0x00FE,
        (
            '在战争中房子几乎\n',
            '都被燃烧弹烧掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是阿加特家那边，\n',
            '几乎被烧得一干二净……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在是太惨了，\n',
            '所以大家一起帮忙重建了房子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_B81(): pass

    label('loc_B81')

    Jump('loc_C65')

    def _loc_B84(): pass

    label('loc_B84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_C65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BDF',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '巴德斯去哪儿了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再三叮嘱他\n',
            '外面太危险不要出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C65')

    def _loc_BDF(): pass

    label('loc_BDF')

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '巴德斯去哪儿了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再三叮嘱他\n',
            '外面太危险不要出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，不愧是爷爷和孙子啊。\n',
            '不听劝告这点真是一模一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_C65(): pass

    label('loc_C65')

    TalkEnd(0x000D)

    Return()

# id: 0x0005 offset: 0xC69
@scena.Code('func_05_C69')
def func_05_C69():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_D51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFC',
    )

    ChrTalk(
        0x00FE,
        (
            '城里似乎飞船和搬运车\n',
            '都动不了了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在村子倒还\n',
            '没什么问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这情况继续下去，\n',
            '不知道会变成怎样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_D4E')

    def _loc_CFC(): pass

    label('loc_CFC')

    ChrTalk(
        0x00FE,
        (
            '城里似乎飞船和搬运车\n',
            '都动不了了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……考虑到将后的事\n',
            '真觉得有些不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D4E(): pass

    label('loc_D4E')

    Jump('loc_11CB')

    def _loc_D51(): pass

    label('loc_D51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_E50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DEE',
    )

    ChrTalk(
        0x00FE,
        (
            '本以为果树园的事告一段落了，\n',
            '但怎么导力器又出问题了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是屋漏偏逢连夜雨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，什么时候\n',
            '才能安安稳稳过日子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_E4D')

    def _loc_DEE(): pass

    label('loc_DEE')

    ChrTalk(
        0x00FE,
        (
            '本以为果树园的事告一段落了，\n',
            '但怎么导力器又出问题了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是屋漏偏逢连夜雨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E4D(): pass

    label('loc_E4D')

    Jump('loc_11CB')

    def _loc_E50(): pass

    label('loc_E50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_F5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EAF',
    )

    ChrTalk(
        0x00FE,
        (
            '我老公他们在很努力\n',
            '的种植新树苗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我们夫妇来说\n',
            '这也是新的起点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F5A')

    def _loc_EAF(): pass

    label('loc_EAF')

    ChrTalk(
        0x00FE,
        (
            '我老公他们在很努力\n',
            '的种植新树苗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一周，\n',
            '每天都在不安中度过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '靠大家的捐款，\n',
            '当前的生活应该能撑过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，总算松了口气……\n',
            '现在真是这感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_F5A(): pass

    label('loc_F5A')

    Jump('loc_11CB')

    def _loc_F5D(): pass

    label('loc_F5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1036',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_FC2',
    )

    ChrTalk(
        0x00FE,
        (
            '果树园的事\n',
            '好像谈妥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知是不是我多心，老公的表情\n',
            '好象变得明朗了许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1033')

    def _loc_FC2(): pass

    label('loc_FC2')

    ChrTalk(
        0x00FE,
        (
            '果树园的事\n',
            '好像谈妥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知是不是我多心，老公的表情\n',
            '好象变得明朗了许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是有什么好事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1033(): pass

    label('loc_1033')

    Jump('loc_11CB')

    def _loc_1036(): pass

    label('loc_1036')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_1096',
    )

    ChrTalk(
        0x00FE,
        (
            '老公还没从果树园\n',
            '回来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是个很认真的人，\n',
            '但希望不要太钻牛角尖就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11CB')

    def _loc_1096(): pass

    label('loc_1096')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_11CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_10F9',
    )

    ChrTalk(
        0x00FE,
        (
            '我老公贝斯卡对果树栽培的\n',
            '研究可是满腔热情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是……\n',
            '却发生这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11CB')

    def _loc_10F9(): pass

    label('loc_10F9')

    ChrTalk(
        0x00FE,
        (
            '我老公贝斯卡对果树栽培的\n',
            '研究可是满腔热情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一边购买种植用机械，\n',
            '一边又选择树木的品种……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了果园的发展\n',
            '花尽了心血呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，尽管如此……\n',
            '却发生这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……该怎么\n',
            '安慰他才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_11CB(): pass

    label('loc_11CB')

    TalkEnd(0x000E)

    Return()

# id: 0x0006 offset: 0x11CF
@scena.Code('func_06_11CF')
def func_06_11CF():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1263',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1239',
    )

    ChrTalk(
        0x00FE,
        (
            '每次发生什么事件\n',
            '就会联想到帝国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是１０年前的事\n',
            '但实在是令人悲哀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1260')

    def _loc_1239(): pass

    label('loc_1239')

    ChrTalk(
        0x00FE,
        (
            '每次发生什么事件\n',
            '就会联想到帝国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1260(): pass

    label('loc_1260')

    Jump('loc_1732')

    def _loc_1263(): pass

    label('loc_1263')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_137F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_12DB',
    )

    ChrTalk(
        0x00FE,
        (
            '终于恢复到\n',
            '平常的生活中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的人也好久没\n',
            '去扫墓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定有许多\n',
            '想对故人报告的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137C')

    def _loc_12DB(): pass

    label('loc_12DB')

    ChrTalk(
        0x00FE,
        (
            '终于恢复到\n',
            '平常的生活中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '重建果树园\n',
            '应该要花不少时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但全村人齐心合力的话，\n',
            '一定能克服困难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就像度过\n',
            '百日战役后的混乱时期一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_137C(): pass

    label('loc_137C')

    Jump('loc_1732')

    def _loc_137F(): pass

    label('loc_137F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_150A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 4, 0x1A4C)),
            Expr.Return,
        ),
        'loc_13D4',
    )

    ChrTalk(
        0x00FE,
        (
            '今后似乎\n',
            '还会有很多很多困难的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也请\n',
            '多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1507')

    def _loc_13D4(): pass

    label('loc_13D4')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0106, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了……\n',
            '看来恢复精神了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F啊啊，抱歉。\n',
            '还让婆婆也担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#051F不过，已经没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#051F虽然不算完全恢复，\n',
            '不过马上开始工作是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，那就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后似乎\n',
            '还会有很多很多困难的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以无论如何\n',
            '自己要多多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0349, 4, 0x1A4C))

    def _loc_1507(): pass

    label('loc_1507')

    Jump('loc_1732')

    def _loc_150A(): pass

    label('loc_150A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_1659',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_157F',
    )

    ChrTalk(
        0x00FE,
        (
            '米夏有着可爱的笑容，\n',
            '是个为哥哥着想的好妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那以后就过了１０年啊……\n',
            '时间过得真快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1656')

    def _loc_157F(): pass

    label('loc_157F')

    ChrTalk(
        0x00FE,
        (
            '米夏有着可爱的笑容，\n',
            '是个为哥哥着想的好妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，也有像哥哥一样\n',
            '坚强的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是一个一旦决定的事\n',
            '就一定会贯彻到底的女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果她没事，现在应该\n',
            '在果园独当一面了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这样想过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1656(): pass

    label('loc_1656')

    Jump('loc_1732')

    def _loc_1659(): pass

    label('loc_1659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1732',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_16B8',
    )

    ChrTalk(
        0x00FE,
        (
            '孩子们的哭叫，\n',
            '树木燃烧的气味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……让人联想起\n',
            '１０年前的战争啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1732')

    def _loc_16B8(): pass

    label('loc_16B8')

    ChrTalk(
        0x00FE,
        (
            '孩子们的哭叫，\n',
            '树木燃烧的气味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……让人联想起\n',
            '１０年前的战争啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那时候也是，一瞬间\n',
            '失去了所有东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1732(): pass

    label('loc_1732')

    TalkEnd(0x000F)

    Return()

# id: 0x0007 offset: 0x1736
@scena.Code('func_07_1736')
def func_07_1736():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1BE0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 3, 0x2093)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A3A',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17D5',
    )

    ChrTalk(
        0x00FE,
        (
            '噢，是阿加特和大家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难不成是来\n',
            '看看村子的情况的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F嗯，差不多吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看起来好像\n',
            '没什么特别的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_1842')

    def _loc_17D5(): pass

    label('loc_17D5')

    ChrTalk(
        0x00FE,
        (
            '噢，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F你好，村长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F前阵子承蒙照顾了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……村子的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    def _loc_1842(): pass

    label('loc_1842')

    ChrTalk(
        0x00FE,
        (
            '呼，现在还很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原本我们村子\n',
            '就没太多的导力机械嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这回倒是多亏这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18F6',
    )

    ChrTalk(
        0x0108,
        (
            '#070F的确，城市那边\n',
            '比村子这混乱多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1971')

    def _loc_18F6(): pass

    label('loc_18F6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1935',
    )

    ChrTalk(
        0x0103,
        (
            '#020F的确，城市那边\n',
            '比村子这混乱多了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1971')

    def _loc_1935(): pass

    label('loc_1935')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1971',
    )

    ChrTalk(
        0x0106,
        (
            '#050F的确，城市那边\n',
            '比村子这混乱多了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1971(): pass

    label('loc_1971')

    ChrTalk(
        0x0102,
        (
            '#1043F可以使平常生活变得便利，\n',
            '但是失去之后完全不知所措……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……算是导力文明的利弊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '水能载舟亦能覆舟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '任何技术\n',
            '都隐藏着危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实问题还是出在\n',
            '我们自己身上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x0412, 3, 0x2093))

    Jump('loc_1BDD')

    def _loc_1A3A(): pass

    label('loc_1A3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1BA4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1A84',
    )

    ChrTalk(
        0x00FE,
        (
            '现在村子还很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了没有大力\n',
            '推进导力化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA1')

    def _loc_1A84(): pass

    label('loc_1A84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B2A',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用\n',
            '对王国军来说是很严重的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说缔结了互不侵犯条约，\n',
            '但在我看来\n',
            '帝国军的动向还是很可疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，希望是我\n',
            '杞人忧天吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1BA1')

    def _loc_1B2A(): pass

    label('loc_1B2A')

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用\n',
            '对王国军来说是很严重的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说缔结了互不侵犯条约，\n',
            '但在我看来\n',
            '帝国军的动向还是很可疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BA1(): pass

    label('loc_1BA1')

    Jump('loc_1BDD')

    def _loc_1BA4(): pass

    label('loc_1BA4')

    ChrTalk(
        0x00FE,
        (
            '现在村子还很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了没有大力\n',
            '推进导力化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1BDD(): pass

    label('loc_1BDD')

    Jump('loc_1EB1')

    def _loc_1BE0(): pass

    label('loc_1BE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1E6A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 3, 0x1A4B)),
            Expr.Return,
        ),
        'loc_1C39',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然很期待\n',
            '你们的活跃表现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，什么事情\n',
            '都不要太勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E67')

    def _loc_1C39(): pass

    label('loc_1C39')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '噢，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '捕获作战那边\n',
            '有什么进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，龙失控的原因\n',
            '差不多知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F下次作战如果顺利，\n',
            '说不定就可以阻止它的失控。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是吗，真是好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，还是不能\n',
            '太勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '特别是阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你要是有个三长两短\n',
            '我可不答应啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#552F嗯，不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这里有个\n',
            '监督我的小鬼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#067F啊，嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，那就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，什么事情\n',
            '都要多加小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙是种超过人类智慧想象的生物。\n',
            '不知道会发生什么事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F啊啊，我会\n',
            '牢牢记住的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0349, 3, 0x1A4B))

    def _loc_1E67(): pass

    label('loc_1E67')

    Jump('loc_1EB1')

    def _loc_1E6A(): pass

    label('loc_1E6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_1EB1',
    )

    ChrTalk(
        0x00FE,
        (
            '阿加特的事\n',
            '就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么\n',
            '去柏斯的路上要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EB1(): pass

    label('loc_1EB1')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x1EB5
@scena.Code('func_08_1EB5')
def func_08_1EB5():
    TalkBegin(0x0009)

    ChrTalk(
        0x0009,
        (
            '#0070890018V#060F我会在这里\n',
            '好好照顾阿加特哥哥的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890019V姐姐你们\n',
            '也一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x1F1D
@scena.Code('func_09_1F1D')
def func_09_1F1D():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetPos(0x0000, -27360, 0, 44980, 305)
    CameraMove(-27230, 0, 39560, 0)
    OP_67(0, 7150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0008, -24200, 400, 47000, 0)
    ChrSetPos(0x0009, -25480, 0, 46660, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    OP_6F(0x0001, 10)
    OP_4A(0x0009, 255)

    @scena.Lambda('lambda_1FC4')
    def lambda_1FC4():
        CameraMove(-24990, 0, 47100, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FC4)

    @scena.Lambda('lambda_1FDC')
    def lambda_1FDC():
        OP_67(0, 6150, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FDC)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    Fade(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2017',
    )

    Call(0, 0x0012)

    def _loc_2017(): pass

    label('loc_2017')

    CameraMove(4120, 200, 47460, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 3250, 200, 45650, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2097',
    )

    ChrSetPos(0x00F7, 4580, 200, 45570, 0)
    ChrSetPos(0x00F8, 2310, 200, 46950, 90)

    Jump('loc_20B9')

    def _loc_2097(): pass

    label('loc_2097')

    ChrSetPos(0x00F8, 4580, 200, 45570, 0)
    ChrSetPos(0x00F7, 2310, 200, 46950, 90)

    def _loc_20B9(): pass

    label('loc_20B9')

    ChrSetPos(0x000B, 3300, 250, 48050, 180)
    ChrSetPos(0x000A, 4600, 200, 48050, 180)
    ChrSetPos(0x000C, 2350, 0, 48960, 180)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x00F7, 0x0004)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x00F7, 0x0040)
    ChrSetFlags(0x00F8, 0x0040)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x00F7, 0x0080)
    ChrClearFlags(0x00F8, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x00F7, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetSubChip(0x000A, 7)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 11)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2186',
    )

    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0103, 6)

    def _loc_2186(): pass

    label('loc_2186')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_219E',
    )

    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0104, 7)

    def _loc_219E(): pass

    label('loc_219E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21B6',
    )

    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0105, 8)

    def _loc_21B6(): pass

    label('loc_21B6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21CE',
    )

    ChrSetSubChip(0x0108, 0)
    ChrSetChipByIndex(0x0108, 9)

    def _loc_21CE(): pass

    label('loc_21CE')

    OP_4A(0x000A, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x000A,
        (
            '#1180301313V原来如此……\n',
            '竟然是这样的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301314V艾丝蒂尔小姐，将军阁下。\n',
            '给你们添了不少麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301315V#1003F哪里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301316V结果我们还是没能\n',
            '阻止龙的失控……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301317V#1007F没派上什么用场，\n',
            '实在抱歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0600301318V#163F#5P嗯，别泄气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301319V#160F无论结果如何，你们的\n',
            '快速行动就已经帮了大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301320V超市的救援行动，\n',
            '还有果树园的灭火行动等等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301321V#1016F啊、啊哈哈……\n',
            '将军大人这样夸奖\n',
            '真让人愧不敢当呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301322V#1026F先不说这个……\n',
            '关于阿加特的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301323V他妹妹米夏\n',
            '真的在１０年前的战争中……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301324V唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301325V帝国军和王国军的战斗\n',
            '就发生在村子近郊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301326V当时，帝国军的燃烧弾\n',
            '击中了几处民宅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301327V结果不但烧毁了房屋，\n',
            '还出现了牺牲者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301328V米夏就是其中之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301329V#1003F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2613',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2562',
    )

    ChrSetSubChip(0x00F7, 2)
    Sleep(300)

    Jump('loc_2587')

    def _loc_2562(): pass

    label('loc_2562')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_257D',
    )

    ChrSetSubChip(0x00F8, 2)
    Sleep(300)

    Jump('loc_2587')

    def _loc_257D(): pass

    label('loc_257D')

    ChrSetSubChip(0x00F8, 1)
    Sleep(300)

    def _loc_2587(): pass

    label('loc_2587')

    ChrTalk(
        0x0103,
        (
            '#0030301330V#524F其实我也知道\n',
            '一点内情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030301331V但看阿加特不太想说的\n',
            '样子就没开口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301332V#1026F原来是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0103, 0)

    def _loc_2613(): pass

    label('loc_2613')

    ChrTalk(
        0x000B,
        (
            '#0600301333V#163F#5P……从某种意义上来说，\n',
            '这是我们王国军的失败。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301334V#160F设置在村子周围的防线\n',
            '招来了帝国军的猛烈攻击……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301335V结果造成了\n',
            '巨大的损害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301336V#1026F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0600301337V#163F#5P而负责这个防线部署\n',
            '的人正是我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301338V可以说一切都是我的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#1180301339V#2P……将军阁下。\n',
            '请不必太过自责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301340V#2P当时王国军只是\n',
            '履行了使命而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301341V#2P结果只是几个巧合的重叠\n',
            '造成了这悲剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 1)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0600301342V#160F#5P不，请不要包庇我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301343V对失去亲人的人来说\n',
            '这种理由是行不通的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301344V就像那红头发的年轻人一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301345V#2P……那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 0)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0600301346V#163F#5P村里举行牺牲者的葬礼时，\n',
            '我作为军方代表出席了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301347V当时看到的那红头发少年的眼神，\n',
            '我现在还历历在目。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301348V仿佛是将无尽的哀伤\n',
            '硬生生用愤怒压制住……\n',
            '那样令人心痛的眼神。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301349V#160F让他带有这种眼神……\n',
            '一切都是我造成的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301350V#2P……不。\n',
            '不是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301351V#2P阿加特真正痛责的\n',
            '不是帝国军，更不是阁下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301352V#2P其实是他自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 1)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0600301353V#161F#5P……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301354V#1015F怎，怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)
    Sleep(50)

    ChrTalk(
        0x000A,
        (
            '#1180301355V我也不知道该怎么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301356V不过阿加特似乎认为米夏的死\n',
            '是自己的責任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301357V虽然绝对不是这样，\n',
            '但他就是一直认为都是自己的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301358V而对于自己的强烈自责，\n',
            '他离开了村子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301359V带着如何才能补偿米夏的疑问，\n',
            '四处寻找心中的答案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301360V恐怕在卢安度过那些\n',
            '颓废的日子，就是因为\n',
            '还没有找到答案吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301361V#1003F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301362V之后，虽然\n',
            '走上了游击士的道路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301363V但看来，他还是\n',
            '没有找到答案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301364V和１０年前一样，\n',
            '还被困在深深的哀伤\n',
            '和对自己的愤怒之中吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0600301365V#163F#5P……真令人心痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301366V#1002F……对了，将军……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301367V还是让我们\n',
            '也帮忙对付龙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 0)
    Sleep(50)

    ChrTalk(
        0x000B,
        (
            '#0600301368V#161F#5P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301369V#1000F我们游击士\n',
            '有军方没有的优势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301370V行动迅速、\n',
            '亲近市民等等……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301371V军人们平时进不去的\n',
            '隐秘之地我们也可以深入。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301372V一定能派上用场的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0600301373V#163F#5P但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301374V#1010F我想阿加特他\n',
            '或许就是感到\n',
            '这方面的可能性呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301375V如何才能补偿妹妹，\n',
            '为了找到答案而参加游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301376V#1003F……所以，阿加特\n',
            '会被老爸劝导成为游击士的理由，\n',
            '现在终于理解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301377V因为老爸也是因妈妈的去世\n',
            '才毅然决定走上游击士的道路的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0600301378V#160F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301379V#1002F为了再一次确认\n',
            '游击士的意义所在……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301380V更重要的是，为了帮助\n',
            '眼前遇到困难的人们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301381V我希望能尽现在自己\n',
            '最大的努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301382V所以……\n',
            '请让我们协助作战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_30E7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060211101V#542F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030301384V#027F呵呵，说得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E6')

    def _loc_30E7(): pass

    label('loc_30E7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3153',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301385V#035F呼，不愧是艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030301386V#027F嗯嗯，说得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E6')

    def _loc_3153(): pass

    label('loc_3153')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_31B9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301387V#524F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080301388V#070F呵呵，说得好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E6')

    def _loc_31B9(): pass

    label('loc_31B9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_321D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060211101V#542F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040301390V#035F呼，真厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E6')

    def _loc_321D(): pass

    label('loc_321D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3283',
    )

    ChrTalk(
        0x0105,
        (
            '#0060211101V#542F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080301388V#070F呵呵，说得好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E6')

    def _loc_3283(): pass

    label('loc_3283')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32E6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301390V#035F呼，真厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080301394V#070F啊啊，说得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32E6(): pass

    label('loc_32E6')

    ChrTalk(
        0x000B,
        (
            '#0600301395V#160F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301396V#163F１０年前，如果柏斯地区\n',
            '也有游击士，或许……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301397V#1015F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0600301398V#163F#5P不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301399V#160F我代替繁忙的卡西乌斯\n',
            '负责担任\n',
            '这次对龙作战的指挥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301400V差不多该回哈肯大门了，\n',
            '军事会议就要开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301401V你的提案\n',
            '到时再做讨论。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301402V#1018F这，这么说……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0600301403V#163F#5P别高兴得太早。\n',
            '单纯只是讨论而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301404V#160F今晚会把军事会议的结果\n',
            '传达给柏斯支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301405V我能保证的就只有这些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301406V#1006F……嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_355A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301407V#027F恭候您的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35C7')

    def _loc_355A(): pass

    label('loc_355A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3592',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301408V#071F恭候您的联络了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35C7')

    def _loc_3592(): pass

    label('loc_3592')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35C7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301409V#031F恭候您的联络啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35C7(): pass

    label('loc_35C7')

    ChrTalk(
        0x000B,
        (
            '#0600301410V#160F#5P那么我\n',
            '就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 1)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0600301411V#160F#5P村长，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#1180301412V#2P哪里哪里。\n',
            '请再来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetFlags(0x000B, 0x0001)
    ChrSetPos(0x000B, 2480, 0, 48000, 270)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 3)
    OP_0D()

    @scena.Lambda('lambda_368B')
    def lambda_368B():
        CameraMove(1500, 0, 44410, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_368B)

    CreateThread(0x000B, 0x01, 0x00, func_0A_3BA5)
    Sleep(800)

    CreateThread(0x000C, 0x01, 0x00, func_0B_3C15)
    ChrSetSubChip(0x0101, 1)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36DE',
    )

    ChrSetSubChip(0x00F7, 1)
    Sleep(50)

    ChrSetSubChip(0x00F8, 2)
    Sleep(300)

    Jump('loc_36F2')

    def _loc_36DE(): pass

    label('loc_36DE')

    ChrSetSubChip(0x00F7, 2)
    Sleep(50)

    ChrSetSubChip(0x00F8, 1)
    Sleep(300)

    def _loc_36F2(): pass

    label('loc_36F2')

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    CameraMove(4370, 0, 47120, 3000)
    WaitForThreadExit(0x000C, 0x0001)
    ChrSetSubChip(0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010301413V#1006F好了，我们\n',
            '差不多也该回柏斯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301414V#1015F阿加特……\n',
            '还是不要动的好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37FD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301415V#047F他那个伤势还是静养２、３日\n',
            '会比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060301416V#542F今晚就让他好好\n',
            '睡一觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F0')

    def _loc_37FD(): pass

    label('loc_37FD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3878',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301417V#074F他那个伤势还是静养２、３日\n',
            '会比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080301418V#070F今晚就让他好好\n',
            '睡一觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F0')

    def _loc_3878(): pass

    label('loc_3878')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38F0',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301419V#035F他那个伤势还是静养２、３日\n',
            '会比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040301420V#030F今晚就让他好好\n',
            '睡一觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38F0(): pass

    label('loc_38F0')

    ChrTalk(
        0x0101,
        (
            '#0010220715V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301422V那就去看看他，\n',
            '顺便和提妲说说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00F8, 0)
    Sleep(50)

    ChrSetSubChip(0x00F7, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010301423V#1015F……村长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301424V这种状况下还麻烦您实在抱歉。\n',
            '阿加特的事，就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301425V#5P呵呵，那家伙\n',
            '就是我们的亲人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301426V#5P虽说事态比较严重，\n',
            '但和１０年前相比还算好的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1180301427V#5P没有出现牺牲者\n',
            '就该感谢女神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(1820, 0, 44890, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 1820, 0, 44890, 225)
    ChrSetPos(0x0001, 1820, 0, 44890, 225)
    ChrSetPos(0x0002, 1820, 0, 44890, 225)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x00F7, 0x0004)
    ChrClearFlags(0x00F8, 0x0004)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x00F7, 0x0040)
    ChrClearFlags(0x00F8, 0x0040)
    ChrSetFlags(0x0101, 0x0001)
    ChrSetFlags(0x00F7, 0x0001)
    ChrSetFlags(0x00F8, 0x0001)
    ChrSetFlags(0x000B, 0x0001)
    ChrSetFlags(0x000A, 0x0001)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 7570, 0, 46210, 90)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetPos(0x000A, -2100, 0, 48460, 0)
    CreateThread(0x000A, 0x00, 0x00, func_02_440)
    CreateThread(0x000F, 0x00, 0x00, func_02_440)
    SetScenaFlags(ScenaFlag(0x0343, 2, 0x1A1A))
    OP_28(0x0094, 0x01, 0x0080)
    OP_28(0x0094, 0x01, 0x0100)
    OP_28(0x0094, 0x01, 0x0200)
    OP_28(0x0094, 0x01, 0x0400)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000A offset: 0x3BA5
@scena.Code('func_0A_3BA5')
def func_0A_3BA5():
    ChrWalkTo(0x00FE, 860, 0, 47770, 2000, 0x00)
    ChrWalkTo(0x00FE, -140, 0, 40510, 2000, 0x00)
    OP_4A(0x000C, 255)
    ChrSetSubChip(0x000C, 0)
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_4B(0x000C, 255)

    @scena.Lambda('lambda_3BEA')
    def lambda_3BEA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3BEA)

    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -140, 0, 38210, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000B offset: 0x3C15
@scena.Code('func_0B_3C15')
def func_0B_3C15():
    ChrWalkTo(0x00FE, 860, 0, 47770, 2000, 0x00)
    ChrWalkTo(0x00FE, -140, 0, 40510, 2000, 0x00)

    @scena.Lambda('lambda_3C43')
    def lambda_3C43():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3C43)

    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -140, 0, 38210, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    PlaySE(7, 0x00, 0x64)

    Return()

# id: 0x000C offset: 0x3C73
@scena.Code('func_0C_3C73')
def func_0C_3C73():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C86',
    )

    Call(0, 0x0012)

    def _loc_3C86(): pass

    label('loc_3C86')

    CameraMove(-24530, 0, 47200, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -25870, -500, 37510, 0)
    ChrSetPos(0x00F7, -25870, -500, 37510, 0)
    ChrSetPos(0x00F8, -25870, -500, 37510, 0)
    OP_4A(0x0009, 255)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(113, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3D30')
    def lambda_3D30():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_3D30')

    DispatchAsync2(0x0009, 0x0001, lambda_3D30)

    PlaySE(6, 0x00, 0x64)

    @scena.Lambda('lambda_3D46')
    def lambda_3D46():
        CameraMove(-25990, 0, 46100, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D46)

    @scena.Lambda('lambda_3D5E')
    def lambda_3D5E():
        ChrTurnDirection(0x0009, 0x0101, 400)
        Yield()

        Jump('lambda_3D5E')

    DispatchAsync2(0x0009, 0x0001, lambda_3D5E)

    CreateThread(0x0101, 0x01, 0x00, func_0D_4F32)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_0E_4F4E)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_0F_4F7E)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0070301428V#560F啊，姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301429V#1006F#6P提妲，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301430V阿加特的情况怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301431V#561F嗯……\n',
            '好像睡得很熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301432V#066F不过，脸色变得好起来了，\n',
            '好好休息应该没问题吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301433V#1025F#6P是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301434V#1006F话说……\n',
            '这里就是阿加特的家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0101, 90, 400)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F2A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301435V#031F#6P唔，狭小而温暖…\n',
            '令人感觉很舒服呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FC5')

    def _loc_3F2A(): pass

    label('loc_3F2A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F78',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301436V#048F#6P狭小而温暖…\n',
            '令人感觉很舒服的家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FC5')

    def _loc_3F78(): pass

    label('loc_3F78')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FC5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301437V#021F#6P嗯～狭小而温暖…\n',
            '令人感觉很舒服的家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FC5(): pass

    label('loc_3FC5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4011',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301438V#070F#6P他就在这里和妹妹两人\n',
            '相依为命啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40A8')

    def _loc_4011(): pass

    label('loc_4011')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_405F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301439V#027F#6P他就在这里和妹妹两人\n',
            '相依为命啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40A8')

    def _loc_405F(): pass

    label('loc_405F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40A8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301440V#048F#6P他就在这里和妹妹两人\n',
            '相依为命啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40A8(): pass

    label('loc_40A8')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010301441V#1004F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_40F4')
    def lambda_40F4():
        CameraMove(-26280, 0, 46950, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_40F4)

    @scena.Lambda('lambda_410C')
    def lambda_410C():
        ChrWalkTo(0x00FE, -26450, 0, 46830, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_410C)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0009, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010301442V#1011F#6P这照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x00F7, 0x01, 0x00, func_10_4F9A)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_11_4FB6)
    Sleep(500)

    FadeOut(500, 0, -1)
    OP_0D()
    OP_AD('ED6_DT24/C_VIS107._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(100, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010301443V#1006F这是阿加特\n',
            '小时候的照片吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301444V那么，这个女孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(300, 310, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070301445V#066F嗯……\n',
            '应该是米夏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42B1',
    )

    SetMessageWindowPos(200, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0030301446V#021F哎呀呀……\n',
            '好可爱的女孩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030301447V应该和阿加特\n',
            '关系相当亲密吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()

    Jump('loc_43AE')

    def _loc_42B1(): pass

    label('loc_42B1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4338',
    )

    SetMessageWindowPos(200, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040301448V#031F唔……\n',
            '真是个可爱女孩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040301449V#030F应该和阿加特\n',
            '关系相当亲密吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()

    Jump('loc_43AE')

    def _loc_4338(): pass

    label('loc_4338')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43AE',
    )

    SetMessageWindowPos(200, 320, -1, -1)
    TalkSetChrName('科洛丝')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0060301450V#048F好可爱的女孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060301451V应该和阿加特\n',
            '关系相当亲密吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()

    def _loc_43AE(): pass

    label('loc_43AE')

    SetMessageWindowPos(300, 310, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070301452V#067F嘿嘿，我想是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301453V阿加特和米夏\n',
            '都笑得好开心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(100, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010301454V#1006F嗯……真的是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301455V年龄的话，阿加特是１４岁左右，\n',
            '米夏是１２岁的样子吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301456V阿加特…啊哈\n',
            '那时还是个毛头小子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301457V#1001F呵呵，真好玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4596',
    )

    SetMessageWindowPos(150, 320, -1, -1)
    TalkSetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080301458V#070F嗯，男人过去的照片\n',
            '不要太认真考究。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080301459V很难为情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(100, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010301460V#1016F啊哈哈……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()

    def _loc_4596(): pass

    label('loc_4596')

    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetDirection(0x0101, 180, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010301461V#1015F#5P话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301462V为什么阿加特\n',
            '要隐瞒妹妹的事呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301463V一直说的好像\n',
            '她还活着一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301464V#063F嗯……不过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301465V#561F仔细一想阿加特哥哥\n',
            '好象从来没说过\n',
            '米夏还活着呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301466V『偶尔回去露个脸』\n',
            '原来是说扫墓……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010301467V#1026F这么说来也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301468V#1015F不过，我们\n',
            '都误会了这事\n',
            '阿加特应该也知道吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301469V为什么从来不纠正呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301470V#063F这我也不大清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301471V#067F不过，阿加特哥哥\n',
            '说过工作告一段落之后\n',
            '会介绍给我的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301472V我想他是打算在那时\n',
            '好好解释的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301473V#1006F是吗……也是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301474V#1007F嗯，他到底是怎么想的\n',
            '以后再问吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301475V#1015F对了，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301476V我们差不多\n',
            '该回柏斯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301477V#064F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了必须去协会\n',
            '等候王国军联络的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0070301478V#063F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230334V……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301480V#561F那，那个，姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301481V#1006F恩，我们了解，你不用多说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301482V为了照顾阿加特\n',
            '你想说要留在这里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0070301483V#065F啊啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301484V#1028F哼哼，可别小看\n',
            '姐姐我哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301485V妹妹在想什么\n',
            '我全～都知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301486V#562F啊，啊呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4AEC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301487V#021F#6P呵呵，这边的事\n',
            '就不必担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B75')

    def _loc_4AEC(): pass

    label('loc_4AEC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B32',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301488V#031F#6P呼，这边的事\n',
            '就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B75')

    def _loc_4B32(): pass

    label('loc_4B32')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B75',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301489V#041F#6P呵呵，这边的事\n',
            '请不必担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B75(): pass

    label('loc_4B75')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4BCE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301490V#070F#6P你啊，\n',
            '就专心照顾阿加特吧，\n',
            '让他早日恢复健康。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C89')

    def _loc_4BCE(): pass

    label('loc_4BCE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C2B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301491V#048F#6P提妲啊，\n',
            '你就专心照顾阿加特吧，\n',
            '让他早日恢复健康。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C89')

    def _loc_4C2B(): pass

    label('loc_4C2B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C89',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301492V#035F#6P呼，提妲\n',
            '就用你的爱来照顾阿加特，\n',
            '让他早日恢复原样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C89(): pass

    label('loc_4C89')

    TerminateThread(0x0009, 0x01)
    ChrSetDirection(0x0009, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070301493V#560F#2P姐姐……大家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301494V#067F那个那个……\n',
            '感激不尽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301495V#1016F哎呀～不需要\n',
            '特别道谢啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301496V#1006F阿加特要是醒了，\n',
            '能把刚才的事转告他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 270, 400)

    ChrTalk(
        0x0009,
        (
            '#0070301497V#064F啊，可能要协助王国军\n',
            '作战的事对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301498V#1006F嗯，还有阿加特\n',
            '要是再勉强乱来的话，\n',
            '就算用身子挡也要挡住他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301499V在没有完全恢复之前，\n',
            '绝对不许他起床哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301500V#067F嗯……我会努力的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301501V#560F姐姐你们……\n',
            '也要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-25860, 0, 43830, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0000, -25790, 0, 43940, 180)
    ChrSetPos(0x0001, -25790, 0, 43940, 180)
    ChrSetPos(0x0002, -25790, 0, 43940, 180)
    ChrClearFlags(0x00F7, 0x0004)
    ChrClearFlags(0x00F8, 0x0004)
    OP_69(0x0000, 0)
    ChrSetDirection(0x0009, 90, 0)
    OP_4B(0x0009, 255)
    SetScenaFlags(ScenaFlag(0x0343, 3, 0x1A1B))
    OP_28(0x0094, 0x01, 0x0800)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000D offset: 0x4F32
@scena.Code('func_0D_4F32')
def func_0D_4F32():
    ChrWalkTo(0x00FE, -25840, 0, 44990, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x4F4E
@scena.Code('func_0E_4F4E')
def func_0E_4F4E():
    ChrWalkTo(0x00FE, -26380, 0, 42790, 2000, 0x00)
    ChrWalkTo(0x00FE, -25090, 0, 43490, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x4F7E
@scena.Code('func_0F_4F7E')
def func_0F_4F7E():
    ChrWalkTo(0x00FE, -26420, 0, 43720, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0010 offset: 0x4F9A
@scena.Code('func_10_4F9A')
def func_10_4F9A():
    ChrWalkTo(0x00FE, -25380, 0, 45320, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0011 offset: 0x4FB6
@scena.Code('func_11_4FB6')
def func_11_4FB6():
    ChrWalkTo(0x00FE, -26020, 0, 44980, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0012 offset: 0x4FD2
@scena.Code('func_12_4FD2')
def func_12_4FD2():
    FadeOut(0, 0, -1)
    CameraMove(-15500, 30, 64410, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
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
        (0x00000000, 'loc_5089'),
        (0x00000001, 'loc_508F'),
        (-1, 'loc_5095'),
    )

    def _loc_5089(): pass

    label('loc_5089')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5095')

    def _loc_508F(): pass

    label('loc_508F')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5095')

    def _loc_5095(): pass

    label('loc_5095')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x0013 offset: 0x50CD
@scena.Code('func_13_50CD')
def func_13_50CD():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS107._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
