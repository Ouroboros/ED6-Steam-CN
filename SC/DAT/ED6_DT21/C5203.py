import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5203   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5203.x'
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
        ('ED6_DT29/CH13012._CH', 'ED6_DT29/CH13012P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雷电漂浮鱼',
            x                   = 215200,
            z                   = 3000,
            y                   = 742660,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x172
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 102030,
            z           = 0,
            y           = 442060,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0444,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 129440,
            z           = 0,
            y           = 527920,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0440,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 205850,
            z           = -8000,
            y           = 536430,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0441,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 199590,
            z           = -4000,
            y           = 514909,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0444,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 192670,
            z           = 4000,
            y           = 550140,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0440,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 215040,
            z           = 0,
            y           = 625890,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0444,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x21A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 207310,
            y           = 0,
            z           = 725940,
            range       = 221440,
            dword_10    = 0x000007D0,
            dword_14    = 0x000B1FBC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x23A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 309300,
            triggerZ            = 0,
            triggerY            = 524000,
            triggerRange        = 1000,
            actorX              = 309910,
            actorZ              = 0,
            actorY              = 524000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 309300,
            triggerZ            = 0,
            triggerY            = 464000,
            triggerRange        = 1000,
            actorX              = 310000,
            actorZ              = 0,
            actorY              = 464000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 207370,
            triggerZ            = 0,
            triggerY            = 550010,
            triggerRange        = 1000,
            actorX              = 208030,
            actorZ              = 0,
            actorY              = 550010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 220660,
            triggerZ            = 0,
            triggerY            = 550040,
            triggerRange        = 1000,
            actorX              = 220000,
            actorZ              = 0,
            actorY              = 549950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2CA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 6, 0x22FE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E8',
    )

    ChrSetPos(0x0008, 215200, 3000, 742660, 180)
    ChrClearFlags(0x0008, 0x0080)

    def _loc_2E8(): pass

    label('loc_2E8')

    Return()

# id: 0x0001 offset: 0x2E9
@scena.Code('func_01_2E9')
def func_01_2E9():
    Call(0, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 0, 0x2318)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FF',
    )

    OP_6F(0x0009, 0)

    Jump('loc_306')

    def _loc_2FF(): pass

    label('loc_2FF')

    OP_6F(0x0009, 60)

    def _loc_306(): pass

    label('loc_306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 2, 0x231A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_318',
    )

    OP_6F(0x000A, 0)

    Jump('loc_31F')

    def _loc_318(): pass

    label('loc_318')

    OP_6F(0x000A, 60)

    def _loc_31F(): pass

    label('loc_31F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 4, 0x231C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_331',
    )

    OP_6F(0x000B, 0)

    Jump('loc_338')

    def _loc_331(): pass

    label('loc_331')

    OP_6F(0x000B, 60)

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 5, 0x231D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34A',
    )

    OP_6F(0x000C, 0)

    Jump('loc_351')

    def _loc_34A(): pass

    label('loc_34A')

    OP_6F(0x000C, 60)

    def _loc_351(): pass

    label('loc_351')

    Return()

# id: 0x0002 offset: 0x352
@scena.Code('func_02_352')
def func_02_352():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_367',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_352')

    def _loc_367(): pass

    label('loc_367')

    Return()

