import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0412_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0412   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0412.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT06/CH20031._CH', 'ED6_DT06/CH20031P._CP'),
        ('ED6_DT09/CH10070._CH', 'ED6_DT09/CH10070P._CP'),
        ('ED6_DT09/CH10071._CH', 'ED6_DT09/CH10071P._CP'),
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT09/CH10041._CH', 'ED6_DT09/CH10041P._CP'),
        ('ED6_DT09/CH10150._CH', 'ED6_DT09/CH10150P._CP'),
        ('ED6_DT09/CH10151._CH', 'ED6_DT09/CH10151P._CP'),
    ]

# id: 0x10001 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '鲁克',
            x                   = 0,
            z                   = 0,
            y                   = 19000,
            direction           = 0,
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
            name                = '帕特',
            x                   = 3000,
            z                   = 0,
            y                   = 19000,
            direction           = 0,
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
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
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
    )

# id: 0x10002 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -18100,
            z           = 0,
            y           = 110,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0031,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 18020,
            z           = 0,
            y           = 10,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0032,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x322
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x322
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x322
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_32E'),
        (-1, 'loc_340'),
    )

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 7, 0x217)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33D',
    )

    SetScenaFlags(ScenaFlag(0x0042, 7, 0x217))
    Event(0, func_03_358)

    def _loc_33D(): pass

    label('loc_33D')

    Jump('loc_340')

    def _loc_340(): pass

    label('loc_340')

    Return()

# id: 0x0001 offset: 0x341
@scena.Code('func_01_341')
def func_01_341():
    Return()

# id: 0x0002 offset: 0x342
@scena.Code('func_02_342')
def func_02_342():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_357',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_342')

    def _loc_357(): pass

    label('loc_357')

    Return()

