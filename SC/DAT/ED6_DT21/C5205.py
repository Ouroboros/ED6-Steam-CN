import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5205_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5205   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5205.x'
    header.mapIndex       = 1
    header.bgm            = 63
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
        ('ED6_DT29/CH12950._CH', 'ED6_DT29/CH12950P._CP'),
        ('ED6_DT29/CH12951._CH', 'ED6_DT29/CH12951P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT29/CH12960._CH', 'ED6_DT29/CH12960P._CP'),
        ('ED6_DT29/CH12961._CH', 'ED6_DT29/CH12961P._CP'),
        ('ED6_DT29/CH13010._CH', 'ED6_DT29/CH13010P._CP'),
        ('ED6_DT29/CH13011._CH', 'ED6_DT29/CH13011P._CP'),
        ('ED6_DT29/CH12200._CH', 'ED6_DT29/CH12200P._CP'),
        ('ED6_DT29/CH12201._CH', 'ED6_DT29/CH12201P._CP'),
        ('ED6_DT29/CH13020._CH', 'ED6_DT29/CH13020P._CP'),
        ('ED6_DT29/CH13021._CH', 'ED6_DT29/CH13021P._CP'),
        ('ED6_DT29/CH13022._CH', 'ED6_DT29/CH13022P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 25400,
            z                   = 2000,
            y                   = 264500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '灰白神灵',
            x                   = -494240,
            z                   = 1000,
            y                   = 349840,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '地震控制用假人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x182
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -13960,
            z           = 0,
            y           = 232650,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0521,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 23950,
            z           = 0,
            y           = 246580,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x051E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -499610,
            y           = 0,
            z           = 338130,
            range       = -487150,
            dword_10    = 0x000007D0,
            dword_14    = 0x000537DC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x1DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 24790,
            triggerZ            = 0,
            triggerY            = 264470,
            triggerRange        = 1000,
            actorX              = 25400,
            actorZ              = 0,
            actorY              = 264500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 19370,
            triggerZ            = 0,
            triggerY            = 264470,
            triggerRange        = 1000,
            actorX              = 20030,
            actorZ              = 0,
            actorY              = 264500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14260,
            triggerZ            = 0,
            triggerY            = 264510,
            triggerRange        = 1000,
            actorX              = 14880,
            actorZ              = 0,
            actorY              = 264540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9260,
            triggerZ            = 0,
            triggerY            = 264520,
            triggerRange        = 1000,
            actorX              = 9870,
            actorZ              = 0,
            actorY              = 264550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4140,
            triggerZ            = 0,
            triggerY            = 264520,
            triggerRange        = 1000,
            actorX              = 4790,
            actorZ              = 0,
            actorY              = 264500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -960,
            triggerZ            = 0,
            triggerY            = 264510,
            triggerRange        = 1000,
            actorX              = -320,
            actorZ              = 0,
            actorY              = 264540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -6070,
            triggerZ            = 0,
            triggerY            = 264500,
            triggerRange        = 1000,
            actorX              = -5470,
            actorZ              = 0,
            actorY              = 264530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 5, 0x22FD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FF',
    )

    ChrSetPos(0x0009, -493940, 1000, 344240, 180)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0009, 0x0080)

    def _loc_2FF(): pass

    label('loc_2FF')

    Return()

# id: 0x0001 offset: 0x300
@scena.Code('func_01_300')
def func_01_300():
    Call(0, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_32A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x42),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)
    MapSetFlags(0x00100000)
    CreateThread(0x000A, 0x03, 0x00, func_08_9E1)
    PlaySE(133, 0x01, 0x46)

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 2, 0x234A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33C',
    )

    OP_6F(0x0006, 0)

    Jump('loc_343')

    def _loc_33C(): pass

    label('loc_33C')

    OP_6F(0x0006, 60)

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 4, 0x234C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_355',
    )

    OP_6F(0x0007, 0)

    Jump('loc_35C')

    def _loc_355(): pass

    label('loc_355')

    OP_6F(0x0007, 60)

    def _loc_35C(): pass

    label('loc_35C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 5, 0x234D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36E',
    )

    OP_6F(0x0008, 0)

    Jump('loc_375')

    def _loc_36E(): pass

    label('loc_36E')

    OP_6F(0x0008, 60)

    def _loc_375(): pass

    label('loc_375')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 6, 0x234E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_387',
    )

    OP_6F(0x0009, 0)

    Jump('loc_38E')

    def _loc_387(): pass

    label('loc_387')

    OP_6F(0x0009, 60)

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 7, 0x234F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A0',
    )

    OP_6F(0x000A, 0)

    Jump('loc_3A7')

    def _loc_3A0(): pass

    label('loc_3A0')

    OP_6F(0x000A, 60)

    def _loc_3A7(): pass

    label('loc_3A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046A, 0, 0x2350)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_6F(0x000B, 0)

    Jump('loc_3C0')

    def _loc_3B9(): pass

    label('loc_3B9')

    OP_6F(0x000B, 60)

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046A, 1, 0x2351)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D2',
    )

    OP_6F(0x000C, 0)

    Jump('loc_3D9')

    def _loc_3D2(): pass

    label('loc_3D2')

    OP_6F(0x000C, 60)

    def _loc_3D9(): pass

    label('loc_3D9')

    Return()

