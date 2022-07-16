import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0412_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0412   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '鲁克'),
    TXT(0x02, '帕特'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '魔兽'),
    TXT(0x07, '魔兽'),
    TXT(0x08, '魔兽'),
    TXT(0x09, '卡西乌斯'),
    TXT(0x0A, '卡西乌斯'),
    TXT(0x0B, '卡西乌斯'),
    TXT(0x0C, '卡西乌斯'),
    TXT(0x0D, '卡西乌斯'),
    TXT(0x0E, ''),
]

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

# id: 0xFFFF offset: 0x2CF5
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

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
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

# id: 0x10004 offset: 0x322
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x322
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x322
@scena.Code('PreInit')
def PreInit():
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
    Event(0, 0x0003)

    def _loc_33D(): pass

    label('loc_33D')

    Jump('loc_340')

    def _loc_340(): pass

    label('loc_340')

    Return()

# id: 0x0001 offset: 0x341
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x342
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_357',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_357(): pass

    label('loc_357')

    Return()

# id: 0x0003 offset: 0x358
@scena.Code('func_03_358')
def func_03_358():
    EventBegin(0x00)
    FormationAddMember(0x3F, 0xFF)
    FormationAddMember(0x40, 0xFF)
    SetChrFlags(0x0140, 0x0080)
    SetChrFlags(0x0141, 0x0080)
    FadeIn(2000, 0)
    CameraMove(20, 500, 21100, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_6E(275, 0)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrPos(0x0101, -680, 250, 20560, 180)
    SetChrPos(0x0102, 630, 250, 20650, 180)
    SetChrPos(0x0008, -3860, 0, -3700, 45)
    SetChrPos(0x0009, -2850, 0, -4300, 45)
    SetChrPos(0x000A, -2830, 0, 1630, 180)
    SetChrPos(0x000B, -2120, 0, 2880, 209)
    SetChrPos(0x000C, -1510, 0, -250, 192)
    SetChrPos(0x000D, 840, 0, 1810, 201)
    SetChrPos(0x000E, 1750, 0, -1350, 180)
    ChrTurnDirection(0x000A, 0x0008, 0)
    ChrTurnDirection(0x000B, 0x0008, 0)
    ChrTurnDirection(0x000C, 0x0008, 0)
    ChrTurnDirection(0x000D, 0x0008, 0)
    ChrTurnDirection(0x000E, 0x0008, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
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
        (0x00000000, 'loc_599'),
        (0x00000001, 'loc_FE9'),
        (-1, 'loc_1954'),
    )

    def _loc_599(): pass

    label('loc_599')

    OP_28(0x0001, 0x01, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010000948V#005F我要进去救他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 5)
    Sleep(500)

    @scena.Lambda('lambda_05D1')
    def lambda_05D1():
        ChrWalkTo(0x00FE, -800, 0, 3090, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05D1)

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
    SetChrChipByIndex(0x0102, 7)
    Sleep(500)

    @scena.Lambda('lambda_065A')
    def lambda_065A():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_065A)

    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    Sleep(100)

    CreateThread(0x000B, 0x03, 0x00, 0x0002)
    Sleep(200)

    @scena.Lambda('lambda_068D')
    def lambda_068D():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_068D)

    CreateThread(0x000C, 0x03, 0x00, 0x0002)
    Sleep(100)

    CreateThread(0x000D, 0x03, 0x00, 0x0002)
    Sleep(200)

    CreateThread(0x000E, 0x03, 0x00, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_06CC')
    def lambda_06CC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_06CC)

    @scena.Lambda('lambda_06DA')
    def lambda_06DA():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_06DA)

    SetChrFlags(0x0102, 0x0080)
    TerminateThread(0x0101, 0xFF)
    Fade(1000)
    CameraMove(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x0101, 1090, 0, 9990, 66)

    @scena.Lambda('lambda_0744')
    def lambda_0744():
        CameraMove(-3060, 0, -2370, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0744)

    @scena.Lambda('lambda_075C')
    def lambda_075C():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_075C)

    Sleep(100)

    @scena.Lambda('lambda_0777')
    def lambda_0777():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0777)

    Sleep(100)

    @scena.Lambda('lambda_0792')
    def lambda_0792():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0792)

    @scena.Lambda('lambda_07A8')
    def lambda_07A8():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07A8)

    Sleep(100)

    @scena.Lambda('lambda_07C3')
    def lambda_07C3():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000578, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_07C3)

    Sleep(1000)

    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_07F0')
    def lambda_07F0():
        ChrMoveTo(0x00FE, -4470, 0, -4480, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07F0)

    Sleep(500)

    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0822')
    def lambda_0822():
        ChrMoveTo(0x00FE, -3430, 0, -5380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0822)

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

    @scena.Lambda('lambda_08BD')
    def lambda_08BD():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_08BD)

    @scena.Lambda('lambda_08CB')
    def lambda_08CB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_08CB)

    @scena.Lambda('lambda_08D9')
    def lambda_08D9():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_08D9)

    @scena.Lambda('lambda_08E7')
    def lambda_08E7():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_08E7)

    @scena.Lambda('lambda_08F5')
    def lambda_08F5():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_08F5)

    @scena.Lambda('lambda_0903')
    def lambda_0903():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0903)

    @scena.Lambda('lambda_0911')
    def lambda_0911():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0911)

    Sleep(300)

    @scena.Lambda('lambda_0924')
    def lambda_0924():
        ChrWalkTo(0x00FE, -1170, 0, 2290, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0924)

    @scena.Lambda('lambda_093F')
    def lambda_093F():
        CameraMove(-2220, 0, -1110, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_093F)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_095C')
    def lambda_095C():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_095C')

    DispatchAsync2(0x000A, 0x0002, lambda_095C)

    @scena.Lambda('lambda_096D')
    def lambda_096D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_096D')

    DispatchAsync2(0x000B, 0x0002, lambda_096D)

    @scena.Lambda('lambda_097E')
    def lambda_097E():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_097E')

    DispatchAsync2(0x000C, 0x0002, lambda_097E)

    @scena.Lambda('lambda_098F')
    def lambda_098F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_098F')

    DispatchAsync2(0x000D, 0x0002, lambda_098F)

    @scena.Lambda('lambda_09A0')
    def lambda_09A0():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09A0')

    DispatchAsync2(0x000E, 0x0002, lambda_09A0)

    @scena.Lambda('lambda_09B1')
    def lambda_09B1():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09B1')

    DispatchAsync2(0x0009, 0x0002, lambda_09B1)

    @scena.Lambda('lambda_09C2')
    def lambda_09C2():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_09C2')

    DispatchAsync2(0x0008, 0x0002, lambda_09C2)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0101, 10)
    SetChrFlags(0x0101, 0x1000)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_09ED')
    def lambda_09ED():
        OP_99(0x00FE, 0x00, 0x0C, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09ED)

    SetChrDirection(0x0101, 270, 0)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0101, -2009, 0, -1880, 2000, 6000)
    PlaySE(164, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0A5A')
    def lambda_0A5A():
        ChrMoveTo(0x00FE, -4090, 0, -1570, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0A5A)

    @scena.Lambda('lambda_0A75')
    def lambda_0A75():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A75)

    @scena.Lambda('lambda_0A8B')
    def lambda_0A8B():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0A8B)

    Sleep(150)

    @scena.Lambda('lambda_0AA6')
    def lambda_0AA6():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0AA6)

    Sleep(100)

    @scena.Lambda('lambda_0AC1')
    def lambda_0AC1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0AC1)

    Sleep(200)

    @scena.Lambda('lambda_0ADC')
    def lambda_0ADC():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0ADC)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0101, 5)

    @scena.Lambda('lambda_0B02')
    def lambda_0B02():
        SetChrDirection(0x00FE, 19, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B02)

    @scena.Lambda('lambda_0B10')
    def lambda_0B10():
        ChrMoveTo(0x00FE, -2780, 0, -3040, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B10)

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

    @scena.Lambda('lambda_0B86')
    def lambda_0B86():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B86)

    @scena.Lambda('lambda_0B94')
    def lambda_0B94():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0B94)

    @scena.Lambda('lambda_0BA2')
    def lambda_0BA2():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0BA2)

    @scena.Lambda('lambda_0BB0')
    def lambda_0BB0():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0BB0)

    @scena.Lambda('lambda_0BBE')
    def lambda_0BBE():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0BBE)

    @scena.Lambda('lambda_0BCC')
    def lambda_0BCC():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0BCC)

    @scena.Lambda('lambda_0BDA')
    def lambda_0BDA():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0BDA)

    ClearChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0102, 0x1000)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0102, 7)
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

    SetChrChipByIndex(0x0102, 9)
    OP_99(0x0102, 0x00, 0x05, 2500)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_0C43')
    def lambda_0C43():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C43')

    DispatchAsync2(0x000A, 0x0002, lambda_0C43)

    @scena.Lambda('lambda_0C54')
    def lambda_0C54():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C54')

    DispatchAsync2(0x000B, 0x0002, lambda_0C54)

    @scena.Lambda('lambda_0C65')
    def lambda_0C65():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C65')

    DispatchAsync2(0x000C, 0x0002, lambda_0C65)

    @scena.Lambda('lambda_0C76')
    def lambda_0C76():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C76')

    DispatchAsync2(0x000D, 0x0002, lambda_0C76)

    @scena.Lambda('lambda_0C87')
    def lambda_0C87():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C87')

    DispatchAsync2(0x000E, 0x0002, lambda_0C87)

    @scena.Lambda('lambda_0C98')
    def lambda_0C98():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0C98')

    DispatchAsync2(0x0009, 0x0002, lambda_0C98)

    @scena.Lambda('lambda_0CA9')
    def lambda_0CA9():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_0CA9')

    DispatchAsync2(0x0008, 0x0002, lambda_0CA9)

    @scena.Lambda('lambda_0CBA')
    def lambda_0CBA():
        OP_99(0x00FE, 0x05, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0CBA)

    @scena.Lambda('lambda_0CCA')
    def lambda_0CCA():
        ChrWalkTo(0x00FE, -40, 0, -910, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0CCA)

    Sleep(100)

    @scena.Lambda('lambda_0CEA')
    def lambda_0CEA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1200)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0CEA)

    SetChrFlags(0x0102, 0x0040)
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

    SetChrChipByIndex(0x0102, 7)

    @scena.Lambda('lambda_0D4F')
    def lambda_0D4F():
        SetChrDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D4F)

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
        (0x00000001, 'loc_E56'),
        (-1, 'loc_E5B'),
    )

    def _loc_E56(): pass

    label('loc_E56')

    OP_B4(0x00)

    Jump('loc_E5B')

    def _loc_E5B(): pass

    label('loc_E5B')

    SetChrFlags(0x0140, 0x0080)
    SetChrFlags(0x0141, 0x0080)
    EventBegin(0x00)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    CameraMove(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    CameraSetDistance(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrDirection(0x0008, 28, 0)
    SetChrDirection(0x0009, 28, 0)
    SetChrPos(0x0101, -3210, 0, -460, 291)
    SetChrPos(0x0102, -50, 0, -1270, 72)

    @scena.Lambda('lambda_0EF4')
    def lambda_0EF4():
        OP_6E(504, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EF4)

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

    SetChrChipByIndex(0x0101, 65535)
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

    SetChrChipByIndex(0x0102, 65535)
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

    Jump('loc_1954')

    def _loc_FE9(): pass

    label('loc_FE9')

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
    SetChrChipByIndex(0x0101, 5)
    Sleep(250)

    SetChrChipByIndex(0x0102, 7)
    Sleep(250)

    @scena.Lambda('lambda_1040')
    def lambda_1040():
        ChrWalkTo(0x00FE, -800, 0, 3090, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1040)

    Sleep(250)

    @scena.Lambda('lambda_1060')
    def lambda_1060():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1060)

    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    Sleep(100)

    CreateThread(0x000B, 0x03, 0x00, 0x0002)
    Sleep(200)

    @scena.Lambda('lambda_1093')
    def lambda_1093():
        ChrWalkTo(0x00FE, 1090, 0, 9990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1093)

    CreateThread(0x000C, 0x03, 0x00, 0x0002)
    Sleep(100)

    CreateThread(0x000D, 0x03, 0x00, 0x0002)
    Sleep(200)

    CreateThread(0x000E, 0x03, 0x00, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_10D2')
    def lambda_10D2():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_10D2)

    @scena.Lambda('lambda_10E0')
    def lambda_10E0():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_10E0)

    SetChrFlags(0x0102, 0x0080)
    TerminateThread(0x0101, 0xFF)
    Fade(1000)
    CameraMove(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x0101, 1090, 0, 9990, 66)

    @scena.Lambda('lambda_114A')
    def lambda_114A():
        CameraMove(-3060, 0, -2370, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_114A)

    @scena.Lambda('lambda_1162')
    def lambda_1162():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1162)

    Sleep(100)

    @scena.Lambda('lambda_117D')
    def lambda_117D():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_117D)

    Sleep(100)

    @scena.Lambda('lambda_1198')
    def lambda_1198():
        OP_94(0x00, 0x00FE, 0x0000, 0x000007D0, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1198)

    @scena.Lambda('lambda_11AE')
    def lambda_11AE():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000834, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_11AE)

    Sleep(100)

    @scena.Lambda('lambda_11C9')
    def lambda_11C9():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000578, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_11C9)

    Sleep(1000)

    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_11F6')
    def lambda_11F6():
        ChrMoveTo(0x00FE, -4470, 0, -4480, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11F6)

    Sleep(500)

    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_1228')
    def lambda_1228():
        ChrMoveTo(0x00FE, -3430, 0, -5380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1228)

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

    @scena.Lambda('lambda_12C3')
    def lambda_12C3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_12C3)

    @scena.Lambda('lambda_12D1')
    def lambda_12D1():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_12D1)

    @scena.Lambda('lambda_12DF')
    def lambda_12DF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_12DF)

    @scena.Lambda('lambda_12ED')
    def lambda_12ED():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_12ED)

    @scena.Lambda('lambda_12FB')
    def lambda_12FB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_12FB)

    @scena.Lambda('lambda_1309')
    def lambda_1309():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1309)

    @scena.Lambda('lambda_1317')
    def lambda_1317():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1317)

    Sleep(300)

    @scena.Lambda('lambda_132A')
    def lambda_132A():
        ChrWalkTo(0x00FE, -1170, 0, 2290, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_132A)

    @scena.Lambda('lambda_1345')
    def lambda_1345():
        CameraMove(-2220, 0, -1110, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1345)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1362')
    def lambda_1362():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1362')

    DispatchAsync2(0x000A, 0x0002, lambda_1362)

    @scena.Lambda('lambda_1373')
    def lambda_1373():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1373')

    DispatchAsync2(0x000B, 0x0002, lambda_1373)

    @scena.Lambda('lambda_1384')
    def lambda_1384():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1384')

    DispatchAsync2(0x000C, 0x0002, lambda_1384)

    @scena.Lambda('lambda_1395')
    def lambda_1395():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1395')

    DispatchAsync2(0x000D, 0x0002, lambda_1395)

    @scena.Lambda('lambda_13A6')
    def lambda_13A6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_13A6')

    DispatchAsync2(0x000E, 0x0002, lambda_13A6)

    @scena.Lambda('lambda_13B7')
    def lambda_13B7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_13B7')

    DispatchAsync2(0x0009, 0x0002, lambda_13B7)

    @scena.Lambda('lambda_13C8')
    def lambda_13C8():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_13C8')

    DispatchAsync2(0x0008, 0x0002, lambda_13C8)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0101, 10)
    SetChrFlags(0x0101, 0x1000)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_13F3')
    def lambda_13F3():
        OP_99(0x00FE, 0x00, 0x0C, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13F3)

    SetChrDirection(0x0101, 270, 0)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0101, -2009, 0, -1880, 2000, 6000)
    PlaySE(164, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1460')
    def lambda_1460():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1460)

    @scena.Lambda('lambda_1472')
    def lambda_1472():
        ChrMoveTo(0x00FE, -4090, 0, -1570, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1472)

    @scena.Lambda('lambda_148D')
    def lambda_148D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_148D)

    @scena.Lambda('lambda_14A3')
    def lambda_14A3():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_14A3)

    Sleep(150)

    @scena.Lambda('lambda_14BE')
    def lambda_14BE():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_14BE)

    Sleep(100)

    @scena.Lambda('lambda_14D9')
    def lambda_14D9():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_14D9)

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

    SetChrChipByIndex(0x0101, 5)

    @scena.Lambda('lambda_1504')
    def lambda_1504():
        SetChrDirection(0x00FE, 19, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1504)

    @scena.Lambda('lambda_1512')
    def lambda_1512():
        ChrMoveTo(0x00FE, -2780, 0, -3040, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1512)

    @scena.Lambda('lambda_152D')
    def lambda_152D():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_152D)

    @scena.Lambda('lambda_153B')
    def lambda_153B():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_153B)

    @scena.Lambda('lambda_1549')
    def lambda_1549():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1549)

    @scena.Lambda('lambda_1557')
    def lambda_1557():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_1557)

    @scena.Lambda('lambda_1565')
    def lambda_1565():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1565)

    @scena.Lambda('lambda_1573')
    def lambda_1573():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1573)

    ClearChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0102, 0x1000)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0102, 7)
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

    SetChrChipByIndex(0x0102, 9)
    OP_99(0x0102, 0x00, 0x05, 2500)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_15DC')
    def lambda_15DC():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_15DC')

    DispatchAsync2(0x000A, 0x0002, lambda_15DC)

    @scena.Lambda('lambda_15ED')
    def lambda_15ED():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_15ED')

    DispatchAsync2(0x000B, 0x0002, lambda_15ED)

    @scena.Lambda('lambda_15FE')
    def lambda_15FE():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_15FE')

    DispatchAsync2(0x000C, 0x0002, lambda_15FE)

    @scena.Lambda('lambda_160F')
    def lambda_160F():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_160F')

    DispatchAsync2(0x000D, 0x0002, lambda_160F)

    @scena.Lambda('lambda_1620')
    def lambda_1620():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1620')

    DispatchAsync2(0x000E, 0x0002, lambda_1620)

    @scena.Lambda('lambda_1631')
    def lambda_1631():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1631')

    DispatchAsync2(0x0009, 0x0002, lambda_1631)

    @scena.Lambda('lambda_1642')
    def lambda_1642():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1642')

    DispatchAsync2(0x0008, 0x0002, lambda_1642)

    @scena.Lambda('lambda_1653')
    def lambda_1653():
        OP_99(0x00FE, 0x05, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1653)

    @scena.Lambda('lambda_1663')
    def lambda_1663():
        ChrWalkTo(0x00FE, -40, 0, -910, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1663)

    Sleep(100)

    @scena.Lambda('lambda_1683')
    def lambda_1683():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1200)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1683)

    SetChrFlags(0x0102, 0x0040)
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

    SetChrChipByIndex(0x0102, 7)

    @scena.Lambda('lambda_16E8')
    def lambda_16E8():
        SetChrDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16E8)

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
        (0x00000001, 'loc_17D1'),
        (-1, 'loc_17D6'),
    )

    def _loc_17D1(): pass

    label('loc_17D1')

    OP_B4(0x00)

    Jump('loc_17D6')

    def _loc_17D6(): pass

    label('loc_17D6')

    EventBegin(0x00)
    SetChrFlags(0x0140, 0x0080)
    SetChrFlags(0x0141, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    CameraMove(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    CameraSetDistance(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrDirection(0x0008, 28, 0)
    SetChrDirection(0x0009, 28, 0)
    SetChrPos(0x0101, -3210, 0, -460, 291)
    SetChrPos(0x0102, -50, 0, -1270, 72)

    @scena.Lambda('lambda_186F')
    def lambda_186F():
        OP_6E(504, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_186F)

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

    SetChrChipByIndex(0x0101, 65535)
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

    SetChrChipByIndex(0x0102, 65535)
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

    Jump('loc_1954')

    def _loc_1954(): pass

    label('loc_1954')

    ChrTalk(
        0x0009,
        (
            '#0860000977V结、结束了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1979')
    def lambda_1979():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1979)

    @scena.Lambda('lambda_1987')
    def lambda_1987():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1987)

    ChrTalk(
        0x0008,
        (
            '#0850000978V厉害～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_19AC')
    def lambda_19AC():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_19AC')

    DispatchAsync2(0x0008, 0x0001, lambda_19AC)

    @scena.Lambda('lambda_19BD')
    def lambda_19BD():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_19BD')

    DispatchAsync2(0x0101, 0x0001, lambda_19BD)

    @scena.Lambda('lambda_19CE')
    def lambda_19CE():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_19CE')

    DispatchAsync2(0x0102, 0x0001, lambda_19CE)

    OP_62(0x0008, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    ChrJumpToRelative(0x0008, 0, 0, 0, 700, 6000)
    ChrJumpToRelative(0x0008, 0, 0, 0, 700, 6000)
    Sleep(300)

    @scena.Lambda('lambda_1A24')
    def lambda_1A24():
        ChrWalkTo(0x00FE, -3690, 0, -1560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1A24)

    Sleep(300)

    @scena.Lambda('lambda_1A44')
    def lambda_1A44():
        CameraMove(-3440, 0, -2740, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1A44)

    Sleep(100)

    @scena.Lambda('lambda_1A61')
    def lambda_1A61():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1A61')

    DispatchAsync2(0x0009, 0x0001, lambda_1A61)

    @scena.Lambda('lambda_1A72')
    def lambda_1A72():
        ChrWalkTo(0x00FE, -1020, 0, -3170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1A72)

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

    @scena.Lambda('lambda_1B57')
    def lambda_1B57():
        CameraMove(-4540, 0, -1610, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1B57)

    SetChrFlags(0x0101, 0x0040)
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

    @scena.Lambda('lambda_1C50')
    def lambda_1C50():
        SetChrDirection(0x00FE, 270, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1C50)

    @scena.Lambda('lambda_1C5E')
    def lambda_1C5E():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000005DC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1C5E)

    ClearChrFlags(0x0101, 0x1000)
    ChrMoveTo(0x0101, -6730, 0, 270, 5000, 0x00)
    SetChrFlags(0x0008, 0x0004)
    ChrMoveToRelativeAsync(0x0008, 0, 100, 0, 800, 0x00)

    @scena.Lambda('lambda_1CA6')
    def lambda_1CA6():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CA6)

    OP_97(0x0008, -6730, 270, -180000, 4000, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010000985V#005F给·我·好·好·反·省！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1CF3')
    def lambda_1CF3():
        ChrMoveToRelativeAsync(0x00FE, 1200, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CF3)

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

    @scena.Lambda('lambda_1E4D')
    def lambda_1E4D():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_1E4D')

    DispatchAsync2(0x0008, 0x0003, lambda_1E4D)

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
    SetChrChipByIndex(0x000A, 11)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -16000, 0, 0, 282)

    @scena.Lambda('lambda_1EC5')
    def lambda_1EC5():
        ChrWalkTo(0x00FE, -11000, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1EC5)

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

    ClearChrFlags(0x0101, 0x1000)

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
    ClearChrFlags(0x0008, 0x0004)
    ChrTurnDirection(0x0101, 0x000A, 400)
    ChrTurnDirection(0x0008, 0x0101, 400)

    @scena.Lambda('lambda_1FA9')
    def lambda_1FA9():
        CameraMove(-6670, 0, -1080, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1FA9)

    @scena.Lambda('lambda_1FC1')
    def lambda_1FC1():
        ChrWalkTo(0x00FE, -9500, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1FC1)

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
    CreateThread(0x0102, 0x00, 0x00, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0014, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrPos(0x0011, -21000, 0, 0, 0)
    SetChrPos(0x0012, -21040, 0, 0, 0)
    SetChrPos(0x0013, -21040, 0, 0, 0)
    SetChrPos(0x0014, -21040, 0, 0, 0)
    SetChrPos(0x0010, -21040, 0, 0, 0)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0014, 0x0040)
    SetChrFlags(0x0010, 0x0040)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 200, 0)
    ChrSetRGBAMask(0x0012, 255, 255, 255, 150, 0)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 100, 0)
    ChrSetRGBAMask(0x0014, 255, 255, 255, 50, 0)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 12)

    @scena.Lambda('lambda_2129')
    def lambda_2129():
        ChrWalkTo(0x000A, -5500, 0, 0, 2700, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2129)

    @scena.Lambda('lambda_2144')
    def lambda_2144():
        CameraMove(-5130, 0, -1080, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2144)

    @scena.Lambda('lambda_215C')
    def lambda_215C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_215C)

    @scena.Lambda('lambda_2172')
    def lambda_2172():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000258, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2172)

    SetChrFlags(0x0010, 0x0002)
    SetChrFlags(0x0011, 0x0002)
    SetChrFlags(0x0012, 0x0002)
    SetChrFlags(0x0013, 0x0002)
    SetChrFlags(0x0014, 0x0002)
    SetChrSubChip(0x0010, 0)
    SetChrSubChip(0x0011, 0)
    SetChrSubChip(0x0012, 0)
    SetChrSubChip(0x0013, 0)
    SetChrSubChip(0x0014, 0)
    SetChrFlags(0x0010, 0x0020)
    SetChrFlags(0x0011, 0x0020)
    SetChrFlags(0x0012, 0x0020)
    SetChrFlags(0x0013, 0x0020)
    SetChrFlags(0x0014, 0x0020)
    SetChrChipByIndex(0x0010, 13)
    SetChrChipByIndex(0x0011, 13)
    SetChrChipByIndex(0x0012, 13)
    SetChrChipByIndex(0x0013, 13)
    SetChrChipByIndex(0x0014, 13)

    @scena.Lambda('lambda_21EC')
    def lambda_21EC():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_21EC)

    Sleep(100)

    @scena.Lambda('lambda_220C')
    def lambda_220C():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_220C)

    Sleep(100)

    @scena.Lambda('lambda_222C')
    def lambda_222C():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_222C)

    Sleep(100)

    @scena.Lambda('lambda_224C')
    def lambda_224C():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_224C)

    Sleep(100)

    @scena.Lambda('lambda_226C')
    def lambda_226C():
        ChrWalkTo(0x00FE, -10000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_226C)

    OP_20(0x000003E8)
    WaitForThreadExit(0x0010, 0x0001)
    CreateThread(0x0011, 0x01, 0x00, 0x0006)
    CreateThread(0x0012, 0x01, 0x00, 0x0007)
    CreateThread(0x0013, 0x01, 0x00, 0x0008)
    CreateThread(0x0014, 0x01, 0x00, 0x0009)
    SetChrSubChip(0x0010, 1)
    ChrJumpTo(0x0010, -7700, 0, 1500, 1200, 10000)
    PlaySE(164, 0x00, 0x64)
    CreateThread(0x0010, 0x01, 0x00, 0x0005)
    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(155, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x00FF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x09, 0xFF, 0x00FF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x00, 0xFF, 0x00FF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrFlags(0x000A, 0x0040)

    @scena.Lambda('lambda_238D')
    def lambda_238D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_238D)

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

    SetChrChipByIndex(0x0102, 65535)
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

    @scena.Lambda('lambda_23FE')
    def lambda_23FE():
        OP_6C(270000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_23FE)

    @scena.Lambda('lambda_240E')
    def lambda_240E():
        CameraMove(-5500, 0, 0, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_240E)

    Sleep(1300)

    SetChrSubChip(0x0010, 4)
    Sleep(1200)

    @scena.Lambda('lambda_2435')
    def lambda_2435():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2435)

    @scena.Lambda('lambda_2443')
    def lambda_2443():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2443)

    @scena.Lambda('lambda_2451')
    def lambda_2451():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2451)

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

    @scena.Lambda('lambda_24F0')
    def lambda_24F0():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_24F0')

    DispatchAsync2(0x0101, 0x0001, lambda_24F0)

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

    @scena.Lambda('lambda_25FB')
    def lambda_25FB():
        CameraMove(-6270, 0, 130, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_25FB)

    @scena.Lambda('lambda_2613')
    def lambda_2613():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_2613')

    DispatchAsync2(0x0008, 0x0001, lambda_2613)

    @scena.Lambda('lambda_2624')
    def lambda_2624():
        ChrMoveTo(0x00FE, -4400, 0, 1530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2624)

    @scena.Lambda('lambda_263F')
    def lambda_263F():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_263F')

    DispatchAsync2(0x0009, 0x0001, lambda_263F)

    @scena.Lambda('lambda_2650')
    def lambda_2650():
        ChrMoveTo(0x00FE, -2590, 0, -1600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2650)

    ChrWalkTo(0x0102, -4720, 0, -750, 3000, 0x00)
    TerminateThread(0x0102, 0xFF)
    SetChrDirection(0x0102, 315, 400)
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

    @scena.Lambda('lambda_27AE')
    def lambda_27AE():
        ChrWalkTo(0x00FE, -5700, 0, -1720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27AE)

    Sleep(200)

    @scena.Lambda('lambda_27CE')
    def lambda_27CE():
        ChrWalkTo(0x00FE, -7050, 0, 1000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_27CE)

    @scena.Lambda('lambda_27E9')
    def lambda_27E9():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_27E9')

    DispatchAsync2(0x0008, 0x0001, lambda_27E9)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_27FF')
    def lambda_27FF():
        ChrWalkTo(0x00FE, -7000, 0, -1050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_27FF)

    @scena.Lambda('lambda_281A')
    def lambda_281A():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_281A')

    DispatchAsync2(0x0009, 0x0001, lambda_281A)

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
    SetChrSubChip(0x0010, 0)
    ClearChrFlags(0x0010, 0x0002)
    ClearChrFlags(0x0010, 0x0020)
    SetChrChipByIndex(0x0010, 4)
    SetChrDirection(0x0010, 90, 0)
    SetChrDirection(0x0010, 270, 400)

    @scena.Lambda('lambda_2906')
    def lambda_2906():
        ChrWalkTo(0x00FE, -37590, 0, -120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2906)

    Sleep(300)

    @scena.Lambda('lambda_2926')
    def lambda_2926():
        ChrWalkTo(0x00FE, -37590, 0, -120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2926)

    Sleep(100)

    @scena.Lambda('lambda_2946')
    def lambda_2946():
        ChrWalkTo(0x00FE, -37590, 0, -120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2946)

    @scena.Lambda('lambda_2961')
    def lambda_2961():
        OP_6E(471, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2961)

    @scena.Lambda('lambda_2971')
    def lambda_2971():
        OP_6C(224000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2971)

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
    SetChrDirection(0x0101, 45, 400)
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