# id: 0x0003 offset: 0x368
@scena.Code('func_03_368')
def func_03_368():
    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_391'),
        (0x00000003, 'loc_39E'),
        (0x00000004, 'loc_3AB'),
        (0x00000005, 'loc_3B8'),
        (0x00000006, 'loc_3C5'),
        (0x00000007, 'loc_3D2'),
        (0x00000008, 'loc_3DF'),
        (0x0000000A, 'loc_3EC'),
        (-1, 'loc_3F9'),
    )

    def _loc_391(): pass

    label('loc_391')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 13)

    Jump('loc_3F9')

    def _loc_39E(): pass

    label('loc_39E')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)

    Jump('loc_3F9')

    def _loc_3AB(): pass

    label('loc_3AB')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 13)

    Jump('loc_3F9')

    def _loc_3B8(): pass

    label('loc_3B8')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 13)

    Jump('loc_3F9')

    def _loc_3C5(): pass

    label('loc_3C5')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 13)

    Jump('loc_3F9')

    def _loc_3D2(): pass

    label('loc_3D2')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 13)

    Jump('loc_3F9')

    def _loc_3DF(): pass

    label('loc_3DF')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 13)

    Jump('loc_3F9')

    def _loc_3EC(): pass

    label('loc_3EC')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 13)

    Jump('loc_3F9')

    def _loc_3F9(): pass

    label('loc_3F9')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_422'),
        (0x00000003, 'loc_42F'),
        (0x00000004, 'loc_43C'),
        (0x00000005, 'loc_449'),
        (0x00000006, 'loc_456'),
        (0x00000007, 'loc_463'),
        (0x00000008, 'loc_470'),
        (0x0000000A, 'loc_47D'),
        (-1, 'loc_48A'),
    )

    def _loc_422(): pass

    label('loc_422')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 14)

    Jump('loc_48A')

    def _loc_42F(): pass

    label('loc_42F')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 14)

    Jump('loc_48A')

    def _loc_43C(): pass

    label('loc_43C')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 14)

    Jump('loc_48A')

    def _loc_449(): pass

    label('loc_449')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 14)

    Jump('loc_48A')

    def _loc_456(): pass

    label('loc_456')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 14)

    Jump('loc_48A')

    def _loc_463(): pass

    label('loc_463')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 14)

    Jump('loc_48A')

    def _loc_470(): pass

    label('loc_470')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 14)

    Jump('loc_48A')

    def _loc_47D(): pass

    label('loc_47D')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 14)

    Jump('loc_48A')

    def _loc_48A(): pass

    label('loc_48A')

    Return()

# id: 0x0004 offset: 0x48B
@scena.Code('func_04_48B')
def func_04_48B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 6, 0x22FE)),
            Expr.Return,
        ),
        'loc_493',
    )

    Return()

    def _loc_493(): pass

    label('loc_493')

    EventBegin(0x00)
    Fade(500)
    CameraMove(214520, 0, 729820, 0)
    OP_67(0, 4640, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0008, 215200, 3000, 742660, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0020)
    CreateThread(0x0008, 0x00, 0x00, func_02_352)

    @scena.Lambda('lambda_04FF')
    def lambda_04FF():
        ChrMoveTo(0x00FE, 215200, 0, 736660, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_04FF)

    ChrSetPos(0x0101, 214970, 0, 726800, 0)
    ChrSetPos(0x0102, 214100, 0, 725930, 0)
    ChrSetPos(0x00F8, 215230, 0, 724720, 0)
    ChrSetPos(0x00F9, 216260, 0, 725130, 0)

    @scena.Lambda('lambda_055E')
    def lambda_055E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_055E)

    @scena.Lambda('lambda_0579')
    def lambda_0579():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0579)

    @scena.Lambda('lambda_0594')
    def lambda_0594():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0594)

    @scena.Lambda('lambda_05AF')
    def lambda_05AF():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_05AF)

    @scena.Lambda('lambda_05CA')
    def lambda_05CA():
        CameraMove(214520, 0, 734820, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05CA)

    OP_0D()
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
    Sleep(200)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 11)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 12)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x00F8, 13)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 14)
    ChrSetSubChip(0x00F9, 0)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    TerminateThread(0x0008, 0x00)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_069D')
    def lambda_069D():
        OP_99(0x00FE, 0x00, 0x07, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_069D)

    @scena.Lambda('lambda_06AD')
    def lambda_06AD():
        ChrMoveTo(0x00FE, 216200, 0, 726800, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_06AD)

    Sleep(300)

    Battle(0x00000446, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_6E8'),
        (0x00000000, 'loc_6ED'),
        (0x00000002, 'loc_6F4'),
        (-1, 'loc_6FB'),
    )

    def _loc_6E8(): pass

    label('loc_6E8')

    OP_B4(0x00)

    Jump('loc_6FB')

    def _loc_6ED(): pass

    label('loc_6ED')

    Call(0, 0x0005)

    Jump('loc_6FB')

    def _loc_6F4(): pass

    label('loc_6F4')

    Call(0, 0x0006)

    Jump('loc_6FB')

    def _loc_6FB(): pass

    label('loc_6FB')

    Return()

