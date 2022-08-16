import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3108_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3108   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3108.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希德中校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '格斯塔夫维修长',
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
            name                = '菲',
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
            name                = '维修员',
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
            name                = '维修员',
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
            name                = '维修员',
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
            name                = '维修员',
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
            name                = '工房船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '工房船影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '埃尔赛尤号的影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x332
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x332
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x332
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x332
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_B1('C3108_1')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_09_F09)

    Jump('loc_374')

    def _loc_35A(): pass

    label('loc_35A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_374',
    )

    MapSetFlags(0x10000000)
    OP_B1('C3108_2')
    Event(0, func_02_376)

    def _loc_374(): pass

    label('loc_374')

    Return()

# id: 0x0001 offset: 0x375
@scena.Code('func_01_375')
def func_01_375():
    Return()

# id: 0x0002 offset: 0x376
@scena.Code('func_02_376')
def func_02_376():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    MapClearFlags(0x00000010)
    ChrSetFlags(0x0014, 0x0004)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetPos(0x0014, 570, 30000, 22920, 360)
    ChrSetPos(0x0015, 570, 15000, 22920, 360)
    ChrSetPos(0x0016, 10000, -10000, 54840, 270)
    OP_A1(0x0014, 0x0000)
    OP_A1(0x0015, 0x0001)
    OP_A1(0x0016, 0x0002)
    CameraMove(5630, 0, 36820, 0)
    OP_67(0, 22750, -10000, 0)
    CameraSetDistance(11040, 0)
    UnlockAchievement(0x64, 0x0001, 0x00)
    OP_6C(45000, 0)
    OP_6E(150, 0)
    PlaySE(121, 0x00, 0x64)

    @scena.Lambda('lambda_0434')
    def lambda_0434():
        CameraMove(2240, 0, 31860, 10000)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0434)

    @scena.Lambda('lambda_044C')
    def lambda_044C():
        OP_67(0, 20330, -10000, 10000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_044C)

    CameraSetDistance(9000, 10000)
    UnlockAchievement(0x64, 0x0002, 0x00)
    OP_C8(0x0200, 0x0046, 'C_PLAC10._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    OP_6F(0x0000, 60)

    @scena.Lambda('lambda_0497')
    def lambda_0497():
        ChrMoveToRelativeAsync(0x00FE, 0, -15000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_0497)

    @scena.Lambda('lambda_04B2')
    def lambda_04B2():
        ChrMoveToRelativeAsync(0x00FE, 0, -23000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_04B2)

    Sleep(2500)

    @scena.Lambda('lambda_04D2')
    def lambda_04D2():
        ChrMoveToRelativeAsync(0x00FE, 0, -23000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_04D2)

    Sleep(1500)

    @scena.Lambda('lambda_04F2')
    def lambda_04F2():
        ChrMoveToRelativeAsync(0x00FE, 0, -23000, 0, 3600, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_04F2)

    Sleep(900)

    @scena.Lambda('lambda_0512')
    def lambda_0512():
        ChrMoveToRelativeAsync(0x00FE, 0, -23000, 0, 3200, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_0512)

    Sleep(800)

    @scena.Lambda('lambda_0532')
    def lambda_0532():
        ChrMoveToRelativeAsync(0x00FE, 0, -23000, 0, 2800, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_0532)

    Sleep(700)

    @scena.Lambda('lambda_0552')
    def lambda_0552():
        ChrMoveToRelativeAsync(0x00FE, 0, -23000, 0, 2400, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_0552)

    FadeOut(1000, 0, -1)
    Sleep(600)

    @scena.Lambda('lambda_057C')
    def lambda_057C():
        ChrMoveToRelativeAsync(0x00FE, 0, -23000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_057C)

    Sleep(500)

    OP_0D()
    Sleep(500)

    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0014, 0x01)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x000F, 0x01)
    ChrSetPos(0x0014, 570, 100, 22920, 360)
    ChrSetPos(0x0015, 570, 100, 22920, 360)
    CameraMove(-15480, 15220, 18720, 0)
    OP_67(0, 9940, -10000, 0)
    CameraSetDistance(2980, 0)
    UnlockAchievement(0x64, 0x0003, 0x00)
    OP_6C(31000, 0)
    OP_6E(367, 0)
    ChrSetBattleFlags(0x000E, 0x0020)
    ChrSetBattleFlags(0x000F, 0x0020)
    ChrSetBattleFlags(0x0010, 0x0020)
    ChrSetBattleFlags(0x0011, 0x0020)
    ChrSetBattleFlags(0x0012, 0x0020)
    ChrSetBattleFlags(0x0013, 0x0020)
    Yield()
    OP_89(0x000E, -800, 2300, 23440, 270)
    OP_89(0x000F, -1170, 2300, 23910, 270)
    OP_89(0x0011, -740, 2300, 23530, 270)
    OP_89(0x0010, -1600, 2300, 22200, 270)
    OP_89(0x0013, -740, 2300, 23530, 270)
    OP_89(0x0012, -740, 2300, 23530, 270)
    OP_E5(0x0F, 0x00, 0x00)
    OP_E5(0x10, 0x00, 0x00)
    OP_E5(0x11, 0x00, 0x00)
    OP_E5(0x12, 0x00, 0x00)
    OP_E5(0x13, 0x00, 0x00)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(118, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 1)
    OP_73(0x0000)
    CreateThread(0x000F, 0x00, 0x00, func_07_E77)
    Sleep(700)

    CreateThread(0x0011, 0x01, 0x00, func_04_D9C)
    Sleep(600)

    CreateThread(0x0010, 0x01, 0x00, func_03_D53)
    Sleep(600)

    CreateThread(0x0012, 0x01, 0x00, func_05_DE5)
    Sleep(500)

    CreateThread(0x0013, 0x01, 0x00, func_06_E2E)
    Sleep(1000)

    CreateThread(0x000E, 0x00, 0x00, func_08_EC0)
    Sleep(3000)

    @scena.Lambda('lambda_0728')
    def lambda_0728():
        CameraMove(1040, 0, 47760, 5000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0728)

    UnlockAchievement(0x64, 0x0004, 0x00)

    @scena.Lambda('lambda_0745')
    def lambda_0745():
        OP_67(0, 9770, -10000, 5000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0745)

    CameraSetDistance(3510, 5000)
    UnlockAchievement(0x64, 0x0005, 0x00)

    @scena.Lambda('lambda_076B')
    def lambda_076B():
        OP_6C(66000, 5000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_076B)

    @scena.Lambda('lambda_077B')
    def lambda_077B():
        OP_6E(349, 5000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_077B)

    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000E, 0x0002)
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x000F, 0x0002)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0560240001V#691F#5P哦哦，埃尔赛尤号\n',
            '好像先到达了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240002V#693F啊～真是无论何时看\n',
            '都会令人震撼的机体啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1980240003V#2P真的是……\n',
            '令人着迷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1980240004V#2P要是每天都能整备这种飞船，\n',
            '维修技师可是享尽福气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0560240005V#691F#5P嗨，这应该是我说才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -10930, 0, 35080, 72)

    NpcTalk(
        0x000D,
        '男性的声音',
        (
            '#0620240006V#1P呀，格斯塔夫维修长。\n',
            '多亏你百忙之中能过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_093F')
    def lambda_093F():
        ChrTurnDirection(0x000F, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_093F)

    ChrTurnDirection(0x000E, 0x000D, 400)

    @scena.Lambda('lambda_0954')
    def lambda_0954():
        ChrWalkTo(0x00FE, -5550, 0, 40510, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0954)

    Fade(1000)
    CameraMove(-4280, 0, 41130, 0)
    OP_67(0, 10220, -10000, 0)
    CameraSetDistance(2490, 0)
    OP_6C(192000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_09B1')
    def lambda_09B1():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_09B1')

    DispatchAsync2(0x000E, 0x0001, lambda_09B1)

    @scena.Lambda('lambda_09C2')
    def lambda_09C2():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_09C2')

    DispatchAsync2(0x000F, 0x0001, lambda_09C2)

    OP_0D()
    WaitForThreadExit(0x000D, 0x0001)
    ChrTurnDirection(0x000D, 0x000E, 400)
    WaitForThreadExit(0x000D, 0x0002)

    ChrTalk(
        0x000E,
        (
            '#0560240007V#691F#6P哟、希德中校。\n',
            '又是你来迎接吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240008V莫非升迁之后成了这里的\n',
            '守备队长了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0620240009V#701F#2P哈哈，你说的没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240010V其实我正准备和部下过一会儿一起\n',
            '搭乘警备艇出发呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240011V准备工作已经结束了，反正也闲着，\n',
            '就来接你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0560240012V#693F#6P哈哈，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240013V#692F说起来，这里\n',
            '似乎也发生地震了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240014V埃尔赛尤号不会\n',
            '有所损坏吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0620240015V#703F#2P不，埃尔赛尤号是在\n',
            '地震发生之后到达的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240016V地震的时候，也是因为事先已经作了周全的准备，\n',
            '所以几乎没有出现什么太大的损害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240017V#701F这里的设施也都运行正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0560240018V#691F#6P那可真是帮了大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240019V我想现在就立刻\n',
            '开始进入作业……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240020V亲卫队的人都在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0620240021V#701F#2P啊啊……我来带路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240022V现在去的话，我想\n',
            '还能看到有趣的东西哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0560240023V#692F#6P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C3101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xD53
@scena.Code('func_03_D53')
def func_03_D53():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -10090, 0, 23580, 4000, 0x00)
    ChrWalkTo(0x00FE, -8820, 0, 39140, 4000, 0x00)
    ChrWalkTo(0x00FE, 1280, 0, 46840, 4000, 0x00)
    ChrSetDirection(0x00FE, 325, 400)

    Return()

# id: 0x0004 offset: 0xD9C
@scena.Code('func_04_D9C')
def func_04_D9C():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -10420, 0, 23770, 4000, 0x00)
    ChrWalkTo(0x00FE, -8930, 0, 38070, 4000, 0x00)
    ChrWalkTo(0x00FE, -180, 0, 46870, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0005 offset: 0xDE5
@scena.Code('func_05_DE5')
def func_05_DE5():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -10230, 0, 23130, 4000, 0x00)
    ChrWalkTo(0x00FE, -8930, 0, 36070, 4000, 0x00)
    ChrWalkTo(0x00FE, -2360, 0, 47470, 4000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x0006 offset: 0xE2E
@scena.Code('func_06_E2E')
def func_06_E2E():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -10640, 0, 23910, 4000, 0x00)
    ChrWalkTo(0x00FE, -8930, 0, 36070, 4000, 0x00)
    ChrWalkTo(0x00FE, -3510, 0, 47560, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 45)

    Return()

# id: 0x0007 offset: 0xE77
@scena.Code('func_07_E77')
def func_07_E77():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -10230, 0, 23130, 4000, 0x00)
    ChrWalkTo(0x00FE, -8930, 0, 37070, 4000, 0x00)
    ChrWalkTo(0x00FE, -1020, 0, 42350, 4000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x0008 offset: 0xEC0
@scena.Code('func_08_EC0')
def func_08_EC0():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -10640, 0, 23910, 4000, 0x00)
    ChrWalkTo(0x00FE, -7160, 0, 39220, 4000, 0x00)
    ChrWalkTo(0x00FE, -2900, 0, 42440, 4000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x0009 offset: 0xF09
@scena.Code('func_09_F09')
def func_09_F09():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0101, 0x0080)
    CameraMove(1860, 0, 29300, 0)
    OP_67(0, 15020, -10000, 0)
    OP_6C(15000, 0)
    CameraSetDistance(8600, 0)
    OP_6E(255, 0)
    OP_A1(0x0009, 0x0003)
    OP_A1(0x000A, 0x0001)
    OP_A1(0x000B, 0x0002)
    OP_A1(0x000C, 0x0000)
    ChrSetPos(0x0009, 1620, 0, 23850, 0)
    ChrSetPos(0x000A, 10180, -10450, 61010, 0)
    ChrSetPos(0x000B, 28590, -10450, 60800, 0)
    ChrSetPos(0x000C, -8380, -10450, 60710, 0)
    OP_A1(0x0017, 0x0007)
    OP_A1(0x0018, 0x0005)
    OP_A1(0x0019, 0x0006)
    OP_A1(0x001A, 0x0004)
    ChrSetPos(0x0017, 1620, 100, 23850, 0)
    ChrSetPos(0x0018, 10180, -10450, 61010, 0)
    ChrSetPos(0x0019, 28590, -10450, 60800, 0)
    ChrSetPos(0x001A, -8380, -10450, 60710, 0)
    MapClearFlags(0x00000010)
    ChrSetPos(0x0008, 10750, 0, 30020, 270)
    ChrClearFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_101F')
    def lambda_101F():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_101F')

    DispatchAsync2(0x0008, 0x0001, lambda_101F)

    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    CreateThread(0x0009, 0x00, 0x00, func_0A_12A0)

    @scena.Lambda('lambda_104B')
    def lambda_104B():
        CameraMove(9110, 0, 26810, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_104B)

    @scena.Lambda('lambda_1063')
    def lambda_1063():
        OP_67(0, 18670, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1063)

    @scena.Lambda('lambda_107B')
    def lambda_107B():
        CameraSetDistance(6000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_107B)

    @scena.Lambda('lambda_108B')
    def lambda_108B():
        OP_6C(56000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_108B)

    FadeIn(2000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(11060, 0, 30510, 0)
    OP_67(0, 7040, -10000, 0)
    CameraSetDistance(3060, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(2000)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0160310504V#1125F#5P……没想到它竟然\n',
            '会落到那些人手里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160310505V#1122F既然如此，不如让我亲手了结……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0x01)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160310506V#1128F#5P……不行不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160310507V如果我在此时贸然行动，\n',
            '只会重蹈覆辙而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160310508V#1120F呼呼，也就是说，不管是我还是它\n',
            '都处在相同立场啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    ChrSetDirection(0x0008, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160310509V#1125F#6P女神啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160310510V#1122F请引导我们这些\n',
            '混乱大地上的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x12A0
@scena.Code('func_0A_12A0')
def func_0A_12A0():
    PlaySE(117, 0x00, 0x64)
    CreateThread(0x0009, 0x01, 0x00, func_0B_12D6)
    Sleep(500)

    CreateThread(0x000A, 0x01, 0x00, func_0C_1593)
    Sleep(500)

    CreateThread(0x000B, 0x01, 0x00, func_0D_18D2)
    Sleep(500)

    CreateThread(0x000C, 0x01, 0x00, func_0E_1B8A)
    Sleep(8500)

    Return()

# id: 0x000B offset: 0x12D6
@scena.Code('func_0B_12D6')
def func_0B_12D6():
    PlaySE(119, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x00FF, 1620, 0, 23850, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    OP_6F(0x0000, 360)
    OP_70(0x0000, 500)
    Sleep(500)

    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 1500, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 2000, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 3000, 0x00)
    StopEffect(0x01, 0x02)
    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 4000, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 3000, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 2000, 0x00)
    OP_B0(0x0000, 0x2D)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 500)
    OP_70(0x0000, 520)
    Sleep(500)

    @scena.Lambda('lambda_13C5')
    def lambda_13C5():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_13C5)

    @scena.Lambda('lambda_13E0')
    def lambda_13E0():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_13E0)

    Sleep(300)

    @scena.Lambda('lambda_1400')
    def lambda_1400():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1400)

    @scena.Lambda('lambda_141B')
    def lambda_141B():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_141B)

    Sleep(300)

    @scena.Lambda('lambda_143B')
    def lambda_143B():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_143B)

    @scena.Lambda('lambda_1456')
    def lambda_1456():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1456)

    Sleep(300)

    @scena.Lambda('lambda_1476')
    def lambda_1476():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1476)

    @scena.Lambda('lambda_1491')
    def lambda_1491():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1491)

    Sleep(300)

    @scena.Lambda('lambda_14B1')
    def lambda_14B1():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_14B1)

    @scena.Lambda('lambda_14CC')
    def lambda_14CC():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_14CC)

    Sleep(300)

    @scena.Lambda('lambda_14EC')
    def lambda_14EC():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_14EC)

    @scena.Lambda('lambda_1507')
    def lambda_1507():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1507)

    Sleep(300)

    @scena.Lambda('lambda_1527')
    def lambda_1527():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1527)

    @scena.Lambda('lambda_1542')
    def lambda_1542():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1542)

    Sleep(300)

    @scena.Lambda('lambda_1562')
    def lambda_1562():
        ChrMoveTo(0x00FE, 1620, 20000, -33600, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1562)

    @scena.Lambda('lambda_157D')
    def lambda_157D():
        ChrMoveTo(0x00FE, 1620, 100, -33600, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_157D)

    Return()