# id: 0x0004 offset: 0x2AE7
@scena.Code('func_04_2AE7')
def func_04_2AE7():
    ClearChrFlags(0x0102, 0x1000)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0102, 7)
    Sleep(500)

    @scena.Lambda('lambda_2B07')
    def lambda_2B07():
        ChrWalkTo(0x00FE, -2560, 0, -940, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2B07)

    Return()

# id: 0x0005 offset: 0x2B1D
@scena.Code('func_05_2B1D')
def func_05_2B1D():
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    PlaySE(164, 0x00, 0x64)
    SetChrSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    PlaySE(164, 0x00, 0x64)
    SetChrSubChip(0x00FE, 3)

    Return()

# id: 0x0006 offset: 0x2B65
@scena.Code('func_06_2B65')
def func_06_2B65():
    Sleep(100)

    SetChrSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    SetChrSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    SetChrFlags(0x0011, 0x0080)

    Return()

# id: 0x0007 offset: 0x2BC4
@scena.Code('func_07_2BC4')
def func_07_2BC4():
    Sleep(200)

    SetChrSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    SetChrSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    SetChrFlags(0x0012, 0x0080)

    Return()

# id: 0x0008 offset: 0x2C23
@scena.Code('func_08_2C23')
def func_08_2C23():
    Sleep(300)

    SetChrSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    SetChrSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    SetChrFlags(0x0013, 0x0080)

    Return()

# id: 0x0009 offset: 0x2C82
@scena.Code('func_09_2C82')
def func_09_2C82():
    Sleep(400)

    SetChrSubChip(0x00FE, 1)
    ChrJumpTo(0x00FE, -7700, 0, 1500, 1200, 10000)
    ChrJumpTo(0x00FE, -6200, 0, 150, 1000, 5000)
    SetChrSubChip(0x00FE, 2)
    Sleep(500)

    ChrJumpTo(0x00FE, -7700, 0, 0, 500, 5000)
    SetChrFlags(0x0014, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