# id: 0x0002 offset: 0x3DA
@scena.Code('func_02_3DA')
def func_02_3DA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3DA')

    def _loc_3EF(): pass

    label('loc_3EF')

    Return()

# id: 0x0003 offset: 0x3F0
@scena.Code('func_03_3F0')
def func_03_3F0():
    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_419'),
        (0x00000003, 'loc_426'),
        (0x00000004, 'loc_433'),
        (0x00000005, 'loc_440'),
        (0x00000006, 'loc_44D'),
        (0x00000007, 'loc_45A'),
        (0x00000008, 'loc_467'),
        (0x0000000A, 'loc_474'),
        (-1, 'loc_481'),
    )

    def _loc_419(): pass

    label('loc_419')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 15)

    Jump('loc_481')

    def _loc_426(): pass

    label('loc_426')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 15)

    Jump('loc_481')

    def _loc_433(): pass

    label('loc_433')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 15)

    Jump('loc_481')

    def _loc_440(): pass

    label('loc_440')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 15)

    Jump('loc_481')

    def _loc_44D(): pass

    label('loc_44D')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 15)

    Jump('loc_481')

    def _loc_45A(): pass

    label('loc_45A')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 15)

    Jump('loc_481')

    def _loc_467(): pass

    label('loc_467')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 15)

    Jump('loc_481')

    def _loc_474(): pass

    label('loc_474')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 15)

    Jump('loc_481')

    def _loc_481(): pass

    label('loc_481')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_4AA'),
        (0x00000003, 'loc_4B7'),
        (0x00000004, 'loc_4C4'),
        (0x00000005, 'loc_4D1'),
        (0x00000006, 'loc_4DE'),
        (0x00000007, 'loc_4EB'),
        (0x00000008, 'loc_4F8'),
        (0x0000000A, 'loc_505'),
        (-1, 'loc_512'),
    )

    def _loc_4AA(): pass

    label('loc_4AA')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 16)

    Jump('loc_512')

    def _loc_4B7(): pass

    label('loc_4B7')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 16)

    Jump('loc_512')

    def _loc_4C4(): pass

    label('loc_4C4')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 16)

    Jump('loc_512')

    def _loc_4D1(): pass

    label('loc_4D1')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 16)

    Jump('loc_512')

    def _loc_4DE(): pass

    label('loc_4DE')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 16)

    Jump('loc_512')

    def _loc_4EB(): pass

    label('loc_4EB')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 16)

    Jump('loc_512')

    def _loc_4F8(): pass

    label('loc_4F8')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 16)

    Jump('loc_512')

    def _loc_505(): pass

    label('loc_505')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 16)

    Jump('loc_512')

    def _loc_512(): pass

    label('loc_512')

    Return()

