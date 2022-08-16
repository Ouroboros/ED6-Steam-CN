import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1203   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1203.x'
    header.mapIndex       = 61
    header.bgm            = 86
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
        ('ED6_DT09/CH10290._CH', 'ED6_DT09/CH10290P._CP'),
        ('ED6_DT09/CH10291._CH', 'ED6_DT09/CH10291P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10320._CH', 'ED6_DT09/CH10320P._CP'),
        ('ED6_DT09/CH10321._CH', 'ED6_DT09/CH10321P._CP'),
        ('ED6_DT09/CH10330._CH', 'ED6_DT09/CH10330P._CP'),
        ('ED6_DT09/CH10331._CH', 'ED6_DT09/CH10331P._CP'),
        ('ED6_DT09/CH10350._CH', 'ED6_DT09/CH10350P._CP'),
        ('ED6_DT09/CH10351._CH', 'ED6_DT09/CH10351P._CP'),
        ('ED6_DT09/CH10540._CH', 'ED6_DT09/CH10540P._CP'),
        ('ED6_DT09/CH10541._CH', 'ED6_DT09/CH10541P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
        ('ED6_DT09/CH10900._CH', 'ED6_DT09/CH10900P._CP'),
        ('ED6_DT09/CH10901._CH', 'ED6_DT09/CH10901P._CP'),
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
        ('ED6_DT07/CH00312._CH', 'ED6_DT07/CH00312P._CP'),
        ('ED6_DT07/CH00290._CH', 'ED6_DT07/CH00290P._CP'),
        ('ED6_DT07/CH00292._CH', 'ED6_DT07/CH00292P._CP'),
        ('ED6_DT07/CH00300._CH', 'ED6_DT07/CH00300P._CP'),
        ('ED6_DT07/CH00305._CH', 'ED6_DT07/CH00305P._CP'),
        ('ED6_DT07/CH00306._CH', 'ED6_DT07/CH00306P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00343._CH', 'ED6_DT07/CH00343P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00443._CH', 'ED6_DT07/CH00443P._CP'),
        ('ED6_DT07/CH00444._CH', 'ED6_DT07/CH00444P._CP'),
        ('ED6_DT26/CH20299._CH', 'ED6_DT26/CH20299P._CP'),
        ('ED6_DT07/CH00316._CH', 'ED6_DT07/CH00316P._CP'),
        ('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP'),
        ('ED6_DT27/CH04017._CH', 'ED6_DT27/CH04017P._CP'),
        ('ED6_DT27/CH0401A._CH', 'ED6_DT27/CH0401AP._CP'),
    ]

# id: 0x10001 offset: 0x202
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乔丝特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古罗尼山道方向',
            x                   = -505000,
            z                   = 10,
            y                   = 56760,
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
            name                = '柏斯方向',
            x                   = -352510,
            z                   = 0,
            y                   = 15930,
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

# id: 0x10002 offset: 0x3A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -391300,
            z           = -10,
            y           = 18680,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -416900,
            z           = 560,
            y           = 32439,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -468920,
            z           = 50,
            y           = 69100,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -449270,
            z           = -30,
            y           = 48370,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x412
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x412
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -454930,
            triggerZ            = 510,
            triggerY            = 62180,
            triggerRange        = 1000,
            actorX              = -454930,
            actorZ              = 510,
            actorY              = 62880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x436
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_449',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_02_46B)

    def _loc_449(): pass

    label('loc_449')

    Return()

# id: 0x0001 offset: 0x44A
@scena.Code('func_01_44A')
def func_01_44A():
    OP_16(0x02, 4000, -560000, -90000, 2293787)
    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0000)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0002 offset: 0x46B