# id: 0x000C offset: 0x1593
@scena.Code('func_0C_1593')
def func_0C_1593():
    PlayEffect(0x01, 0x02, 0x00FF, 10180, -10450, 61010, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    OP_6F(0x0001, 360)
    OP_70(0x0001, 500)
    Sleep(500)

    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 1500, 0x00)

    @scena.Lambda('lambda_15FA')
    def lambda_15FA():
        ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_15FA)

    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 2000, 0x00)

    @scena.Lambda('lambda_1629')
    def lambda_1629():
        ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1629)

    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 3000, 0x00)
    StopEffect(0x02, 0x02)

    @scena.Lambda('lambda_165B')
    def lambda_165B():
        ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_165B)

    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 4000, 0x00)

    @scena.Lambda('lambda_168A')
    def lambda_168A():
        ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_168A)

    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 3000, 0x00)

    @scena.Lambda('lambda_16B9')
    def lambda_16B9():
        ChrMoveToRelativeAsync(0x00FE, 0, 450, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_16B9)

    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 2000, 0x00)
    OP_B0(0x0001, 0x2D)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 520)
    Sleep(500)

    @scena.Lambda('lambda_1704')
    def lambda_1704():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1704)

    @scena.Lambda('lambda_171F')
    def lambda_171F():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_171F)

    Sleep(300)

    @scena.Lambda('lambda_173F')
    def lambda_173F():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_173F)

    @scena.Lambda('lambda_175A')
    def lambda_175A():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_175A)

    Sleep(300)

    @scena.Lambda('lambda_177A')
    def lambda_177A():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_177A)

    @scena.Lambda('lambda_1795')
    def lambda_1795():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1795)

    Sleep(300)

    @scena.Lambda('lambda_17B5')
    def lambda_17B5():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_17B5)

    @scena.Lambda('lambda_17D0')
    def lambda_17D0():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_17D0)

    Sleep(300)

    @scena.Lambda('lambda_17F0')
    def lambda_17F0():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_17F0)

    @scena.Lambda('lambda_180B')
    def lambda_180B():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_180B)

    Sleep(300)

    @scena.Lambda('lambda_182B')
    def lambda_182B():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_182B)

    @scena.Lambda('lambda_1846')
    def lambda_1846():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1846)

    Sleep(300)

    @scena.Lambda('lambda_1866')
    def lambda_1866():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1866)

    @scena.Lambda('lambda_1881')
    def lambda_1881():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1881)

    Sleep(300)

    @scena.Lambda('lambda_18A1')
    def lambda_18A1():
        ChrMoveTo(0x00FE, 10180, 20000, -33600, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_18A1)

    @scena.Lambda('lambda_18BC')
    def lambda_18BC():
        ChrMoveTo(0x00FE, 10180, 0, -33600, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_18BC)

    Return()

