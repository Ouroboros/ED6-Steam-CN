import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1503_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1503   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1503.x'
    header.mapIndex       = 59
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/R1503_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH00064._CH', 'ED6_DT07/CH00064P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 1280,
            z                   = 10,
            y                   = 19450,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 2300,
            z                   = 20,
            y                   = 19450,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -120,
            z                   = 50,
            y                   = 21740,
            direction           = 180,
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
            name                = '拉文努山道方向',
            x                   = -111060,
            z                   = -20,
            y                   = -19200,
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
            name                = '拉文努山道方向',
            x                   = 1140,
            z                   = 10,
            y                   = -19200,
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
            x           = -118500,
            y           = -2000,
            z           = 3200,
            range       = -103000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x000017D4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x182
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -114320,
            triggerZ            = 0,
            triggerY            = 6860,
            triggerRange        = 1500,
            actorX              = -114320,
            actorZ              = 50,
            actorY              = 6860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2180,
            triggerZ            = 0,
            triggerY            = 6860,
            triggerRange        = 1500,
            actorX              = -2180,
            actorZ              = 50,
            actorY              = 6860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6240,
            triggerZ            = 0,
            triggerY            = 17780,
            triggerRange        = 1000,
            actorX              = 6240,
            actorZ              = 1000,
            actorY              = 17780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -105760,
            triggerZ            = 0,
            triggerY            = 17780,
            triggerRange        = 1000,
            actorX              = -105760,
            actorZ              = 1000,
            actorY              = 17780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x212
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_21C',
    )

    Jump('loc_2CE')

    def _loc_21C(): pass

    label('loc_21C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29B',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    OP_72(0x0000, 0x0002)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0002)
    OP_72(0x0001, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_28E',
    )

    ChrSetPos(0x0008, -107510, 0, 18670, 270)
    ChrSetPos(0x0009, -108310, 10, 21740, 180)
    ChrSetPos(0x000A, -112120, -20, 21740, 180)

    Jump('loc_298')

    def _loc_28E(): pass

    label('loc_28E')

    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0009, 0x0010)

    def _loc_298(): pass

    label('loc_298')

    Jump('loc_2CE')

    def _loc_29B(): pass

    label('loc_29B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_2CE',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0009, 4130, 10, 21680, 180)
    ChrSetPos(0x000A, 0, 10, 21680, 180)

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2ED',
    )

    Event(1, 0x0003)

    def _loc_2ED(): pass

    label('loc_2ED')

    Return()