@scena.Code('func_02_46B')
def func_02_46B():
    EventBegin(0x00)
    MapClearFlags(0x00000010)
    OP_DB()
    LoadEffect(0x00, 'map\\\\mp019_00.eff')
    LoadEffect(0x01, 'monster\\ms00300.eff')
    LoadEffect(0x02, 'battle\\btgun00.eff')
    LoadEffect(0x03, 'monster\\msc0130.eff')
    LoadEffect(0x04, 'Craft\\\\cr161_00.eff')
    LoadEffect(0x05, 'monster\\msc0100.eff')
    LoadEffect(0x06, 'map\\mp047_00.eff')
    LoadEffect(0x07, 'craft\\\\cr162_02.eff')
    CameraMove(-377740, 0, 17860, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2580, 0)
    OP_6C(118000, 0)
    OP_6E(626, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetChipByIndex(0x000A, 26)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetChipByIndex(0x000B, 28)
    ChrSetPos(0x000A, -418370, 10, 17500, 90)
    ChrSetPos(0x000B, -405790, 1120, 27140, 270)
    ChrSetPos(0x0009, -404680, 1120, 10760, 180)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetPos(0x000C, -344960, 0, 16730, 270)
    ChrSetPos(0x000D, -345890, 0, 18630, 270)
    ChrSetPos(0x000E, -350960, 0, 15420, 270)
    ChrSetPos(0x000F, -348390, 0, 16440, 270)
    ChrSetPos(0x0010, -348330, 0, 17970, 270)
    ChrSetPos(0x0011, -350850, 0, 16990, 270)

    @scena.Lambda('lambda_0676')
    def lambda_0676():
        OP_6E(426, 18000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0676)

    OP_C8(0x0200, 0x0046, 'C_PLAC13._CH', 0x00, 0x03E8)
    FadeIn(2000, 0)
    CreateThread(0x000C, 0x00, 0x00, func_03_1F4D)
    CreateThread(0x000D, 0x00, 0x00, func_04_1FB4)
    CreateThread(0x000E, 0x00, 0x00, func_05_201B)
    CreateThread(0x000F, 0x00, 0x00, func_06_2096)
    CreateThread(0x0010, 0x00, 0x00, func_07_2111)
    CreateThread(0x0011, 0x00, 0x00, func_08_218C)
    Sleep(8000)

    @scena.Lambda('lambda_06D3')
    def lambda_06D3():
        CameraMove(-398320, 0, 19820, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_06D3)

    @scena.Lambda('lambda_06EB')
    def lambda_06EB():
        OP_67(0, 5400, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_06EB)

    @scena.Lambda('lambda_0703')
    def lambda_0703():
        OP_6C(62000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0703)

    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)
    WaitForThreadExit(0x0000, 0x0003)
    Fade(1000)
    CameraMove(-415430, 5330, 19650, 0)
    OP_67(0, 3540, -10000, 0)
    CameraSetDistance(2580, 0)
    OP_6C(90000, 0)
    OP_6E(426, 0)
    ChrSetPos(0x000A, -423010, 5360, 19710, 90)
    TerminateThread(0x000C, 0x00)
    ChrSetPos(0x000C, -394550, 0, 19140, 270)

    @scena.Lambda('lambda_078F')
    def lambda_078F():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_078F)

    TerminateThread(0x000D, 0x00)
    ChrSetPos(0x000D, -395580, 0, 21300, 270)

    @scena.Lambda('lambda_07BA')
    def lambda_07BA():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_07BA)

    TerminateThread(0x000E, 0x00)
    ChrSetPos(0x000E, -399330, 0, 17930, 270)

    @scena.Lambda('lambda_07E5')
    def lambda_07E5():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_07E5)

    TerminateThread(0x000F, 0x00)
    ChrSetPos(0x000F, -397170, 0, 19450, 270)

    @scena.Lambda('lambda_0810')
    def lambda_0810():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0810)

    TerminateThread(0x0010, 0x00)
    ChrSetPos(0x0010, -397650, 0, 21940, 270)

    @scena.Lambda('lambda_083B')
    def lambda_083B():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_083B)

    TerminateThread(0x0011, 0x00)
    ChrSetPos(0x0011, -399630, 0, 20170, 270)

    @scena.Lambda('lambda_0866')
    def lambda_0866():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_0866)

    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0300260250V#196F#5S#5P#9A喝啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    TerminateThread(0x000C, 0x00)
    ChrSetSubChip(0x000C, 0)
    TerminateThread(0x000D, 0x00)
    ChrSetSubChip(0x000D, 0)
    TerminateThread(0x000E, 0x00)
    ChrSetSubChip(0x000E, 0)
    TerminateThread(0x000F, 0x00)
    ChrSetSubChip(0x000F, 0)
    TerminateThread(0x0010, 0x00)
    ChrSetSubChip(0x0010, 0)
    TerminateThread(0x0011, 0x00)
    ChrSetSubChip(0x0011, 0)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_08FB')
    def lambda_08FB():
        CameraMove(-402920, 0, 19580, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_08FB)

    @scena.Lambda('lambda_0913')
    def lambda_0913():
        OP_67(0, 4880, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0913)

    @scena.Lambda('lambda_092B')
    def lambda_092B():
        OP_6C(82000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_092B)

    @scena.Lambda('lambda_093B')
    def lambda_093B():
        ChrJumpTo(0x00FE, -410660, 0, 18520, 800, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_093B)

    @scena.Lambda('lambda_0959')
    def lambda_0959():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0959)

    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(164, 0x00, 0x64)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_097A')
    def lambda_097A():
        ChrJumpTo(0x00FE, -408840, 0, 18820, 600, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_097A)

    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetPos(0x0012, -400080, 0, 20260, 0)
    ChrSetChipByIndex(0x000A, 27)
    OP_99(0x000A, 0x00, 0x04, 1000)
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000A, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(100)

    OP_99(0x000A, 0x04, 0x00, 1000)
    Sleep(700)

    CreateThread(0x000F, 0x00, 0x00, func_0A_225A)
    OP_7C(100, 100, 3000, 400)
    Sleep(50)

    CreateThread(0x000D, 0x00, 0x00, func_09_2207)
    Sleep(50)

    CreateThread(0x0011, 0x00, 0x00, func_0A_225A)
    Sleep(50)

    CreateThread(0x000C, 0x00, 0x00, func_09_2207)
    Sleep(50)

    CreateThread(0x000E, 0x00, 0x00, func_09_2207)
    CreateThread(0x0010, 0x00, 0x00, func_0A_225A)
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x000A,
        (
            '#0300260251V#196F#6P吉尔，下一个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A8B')
    def lambda_0A8B():
        CameraMove(-401900, 60, 23650, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0A8B)

    @scena.Lambda('lambda_0AA3')
    def lambda_0AA3():
        OP_6C(70000, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0AA3)

    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x000B,
        (
            '#0290260252V#201F#5P交给我吧大哥！',
            TxtCtl.Enter,
        ),
    )

    ChrSetChipByIndex(0x000B, 29)
    OP_99(0x000B, 0x00, 0x03, 1750)
    OP_99(0x000B, 0x00, 0x03, 1750)
    CloseMessageWindow()
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_0B01')
    def lambda_0B01():
        ChrJumpTo(0x00FE, -406840, 740, 26030, 600, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B01)

    Sleep(100)

    ChrSetDirection(0x000B, 205, 0)
    Sleep(100)

    ChrSetDirection(0x000B, 160, 0)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0B41')
    def lambda_0B41():
        CameraMove(-400120, 0, 21590, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0B41)

    @scena.Lambda('lambda_0B59')
    def lambda_0B59():
        OP_6C(90000, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0B59)

    ChrSetChipByIndex(0x000B, 29)
    ChrSetSubChip(0x000B, 4)
    ChrSetDirection(0x000B, 115, 0)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_0B7F')
    def lambda_0B7F():
        ChrJumpTo(0x00FE, -405050, 210, 24440, 600, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B7F)

    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    ChrSetChipByIndex(0x000B, 30)
    ChrSetSubChip(0x000B, 1)
    ChrSetPos(0x0012, -399630, 0, 20170, 0)
    PlayEffect(0x01, 0x01, 0x000B, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(50)

    ChrSetPos(0x0012, -400940, 0, 21210, 0)
    PlayEffect(0x01, 0x02, 0x000B, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(100)

    ChrSetPos(0x0012, -399060, 0, 18490, 0)
    PlayEffect(0x01, 0x03, 0x000B, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(1300)

    CreateThread(0x000F, 0x00, 0x00, func_0A_225A)
    OP_7C(100, 100, 3000, 200)
    Sleep(50)

    CreateThread(0x0011, 0x00, 0x00, func_0A_225A)
    Sleep(100)

    CreateThread(0x000C, 0x00, 0x00, func_09_2207)
    CreateThread(0x000D, 0x00, 0x00, func_09_2207)
    OP_7C(100, 100, 3000, 200)
    Sleep(100)

    CreateThread(0x0010, 0x00, 0x00, func_0A_225A)
    CreateThread(0x000E, 0x00, 0x00, func_09_2207)
    OP_7C(100, 100, 3000, 200)
    Fade(250)
    ChrSetChipByIndex(0x000B, 28)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0290260253V#201F#6P#3S乔丝特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D38')
    def lambda_0D38():
        CameraMove(-401900, 60, 14630, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0D38)

    @scena.Lambda('lambda_0D50')
    def lambda_0D50():
        OP_6C(112000, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0D50)

    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0090260254V#210F#6PＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(163, 0x00, 0x64)
    ChrSetFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_0D94')
    def lambda_0D94():
        ChrJumpTo(0x00FE, -406430, 320, 13010, 600, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D94)

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        ChrSetDirection(0x00FE, 51, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0DB2)

    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0DCA')
    def lambda_0DCA():
        CameraMove(-398750, 50, 17130, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0DCA)

    @scena.Lambda('lambda_0DE2')
    def lambda_0DE2():
        OP_6C(96000, 600)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0DE2)

    @scena.Lambda('lambda_0DF2')
    def lambda_0DF2():
        ChrJumpTo(0x00FE, -404070, 580, 14610, 600, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0DF2)

    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrClearFlags(0x0009, 0x0004)
    ChrSetChipByIndex(0x0009, 39)
    ChrSetSubChip(0x0009, 0)
    Sleep(200)

    ChrSetChipByIndex(0x0009, 39)
    ChrSetSubChip(0x0009, 1)
    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)
    StopEffect(0x03, 0x00)
    ChrSetPos(0x0012, -401340, 0, 20290, 0)
    PlayEffect(0x01, 0x01, 0x0009, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(50)

    ChrSetPos(0x0012, -399070, 0, 18620, 0)
    PlayEffect(0x01, 0x02, 0x0009, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(100)

    ChrSetPos(0x0012, -399810, 0, 21560, 0)
    PlayEffect(0x01, 0x03, 0x0009, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(350)

    ChrSetChipByIndex(0x0009, 25)
    OP_99(0x0009, 0x00, 0x02, 1000)
    ChrSetPos(0x0012, -401340, 0, 20290, 0)
    PlayEffect(0x02, 0x04, 0x0009, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    WaitEffect(0x04, 0x02)
    StopEffect(0x01, 0x00)
    PlayEffect(0x03, 0xFF, 0x0012, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0009, 0x03, 0x00, func_0D_23ED)
    ChrSetPos(0x0012, -399070, 0, 18620, 0)
    PlayEffect(0x02, 0x05, 0x0009, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    WaitEffect(0x05, 0x02)
    StopEffect(0x02, 0x00)
    PlayEffect(0x03, 0xFF, 0x0012, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0012, -399810, 0, 21560, 0)
    PlayEffect(0x02, 0x06, 0x0009, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)

    @scena.Lambda('lambda_107F')
    def lambda_107F():
        OP_99(0x00FE, 0x02, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_107F)

    WaitEffect(0x06, 0x02)
    StopEffect(0x03, 0x00)
    PlayEffect(0x03, 0xFF, 0x0012, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0090260255V#214F#4P约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10F1')
    def lambda_10F1():
        CameraMove(-392600, 0, 21260, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_10F1)

    @scena.Lambda('lambda_1109')
    def lambda_1109():
        OP_67(0, 3400, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1109)

    @scena.Lambda('lambda_1121')
    def lambda_1121():
        OP_6C(82000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1121)

    @scena.Lambda('lambda_1131')
    def lambda_1131():
        OP_6E(400, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_1131)

    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetPos(0x0008, -392600, 0, 21260, 270)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0008, 42)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)
    WaitForThreadExit(0x0000, 0x0003)
    PlayEffect(0x07, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 255, 100)
    Sleep(500)

    PlaySE(213, 0x00, 0x64)
    OP_99(0x0008, 0x00, 0x07, 2000)
    Sleep(500)

    ChrSetDirection(0x000C, 260, 0)
    ChrSetDirection(0x000D, 260, 0)
    ChrSetDirection(0x000E, 260, 0)
    ChrSetDirection(0x000F, 260, 0)
    ChrSetDirection(0x0010, 260, 0)
    ChrSetDirection(0x0011, 260, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x01F4)

    @scena.Lambda('lambda_1218')
    def lambda_1218():
        CameraMove(-400180, 10, 18460, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_1218)

    @scena.Lambda('lambda_1230')
    def lambda_1230():
        OP_6C(114000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1230)

    @scena.Lambda('lambda_1240')
    def lambda_1240():
        OP_6E(380, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1240)

    ChrSetChipByIndex(0x0008, 40)
    ChrSetSubChip(0x0008, 7)

    @scena.Lambda('lambda_125A')
    def lambda_125A():
        ChrJumpTo(0x00FE, -404610, 0, 19590, 100, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_125A)

    @scena.Lambda('lambda_1278')
    def lambda_1278():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1278)

    WaitForThreadExit(0x0008, 0x0000)
    PlayEffect(0x04, 0x00, 0x000C, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    ChrSetFlags(0x000C, 0x0020)
    ChrSetChipByIndex(0x000C, 36)

    @scena.Lambda('lambda_12CE')
    def lambda_12CE():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12CE)

    @scena.Lambda('lambda_12E9')
    def lambda_12E9():
        OP_9E(0x00FE, 30, 0, 800, 4000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_12E9)

    Sleep(200)

    PlayEffect(0x04, 0x01, 0x0010, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetChipByIndex(0x0010, 32)

    @scena.Lambda('lambda_1347')
    def lambda_1347():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1347)

    @scena.Lambda('lambda_1362')
    def lambda_1362():
        OP_9E(0x00FE, 30, 0, 800, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_1362)

    Sleep(200)

    PlayEffect(0x04, 0x02, 0x000E, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    ChrSetFlags(0x000E, 0x0020)
    ChrSetChipByIndex(0x000E, 36)

    @scena.Lambda('lambda_13C0')
    def lambda_13C0():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_13C0)

    @scena.Lambda('lambda_13DB')
    def lambda_13DB():
        OP_9E(0x00FE, 30, 0, 800, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_13DB)

    Sleep(200)

    PlayEffect(0x04, 0x03, 0x000D, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetChipByIndex(0x000D, 36)

    @scena.Lambda('lambda_1439')
    def lambda_1439():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1439)

    @scena.Lambda('lambda_1454')
    def lambda_1454():
        OP_9E(0x00FE, 30, 0, 800, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1454)

    Sleep(200)

    PlayEffect(0x04, 0x04, 0x0011, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetChipByIndex(0x0011, 32)

    @scena.Lambda('lambda_14B2')
    def lambda_14B2():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_14B2)

    @scena.Lambda('lambda_14CD')
    def lambda_14CD():
        OP_9E(0x00FE, 30, 0, 800, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_14CD)

    Sleep(200)

    PlayEffect(0x04, 0x05, 0x000F, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    ChrSetFlags(0x000F, 0x0020)
    ChrSetChipByIndex(0x000F, 32)

    @scena.Lambda('lambda_152B')
    def lambda_152B():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_152B)

    @scena.Lambda('lambda_1546')
    def lambda_1546():
        OP_9E(0x00FE, 30, 0, 800, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1546)

    WaitEffect(0x05, 0x02)
    PlaySE(155, 0x00, 0x64)
    Sleep(1000)

    PlayEffect(0x07, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0008, -404610, 0, 19590, 270)

    @scena.Lambda('lambda_15B3')
    def lambda_15B3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 100)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_15B3)

    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0020260256V#1035F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x07, 0x0B, 1500)
    ChrSetChipByIndex(0x0008, 41)
    ChrSetSubChip(0x0008, 2)
    ChrSetFlags(0x0008, 0x0002)
    OP_99(0x0008, 0x02, 0x10, 1500)
    ChrSetDirection(0x000B, 124, 0)
    ChrSetDirection(0x000C, 254, 0)
    ChrSetDirection(0x000D, 254, 0)
    ChrSetDirection(0x000E, 254, 0)
    ChrSetDirection(0x000F, 254, 0)
    ChrSetDirection(0x0010, 254, 0)
    ChrSetDirection(0x0011, 254, 0)

    @scena.Lambda('lambda_1672')
    def lambda_1672():
        CameraMove(-400090, 10, 18730, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_1672)

    @scena.Lambda('lambda_168A')
    def lambda_168A():
        OP_6C(100000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_168A)

    @scena.Lambda('lambda_169A')
    def lambda_169A():
        OP_6E(448, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_169A)

    CreateThread(0x000C, 0x00, 0x00, func_0B_22AD)
    Sleep(200)

    CreateThread(0x0010, 0x00, 0x00, func_0C_234D)
    Sleep(200)

    CreateThread(0x000E, 0x00, 0x00, func_0B_22AD)
    Sleep(200)

    CreateThread(0x000D, 0x00, 0x00, func_0B_22AD)
    Sleep(200)

    CreateThread(0x0011, 0x00, 0x00, func_0C_234D)
    Sleep(200)

    CreateThread(0x000F, 0x00, 0x00, func_0C_234D)
    FadeOut(2500, 16777215, -1)
    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)
    Sleep(2000)

    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetChipByIndex(0x000C, 38)
    ChrSetSubChip(0x000C, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0002)
    ChrSetChipByIndex(0x000E, 38)
    ChrSetSubChip(0x000E, 1)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0002)
    ChrSetChipByIndex(0x0010, 38)
    ChrSetSubChip(0x0010, 2)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetChipByIndex(0x0011, 38)
    ChrSetSubChip(0x0011, 2)
    CameraMove(-404970, 0, 18110, 0)
    OP_67(0, 6240, -10000, 0)
    OP_6C(118000, 0)
    OP_6E(368, 0)

    @scena.Lambda('lambda_1794')
    def lambda_1794():
        OP_6E(368, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_1794)

    OP_20(0x00000BB8)
    FadeIn(3000, 16777215)
    ChrSetChipByIndex(0x0009, 19)
    ChrTurnDirection(0x0009, 0x0008, 400)

    @scena.Lambda('lambda_17BE')
    def lambda_17BE():
        ChrWalkTo(0x00FE, -406580, 0, 17800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_17BE)

    ChrSetChipByIndex(0x000B, 21)
    ChrTurnDirection(0x000B, 0x0008, 400)

    @scena.Lambda('lambda_17E5')
    def lambda_17E5():
        ChrWalkTo(0x00FE, -407260, 0, 20320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_17E5)

    ChrSetChipByIndex(0x000A, 20)
    ChrTurnDirection(0x000A, 0x0008, 400)

    @scena.Lambda('lambda_180C')
    def lambda_180C():
        ChrWalkTo(0x00FE, -407410, 0, 19120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_180C)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_182C')
    def lambda_182C():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_182C)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_183F')
    def lambda_183F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_183F)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_1852')
    def lambda_1852():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1852)

    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)
    WaitForThreadExit(0x0000, 0x0003)
    OP_0D()
    PlayBGM(84)

    ChrTalk(
        0x000B,
        (
            '#0290260257V#202F#6P嘿嘿，你的本事\n',
            '还是一样地出色嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 18)
    ChrSetSubChip(0x0008, 0)
    ChrClearFlags(0x0008, 0x0002)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0020260258V#1031F#5P……你们的\n',
            '连携攻击才是相当漂亮。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260259V托你们的福一口气解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090260260V#413F#4P哼、哼……\n',
            '拍马屁也没有什么好处哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090260261V#212F这是第１０只了吧？\n',
            '还要再猎杀多少才行呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020260262V#1033F#5P是啊……\n',
            '我想差不多该猎杀完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260263V#1035F王国军大概也出动了\n',
            '我们就在这里收手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090260264V#210F#4P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300260265V#198F#4P不过这结社\n',
            '还真不知道在想些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300260266V#190F为什么要让那些\n',
            '黑小子的人偶四处游荡啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0290260267V#206F#6P对，就是这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290260268V真正的特务兵余党们\n',
            '到底去哪儿了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020260269V#1035F#5P或许，很有可能是\n',
            '那张纸条上提到的『茶会』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260270V#1031F人形兵器恐怕是用来\n',
            '转移军方的注意力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0290260271V#203F#6P原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290260272V#207F虽然不知道在哪儿搞什么鬼\n',
            '但是总感觉十分可疑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300260273V#198F#4P不过，我们也没有\n',
            '义务要出手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300260274V#197F那个『茶会』\n',
            '也可以不管吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020260275V#1033F#5P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260276V#1035F现在游击士们\n',
            '应该正在搜索那个废坑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260277V就这样交给军方和协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090260278V#210F#4P是啊是啊，留下\n',
            '纸条和设计图就足够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090260279V反正也帮协会\n',
            '处理了人偶。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090260280V#211F之后的事情交给那个\n',
            '少根筋的女人他们就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020260281V#1033F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090260282V#216F#4P哼，哼，什么嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090260283V#215F到现在还在担心以前的同伴？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020260284V#1035F#5P不……\n',
            '他们已经和我无关了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260285V#1031F如果『茶会』开始的话\n',
            '军方的注意力也会集中到那边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260286V这样的机会可不能错过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300260287V#490F#4P哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0290260288V#202F#6P那么～看来有得忙啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    Sleep(1000)

    Sleep(1000)

    PlaySE(13, 0x00, 0x64)
    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x00000010)
    NewScene('ED6_DT21/T4302._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1F4D
@scena.Code('func_03_1F4D')
def func_03_1F4D():
    ChrWalkTo(0x00FE, -376850, 0, 16730, 3000, 0x00)
    ChrWalkTo(0x00FE, -383070, 0, 21460, 3000, 0x00)
    ChrWalkTo(0x00FE, -387860, 0, 21460, 3000, 0x00)
    ChrWalkTo(0x00FE, -394550, 0, 19140, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00000BB8, 0x00)

    Return()

# id: 0x0004 offset: 0x1FB4
@scena.Code('func_04_1FB4')
def func_04_1FB4():
    ChrWalkTo(0x00FE, -377130, 0, 18630, 3000, 0x00)
    ChrWalkTo(0x00FE, -380940, 0, 23350, 3000, 0x00)
    ChrWalkTo(0x00FE, -388710, 0, 23350, 3000, 0x00)
    ChrWalkTo(0x00FE, -395580, 0, 21300, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00000BB8, 0x00)

    Return()

# id: 0x0005 offset: 0x201B
@scena.Code('func_05_201B')
def func_05_201B():
    ChrWalkTo(0x00FE, -377730, 0, 15420, 3000, 0x00)
    ChrWalkTo(0x00FE, -383170, 0, 20900, 3000, 0x00)
    ChrWalkTo(0x00FE, -388520, 0, 20800, 3000, 0x00)
    ChrWalkTo(0x00FE, -398330, 0, 17930, 3000, 0x00)
    ChrWalkTo(0x00FE, -399330, 0, 17930, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00000BB8, 0x00)

    Return()

# id: 0x0006 offset: 0x2096
@scena.Code('func_06_2096')
def func_06_2096():
    ChrWalkTo(0x00FE, -378030, 0, 16440, 3000, 0x00)
    ChrWalkTo(0x00FE, -382670, 0, 21880, 3000, 0x00)
    ChrWalkTo(0x00FE, -387040, 0, 21880, 3000, 0x00)
    ChrWalkTo(0x00FE, -391690, 0, 20050, 3000, 0x00)
    ChrWalkTo(0x00FE, -397170, 0, 19450, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00000BB8, 0x00)

    Return()

# id: 0x0007 offset: 0x2111
@scena.Code('func_07_2111')
def func_07_2111():
    ChrWalkTo(0x00FE, -377070, 0, 17970, 3000, 0x00)
    ChrWalkTo(0x00FE, -382780, 0, 23850, 3000, 0x00)
    ChrWalkTo(0x00FE, -388460, 0, 23850, 3000, 0x00)
    ChrWalkTo(0x00FE, -393240, 0, 21760, 3000, 0x00)
    ChrWalkTo(0x00FE, -397650, 0, 21940, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00000BB8, 0x00)

    Return()

# id: 0x0008 offset: 0x218C
@scena.Code('func_08_218C')
def func_08_218C():
    ChrWalkTo(0x00FE, -377090, 0, 16990, 3000, 0x00)
    ChrWalkTo(0x00FE, -383070, 0, 22840, 3000, 0x00)
    ChrWalkTo(0x00FE, -388850, 0, 22840, 3000, 0x00)
    ChrWalkTo(0x00FE, -396340, 0, 20170, 3000, 0x00)
    ChrWalkTo(0x00FE, -399630, 0, 20170, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)
    OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00000BB8, 0x00)

    Return()

# id: 0x0009 offset: 0x2207
@scena.Code('func_09_2207')
def func_09_2207():
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 36)

    @scena.Lambda('lambda_2217')
    def lambda_2217():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2217)

    @scena.Lambda('lambda_2232')
    def lambda_2232():
        OP_9E(0x00FE, 20, 0, 400, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2232)

    WaitForThreadExit(0x00FE, 0x0001)
    TerminateThread(0x00FE, 0x02)
    ChrSetChipByIndex(0x00FE, 35)
    ChrClearFlags(0x00FE, 0x0020)

    Return()