# id: 0x000D offset: 0x18D2
@scena.Code('func_0D_18D2')
def func_0D_18D2():
    PlayEffect(0x01, 0x03, 0x00FF, 28590, -10450, 60800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    OP_6F(0x0002, 360)
    OP_70(0x0002, 500)
    Sleep(500)

    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 1500, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 2000, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 3000, 0x00)
    StopEffect(0x03, 0x02)
    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 4000, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 3000, 0x00)
    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 2000, 0x00)
    OP_B0(0x0002, 0x2D)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 500)
    OP_70(0x0002, 520)
    Sleep(500)

    @scena.Lambda('lambda_19BC')
    def lambda_19BC():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_19BC)

    @scena.Lambda('lambda_19D7')
    def lambda_19D7():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_19D7)

    Sleep(300)

    @scena.Lambda('lambda_19F7')
    def lambda_19F7():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_19F7)

    @scena.Lambda('lambda_1A12')
    def lambda_1A12():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1A12)

    Sleep(300)

    @scena.Lambda('lambda_1A32')
    def lambda_1A32():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1A32)

    @scena.Lambda('lambda_1A4D')
    def lambda_1A4D():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1A4D)

    Sleep(300)

    @scena.Lambda('lambda_1A6D')
    def lambda_1A6D():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1A6D)

    @scena.Lambda('lambda_1A88')
    def lambda_1A88():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1A88)

    Sleep(300)

    @scena.Lambda('lambda_1AA8')
    def lambda_1AA8():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1AA8)

    @scena.Lambda('lambda_1AC3')
    def lambda_1AC3():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1AC3)

    Sleep(300)

    @scena.Lambda('lambda_1AE3')
    def lambda_1AE3():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1AE3)

    @scena.Lambda('lambda_1AFE')
    def lambda_1AFE():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1AFE)

    Sleep(300)

    @scena.Lambda('lambda_1B1E')
    def lambda_1B1E():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1B1E)

    @scena.Lambda('lambda_1B39')
    def lambda_1B39():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1B39)

    Sleep(300)

    @scena.Lambda('lambda_1B59')
    def lambda_1B59():
        ChrMoveTo(0x00FE, 28590, 20000, -33600, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1B59)

    @scena.Lambda('lambda_1B74')
    def lambda_1B74():
        ChrMoveTo(0x00FE, 28590, -10450, -33600, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1B74)

    Return()