# id: 0x0004 offset: 0x513
@scena.Code('func_04_513')
def func_04_513():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 5, 0x22FD)),
            Expr.Return,
        ),
        'loc_51B',
    )

    Return()

    def _loc_51B(): pass

    label('loc_51B')

    EventBegin(0x00)
    Fade(500)
    CameraMove(-495000, 0, 344000, 0)
    OP_67(0, 4640, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0009, -494240, 3000, 349840, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0009, 12)
    ChrSetSubChip(0x0009, 5)
    ChrSetPos(0x0101, -494200, 0, 340900, 0)
    ChrSetPos(0x0102, -495070, 0, 340030, 0)
    ChrSetPos(0x00F8, -493940, 0, 338820, 0)
    ChrSetPos(0x00F9, -492910, 0, 339230, 0)

    @scena.Lambda('lambda_05D9')
    def lambda_05D9():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05D9)

    @scena.Lambda('lambda_05F4')
    def lambda_05F4():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05F4)

    @scena.Lambda('lambda_060F')
    def lambda_060F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_060F)

    @scena.Lambda('lambda_062A')
    def lambda_062A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_062A)

    @scena.Lambda('lambda_0645')
    def lambda_0645():
        CameraMove(-495000, 0, 348000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0645)

    OP_0D()

    @scena.Lambda('lambda_065E')
    def lambda_065E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_065E)

    @scena.Lambda('lambda_0670')
    def lambda_0670():
        ChrMoveTo(0x00FE, -494240, 1000, 349840, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0670)

    CreateThread(0x0009, 0x00, 0x00, func_05_792)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 13)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 14)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x00F8, 15)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 16)
    ChrSetSubChip(0x00F9, 0)
    WaitForThreadExit(0x0009, 0x0000)
    Sleep(400)

    @scena.Lambda('lambda_0739')
    def lambda_0739():
        OP_99(0x00FE, 0x05, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_0739)

    WaitForThreadExit(0x0009, 0x0003)

    @scena.Lambda('lambda_074E')
    def lambda_074E():
        OP_99(0x00FE, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_074E)

    Sleep(500)

    Battle(0x00000523, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_77E'),
        (0x00000000, 'loc_783'),
        (0x00000002, 'loc_78A'),
        (-1, 'loc_791'),
    )

    def _loc_77E(): pass

    label('loc_77E')

    OP_B4(0x00)

    Jump('loc_791')

    def _loc_783(): pass

    label('loc_783')

    Call(0, 0x0006)

    Jump('loc_791')

    def _loc_78A(): pass

    label('loc_78A')

    Call(0, 0x0007)

    Jump('loc_791')

    def _loc_791(): pass

    label('loc_791')

    Return()

# id: 0x0005 offset: 0x792
@scena.Code('func_05_792')
def func_05_792():
    ChrSetDirection(0x00FE, 90, 800)
    ChrSetDirection(0x00FE, 0, 800)
    ChrSetDirection(0x00FE, 270, 800)
    ChrSetDirection(0x00FE, 180, 800)
    ChrSetDirection(0x00FE, 90, 800)
    ChrSetDirection(0x00FE, 0, 800)
    ChrSetDirection(0x00FE, 270, 800)
    ChrSetDirection(0x00FE, 180, 800)
    ChrSetDirection(0x00FE, 90, 800)
    ChrSetDirection(0x00FE, 0, 800)
    ChrSetDirection(0x00FE, 270, 800)
    ChrSetDirection(0x00FE, 180, 800)
    ChrSetDirection(0x00FE, 90, 800)
    ChrSetDirection(0x00FE, 0, 800)
    ChrSetDirection(0x00FE, 270, 800)
    ChrSetDirection(0x00FE, 180, 800)
    ChrSetDirection(0x00FE, 90, 800)
    ChrSetDirection(0x00FE, 0, 800)
    ChrSetDirection(0x00FE, 270, 800)
    ChrSetDirection(0x00FE, 180, 800)

    Return()