# id: 0x0003 offset: 0x358
@scena.Code('func_03_358')
def func_03_358():
    EventBegin(0x00)
    FormationAddMember(0x3F, 0xFF)
    FormationAddMember(0x40, 0xFF)
    ChrSetFlags(0x0140, 0x0080)
    ChrSetFlags(0x0141, 0x0080)
    FadeIn(2000, 0)
    CameraMove(20, 500, 21100, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_6E(275, 0)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetPos(0x0101, -680, 250, 20560, 180)
    ChrSetPos(0x0102, 630, 250, 20650, 180)
    ChrSetPos(0x0008, -3860, 0, -3700, 45)
    ChrSetPos(0x0009, -2850, 0, -4300, 45)
    ChrSetPos(0x000A, -2830, 0, 1630, 180)
    ChrSetPos(0x000B, -2120, 0, 2880, 209)
    ChrSetPos(0x000C, -1510, 0, -250, 192)
    ChrSetPos(0x000D, 840, 0, 1810, 201)
    ChrSetPos(0x000E, 1750, 0, -1350, 180)
    ChrTurnDirection(0x000A, 0x0008, 0)
    ChrTurnDirection(0x000B, 0x0008, 0)
    ChrTurnDirection(0x000C, 0x0008, 0)
    ChrTurnDirection(0x000D, 0x0008, 0)
    ChrTurnDirection(0x000E, 0x0008, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    OP_6E(262, 2500)
    OP_0D()

    NpcTalk(
        0x0008,
        '鲁克的声音',
        (
            '#0850000946V#1S呜哇哇哇～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '帕特的声音',
        (
            '#0860000947V#1S救、救命啊——！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

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
        10,
        0,
        (
            TXT(0x00, '【自己一口气冲进去】\n'),
            TXT(0x01, '【和约修亚一起出击】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5A3'),
        (0x00000001, 'loc_1043'),
        (-1, 'loc_19EF'),
    )

    def _loc_5A3(): pass

    label('loc_5A3')

    OP_28(0x0001, 0x01, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010000948V#005F我要进去救他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 5)
    Sleep(500)

    @scena.Lambda('lambda_05E0')
    def lambda_05E0():
        ChrWalkTo(0x00FE, -800, 0, 3090, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05E0)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020000949V#012F艾丝蒂尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000950V#012F老是这么冲动，真拿你没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 7)
    Sleep(500)

    @scena.Lambda('lambda_0673')
    def lambda_0673():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0673)

    CreateThread(0x000A, 0x03, 0x00, func_02_342)
    Sleep(100)

    CreateThread(0x000B, 0x03, 0x00, func_02_342)
    Sleep(200)

    @scena.Lambda('lambda_06A6')
    def lambda_06A6():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06A6)

    CreateThread(0x000C, 0x03, 0x00, func_02_342)
    Sleep(100)

    CreateThread(0x000D, 0x03, 0x00, func_02_342)
    Sleep(200)

    CreateThread(0x000E, 0x03, 0x00, func_02_342)
    Sleep(500)

    @scena.Lambda('lambda_06E5')
    def lambda_06E5():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_06E5)

    @scena.Lambda('lambda_06F3')
    def lambda_06F3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_06F3)

    ChrSetFlags(0x0102, 0x0080)
    TerminateThread(0x0101, 0xFF)
    Fade(1000)
    CameraMove(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    ChrSetPos(0x0101, 1090, 0, 9990, 66)

    @scena.Lambda('lambda_075D')
    def lambda_075D():
        CameraMove(-3060, 0, -2370, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_075D)

    @scena.Lambda('lambda_0775')
    def lambda_0775():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0775)

    Sleep(100)

    @scena.Lambda('lambda_0790')
    def lambda_0790():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0790)

    Sleep(100)

    @scena.Lambda('lambda_07AB')
    def lambda_07AB():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_07AB)

    @scena.Lambda('lambda_07C1')
    def lambda_07C1():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07C1)

    Sleep(100)

    @scena.Lambda('lambda_07DC')
    def lambda_07DC():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000578, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_07DC)

    Sleep(1000)

    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0809')
    def lambda_0809():
        ChrMoveTo(0x00FE, -4470, 0, -4480, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0809)

    Sleep(500)

    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_083B')
    def lambda_083B():
        ChrMoveTo(0x00FE, -3430, 0, -5380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_083B)

    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0850000951V滚、滚开呀，你们这些怪物～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0860000952V呜哇哇哇～\n',
            '不要过来啊，笨蛋——！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000953V#10A喝啊～～！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(300)

    @scena.Lambda('lambda_08E5')
    def lambda_08E5():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_08E5)

    @scena.Lambda('lambda_08F3')
    def lambda_08F3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_08F3)

    @scena.Lambda('lambda_0901')
    def lambda_0901():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0901)

    @scena.Lambda('lambda_090F')
    def lambda_090F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_090F)

    @scena.Lambda('lambda_091D')
    def lambda_091D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_091D)

    @scena.Lambda('lambda_092B')
    def lambda_092B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_092B)

    @scena.Lambda('lambda_0939')
    def lambda_0939():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0939)

    Sleep(300)

    @scena.Lambda('lambda_094C')
    def lambda_094C():
        ChrWalkTo(0x00FE, -1170, 0, 2290, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_094C)

    @scena.Lambda('lambda_0967')
    def lambda_0967():
        CameraMove(-2220, 0, -1110, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0967)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_0984')
    def lambda_0984():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_0984')

    DispatchAsync2(0x000A, 0x0002, lambda_0984)

    @scena.Lambda('lambda_0995')
    def lambda_0995():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_0995')

    DispatchAsync2(0x000B, 0x0002, lambda_0995)

    @scena.Lambda('lambda_09A6')
    def lambda_09A6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09A6')

    DispatchAsync2(0x000C, 0x0002, lambda_09A6)

    @scena.Lambda('lambda_09B7')
    def lambda_09B7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09B7')

    DispatchAsync2(0x000D, 0x0002, lambda_09B7)

    @scena.Lambda('lambda_09C8')
    def lambda_09C8():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09C8')

    DispatchAsync2(0x000E, 0x0002, lambda_09C8)

    @scena.Lambda('lambda_09D9')
    def lambda_09D9():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09D9')

    DispatchAsync2(0x0009, 0x0002, lambda_09D9)

    @scena.Lambda('lambda_09EA')
    def lambda_09EA():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09EA')

    DispatchAsync2(0x0008, 0x0002, lambda_09EA)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 10)
    ChrSetFlags(0x0101, 0x1000)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_0A15')
    def lambda_0A15():
        OP_99(0x00FE, 0x00, 0x0C, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A15)

    ChrSetDirection(0x0101, 270, 0)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0101, -2009, 0, -1880, 2000, 6000)
    PlaySE(164, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0A82')
    def lambda_0A82():
        ChrMoveTo(0x00FE, -4090, 0, -1570, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0A82)

    @scena.Lambda('lambda_0A9D')
    def lambda_0A9D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A9D)

    @scena.Lambda('lambda_0AB3')
    def lambda_0AB3():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0AB3)

    Sleep(150)

    @scena.Lambda('lambda_0ACE')
    def lambda_0ACE():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0ACE)

    Sleep(100)

    @scena.Lambda('lambda_0AE9')
    def lambda_0AE9():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0AE9)

    Sleep(200)

    @scena.Lambda('lambda_0B04')
    def lambda_0B04():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0B04)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 5)

    @scena.Lambda('lambda_0B2A')
    def lambda_0B2A():
        ChrSetDirection(0x00FE, 19, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B2A)

    @scena.Lambda('lambda_0B38')
    def lambda_0B38():
        ChrMoveTo(0x00FE, -2780, 0, -3040, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B38)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0850000954V艾丝蒂尔姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000955V#005F你们两个！\n',
            '这里太危险了，快躲到旁边去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BB8')
    def lambda_0BB8():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0BB8)

    @scena.Lambda('lambda_0BC6')
    def lambda_0BC6():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0BC6)

    @scena.Lambda('lambda_0BD4')
    def lambda_0BD4():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0BD4)

    @scena.Lambda('lambda_0BE2')
    def lambda_0BE2():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0BE2)

    @scena.Lambda('lambda_0BF0')
    def lambda_0BF0():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0BF0)

    @scena.Lambda('lambda_0BFE')
    def lambda_0BFE():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0BFE)

    @scena.Lambda('lambda_0C0C')
    def lambda_0C0C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0C0C)

    ChrClearFlags(0x0102, 0x0080)
    ChrSetFlags(0x0102, 0x1000)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 7)
    ChrTurnDirection(0x0102, 0x0101, 0)
    ChrJumpTo(0x0102, -370, 0, 2200, 1000, 7000)
    PlaySE(164, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 9)
    OP_99(0x0102, 0x00, 0x05, 2500)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_0C75')
    def lambda_0C75():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C75')

    DispatchAsync2(0x000A, 0x0002, lambda_0C75)

    @scena.Lambda('lambda_0C86')
    def lambda_0C86():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C86')

    DispatchAsync2(0x000B, 0x0002, lambda_0C86)

    @scena.Lambda('lambda_0C97')
    def lambda_0C97():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C97')

    DispatchAsync2(0x000C, 0x0002, lambda_0C97)

    @scena.Lambda('lambda_0CA8')
    def lambda_0CA8():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0CA8')

    DispatchAsync2(0x000D, 0x0002, lambda_0CA8)

    @scena.Lambda('lambda_0CB9')
    def lambda_0CB9():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0CB9')

    DispatchAsync2(0x000E, 0x0002, lambda_0CB9)

    @scena.Lambda('lambda_0CCA')
    def lambda_0CCA():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0CCA')

    DispatchAsync2(0x0009, 0x0002, lambda_0CCA)

    @scena.Lambda('lambda_0CDB')
    def lambda_0CDB():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0CDB')

    DispatchAsync2(0x0008, 0x0002, lambda_0CDB)

    @scena.Lambda('lambda_0CEC')
    def lambda_0CEC():
        OP_99(0x00FE, 0x05, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0CEC)

    @scena.Lambda('lambda_0CFC')
    def lambda_0CFC():
        ChrWalkTo(0x00FE, -40, 0, -910, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0CFC)

    Sleep(100)

    @scena.Lambda('lambda_0D1C')
    def lambda_0D1C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1200)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0D1C)

    ChrSetFlags(0x0102, 0x0040)
    PlayEffect(0x08, 0xFF, 0x00FF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0102, 0xFF)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 7)

    @scena.Lambda('lambda_0D81')
    def lambda_0D81():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D81)

    ChrJumpTo(0x0102, -1930, 0, -3170, 500, 7000)
    PlaySE(164, 0x00, 0x64)

    ChrTalk(
        0x0009,
        (
            '#0860000956V是约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000957V#012F#4P艾丝蒂尔……\n',
            '知不知道自己一个人冲进来很危险的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000958V#006F要训我的话等战斗结束后再说！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000959V来吧，一口气把这些魔兽通通收拾掉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Battle(0x00000386, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_E9C'),
        (-1, 'loc_EA1'),
    )

    def _loc_E9C(): pass

    label('loc_E9C')

    OP_B4(0x00)

    Jump('loc_EA1')

    def _loc_EA1(): pass

    label('loc_EA1')

    ChrSetFlags(0x0140, 0x0080)
    ChrSetFlags(0x0141, 0x0080)
    EventBegin(0x00)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    CameraMove(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    CameraSetDistance(1710, 0)
    OP_6E(554, 0)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetDirection(0x0008, 28, 0)
    ChrSetDirection(0x0009, 28, 0)
    ChrSetPos(0x0101, -3210, 0, -460, 291)
    ChrSetPos(0x0102, -50, 0, -1270, 72)

    @scena.Lambda('lambda_0F3A')
    def lambda_0F3A():
        OP_6E(504, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F3A)

    OP_6C(225000, 3000)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000960V#502F大获全胜，大获全胜☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000961V#017F真的大获全胜吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000962V还没看清情况\n',
            '就那么莽撞地冲进来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000963V#001F算了～算了。\n',
            '我们不是打了一场漂亮的战斗嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19EF')

    def _loc_1043(): pass

    label('loc_1043')

    OP_28(0x0001, 0x01, 0x0008)
    OP_2B(0x0001, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010000964V#005F约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000965V#012F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 5)
    Sleep(250)

    ChrSetChipByIndex(0x0102, 7)
    Sleep(250)

    @scena.Lambda('lambda_10A4')
    def lambda_10A4():
        ChrWalkTo(0x00FE, -800, 0, 3090, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10A4)

    Sleep(250)

    @scena.Lambda('lambda_10C4')
    def lambda_10C4():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10C4)

    CreateThread(0x000A, 0x03, 0x00, func_02_342)
    Sleep(100)

    CreateThread(0x000B, 0x03, 0x00, func_02_342)
    Sleep(200)

    @scena.Lambda('lambda_10F7')
    def lambda_10F7():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10F7)

    CreateThread(0x000C, 0x03, 0x00, func_02_342)
    Sleep(100)

    CreateThread(0x000D, 0x03, 0x00, func_02_342)
    Sleep(200)

    CreateThread(0x000E, 0x03, 0x00, func_02_342)
    Sleep(500)

    @scena.Lambda('lambda_1136')
    def lambda_1136():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1136)

    @scena.Lambda('lambda_1144')
    def lambda_1144():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1144)

    ChrSetFlags(0x0102, 0x0080)
    TerminateThread(0x0101, 0xFF)
    Fade(1000)
    CameraMove(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    ChrSetPos(0x0101, 1090, 0, 9990, 66)

    @scena.Lambda('lambda_11AE')
    def lambda_11AE():
        CameraMove(-3060, 0, -2370, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_11AE)

    @scena.Lambda('lambda_11C6')
    def lambda_11C6():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11C6)

    Sleep(100)

    @scena.Lambda('lambda_11E1')
    def lambda_11E1():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_11E1)

    Sleep(100)

    @scena.Lambda('lambda_11FC')
    def lambda_11FC():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11FC)

    @scena.Lambda('lambda_1212')
    def lambda_1212():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1212)

    Sleep(100)

    @scena.Lambda('lambda_122D')
    def lambda_122D():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000578, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_122D)

    Sleep(1000)

    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_125A')
    def lambda_125A():
        ChrMoveTo(0x00FE, -4470, 0, -4480, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_125A)

    Sleep(500)

    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_128C')
    def lambda_128C():
        ChrMoveTo(0x00FE, -3430, 0, -5380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_128C)

    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0850000966V滚、滚开呀，你们这些怪物～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0860000967V呜哇哇哇～\n',
            '不要过来啊，笨蛋——！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000968V#10A喝啊～～！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(300)

    @scena.Lambda('lambda_1336')
    def lambda_1336():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1336)

    @scena.Lambda('lambda_1344')
    def lambda_1344():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1344)

    @scena.Lambda('lambda_1352')
    def lambda_1352():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1352)

    @scena.Lambda('lambda_1360')
    def lambda_1360():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1360)

    @scena.Lambda('lambda_136E')
    def lambda_136E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_136E)

    @scena.Lambda('lambda_137C')
    def lambda_137C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_137C)

    @scena.Lambda('lambda_138A')
    def lambda_138A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_138A)

    Sleep(300)

    @scena.Lambda('lambda_139D')
    def lambda_139D():
        ChrWalkTo(0x00FE, -1170, 0, 2290, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_139D)

    @scena.Lambda('lambda_13B8')
    def lambda_13B8():
        CameraMove(-2220, 0, -1110, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13B8)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_13D5')
    def lambda_13D5():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_13D5')

    DispatchAsync2(0x000A, 0x0002, lambda_13D5)

    @scena.Lambda('lambda_13E6')
    def lambda_13E6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_13E6')

    DispatchAsync2(0x000B, 0x0002, lambda_13E6)

    @scena.Lambda('lambda_13F7')
    def lambda_13F7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_13F7')

    DispatchAsync2(0x000C, 0x0002, lambda_13F7)

    @scena.Lambda('lambda_1408')
    def lambda_1408():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1408')

    DispatchAsync2(0x000D, 0x0002, lambda_1408)

    @scena.Lambda('lambda_1419')
    def lambda_1419():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1419')

    DispatchAsync2(0x000E, 0x0002, lambda_1419)

    @scena.Lambda('lambda_142A')
    def lambda_142A():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_142A')

    DispatchAsync2(0x0009, 0x0002, lambda_142A)

    @scena.Lambda('lambda_143B')
    def lambda_143B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_143B')

    DispatchAsync2(0x0008, 0x0002, lambda_143B)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 10)
    ChrSetFlags(0x0101, 0x1000)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_1466')
    def lambda_1466():
        OP_99(0x00FE, 0x00, 0x0C, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1466)

    ChrSetDirection(0x0101, 270, 0)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0101, -2009, 0, -1880, 2000, 6000)
    PlaySE(164, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_14D3')
    def lambda_14D3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_14D3)

    @scena.Lambda('lambda_14E5')
    def lambda_14E5():
        ChrMoveTo(0x00FE, -4090, 0, -1570, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_14E5)

    @scena.Lambda('lambda_1500')
    def lambda_1500():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1500)

    @scena.Lambda('lambda_1516')
    def lambda_1516():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1516)

    Sleep(150)

    @scena.Lambda('lambda_1531')
    def lambda_1531():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1531)

    Sleep(100)

    @scena.Lambda('lambda_154C')
    def lambda_154C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_154C)

    Sleep(200)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 5)

    @scena.Lambda('lambda_1577')
    def lambda_1577():
        ChrSetDirection(0x00FE, 19, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1577)

    @scena.Lambda('lambda_1585')
    def lambda_1585():
        ChrMoveTo(0x00FE, -2780, 0, -3040, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1585)

    @scena.Lambda('lambda_15A0')
    def lambda_15A0():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_15A0)

    @scena.Lambda('lambda_15AE')
    def lambda_15AE():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_15AE)

    @scena.Lambda('lambda_15BC')
    def lambda_15BC():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_15BC)

    @scena.Lambda('lambda_15CA')
    def lambda_15CA():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_15CA)

    @scena.Lambda('lambda_15D8')
    def lambda_15D8():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_15D8)

    @scena.Lambda('lambda_15E6')
    def lambda_15E6():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_15E6)

    ChrClearFlags(0x0102, 0x0080)
    ChrSetFlags(0x0102, 0x1000)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 7)
    ChrTurnDirection(0x0102, 0x0101, 0)
    ChrJumpTo(0x0102, -370, 0, 2200, 1000, 7000)
    PlaySE(164, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 9)
    OP_99(0x0102, 0x00, 0x05, 2500)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_164F')
    def lambda_164F():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_164F')

    DispatchAsync2(0x000A, 0x0002, lambda_164F)

    @scena.Lambda('lambda_1660')
    def lambda_1660():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1660')

    DispatchAsync2(0x000B, 0x0002, lambda_1660)

    @scena.Lambda('lambda_1671')
    def lambda_1671():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1671')

    DispatchAsync2(0x000C, 0x0002, lambda_1671)

    @scena.Lambda('lambda_1682')
    def lambda_1682():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1682')

    DispatchAsync2(0x000D, 0x0002, lambda_1682)

    @scena.Lambda('lambda_1693')
    def lambda_1693():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1693')

    DispatchAsync2(0x000E, 0x0002, lambda_1693)

    @scena.Lambda('lambda_16A4')
    def lambda_16A4():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_16A4')

    DispatchAsync2(0x0009, 0x0002, lambda_16A4)

    @scena.Lambda('lambda_16B5')
    def lambda_16B5():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_16B5')

    DispatchAsync2(0x0008, 0x0002, lambda_16B5)

    @scena.Lambda('lambda_16C6')
    def lambda_16C6():
        OP_99(0x00FE, 0x05, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_16C6)

    @scena.Lambda('lambda_16D6')
    def lambda_16D6():
        ChrWalkTo(0x00FE, -40, 0, -910, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16D6)

    Sleep(100)

    @scena.Lambda('lambda_16F6')
    def lambda_16F6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1200)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_16F6)

    ChrSetFlags(0x0102, 0x0040)
    PlayEffect(0x08, 0xFF, 0x00FF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0102, 0xFF)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 7)

    @scena.Lambda('lambda_175B')
    def lambda_175B():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_175B)

    ChrJumpTo(0x0102, -1930, 0, -3170, 500, 7000)
    PlaySE(164, 0x00, 0x64)

    ChrTalk(
        0x0008,
        (
            '#0850000969V艾丝蒂尔姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0860000970V是约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000971V#005F你们两个！\n',
            '这里太危险了，快躲到旁边去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000972V#012F#4P我们会马上收拾它们的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Battle(0x000003B0, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1858'),
        (-1, 'loc_185D'),
    )

    def _loc_1858(): pass

    label('loc_1858')

    OP_B4(0x00)

    Jump('loc_185D')

    def _loc_185D(): pass

    label('loc_185D')

    EventBegin(0x00)
    ChrSetFlags(0x0140, 0x0080)
    ChrSetFlags(0x0141, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    CameraMove(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    CameraSetDistance(1710, 0)
    OP_6E(554, 0)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetDirection(0x0008, 28, 0)
    ChrSetDirection(0x0009, 28, 0)
    ChrSetPos(0x0101, -3210, 0, -460, 291)
    ChrSetPos(0x0102, -50, 0, -1270, 72)

    @scena.Lambda('lambda_18F6')
    def lambda_18F6():
        OP_6E(504, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18F6)

    OP_6C(225000, 3000)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000973V#001F好啦，都收拾掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000974V#019F嗯，大家都没事，太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000975V#010F而且我们联合出击的时机\n',
            '也掌握得很不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000976V#008F嘿嘿，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19EF')

    def _loc_19EF(): pass

    label('loc_19EF')

    ChrTalk(
        0x0009,
        (
            '#0860000977V结、结束了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A19')
    def lambda_1A19():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A19)

    @scena.Lambda('lambda_1A27')
    def lambda_1A27():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1A27)

    ChrTalk(
        0x0008,
        (
            '#0850000978V厉害～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A51')
    def lambda_1A51():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1A51')

    DispatchAsync2(0x0008, 0x0001, lambda_1A51)

    @scena.Lambda('lambda_1A62')
    def lambda_1A62():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1A62')

    DispatchAsync2(0x0101, 0x0001, lambda_1A62)

    @scena.Lambda('lambda_1A73')
    def lambda_1A73():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1A73')

    DispatchAsync2(0x0102, 0x0001, lambda_1A73)

    OP_62(0x0008, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrJumpToRelative(0x0008, 0, 0, 0, 700, 6000)
    ChrJumpToRelative(0x0008, 0, 0, 0, 700, 6000)
    Sleep(300)

    @scena.Lambda('lambda_1AC9')
    def lambda_1AC9():
        ChrWalkTo(0x00FE, -3690, 0, -1560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1AC9)

    Sleep(300)

    @scena.Lambda('lambda_1AE9')
    def lambda_1AE9():
        CameraMove(-3440, 0, -2740, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1AE9)

    Sleep(100)

    @scena.Lambda('lambda_1B06')
    def lambda_1B06():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1B06')

    DispatchAsync2(0x0009, 0x0001, lambda_1B06)

    @scena.Lambda('lambda_1B17')
    def lambda_1B17():
        ChrWalkTo(0x00FE, -1020, 0, -3170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1B17)

    WaitForThreadExit(0x0008, 0x0002)
    ChrJumpTo(0x0008, -4500, 0, -1030, 800, 6000)
    ChrJumpTo(0x0008, -4250, 0, -190, 1200, 6000)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0850000979V艾丝蒂尔，你还蛮厉害的嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0850000980V虽然只是个小女孩，不过还真有一手啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000981V#005F你这个笨蛋！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C0B')
    def lambda_1C0B():
        CameraMove(-4540, 0, -1610, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1C0B)

    ChrSetFlags(0x0101, 0x0040)
    OP_92(0x0101, 0x0008, 400, 6000, 0x00)
    PlaySE(125, 0x00, 0x64)
    OP_94(0x01, 0x0008, 0x00B4, 0x000001F4, 0x00001770, 0x00)
    Sleep(500)

    ChrMoveTo(0x0008, -5750, 0, 20, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0850000982V好疼，你干什么呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000983V#009F真是的，你呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000984V居然把这么乖的帕特\n',
            '都带到这种地方来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1300)

    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    TerminateThread(0x0008, 0xFF)

    @scena.Lambda('lambda_1D13')
    def lambda_1D13():
        ChrSetDirection(0x00FE, 270, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D13)

    @scena.Lambda('lambda_1D21')
    def lambda_1D21():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000005DC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1D21)

    ChrClearFlags(0x0101, 0x1000)
    ChrMoveTo(0x0101, -6730, 0, 270, 5000, 0x00)
    ChrSetFlags(0x0008, 0x0004)
    ChrMoveToRelativeAsync(0x0008, 0, 100, 0, 800, 0x00)

    @scena.Lambda('lambda_1D69')
    def lambda_1D69():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D69)

    OP_97(0x0008, -6730, 270, -180000, 4000, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010000985V#005F给·我·好·好·反·省！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DBB')
    def lambda_1DBB():
        ChrMoveToRelativeAsync(0x00FE, 1200, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DBB)

    ChrMoveToRelativeAsync(0x0008, 1200, 0, 0, 2000, 0x00)
    OP_9E(0x0008, 60, 0, 300, 8000)
    OP_9E(0x0008, 60, 0, 300, 8000)

    ChrTalk(
        0x0008,
        (
            '#0850000986V疼疼疼，快住手！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0850000987V粗暴女！白痴艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000988V#009F而且还用这种口气\n',
            '对你的救命恩人说话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000989V#009F看来不给你点严厉的惩罚是不行的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 60, 0, 500, 8000)

    ChrTalk(
        0x0008,
        (
            '#0850000990V疼疼疼疼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0850000991V艾丝蒂尔姐姐！\n',
            '饶了我吧，都是我不好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F33')
    def lambda_1F33():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_1F33')

    DispatchAsync2(0x0008, 0x0003, lambda_1F33)

    ChrTalk(
        0x0009,
        (
            '#0860000992V#1P那、那个……姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0860000993V#1P这样就够了吧，饶了他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000A, 11)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -16000, 0, 0, 282)

    @scena.Lambda('lambda_1FB5')
    def lambda_1FB5():
        ChrWalkTo(0x00FE, -11000, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1FB5)

    ChrTalk(
        0x0101,
        (
            '#0010000994V#006F没关系的，对这样的调皮蛋来说\n',
            '小小的惩罚反而有好处……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0001)
    ChrTurnDirection(0x000A, 0x0101, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrClearFlags(0x0101, 0x1000)

    ChrTalk(
        0x0102,
        (
            '#0020000995V#016F艾丝蒂尔，后面！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000996V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0101, 0xFF)
    ChrClearFlags(0x0008, 0x0004)
    ChrTurnDirection(0x0101, 0x000A, 400)
    ChrTurnDirection(0x0008, 0x0101, 400)

    @scena.Lambda('lambda_20A8')
    def lambda_20A8():
        CameraMove(-6670, 0, -1080, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_20A8)

    @scena.Lambda('lambda_20C0')
    def lambda_20C0():
        ChrWalkTo(0x00FE, -9500, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_20C0)

    Sleep(1500)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000997V#002F糟了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'battle\\\\mgblood.eff')

    ChrTalk(
        0x0102,
        (
            '#0020000998V#510F#4P……该死！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0102, 0x00, 0x00, func_04_2C86)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x0012, 0x0004)
    ChrSetFlags(0x0013, 0x0004)
    ChrSetFlags(0x0014, 0x0004)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetPos(0x0011, -21000, 0, 0, 0)
    ChrSetPos(0x0012, -21040, 0, 0, 0)
    ChrSetPos(0x0013, -21040, 0, 0, 0)
    ChrSetPos(0x0014, -21040, 0, 0, 0)
    ChrSetPos(0x0010, -21040, 0, 0, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 200, 0)
    ChrSetRGBAMask(0x0012, 255, 255, 255, 150, 0)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 100, 0)
    ChrSetRGBAMask(0x0014, 255, 255, 255, 50, 0)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 12)

    @scena.Lambda('lambda_2232')
    def lambda_2232():
        ChrWalkTo(0x000A, -5500, 0, 0, 2700, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2232)

    @scena.Lambda('lambda_224D')
    def lambda_224D():
        CameraMove(-5130, 0, -1080, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_224D)

    @scena.Lambda('lambda_2265')
    def lambda_2265():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2265)

    @scena.Lambda('lambda_227B')
    def lambda_227B():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_227B)

    ChrSetFlags(0x0010, 0x0002)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetFlags(0x0012, 0x0002)
    ChrSetFlags(0x0013, 0x0002)
    ChrSetFlags(0x0014, 0x0002)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0011, 0)
    ChrSetSubChip(0x0012, 0)
    ChrSetSubChip(0x0013, 0)
    ChrSetSubChip(0x0014, 0)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetFlags(0x0012, 0x0020)
    ChrSetFlags(0x0013, 0x0020)
    ChrSetFlags(0x0014, 0x0020)
    ChrSetChipByIndex(0x0010, 13)
    ChrSetChipByIndex(0x0011, 13)
    ChrSetChipByIndex(0x0012, 13)
    ChrSetChipByIndex(0x0013, 13)
    ChrSetChipByIndex(0x0014, 13)

    @scena.Lambda('lambda_22F5')
    def lambda_22F5():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_22F5)

    Sleep(100)

    @scena.Lambda('lambda_2315')
    def lambda_2315():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2315)

    Sleep(100)

    @scena.Lambda('lambda_2335')
    def lambda_2335():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2335)

    Sleep(100)

    @scena.Lambda('lambda_2355')
    def lambda_2355():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2355)

    Sleep(100)

    @scena.Lambda('lambda_2375')
    def lambda_2375():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_2375)

    OP_20(0x000003E8)
    WaitForThreadExit(0x0010, 0x0001)
    CreateThread(0x0011, 0x01, 0x00, func_06_2D04)
    CreateThread(0x0012, 0x01, 0x00, func_07_2D63)
    CreateThread(0x0013, 0x01, 0x00, func_08_2DC2)
    CreateThread(0x0014, 0x01, 0x00, func_09_2E21)
    ChrSetSubChip(0x0010, 1)
    ChrJumpTo(0x0010, -7700, 0, 1500, 1200, 10000)
    PlaySE(164, 0x00, 0x64)
    CreateThread(0x0010, 0x01, 0x00, func_05_2CBC)
    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(155, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x09, 0xFF, 0x00FF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x00, 0xFF, 0x00FF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x000A, 0x0040)

    @scena.Lambda('lambda_2496')
    def lambda_2496():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2496)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000999V#004F……啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0010, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020001000V#010F太好了，终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2511')
    def lambda_2511():
        OP_6C(270000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2511)

    @scena.Lambda('lambda_2521')
    def lambda_2521():
        CameraMove(-5500, 0, 0, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2521)

    Sleep(1300)

    ChrSetSubChip(0x0010, 4)
    Sleep(1200)

    @scena.Lambda('lambda_2548')
    def lambda_2548():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2548)

    @scena.Lambda('lambda_2556')
    def lambda_2556():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2556)

    @scena.Lambda('lambda_2564')
    def lambda_2564():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2564)

    PlayBGM(88)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0160001001V#085F还是太嫩了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001002V为了防备难以预见的威胁，\n',
            '必须时常保持敏锐的感觉才行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001003V#080F这也是游击士的心得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2612')
    def lambda_2612():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_2612')

    DispatchAsync2(0x0101, 0x0001, lambda_2612)

    ChrTalk(
        0x0101,
        (
            '#0010001004V#004F#4P老、老爸！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001005V为、为什么你会在这儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0160001006V#080F没什么，爱娜把事情都告诉我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001007V虽然前往目的地的速度\n',
            '和处事的判断力都相当不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001008V不过最后还是松懈了啊，知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001009V#007F#4P哎呀，真没面子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_273B')
    def lambda_273B():
        CameraMove(-6270, 0, 130, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_273B)

    @scena.Lambda('lambda_2753')
    def lambda_2753():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_2753')

    DispatchAsync2(0x0008, 0x0001, lambda_2753)

    @scena.Lambda('lambda_2764')
    def lambda_2764():
        ChrMoveTo(0x00FE, -4400, 0, 1530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2764)

    @scena.Lambda('lambda_277F')
    def lambda_277F():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_277F')

    DispatchAsync2(0x0009, 0x0001, lambda_277F)

    @scena.Lambda('lambda_2790')
    def lambda_2790():
        ChrMoveTo(0x00FE, -2590, 0, -1600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2790)

    ChrWalkTo(0x0102, -4720, 0, -750, 3000, 0x00)
    TerminateThread(0x0102, 0xFF)
    ChrSetDirection(0x0102, 315, 400)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020001010V#013F多亏您来了，爸爸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001011V对不起，有我在还发生这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0160001012V#081F啊，要做到真正保护好别人，\n',
            '其实你也还差得远呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001013V不过再努力一下就会好很多的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001014V#011F……嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0160001015V#080F那我们回去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001016V孩子们，还走得动吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0860001017V嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2916')
    def lambda_2916():
        ChrWalkTo(0x00FE, -5700, 0, -1720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2916)

    Sleep(200)

    @scena.Lambda('lambda_2936')
    def lambda_2936():
        ChrWalkTo(0x00FE, -7050, 0, 1000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2936)

    @scena.Lambda('lambda_2951')
    def lambda_2951():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_2951')

    DispatchAsync2(0x0008, 0x0001, lambda_2951)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_2967')
    def lambda_2967():
        ChrWalkTo(0x00FE, -7000, 0, -1050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2967)

    @scena.Lambda('lambda_2982')
    def lambda_2982():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_2982')

    DispatchAsync2(0x0009, 0x0001, lambda_2982)

    WaitForThreadExit(0x0009, 0x0002)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0850001018V太、太有型了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0850001019V卡西乌斯叔叔，\n',
            '你比艾丝蒂尔要酷上一百倍呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0160001020V#081F哈哈哈，那是当然的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001021V好了，那我们回城镇去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0850001022V嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 0)
    ChrClearFlags(0x0010, 0x0002)
    ChrClearFlags(0x0010, 0x0020)
    ChrSetChipByIndex(0x0010, 4)
    ChrSetDirection(0x0010, 90, 0)
    ChrSetDirection(0x0010, 270, 400)

    @scena.Lambda('lambda_2A87')
    def lambda_2A87():
        ChrWalkTo(0x00FE, -37590, 0, -120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2A87)

    Sleep(300)

    @scena.Lambda('lambda_2AA7')
    def lambda_2AA7():
        ChrWalkTo(0x00FE, -37590, 0, -120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2AA7)

    Sleep(100)

    @scena.Lambda('lambda_2AC7')
    def lambda_2AC7():
        ChrWalkTo(0x00FE, -37590, 0, -120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2AC7)

    @scena.Lambda('lambda_2AE2')
    def lambda_2AE2():
        OP_6E(471, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AE2)

    @scena.Lambda('lambda_2AF2')
    def lambda_2AF2():
        OP_6C(224000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2AF2)

    CameraMove(-6000, 0, 290, 2500)
    OP_63(0x0101)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001023V#007F#4P……唔～…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001024V虽然很感谢老爸救了我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001025V可是为什么他会把\n',
            '我的风头全都抢光了啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    ChrSetDirection(0x0101, 45, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010001026V#009F#5S#4P我不要啊——！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001027V#019F哈哈，这也没办法啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001028V#010F不管怎么说……\n',
            '他可是卡西乌斯·布莱特啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_28(0x0001, 0x01, 0x0020)
    FormationDelMember(0x3F, 0xFF)
    FormationDelMember(0x40, 0xFF)
    SetScenaFlags(ScenaFlag(0x0042, 7, 0x217))
    NewScene('ED6_DT01/T0121._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x2C86
@scena.Code('func_04_2C86')
def func_04_2C86():
    ChrClearFlags(0x0102, 0x1000)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 7)
    Sleep(500)

    @scena.Lambda('lambda_2CA6')
    def lambda_2CA6():
        ChrWalkTo(0x00FE, -2560, 0, -940, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2CA6)

    Return()

# id: 0x0005 offset: 0x2CBC
@scena.Code('func_05_2CBC')
def func_05_2CBC():
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x00FE, 3)

    Return()

# id: 0x0006 offset: 0x2D04
@scena.Code('func_06_2D04')
def func_06_2D04():
    Sleep(100)

    ChrSetSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    ChrSetSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    ChrSetFlags(0x0011, 0x0080)

    Return()

# id: 0x0007 offset: 0x2D63
@scena.Code('func_07_2D63')
def func_07_2D63():
    Sleep(200)

    ChrSetSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    ChrSetSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    ChrSetFlags(0x0012, 0x0080)

    Return()

# id: 0x0008 offset: 0x2DC2
@scena.Code('func_08_2DC2')
def func_08_2DC2():
    Sleep(300)

    ChrSetSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    ChrSetSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    ChrSetFlags(0x0013, 0x0080)

    Return()

# id: 0x0009 offset: 0x2E21
@scena.Code('func_09_2E21')
def func_09_2E21():
    Sleep(400)

    ChrSetSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    ChrSetSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    ChrSetFlags(0x0014, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
