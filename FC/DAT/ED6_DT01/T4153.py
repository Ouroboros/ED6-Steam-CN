import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4153_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4153   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4153.x'
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
            dword_08        = 0x000101D0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 4200,
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
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵',
            x                   = -2980,
            z                   = 0,
            y                   = 68330,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 3120,
            z                   = 0,
            y                   = 68420,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -32570,
            z                   = 0,
            y                   = 50050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -9530,
            z                   = 250,
            y                   = 32240,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 9480,
            z                   = 250,
            y                   = 37480,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -2560,
            z                   = 0,
            y                   = 29100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 2640,
            z                   = 0,
            y                   = 29290,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 3800,
            z                   = 0,
            y                   = 65780,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·西街区',
            x                   = -40080,
            z                   = 0,
            y                   = 17660,
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
            name                = '格兰赛尔城方向',
            x                   = 100,
            z                   = 0,
            y                   = 104130,
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
            name                = '王都格兰赛尔·东街区',
            x                   = 40430,
            z                   = 0,
            y                   = 64060,
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
            name                = '王都格兰赛尔·南街区',
            x                   = 20,
            z                   = 0,
            y                   = -3500,
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

# id: 0x10002 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x23A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 18520,
            y           = 0,
            z           = 44050,
            range       = 1500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000A,
        ),
    )

# id: 0x10004 offset: 0x25A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x25A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_268',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_03_53C)

    def _loc_268(): pass

    label('loc_268')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_276',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_04_838)

    def _loc_276(): pass

    label('loc_276')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006E, 'loc_282'),
        (-1, 'loc_298'),
    )

    def _loc_282(): pass

    label('loc_282')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 4, 0x62C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_295',
    )

    SetScenaFlags(ScenaFlag(0x00C5, 4, 0x62C))
    Event(0, func_09_E06)

    def _loc_295(): pass

    label('loc_295')

    Jump('loc_298')

    def _loc_298(): pass

    label('loc_298')

    Return()

# id: 0x0001 offset: 0x299
@scena.Code('func_01_299')
def func_01_299():
    OP_16(0x02, 4000, -138000, -78000, 196702)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2ED',
    )

    OP_72(0x0006, 0x0008)
    OP_72(0x0006, 0x0020)
    OP_72(0x0006, 0x0002)
    OP_6F(0x0006, 0)
    OP_72(0x0002, 0x0010)
    OP_72(0x0005, 0x0008)
    OP_72(0x0005, 0x0020)
    OP_72(0x0005, 0x0002)
    OP_6F(0x0005, 0)
    OP_72(0x0003, 0x0010)

    def _loc_2ED(): pass

    label('loc_2ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3BE',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    CreateThread(0x0008, 0x01, 0x00, func_08_B99)
    CreateThread(0x0009, 0x01, 0x00, func_08_B99)
    CreateThread(0x000A, 0x01, 0x00, func_08_B99)
    CreateThread(0x000B, 0x01, 0x00, func_08_B99)
    CreateThread(0x000C, 0x01, 0x00, func_08_B99)
    CreateThread(0x000D, 0x01, 0x00, func_08_B99)
    CreateThread(0x000E, 0x01, 0x00, func_08_B99)
    CreateThread(0x000F, 0x01, 0x00, func_07_92C)

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_364',
    )

    def _loc_364(): pass

    label('loc_364')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_378',
    )

    ChrSetFlags(0x000F, 0x0080)
    TerminateThread(0x000F, 0xFF)

    def _loc_378(): pass

    label('loc_378')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_383',
    )

    def _loc_383(): pass

    label('loc_383')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_3A0',
    )

    ChrSetFlags(0x000C, 0x0080)
    TerminateThread(0x000C, 0xFF)
    ChrSetFlags(0x000E, 0x0080)
    TerminateThread(0x000E, 0xFF)

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_3AB',
    )

    def _loc_3AB(): pass

    label('loc_3AB')

    CameraSetDistance(4200, 0)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3BE(): pass

    label('loc_3BE')

    Return()

# id: 0x0002 offset: 0x3BF
@scena.Code('func_02_3BF')
def func_02_3BF():
    ExecExpressionWithReg(
        0x0003,
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
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_526')

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FD',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_526')

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_416',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_526')

    def _loc_416(): pass

    label('loc_416')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_526')

    def _loc_42F(): pass

    label('loc_42F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_448',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_526')

    def _loc_448(): pass

    label('loc_448')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_461',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_526')

    def _loc_461(): pass

    label('loc_461')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_526')

    def _loc_47A(): pass

    label('loc_47A')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_493',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_526')

    def _loc_493(): pass

    label('loc_493')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AC',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_526')

    def _loc_4AC(): pass

    label('loc_4AC')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_526')

    def _loc_4C5(): pass

    label('loc_4C5')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_526')

    def _loc_4DE(): pass

    label('loc_4DE')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_526')

    def _loc_4F7(): pass

    label('loc_4F7')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_510',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_526')

    def _loc_510(): pass

    label('loc_510')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_526',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_526(): pass

    label('loc_526')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_53B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_526')

    def _loc_53B(): pass

    label('loc_53B')

    Return()