# id: 0x0001 offset: 0x2EE
@scena.Code('func_01_2EE')
def func_01_2EE():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_302'),
        (0x00000065, 'loc_31C'),
        (0x00000066, 'loc_31C'),
        (-1, 'loc_336'),
    )

    def _loc_302(): pass

    label('loc_302')

    OP_16(0x02, 4000, -127000, -121000, 2293867)
    ChrClearFlags(0x000B, 0x0004)

    Jump('loc_336')

    def _loc_31C(): pass

    label('loc_31C')

    OP_16(0x02, 4000, -239000, -121000, 2293794)
    ChrClearFlags(0x000C, 0x0004)

    Jump('loc_336')

    def _loc_336(): pass

    label('loc_336')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34E',
    )

    OP_B1('R1503_y')

    Jump('loc_357')

    def _loc_34E(): pass

    label('loc_34E')

    OP_B1('R1503_n')

    def _loc_357(): pass

    label('loc_357')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_41B',
    )

    OP_72(0x0000, 0x0002)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0002)
    OP_72(0x0001, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_418',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 6240, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x02, 'map\\\\mp027_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, -105760, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_418(): pass

    label('loc_418')

    Jump('loc_423')

    def _loc_41B(): pass

    label('loc_41B')

    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    def _loc_423(): pass

    label('loc_423')

    Return()

# id: 0x0002 offset: 0x424
@scena.Code('func_02_424')
def func_02_424():
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
        'loc_449',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_58B')

    def _loc_449(): pass

    label('loc_449')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_462',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_58B')

    def _loc_462(): pass

    label('loc_462')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_58B')

    def _loc_47B(): pass

    label('loc_47B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_494',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_58B')

    def _loc_494(): pass

    label('loc_494')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AD',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_58B')

    def _loc_4AD(): pass

    label('loc_4AD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C6',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_58B')

    def _loc_4C6(): pass

    label('loc_4C6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DF',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_58B')

    def _loc_4DF(): pass

    label('loc_4DF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_58B')

    def _loc_4F8(): pass

    label('loc_4F8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_511',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_58B')

    def _loc_511(): pass

    label('loc_511')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_58B')

    def _loc_52A(): pass

    label('loc_52A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_543',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_58B')

    def _loc_543(): pass

    label('loc_543')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_58B')

    def _loc_55C(): pass

    label('loc_55C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_575',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_58B')

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58B',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_58B(): pass

    label('loc_58B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_58B')

    def _loc_5A0(): pass

    label('loc_5A0')

    Return()

# id: 0x0003 offset: 0x5A1
@scena.Code('func_03_5A1')
def func_03_5A1():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_709',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_65B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_600',
    )

    ChrTalk(
        0x00FE,
        (
            '后面的事情就\n',
            '交给我们王国军吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，接下来也请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_658')

    def _loc_600(): pass

    label('loc_600')

    ChrTalk(
        0x00FE,
        (
            '诸位，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后面的事情就\n',
            '交给我们王国军吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，接下来也请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_658(): pass

    label('loc_658')

    Jump('loc_709')

    def _loc_65B(): pass

    label('loc_65B')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_6F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6B7',
    )

    ChrTalk(
        0x00FE,
        (
            '那边的回复装置\n',
            '可以自由使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么就拜托你们\n',
            '继续扫荡魔兽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F0')

    def _loc_6B7(): pass

    label('loc_6B7')

    ChrTalk(
        0x00FE,
        (
            '哦，回来了吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边的回复装置\n',
            '可以自由使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_6F0(): pass

    label('loc_6F0')

    Jump('loc_709')

    def _loc_6F3(): pass

    label('loc_6F3')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_705',
    )

    Call(1, 0x0001)

    Jump('loc_709')

    def _loc_705(): pass

    label('loc_705')

    Call(1, 0x0000)

    def _loc_709(): pass

    label('loc_709')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x70D
@scena.Code('func_04_70D')
def func_04_70D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_7C1',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_75B',
    )

    ChrTalk(
        0x00FE,
        (
            '这次真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下我们\n',
            '可以专心警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BE')

    def _loc_75B(): pass

    label('loc_75B')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_7A8',
    )

    ChrTalk(
        0x00FE,
        (
            '要注意\n',
            '颜色不一样的家伙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对方会使用\n',
            '没见过的魔法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BE')

    def _loc_7A8(): pass

    label('loc_7A8')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_7BA',
    )

    Call(1, 0x0001)

    Jump('loc_7BE')

    def _loc_7BA(): pass

    label('loc_7BA')

    Call(1, 0x0000)

    def _loc_7BE(): pass

    label('loc_7BE')

    Jump('loc_7F7')

    def _loc_7C1(): pass

    label('loc_7C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_7F7',
    )

    ChrTalk(
        0x00FE,
        (
            '辛苦了。\n',
            '后边的警备就交给我们国境师团吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F7(): pass

    label('loc_7F7')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x7FB
@scena.Code('func_05_7FB')
def func_05_7FB():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_8F2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_859',
    )

    ChrTalk(
        0x00FE,
        (
            '各位，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，到底是游击士啊。\n',
            '消灭魔兽真是手到擒来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EF')

    def _loc_859(): pass

    label('loc_859')

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_8AB',
    )

    ChrTalk(
        0x00FE,
        (
            '里、里面的情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没不断出现\n',
            '那个奇怪的魔兽就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EF')

    def _loc_8AB(): pass

    label('loc_8AB')

    ChrTalk(
        0x00FE,
        (
            '这个时候\n',
            '前面是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至于原因……\n',
            '请问我的上司吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8EF(): pass

    label('loc_8EF')

    Jump('loc_945')

    def _loc_8F2(): pass

    label('loc_8F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_945',
    )

    ChrTalk(
        0x00FE,
        (
            '这个时候\n',
            '前面是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟算是事件的现场嘛。\n',
            '需要保持原样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_945(): pass

    label('loc_945')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x949
@scena.Code('func_06_949')
def func_06_949():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 6, 0x1A16)),
            Expr.Return,
        ),
        'loc_951',
    )

    Return()

    def _loc_951(): pass

    label('loc_951')

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
        'loc_969',
    )

    Call(0, 0x0007)
    Sleep(200)

    def _loc_969(): pass

    label('loc_969')

    Fade(1000)
    CameraMove(-110460, -10, 4260, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -110960, -10, 4750, 0)
    ChrSetPos(0x0107, -109990, 0, 4740, 0)
    ChrSetPos(0x00F8, -111260, 0, 3400, 0)
    ChrSetPos(0x00F9, -110120, 0, 3250, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010301071V#1004F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-108610, 10, 24070, 3000)
    Sleep(1500)

    @scena.Lambda('lambda_0A34')
    def lambda_0A34():
        CameraMove(-109220, -30, 22140, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A34)

    @scena.Lambda('lambda_0A4C')
    def lambda_0A4C():
        ChrWalkTo(0x00FE, -110680, 0, 20670, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A4C)

    Sleep(100)

    @scena.Lambda('lambda_0A6C')
    def lambda_0A6C():
        ChrWalkTo(0x00FE, -109430, 30, 20440, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0A6C)

    Sleep(100)

    @scena.Lambda('lambda_0A8C')
    def lambda_0A8C():
        ChrWalkTo(0x00FE, -111230, 20, 19330, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0A8C)

    Sleep(100)

    @scena.Lambda('lambda_0AAC')
    def lambda_0AAC():
        ChrWalkTo(0x00FE, -109680, 40, 19050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0AAC)

    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010301072V#1020F这里……\n',
            '是废坑的入口吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301073V门开着就是说\n',
            '难道…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrWalkTo(0x0107, -109790, -30, 22470, 2000, 0x00)
    Sleep(500)

    Fade(250)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 0)
    OP_0D()
    Sleep(1000)

    Fade(250)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_0D()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070301074V#065F#5P姐、姐姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301075V这个掉下来的锁……\n',
            '好像是刚刚取下的！',
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
            '#0010301076V#1002F果然……！',
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
        'loc_C64',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301077V#072F#4P是他干的吧。\n',
            '看来似乎跑进去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CFD')

    def _loc_C64(): pass

    label('loc_C64')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301078V#022F#4P是阿加特干的吧。\n',
            '是不是跑进去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CFD')

    def _loc_CB2(): pass

    label('loc_CB2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CFD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301079V#032F#4P阿加特干的吧。\n',
            '看来似乎跑进去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CFD(): pass

    label('loc_CFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D3E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301080V#043F#4P要赶快追上去才行……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBF')

    def _loc_D3E(): pass

    label('loc_D3E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D80',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301081V#032F#4P唔……\n',
            '似乎要抓紧才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBF')

    def _loc_D80(): pass

    label('loc_D80')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DBF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301082V#022F#4P这……\n',
            '看来要抓紧才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DBF(): pass

    label('loc_DBF')

    ChrSetDirection(0x0101, 180, 500)

    ChrTalk(
        0x0101,
        (
            '#0010301083V#1005F#5PＯＫ～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 180, 500)

    ChrTalk(
        0x0107,
        (
            '#0070301084V#062F#5P好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0342, 6, 0x1A16))
    OP_28(0x0094, 0x01, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xE1A
@scena.Code('func_07_E1A')
def func_07_E1A():
    FadeOut(0, 0, -1)
    CameraMove(-153930, -10, 11410, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0x00000000, 'loc_ED1'),
        (0x00000001, 'loc_ED7'),
        (-1, 'loc_EDD'),
    )

    def _loc_ED1(): pass

    label('loc_ED1')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_EDD')

    def _loc_ED7(): pass

    label('loc_ED7')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_EDD')

    def _loc_EDD(): pass

    label('loc_EDD')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['提妲'],
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

# id: 0x0008 offset: 0xF17
@scena.Code('func_08_F17')
def func_08_F17():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉文努矿山',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xF54
@scena.Code('func_09_F54')
def func_09_F54():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FA5',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_1160')

    def _loc_FA5(): pass

    label('loc_FA5')

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
        'loc_1145',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 6240, 1000, 17780, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 50)
    OP_73(0x0000)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 6240, 1000, 17780, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 6240, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_1145(): pass

    label('loc_1145')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_115F',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_115F(): pass

    label('loc_115F')

    Return()

    def _loc_1160(): pass

    label('loc_1160')

    Return()

# id: 0x000A offset: 0x1161
@scena.Code('func_0A_1161')
def func_0A_1161():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11B2',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_136D')

    def _loc_11B2(): pass

    label('loc_11B2')

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
        'loc_1352',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x02, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, -105760, 1000, 17780, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 50)
    OP_73(0x0001)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x03, 'map\\\\mp027_01.eff')
    PlayEffect(0x03, 0x03, 0x00FF, -105760, 1000, 17780, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x03, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, -105760, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0001, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_1352(): pass

    label('loc_1352')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_136C',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_136C(): pass

    label('loc_136C')

    Return()

    def _loc_136D(): pass

    label('loc_136D')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
