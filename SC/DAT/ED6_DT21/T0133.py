import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0133_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0133   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0133.x'
    header.mapIndex       = 10
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0133_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01044._CH', 'ED6_DT07/CH01044P._CP'),
    ]

# id: 0x10001 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '潘杜老人',
            x                   = 3275,
            z                   = 0,
            y                   = 2522,
            direction           = 180,
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
            name                = '梅尔达斯',
            x                   = 3290,
            z                   = 0,
            y                   = 3300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 55210,
            z                   = 10300,
            y                   = 44150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x1AA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -300,
            triggerZ            = 0,
            triggerY            = 4140,
            triggerRange        = 800,
            actorX              = -300,
            actorZ              = 1000,
            actorY              = 4140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53450,
            triggerZ            = 10300,
            triggerY            = 47970,
            triggerRange        = 800,
            actorX              = 53450,
            actorZ              = 10000,
            actorY              = 47970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 51520,
            triggerZ            = 10300,
            triggerY            = 46970,
            triggerRange        = 1700,
            actorX              = 51520,
            actorZ              = 11300,
            actorY              = 46970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x216
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_25D',
    )

    ChrSetPos(0x0008, 55710, 10300, 47580, 270)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 54840, 10300, 46250, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24F',
    )

    Jump('loc_25A')

    def _loc_24F(): pass

    label('loc_24F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25A',
    )

    Jump('loc_25A')

    def _loc_25A(): pass

    label('loc_25A')

    Jump('loc_2B6')

    def _loc_25D(): pass

    label('loc_25D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_27F',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27C',
    )

    ChrClearFlags(0x000A, 0x0080)

    def _loc_27C(): pass

    label('loc_27C')

    Jump('loc_2B6')

    def _loc_27F(): pass

    label('loc_27F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_289',
    )

    Jump('loc_2B6')

    def _loc_289(): pass

    label('loc_289')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_29A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_297',
    )

    def _loc_297(): pass

    label('loc_297')

    Jump('loc_2B6')

    def _loc_29A(): pass

    label('loc_29A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2B1',
    )

    ChrSetFlags(0x0008, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AE',
    )

    def _loc_2AE(): pass

    label('loc_2AE')

    Jump('loc_2B6')

    def _loc_2B1(): pass

    label('loc_2B1')

    ChrSetFlags(0x0008, 0x0010)

    def _loc_2B6(): pass

    label('loc_2B6')

    Return()

# id: 0x0001 offset: 0x2B7
@scena.Code('func_01_2B7')
def func_01_2B7():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35B',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_303',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2EE',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)

    Jump('loc_303')

    def _loc_2EE(): pass

    label('loc_2EE')

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 80000, 0)

    def _loc_303(): pass

    label('loc_303')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31B',
    )

    OP_B1('t0133_n')

    Jump('loc_358')

    def _loc_31B(): pass

    label('loc_31B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34F',
    )

    OP_B1('t0133_y')
    OP_11(0xDB, 0xB7, 0xFF, 0, 65400, 0)

    Jump('loc_358')

    def _loc_34F(): pass

    label('loc_34F')

    OP_B1('t0133_n')

    def _loc_358(): pass

    label('loc_358')

    Jump('loc_369')

    def _loc_35B(): pass

    label('loc_35B')

    OP_B1('t0133_n')
    MapClearFlags(0x00000010)
    def _loc_369(): pass

    label('loc_369')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_375',
    )

    OP_64(0x02, 0x0001)

    def _loc_375(): pass

    label('loc_375')

    OP_E8(0xDC, 0x05, 0x00, 0x00)

    Return()