# id: 0x0005 offset: 0x6FC
@scena.Code('func_05_6FC')
def func_05_6FC():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x01)
    ChrSetFlags(0x0008, 0x0080)
    CameraMove(214940, 0, 728800, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 214940, 0, 728800, 0)
    ChrSetPos(0x0001, 214940, 0, 728800, 0)
    ChrSetPos(0x0002, 214940, 0, 728800, 0)
    ChrSetPos(0x0003, 214940, 0, 728800, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    SetScenaFlags(ScenaFlag(0x045F, 6, 0x22FE))
    OP_B2(0x00, 0x00, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x7D3
@scena.Code('func_06_7D3')
def func_06_7D3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x01)
    ChrSetPos(0x0008, 215200, 3000, 742660, 180)
    ChrClearFlags(0x0008, 0x0080)
    CameraMove(214940, 0, 723800, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 214940, 0, 723800, 180)
    ChrSetPos(0x0001, 214940, 0, 723800, 180)
    ChrSetPos(0x0002, 214940, 0, 723800, 180)
    ChrSetPos(0x0003, 214940, 0, 723800, 180)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x8B3
@scena.Code('func_07_8B3')
def func_07_8B3():
    UnlockAchievement(0x02, 0x0116, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 0, 0x2318)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_990',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['英仙神靴'], 1)"),
            Expr.Return,
        ),
        'loc_927',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['英仙神靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0463, 0, 0x2318))

    Jump('loc_98D')

    def _loc_927(): pass

    label('loc_927')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['英仙神靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['英仙神靴']),
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

    def _loc_98D(): pass

    label('loc_98D')

    Jump('loc_9C1')

    def _loc_990(): pass

    label('loc_990')

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
    def _loc_9C1(): pass

    label('loc_9C1')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x9CF
@scena.Code('func_08_9CF')
def func_08_9CF():
    UnlockAchievement(0x02, 0x0117, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 2, 0x231A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AAC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000A, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['狮子王剑'], 1)"),
            Expr.Return,
        ),
        'loc_A43',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['狮子王剑']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0463, 2, 0x231A))

    Jump('loc_AA9')

    def _loc_A43(): pass

    label('loc_A43')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['狮子王剑']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['狮子王剑']),
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

    def _loc_AA9(): pass

    label('loc_AA9')

    Jump('loc_ADD')

    def _loc_AAC(): pass

    label('loc_AAC')

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
    def _loc_ADD(): pass

    label('loc_ADD')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xAEB
@scena.Code('func_09_AEB')
def func_09_AEB():
    UnlockAchievement(0x02, 0x0118, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 4, 0x231C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BC8',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_B5F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0463, 4, 0x231C))

    Jump('loc_BC5')

    def _loc_B5F(): pass

    label('loc_B5F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
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

    def _loc_BC5(): pass

    label('loc_BC5')

    Jump('loc_BF9')

    def _loc_BC8(): pass

    label('loc_BC8')

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
    def _loc_BF9(): pass

    label('loc_BF9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xC07
@scena.Code('func_0A_C07')
def func_0A_C07():
    UnlockAchievement(0x02, 0x0119, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0463, 5, 0x231D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CE4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['风耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_C7B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['风耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0463, 5, 0x231D))

    Jump('loc_CE1')

    def _loc_C7B(): pass

    label('loc_C7B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['风耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['风耀珠']),
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

    def _loc_CE1(): pass

    label('loc_CE1')

    Jump('loc_D15')

    def _loc_CE4(): pass

    label('loc_CE4')

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
    def _loc_D15(): pass

    label('loc_D15')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