# id: 0x000E offset: 0x1B8A
@scena.Code('func_0E_1B8A')
def func_0E_1B8A():
    PlayEffect(0x01, 0x04, 0x00FF, -8380, -10450, 60710, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    OP_6F(0x0003, 360)
    OP_70(0x0003, 500)
    Sleep(500)

    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 1500, 0x00)

    @scena.Lambda('lambda_1BF1')
    def lambda_1BF1():
        ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1BF1)

    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 2000, 0x00)

    @scena.Lambda('lambda_1C20')
    def lambda_1C20():
        ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1C20)

    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 3000, 0x00)
    StopEffect(0x04, 0x02)

    @scena.Lambda('lambda_1C52')
    def lambda_1C52():
        ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1C52)

    ChrMoveToRelativeAsync(0x00FE, 0, 4000, 0, 4000, 0x00)

    @scena.Lambda('lambda_1C81')
    def lambda_1C81():
        ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1C81)

    ChrMoveToRelativeAsync(0x00FE, 0, 3000, 0, 3000, 0x00)

    @scena.Lambda('lambda_1CB0')
    def lambda_1CB0():
        ChrMoveToRelativeAsync(0x00FE, 0, 450, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1CB0)

    ChrMoveToRelativeAsync(0x00FE, 0, 1000, 0, 2000, 0x00)
    OP_B0(0x0003, 0x2D)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 500)
    OP_70(0x0003, 520)
    Sleep(500)

    @scena.Lambda('lambda_1CFB')
    def lambda_1CFB():
        ChrMoveTo(0x00FE, -8360, 20000, -33590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1CFB)

    @scena.Lambda('lambda_1D16')
    def lambda_1D16():
        ChrMoveTo(0x00FE, -8360, 0, -33590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1D16)

    Sleep(300)

    @scena.Lambda('lambda_1D36')
    def lambda_1D36():
        ChrMoveTo(0x00FE, -8360, 20000, -33590, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1D36)

    @scena.Lambda('lambda_1D51')
    def lambda_1D51():
        ChrMoveTo(0x00FE, -8360, 0, -33590, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1D51)

    Sleep(300)

    @scena.Lambda('lambda_1D71')
    def lambda_1D71():
        ChrMoveTo(0x00FE, -8360, 20000, -63590, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1D71)

    @scena.Lambda('lambda_1D8C')
    def lambda_1D8C():
        ChrMoveTo(0x00FE, -8360, 0, -63590, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1D8C)

    Sleep(300)

    @scena.Lambda('lambda_1DAC')
    def lambda_1DAC():
        ChrMoveTo(0x00FE, -8360, 20000, -63590, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1DAC)

    @scena.Lambda('lambda_1DC7')
    def lambda_1DC7():
        ChrMoveTo(0x00FE, -8360, 0, -63590, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1DC7)

    Sleep(300)

    @scena.Lambda('lambda_1DE7')
    def lambda_1DE7():
        ChrMoveTo(0x00FE, -8360, 20000, -63590, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1DE7)

    @scena.Lambda('lambda_1E02')
    def lambda_1E02():
        ChrMoveTo(0x00FE, -8360, 0, -63590, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1E02)

    Sleep(300)

    @scena.Lambda('lambda_1E22')
    def lambda_1E22():
        ChrMoveTo(0x00FE, -8360, 20000, -63590, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1E22)

    @scena.Lambda('lambda_1E3D')
    def lambda_1E3D():
        ChrMoveTo(0x00FE, -8360, 0, -63590, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1E3D)

    Sleep(300)

    @scena.Lambda('lambda_1E5D')
    def lambda_1E5D():
        ChrMoveTo(0x00FE, -8360, 20000, -63590, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1E5D)

    @scena.Lambda('lambda_1E78')
    def lambda_1E78():
        ChrMoveTo(0x00FE, -8360, 0, -63590, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1E78)

    Sleep(300)

    @scena.Lambda('lambda_1E98')
    def lambda_1E98():
        ChrMoveTo(0x00FE, -8360, 20000, -63590, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1E98)

    @scena.Lambda('lambda_1EB3')
    def lambda_1EB3():
        ChrMoveTo(0x00FE, -8360, 0, -63590, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1EB3)

    CreateThread(0x0009, 0x01, 0x00, func_0F_1ED0)

    Return()

# id: 0x000F offset: 0x1ED0
@scena.Code('func_0F_1ED0')
def func_0F_1ED0():
    OP_24(0x0075, 0x5A)
    OP_24(0x0077, 0x5A)
    Sleep(200)

    OP_24(0x0075, 0x50)
    OP_24(0x0077, 0x50)
    Sleep(200)

    OP_24(0x0075, 0x46)
    OP_24(0x0077, 0x46)
    Sleep(200)

    OP_24(0x0075, 0x3C)
    OP_24(0x0077, 0x3C)
    Sleep(200)

    OP_24(0x0075, 0x32)
    OP_24(0x0077, 0x32)
    Sleep(200)

    OP_24(0x0075, 0x28)
    OP_24(0x0077, 0x28)
    Sleep(200)

    OP_24(0x0075, 0x1E)
    OP_24(0x0077, 0x1E)
    Sleep(200)

    OP_23(0x0075)
    OP_23(0x0077)
    OP_23(0x00CF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