# id: 0x0006 offset: 0x81F
@scena.Code('func_06_81F')
def func_06_81F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x01)
    ChrSetFlags(0x0009, 0x0080)
    CameraMove(-494000, 0, 340660, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -494000, 0, 340660, 0)
    ChrSetPos(0x0001, -494000, 0, 340660, 0)
    ChrSetPos(0x0002, -494000, 0, 340660, 0)
    ChrSetPos(0x0003, -494000, 0, 340660, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetSubChip(0x00F7, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    SetScenaFlags(ScenaFlag(0x045F, 5, 0x22FD))
    OP_B2(0x00, 0x00, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x8F6
@scena.Code('func_07_8F6')
def func_07_8F6():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x01)
    ChrSetPos(0x0009, -493940, 3000, 344240, 180)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0009, 0x0080)
    CameraMove(-494000, 0, 336660, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -494000, 0, 336660, 180)
    ChrSetPos(0x0001, -494000, 0, 336660, 180)
    ChrSetPos(0x0002, -494000, 0, 336660, 180)
    ChrSetPos(0x0003, -494000, 0, 336660, 180)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetSubChip(0x00F7, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x9E1
@scena.Code('func_08_9E1')
def func_08_9E1():
    OP_C4(0x00, 0x00000020)
    def _loc_9E7(): pass

    label('loc_9E7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A09',
    )

    OP_7C(60, 60, 1000, 900)
    Sleep(1000)

    Jump('loc_9E7')

    def _loc_A09(): pass

    label('loc_A09')

    Return()

# id: 0x0009 offset: 0xA0A
@scena.Code('func_09_A0A')
def func_09_A0A():
    UnlockAchievement(0x02, 0x0123, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 2, 0x234A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BA2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 3, 0x234B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AEE',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0A61')
    def lambda_0A61():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A61)

    @scena.Lambda('lambda_0A7C')
    def lambda_0A7C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0A7C)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000522, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_AC9'),
        (0x00000002, 'loc_ADB'),
        (0x00000001, 'loc_AEB'),
        (-1, 'loc_AEE'),
    )

    def _loc_AC9(): pass

    label('loc_AC9')

    SetScenaFlags(ScenaFlag(0x0469, 3, 0x234B))
    OP_6F(0x0006, 60)
    Sleep(500)

    Jump('loc_AEE')

    def _loc_ADB(): pass

    label('loc_ADB')

    OP_6F(0x0006, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_AEB(): pass

    label('loc_AEB')

    OP_B4(0x00)

    Return()

    def _loc_AEE(): pass

    label('loc_AEE')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['帕特农神靴'], 1)"),
            Expr.Return,
        ),
        'loc_B3D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['帕特农神靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0469, 2, 0x234A))

    Jump('loc_B9F')

    def _loc_B3D(): pass

    label('loc_B3D')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['帕特农神靴']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['帕特农神靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_B9F(): pass

    label('loc_B9F')

    Jump('loc_BD1')

    def _loc_BA2(): pass

    label('loc_BA2')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_BD1(): pass

    label('loc_BD1')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xBDF
@scena.Code('func_0A_BDF')
def func_0A_BDF():
    UnlockAchievement(0x02, 0x0124, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 4, 0x234C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CBC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_C53',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0469, 4, 0x234C))

    Jump('loc_CB9')

    def _loc_C53(): pass

    label('loc_C53')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_CB9(): pass

    label('loc_CB9')

    Jump('loc_CED')

    def _loc_CBC(): pass

    label('loc_CBC')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_CED(): pass

    label('loc_CED')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0xCFB
@scena.Code('func_0B_CFB')
def func_0B_CFB():
    UnlockAchievement(0x02, 0x0125, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 5, 0x234D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DD8',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_D6F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0469, 5, 0x234D))

    Jump('loc_DD5')

    def _loc_D6F(): pass

    label('loc_D6F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_DD5(): pass

    label('loc_DD5')

    Jump('loc_E09')

    def _loc_DD8(): pass

    label('loc_DD8')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_E09(): pass

    label('loc_E09')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0xE17
@scena.Code('func_0C_E17')
def func_0C_E17():
    UnlockAchievement(0x02, 0x0126, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 6, 0x234E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['土人偶'], 1)"),
            Expr.Return,
        ),
        'loc_E8B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['土人偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0469, 6, 0x234E))

    Jump('loc_EF1')

    def _loc_E8B(): pass

    label('loc_E8B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['土人偶']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['土人偶']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)

    def _loc_EF1(): pass

    label('loc_EF1')

    Jump('loc_F25')

    def _loc_EF4(): pass

    label('loc_EF4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_F25(): pass

    label('loc_F25')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000D offset: 0xF33
@scena.Code('func_0D_F33')
def func_0D_F33():
    UnlockAchievement(0x02, 0x0127, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 7, 0x234F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1010',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000A, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_FA7',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0469, 7, 0x234F))

    Jump('loc_100D')

    def _loc_FA7(): pass

    label('loc_FA7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0)

    def _loc_100D(): pass

    label('loc_100D')

    Jump('loc_1041')

    def _loc_1010(): pass

    label('loc_1010')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1041(): pass

    label('loc_1041')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x104F
@scena.Code('func_0E_104F')
def func_0E_104F():
    UnlockAchievement(0x02, 0x0128, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046A, 0, 0x2350)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_112C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_10C3',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046A, 0, 0x2350))

    Jump('loc_1129')

    def _loc_10C3(): pass

    label('loc_10C3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0)

    def _loc_1129(): pass

    label('loc_1129')

    Jump('loc_115D')

    def _loc_112C(): pass

    label('loc_112C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_115D(): pass

    label('loc_115D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000F offset: 0x116B
@scena.Code('func_0F_116B')
def func_0F_116B():
    UnlockAchievement(0x02, 0x0129, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046A, 1, 0x2351)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1248',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['水耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_11DF',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['水耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046A, 1, 0x2351))

    Jump('loc_1245')

    def _loc_11DF(): pass

    label('loc_11DF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['水耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['水耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000C, 60)
    OP_70(0x000C, 0)

    def _loc_1245(): pass

    label('loc_1245')

    Jump('loc_1279')

    def _loc_1248(): pass

    label('loc_1248')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1279(): pass

    label('loc_1279')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