# id: 0x000A offset: 0x225A
@scena.Code('func_0A_225A')
def func_0A_225A():
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 32)

    @scena.Lambda('lambda_226A')
    def lambda_226A():
        ChrMoveToRelativeAsync(0x00FE, 500, 0, 100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_226A)

    @scena.Lambda('lambda_2285')
    def lambda_2285():
        OP_9E(0x00FE, 20, 0, 400, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2285)

    WaitForThreadExit(0x00FE, 0x0001)
    TerminateThread(0x00FE, 0x02)
    ChrSetChipByIndex(0x00FE, 31)
    ChrClearFlags(0x00FE, 0x0020)

    Return()

# id: 0x000B offset: 0x22AD
@scena.Code('func_0B_22AD')
def func_0B_22AD():
    ChrClearFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 37)

    @scena.Lambda('lambda_22BD')
    def lambda_22BD():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_22BD)

    PlayEffect(0x05, 0xFF, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1200)

    PlayEffect(0x06, 0xFF, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x00FE, 0x0080)
    OP_7C(100, 100, 3000, 400)

    Return()

# id: 0x000C offset: 0x234D
@scena.Code('func_0C_234D')
def func_0C_234D():
    ChrClearFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 33)

    @scena.Lambda('lambda_235D')
    def lambda_235D():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_235D)

    PlayEffect(0x05, 0xFF, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1200)

    PlayEffect(0x06, 0xFF, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x00FE, 0x0080)
    OP_7C(100, 100, 3000, 400)

    Return()