# id: 0x0003 offset: 0x53C
@scena.Code('func_03_53C')
def func_03_53C():
    EventBegin(0x00)
    CameraMove(4100, 0, 67150, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0102, 3070, 0, 73100, 0)
    ChrSetPos(0x0101, 4410, 0, 72960, 0)

    @scena.Lambda('lambda_05A3')
    def lambda_05A3():
        ChrWalkTo(0x00FE, 4520, 0, 66690, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05A3)

    Sleep(300)

    @scena.Lambda('lambda_05C3')
    def lambda_05C3():
        ChrWalkTo(0x00FE, 3100, 0, 66940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05C3)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_05E3')
    def lambda_05E3():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05E3)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_05F6')
    def lambda_05F6():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05F6)

    ChrTalk(
        0x0101,
        (
            '#000F唔……\n',
            '比想象中收获更大呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且，那个公爵\n',
            '竟然是女王陛下的代理人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F实际掌权的，\n',
            '是理查德上校吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且，自己的阴谋\n',
            '周围的人都浑然不觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '演技和操纵情报的手段\n',
            '还真是高明啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F真是的，约修亚。\n',
            '这可不是称赞敌人的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，那个公爵\n',
            '好像去武术大会了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100848V我们也去看看如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '调查一下公爵的行动，\n',
            '也没什么损失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那么就决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我们赶快去王立竞技场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，王立竞技场\n',
            '是在哪个方向呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我记得应该是在东街区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100854V先回到大街上然后往东走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x838
@scena.Code('func_04_838')
def func_04_838():
    EventBegin(0x00)
    CameraMove(2190, 0, 46270, 0)
    OP_67(0, 29260, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(432, 0)

    @scena.Lambda('lambda_087D')
    def lambda_087D():
        OP_6C(90000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_087D)

    Sleep(1000)

    @scena.Lambda('lambda_0892')
    def lambda_0892():
        CameraMove(10350, 3620, 43920, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0892)

    @scena.Lambda('lambda_08AA')
    def lambda_08AA():
        OP_67(0, 3740, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_08AA)

    Sleep(10000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x8CE
@scena.Code('func_05_8CE')
def func_05_8CE():
    Return()

# id: 0x0006 offset: 0x8CF
@scena.Code('func_06_8CF')
def func_06_8CF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_92B',
    )

    ChrWalkTo(0x00FE, 3800, 0, 40510, 3000, 0x00)
    ChrWalkTo(0x00FE, -2970, 0, 40510, 3000, 0x00)
    ChrWalkTo(0x00FE, -2970, 0, 65560, 3000, 0x00)
    ChrWalkTo(0x00FE, 3800, 0, 65780, 3000, 0x00)

    Jump('func_06_8CF')

    def _loc_92B(): pass

    label('loc_92B')

    Return()

# id: 0x0007 offset: 0x92C
@scena.Code('func_07_92C')
def func_07_92C():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B98',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_95F',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_95F(): pass

    label('loc_95F')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_985',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_985(): pass

    label('loc_985')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9AB',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_9AB(): pass

    label('loc_9AB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9D2',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_9D2(): pass

    label('loc_9D2')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9F8',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_9F8(): pass

    label('loc_9F8')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A1E',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_A1E(): pass

    label('loc_A1E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A43',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_A43(): pass

    label('loc_A43')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A68',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7C')

    def _loc_A68(): pass

    label('loc_A68')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A7C(): pass

    label('loc_A7C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B95',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B86',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111259V#580F（糟糕……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111260V#017F（被发现了吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B86(): pass

    label('loc_B86')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 105, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_B95(): pass

    label('loc_B95')

    Jump('func_07_92C')

    def _loc_B98(): pass

    label('loc_B98')

    Return()

# id: 0x0008 offset: 0xB99
@scena.Code('func_08_B99')
def func_08_B99():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E05',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BCC',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_BCC(): pass

    label('loc_BCC')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BF2',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_BF2(): pass

    label('loc_BF2')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C18',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_C18(): pass

    label('loc_C18')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C3F',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_C3F(): pass

    label('loc_C3F')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C65',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_C65(): pass

    label('loc_C65')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C8B',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_C8B(): pass

    label('loc_C8B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CB0',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_CB0(): pass

    label('loc_CB0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CD5',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CE9')

    def _loc_CD5(): pass

    label('loc_CD5')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CE9(): pass

    label('loc_CE9')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E02',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF3',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111259V#580F（糟糕……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111260V#017F（被发现了吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF3(): pass

    label('loc_DF3')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 106, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_E02(): pass

    label('loc_E02')

    Jump('func_08_B99')

    def _loc_E05(): pass

    label('loc_E05')

    Return()

# id: 0x0009 offset: 0xE06
@scena.Code('func_09_E06')
def func_09_E06():
    EventBegin(0x00)
    CameraMove(17700, 510, 43970, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6E(262, 0)
    OP_6C(90000, 0)
    ChrSetPos(0x0101, 17540, 510, 44210, 270)
    ChrSetPos(0x0102, 17540, 510, 43360, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010111253V#004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E96')
    def lambda_0E96():
        OP_6C(45000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E96)

    CameraMove(4010, 0, 38720, 3000)
    ChrSetPos(0x0101, 13280, 250, 49870, 225)
    ChrSetPos(0x0102, 14070, 250, 49980, 225)
    Sleep(1000)

    CameraMove(13610, 250, 50130, 3000)

    ChrTalk(
        0x0102,
        (
            '#0020111254V#012F（巡逻好像已经开始了呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111255V（如果被士兵发现了\n',
            '　就会被送回旅馆……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111256V（尽量避开士兵的巡逻视线，\n',
            '　不被他们发现而到达大圣堂。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111257V#006F（嗯，ＯＫ！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0xFC0
@scena.Code('func_0A_FC0')
def func_0A_FC0():
    OP_13(0x00B4)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