# id: 0x0002 offset: 0x37B
@scena.Code('func_02_37B')
def func_02_37B():
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
        'loc_3A0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_4E2')

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_4E2')

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D2',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_4E2')

    def _loc_3D2(): pass

    label('loc_3D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EB',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_4E2')

    def _loc_3EB(): pass

    label('loc_3EB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_404',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_4E2')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41D',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_4E2')

    def _loc_41D(): pass

    label('loc_41D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_436',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_4E2')

    def _loc_436(): pass

    label('loc_436')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_4E2')

    def _loc_44F(): pass

    label('loc_44F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_468',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_4E2')

    def _loc_468(): pass

    label('loc_468')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_481',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_4E2')

    def _loc_481(): pass

    label('loc_481')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_49A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_4E2')

    def _loc_49A(): pass

    label('loc_49A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B3',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_4E2')

    def _loc_4B3(): pass

    label('loc_4B3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_4E2')

    def _loc_4CC(): pass

    label('loc_4CC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E2',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_4E2(): pass

    label('loc_4E2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4F7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_4E2')

    def _loc_4F7(): pass

    label('loc_4F7')

    Return()

# id: 0x0003 offset: 0x4F8
@scena.Code('func_03_4F8')
def func_03_4F8():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_614',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 1, 0x2099)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_511',
    )

    Call(0, 0x0005)

    Jump('loc_611')

    def _loc_511(): pass

    label('loc_511')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_559',
    )

    ChrTalk(
        0x00FE,
        (
            '你们难得\n',
            '回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别总是工作，\n',
            '偶尔也要享受一下啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_611')

    def _loc_559(): pass

    label('loc_559')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AA',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器瘫痪的理由\n',
            '现在还不能确定…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '但真是头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_611')

    def _loc_5AA(): pass

    label('loc_5AA')

    ChrTalk(
        0x00FE,
        (
            '那个跟岛一样的东西\n',
            '出现在天空的同时，\n',
            '时钟就停止运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎不是偶然啊。\n',
            '肯定有什么关联吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_611(): pass

    label('loc_611')

    Jump('loc_A2A')

    def _loc_614(): pass

    label('loc_614')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_786',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_692',
    )

    ChrTalk(
        0x00FE,
        (
            '那个料理我\n',
            '还是记得很清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，去问问城里的\n',
            '婆婆们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我们那个年代，\n',
            '几乎谁都会做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_783')

    def _loc_692(): pass

    label('loc_692')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0100)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6BD',
    )

    Call(1, 0x0000)

    Jump('loc_783')

    def _loc_6BD(): pass

    label('loc_6BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_70F',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁克那小子\n',
            '似乎也恢复健康了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '玩闹时的叫喊声\n',
            '在这里都能听到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_783')

    def _loc_70F(): pass

    label('loc_70F')

    ChrTalk(
        0x00FE,
        (
            '鲁克那小子\n',
            '似乎也恢复健康了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '玩闹时的叫喊声\n',
            '在这里都能听到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，洛连特还是适合\n',
            '灿烂的阳光啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_783(): pass

    label('loc_783')

    Jump('loc_A2A')

    def _loc_786(): pass

    label('loc_786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_8A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_80B',
    )

    ChrTalk(
        0x00FE,
        (
            '和帝国的互不侵犯条约顺利签订，\n',
            '对利贝尔来说也是一个里程碑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对『百日战役』的牺牲者\n',
            '也算是一个交代和缅怀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89D')

    def _loc_80B(): pass

    label('loc_80B')

    ChrTalk(
        0x00FE,
        (
            '说起来的话，今天\n',
            '好像就是互不侵犯条约的签字仪式啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔也要踏出\n',
            '崭新的一步了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对『百日战役』的牺牲者\n',
            '也算是一个交代和缅怀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_89D(): pass

    label('loc_89D')

    Jump('loc_A2A')

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_970',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_901',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，钟楼的钟声\n',
            '听起来很不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些、那些都\n',
            '一定是因为这次的浓雾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96D')

    def _loc_901(): pass

    label('loc_901')

    ChrTalk(
        0x00FE,
        (
            '今天早上也是\n',
            '一片浓雾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是心理问题吗，总觉得钟声\n',
            '也变得很不对劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听起来似乎\n',
            '很不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_96D(): pass

    label('loc_96D')

    Jump('loc_A2A')

    def _loc_970(): pass

    label('loc_970')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_A2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9CF',
    )

    ChrTalk(
        0x00FE,
        (
            '今天也没问题了，\n',
            '希望能永远和平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战争永远都是\n',
            '我们不希望看见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A2A')

    def _loc_9CF(): pass

    label('loc_9CF')

    ChrTalk(
        0x00FE,
        (
            '嗯…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也没问题了，\n',
            '希望能永远和平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战争永远都是\n',
            '我们不希望看见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A2A(): pass

    label('loc_A2A')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0xA2E
@scena.Code('func_04_A2E')
def func_04_A2E():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 1, 0x2099)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A40',
    )

    Call(0, 0x0005)

    Jump('loc_BF2')

    def _loc_A40(): pass

    label('loc_A40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_A97',
    )

    ChrTalk(
        0x00FE,
        (
            '可是导力器\n',
            '为什么会突然停止呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 270, 400)

    ChrTalk(
        0x00FE,
        (
            '果然是因为那座岛\n',
            '的缘故吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_A97(): pass

    label('loc_A97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AF4',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器为什么会突然瘫痪呢，\n',
            '谁也想不出理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是因为天上\n',
            '那座岛屿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_AF4(): pass

    label('loc_AF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BA4',
    )

    ChrTalk(
        0x00FE,
        (
            '最近一直在这钟楼上\n',
            '眺望那座岛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么大的东西能漂浮在空中，\n',
            '真让人不敢相信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器瘫痪也是\n',
            '因为它的缘故吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么想的话，\n',
            '总有种不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_BF2')

    def _loc_BA4(): pass

    label('loc_BA4')

    ChrTalk(
        0x00FE,
        (
            '导力器瘫痪的时候也是\n',
            '那座岛出现的时候…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话，总有种\n',
            '不好的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF2(): pass

    label('loc_BF2')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xBF6
@scena.Code('func_05_BF6')
def func_05_BF6():
    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0009, 0x0101, 400)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '哦，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '啊，怎么回事，\n',
            '约修亚也在一起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼呼，\n',
            '有一阵没见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F您两位\n',
            '还和以前一样，没什么变化啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里还是老样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '城中有很多老机械，\n',
            '工作总是很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在就在检查\n',
            '钟楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '时钟的时针不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F啊，说起来的话，\n',
            '这座钟的时针…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F……是导力式的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊啊，城里的导力器\n',
            '全都不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊，不知道有没有用，\n',
            '我打算给时钟加些油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们也是难得\n',
            '回来一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不要总想着工作，\n',
            '偶尔也要放松一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#1040F呵呵，说的是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#1001F嗯，闲下来的话\n',
            '会休息一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0413, 1, 0x2099))
    OP_4B(0x0009, 255)
    OP_4B(0x0008, 255)
    ChrSetDirection(0x0009, 180, 0)
    ChrSetDirection(0x0008, 135, 0)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0006 offset: 0xE66
@scena.Code('func_06_E66')
def func_06_E66():
    UnlockAchievement(0x01, 0x0005, 0x00)
    TalkBegin(0x000A)

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_F3D',
    )

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
            TXT(0x01, '报告\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F26',
    )

    ChrTalk(
        0x00FE,
        (
            '#3600470610V女神啊、拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3600470611V请一定让游击士们\n',
            '把药的材料收集全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3A')

    def _loc_F26(): pass

    label('loc_F26')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F3A',
    )

    Call(1, 0x0004)

    Jump('loc_F3A')

    def _loc_F3A(): pass

    label('loc_F3A')

    Jump('loc_FB5')

    def _loc_F3D(): pass

    label('loc_F3D')

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_F60',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_F59',
    )

    Call(1, 0x0002)

    Jump('loc_F5D')

    def _loc_F59(): pass

    label('loc_F59')

    Call(1, 0x0001)

    def _loc_F5D(): pass

    label('loc_F5D')

    Jump('loc_FB5')

    def _loc_F60(): pass

    label('loc_F60')

    ChrTalk(
        0x00FE,
        (
            '#3600470612V女神啊、拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3600470613V让我顺利接近那位\n',
            '美丽的姐姐吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_FB5(): pass

    label('loc_FB5')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0xFB9
@scena.Code('func_07_FB9')
def func_07_FB9():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS186._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xFE7
@scena.Code('func_08_FE7')
def func_08_FE7():
    NewScene('ED6_DT21/T0133._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0xFF1
@scena.Code('func_09_FF1')
def func_09_FF1():
    NewScene('ED6_DT21/T0133._SN', 102, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