# id: 0x000D offset: 0x23ED
@scena.Code('func_0D_23ED')
def func_0D_23ED():
    CreateThread(0x000F, 0x00, 0x00, func_0A_225A)
    Sleep(50)

    CreateThread(0x0011, 0x00, 0x00, func_0A_225A)
    OP_7C(100, 100, 3000, 200)
    Sleep(100)

    CreateThread(0x000C, 0x00, 0x00, func_09_2207)
    Sleep(50)

    CreateThread(0x000D, 0x00, 0x00, func_09_2207)
    OP_7C(100, 100, 3000, 200)
    Sleep(100)

    CreateThread(0x0010, 0x00, 0x00, func_0A_225A)
    Sleep(50)

    CreateThread(0x000E, 0x00, 0x00, func_09_2207)
    OP_7C(100, 100, 3000, 200)

    Return()

# id: 0x000E offset: 0x2464
@scena.Code('func_0E_2464')
def func_0E_2464():
    OP_7C(200, 200, 3000, 1000)
    Sleep(200)

    OP_7C(200, 200, 3000, 1000)
    Sleep(200)

    OP_7C(200, 200, 3000, 1000)

    Return()

# id: 0x000F offset: 0x24A2
@scena.Code('func_0F_24A2')
def func_0F_24A2():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
